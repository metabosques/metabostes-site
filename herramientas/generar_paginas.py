"""Genera las páginas de servicio, el blog, el pie común, los datos estructurados, el sitemap y llms.txt.

Uso: python3 herramientas/generar_paginas.py   (desde la raíz del repositorio)

- Textos de servicios: herramientas/contenido_servicios.py  -> /<slug>  (archivo <slug>.html en la raíz)
- Guías del blog:      herramientas/contenido_blog.py       -> /blog/<slug> (archivo blog/<slug>.html) y /blog/
- Redes sociales:      herramientas/redes.json (una red vacía no se muestra)
- En index.html se reemplaza lo que hay entre los comentarios <!-- servicios:... -->, <!-- opciones:... -->,
  <!-- faq:... -->, <!-- schema:... --> y <!-- pie:... -->. En las demás páginas fijas, solo el pie.
- Las URL antiguas /servicios/<slug>/ quedan como redirecciones a la URL nueva.
"""
import html, json, os, re, sys, datetime
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "herramientas"))
from contenido_servicios import SERVICIOS, REDIRECCIONES  # noqa: E402
from contenido_blog import GUIAS, AVISO  # noqa: E402

SITIO = "https://metabosques.com"
HOY = datetime.date.today().isoformat()
WA = "573007925238"
TEL = "+57 300 792 5238"
CORREO = "amoreno@metabosques.com"
PRINCIPALES = [s for s in SERVICIOS if s["principal"]]
COMPLEMENTARIOS = [s for s in SERVICIOS if not s["principal"]]
POR_SLUG = {s["slug"]: s for s in SERVICIOS}
GUIA_POR_SLUG = {g["slug"]: g for g in GUIAS}
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

with open(os.path.join(RAIZ, "herramientas", "redes.json"), encoding="utf-8") as f:
    REDES = {k: v.strip() for k, v in json.load(f).items() if v and v.strip()}

ICONOS = {
    "Instagram": '<path d="M12 7.2a4.8 4.8 0 1 0 0 9.6 4.8 4.8 0 0 0 0-9.6Zm0 7.9a3.1 3.1 0 1 1 0-6.2 3.1 3.1 0 0 1 0 6.2Zm5-8.1a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0ZM12 3.6c2.7 0 3 0 4.1.1 2.7.1 4 1.4 4.1 4.1.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c-.1 2.7-1.4 4-4.1 4.1-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-2.7-.1-4-1.4-4.1-4.1C3.7 15 3.6 14.7 3.6 12s0-3 .1-4.1c.1-2.7 1.4-4 4.1-4.1 1.1-.2 1.4-.2 4.2-.2ZM12 2c-2.7 0-3.1 0-4.1.1C4.2 2.2 2.2 4.2 2.1 7.9 2 8.9 2 9.3 2 12s0 3.1.1 4.1c.1 3.7 2.1 5.7 5.8 5.8 1 .1 1.4.1 4.1.1s3.1 0 4.1-.1c3.7-.1 5.7-2.1 5.8-5.8.1-1 .1-1.4.1-4.1s0-3.1-.1-4.1c-.1-3.7-2.1-5.7-5.8-5.8C15.1 2 14.7 2 12 2Z"/>',
    "Facebook": '<path d="M13.5 21.9v-7.7h2.6l.4-3h-3V9.3c0-.9.3-1.5 1.5-1.5h1.6V5.1c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6v7.7C5.6 21.2 2 17 2 12 2 6.5 6.5 2 12 2s10 4.5 10 10c0 5-3.6 9.2-8.5 9.9Z"/>',
    "LinkedIn": '<path d="M20.4 2H3.6C2.7 2 2 2.7 2 3.5v17c0 .8.7 1.5 1.6 1.5h16.8c.9 0 1.6-.7 1.6-1.5v-17c0-.8-.7-1.5-1.6-1.5ZM8 19H5V9.5h3V19ZM6.5 8.2a1.7 1.7 0 1 1 0-3.4 1.7 1.7 0 0 1 0 3.4ZM19 19h-3v-4.6c0-1.1 0-2.5-1.5-2.5S12.8 13 12.8 14.3V19h-3V9.5h2.8v1.3h.1c.4-.7 1.4-1.5 2.8-1.5 3 0 3.6 2 3.6 4.6V19Z"/>',
    "YouTube": '<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.5 2.5 0 0 0-1.8 1.8C2 8.8 2 12 2 12s0 3.2.4 4.8c.2.9.9 1.6 1.8 1.8 1.6.4 7.8.4 7.8.4s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8ZM10 15V9l5.2 3L10 15Z"/>',
}
ICONO_WA = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.2.1-.1 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.1 5.1 0 0 0 1.1 2.7 11.7 11.7 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>'

