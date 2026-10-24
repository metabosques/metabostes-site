"""Genera las páginas de servicio, el pie común, los datos estructurados y el sitemap.

Uso: python3 herramientas/generar_paginas.py   (desde la raíz del repositorio)

- Las redes sociales se leen de herramientas/redes.json; una red con valor vacío no se muestra.
- Las páginas de servicio se escriben en servicios/<slug>/index.html (URL limpia /servicios/<slug>/).
- En index.html, politica-privacidad.html, gracias.html y 404.html se reemplaza lo que hay entre
  los comentarios <!-- pie:inicio --> y <!-- pie:fin -->, y el JSON-LD entre <!-- schema:inicio --> y <!-- schema:fin -->.
"""
import html, json, os, re, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = "https://metabosques.com"
HOY = datetime.date.today().isoformat()
WA = "573007925238"
TEL = "+57 300 792 5238"
CORREO = "amoreno@metabosques.com"

with open(os.path.join(RAIZ, "herramientas", "redes.json"), encoding="utf-8") as f:
    REDES = {k: v.strip() for k, v in json.load(f).items() if v and v.strip()}

ICONOS = {
    "Instagram": '<path d="M12 7.2a4.8 4.8 0 1 0 0 9.6 4.8 4.8 0 0 0 0-9.6Zm0 7.9a3.1 3.1 0 1 1 0-6.2 3.1 3.1 0 0 1 0 6.2Zm5-8.1a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0ZM12 3.6c2.7 0 3 0 4.1.1 2.7.1 4 1.4 4.1 4.1.1 1.1.1 1.4.1 4.1s0 3-.1 4.1c-.1 2.7-1.4 4-4.1 4.1-1.1.1-1.4.1-4.1.1s-3 0-4.1-.1c-2.7-.1-4-1.4-4.1-4.1C3.7 15 3.6 14.7 3.6 12s0-3 .1-4.1c.1-2.7 1.4-4 4.1-4.1 1.1-.2 1.4-.2 4.2-.2ZM12 2c-2.7 0-3.1 0-4.1.1C4.2 2.2 2.2 4.2 2.1 7.9 2 8.9 2 9.3 2 12s0 3.1.1 4.1c.1 3.7 2.1 5.7 5.8 5.8 1 .1 1.4.1 4.1.1s3.1 0 4.1-.1c3.7-.1 5.7-2.1 5.8-5.8.1-1 .1-1.4.1-4.1s0-3.1-.1-4.1c-.1-3.7-2.1-5.7-5.8-5.8C15.1 2 14.7 2 12 2Z"/>',
    "Facebook": '<path d="M13.5 21.9v-7.7h2.6l.4-3h-3V9.3c0-.9.3-1.5 1.5-1.5h1.6V5.1c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6v7.7C5.6 21.2 2 17 2 12 2 6.5 6.5 2 12 2s10 4.5 10 10c0 5-3.6 9.2-8.5 9.9Z"/>',
    "LinkedIn": '<path d="M20.4 2H3.6C2.7 2 2 2.7 2 3.5v17c0 .8.7 1.5 1.6 1.5h16.8c.9 0 1.6-.7 1.6-1.5v-17c0-.8-.7-1.5-1.6-1.5ZM8 19H5V9.5h3V19ZM6.5 8.2a1.7 1.7 0 1 1 0-3.4 1.7 1.7 0 0 1 0 3.4ZM19 19h-3v-4.6c0-1.1 0-2.5-1.5-2.5S12.8 13 12.8 14.3V19h-3V9.5h2.8v1.3h.1c.4-.7 1.4-1.5 2.8-1.5 3 0 3.6 2 3.6 4.6V19Z"/>',
    "YouTube": '<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.5 2.5 0 0 0-1.8 1.8C2 8.8 2 12 2 12s0 3.2.4 4.8c.2.9.9 1.6 1.8 1.8 1.6.4 7.8.4 7.8.4s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8ZM10 15V9l5.2 3L10 15Z"/>',
}

