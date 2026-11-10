(function () {
  function init() {
    const input = document.getElementById('qa-filter');
    const count = document.getElementById('qa-count');
    const empty = document.getElementById('qa-empty');
    if (!input || !count || !empty) return;

    const items = Array.prototype.slice.call(document.querySelectorAll('.qa-item'));
    const groups = Array.prototype.slice.call(document.querySelectorAll('.qa-group'));

    function apply() {
      const q = (input.value || '').trim().toLowerCase();
      let shown = 0;
      items.forEach(function (el) {
        const hay = (el.getAttribute('data-text') || '').toLowerCase();
        const hit = !q || hay.indexOf(q) !== -1;
        el.hidden = !hit;
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
    apply();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  document.addEventListener('pjax:complete', init);
})();