AREA = [{"@type": "Country", "name": "Colombia"}] + [
    {"@type": "Place", "name": f"Región {r} de Colombia"} for r in ("Caribe", "Andina", "Pacífica", "Orinoquía", "Amazonía")]

FAQ_PORTADA = [
    ("¿En qué regiones de Colombia trabajan?",
     "En todo Colombia. Llevamos el equipo técnico y de campo a cualquier región del país: Caribe, Andina, Pacífico, Orinoquía y Amazonía. Hemos trabajado en franjas costeras, humedales y sabanas. Nuestra sede administrativa está en Medellín."),
    ("¿Qué cambió en las compensaciones por pérdida de biodiversidad en 2026?",
     "En 2026 se actualizó el manual nacional de compensación del medio biótico. Cambiaron los factores por tipo de ecosistema, se agregó un ajuste según dónde se compensa y el plan exige zonificación detallada, análisis de adicionalidad y participación comunitaria. Te ayudamos a calcular el área y a ajustar tu plan."),
    ("¿Ayudan a cumplir la inversión forzosa del 1 %?",
     "Sí. Revisamos la obligación y la liquidación, formulamos el plan de inversión, lo tramitamos ante la autoridad ambiental y lo ejecutamos en la cuenca."),
    ("¿Tramitan permisos de aprovechamiento forestal?",
     "Sí. Hacemos el inventario forestal, el plan de aprovechamiento y la compensación, radicamos la solicitud y acompañamos el trámite hasta la resolución. También ejecutamos la tala y tramitamos los salvoconductos."),
    ("¿Se encargan del mantenimiento y los informes después de la siembra?",
     "Sí. Hacemos el mantenimiento de las áreas establecidas, medimos los indicadores y entregamos los informes de cumplimiento ambiental (ICA) que pide la autoridad."),
    ("¿Qué información necesitan para cotizar un proyecto?",
     "La ubicación del predio, el área aproximada, la autoridad ambiental que lleva el caso y los plazos. Si tienes el acto administrativo con la obligación, compártelo."),
    ("¿Cuánto tardan en responder una solicitud?",
     "Respondemos en un día hábil por correo o WhatsApp."),
]

e = html.escape


def url_servicio(s):
    return f"/{s['slug']}"


def url_guia(g):
    return f"/blog/{g['slug']}"