SERVICIOS = [
    {
        "slug": "restauracion-ecologica-compensaciones",
        "nombre": "Restauración ecológica y compensaciones",
        "titulo": "Restauración ecológica y compensaciones bióticas en Colombia",
        "descripcion": "Diseñamos, tramitamos y ejecutamos planes de compensación biótica y forestal con restauración activa, pasiva y enriquecimiento con especies nativas en Colombia.",
        "tipo": "Restauración ecológica y compensación ambiental",
        "intro": "Cuando un proyecto genera una obligación de compensación, la autoridad ambiental exige un plan técnico, su ejecución en campo y pruebas de que la restauración funciona. Nos encargamos de las tres cosas.",
        "incluye": [
            "Diagnóstico del área a compensar y de las áreas candidatas para restaurar.",
            "Plan de compensación biótica y forestal con sus estrategias de restauración activa, pasiva o enriquecimiento.",
            "Producción o selección de material vegetal de especies nativas y siembra con mano de obra local.",
            "Mantenimiento de las áreas establecidas: control de competencia, fertilización y resiembra.",
            "Monitoreo con indicadores de supervivencia, cobertura y regeneración.",
        ],
        "entrega": "El plan de compensación, el establecimiento y mantenimiento en campo, y los informes de cumplimiento ambiental (ICA) para la autoridad.",
        "para": "Empresas con licencias o permisos ambientales que tienen obligaciones de compensación por pérdida de biodiversidad o por aprovechamiento forestal, y entidades públicas con metas de restauración.",
        "ecosistemas": "Hemos trabajado en franjas costeras, humedales y sabanas, con siembra, vivero y monitoreo propios.",
    },
    {
        "slug": "aprovechamiento-forestal",
        "nombre": "Aprovechamientos forestales sostenibles",
        "titulo": "Aprovechamiento forestal: inventario, permiso y salvoconductos",
        "descripcion": "Formulamos, tramitamos y ejecutamos planes de aprovechamiento forestal ante las corporaciones autónomas regionales: inventario, marcación, cubicación, permiso y salvoconductos.",
        "tipo": "Aprovechamiento forestal",
        "intro": "Talar o intervenir árboles para un proyecto requiere un permiso de aprovechamiento forestal. Preparamos la información técnica que pide la corporación, acompañamos el trámite y ejecutamos el aprovechamiento cumpliendo lo autorizado.",
        "incluye": [
            "Inventario forestal al 100 % o por muestreo, según lo que exija la autoridad.",
            "Marcación, identificación de especies y cubicación de volúmenes.",
            "Formulación del plan de aprovechamiento y radicación ante la corporación autónoma regional.",
            "Gestión de los salvoconductos para la movilización de la madera.",
            "Definición de la compensación forestal asociada al permiso.",
        ],
        "entrega": "El inventario forestal, la marcación y cubicación, y el trámite del permiso de aprovechamiento y de los salvoconductos.",
        "para": "Empresas de energía, infraestructura, construcción y agroindustria que necesitan intervenir coberturas vegetales, y propietarios de predios con árboles por aprovechar.",
        "ecosistemas": "El trámite cambia de una corporación a otra; adaptamos la información técnica a lo que pide cada una.",
    },
    {
        "slug": "consultoria-ambiental",
        "nombre": "Consultoría ambiental",
        "titulo": "Consultoría ambiental: estudios de impacto, planes de manejo y SIG",
        "descripcion": "Estudios de impacto ambiental, planes de manejo, monitoreo de fauna y flora y cartografía SIG para licencias y permisos ambientales en Colombia.",
        "tipo": "Consultoría ambiental",
        "intro": "Acompañamos a empresas y entidades desde la línea base hasta la obtención y el seguimiento de licencias y permisos ambientales, con trabajo de campo propio y análisis espacial.",
        "incluye": [
            "Estudios de impacto ambiental (EIA) y planes de manejo ambiental.",
            "Caracterización y monitoreo de fauna y flora, incluido fototrampeo con cámaras trampa.",
            "Cartografía y análisis espacial en sistemas de información geográfica (SIG).",
            "Acompañamiento en solicitudes de licencias, permisos y sus modificaciones.",
            "Respuesta a requerimientos de la autoridad ambiental.",
        ],
        "entrega": "Estudios de impacto y planes de manejo, monitoreos de fauna y flora, y cartografía SIG lista para radicar.",
        "para": "Proyectos que necesitan licencia o permiso ambiental, y titulares que deben atender seguimientos o requerimientos de la autoridad.",
        "ecosistemas": "Los monitoreos se diseñan para cada ecosistema y para los indicadores que pide la licencia.",
    },
    {
        "slug": "mantenimiento-obras-ambientales",
        "nombre": "Mantenimiento y obras ambientales",
        "titulo": "Mantenimiento de zonas verdes, compensaciones y obras ambientales",
        "descripcion": "Mantenimiento de áreas verdes y zonas de compensación, rocería, revegetalización, limpieza de paneles solares y obras civiles menores con criterio paisajístico.",
        "tipo": "Mantenimiento ambiental",
        "intro": "Una siembra o una zona verde sin mantenimiento se pierde. Ofrecemos cuadrillas con supervisión técnica para conservar las áreas establecidas y la infraestructura asociada.",
        "incluye": [
            "Rocería y control de competencia en zonas de compensación y áreas verdes.",
            "Revegetalización de taludes y áreas intervenidas.",
            "Limpieza de paneles solares en parques fotovoltaicos.",
            "Obras civiles menores con criterio paisajístico.",
            "Registro fotográfico y reportes de cada intervención.",
        ],
        "entrega": "Rocería y revegetalización, limpieza de paneles solares y obras civiles menores, con reportes de cada visita.",
        "para": "Operadores de infraestructura y parques solares, y empresas que deben mantener sus áreas de compensación durante varios años.",
        "ecosistemas": "Programamos la frecuencia de mantenimiento según el clima y el crecimiento de cada zona.",
    },
    {
        "slug": "naturaunidad",
        "nombre": "NaturaUnidad",
        "titulo": "NaturaUnidad: soluciones basadas en la naturaleza para carbono y biodiversidad",
        "descripcion": "Soluciones basadas en la naturaleza para metas corporativas de carbono y biodiversidad, con línea base, indicadores verificables y reportes de sostenibilidad.",
        "tipo": "Soluciones basadas en la naturaleza",
        "intro": "NaturaUnidad es nuestra línea para empresas que quieren ir más allá de la obligación legal: proyectos de restauración voluntaria con resultados que se pueden medir y reportar.",
        "incluye": [
            "Línea base de biodiversidad del área del proyecto.",
            "Diseño de la intervención de restauración con especies nativas.",
            "Indicadores verificables de carbono y biodiversidad.",
            "Seguimiento en campo y reportes para informes de sostenibilidad.",
        ],
        "entrega": "La línea base de biodiversidad, indicadores verificables y reportes de sostenibilidad.",
        "para": "Empresas con metas de carbono neutralidad, biodiversidad o reportes ESG que buscan proyectos en Colombia con trazabilidad.",
        "ecosistemas": "Cada proyecto se diseña con la comunidad y el ecosistema del lugar.",
    },
]

