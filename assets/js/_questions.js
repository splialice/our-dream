(function () {
  function init() {
    const hub = document.querySelector('.qa-hub');
    if (!hub || hub.dataset.qaBound === '1') return;
    const input = hub.querySelector('#qa-filter');
    const chips = hub.querySelector('#qa-chips');
    if (!input || !chips) return;
    hub.dataset.qaBound = '1';
    hub.querySelector('[data-qa-controls]').hidden = false;
    const items = Array.from(hub.querySelectorAll('.qa-item'));
    const groups = Array.from(hub.querySelectorAll('.qa-group'));
    const buttons = Array.from(chips.querySelectorAll('.qa-chip'));
    const count = hub.querySelector('#qa-count');
    const empty = hub.querySelector('#qa-empty');
    const view = hub.querySelector('#qa-view-label');
    const clear = hub.querySelector('.qa-tools [data-qa-reset]');
    let active = 'all';

    function apply() {
      const query = input.value.trim().toLocaleLowerCase();
      let shown = 0;
      items.forEach(function (item) {
        const group = item.closest('.qa-group').dataset.groupIndex;
        const match = (active === 'all' || active === group) && (!query || item.dataset.text.toLocaleLowerCase().includes(query));
        item.hidden = !match;
        if (!match) item.open = false;
        if (match) shown++;
      });
      groups.forEach(function (group) {
        const n = group.querySelectorAll('.qa-item:not([hidden])').length;
        group.hidden = n === 0;
        group.querySelector('[data-group-count]').textContent = n;
      });
      buttons.forEach(function (button) {
        const selected = button.dataset.group === active;
        button.classList.toggle('is-active', selected);
        if (selected) button.setAttribute('aria-current', 'true');
        else button.removeAttribute('aria-current');
      });
      const current = buttons.find(button => button.dataset.group === active);
      view.textContent = query ? 'Search results' : current.querySelector('span').textContent;
      count.textContent = shown + (shown === 1 ? ' answer' : ' answers');
      empty.hidden = shown !== 0;
      clear.hidden = !query && active === 'all';
    }

    input.addEventListener('input', apply);
    buttons.forEach(function (button) {
      button.addEventListener('click', function (event) {
        // Preserve native jump links when JS is unavailable and modified clicks.
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        active = button.dataset.group;
        apply();
      });
    });
    hub.querySelectorAll('[data-qa-reset]').forEach(function (button) {
      button.addEventListener('click', function () {
        input.value = '';
        active = 'all';
        apply();
        input.focus();
      });
    });
    input.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        input.value = '';
        apply();
      }
    });
    // Keep native details semantics. Multiple answers may remain open for comparison.
    apply();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
  document.addEventListener('pjax:complete', init);
  if (window.MutationObserver) {
    new MutationObserver(init).observe(document.querySelector('.site-main') || document.body, { childList: true, subtree: true });
  }
})();