def fecha_larga(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def wa_link(texto):
    return f"https://wa.me/{WA}?text={quote(texto)}"


# ---------------------------------------------------------------- piezas comunes

def redes_html():
    if not REDES:
        return ""
    items = []
    for nombre, url in REDES.items():
        items.append(
            f'<a href="{e(url)}" target="_blank" rel="noopener me" aria-label="Metabosques en {nombre}">'
            f'<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="currentColor">{ICONOS.get(nombre, "")}</svg>'
            f'<span>{nombre}</span></a>')
    return '\n      <nav class="redes" aria-label="Redes sociales">' + "".join(items) + "</nav>"


def pie_html():
    principales = "".join(f'<a href="{url_servicio(s)}">{e(s["nombre"])}</a>' for s in PRINCIPALES)
    otros = "".join(f'<a href="{url_servicio(s)}">{e(s["nombre"])}</a>' for s in COMPLEMENTARIOS)
    guias = "".join(f'<a href="{url_guia(g)}">{e(g["corto"])}</a>' for g in GUIAS)
    return f"""<!-- pie:inicio -->
  <footer class="pie">
    <div class="pie-bloque">
      <p class="pie-marca">Metabosques S.A.S.</p>
      <p>Servicios ambientales en toda Colombia. Sede administrativa en Medellín.</p>
      <p><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{TEL}</a> · <a href="mailto:{CORREO}">{CORREO}</a></p>{redes_html()}
    </div>
    <nav class="pie-bloque" aria-label="Servicios">
      <p class="pie-titulo">Servicios</p>{principales}{otros}
    </nav>
    <nav class="pie-bloque" aria-label="Guías">
      <p class="pie-titulo"><a href="/blog/">Blog</a></p>{guias}
    </nav>
    <nav class="pie-bloque" aria-label="Más">
      <p class="pie-titulo">Metabosques</p><a href="/#como-trabajamos">Cómo trabajamos</a><a href="/#en-campo">En campo</a><a href="/#preguntas">Preguntas frecuentes</a><a href="/#contacto">Contacto</a><a href="/politica-privacidad.html">Política de privacidad</a>
    </nav>
    <p class="pie-legal">© <span id="anio">2026</span> Metabosques S.A.S.</p>
  </footer>
  <a class="wa" href="{wa_link('Hola Metabosques, quiero información sobre sus servicios.')}" target="_blank" rel="noopener" aria-label="Escribir a Metabosques por WhatsApp">
    <img src="/assets/wa.svg" alt="" width="28" height="28">
  </a>
  <!-- pie:fin -->"""


def negocio(completo=True):
    d = {
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{SITIO}/#negocio",
        "name": "Metabosques S.A.S.",
        "url": f"{SITIO}/",
        "telephone": "+573007925238",
        "email": CORREO,
        "image": f"{SITIO}/assets/og-image.jpg",
        "address": {"@type": "PostalAddress", "addressLocality": "Medellín", "addressRegion": "Antioquia", "addressCountry": "CO"},
    }
    if not completo:
        return d
    d.update({
        "alternateName": "Metabosques",
        "description": "Empresa ambiental colombiana con cobertura en todo el país y sede administrativa en Medellín. Aprovechamiento forestal, compensación por pérdida de biodiversidad, inversión forzosa del 1 %, rescate de flora y fauna, restauración ecológica y seguimiento ambiental.",
        "logo": f"{SITIO}/assets/logo.png",
        "areaServed": AREA,
        "priceRange": "Cotización por proyecto",
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"},
        "contactPoint": {"@type": "ContactPoint", "contactType": "Ventas", "telephone": "+573007925238", "email": CORREO, "availableLanguage": "es", "areaServed": "CO"},
        "knowsAbout": ["Aprovechamiento forestal", "Compensación por pérdida de biodiversidad", "Inversión forzosa del 1 %", "Rescate de flora y fauna", "Restauración ecológica", "Seguimiento ambiental", "Informes de cumplimiento ambiental (ICA)", "Consultoría ambiental"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Servicios ambientales",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@id": f"{SITIO}{url_servicio(s)}#servicio"}} for s in SERVICIOS],
        },
    })
    if REDES:
        d["sameAs"] = list(REDES.values())
    return d


def servicio_ld(s, portada=False):
    return {
        "@type": "Service", "@id": f"{SITIO}{url_servicio(s)}#servicio", "name": s["nombre"], "serviceType": s["tipo"],
        "description": s["resumen"] if portada else s["descripcion"], "url": f"{SITIO}{url_servicio(s)}", "provider": {"@id": f"{SITIO}/#negocio"}, "areaServed": AREA,
    }


def faq_ld(pares, ident):
    return {"@type": "FAQPage", "@id": ident,
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pares]}


def migas_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITIO}{u}"} for i, (n, u) in enumerate(items)]}


def ld(grafo):
    return ('<!-- schema:inicio -->\n  <script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)
            + "\n  </script>\n  <!-- schema:fin -->")


def faq_html(pares, nivel="h3"):
    return "".join(f'<details><summary><{nivel}>{e(q)}</{nivel}></summary><p>{e(a)}</p></details>' for q, a in pares)


def cabeza(title, descripcion, ruta, extra="", tipo_og="website"):
    url = f"{SITIO}{ruta}"
    return f"""<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(title)} | Metabosques</title>
  <meta name="description" content="{e(descripcion)}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0F2A22">
  <link rel="icon" href="/assets/favicon.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">
  <meta property="og:type" content="{tipo_og}">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="Metabosques">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(descripcion)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITIO}/assets/og-image.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles.css">
  {extra}
</head>
<body>
  <a class="skip" href="#contenido">Saltar al contenido</a>
  <header class="top">
    <div class="wrap">
      <a class="marca" href="/" aria-label="Metabosques, inicio">
        <img src="/assets/logo.png" alt="" width="40" height="40">
        <span>Metabosques</span>
      </a>
      <a class="btn btn-cinta" href="/#contacto">Cotizar un proyecto</a>
    </div>
  </header>
"""


def cola():
    return "  " + pie_html() + '\n  <script>var a=document.getElementById("anio");if(a)a.textContent=new Date().getFullYear();</script>\n</body>\n</html>\n'