FAQ = [
    ("¿En qué regiones de Colombia trabajan?",
     "Tenemos sede en Medellín y ejecutamos proyectos en todo el país. Hemos trabajado en franjas costeras, humedales y sabanas, con vivero, siembra y monitoreo propios."),
    ("¿Qué es una compensación biótica y quién debe hacerla?",
     "Es la obligación de restaurar o conservar un área equivalente a la que un proyecto afecta. La deben cumplir las empresas cuya licencia o permiso ambiental la exige, por ejemplo por pérdida de biodiversidad o por un aprovechamiento forestal."),
    ("¿Hacen el trámite ante la corporación autónoma regional?",
     "Sí. Formulamos los planes y estudios, los radicamos ante la autoridad ambiental competente y respondemos sus requerimientos hasta obtener el permiso o la aprobación."),
    ("¿Se encargan del mantenimiento después de la siembra?",
     "Sí. Hacemos el mantenimiento de las áreas establecidas, medimos los indicadores y entregamos los informes de cumplimiento ambiental (ICA) que pide la autoridad."),
    ("¿Qué información necesitan para cotizar un proyecto?",
     "La ubicación del predio, el área aproximada, la autoridad ambiental que lleva el caso y los plazos. Si tienes el acto administrativo con la obligación, compártelo."),
    ("¿Cuánto tardan en responder una solicitud?",
     "Respondemos en un día hábil por correo o WhatsApp."),
    ("¿Qué es NaturaUnidad?",
     "Es nuestra línea de soluciones basadas en la naturaleza para empresas con metas voluntarias de carbono y biodiversidad, con indicadores verificables y reportes de sostenibilidad."),
]

