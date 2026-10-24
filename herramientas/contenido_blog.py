"""Guías del blog. 'cuerpo' es HTML que se inserta tal cual. Fechas en formato AAAA-MM-DD."""

AVISO = "Esta guía es informativa y no reemplaza la lectura de la norma ni la asesoría jurídica para tu caso. Fecha de revisión: {fecha}."

GUIAS = [
    {
        "slug": "como-calcular-compensacion-resolucion-305",
        "corto": "Cómo calcular una compensación",
        "titulo": "¿Cómo calcular una compensación con la Resolución 305 de 2026?",
        "title": "Cómo calcular una compensación por pérdida de biodiversidad con la Res. 305 de 2026",
        "descripcion": "Guía paso a paso para calcular el área a compensar con el nuevo manual de compensación del medio biótico (Resolución 305 de 2026): factores, ajuste por ubicación, ejemplo y transición.",
        "resumen": "Factores por ecosistema, ajuste por ubicación, un ejemplo con números y lo que debes saber del régimen de transición.",
        "fecha": "2026-10-24",
        "servicio": "compensacion-perdida-biodiversidad",
        "cuerpo": """
      <p>El 7 de abril de 2026 el Ministerio de Ambiente expidió la Resolución 0305, que adoptó la actualización del <em>Manual para la Compensación del Medio Biótico y de la Sustracción de Áreas de Reserva Forestal</em>. Se publicó en el Diario Oficial el 15 de abril de 2026, rige desde esa fecha y derogó la Resolución 256 de 2018. Si tu proyecto tiene licencia ambiental, un permiso de aprovechamiento forestal único o una sustracción de reserva forestal, así se calcula hoy lo que debes compensar.</p>

      <h2>Antes de empezar: ¿te aplica?</h2>
      <p>El manual aplica a tres trámites:</p>
      <ul class="lista">
        <li>Proyectos sujetos a licencia ambiental.</li>
        <li>Sustracciones temporales o definitivas de reservas forestales nacionales o regionales.</li>
        <li>Permisos de aprovechamiento forestal único, incluidos ahora los de plantaciones protectoras y protectoras-productoras.</li>
      </ul>
      <p>Quedan por fuera las compensaciones abióticas y socioeconómicas, los ecosistemas marino-costeros, el manejo de flora en veda y el aprovechamiento de árboles aislados. Este último se atiende con reposición de individuos, en la proporción que defina la autoridad.</p>

      <h2>Paso 1. Mide el área impactada por ecosistema</h2>
      <p>Con la cartografía del proyecto, separa el área que vas a intervenir según el tipo de cobertura y ecosistema: natural, vegetación secundaria o de transición, y transformado (pastos, cultivos, áreas intervenidas). El cálculo se hace por separado para cada uno.</p>

      <h2>Paso 2. Asigna el factor de compensación</h2>
      <p>Cada ecosistema tiene un factor que refleja qué tan valioso y escaso es. El manual de 2026 cambió los rangos:</p>
      <div class="tabla-wrap"><table class="tabla">
        <thead><tr><th scope="col">Tipo de ecosistema</th><th scope="col">Factor (manual 2026)</th></tr></thead>
        <tbody>
          <tr><td>Natural</td><td>4 a 10</td></tr>
          <tr><td>Vegetación secundaria o de transición</td><td>2 a 5</td></tr>
          <tr><td>Transformado</td><td>1 (puede subir si está en la matriz de un ecosistema estratégico)</td></tr>
        </tbody>
      </table></div>
      <p>El valor exacto para cada ecosistema sale de los anexos del manual. En el manual de 2018 todos los ecosistemas se movían en un solo rango de 1 a 10.</p>
      <p>Para los ecosistemas transformados hay que elegir un ecosistema de referencia. El orden de prioridad es:</p>
      <ol class="lista">
        <li>El del bioma con mayor área impactada por el proyecto.</li>
        <li>El que dé el factor de compensación más alto.</li>
        <li>Los ecosistemas relictuales del paisaje.</li>
      </ol>

      <h2>Paso 3. Ajusta el factor según dónde vas a compensar</h2>
      <p>Esta es una de las novedades más importantes: compensar lejos cuesta más área. Al factor base (FC) se le suma un valor según la ubicación de la compensación:</p>
      <div class="tabla-wrap"><table class="tabla">
        <thead><tr><th scope="col">Dónde se compensa</th><th scope="col">Factor que aplica</th></tr></thead>
        <tbody>
          <tr><td>Área de influencia del proyecto</td><td>FC</td></tr>
          <tr><td>Misma subzona hidrográfica</td><td>FC + 0,3</td></tr>
          <tr><td>Misma zona hidrográfica</td><td>FC + 0,6</td></tr>
          <tr><td>Área de influencia o subzona hidrográfica, pero en otro bioma</td><td>FC + 0,9</td></tr>
          <tr><td>Áreas protegidas en cualquier lugar del país</td><td>FC + 1,2</td></tr>
        </tbody>
      </table></div>

      <h2>Paso 4. Multiplica y suma</h2>
      <p class="formula">Área a compensar = Σ (área impactada de cada ecosistema × su factor ajustado)</p>
      <p>La fórmula general es la misma del manual anterior; lo que cambia son los factores. En los aprovechamientos forestales únicos el factor ahora varía según cada tipo de cobertura presente.</p>

      <h2>Un ejemplo con números</h2>
      <p>Un parque solar va a intervenir 12 hectáreas: 2 ha de bosque de galería, 4 ha de vegetación secundaria y 6 ha de pastos. Para el ejemplo supondremos factores de 7, 3 y 1. <strong>Son valores ilustrativos;</strong> los reales salen de los anexos del manual para el ecosistema de tu proyecto.</p>
      <div class="tabla-wrap"><table class="tabla">
        <thead><tr><th scope="col">Ecosistema</th><th scope="col">Área (ha)</th><th scope="col">En el área de influencia</th><th scope="col">En la misma subzona hidrográfica (+0,3)</th></tr></thead>
        <tbody>
          <tr><td>Bosque de galería</td><td>2</td><td>2 × 7 = 14</td><td>2 × 7,3 = 14,6</td></tr>
          <tr><td>Vegetación secundaria</td><td>4</td><td>4 × 3 = 12</td><td>4 × 3,3 = 13,2</td></tr>
          <tr><td>Pastos</td><td>6</td><td>6 × 1 = 6</td><td>6 × 1,3 = 7,8</td></tr>
          <tr><th scope="row">Total</th><td>12</td><td><strong>32 ha</strong></td><td><strong>35,6 ha</strong></td></tr>
        </tbody>
      </table></div>
      <p>Si en el área de influencia no hay predios disponibles, compensar en la misma subzona hidrográfica sube la obligación en 3,6 hectáreas. Por eso conviene buscar áreas cercanas desde el inicio.</p>

      <h2>Paso 5. Define qué hacer en el área</h2>
      <p>El plan debe responder qué, cuánto, dónde y cómo compensar, con el objetivo de no tener pérdida neta de biodiversidad. Las acciones principales son la preservación y la restauración. El manual también reconoce las comunidades energéticas como mecanismo, y en las sustracciones el uso sostenible puede complementar el plan, pero no sustituirlo. Además, el plan debe incluir:</p>
      <ul class="lista">
        <li>Zonificación de las áreas potenciales a escala 1:25.000 o más detallada.</li>
        <li>Un análisis de adicionalidad que compare el escenario actual con el escenario con las medidas.</li>
        <li>Evidencia de participación de las comunidades del área de influencia.</li>
        <li>Objetivos, metas, indicadores y cronograma.</li>
      </ul>

      <h2>Paso 6. Presenta, ejecuta y reporta</h2>
      <ul class="lista">
        <li><strong>Cuándo se presenta:</strong> con la solicitud de la licencia o del permiso. En las sustracciones, dentro de los seis meses siguientes a la ejecutoria del acto que la otorga.</li>
        <li><strong>Qué aprueba la autoridad:</strong> la zonificación de áreas potenciales, no los predios. Los predios concretos se reportan en los informes de cumplimiento ambiental (ICA).</li>
        <li><strong>Ajustes:</strong> los requerimientos de ajuste se atienden dentro de los seis meses siguientes a la firmeza del acto.</li>
        <li><strong>Compensación anticipada:</strong> puedes empezar a compensar antes del impacto si el plan completo está aprobado.</li>
        <li><strong>Monitoreo:</strong> al menos una vez al año.</li>
        <li><strong>Cambios mayores:</strong> modificar la zonificación, los objetivos, las metas, los indicadores o el plazo total requiere aprobación de la autoridad.</li>
      </ul>

      <h2>Régimen de transición</h2>
      <ul class="lista">
        <li><strong>Solicitudes radicadas en los tres meses siguientes a la entrada en vigencia:</strong> podían pedir expresamente que se les aplicara la Resolución 256 de 2018. Si no lo pidieron, aplica el manual nuevo.</li>
        <li><strong>Trámites que ya estaban en curso:</strong> siguen con la norma anterior, con 12 meses para acogerse voluntariamente al manual nuevo presentando un plan modificado.</li>
        <li><strong>Planes que ya se estaban ejecutando:</strong> siguen con su instrumento original y tienen la misma opción de 12 meses para acogerse.</li>
        <li><strong>Proyectos con licencia, permiso o sustracción pero sin plan aprobado:</strong> deben presentarlo en un plazo de seis meses.</li>
      </ul>
      <p>Acogerse al manual nuevo puede reducir o aumentar el área según tu caso. Vale la pena hacer el cálculo con las dos normas antes de decidir.</p>

      <h2>Errores frecuentes</h2>
      <ul class="lista">
        <li>Calcular con un solo factor para todo el proyecto en lugar de hacerlo por ecosistema.</li>
        <li>Olvidar el ajuste por ubicación cuando la compensación queda fuera del área de influencia.</li>
        <li>Presentar predios sin zonificación a la escala exigida ni análisis de adicionalidad.</li>
        <li>Dejar pasar los plazos de transición sin evaluar si conviene acogerse.</li>
      </ul>""",
        "fuentes": [
            ("Resolución 305 de 2026, Ministerio de Ambiente y Desarrollo Sostenible", "https://www.minambiente.gov.co/documento-normativa/resolucion-305-de-2026/"),
            ("Resolución 0305 de 2026 en el centro de documentación de la ANLA", "https://www.anla.gov.co/wanla/eureka/normativa/resoluciones/resolucion-0305-de-2026-actualizacion-del-manual-para-la-compensacion-del-medio-biotico-y-de-la-sustraccion-de-areas-de-reserva-forestal"),
            ("Comparación entre los manuales de compensación de 2018 y 2026, Holland & Knight", "https://www.hklaw.com/en/insights/publications/2026/04/comparacion-entre-manuales-de-compensacion-del-componente-biotico"),
        ],
    },
    {
        "slug": "inversion-forzosa-1-por-ciento-como-se-cumple",
        "corto": "Inversión forzosa del 1 %: cómo se cumple",
        "titulo": "¿Qué es la inversión forzosa del 1 % y cómo se cumple?",
        "title": "Inversión forzosa del 1 %: qué es, quién debe hacerla y cómo se cumple",
        "descripcion": "Guía práctica sobre la inversión forzosa de no menos del 1 % en Colombia: quién está obligado, cómo se liquida, en qué se puede invertir, plazos del plan de inversión y actualización anual.",
        "resumen": "Quién está obligado, cómo se liquida, en qué se puede invertir y los plazos del plan de inversión.",
        "fecha": "2026-10-24",
        "servicio": "inversion-forzosa-1-por-ciento",
        "cuerpo": """
      <p>La inversión forzosa del 1 % es una obligación que nace del parágrafo del artículo 43 de la Ley 99 de 1993. Exige que los proyectos licenciados que usan agua tomada directamente de la naturaleza devuelvan a la cuenca al menos el 1 % de su inversión, en acciones de recuperación, preservación y conservación. Hoy está reglamentada en el Decreto 1076 de 2015, con los cambios de los Decretos 2099 de 2016 y 075 de 2017.</p>

      <h2>1. ¿Estás obligado?</h2>
      <p>La obligación aplica solo si se cumplen todas estas condiciones al mismo tiempo:</p>
      <ul class="lista">
        <li>El proyecto requiere licencia ambiental.</li>
        <li>Capta agua directamente de una fuente natural, superficial o subterránea.</li>
        <li>Usa esa agua en cualquier etapa: construcción u operación.</li>
        <li>La usa para cualquier actividad: consumo humano, riego, procesos industriales u otra.</li>
      </ul>
      <p>Según un concepto del Ministerio de Ambiente de 2025, un proyecto que recibe el agua de un acueducto o de otro prestador no está obligado. Las modificaciones de licencia que aumentan el uso de agua o agregan fuentes generan una obligación adicional, que se liquida sobre la inversión de esa modificación.</p>

      <h2>2. Cómo se liquida</h2>
      <ul class="lista">
        <li><strong>Base:</strong> la inversión total del proyecto licenciado, es decir, el capital invertido en las etapas previas a la producción, con los activos fijos y los costos para desarrollar el proyecto.</li>
        <li><strong>Valor:</strong> no menos del 1 % de esa base.</li>
        <li><strong>Soporte:</strong> la liquidación se presenta en pesos, discriminada por partidas contables y certificada por contador público o revisor fiscal.</li>
      </ul>
      <p>Los proyectos licenciados antes de la reglamentación actual tienen reglas de transición propias, así que vale la pena revisar el caso concreto.</p>

      <h2>3. En qué se puede invertir</h2>
      <p>Si la cuenca tiene un Plan de Ordenación y Manejo (POMCA) adoptado, el dinero puede ir a:</p>
      <ul class="lista">
        <li>Restauración ecológica, rehabilitación y recuperación, incluidos proyectos de uso sostenible: forestales, agroforestales y silvopastoriles.</li>
        <li>Interceptores y sistemas de tratamiento de aguas residuales domésticas en municipios de categorías 4, 5 y 6, siempre que la entidad territorial garantice su operación.</li>
        <li>Monitoreo del recurso hídrico con estaciones hidrometeorológicas o radares, con la tecnología que defina el IDEAM.</li>
      </ul>
      <p>Como acción complementaria se pueden comprar predios o mejoras en áreas de interés estratégico para la conservación. Si la cuenca no tiene POMCA, una parte puede destinarse a formularlo. Hasta el 10 % del valor de una actividad puede ir a estudios y diseños, y se pueden usar mecanismos como el pago por servicios ambientales, los acuerdos de conservación y los bancos de hábitat.</p>
      <p>No cuentan como inversión del 1 % las obligaciones que ya están en el plan de manejo ambiental del proyecto, como la prevención, la mitigación, la corrección o la compensación.</p>

      <h2>4. Dónde se invierte</h2>
      <p>El orden es este: primero la subzona hidrográfica donde está el proyecto y, con justificación técnica, la zona hidrográfica. Los proyectos lineales, como vías o líneas de transmisión, pueden repartir la inversión entre las subzonas o zonas que atraviesan. También se puede invertir en áreas protegidas del SINAP dentro de ese ámbito, si la actividad es compatible con su categoría de manejo.</p>

      <h2>5. Plazos del trámite</h2>
      <ol class="lista">
        <li><strong>Con el estudio de impacto ambiental:</strong> se proponen las líneas generales de inversión y el ámbito geográfico. La autoridad las aprueba en la licencia. Si evalúa la ANLA, pide concepto a las corporaciones con jurisdicción.</li>
        <li><strong>Durante la construcción:</strong> se pueden presentar planes parciales, de al menos el 1 % de lo invertido hasta ese momento.</li>
        <li><strong>Seis meses después de terminar la construcción y el montaje:</strong> se presenta el plan de inversión con las acciones específicas y la liquidación, en el formato del Ministerio. La autoridad tiene 30 días hábiles para pronunciarse.</li>
        <li><strong>Ejecución:</strong> empieza después de iniciar la captación de agua.</li>
        <li><strong>Cada año:</strong> el saldo no ejecutado se actualiza con el IPC, con corte al 31 de diciembre, y se reporta antes del 31 de marzo siguiente.</li>
      </ol>
      <p>El plan se puede modificar en cualquier momento sin modificar la licencia. Y si una modificación posterior aumenta el uso de agua, hay que adicionar la inversión.</p>

      <h2>6. Cómo hacer que la inversión sí se ejecute</h2>
      <p>El atraso más común no está en aprobar el plan, sino en ejecutarlo. Estas prácticas ayudan:</p>
      <ul class="lista">
        <li>Concertar desde el principio con la corporación, los municipios y las comunidades de la cuenca.</li>
        <li>Identificar los predios y verificar su situación jurídica antes de comprometer acciones.</li>
        <li>Preferir acciones que se puedan medir: hectáreas restauradas, predios conservados, estaciones operando.</li>
        <li>Llevar el control del saldo y de su actualización anual junto con los ICA.</li>
      </ul>""",
        "fuentes": [
            ("Decreto 2099 de 2016 (inversión forzosa del 1 %), texto en la CRA", "https://normas.cra.gov.co/gestor/docs/decreto_2099_2016.htm"),
            ("Concepto del Ministerio de Ambiente sobre el plan de inversión forzosa del 1 % (2025)", "https://www.minambiente.gov.co/wp-content/uploads/2025/08/concep_250617_020652-–-ALCANCE-E-INTERPRETACION-PLAN-DE-INVERSION-FORZOSA-1-REGULADO-L-99-93-Y-D-2099-16.pdf"),
            ("Decreto 075 de 2017", "https://www.dmsjuridica.com/buscador_20179478954/legislacion/decretos/2023/08/16/decreto-75-de-2017/?pdf=50426"),
        ],
    },
    {
        "slug": "permiso-aprovechamiento-forestal-car-paso-a-paso",
        "corto": "Permiso de aprovechamiento forestal, paso a paso",
        "titulo": "Permisos de aprovechamiento forestal ante la CAR, paso a paso",
        "title": "Permiso de aprovechamiento forestal ante la CAR: guía paso a paso",
        "descripcion": "Cómo tramitar un permiso de aprovechamiento forestal único ante la corporación autónoma regional: qué revisar antes, inventario, plan de aprovechamiento, documentos, evaluación, salvoconductos y compensación.",
        "resumen": "Qué revisar antes, inventario, plan de aprovechamiento, documentos, evaluación, salvoconductos y compensación.",
        "fecha": "2026-10-24",
        "servicio": "aprovechamiento-forestal",
        "cuerpo": """
      <p>Talar vegetación natural para construir un parque solar, una vía, una línea de transmisión o cualquier obra requiere autorización de la autoridad ambiental. Cuando el proyecto no tiene licencia ambiental, esa autorización es un permiso de aprovechamiento forestal que se pide a la corporación autónoma regional (CAR) o a la autoridad ambiental urbana del lugar. Este es el camino, paso a paso.</p>

      <h2>Paso 0. Confirma qué trámite necesitas</h2>
      <ul class="lista">
        <li><strong>Si el proyecto tiene licencia ambiental,</strong> el aprovechamiento forestal se evalúa dentro de la licencia. No se pide un permiso aparte a la CAR.</li>
        <li><strong>Si vas a remover el bosque para darle otro uso al suelo,</strong> el trámite es un aprovechamiento forestal único, que es el caso típico de las obras.</li>
        <li><strong>Si son árboles aislados,</strong> como árboles sueltos en potreros o zonas urbanas, el trámite es el de aprovechamiento de árboles aislados, con reposición de individuos.</li>
        <li><strong>Si vas a aprovechar el bosque y mantenerlo,</strong> el trámite es un aprovechamiento persistente, con plan de manejo.</li>
      </ul>

      <h2>Paso 1. Revisa las restricciones del área</h2>
      <p>Antes de gastar en inventarios, verifica que el área se pueda intervenir. Revisa:</p>
      <ul class="lista">
        <li>Reservas forestales nacionales y regionales, como las de Ley 2.ª de 1959. En algunas de sus zonas no se permiten aprovechamientos únicos sin sustracción previa.</li>
        <li>Áreas protegidas del SINAP y su zonificación.</li>
        <li>Rondas hídricas y la zonificación del POMCA y del plan de ordenamiento territorial.</li>
        <li>Especies en veda o amenazadas que puedan estar en el área.</li>
      </ul>

      <h2>Paso 2. Haz el inventario forestal</h2>
      <p>Cada corporación fija su protocolo en sus términos de referencia. En obras es común el censo de todos los individuos a intervenir. Cuando se acepta muestreo, algunas corporaciones piden un error de muestreo no mayor al 15 % con una probabilidad del 95 %. El inventario debe incluir:</p>
      <ul class="lista">
        <li>La identificación botánica de cada especie y su estado de amenaza o veda.</li>
        <li>Diámetros, alturas y volúmenes por especie.</li>
        <li>La ubicación georreferenciada de los individuos o de las parcelas.</li>
        <li>El inventario de epífitas cuando la autoridad lo exige.</li>
      </ul>

      <h2>Paso 3. Elabora el plan de aprovechamiento forestal</h2>
      <p>Es el documento técnico central. Por lo general incluye:</p>
      <ul class="lista">
        <li>Los objetivos y la justificación, con las especies y los volúmenes a aprovechar.</li>
        <li>La localización con cartografía, los linderos y el área.</li>
        <li>La caracterización biofísica del área y los resultados del inventario.</li>
        <li>El método de aprovechamiento: tala, extracción, transporte, manejo de residuos y sitios de acopio.</li>
        <li>Los impactos y las medidas de manejo.</li>
        <li>La compensación o reposición forestal y el cronograma.</li>
      </ul>

      <h2>Paso 4. Reúne los documentos y radica</h2>
      <p>El Decreto 1076 de 2015 pide que la solicitud incluya:</p>
      <ul class="lista">
        <li>El nombre del solicitante.</li>
        <li>La ubicación del predio, sus linderos y su régimen de propiedad.</li>
        <li>Las especies y los volúmenes a aprovechar, y el uso que se dará a los productos.</li>
        <li>Un mapa del área.</li>
      </ul>
      <p>Para un aprovechamiento único en bosque natural de propiedad privada se suman:</p>
      <ul class="lista">
        <li>Un estudio técnico que demuestre que el suelo tiene mejor aptitud para un uso distinto al forestal.</li>
        <li>Un certificado de tradición del predio reciente.</li>
        <li>El plan de aprovechamiento.</li>
      </ul>
      <p>Si tramitas en nombre de otra persona, agrega el poder o la autorización del propietario. Muchas corporaciones usan el formulario único nacional de solicitud y cobran un valor por la evaluación.</p>

      <h2>Paso 5. Prepara el plan de compensación</h2>
      <p>Para los aprovechamientos únicos aplica el manual de compensación del medio biótico de la Resolución 305 de 2026: el área a compensar se calcula por ecosistema y por ubicación. Presentarlo con la solicitud evita requerimientos y demoras. En nuestra <a href="/blog/como-calcular-compensacion-resolucion-305">guía de la Resolución 305</a> explicamos el cálculo.</p>

      <h2>Paso 6. Evaluación de la corporación</h2>
      <ol class="lista">
        <li>La corporación expide el auto de inicio del trámite y lo publica.</li>
        <li>Hace una visita técnica al predio, a la que conviene asistir con el profesional que hizo el inventario.</li>
        <li>Si falta información, la requiere.</li>
        <li>Emite el concepto técnico y la resolución que otorga o niega el permiso, con sus obligaciones.</li>
      </ol>
      <p>El Decreto 1076 no fija un plazo especial para decidir. Una solicitud completa desde el inicio es lo que más acorta el trámite.</p>

      <h2>Paso 7. Ejecuta y moviliza la madera</h2>
      <ul class="lista">
        <li>Aprovecha solo los individuos y los volúmenes autorizados, con la marcación que exija la corporación.</li>
        <li>Para transportar la madera fuera del predio, tramita el salvoconducto único nacional en línea (Resolución 1909 de 2017).</li>
        <li>Si hay fauna o epífitas, ejecuta antes el ahuyentamiento y el rescate.</li>
      </ul>

      <h2>Paso 8. Cumple y reporta</h2>
      <p>Ejecuta la compensación o la reposición en los plazos de la resolución y entrega los informes de avance que pida la corporación. El incumplimiento puede acarrear medidas preventivas y sanciones bajo la Ley 1333 de 2009, modificada por la Ley 2387 de 2024.</p>

      <h2>Lista de chequeo</h2>
      <ul class="lista">
        <li>Trámite correcto definido: dentro de licencia, único, árboles aislados o persistente.</li>
        <li>Restricciones del área verificadas.</li>
        <li>Inventario según los términos de referencia de la corporación.</li>
        <li>Plan de aprovechamiento con cartografía.</li>
        <li>Documentos del predio y poderes.</li>
        <li>Plan de compensación según la Resolución 305 de 2026.</li>
        <li>Plan de rescate de fauna y flora.</li>
      </ul>""",
        "fuentes": [
            ("Concepto del Ministerio de Ambiente sobre términos de trámites ambientales, incluido el aprovechamiento forestal (2025)", "https://www.minambiente.gov.co/wp-content/uploads/2025/08/concep_250424_013249-TERMINOS-PARA-DAR-RESPUESTA-A-TRAMITES-DE-CARACTER-AMBIENTAL.pdf"),
            ("Términos de referencia para aprovechamiento forestal único en bosque natural, Cornare", "https://www.cornare.gov.co/Tramites-Ambientales/TR/Terminos_Referencia_Aprovechamiento_Forestal_BN_Unico.pdf"),
            ("Intervención de especies en veda en trámites de licenciamiento, ANLA", "https://www.anla.gov.co/01_anla/index.php/noticias/299-tramites-de-licenciamiento-ambiental-que-impliquen-intervencion-de-especies-en-veda"),
            ("Resolución 305 de 2026, Ministerio de Ambiente y Desarrollo Sostenible", "https://www.minambiente.gov.co/documento-normativa/resolucion-305-de-2026/"),
        ],
    },
]