def boton_wa(texto, etiqueta="Escribir por WhatsApp"):
    return f'<a class="btn btn-wa" href="{wa_link(texto)}" target="_blank" rel="noopener">{ICONO_WA}<span>{etiqueta}</span></a>'


def caja_cta(texto_wa, titulo="¿Tienes un proyecto con esta obligación?"):
    return f"""
      <aside class="cta-caja" aria-label="Contacto">
        <p class="cta-titulo">{e(titulo)}</p>
        <p>Cuéntanos la ubicación, el área y la autoridad ambiental. Te respondemos en un día hábil, en cualquier región del país.</p>
        <div class="acciones">{boton_wa(texto_wa)}<a class="btn btn-bosque" href="/#contacto">Cotizar por formulario</a></div>
      </aside>"""


def migas_html(items):
    partes = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            partes.append(f'<span aria-current="page">{e(n)}</span>')
        else:
            partes.append(f'<a href="{u}">{e(n)}</a>')
    return '<nav class="migas" aria-label="Ruta">' + ' <span aria-hidden="true">/</span> '.join(partes) + "</nav>"


# ---------------------------------------------------------------- páginas

def pagina_servicio(s):
    ruta = url_servicio(s)
    migas = [("Inicio", "/"), ("Servicios", "/#servicios"), (s["nombre"], ruta)]
    pag = {"@type": "WebPage", "@id": f"{SITIO}{ruta}#pagina", "url": f"{SITIO}{ruta}", "name": s["h1"], "description": s["descripcion"],
           "inLanguage": "es-CO", "about": {"@id": f"{SITIO}{ruta}#servicio"}, "isPartOf": {"@id": f"{SITIO}/#sitio"}, "dateModified": HOY}
    grafo = [negocio(False), servicio_ld(s), pag, migas_ld(migas)]
    if s["faq"]:
        grafo.append(faq_ld(s["faq"], f"{SITIO}{ruta}#preguntas"))
    guia = ""
    if s.get("guia"):
        g = GUIA_POR_SLUG[s["guia"]]
        guia = f"""
      <a class="guia-enlace" href="{url_guia(g)}"><span>Guía práctica</span><strong>{e(g['titulo'])}</strong></a>"""
    hermanos = PRINCIPALES if s["principal"] else SERVICIOS
    otros = "".join(f'<li><a href="{url_servicio(o)}">{e(o["nombre"])}</a></li>' for o in hermanos if o is not s)
    cuerpo = f"""  <main class="interna servicio" id="contenido">
    <div class="wrap">
      {migas_html(migas)}
      <h1>{e(s['h1'])}</h1>
      <p class="lead">{e(s['lead'])}</p>
      <div class="acciones">{boton_wa(s['wa'])}<a class="btn btn-cinta" href="/#contacto">Cotizar el proyecto</a></div>
{s['cuerpo']}
{guia}
      <section class="faq-bloque" aria-labelledby="t-faq">
        <h2 id="t-faq">Preguntas frecuentes</h2>
        <div class="faq">{faq_html(s['faq'])}</div>
      </section>
{caja_cta(s['wa'])}

      <h2>Otros servicios</h2>
      <ul class="lista">{otros}</ul>
    </div>
  </main>
"""
    return cabeza(s["title"], s["descripcion"], ruta, ld(grafo)) + cuerpo + cola()


def pagina_guia(g):
    ruta = url_guia(g)
    s = POR_SLUG[g["servicio"]]
    migas = [("Inicio", "/"), ("Blog", "/blog/"), (g["titulo"], ruta)]
    palabras = len(re.sub(r"<[^>]+>", " ", g["cuerpo"]).split())
    minutos = max(1, round(palabras / 200))
    articulo = {
        "@type": "BlogPosting", "@id": f"{SITIO}{ruta}#articulo", "headline": g["titulo"], "description": g["descripcion"],
        "url": f"{SITIO}{ruta}", "mainEntityOfPage": f"{SITIO}{ruta}", "inLanguage": "es-CO",
        "datePublished": g["fecha"], "dateModified": g["fecha"], "image": f"{SITIO}/assets/og-image.jpg",
        "author": {"@id": f"{SITIO}/#negocio"}, "publisher": {"@id": f"{SITIO}/#negocio"},
        "about": {"@id": f"{SITIO}{url_servicio(s)}#servicio"}, "isPartOf": {"@id": f"{SITIO}/blog/#blog"}, "wordCount": palabras,
    }
    fuentes = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a></li>' for t, u in g["fuentes"])
    cuerpo = f"""  <main class="interna guia" id="contenido">
    <article class="wrap">
      {migas_html(migas)}
      <h1>{e(g['titulo'])}</h1>
      <p class="meta-guia">Por Metabosques · <time datetime="{g['fecha']}">{fecha_larga(g['fecha'])}</time> · {minutos} min de lectura</p>
      <p class="lead">{e(g['resumen'])}</p>
{g['cuerpo']}
      <p class="aviso">{e(AVISO.format(fecha=fecha_larga(g['fecha'])))}</p>
      <section class="fuentes" aria-labelledby="t-fuentes">
        <h2 id="t-fuentes">Fuentes</h2>
        <ul class="lista">{fuentes}</ul>
      </section>
{caja_cta(s['wa'], titulo='¿Quieres que lo hagamos por ti?')}
      <p class="volver"><a href="{url_servicio(s)}">Ver el servicio: {e(s['nombre'])}</a> · <a href="/blog/">Más guías</a></p>
    </article>
  </main>
"""
    return cabeza(g["title"], g["descripcion"], ruta, ld([negocio(False), articulo, migas_ld(migas)]), tipo_og="article") + cuerpo + cola()


