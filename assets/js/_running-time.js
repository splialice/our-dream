// ===== 页脚运行时间功能 =====

let runningTimeInterval = null;

// 初始化运行时间显示
function initRunningTime() {
  const container = document.querySelector('.footer-running-time');
  if (!container) return;
  
  const startDateStr = container.dataset.startDate;
  if (!startDateStr) return;
  
  // 按本地时区的当天 00:00 解析，避免 new Date("YYYY-MM-DD") 被当作 UTC 午夜，
  // 导致 UTC+8 等东八区访问者的小时数偏 8 小时。
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(startDateStr.trim());
  if (!match) return;
  const startDate = new Date(Number(match[1]), Number(match[2]) - 1, Number(match[3]));
  if (isNaN(startDate.getTime())) {
    return;
  }
  
  // 更新显示函数
  function updateRunningTime() {
    const now = new Date();
    const diff = now - startDate;
    
    // 计算时间差
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((diff % (1000 * 60)) / 1000);
    
    // 更新显示
    const timeEl = container.querySelector('.running-time-value');
    if (timeEl) {
      timeEl.innerHTML = `<span class="time-unit">${days}</span>d <span class="time-unit">${hours}</span>h <span class="time-unit">${minutes}</span>m <span class="time-unit">${seconds}</span>s`;
    }
  }
  
  // 立即更新一次
  updateRunningTime();
  
  // 每秒更新
  runningTimeInterval = setInterval(updateRunningTime, 1000);
}

// 清理运行时间计时器
function cleanupRunningTime() {
  if (runningTimeInterval) {
    clearInterval(runningTimeInterval);
    runningTimeInterval = null;
  }
}

// 导出到全局（供PJAX使用）
window.initRunningTime = initRunningTime;
window.cleanupRunningTime = cleanupRunningTime;

// 页面加载时初始化
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initRunningTime);
} else {
  initRunningTime();
}