e = html.escape


def redes_html():
    if not REDES:
        return ""
    items = []
    for nombre, url in REDES.items():
        icono = ICONOS.get(nombre, "")
        items.append(
            f'<a href="{e(url)}" target="_blank" rel="noopener me" aria-label="Metabosques en {nombre}">'
            f'<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" fill="currentColor">{icono}</svg>'
            f'<span>{nombre}</span></a>'
        )
    return '\n      <nav class="redes" aria-label="Redes sociales">' + "".join(items) + "</nav>"


def pie_html():
    servicios = "".join(f'<a href="/servicios/{s["slug"]}/">{e(s["nombre"])}</a>' for s in SERVICIOS)
    return f"""<!-- pie:inicio -->
  <footer class="pie">
    <div class="pie-bloque">
      <p class="pie-marca">Metabosques S.A.S.</p>
      <p>Restauración ecológica y gestión forestal. Medellín, Colombia.</p>
      <p><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{TEL}</a> · <a href="mailto:{CORREO}">{CORREO}</a></p>{redes_html()}
    </div>
    <nav class="pie-bloque" aria-label="Servicios">
      <p class="pie-titulo">Servicios</p>{servicios}
    </nav>
    <nav class="pie-bloque" aria-label="Más">
      <p class="pie-titulo">Metabosques</p><a href="/#como-trabajamos">Cómo trabajamos</a><a href="/#en-campo">En campo</a><a href="/#preguntas">Preguntas frecuentes</a><a href="/#contacto">Contacto</a><a href="/politica-privacidad.html">Política de privacidad</a>
    </nav>
    <p class="pie-legal">© <span id="anio">2026</span> Metabosques S.A.S.</p>
  </footer>
  <a class="wa" href="https://wa.me/{WA}?text=Hola%20Metabosques%2C%20quiero%20informaci%C3%B3n%20sobre%20sus%20servicios." target="_blank" rel="noopener" aria-label="Escribir a Metabosques por WhatsApp">
    <img src="/assets/wa.svg" alt="" width="28" height="28">
  </a>
  <!-- pie:fin -->"""


def negocio():
    d = {
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": f"{SITIO}/#negocio",
        "name": "Metabosques S.A.S.",
        "alternateName": "Metabosques",
        "description": "Empresa ambiental colombiana con sede en Medellín. Restauración ecológica, compensaciones bióticas, aprovechamiento forestal, consultoría ambiental y mantenimiento de áreas de compensación.",
        "url": f"{SITIO}/",
        "logo": f"{SITIO}/assets/logo.png",
        "image": f"{SITIO}/assets/og-image.jpg",
        "email": CORREO,
        "telephone": "+573007925238",
        "address": {"@type": "PostalAddress", "addressLocality": "Medellín", "addressRegion": "Antioquia", "addressCountry": "CO"},
        "areaServed": {"@type": "Country", "name": "Colombia"},
        "priceRange": "Cotización por proyecto",
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"},
        "contactPoint": {"@type": "ContactPoint", "contactType": "Ventas", "telephone": "+573007925238", "email": CORREO, "availableLanguage": "es"},
        "knowsAbout": ["Restauración ecológica", "Compensaciones bióticas", "Aprovechamiento forestal", "Consultoría ambiental", "Monitoreo de fauna y flora", "Sistemas de información geográfica", "Soluciones basadas en la naturaleza"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Servicios ambientales",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@id": f"{SITIO}/servicios/{s['slug']}/#servicio"}} for s in SERVICIOS],
        },
    }
    if REDES:
        d["sameAs"] = list(REDES.values())
    return d


