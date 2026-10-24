/* Metabosques — sonido de fondo generado en el navegador (Web Audio, sin archivos).
   Inspirado en el tratamiento de orano.group/experience: un ambiente en bucle que cambia con la escena,
   un efecto corto cuando la figura se rearma y un control con una onda animada.
   Cada especie tiene su acorde y su capa de naturaleza. Arranca apagado: el navegador solo permite
   sonido después de un clic, y la preferencia se recuerda en este navegador. */
(function () {
  var AC = window.AudioContext || window.webkitAudioContext;
  var btn = document.getElementById('sonido');
  if (!btn) return;
  if (!AC) { btn.hidden = true; return; }

  var raiz = document.documentElement;
  var lienzo = btn.querySelector('canvas');
  var etiqueta = btn.querySelector('span');

  // Acordes en Hz (tonalidades vecinas para que los cambios se fundan)
  var ACORDES = {
    ceiba:      [146.83, 220.00, 329.63, 369.99],
    colibri:    [196.00, 293.66, 440.00, 493.88],
    palma:      [164.81, 246.94, 293.66, 392.00],
    fragmentos: [146.83, 220.00, 293.66, 220.00],
    jaguar:     [123.47, 185.00, 293.66, 440.00],
    morpho:     [293.66, 369.99, 440.00, 554.37]
  };
  var AMBIENTE = {
    ceiba:      { viento: 0.10, capa: 'aves',     ritmo: [2.2, 5.5] },
    colibri:    { viento: 0.05, capa: 'colibri',  ritmo: [1.4, 3.2] },
    palma:      { viento: 0.24, capa: 'aves',     ritmo: [5, 10] },
    fragmentos: { viento: 0.06, capa: null,       ritmo: [4, 8] },
    jaguar:     { viento: 0.07, capa: 'grillos',  ritmo: [0.5, 1.4] },
    morpho:     { viento: 0.05, capa: 'campanas', ritmo: [1.6, 3.8] }
  };

  var ctx, master, efectos, reverb, filtroPad, gainPad, filtroViento, gainViento, ruido;
  var osciladores = [];
  var activo = false, escena = raiz.getAttribute('data-escena') || 'ceiba', temporizador = null, suspender = null;

  function azar(a, b) { return a + Math.random() * (b - a); }

  function impulso(seg) {
    var n = Math.floor(ctx.sampleRate * seg), b = ctx.createBuffer(2, n, ctx.sampleRate);
    for (var c = 0; c < 2; c++) {
      var d = b.getChannelData(c);
      for (var i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / n, 2.6);
    }
    return b;
  }

  function montar() {
    ctx = new AC();
    var comp = ctx.createDynamicsCompressor();
    comp.connect(ctx.destination);
    master = ctx.createGain(); master.gain.value = 0; master.connect(comp);

    reverb = ctx.createConvolver(); reverb.buffer = impulso(3.2);
    var gReverb = ctx.createGain(); gReverb.gain.value = 0.55;
    reverb.connect(gReverb); gReverb.connect(master);

    efectos = ctx.createGain(); efectos.gain.value = 1;
    efectos.connect(master); efectos.connect(reverb);

    // Pad: cuatro voces suaves con filtro que respira
    filtroPad = ctx.createBiquadFilter(); filtroPad.type = 'lowpass'; filtroPad.frequency.value = 900; filtroPad.Q.value = 0.4;
    gainPad = ctx.createGain(); gainPad.gain.value = 0.05;
    filtroPad.connect(gainPad); gainPad.connect(master); gainPad.connect(reverb);
    var lfo = ctx.createOscillator(), lfoG = ctx.createGain();
    lfo.frequency.value = 0.05; lfoG.gain.value = 300; lfo.connect(lfoG); lfoG.connect(filtroPad.frequency); lfo.start();
    ACORDES[escena].forEach(function (f, i) {
      var o = ctx.createOscillator(), g = ctx.createGain();
      o.type = i % 2 ? 'sine' : 'triangle';
      o.frequency.value = f; o.detune.value = (i - 1.5) * 4;
      g.gain.value = i === 0 ? 0.9 : 0.55;
      o.connect(g); g.connect(filtroPad); o.start();
      osciladores.push(o);
    });

    // Viento: ruido filtrado con movimiento lento
    var n = ctx.sampleRate * 3; ruido = ctx.createBuffer(1, n, ctx.sampleRate);
    var d = ruido.getChannelData(0);
    for (var i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
    var fuente = ctx.createBufferSource(); fuente.buffer = ruido; fuente.loop = true;
    filtroViento = ctx.createBiquadFilter(); filtroViento.type = 'bandpass'; filtroViento.frequency.value = 520; filtroViento.Q.value = 0.7;
    gainViento = ctx.createGain(); gainViento.gain.value = AMBIENTE[escena].viento;
    fuente.connect(filtroViento); filtroViento.connect(gainViento); gainViento.connect(master);
    var lfo2 = ctx.createOscillator(), lfo2G = ctx.createGain();
    lfo2.frequency.value = 0.07; lfo2G.gain.value = 280; lfo2.connect(lfo2G); lfo2G.connect(filtroViento.frequency); lfo2.start();
    fuente.start();
  }

  function panear(nodo, valor) {
    if (!ctx.createStereoPanner) return nodo;
    var p = ctx.createStereoPanner(); p.pan.value = valor; nodo.connect(p); return p;
  }

  function tono(f1, f2, t, dur, vol, tipo, pan) {
    var o = ctx.createOscillator(), g = ctx.createGain();
    o.type = tipo || 'sine';
    o.frequency.setValueAtTime(f1, t);
    if (f2) o.frequency.exponentialRampToValueAtTime(f2, t + dur * 0.7);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(vol, t + Math.min(0.012, dur / 4));
    g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.connect(g); panear(g, pan || 0).connect(efectos);
    o.start(t); o.stop(t + dur + 0.05);
  }

  var CAPAS = {
    aves: function () {
      var t = ctx.currentTime + 0.05, base = azar(2100, 3600), pan = azar(-0.8, 0.8), n = 2 + Math.floor(Math.random() * 4);
      for (var i = 0; i < n; i++) { tono(base, base * azar(1.25, 1.7), t, azar(0.07, 0.12), 0.035, 'sine', pan); t += azar(0.12, 0.2); }
    },
    colibri: function () {
      var t = ctx.currentTime + 0.05, pan = azar(-0.6, 0.6), n = 4 + Math.floor(Math.random() * 5);
      for (var i = 0; i < n; i++) { tono(azar(5200, 6400), null, t, 0.03, 0.022, 'sine', pan); t += azar(0.05, 0.08); }
    },
    grillos: function () {
      var t = ctx.currentTime + 0.05, f = azar(4300, 4900), pan = azar(-0.9, 0.9);
      for (var i = 0; i < 3; i++) { tono(f, null, t, 0.018, 0.014, 'sine', pan); t += 0.035; }
    },
    campanas: function () {
      var notas = [587.33, 659.25, 739.99, 880, 987.77], f = notas[Math.floor(Math.random() * notas.length)];
      var t = ctx.currentTime + 0.05, pan = azar(-0.5, 0.5);
      tono(f, null, t, 2.6, 0.03, 'sine', pan);
      tono(f * 2.76, null, t, 1.2, 0.008, 'sine', pan);
    }
  };

  function programar() {
    clearTimeout(temporizador);
    if (!activo) return;
    var a = AMBIENTE[escena] || AMBIENTE.ceiba;
    temporizador = setTimeout(function () {
      if (activo && a.capa && document.visibilityState === 'visible') CAPAS[a.capa]();
      programar();
    }, azar(a.ritmo[0], a.ritmo[1]) * 1000);
  }

  // Barrido que acompaña el rearmado de las piezas (dura lo mismo que la transición)
  function barrido() {
    if (!activo) return;
    var t = ctx.currentTime, s = ctx.createBufferSource(), f = ctx.createBiquadFilter(), g = ctx.createGain();
    s.buffer = ruido; f.type = 'bandpass'; f.Q.value = 1.1;
    f.frequency.setValueAtTime(320, t);
    f.frequency.exponentialRampToValueAtTime(2400, t + 0.55);
    f.frequency.exponentialRampToValueAtTime(600, t + 1.25);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(0.09, t + 0.45);
    g.gain.exponentialRampToValueAtTime(0.0001, t + 1.3);
    s.connect(f); f.connect(g); g.connect(efectos);
    s.start(t, Math.random() * 1.5); s.stop(t + 1.4);
  }

  function cambiarEscena(nueva) {
    if (!ACORDES[nueva] || nueva === escena) return;
    escena = nueva;
    if (!ctx) return;
    var t = ctx.currentTime;
    ACORDES[nueva].forEach(function (f, i) { osciladores[i].frequency.setTargetAtTime(f, t, 0.7); });
    gainViento.gain.setTargetAtTime(AMBIENTE[nueva].viento, t, 1.2);
    gainPad.gain.setTargetAtTime(nueva === 'fragmentos' ? 0.03 : 0.05, t, 1);
    barrido();
    programar();
  }

  function guardar(v) { try { localStorage.setItem('metabosques-sonido', v ? '1' : '0'); } catch (e) {} }
  function leer() { try { return localStorage.getItem('metabosques-sonido') === '1'; } catch (e) { return false; } }

  function encender() {
    if (!ctx) montar();
    clearTimeout(suspender);
    ctx.resume();
    activo = true;
    master.gain.cancelScheduledValues(ctx.currentTime);
    master.gain.setTargetAtTime(0.85, ctx.currentTime, 0.8);
    programar();
    pintarEstado();
  }
  function apagar() {
    activo = false;
    clearTimeout(temporizador);
    if (ctx) {
      master.gain.cancelScheduledValues(ctx.currentTime);
      master.gain.setTargetAtTime(0, ctx.currentTime, 0.25);
      suspender = setTimeout(function () { if (!activo) ctx.suspend(); }, 1500);
    }
    pintarEstado();
  }
  function pintarEstado() {
    btn.setAttribute('aria-pressed', activo ? 'true' : 'false');
    btn.setAttribute('aria-label', activo ? 'Silenciar sonido de fondo' : 'Activar sonido de fondo');
    if (etiqueta) etiqueta.textContent = activo ? 'Sonido activado' : 'Activar sonido';
    animarOnda();
  }

  btn.addEventListener('click', function () {
    if (activo) { apagar(); guardar(false); } else { encender(); guardar(true); }
  });

  // Quien lo dejó encendido en una visita anterior lo recupera con su primer clic o tecla
  if (leer()) {
    var primerGesto = function (e) {
      if (e.target && e.target.closest && e.target.closest('#sonido')) return;
      window.removeEventListener('pointerdown', primerGesto, true);
      window.removeEventListener('keydown', primerGesto, true);
      if (!activo) encender();
    };
    window.addEventListener('pointerdown', primerGesto, true);
    window.addEventListener('keydown', primerGesto, true);
  }

  // Escena: el script de la figura cambia data-escena en <html>
  new MutationObserver(function () { cambiarEscena(raiz.getAttribute('data-escena')); })
    .observe(raiz, { attributes: true, attributeFilter: ['data-escena'] });

  // Clic en la figura: barrido y un golpe suave de madera
  var figura = document.getElementById('figura');
  if (figura) figura.addEventListener('click', function () {
    if (!activo) return;
    tono(880, 320, ctx.currentTime + 0.01, 0.09, 0.06, 'sine', 0);
    barrido();
  });

  document.addEventListener('visibilitychange', function () {
    if (!ctx || !activo) return;
    if (document.visibilityState === 'hidden') ctx.suspend(); else ctx.resume();
  });

  // ---------- Onda del botón ----------
  var reducir = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var amp = 0, fase = 0, cuadro = null;
  function dibujar() {
    if (!lienzo) return false;
    var dpr = Math.min(window.devicePixelRatio || 1, 2), w = 28, h = 16;
    if (lienzo.width !== w * dpr) { lienzo.width = w * dpr; lienzo.height = h * dpr; }
    var c = lienzo.getContext('2d');
    c.setTransform(dpr, 0, 0, dpr, 0, 0);
    c.clearRect(0, 0, w, h);
    c.strokeStyle = getComputedStyle(btn).color; c.lineWidth = 1.6; c.lineCap = 'round';
    c.beginPath();
    for (var x = 0; x <= w; x++) {
      var env = Math.sin(Math.PI * x / w);
      var y = h / 2 + Math.sin(x / w * Math.PI * 4 + fase) * (h / 2 - 2) * amp * env;
      if (x === 0) c.moveTo(x, y); else c.lineTo(x, y);
    }
    c.stroke();
    var meta = activo ? 1 : 0.1;
    amp += (meta - amp) * 0.12;
    if (!reducir) fase += 0.18;
    return activo || Math.abs(meta - amp) > 0.01;
  }
  function animarOnda() {
    if (reducir) { amp = activo ? 0.8 : 0.1; dibujar(); return; }
    if (cuadro) return;
    (function paso() {
      cuadro = dibujar() ? requestAnimationFrame(paso) : null;
    })();
  }
  amp = 0.1; dibujar();
})();
