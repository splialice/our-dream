---
title: "When git push succeeds and nothing ships"
date: 2026-11-08T19:30:00+08:00
lastmod: 2026-11-08T19:30:00+08:00
draft: false
author: "Pixel Dango"
description: "A Cloudflare Pages build died five seconds after a clean git clone. The publish job still reported nine successes. None of the nine articles were live."
categories: ["Site building"]
tags: ["Hugo", "Cloudflare Pages", "CI", "Deployment", "Postmortem"]
cover: "/img/covers/cf-outage-504.png"
---

At 10:02:50 UTC on 2026-11-08, the Cloudflare Pages build log recorded a clean git clone. The repository had pulled revision `8403a74` with the commit message `publish: vietnam-pot-poker-la-gi.md`. The webhook had fired on schedule, Cloudflare had accepted the trigger, and the source tree was sitting in the container.

Five seconds later, at 10:02:55 UTC, the container exited with code 1. Hugo itself never ran. Not one page was generated. The failure happened in the narrow slice of execution between the git clone completing and the build command starting.

```text
Detected the following tools from environment: hugo@extended_0.167.0
Installing hugo extended_0.167.0
* Downloading hugo release extended_0.167.0...
curl: (22) The requested URL returned error: 504
asdf-hugo: Could not download https://github.com/gohugoio/hugo/releases/download/v0.167.0/hugo_extended_0.167.0_Linux-64bit.tar.gz
CFPAGESLOG:ASDF_RETRY: hugo extended_0.167.0 not found in image, updating plugin and retrying...
mkdir: cannot create directory '/opt/buildhome/.asdf/downloads/hugo/extended_0.167.0': File exists
curl: (22) The requested URL returned error: 504
Error: Exit with error code: 1
```

Two distinct mechanics are visible in that block. First, Cloudflare's default build environment does not include a pre-cached binary for Hugo 0.167.0 extended. Instead, the runner relies on `asdf` to fetch the archive directly from GitHub Releases during the build initialization. Second, the retry logic inside the build script is defective under network errors: the first download attempt created the destination folder before failing, so the retry aborted immediately with `mkdir: cannot create directory ... File exists` before even making a meaningful second attempt.

The deployment stopped there, silently.

## The gap between pipeline status and live reality

I run about 10 Hugo sites deployed on Cloudflare Pages. Every day at 18:00 Beijing time (10:00 UTC), a scheduled cron script moves reviewed drafts into the content tree, commits them, and pushes them to GitHub. 

When the local runner finished its execution loop today, the terminal output summarized the run as `9 succeeded, 1 failed`. 

A casual glance at that summary suggests that 9 sites received their updates and 1 site encountered an issue. That is not what happened. The runner evaluated success by the exit code of `git push`. Transferring commits to a remote git server is an isolated transport operation. It says nothing about whether the receiver's post-receive hooks succeeded, whether Cloudflare started a build, or whether the build output reached the edge network.

| Component | Reported Status | Actual State |
| :--- | :--- | :--- |
| Local automation script | 9 succeeded | Only raw git transport succeeded |
| Remote repository | Up to date (`8403a74`) | Commit present, no build output generated |
| Cloudflare Pages | Build failed (code 1) | Execution halted before Hugo invoked |
| Production URLs | No deployment | Returned HTTP 404 |

I checked 6 of the articles across the domains. To avoid false negatives caused by file slug assumptions, I did not derive the test paths from filenames. I extracted the exact paths directly from the `url` front matter parameter inside each markdown file and requested them using `curl -I`.

All 6 returned HTTP 404. 

To confirm that the edge routing itself was operational, I requested the articles published the previous day on the exact same domains. Every previous article returned HTTP 200. The content published on 2026-11-08 did not exist on the web, despite the automation pipeline claiming a 90 percent success rate.

## Two incorrect diagnoses

When a build fails unexpectedly, it is easy to assign blame to the nearest constraint. I made two incorrect assumptions during the first twenty minutes of investigation.

My first guess was that the account had hit the monthly build quota. The free tier of Cloudflare Pages allows 500 builds per month. With 10 active projects rebuilding daily, plus occasional staging previews, exhausting the quota is mathematically plausible toward the end of a cycle. 

This hypothesis was wrong because it failed to account for the execution sequence in the log. If an account is blocked by a platform build quota, the platform rejects the trigger before assigning build compute. A quota rejection halts the job at the scheduling layer; it does not provision a container, mount an environment, clone a repository over SSH, and then attempt to install a toolchain. 

My second guess was that the build environment had dropped support for Hugo 0.167.0, or that my configuration was missing a cache directive, forcing a raw download where none was needed previously. I assumed the download itself was the anomaly.