def servicio_ld(s):
    return {
        "@type": "Service",
        "@id": f"{SITIO}/servicios/{s['slug']}/#servicio",
        "name": s["nombre"],
        "serviceType": s["tipo"],
        "description": s["descripcion"],
        "url": f"{SITIO}/servicios/{s['slug']}/",
        "provider": {"@id": f"{SITIO}/#negocio"},
        "areaServed": {"@type": "Country", "name": "Colombia"},
        "audience": {"@type": "BusinessAudience", "name": s["para"]},
    }


def ld(grafo):
    return ('<!-- schema:inicio -->\n  <script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)
            + "\n  </script>\n  <!-- schema:fin -->")


def cabeza(titulo, descripcion, ruta, extra=""):
    url = f"{SITIO}{ruta}"
    return f"""<!doctype html>
<html lang="es-CO">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{e(titulo)} | Metabosques</title>
  <meta name="description" content="{e(descripcion)}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#0F2A22">
  <link rel="icon" href="/assets/favicon.png">
  <link rel="apple-touch-icon" href="/assets/logo.png">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_CO">
  <meta property="og:site_name" content="Metabosques">
  <meta property="og:title" content="{e(titulo)}">
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


def pagina_servicio(s):
    ruta = f"/servicios/{s['slug']}/"
    migas = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITIO}/"},
            {"@type": "ListItem", "position": 2, "name": "Servicios", "item": f"{SITIO}/#servicios"},
            {"@type": "ListItem", "position": 3, "name": s["nombre"], "item": f"{SITIO}{ruta}"},
        ],
    }
    pag = {"@type": "WebPage", "@id": f"{SITIO}{ruta}#pagina", "url": f"{SITIO}{ruta}", "name": s["titulo"],
           "description": s["descripcion"], "inLanguage": "es-CO", "about": {"@id": f"{SITIO}{ruta}#servicio"},
           "isPartOf": {"@id": f"{SITIO}/#sitio"}, "dateModified": HOY}
    otros = "".join(f'<li><a href="/servicios/{o["slug"]}/">{e(o["nombre"])}</a></li>' for o in SERVICIOS if o is not s)
    incluye = "".join(f"<li>{e(i)}</li>" for i in s["incluye"])
    wa_txt = f"Hola Metabosques, quiero cotizar: {s['nombre']}"
    from urllib.parse import quote
    cuerpo = f"""  <main class="interna servicio" id="contenido">
    <div class="wrap">
      <nav class="migas" aria-label="Ruta"><a href="/">Inicio</a> <span aria-hidden="true">/</span> <a href="/#servicios">Servicios</a> <span aria-hidden="true">/</span> <span aria-current="page">{e(s['nombre'])}</span></nav>
      <h1>{e(s['titulo'])}</h1>
      <p class="lead">{e(s['intro'])}</p>
      <div class="acciones">
        <a class="btn btn-cinta" href="/#contacto">Cotizar este servicio</a>
        <a class="btn btn-bosque" href="https://wa.me/{WA}?text={quote(wa_txt)}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>

      <h2>Qué incluye</h2>
      <ul class="lista">{incluye}</ul>

      <h2>Qué entregamos</h2>
      <p>{e(s['entrega'])}</p>

      <h2>Para quién es</h2>
      <p>{e(s['para'])}</p>
      <p>{e(s['ecosistemas'])}</p>

      <h2>Cómo trabajamos</h2>
      <p>Un solo equipo responde por el proyecto: visita y diagnóstico, diseño y trámite ante la autoridad ambiental, ejecución en campo, y monitoreo con informes de cumplimiento. Respondemos las solicitudes en un día hábil.</p>

      <h2>Otros servicios</h2>
      <ul class="lista">{otros}</ul>
    </div>
  </main>
