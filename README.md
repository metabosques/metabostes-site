# Metabosques – sitio web (GitHub Pages)

Sitio estático en HTML, CSS y JS, sin dependencias ni paso de compilación. Todo vive en la raíz del repositorio.

## Archivos
- `index.html` – página principal (servicios, cómo trabajamos, proyectos, nosotros, contacto)
- `politica-privacidad.html` – política de tratamiento de datos (Ley 1581 de 2012)
- `gracias.html` – confirmación después de enviar el formulario
- `404.html` – página de error
- `styles.css`, `script.js` – estilos y comportamiento (menú móvil y curvas de nivel generadas)
- `assets/` – logo, favicon, icono de WhatsApp e imagen para redes (`og-image.png`)
- `robots.txt`, `sitemap.xml`, `CNAME`

## Formulario
Usa FormSubmit y llega a amoreno@metabosques.com. La primera vez que alguien lo envíe, FormSubmit manda un correo de activación a esa dirección: hay que confirmarlo una sola vez.

## Fotos de proyectos
El sitio no usa fotos de stock. Para agregar fotos reales de campo, guárdalas en `assets/` (JPG o WebP, 1600 px de ancho, menos de 300 KB) y cámbialas en el bloque `.caso .visual` de `index.html`.

## DNS (GoDaddy)
4 registros A @ (185.199.108.153 / 109.153 / 110.153 / 111.153) + CNAME www → metabosques.github.io
