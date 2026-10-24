# Metabosques – sitio web (GitHub Pages)

Sitio estático en HTML, CSS y JS, sin dependencias ni paso de compilación. Todo vive en la raíz del repositorio.

## Archivos
- `index.html` – página principal (servicios, cómo trabajamos, en campo, nosotros, contacto)
- `politica-privacidad.html` – política de tratamiento de datos (Ley 1581 de 2012)
- `gracias.html` – confirmación después de enviar el formulario
- `404.html` – página de error
- `styles.css`, `script.js` – estilos y comportamiento (menú móvil, curvas de nivel generadas y visor de fotos)
- `assets/` – logo, favicon, icono de WhatsApp e imagen para redes (`og-image.jpg`)
- `servicios/<servicio>/index.html` – una página por servicio (URL limpia /servicios/<servicio>/)
- `robots.txt`, `sitemap.xml`, `llms.txt` (resumen para buscadores de IA), `CNAME`

## Páginas de servicio, pie, datos estructurados y sitemap
Se generan con `python3 herramientas/generar_paginas.py`. Ahí están los textos de los servicios y las preguntas frecuentes.
Las redes sociales del pie se cambian en `herramientas/redes.json` (una red vacía no se muestra). Después de editar, corre el script y publica.
El script reescribe lo que hay entre los comentarios `<!-- pie:... -->`, `<!-- schema:... -->` y `<!-- faq:... -->`; no edites a mano esas partes.

## Formulario
Usa FormSubmit y llega a amoreno@metabosques.com. La primera vez que alguien lo envíe, FormSubmit manda un correo de activación a esa dirección: hay que confirmarlo una sola vez.

## DNS (GoDaddy)
4 registros A @ (185.199.108.153 / 109.153 / 110.153 / 111.153) + CNAME www → metabosques.github.io

## Fotos
Las fotos de campo están en `assets/fotos/` en dos tamaños: `-p.webp` (640 px, galería) y `-g.webp` (visor y portada). Se les quitaron los metadatos de ubicación y el sello de coordenadas de la cámara trampa.

## La figura por piezas
Inspirada en *In Pieces* (species-in-pieces.com): una figura de 48 triángulos hechos con `clip-path` se rearma en una especie colombiana distinta en cada sección (ceiba, colibrí, palma de cera, jaguar, mariposa morfo) y el fondo cambia de color con ella. Al hacer clic en la figura se ve la siguiente especie. Con "reducir movimiento" activado en el dispositivo, los cambios ocurren sin animación.
