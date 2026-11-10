(function () {
  function init() {
    const input = document.getElementById('qa-filter');
    const count = document.getElementById('qa-count');
    const empty = document.getElementById('qa-empty');
    const chips = document.getElementById('qa-chips');
    if (!input || !count || !empty || !chips) return;
    // 已经绑过就跳过，防止同一个输入框被反复挂监听
    if (input.dataset.qaBound === '1') return;
    input.dataset.qaBound = '1';

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

    // 同一条目展开时收起其它条目，一次只开一个
    items.forEach(function (el) {
      el.addEventListener('toggle', function () {
        if (!el.open) return;
        items.forEach(function (other) {
          if (other !== el) other.open = false;
        });
      });
    });

    apply();
  }

  function boot() {
    init();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
  document.addEventListener('pjax:complete', boot);

  // 兜底：站内换页不刷新整页，这里盯着主内容区，
  // 任何方式进入本页都能把交互重新挂上
  if (window.MutationObserver) {
    const target = document.querySelector('.site-main') || document.body;
    if (target) {
      const observer = new MutationObserver(function () {
        init();
      });
      observer.observe(target, { childList: true, subtree: true });
    }
  }
})();