def pagina_blog():
    ruta = "/blog/"
    migas = [("Inicio", "/"), ("Blog", ruta)]
    blog = {"@type": "Blog", "@id": f"{SITIO}/blog/#blog", "url": f"{SITIO}/blog/", "name": "Guías prácticas de Metabosques",
            "inLanguage": "es-CO", "publisher": {"@id": f"{SITIO}/#negocio"},
            "blogPost": [{"@id": f"{SITIO}{url_guia(g)}#articulo"} for g in GUIAS]}
    tarjetas = "".join(f"""
        <li class="entrada">
          <a href="{url_guia(g)}">
            <span class="entrada-fecha"><time datetime="{g['fecha']}">{fecha_larga(g['fecha'])}</time></span>
            <h2>{e(g['titulo'])}</h2>
            <p>{e(g['resumen'])}</p>
            <span class="entrada-mas">Leer la guía</span>
          </a>
        </li>""" for g in GUIAS)
    cuerpo = f"""  <main class="interna blog" id="contenido">
    <div class="wrap">
      {migas_html(migas)}
      <h1>Guías prácticas de cumplimiento ambiental</h1>
      <p class="lead">Explicamos paso a paso las obligaciones ambientales que más dudas generan en Colombia: compensaciones, inversión del 1 % y permisos forestales.</p>
      <ul class="entradas">{tarjetas}
      </ul>
{caja_cta('Hola Metabosques, leí sus guías y quiero apoyo con un proyecto.', titulo='¿Prefieres que lo revisemos contigo?')}
    </div>
  </main>
"""
    return cabeza("Blog: guías prácticas de cumplimiento ambiental", "Guías paso a paso sobre compensación por pérdida de biodiversidad (Res. 305 de 2026), inversión forzosa del 1 % y permisos de aprovechamiento forestal en Colombia.", ruta, ld([negocio(False), blog, migas_ld(migas)])) + cuerpo + cola()


def pagina_redireccion(destino):
    url = f"{SITIO}/{destino}"
    return f"""<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <title>Esta página se trasladó | Metabosques</title>
  <link rel="canonical" href="{url}">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url=/{destino}">
  <script>location.replace("/{destino}" + location.hash);</script>
</head>
<body>
  <p>Esta página se trasladó a <a href="/{destino}">{url}</a>.</p>
</body>
</html>
"""


# ---------------------------------------------------------------- portada

def servicios_portada():
    def li(s):
        return f"""
          <li>
            <h3><a href="{url_servicio(s)}">{e(s['nombre'])}</a></h3>
            <p>{e(s['resumen'])}</p>
            <a class="mas" href="{url_servicio(s)}">Ver el servicio</a>
          </li>"""
    otros = "".join(f'<li><a href="{url_servicio(s)}">{e(s["nombre"])}</a></li>' for s in COMPLEMENTARIOS)
    return ("<!-- servicios:inicio -->" + "".join(li(s) for s in PRINCIPALES) + """
        </ul>
        <p class="tambien">También hacemos:</p>
        <ul class="tambien-lista">""" + otros + "<!-- servicios:fin -->")


def opciones_formulario():
    ops = "".join(f"\n              <option>{e(s['nombre'])}</option>" for s in SERVICIOS)
    return "<!-- opciones:inicio -->" + ops + "\n              <option>Otro</option>\n            <!-- opciones:fin -->"