"""
    extra = ld([negocio_ref(), servicio_ld(s), pag, migas])
    return cabeza(s["titulo"], s["descripcion"], ruta, extra) + cuerpo + "  " + pie_html() + '\n  <script>var a=document.getElementById("anio");if(a)a.textContent=new Date().getFullYear();</script>\n</body>\n</html>\n'


def negocio_ref():
    # en páginas internas basta una versión corta del negocio enlazada por @id
    return {"@type": ["LocalBusiness", "ProfessionalService"], "@id": f"{SITIO}/#negocio", "name": "Metabosques S.A.S.",
            "url": f"{SITIO}/", "telephone": "+573007925238", "email": CORREO, "image": f"{SITIO}/assets/og-image.jpg",
            "address": {"@type": "PostalAddress", "addressLocality": "Medellín", "addressRegion": "Antioquia", "addressCountry": "CO"}}


def faq_html():
    items = "".join(
        f'<details><summary><h3>{e(q)}</h3></summary><p>{e(a)}</p></details>' for q, a in FAQ)
    return items


def reemplazar(texto, marca, nuevo):
    patron = re.compile(rf"<!-- {marca}:inicio -->.*?<!-- {marca}:fin -->", re.S)
    if not patron.search(texto):
        raise SystemExit(f"No encontré los marcadores {marca} en el archivo")
    return patron.sub(lambda m: nuevo, texto)


def main():
    # páginas de servicio
    for s in SERVICIOS:
        d = os.path.join(RAIZ, "servicios", s["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(pagina_servicio(s))

    # portada: schema completo + FAQ
    sitio = {"@type": "WebSite", "@id": f"{SITIO}/#sitio", "url": f"{SITIO}/", "name": "Metabosques", "inLanguage": "es-CO", "publisher": {"@id": f"{SITIO}/#negocio"}}
    faq = {"@type": "FAQPage", "@id": f"{SITIO}/#preguntas",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    ruta = os.path.join(RAIZ, "index.html")
    t = open(ruta, encoding="utf-8").read()
    t = reemplazar(t, "schema", ld([negocio(), sitio] + [servicio_ld(s) for s in SERVICIOS] + [faq]))
    t = reemplazar(t, "faq", "<!-- faq:inicio -->" + faq_html() + "<!-- faq:fin -->")
    t = reemplazar(t, "pie", pie_html())
    open(ruta, "w", encoding="utf-8").write(t)

    for nombre in ("politica-privacidad.html", "gracias.html", "404.html"):
        ruta = os.path.join(RAIZ, nombre)
        t = open(ruta, encoding="utf-8").read()
        t = reemplazar(t, "pie", pie_html())
        open(ruta, "w", encoding="utf-8").write(t)

    # sitemap
    urls = [("/", "1.0"), *[(f"/servicios/{s['slug']}/", "0.8") for s in SERVICIOS], ("/politica-privacidad.html", "0.2")]
    with open(os.path.join(RAIZ, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u, p in urls:
            f.write(f"  <url><loc>{SITIO}{u}</loc><lastmod>{HOY}</lastmod><priority>{p}</priority></url>\n")
        f.write("</urlset>\n")

    # llms.txt: resumen legible para buscadores de IA
    lineas = ["# Metabosques S.A.S.", "",
              "> Empresa ambiental colombiana con sede en Medellín. Diseña, tramita y ejecuta compensaciones bióticas, restauración ecológica, aprovechamiento forestal, consultoría ambiental y mantenimiento de áreas de compensación para empresas y entidades públicas en toda Colombia.",
              "", f"Contacto: {TEL} (WhatsApp) · {CORREO} · {SITIO}/#contacto",
              "Cifras: 250 hectáreas restauradas y 120.000 árboles sembrados.", "", "## Servicios", ""]
    lineas += [f"- [{s['nombre']}]({SITIO}/servicios/{s['slug']}/): {s['descripcion']}" for s in SERVICIOS]
    lineas += ["", "## Preguntas frecuentes", ""]
    for q, a in FAQ:
        lineas += [f"- **{q}** {a}"]
    lineas += ["", "## Otros", "", f"- [Política de privacidad]({SITIO}/politica-privacidad.html)"]
    open(os.path.join(RAIZ, "llms.txt"), "w", encoding="utf-8").write("\n".join(lineas) + "\n")
    print("Listo:", len(SERVICIOS), "páginas de servicio;", len(REDES), "redes en el pie")


if __name__ == "__main__":
    main()
