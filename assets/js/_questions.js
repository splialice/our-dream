(function () {
  function init() {
    const input = document.getElementById('qa-filter');
    const count = document.getElementById('qa-count');
    const empty = document.getElementById('qa-empty');
    const chips = document.getElementById('qa-chips');
    if (!input || !count || !empty || !chips) return;

    const items = Array.prototype.slice.call(document.querySelectorAll('.qa-item'));
    const groups = Array.prototype.slice.call(document.querySelectorAll('.qa-group'));
    const buttons = Array.prototype.slice.call(chips.querySelectorAll('.qa-chip'));
    let activeGroup = 'all';

    function apply() {
      const q = (input.value || '').trim().toLowerCase();
      let shown = 0;
      items.forEach(function (el) {
        const group = el.closest('.qa-group');
        const groupIndex = group ? group.getAttribute('data-group-index') : '';
        const inGroup = activeGroup === 'all' || groupIndex === activeGroup;
        const hay = (el.getAttribute('data-text') || '').toLowerCase();
        const hit = inGroup && (!q || hay.indexOf(q) !== -1);
        el.hidden = !hit;
        if (!hit && el.open) el.open = false;
        if (hit) shown++;
      });
      groups.forEach(function (g) {
        const n = g.querySelectorAll('.qa-item:not([hidden])').length;
        const badge = g.querySelector('[data-group-count]');
        if (badge) badge.textContent = String(n);
        g.hidden = n === 0;
      });
      empty.hidden = shown !== 0;
      count.textContent = shown + ' / ' + items.length + ' questions';
    }

    input.addEventListener('input', apply);
    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        activeGroup = btn.getAttribute('data-group');
        buttons.forEach(function (b) { b.classList.toggle('is-active', b === btn); });
        apply();
      });
    });
    items.forEach(function (el) {
      el.addEventListener('toggle', function () {
        if (!el.open) return;
        items.forEach(function (other) {
          if (other !== el) other.open = false;
        });
      });
    });
    groups.forEach(function (g) {
      const btn = g.querySelector('.qa-collapse');
      if (!btn) return;
      btn.addEventListener('click', function () {
        const collapsed = g.classList.toggle('is-collapsed');
        btn.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
        btn.setAttribute('aria-label', collapsed ? 'Expand section' : 'Collapse section');
      });
    });
    apply();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  document.addEventListener('pjax:complete', init);
})();