def reemplazar(texto, marca, nuevo):
    patron = re.compile(rf"<!-- {marca}:inicio -->.*?<!-- {marca}:fin -->", re.S)
    if not patron.search(texto):
        raise SystemExit(f"No encontré los marcadores {marca}")
    return patron.sub(lambda m: nuevo, texto)


def escribir(ruta_rel, contenido):
    ruta = os.path.join(RAIZ, ruta_rel)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)


def main():
    for s in SERVICIOS:
        escribir(f"{s['slug']}.html", pagina_servicio(s))
    for g in GUIAS:
        escribir(f"blog/{g['slug']}.html", pagina_guia(g))
    escribir("blog/index.html", pagina_blog())
    for viejo, nuevo in REDIRECCIONES.items():
        escribir(f"{viejo}/index.html", pagina_redireccion(nuevo))

    sitio = {"@type": "WebSite", "@id": f"{SITIO}/#sitio", "url": f"{SITIO}/", "name": "Metabosques", "inLanguage": "es-CO", "publisher": {"@id": f"{SITIO}/#negocio"}}
    ruta = os.path.join(RAIZ, "index.html")
    t = open(ruta, encoding="utf-8").read()
    t = reemplazar(t, "schema", ld([negocio(), sitio] + [servicio_ld(s, portada=True) for s in SERVICIOS] + [faq_ld(FAQ_PORTADA, f"{SITIO}/#preguntas")]))
    t = reemplazar(t, "servicios", servicios_portada())
    t = reemplazar(t, "opciones", opciones_formulario())
    t = reemplazar(t, "faq", "<!-- faq:inicio -->" + faq_html(FAQ_PORTADA) + "<!-- faq:fin -->")
    t = reemplazar(t, "pie", pie_html())
    open(ruta, "w", encoding="utf-8").write(t)
    for nombre in ("politica-privacidad.html", "gracias.html", "404.html"):
        r = os.path.join(RAIZ, nombre)
        t = open(r, encoding="utf-8").read()
        open(r, "w", encoding="utf-8").write(reemplazar(t, "pie", pie_html()))

    urls = [("/", "1.0", HOY)] + [(url_servicio(s), "0.9" if s["principal"] else "0.6", HOY) for s in SERVICIOS] \
        + [("/blog/", "0.7", HOY)] + [(url_guia(g), "0.8", g["fecha"]) for g in GUIAS] + [("/politica-privacidad.html", "0.2", HOY)]
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u, p, d in urls:
            f.write(f"  <url><loc>{SITIO}{u}</loc><lastmod>{d}</lastmod><priority>{p}</priority></url>\n")
        f.write("</urlset>\n")

    lineas = ["# Metabosques S.A.S.", "",
              "> Empresa ambiental colombiana que presta servicios en todo el país (sede administrativa en Medellín). Aprovechamiento forestal para parques solares, vías, líneas de transmisión y obras; compensación por pérdida de biodiversidad (Resolución 305 de 2026); inversión forzosa del 1 %; rescate de flora y fauna; restauración ecológica; y seguimiento ambiental con informes de cumplimiento (ICA).",
              "", f"Contacto: {TEL} (WhatsApp) · {CORREO} · {SITIO}/#contacto",
              "Cifras: 250 hectáreas restauradas y 120.000 árboles sembrados.", "", "## Servicios principales", ""]
    lineas += [f"- [{s['nombre']}]({SITIO}{url_servicio(s)}): {s['descripcion']}" for s in PRINCIPALES]
    lineas += ["", "## Servicios complementarios", ""]
    lineas += [f"- [{s['nombre']}]({SITIO}{url_servicio(s)}): {s['descripcion']}" for s in COMPLEMENTARIOS]
    lineas += ["", "## Guías prácticas", ""]
    lineas += [f"- [{g['titulo']}]({SITIO}{url_guia(g)}): {g['descripcion']}" for g in GUIAS]
    lineas += ["", "## Preguntas frecuentes", ""]
    lineas += [f"- **{q}** {a}" for q, a in FAQ_PORTADA]
    lineas += ["", "## Otros", "", f"- [Política de privacidad]({SITIO}/politica-privacidad.html)"]
    escribir("llms.txt", "\n".join(lineas) + "\n")
    print(f"Listo: {len(SERVICIOS)} servicios, {len(GUIAS)} guías, {len(REDIRECCIONES)} redirecciones, {len(urls)} URL en el sitemap")


if __name__ == "__main__":
    main()
