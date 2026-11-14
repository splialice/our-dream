"""Audit a clean Pixel Dango build and optionally production HTTP responses.
python scripts/check_site.py --build
python scripts/check_site.py --public <build-directory>
python scripts/check_site.py --public <build-directory> --live
Build mode always creates a unique output directory, leaving preview public/ untouched.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote,quote
from datetime import datetime,timezone
import argparse,json,subprocess,uuid,urllib.request,urllib.error,xml.etree.ElementTree as ET
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
DOMAIN='https://pixeldango.com'
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.canon=[];self.desc=[];self.og=[];self.ogdesc=[];self.twdesc=[];self.robots=[];self.alias=False;self.links=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href',''))
        if tag=='meta':
            if a.get('name')=='description':self.desc.append(a.get('content',''))
            if a.get('property')=='og:url':self.og.append(a.get('content',''))
            if a.get('property')=='og:description':self.ogdesc.append(a.get('content',''))
            if a.get('name')=='twitter:description':self.twdesc.append(a.get('content',''))
            if a.get('name')=='robots':self.robots.append(a.get('content',''))
            if a.get('http-equiv','').lower()=='refresh':self.alias=True
        if tag=='a' and a.get('href'):self.links.append(a['href'])
def audit(base):
    errors=[];pages={};aliases=[];descriptions=defaultdict(list)
    for f in base.rglob('*.html'):
        if not f.is_file():continue
        rel=f.relative_to(base).as_posix();path='/'+(rel[:-10] if rel.endswith('index.html') else rel)
        p=Page(f.read_text(encoding='utf-8'));pages[path]=p
        if p.alias:aliases.append(path);continue
        if path=='/404.html':
            if not any('noindex' in r for r in p.robots):errors.append('404 should be noindex')
            continue
        if len(p.canon)!=1 or unquote(p.canon[0])!=DOMAIN+unquote(path):errors.append(f'nonself/duplicate canonical: {path}: {p.canon}')
        if len(p.og)!=1 or unquote(p.og[0])!=DOMAIN+unquote(path):errors.append(f'OpenGraph URL mismatch: {path}: {p.og}')
        if len(p.desc)!=1 or not p.desc[0].strip():errors.append(f'description missing/duplicate: {path}')
        else:
            descriptions[p.desc[0]].append(path)
            if p.ogdesc!=p.desc or p.twdesc!=p.desc:errors.append(f'social descriptions differ: {path}')
        if any('noindex' in r for r in p.robots):errors.append(f'unexpected noindex: {path}')
    for desc,urls in descriptions.items():
        if len(urls)>1:errors.append(f'description reused: {urls}')
    if '/404.html' not in pages:errors.append('root 404.html missing: Cloudflare may use SPA fallback')
    locs=[e.text for e in ET.parse(base/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    for u in locs:
        path=unquote(urlsplit(u).path)
        if path not in {unquote(p) for p in pages}:errors.append(f'sitemap target missing: {path}')
    if any(urlsplit(u).path=='/404.html' for u in locs):errors.append('404 must not appear in sitemap')
    snapshot={path:dict(canonical=p.canon,description=p.desc,og=p.og,robots=p.robots,links=p.links,alias=p.alias) for path,p in sorted(pages.items())}
    return dict(time=datetime.now(timezone.utc).isoformat(),public=str(base),html=len(pages),aliases=aliases,sitemap=len(locs),errors=errors,pages=snapshot)
def online(result):
    errors=[];responses=[]
    paths=['/','/page/2/','/this-does-not-exist-xyz123/','/posts/no-such-post-xyz.html/','/tags/appdetails/','/missing-'+uuid.uuid4().hex+'/']
    for path in paths:
        want=200 if path in ['/','/page/2/'] else 404
        try:
            req=urllib.request.Request(DOMAIN+path,headers={'User-Agent':'Mozilla/5.0','Cache-Control':'no-cache'})
            try:r=urllib.request.urlopen(req,timeout=25)
            except urllib.error.HTTPError as e:r=e
            code=r.code;html=r.read().decode('utf-8',errors='replace');p=Page(html)
            row=dict(path=path,status=code,expected=want,final_url=r.geturl(),canonical=p.canon,description=p.desc)
            if code!=want:errors.append(f'{path}: expected HTTP {want}, got {code}')
            if want==200 and path in result['pages']:
                for key,value in [('canonical',p.canon),('description',p.desc),('og',p.og)]:
                    if value!=result['pages'][path][key]:errors.append(f'online {key} differs: {path}')
            responses.append(row)
        except Exception as e:errors.append(f'{path}: {e}')
    return dict(time=datetime.now(timezone.utc).isoformat(),errors=errors,responses=responses)
if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--public',type=Path);ap.add_argument('--build',action='store_true');ap.add_argument('--record',type=Path);ap.add_argument('--live',action='store_true');args=ap.parse_args()
    record=args.record or ROOT/'.seo-check'/uuid.uuid4().hex;record.mkdir(parents=True,exist_ok=True)
    base=args.public
    if args.build:
        base=base or record/'public'
        proc=subprocess.run(['hugo','--source',str(ROOT),'--destination',str(base.resolve()),'--cacheDir',str((record/'cache').resolve()),'--baseURL',DOMAIN+'/','--environment','production','--cleanDestinationDir','--noBuildLock'],capture_output=True,text=True,encoding='utf-8',errors='replace')
        (record/'build.log').write_text(proc.stdout+proc.stderr,encoding='utf-8')
        if proc.returncode:raise SystemExit('Hugo failed; see '+str(record/'build.log'))
    if base is None:ap.error('use --build or specify --public')
    result=audit(base)
    (record/'build.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    if args.live:
        live=online(result);(record/'live.json').write_text(json.dumps(live,ensure_ascii=False,indent=2),encoding='utf-8');result['errors']+=live['errors']
    print(json.dumps({k:v for k,v in result.items() if k!='pages'},ensure_ascii=True,indent=2))
    raise SystemExit(bool(result['errors']))
