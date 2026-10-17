# Metabosques – sitio web (GitHub Pages)

Sitio estático en HTML, CSS y JS, sin dependencias ni paso de compilación. Todo vive en la raíz del repositorio.

## Archivos
- `index.html` – página principal (servicios, cómo trabajamos, en campo, nosotros, contacto)
- `politica-privacidad.html` – política de tratamiento de datos (Ley 1581 de 2012)
- `gracias.html` – confirmación después de enviar el formulario
- `404.html` – página de error
- `styles.css`, `script.js` – estilos y comportamiento (menú móvil, curvas de nivel generadas y visor de fotos)
- `assets/` – logo, favicon, icono de WhatsApp e imagen para redes (`og-image.jpg`)
- `robots.txt`, `sitemap.xml`, `CNAME`

## Formulario
Usa FormSubmit y llega a amoreno@metabosques.com. La primera vez que alguien lo envíe, FormSubmit manda un correo de activación a esa dirección: hay que confirmarlo una sola vez.

## DNS (GoDaddy)
4 registros A @ (185.199.108.153 / 109.153 / 110.153 / 111.153) + CNAME www → metabosques.github.io

## Fotos
Las fotos de campo están en `assets/fotos/` en dos tamaños: `-p.webp` (640 px, galería) y `-g.webp` (visor y portada). Se les quitaron los metadatos de ubicación y el sello de coordenadas de la cámara trampa.