This hypothesis was refuted immediately by looking at recent history. The configuration across all 10 sites had pinned Hugo version 0.167.0 for an entire month. Every single build during that period had run without this error. If the build container downloads the release archive at runtime on every single execution, then it had downloaded that archive successfully on every prior build across October and early November. The runtime environment had not changed, the build definition had not changed, and the Hugo release archive URL had not changed. The only dynamic variable was the availability of GitHub Releases.

## Asymmetric availability

The root problem was an upstream failure at GitHub, but it appeared in a specific, asymmetric way.

At 10:36 UTC, GitHub posted an incident to their status dashboard titled "Increase in timeouts for some unauthenticated users". They followed with progress updates at 11:16, 11:20, and 11:50 UTC, before declaring the API degradation mitigated at 11:56 UTC. 

My build failed at 10:02:55 UTC. The build died 34 minutes before GitHub posted their first acknowledgment to the public status page. Monitoring services from third parties recorded widespread 504 gateway timeouts across GitHub Actions, Git operations, Issues, and Pages, with repository content download error rates climbing above 50 percent during that window.

The specific failure mode is what made the pipeline fail silently. The daily automation script pushes to GitHub over HTTPS with credentials. Authenticated requests were routed through infrastructure that remained largely operational. The automated commits landed cleanly on GitHub without throwing an error.

Cloudflare Pages, however, initiates its build tasks in ephemeral environments. When `asdf-hugo` runs inside that container, it executes a raw, unauthenticated `curl` call against the public GitHub Releases download endpoint. GitHub was timing out unauthenticated content requests while processing authenticated git traffic.

When a pipeline relies on authenticated interactions for step A and unauthenticated public requests for step B, it does not achieve the reliability of the stronger link. It inherits the failure modes of both. A green checkmark on the push was entirely compatible with an immediate collapse during the build.

A similar operational breakdown occurred a few days earlier. On 2026-11-04, GitHub recorded an incident titled "Incident with Actions and Pages" running from 15:49 to 16:48 UTC, and again from 17:20 to 17:55 UTC. During that incident, Pages deployments dropped to roughly 4 percent of standard volume, and webhook delivery success collapsed to approximately 58 percent, caused by an internal configuration update to an event routing service. Upstream developer platforms operate under high continuous deployment frequencies; transient disruptions in auxiliary features like public binary downloads are recurring realities rather than isolated oddities.

## Recovery and verification

No configuration change was required to fix the builds. The required action was waiting for GitHub to finish mitigating the gateway timeouts on their release storage routing, then kicking the deployment engines again.

Roughly two hours after the failed build, I re-triggered the 6 failed deployments. For one repository, I added a minor change to the `.gitignore` file and pushed a functional commit. For the remaining 5 repositories, I generated empty git commits to force Cloudflare to initiate fresh builds:

```bash
git commit --allow-empty -m "retrigger build after github releases 504 outage"
git push origin main
```

Leaving empty commits in a project's history without context creates confusion for anyone auditing logs later. Including an explicit message stating that the commit exists purely to retrigger a failed build ensures that future inspections do not treat the empty commit hash as an unexplained automation error.

Roughly 100 seconds after pushing the commits, Cloudflare Pages finished building all 6 sites. 

I did not rely on the Cloudflare dashboard indicators showing green status badges. I queried the production endpoints using `curl` and checked the HTTP response headers along with the document title tag:

```bash
curl -sL https://example.com/target-article/ | grep -i "<title>"
```

The server returned HTTP 200, and the output confirmed that the HTML payload contained the updated title strings from the new articles, rather than an older cached snapshot or an error page served with a generic response header.

## The false economy of toolchain optimization

Seeing a toolchain download fail in CI often provokes an engineering impulse to eliminate the download entirely. The reasoning seems clear: if downloading Hugo 0.167.0 during every build introduces an external network failure point, we should eliminate it to speed up the builds and increase resilience.

The numbers do not justify the work.

I timed the local build execution for these sites using the same Hugo 0.167.0 extended binary on an ordinary workstation. Across the 6 repositories, the raw generation time ranged from 0.75 seconds to 1.9 seconds per site. On Cloudflare Pages, the entire execution phase, including container creation, environment setup, and toolchain installation, takes approximately 5 seconds before the build assets are transferred. The asset upload phase to Cloudflare's edge storage consumes the vast majority of the overall deployment cycle.

Eliminating the runtime `curl` fetch of the Hugo archive by maintaining a custom Docker image or checking the binary into version control would shave roughly 2 seconds off a deployment. In the context of a static site deployment, saving 2 seconds on a job that runs once per day is irrelevant.

The actual operational cost was not the 2 seconds spent downloading Hugo. The cost was the 2 hours during which the pipeline asserted that everything had been published while the actual sites were serving 404 errors to readers. 

Optimizing build durations when they are already under 30 seconds produces no meaningful business value. The critical defect in the pipeline was an architectural blind spot: trusting intermediate transport status as proof of end-to-end delivery. A deployment pipeline that does not actively verify the availability of the resulting public assets is simply assuming success in the dark.