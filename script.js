function toggleNav(){
  const nav = document.getElementById('nav');
  nav.style.display = nav.style.display === 'block' ? '' : 'block';
}
function animateCounters(){
  const counters = document.querySelectorAll('.kpi-number');
  counters.forEach(c=>{
    const target = +c.dataset.count;
    const duration = 1200;
    const start = performance.now();
    function tick(now){
      const p = Math.min(1,(now-start)/duration);
      c.textContent = Math.floor(target * p).toLocaleString('es-CO');
      if(p<1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });
}
window.addEventListener('load', ()=>{
  const y = document.getElementById('year');
  if(y) y.textContent = new Date().getFullYear();
  animateCounters();
});