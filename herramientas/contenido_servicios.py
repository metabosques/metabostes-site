"""Textos de las páginas de servicio. El HTML de 'cuerpo' se inserta tal cual en la página.

Cada servicio: slug (= URL /<slug>), nombre corto, h1 (con la palabra clave), title, descripcion (meta),
tipo (serviceType), lead, cuerpo (HTML), faq [(pregunta, respuesta)], guia (slug de blog relacionado o None),
wa (texto del mensaje de WhatsApp), principal (True = uno de los 6 servicios principales).
"""

SERVICIOS = [
    {
        "slug": "aprovechamiento-forestal",
        "nombre": "Aprovechamiento forestal",
        "h1": "Aprovechamiento forestal para parques solares, vías, líneas de transmisión y obras",
        "title": "Aprovechamiento forestal para parques solares, vías y líneas de transmisión",
        "descripcion": "Inventario forestal, permiso de aprovechamiento forestal único ante la CAR o dentro de la licencia, tala controlada, salvoconductos y compensación para proyectos en toda Colombia.",
        "resumen": "Inventario forestal, permiso de aprovechamiento, tala controlada y salvoconductos para parques solares, vías, líneas de transmisión y obras.",
        "tipo": "Aprovechamiento forestal",
        "principal": True,
        "lead": "Antes de despejar un lote para un parque solar, abrir una vía o tender una línea de transmisión, la autoridad ambiental tiene que autorizar la intervención de la vegetación. Hacemos el inventario forestal, tramitamos el permiso y ejecutamos el aprovechamiento cumpliendo lo autorizado, en cualquier región del país.",
        "cuerpo": """
      <h2>Para qué proyectos</h2>
      <ul class="lista">
        <li><strong>Parques solares y eólicos:</strong> despeje de lotes, franjas de seguridad y accesos.</li>
        <li><strong>Vías:</strong> corredores nuevos, ampliaciones, variantes y vías de acceso a proyectos.</li>
        <li><strong>Líneas de transmisión y distribución:</strong> servidumbres, sitios de torre y franjas de seguridad.</li>
        <li><strong>Obras civiles e infraestructura:</strong> lotes industriales, urbanismos, redes y adecuaciones de terreno.</li>
      </ul>

      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Verificación de restricciones antes de diseñar: reservas forestales, áreas protegidas, rondas hídricas y especies en veda o amenazadas.</li>
        <li>Inventario forestal: censo de los individuos a intervenir o muestreo estadístico, según lo que exija la autoridad.</li>
        <li>Identificación botánica, cálculo de volúmenes y cartografía del área de aprovechamiento.</li>
        <li>Plan de aprovechamiento forestal y radicación de la solicitud, con acompañamiento hasta la resolución.</li>
        <li>Plan de compensación según el manual de la Resolución 305 de 2026.</li>
        <li>Ejecución: marcación, tala dirigida, troceo, cubicación y apilado de la madera.</li>
        <li>Salvoconductos en línea para movilizar la madera y reportes de cumplimiento.</li>
      </ul>

      <h2>¿Permiso aparte o dentro de la licencia?</h2>
      <p>Si el proyecto tiene licencia ambiental, el aprovechamiento forestal se evalúa y se autoriza dentro de esa licencia, ante la ANLA o la corporación que la otorga. Si el proyecto no requiere licencia, como muchas obras, adecuaciones de lotes o plantas solares por debajo del umbral de licenciamiento, se tramita un permiso de aprovechamiento forestal único ante la corporación autónoma regional o la autoridad ambiental urbana del lugar. Los árboles aislados tienen un trámite propio, con reposición de individuos.</p>

      <h2>Normas que aplicamos</h2>
      <ul class="lista">
        <li>Decreto 1076 de 2015, capítulo de aprovechamiento forestal.</li>
        <li>Resolución 1909 de 2017, salvoconducto único nacional en línea.</li>
        <li>Resolución 0305 de 2026, manual de compensación del medio biótico.</li>
        <li>Decreto-Ley 2106 de 2019, artículo 125, sobre especies en veda.</li>
      </ul>""",
        "faq": [
            ("¿Necesito permiso para talar la vegetación de un lote para un parque solar?",
             "Sí. Talar vegetación natural requiere autorización de la autoridad ambiental. Si el parque tiene licencia ambiental, el aprovechamiento va dentro de la licencia; si no la requiere, se tramita un permiso de aprovechamiento forestal único ante la corporación del lugar."),
            ("¿Cuánto tarda un permiso de aprovechamiento forestal único?",
             "Depende de la corporación y de que la solicitud llegue completa. Lo que más acorta el trámite es radicar desde el inicio el inventario, el plan de aprovechamiento, los documentos del predio y el plan de compensación. En la cotización te damos un cronograma para tu caso."),
            ("¿Qué pasa si en el área hay especies en veda?",
             "Desde el Decreto-Ley 2106 de 2019 ya no se hace un trámite separado de levantamiento de veda: la autoridad impone las medidas de manejo dentro del mismo permiso o licencia. Incluimos esas especies en el inventario y en el plan de rescate."),
            ("¿Qué compensación me van a exigir?",
             "Para el aprovechamiento forestal único aplica el manual de compensación del medio biótico adoptado por la Resolución 305 de 2026. Para árboles aislados, la autoridad define una reposición de individuos."),
        ],
        "guia": "permiso-aprovechamiento-forestal-car-paso-a-paso",
        "wa": "Hola Metabosques, necesito un permiso de aprovechamiento forestal para un proyecto.",
    },
    {
        "slug": "compensacion-perdida-biodiversidad",
        "nombre": "Compensación por pérdida de biodiversidad",
        "h1": "Compensación por pérdida de biodiversidad con la Resolución 305 de 2026",
        "title": "Compensación por pérdida de biodiversidad: Resolución 305 de 2026",
        "descripcion": "Calculamos, formulamos y ejecutamos planes de compensación del medio biótico según el nuevo manual de la Resolución 305 de 2026: área, zonificación, acuerdos con propietarios, restauración e ICA.",
        "resumen": "Cálculo del área, plan de compensación y ejecución según el manual de compensación vigente.",
        "tipo": "Compensación ambiental del medio biótico",
        "principal": True,
        "lead": "Desde abril de 2026, los planes de compensación del medio biótico se rigen por la Resolución 0305 del Ministerio de Ambiente, que adoptó la actualización del manual y derogó la Resolución 256 de 2018. Te ayudamos a definir cuánto, dónde y cómo compensar, a presentar el plan y a ejecutarlo hasta cumplir la obligación.",
        "cuerpo": """
      <h2>Qué cambió con la Resolución 305 de 2026</h2>
      <ul class="lista">
        <li><strong>Factores por tipo de ecosistema.</strong> Ecosistemas naturales entre 4 y 10, vegetación secundaria entre 2 y 5, y ecosistemas transformados con factor 1, que puede subir si están dentro de un ecosistema estratégico.</li>
        <li><strong>La ubicación cuenta.</strong> El factor aumenta cuando la compensación se hace fuera del área de influencia del proyecto: más lejos o en otro bioma, mayor factor.</li>
        <li><strong>Plan más exigente.</strong> Zonificación a escala 1:25.000 o más detallada, análisis de adicionalidad y participación de las comunidades del área de influencia.</li>
        <li><strong>Se aprueba la zonificación, no el predio.</strong> La autoridad aprueba las áreas potenciales; los predios concretos se definen y se reportan en los informes de cumplimiento (ICA).</li>
        <li><strong>Compensación anticipada.</strong> Se puede empezar a compensar antes del impacto si el plan está aprobado.</li>
        <li><strong>Más trámites cubiertos.</strong> Además de licencias, sustracciones y aprovechamientos en bosque natural, incluye aprovechamientos únicos en plantaciones protectoras y protectoras-productoras.</li>
      </ul>

      <h2>Régimen de transición</h2>
      <ul class="lista">
        <li>Los trámites que estaban en curso y los planes que ya se ejecutaban siguen con la Resolución 256 de 2018, pero tienen 12 meses para acogerse voluntariamente al nuevo manual presentando el plan modificado.</li>
        <li>Los proyectos con licencia, permiso o sustracción sin plan de compensación aprobado tienen seis meses para presentarlo. Si estás en ese caso, conviene revisar el plazo cuanto antes.</li>
        <li>Acogerse al nuevo manual no sanea incumplimientos anteriores.</li>
      </ul>

      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Revisión del acto administrativo que impone la obligación y del régimen que te conviene.</li>
        <li>Cálculo del área a compensar por ecosistema y por ubicación.</li>
        <li>Búsqueda de áreas equivalentes y zonificación a la escala que pide el manual.</li>
        <li>Acuerdos con propietarios y comunidades, y análisis de adicionalidad.</li>
        <li>Plan de compensación con objetivos, metas, indicadores y cronograma.</li>
        <li>Ejecución en campo con restauración y preservación, monitoreo anual e informes ICA.</li>
      </ul>""",
        "faq": [
            ("¿Qué es la compensación por pérdida de biodiversidad?",
             "Es la obligación de un proyecto de recuperar o conservar un área ecológicamente equivalente a la que afecta, para que no haya pérdida neta de biodiversidad. La exige la autoridad en licencias ambientales, sustracciones de reservas forestales y aprovechamientos forestales únicos."),
            ("¿Tengo que acogerme a la Resolución 305 si mi plan ya estaba aprobado?",
             "No es obligatorio. Los planes aprobados siguen con la norma anterior, y hay 12 meses para acogerse voluntariamente. Comparamos el área, el costo y los plazos de ambos escenarios para que decidas."),
            ("¿Cómo se calcula el área a compensar?",
             "Se multiplica el área impactada de cada ecosistema por su factor de compensación, ajustado según dónde se haga la compensación. En el blog explicamos el cálculo paso a paso con un ejemplo."),
            ("¿Quién aprueba el plan de compensación?",
             "La autoridad que evalúa el trámite: el Ministerio de Ambiente, la ANLA, las corporaciones autónomas regionales, las autoridades de los grandes centros urbanos o Parques Nacionales Naturales, según el caso."),
        ],
        "guia": "como-calcular-compensacion-resolucion-305",
        "wa": "Hola Metabosques, necesito apoyo con una compensación por pérdida de biodiversidad (Res. 305 de 2026).",
    },
    {
        "slug": "inversion-forzosa-1-por-ciento",
        "nombre": "Inversión forzosa del 1 %",
        "h1": "Inversión forzosa del 1 %: liquidación, plan de inversión y ejecución",
        "title": "Inversión forzosa del 1 %: liquidación, plan y ejecución en la cuenca",
        "descripcion": "Te ayudamos a cumplir la inversión forzosa de no menos del 1 % por uso de agua de fuentes naturales: liquidación, plan de inversión ante la ANLA o la CAR, ejecución en la cuenca y actualización anual.",
        "resumen": "Liquidación, plan de inversión y ejecución en la cuenca para proyectos licenciados que captan agua de fuentes naturales.",
        "tipo": "Inversión forzosa de no menos del 1 %",
        "principal": True,
        "lead": "Si tu proyecto tiene licencia ambiental y capta agua directamente de un río, una quebrada o un acuífero, la ley te obliga a invertir al menos el 1 % del valor del proyecto en recuperar, preservar y conservar la cuenca de donde la tomas. Formulamos el plan de inversión, lo tramitamos y lo ejecutamos en campo.",
        "cuerpo": """
      <h2>¿Quién está obligado?</h2>
      <p>Según el parágrafo del artículo 43 de la Ley 99 de 1993 y el Decreto 1076 de 2015, deben hacer la inversión los proyectos que cumplen todas estas condiciones:</p>
      <ul class="lista">
        <li>Requieren licencia ambiental.</li>
        <li>Captan agua directamente de una fuente natural, superficial o subterránea.</li>
        <li>Usan esa agua en cualquiera de sus etapas, para cualquier actividad.</li>
      </ul>
      <p>Si el agua llega de un acueducto o de otro prestador del servicio, no hay obligación.</p>

      <h2>En qué se puede invertir</h2>
      <ul class="lista">
        <li>Restauración ecológica, rehabilitación y recuperación de la cuenca, incluidos proyectos de uso sostenible (forestales, agroforestales y silvopastoriles).</li>
        <li>Compra de predios o mejoras en áreas de importancia estratégica para la conservación.</li>
        <li>Monitoreo del recurso hídrico con estaciones hidrometeorológicas.</li>
        <li>Interceptores y tratamiento de aguas residuales domésticas en municipios de categorías 4, 5 y 6.</li>
        <li>Mecanismos como pago por servicios ambientales, acuerdos de conservación y bancos de hábitat.</li>
      </ul>
      <p>La inversión se hace primero en la subzona hidrográfica del proyecto y, con justificación técnica, en la zona hidrográfica. Los proyectos lineales pueden distribuirla entre las subzonas que atraviesan.</p>

      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Revisión de la obligación en la licencia y de la liquidación certificada.</li>
        <li>Identificación de predios y acciones en la cuenca, concertada con la autoridad, los municipios y las comunidades.</li>
        <li>Plan de inversión con actividades, metas, presupuesto y cronograma.</li>
        <li>Ejecución en campo: restauración, aislamientos, acuerdos de conservación y monitoreo.</li>
        <li>Actualización anual del saldo no ejecutado e informes de avance.</li>
      </ul>""",
        "faq": [
            ("¿Si tomo el agua de un acueducto debo hacer la inversión del 1 %?",
             "No. La obligación aplica cuando el proyecto licenciado capta el agua directamente de una fuente natural. Si la recibe de un acueducto u otro prestador, no está obligado."),
            ("¿Cuándo se presenta el plan de inversión?",
             "Las líneas generales se proponen con el estudio de impacto ambiental y quedan en la licencia. El plan con las acciones específicas se presenta dentro de los seis meses siguientes al fin de la construcción y el montaje; también se pueden presentar planes parciales durante la construcción."),
            ("¿Qué pasa con el dinero que no se ha ejecutado?",
             "El saldo se actualiza cada año con el IPC, con corte al 31 de diciembre, y la actualización se reporta a la autoridad a más tardar el 31 de marzo del año siguiente."),
            ("¿Se puede cambiar un plan de inversión ya aprobado?",
             "Sí. El Decreto 1076 de 2015 permite modificar el plan de inversión en cualquier momento, sin modificar la licencia, presentando la solicitud a la autoridad."),
        ],
        "guia": "inversion-forzosa-1-por-ciento-como-se-cumple",
        "wa": "Hola Metabosques, necesito apoyo con la inversión forzosa del 1 % de mi proyecto.",
    },
    {
        "slug": "rescate-flora-fauna",
        "nombre": "Rescate de flora y fauna",
        "h1": "Rescate y reubicación de flora y fauna en obras y proyectos",
        "title": "Rescate y reubicación de flora y fauna silvestre en obras",
        "descripcion": "Ahuyentamiento, rescate y reubicación de fauna silvestre, y rescate de epífitas y flora en veda antes y durante la remoción de vegetación, con biólogos en campo e informes para la autoridad.",
        "resumen": "Ahuyentamiento y reubicación de fauna, y rescate de epífitas y especies en veda antes de que entre la maquinaria.",
        "tipo": "Rescate y reubicación de flora y fauna silvestre",
        "principal": True,
        "lead": "Antes de que entre la maquinaria, hay que retirar del frente de obra a los animales y a las plantas que la licencia o el permiso ordenan proteger. Hacemos ese trabajo con biólogos y forestales en campo, y lo documentamos para el informe de cumplimiento.",
        "cuerpo": """
      <h2>Fauna silvestre</h2>
      <ul class="lista">
        <li>Recorridos previos para identificar refugios, nidos y madrigueras.</li>
        <li>Ahuyentamiento antes y durante la tala y el descapote.</li>
        <li>Captura y manipulación por profesionales, solo cuando el ahuyentamiento no basta.</li>
        <li>Reubicación en áreas receptoras con hábitat similar, fuera del alcance de la obra.</li>
        <li>Remisión de individuos heridos al centro de atención de fauna de la autoridad ambiental.</li>
      </ul>

      <h2>Flora</h2>
      <ul class="lista">
        <li>Identificación y marcación de epífitas, como orquídeas, bromelias, musgos y líquenes, y de especies en veda o amenazadas.</li>
        <li>Rescate de epífitas, plántulas, brinzales y semillas.</li>
        <li>Traslado a árboles hospederos o a vivero temporal, y seguimiento de su supervivencia.</li>
      </ul>

      <h2>Qué entregamos</h2>
      <p>El plan de rescate, los registros fotográficos georreferenciados, la base de datos de individuos rescatados y reubicados, y los informes para el ICA.</p>

      <h2>Marco normativo</h2>
      <p>Las medidas de rescate las impone la autoridad en la licencia o el permiso, dentro del plan de manejo ambiental. Para la flora en veda, como la veda nacional de musgos, líquenes, orquídeas y bromelias de la Resolución 0213 de 1977, el Decreto-Ley 2106 de 2019 eliminó el trámite separado de levantamiento de veda: las medidas de conservación se fijan dentro del mismo trámite.</p>""",
        "faq": [
            ("¿Cuándo se hace el rescate de fauna y flora?",
             "Antes de remover la cobertura vegetal y acompañando el frente de tala y descapote, para que ningún individuo quede en el área cuando entra la maquinaria."),
            ("¿A dónde se llevan los animales rescatados?",
             "A áreas receptoras definidas en el plan, con hábitat similar y fuera del alcance de la obra. Los individuos heridos se remiten al centro de atención de fauna de la autoridad ambiental."),
            ("¿Necesito un trámite aparte para intervenir epífitas en veda?",
             "No. Desde el Decreto-Ley 2106 de 2019 la autoridad fija las medidas de manejo dentro de la misma licencia, permiso o autorización. Nosotros las ejecutamos y las documentamos."),
            ("¿Qué recibe la empresa al final?",
             "Un informe con la base de datos de individuos rescatados y reubicados, registros fotográficos georreferenciados y los indicadores para el informe de cumplimiento ambiental."),
        ],
        "guia": None,
        "wa": "Hola Metabosques, necesito rescate y reubicación de flora y fauna para una obra.",
    },
    {
        "slug": "restauracion-ecologica",
        "nombre": "Restauración ecológica",
        "h1": "Restauración ecológica con especies nativas en toda Colombia",
        "title": "Restauración ecológica con especies nativas en Colombia",
        "descripcion": "Restauración activa, pasiva y enriquecimiento con especies nativas para compensaciones, inversión del 1 % y metas voluntarias: diagnóstico, diseño, vivero, siembra, mantenimiento y monitoreo.",
        "resumen": "Diagnóstico, diseño, vivero, siembra con especies nativas, mantenimiento y monitoreo con indicadores.",
        "tipo": "Restauración ecológica",
        "principal": True,
        "lead": "Restaurar es devolverle a un área degradada la estructura y las funciones de su ecosistema de referencia. Lo hacemos de punta a punta: diagnóstico, diseño, material vegetal nativo, siembra con mano de obra local, mantenimiento y monitoreo con indicadores. Llevamos 250 hectáreas restauradas y 120.000 árboles sembrados.",
        "cuerpo": """
      <h2>Estrategias que usamos</h2>
      <ul class="lista">
        <li><strong>Restauración activa:</strong> siembra de especies nativas del ecosistema de referencia.</li>
        <li><strong>Restauración pasiva:</strong> aislamiento y retiro de los factores que impiden la regeneración natural, como el ganado o el fuego.</li>
        <li><strong>Enriquecimiento:</strong> siembra de especies que faltan en bosques y rastrojos degradados.</li>
        <li><strong>Núcleos de regeneración y perchas</strong> para atraer aves y acelerar la llegada de semillas.</li>
      </ul>

      <h2>Para qué obligaciones sirve</h2>
      <ul class="lista">
        <li>Planes de compensación por pérdida de biodiversidad.</li>
        <li>Compensaciones de aprovechamientos forestales.</li>
        <li>Inversión forzosa del 1 % en la cuenca.</li>
        <li>Metas voluntarias de carbono y biodiversidad.</li>
      </ul>

      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Diagnóstico del área y definición del ecosistema de referencia.</li>
        <li>Diseño de la intervención con especies, densidades y arreglos.</li>
        <li>Producción en vivero o selección de material vegetal nativo.</li>
        <li>Siembra con mano de obra local, aislamientos y mantenimientos.</li>
        <li>Monitoreo de supervivencia, crecimiento, cobertura y regeneración natural.</li>
        <li>Informes de cumplimiento para la autoridad ambiental.</li>
      </ul>
      <p>Hemos trabajado en franjas costeras, humedales y sabanas, y llevamos el equipo a cualquier región del país.</p>""",
        "faq": [
            ("¿Cuánto dura un proyecto de restauración?",
             "Incluye el establecimiento y varios años de mantenimiento y monitoreo. El plazo exacto lo fijan el plan aprobado o la obligación que se cumple; lo definimos contigo desde la cotización."),
            ("¿Usan solo especies nativas?",
             "Sí. Elegimos las especies del ecosistema de referencia del lugar y priorizamos material de procedencia local."),
            ("¿Cómo se demuestra que la restauración funciona?",
             "Con indicadores medidos en campo: supervivencia, crecimiento, cobertura, regeneración natural y diversidad. Los reportamos en los informes de cumplimiento."),
            ("¿Puedo usar la restauración para cumplir una compensación o la inversión del 1 %?",
             "Sí. La restauración es una de las acciones principales tanto en los planes de compensación como en la inversión forzosa del 1 %."),
        ],
        "guia": "como-calcular-compensacion-resolucion-305",
        "wa": "Hola Metabosques, quiero cotizar un proyecto de restauración ecológica.",
    },
    {
        "slug": "seguimiento-ambiental",
        "nombre": "Seguimiento ambiental",
        "h1": "Seguimiento ambiental e informes de cumplimiento ambiental (ICA)",
        "title": "Seguimiento ambiental e informes de cumplimiento ambiental (ICA)",
        "descripcion": "Seguimiento a licencias, permisos y planes de manejo: matriz de obligaciones, ICA, monitoreos de fauna y flora, cartografía para la autoridad y respuesta a requerimientos.",
        "resumen": "Control de obligaciones, monitoreos e informes de cumplimiento ambiental (ICA) completos y a tiempo.",
        "tipo": "Seguimiento ambiental",
        "principal": True,
        "lead": "Obtener la licencia es la mitad del camino; cumplirla y demostrarlo es la otra mitad. Llevamos el control de tus obligaciones ambientales, hacemos los monitoreos y preparamos los informes de cumplimiento ambiental (ICA) para que lleguen completos y a tiempo.",
        "cuerpo": """
      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Matriz de obligaciones de la licencia, los permisos, la compensación y la inversión del 1 %, con responsables y fechas.</li>
        <li>Calendario de reportes y alertas de vencimientos.</li>
        <li>Monitoreos de fauna y flora, incluido fototrampeo, y apoyo en monitoreos de agua.</li>
        <li>Informes de cumplimiento ambiental (ICA) en los formatos de la autoridad, con su soporte cartográfico.</li>
        <li>Atención de visitas de seguimiento y respuesta a requerimientos.</li>
        <li>Seguimiento al avance de compensaciones e inversión del 1 %.</li>
      </ul>

      <h2>Por qué importa</h2>
      <p>La autoridad ambiental hace control y seguimiento a los proyectos licenciados según el Decreto 1076 de 2015. Un incumplimiento puede dar lugar a medidas preventivas y sanciones bajo la Ley 1333 de 2009, modificada por la Ley 2387 de 2024. Un ICA completo y bien soportado es la mejor defensa del proyecto.</p>""",
        "faq": [
            ("¿Cada cuánto se presenta el ICA?",
             "Con la periodicidad que fije la licencia o el acto administrativo del proyecto. En los planes de compensación, la Resolución 305 de 2026 exige monitoreo al menos una vez al año."),
            ("¿Pueden hacer el seguimiento de un proyecto que ya está en marcha?",
             "Sí. Empezamos con un diagnóstico del estado de cumplimiento de cada obligación y armamos el plan para ponerse al día."),
            ("¿Qué pasa si no se cumple una obligación?",
             "La autoridad puede imponer medidas preventivas y sanciones según la Ley 1333 de 2009, modificada por la Ley 2387 de 2024. Por eso conviene detectar los atrasos antes de la visita de seguimiento."),
        ],
        "guia": None,
        "wa": "Hola Metabosques, necesito apoyo con el seguimiento ambiental y los ICA de un proyecto.",
    },
    # ---- servicios complementarios ----
    {
        "slug": "consultoria-ambiental",
        "nombre": "Consultoría ambiental",
        "h1": "Consultoría ambiental: estudios de impacto, planes de manejo y SIG",
        "title": "Consultoría ambiental en Colombia: EIA, planes de manejo y SIG",
        "descripcion": "Estudios de impacto ambiental, planes de manejo, caracterización de fauna y flora y cartografía SIG para licencias y permisos ambientales en toda Colombia.",
        "resumen": "Estudios de impacto, planes de manejo, caracterización biótica y cartografía SIG.",
        "tipo": "Consultoría ambiental",
        "principal": False,
        "lead": "Acompañamos a empresas y entidades desde la línea base hasta la obtención de licencias y permisos ambientales, con trabajo de campo propio y análisis espacial.",
        "cuerpo": """
      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Estudios de impacto ambiental (EIA) y planes de manejo ambiental.</li>
        <li>Caracterización de fauna y flora, incluido fototrampeo con cámaras trampa.</li>
        <li>Cartografía y análisis espacial en sistemas de información geográfica (SIG).</li>
        <li>Solicitudes de licencias, permisos y sus modificaciones.</li>
        <li>Respuesta a requerimientos de la autoridad ambiental.</li>
      </ul>""",
        "faq": [
            ("¿Hacen el trabajo de campo o solo los documentos?",
             "Ambos. Hacemos los muestreos de fauna y flora en campo y elaboramos los estudios y la cartografía."),
            ("¿Trabajan con la ANLA y con las corporaciones?",
             "Sí. Preparamos la información según los términos de referencia de la autoridad que evalúa el trámite."),
        ],
        "guia": None,
        "wa": "Hola Metabosques, necesito una consultoría ambiental.",
    },
    {
        "slug": "mantenimiento-obras-ambientales",
        "nombre": "Mantenimiento y obras ambientales",
        "h1": "Mantenimiento de áreas de compensación y obras ambientales",
        "title": "Mantenimiento de áreas de compensación y obras ambientales en Colombia",
        "descripcion": "Mantenimiento de áreas verdes y de compensación, rocería, revegetalización, limpieza de paneles solares y obras civiles menores con criterio paisajístico.",
        "resumen": "Rocería, revegetalización, limpieza de paneles solares y obras civiles menores.",
        "tipo": "Mantenimiento ambiental",
        "principal": False,
        "lead": "Una siembra o una zona verde sin mantenimiento se pierde. Ofrecemos cuadrillas con supervisión técnica para conservar las áreas establecidas y la infraestructura asociada.",
        "cuerpo": """
      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Rocería y control de competencia en zonas de compensación y áreas verdes.</li>
        <li>Revegetalización de taludes y áreas intervenidas.</li>
        <li>Limpieza de paneles solares en parques fotovoltaicos.</li>
        <li>Obras civiles menores con criterio paisajístico.</li>
        <li>Registro fotográfico y reporte de cada intervención.</li>
      </ul>""",
        "faq": [
            ("¿Con qué frecuencia hacen el mantenimiento?",
             "La programamos según el clima, el crecimiento de cada zona y lo que exija la obligación ambiental."),
            ("¿Trabajan en parques solares en operación?",
             "Sí: rocería, control de vegetación y limpieza de paneles, con reportes de cada visita."),
        ],
        "guia": None,
        "wa": "Hola Metabosques, quiero cotizar mantenimiento de áreas verdes o de compensación.",
    },
    {
        "slug": "naturaunidad",
        "nombre": "NaturaUnidad",
        "h1": "NaturaUnidad: soluciones basadas en la naturaleza para carbono y biodiversidad",
        "title": "NaturaUnidad: soluciones basadas en la naturaleza en Colombia",
        "descripcion": "Soluciones basadas en la naturaleza para metas corporativas de carbono y biodiversidad, con línea base, indicadores verificables y reportes de sostenibilidad.",
        "resumen": "Proyectos voluntarios de restauración con indicadores verificables de carbono y biodiversidad.",
        "tipo": "Soluciones basadas en la naturaleza",
        "principal": False,
        "lead": "NaturaUnidad es nuestra línea para empresas que quieren ir más allá de la obligación legal: proyectos de restauración voluntaria con resultados que se pueden medir y reportar.",
        "cuerpo": """
      <h2>Qué incluye</h2>
      <ul class="lista">
        <li>Línea base de biodiversidad del área del proyecto.</li>
        <li>Diseño de la intervención de restauración con especies nativas.</li>
        <li>Indicadores verificables de carbono y biodiversidad.</li>
        <li>Seguimiento en campo y reportes para informes de sostenibilidad.</li>
      </ul>""",
        "faq": [
            ("¿En qué se diferencia de una compensación?",
             "La compensación es una obligación legal; NaturaUnidad es voluntaria y responde a metas propias de la empresa de carbono, biodiversidad o sostenibilidad."),
            ("¿Cómo se reportan los resultados?",
             "Con una línea base y indicadores medidos en campo, que se pueden incluir en los informes de sostenibilidad de la empresa."),
        ],
        "guia": None,
        "wa": "Hola Metabosques, quiero información sobre NaturaUnidad.",
    },
]

# Redirecciones de las URL publicadas antes (servicios/<viejo>/ -> /<nuevo>)
REDIRECCIONES = {
    "servicios/restauracion-ecologica-compensaciones": "restauracion-ecologica",
    "servicios/aprovechamiento-forestal": "aprovechamiento-forestal",
    "servicios/consultoria-ambiental": "consultoria-ambiental",
    "servicios/mantenimiento-obras-ambientales": "mantenimiento-obras-ambientales",
    "servicios/naturaunidad": "naturaunidad",
}
