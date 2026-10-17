(function () {
  // Menú móvil
  var top = document.getElementById('top');
  var btn = document.getElementById('menu-btn');
  if (btn && top) {
    btn.addEventListener('click', function () {
      var abierto = top.classList.toggle('abierto');
      btn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      btn.textContent = abierto ? 'Cerrar' : 'Menú';
    });
    document.querySelectorAll('#nav a').forEach(function (a) {
      a.addEventListener('click', function () {
        top.classList.remove('abierto');
        btn.setAttribute('aria-expanded', 'false');
        btn.textContent = 'Menú';
      });
    });
  }

  var anio = document.getElementById('anio');
  if (anio) anio.textContent = new Date().getFullYear();

  // Curvas de nivel generadas (marching squares sobre un relieve suave)
  function rng(seed) {
    return function () {
      seed = (seed * 1664525 + 1013904223) >>> 0;
      return seed / 4294967296;
    };
  }

  function relieve(seed, n) {
    var r = rng(seed), cerros = [];
    for (var i = 0; i < n; i++) {
      cerros.push({ x: r(), y: r(), s: 0.08 + r() * 0.22, h: (r() < 0.25 ? -0.6 : 1) * (0.4 + r() * 0.8) });
    }
    return function (x, y) {
      var v = 0;
      for (var i = 0; i < cerros.length; i++) {
        var c = cerros[i], dx = x - c.x, dy = y - c.y;
        v += c.h * Math.exp(-(dx * dx + dy * dy) / (2 * c.s * c.s));
      }
      return v + 0.15 * Math.sin(x * 7.3 + y * 3.1) + 0.1 * Math.sin(y * 9.7 - x * 2.2);
    };
  }

  function segmentos(f, w, h, paso, nivel) {
    var cols = Math.ceil(w / paso) + 1, filas = Math.ceil(h / paso) + 1, g = [], s = [];
    var asp = w / h;
    for (var j = 0; j < filas; j++) {
      g[j] = [];
      for (var i = 0; i < cols; i++) g[j][i] = f((i * paso / w) * asp, j * paso / h);
    }
    function lerp(a, b) { return (nivel - a) / (b - a); }
    for (var y = 0; y < filas - 1; y++) {
      for (var x = 0; x < cols - 1; x++) {
        var a = g[y][x], b = g[y][x + 1], c = g[y + 1][x + 1], d = g[y + 1][x];
        var k = (a > nivel ? 8 : 0) | (b > nivel ? 4 : 0) | (c > nivel ? 2 : 0) | (d > nivel ? 1 : 0);
        if (k === 0 || k === 15) continue;
        var px = x * paso, py = y * paso;
        var T = [px + lerp(a, b) * paso, py], R = [px + paso, py + lerp(b, c) * paso];
        var B = [px + lerp(d, c) * paso, py + paso], L = [px, py + lerp(a, d) * paso];
        var p = {1:[L,B],2:[B,R],3:[L,R],4:[T,R],5:[L,T,B,R],6:[T,B],7:[L,T],8:[L,T],9:[T,B],10:[T,R,L,B],11:[T,R],12:[L,R],13:[B,R],14:[L,B]}[k];
        for (var m = 0; m < p.length; m += 2) s.push(p[m], p[m + 1]);
      }
    }
    return s;
  }

  function curvas(canvas, opts) {
    if (!canvas || !canvas.getContext) return;
    var ctx = canvas.getContext('2d');
    var reducir = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var f = relieve(opts.seed, opts.cerros);
    var dibujado = false;

    function pintar(animar) {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = canvas.clientWidth, h = canvas.clientHeight;
      if (!w || !h) return;
      canvas.width = w * dpr; canvas.height = h * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, w, h);
      var niveles = [];
      for (var n = 0; n < opts.niveles; n++) niveles.push(-0.4 + n * (1.9 / opts.niveles));
      var capas = niveles.map(function (nv) { return segmentos(f, w, h, opts.paso, nv); });

      function trazar(i) {
        var s = capas[i];
        var destacada = i === opts.destacada;
        ctx.strokeStyle = destacada ? 'rgba(233,185,73,.85)' : (i % 5 === 0 ? 'rgba(207,227,215,.55)' : 'rgba(207,227,215,.3)');
        ctx.lineWidth = destacada ? 1.6 : (i % 5 === 0 ? 1.1 : 0.8);
        ctx.beginPath();
        for (var k = 0; k < s.length; k += 2) { ctx.moveTo(s[k][0], s[k][1]); ctx.lineTo(s[k + 1][0], s[k + 1][1]); }
        ctx.stroke();
      }

      if (!animar || reducir) { for (var i = 0; i < capas.length; i++) trazar(i); return; }
      var t0 = null, dur = 1400, hechos = 0;
      function tick(t) {
        if (t0 === null) t0 = t;
        var meta = Math.min(capas.length, Math.ceil(((t - t0) / dur) * capas.length));
        while (hechos < meta) trazar(hechos++);
        if (hechos < capas.length) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }

    pintar(opts.animar && !dibujado);
    dibujado = true;
    var espera;
    window.addEventListener('resize', function () {
      clearTimeout(espera);
      espera = setTimeout(function () { pintar(false); }, 150);
    });
  }

  curvas(document.getElementById('curvas'), { seed: 41, cerros: 9, niveles: 22, paso: 9, destacada: 13, animar: true });

  // Visor de fotos
  var visor = document.getElementById('visor');
  var botones = Array.prototype.slice.call(document.querySelectorAll('.foto-abrir'));
  if (visor && botones.length && typeof visor.showModal === 'function') {
    var vImg = document.getElementById('visor-img');
    var vTxt = document.getElementById('visor-texto');
    var vPos = document.getElementById('visor-pos');
    var actual = 0, origen = null;
    function mostrar(i) {
      actual = (i + botones.length) % botones.length;
      var img = botones[actual].querySelector('img');
      vImg.src = img.getAttribute('data-grande');
      vImg.alt = img.alt;
      vTxt.textContent = img.alt;
      vPos.textContent = (actual + 1) + ' de ' + botones.length;
    }
    botones.forEach(function (b, i) {
      b.addEventListener('click', function () { origen = b; mostrar(i); visor.showModal(); });
    });
    document.getElementById('visor-ant').addEventListener('click', function () { mostrar(actual - 1); });
    document.getElementById('visor-sig').addEventListener('click', function () { mostrar(actual + 1); });
    document.getElementById('visor-cerrar').addEventListener('click', function () { visor.close(); });
    visor.addEventListener('click', function (e) { if (e.target === visor) visor.close(); });
    visor.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') mostrar(actual + 1);
      if (e.key === 'ArrowLeft') mostrar(actual - 1);
    });
    visor.addEventListener('close', function () { if (origen) origen.focus(); });
  }
})();
