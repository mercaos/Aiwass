# tarot_data.py
# Base de datos completa del Tarot de Thoth (80 cartas)
# Basado en "Tarot, el espejo del alma" y "El Libro de Thoth" de Crowley

cartas_del_tarot = {
    # ============================================
    # ARCANOS MAYORES (0 - XXI) - 22 CARTAS
    # ============================================
    
    "0. El Loco": {
        "nombre": "0. El Loco",
        "palabras_clave": "Candor, fe, voluntad de arriesgarse, libertad e independencia, creatividad, gran potencial",
        "descripcion": "Estás listo para un nuevo comienzo y tal vez incluso para dar un gran paso hacia delante. Relájate y toma ese primer paso, aunque tus miedos intenten detenerte. Fíate de lo que dice tu corazón. El Loco representa la confianza imperturbable de un ser que vive con el miedo sin sucumbir a él. Es la liberación, la apertura a los sucesos místicos.",
        "pregunta": "¿Por qué sientes que debes cortar todos tus lazos para ser libre? ¿Qué elemento en tu vida actúa como 'el tigre del miedo'? ¿Dónde te lleva el corazón?"
    },
    
    "I. El Mago": {
        "nombre": "I. El Mago",
        "palabras_clave": "Mercurio, comunicación, actitud positiva, flexibilidad, ingenuidad, destreza, habilidad",
        "descripcion": "Tienes excelentes habilidades que deberías compartir con los demás, y una de tus tareas más importantes es encontrar y crear el entorno adecuado para tus actividades y empresas. El Mago representa la voluntad, la sabiduría y la palabra por la que fueron creados los mundos. Con increíble agilidad, hace malabarismos con los distintos instrumentos de comunicación.",
        "pregunta": "¿Cuáles son tus talentos? ¿Con qué medios y en qué marco puedes transmitirlos?"
    },
    
    "I. El Mago (Variante Thoth)": {
        "nombre": "I. El Mago (El Juglar)",
        "palabras_clave": "Mercurio, Sabiduría, Voluntad, la Palabra, Logos, energía irradiada",
        "descripcion": "El Mago es el portador de la Vara, la energía irradiada. Representa la Sabiduría, la Voluntad, la Palabra, el Logos por medio del cual son creados los mundos. Es la voluntad en el acto de manifestación. Es la creación continua, la ley de la razón, la esencia de la Palabra. En su dualidad, representa la verdad y la falsedad, trastorna toda idea establecida.",
        "pregunta": "¿Cómo estás usando tu poder creativo? ¿Eres consciente de tu palabra y su impacto?"
    },
    
    "II. La Sacerdotisa": {
        "nombre": "II. La Sacerdotisa",
        "palabras_clave": "Luna, acceso a los poderes intuitivos, curación, independencia, estabilidad interior, autoconfianza",
        "descripcion": "Tienes la capacidad de contactar con tus poderes intuitivos. Deberías esforzarte por desarrollarlos al máximo. Cuida tu independencia. La Sacerdotisa está en contacto con su capacidad intuitiva y puede fiarse totalmente de ella. La receptividad y la habilidad para escuchar su propia voz interior se manifiestan en su responsabilidad y autoconfianza.",
        "pregunta": "¿Existe alguna esfera de tu vida en la que permites que influyan otras personas y en la que no confías en tu propio conocimiento de la verdad interior?"
    },
    
    "III. La Emperatriz": {
        "nombre": "III. La Emperatriz",
        "palabras_clave": "Venus, belleza, amor, instinto maternal, feminidad, sabiduría, conexión espíritu-materia",
        "descripcion": "La belleza por la que te atrae otra persona está dentro de ti. Ya sea hombre o mujer, te encuentras actualmente en un proceso de desarrollo y realización de tus aspectos femeninos. Se te ofrece la posibilidad de entender y resolver los conflictos no resueltos con figuras maternales. La Emperatriz irradia armonía y su fuerza radica en la sinergia entre los ideales espirituales y la expresión terrenal.",
        "pregunta": "¿Hay una mujer fuerte en tu vida de la que querrías aprender?"
    },
    
    "IV. El Emperador": {
        "nombre": "IV. El Emperador",
        "palabras_clave": "Aries, pionero, descubridor, líder, iniciador, sabiduría creativa, autoridad",
        "descripcion": "Es el momento oportuno para un cambio o un nuevo comienzo. Confía en tu poder. El Emperador representa el comienzo de un nuevo proyecto o una nueva fase en la vida. En el mundo exterior, podría significar el inicio de un proyecto prometedor, cambios profesionales, viajes o paternidad. En el mundo interior, nuevas ideas o una experiencia dramática de autodescubrimiento.",
        "pregunta": "¿Qué necesitas cambiar en tu vida? ¿Hay algo que quieras cambiar?"
    },
    
    "V. El Hierofante": {
        "nombre": "V. El Hierofante",
        "palabras_clave": "Tauro, maestro espiritual, consejero, confidente, guía interior, transformación máxima",
        "descripcion": "La búsqueda de uno mismo lleva a zonas espirituales. Esta carta puede señalar al advenimiento de un maestro o guía espiritual. Debes estar preparado para acogerlo. El Hierofante ha reunido todos los elementos dentro de sí y los ha desarrollado al máximo. Describe a alguien que ha sido consagrado, perfecto e inspirado, la encarnación de lo divino.",
        "pregunta": "¿Alguna vez te has sentido atraído por las enseñanzas de un maestro de la verdad (en el pasado o en el presente)?"
    },
    
    "VI. Los Amantes": {
        "nombre": "VI. Los Amantes",
        "palabras_clave": "Géminis, amor, atracción, reconciliación, unión de los opuestos en el amor",
        "descripcion": "Esta carta puede señalar una relación de amor maravillosa y emocionante. Las relaciones existentes se estrechan o se disuelven. En la atención y la confrontación con compañeros o grupos se vuelven aparentes nuevos caminos hacia el desarrollo personal y la integración de los propios principios. Buscamos en el otro aquello de lo que carecemos.",
        "pregunta": "¿Qué buscas en la persona que amas? ¿Qué constituye para ti una relación amorosa plenamente satisfactoria?"
    },
    
    "VII. El Carro": {
        "nombre": "VII. El Carro",
        "palabras_clave": "Cáncer, nuevos comienzos, cambio a mejor, introspección, meditación, camino espiritual",
        "descripcion": "Un cambio inminente promete una feliz mejora en tu vida. Prepárate y controla tus relaciones actuales. Dejarás atrás algunas de ellas. No hay que precipitarse al tomar decisiones. Todo debe examinarse y prepararse con cuidado. No obstante, una vez que se hayan considerado todas las consecuencias, la partida no debe retrasarse.",
        "pregunta": "¿Qué áreas de tu vida están cambiando? ¿Estás preparado para acabar con lo viejo y hacer sitio para lo nuevo?"
    },
    
    "VIII. El Ajuste": {
        "nombre": "VIII. El Ajuste",
        "palabras_clave": "Libra, equilibrio, armonía, compensación de diferencias, estabilidad, justicia",
        "descripcion": "Observa con cuidado aquellas situaciones de tu vida diaria que tienden a perturbar tu estabilidad interior. Descubre las condiciones que ayudan a encontrar tu armonía y ve incluyendo esta cualidad en más áreas de tu vida. Las tormentas de la vida amenazan constantemente con romper nuestro equilibrio.",
        "pregunta": "¿Qué es lo que más te ayuda a encontrar y permanecer un rato en tu centro meditativo? ¿Qué pasa si lo pierdes?"
    },
    
    "IX. El Ermitaño": {
        "nombre": "IX. El Ermitaño",
        "palabras_clave": "Virgo, encuentra tu luz, mira hacia tu interior, consumación, fertilidad, cosecha",
        "descripcion": "Acepta tu soledad. No te relaciones con los que no te entienden, con los que prefieren verte como uno más del rebaño. Sigue a un maestro sabio si lo encuentras. El que inicia el viaje hacia su luz interior debe enfrentarse primero a sus conflictos sin resolver y sus cuentas pendientes.",
        "pregunta": "¿Hay en tu vida alguna situación o relación sin resolver?"
    },
    
    "X. La Fortuna": {
        "nombre": "X. La Fortuna",
        "palabras_clave": "Júpiter, nuevos comienzos, expansión, creatividad, gran avance, suerte inesperada",
        "descripcion": "Si no ocurre ningún milagro en tu vida es que algo anda mal. Tienes la posibilidad de lograr un avance importante. Aprovecha el momento. La vida nos guarda regalos y oportunidades inesperadas. Necesitamos un ojo observador para verlas. Las viejas limitaciones se ponen en entredicho para permitir que crezca lo nuevo.",
        "pregunta": "¿Estás verdaderamente preparado para la buena suerte? ¿A qué obstáculos te enfrentas?"
    },
    
    "XI. El Deseo": {
        "nombre": "XI. El Deseo",
        "palabras_clave": "Leo, pasión, creatividad polifacética, talentos, fuerza, integración de poderes animales",
        "descripcion": "Cuando estés preparado para aceptar todo lo que hay dentro de ti, podrás moverte con la máxima energía y con capacidad de sentir, ser consciente, amar y comprender. El Deseo es más que una mera fuerza vital. Comprende tanto la pasión como la alegría, así como el placer de experimentar poder. Es la embriaguez divina y el éxtasis cósmico.",
        "pregunta": "¿Qué áreas de tu vida quieres experimentar más plenamente? ¿Estás listo para intentarlo de nuevo?"
    },
    
    "XII. El Colgado": {
        "nombre": "XII. El Colgado",
        "palabras_clave": "Agua, parálisis, fin de una situación estancada, desprenderse, rendirse, sumisión",
        "descripcion": "Tienes ahora la oportunidad de reconocer la rigidez y la parálisis que pueda haber en distintas áreas de tu vida. No hay nada que hacer. La percepción de tu realidad te da la oportunidad de cambiarla. El Colgado se encuentra en una postura que rompe con la voluntad propia. Es una situación sin salida, pero en medio de la desesperación pueden ocurrir milagros.",
        "pregunta": "¿Qué áreas de tu vida se caracterizan por actitudes rígidas? ¿Estás preparado para abandonar tus pautas inflexibles?"
    },
    
    "XIII. La Muerte": {
        "nombre": "XIII. La Muerte",
        "palabras_clave": "Escorpio, muerte y renacimiento, desaparición y renovación, transformación",
        "descripcion": "Estás preparado para hacer los cambios necesarios en tu vida. Acepta el dolor que sigue a la pérdida de lo que es familiar. Hay que disolver urgentemente viejas relaciones. Este proceso puede ser doloroso, pero el hecho de haber sacado esta carta indica una voluntad de hacerlo. Al romper los lazos se tiene ganada ya la mitad de la batalla.",
        "pregunta": "¿A cuál de tus relaciones o situaciones pasadas sigues aferrándote?"
    },
    
    "XIV. El Arte": {
        "nombre": "XIV. El Arte",
        "palabras_clave": "Sagitario, unión de opuestos, equilibrio, transformación interior, alquimia, salto cuántico",
        "descripcion": "Esta carta nos invita a mirar hacia dentro. El proceso de conversión ya no requiere influencias externas en esta etapa de la integración de opuestos. Debes mirar en tu interior para encontrar el tesoro oculto. La unión alquímica del fuego y el agua, la conexión entre el fuego y el agua, la luz y la oscuridad, lo masculino y lo femenino, es un proceso interior.",
        "pregunta": "¿Cuáles son los opuestos, dentro de ti o en tu vida, que esperas unificar?"
    },
    
    "XV. El Diablo": {
        "nombre": "XV. El Diablo",
        "palabras_clave": "Capricornio, poder procreativo, nueva vitalidad, humor, sensualidad, sexualidad",
        "descripcion": "Puede haber personas que te vean como un 'diablo'. Aprende a tratarlas con humor y alegría. Acepta lo que te da la vida. Mantén los pies en la tierra. El Diablo es una de las cartas más incomprendidas. Representa la energía creativa en su manifestación más material y masculina. Su cara tiene una expresión de diversión y gran satisfacción.",
        "pregunta": "¿Hay algo que deseas pero no quieres reconocer que deseas?"
    },
    
    "XVI. La Torre": {
        "nombre": "XVI. La Torre",
        "palabras_clave": "Marte, profunda transformación interior, curación, destrucción de lo viejo",
        "descripcion": "Estás experimentando actualmente, o vas a experimentar dentro de poco, un intenso proceso de transformación. Las cosas que se romperán dentro de ti te ayudarán a purificarte y a prepararte para algo nuevo. ¡Deja que esto ocurra! La Torre es una de las cartas curativas más importantes. La destrucción de relaciones y situaciones sin salida puede ser el comienzo de un proceso de curación.",
        "pregunta": "¿Estás preparado para mirarte a ti mismo y a la vida con nuevos ojos?"
    },
    
    "XVII. La Estrella": {
        "nombre": "XVII. La Estrella",
        "palabras_clave": "Acuario, inspiración, cristalización, autorreconocimiento, claridad de visión, autoconfianza",
        "descripcion": "Deja que tu estrella se alce en el cielo y sigue en contacto con la tierra. Fíate de tus inspiraciones y encuentra maneras de compartir lo que has descubierto con otras personas. Serás puesto a prueba y reconocido por los frutos que des. La fuerza de inspiración te alienta y deja que se convierta en realidad lo que parecía imposible.",
        "pregunta": "¿Estás completamente satisfecho con lo que estás haciendo?"
    },
    
    "XVIII. La Luna": {
        "nombre": "XVIII. La Luna",
        "palabras_clave": "Piscis, pruebas finales, direcciones erróneas, ilusiones, enfrentamiento al subconsciente",
        "descripcion": "Has oído la llamada de lo desconocido. Te encuentras en el umbral de nuevas experiencias. Presta atención a la voz de tu corazón y examina en paz las cosas que te ayudan a encontrar el buen camino. Es un período de pruebas finales que a menudo resultan muy difíciles. En la oscuridad se esconde el gran peligro de perder de vista el objetivo real.",
        "pregunta": "¿Qué zonas de ti mismo te son desconocidas? ¿Cuáles son las experiencias que más temes?"
    },
    
    "XIX. El Sol": {
        "nombre": "XIX. El Sol",
        "palabras_clave": "Sol, intensa energía creativa, conciencia, relación amorosa plenamente satisfactoria",
        "descripcion": "El cumplimiento de tus deseos es posible aquí y ahora. Relájate y disfruta del baile de la rueda. Se encontrarán los compañeros adecuados. Un profundo proceso de transformación alquímica tiene lugar al experimentarse la sensación de euforia. Has descubierto la fuente de toda luz dentro de ti mismo, fuente que irradia amor y sabiduría divina.",
        "pregunta": "¿Qué tarea, qué proyecto se te presenta?"
    },
    
    "XX. El Eón": {
        "nombre": "XX. El Eón",
        "palabras_clave": "Fuego, juicio sano, apertura a las críticas, autoexamen crítico, transformación espiritual",
        "descripcion": "Has sido llamado para renunciar a tu estrecho punto de vista y para ver las cosas y juzgarlas desde un nivel más alto. Si reconoces períodos de tiempo más largos y contextos más generales, percibirás las limitaciones de todo juicio humano. La comprensión global no puede alcanzarse sólo por el entendimiento analítico. Tanto el cuerpo como la mente y el alma tienen derecho a ser considerados.",
        "pregunta": "¿Qué pasos estás tomando hacia un mayor entendimiento y una mayor sabiduría?"
    },
    
    "XXI. El Universo": {
        "nombre": "XXI. El Universo",
        "palabras_clave": "Saturno, consumación, unión cósmica, grandes viajes, ruptura de cadenas, fin del Karma",
        "descripcion": "Tienes ahora la oportunidad de ver las cosas tal como son. Todas las condiciones necesarias para una conclusión o un renacimiento felices están presentes. Los acontecimientos de tu vida están en armonía con el universo. Ahora uno se ve a uno mismo y al mundo tal como son en realidad. Todos los disfraces se han vuelto superfluos. Conectado a la naturalidad original, uno se deja arrastrar por la danza del continuo movimiento del universo.",
        "pregunta": "¿Cuáles son las áreas de tu vida de las que deberías liberarte? ¿Hay un viaje que esté esperando ser iniciado?"
    },
    
    # ============================================
    # FIGURAS (CARTAS DE CORTE) - 16 CARTAS
    # ============================================
    
    # ---- BASTOS ----
    "Caballero de Bastos": {
        "nombre": "Caballero de Bastos",
        "palabras_clave": "Fuego de fuego, energía fogosa, acción dinámica, gran percepción, cambios",
        "descripcion": "Ha llegado el momento de prestar atención y estar abierto a personas o situaciones que pueden provocar cambios dinámicos en tu conciencia. Agradece y acepta estos regalos, pero no te aferres demasiado a ellos. El Caballero personifica el dominio del crecimiento y el desarrollo interior. Su armadura es de piel de reptil, en señal de cambio y regeneración.",
        "pregunta": "¿Te permite tu situación actual desarrollar plenamente tu energía? Si no es así, ¿qué te impide hacerlo?"
    },
    
    "Reina de Bastos": {
        "nombre": "Reina de Bastos",
        "palabras_clave": "Agua de fuego, autoconocimiento, cambio profundo, compasión",
        "descripcion": "Has hecho esfuerzos por mejorar, y has avanzado mucho. Es hora de dejar que otras personas disfruten de los resultados. Aplica el conocimiento que has adquirido en tu vida diaria. La Reina de Bastos es una maestra del autoconocimiento. Ha mirado profundamente hacia su interior. Esto la ha transformado por completo.",
        "pregunta": "¿Cómo puedes compartir con otras personas lo que has encontrado para ti?"
    },
    
    "Príncipe de Bastos": {
        "nombre": "Príncipe de Bastos",
        "palabras_clave": "Aire de fuego, intensidad, amor floreciente, creatividad intuitiva",
        "descripcion": "Tienes todo lo que necesitas. No dejes que nada te detenga, que nadie te haga desacelerar el paso. La vida está lista para darte la bienvenida. Confía en tus posibilidades ilimitadas de creatividad. El Príncipe personifica el dominio sobre la creatividad intuitiva. Todos los sentidos participan para lograr este fin.",
        "pregunta": "¿A qué nuevas experiencias estás abierto ahora?"
    },
    
    "Princesa de Bastos": {
        "nombre": "Princesa de Bastos",
        "palabras_clave": "Tierra de fuego, liberación del miedo, nuevo comienzo, optimismo",
        "descripcion": "Tus viejos miedos han perdido su poder sobre ti. Sus restos mortales ya no pueden aterrorizarte. Piensa en tus puntos más fuertes. El miedo ha sido superado. La Princesa, desnuda, abierta y desprotegida, ha conquistado al tigre del miedo. Realiza su danza de euforia en medio de una gran llama ardiente.",
        "pregunta": "¿Cuál es tu próximo paso hacia la liberación?"
    },
    
    # ---- COPAS ----
    "Caballero de Copas": {
        "nombre": "Caballero de Copas",
        "palabras_clave": "Fuego de agua, entrega a los seres queridos, capacidad de dar, relaciones espirituales",
        "descripcion": "Anhelas una intensa reciprocidad con gente que piense como tú. El Caballero de Copas lleva grandes alas con las que se impulsa. Las alas del espíritu elevan las relaciones emocionales a un nivel más alto de comprensión mutua.",
        "pregunta": "¿Cómo puede esto enriquecer tus relaciones?"
    },
    
    "Reina de Copas": {
        "nombre": "Reina de Copas",
        "palabras_clave": "Agua de agua, así abajo como arriba, manifestación abierta de los sentimientos, maternidad",
        "descripcion": "La manera abierta en que expresas tus sentimientos te llena de belleza. Puede haber gente que no te entienda, ¡no te preocupes! Hay muchas otras personas con las que puedes compartir tus sentimientos. La Reina está envuelta en misterio. Quien quiera entenderla deberá adentrarse hasta el fondo de sus sensaciones.",
        "pregunta": "¿Defiendes abiertamente tus emociones y percepciones?"
    },
    
    "Príncipe de Copas": {
        "nombre": "Príncipe de Copas",
        "palabras_clave": "Aire de agua, anhelo, deseo, entusiasmo, oportunidades de transformación",
        "descripcion": "Acepta tus necesidades y pasiones sexuales y vívelas al máximo. Puedes descubrir muchas cosas. Ríndete completamente a estas necesidades y obsérvate. Los deseos y anhelos deben percibirse y reconocerse. Ellos son los impulsos fundamentales de nuestra energía vital.",
        "pregunta": "¿Qué deseos secretos no estás reconociéndote a ti mismo?"
    },
    
    "Princesa de Copas": {
        "nombre": "Princesa de Copas",
        "palabras_clave": "Tierra de agua, libertad emocional, envidia conquistada, autoconfianza",
        "descripcion": "Has caso de tus sentimientos. Vas por el buen camino. La Princesa es emocionantemente libre. Se ha liberado de las cadenas de la manipulación posesiva. Libre de celos, ahora irradia gracia, dulzura y claridad.",
        "pregunta": "¿Hay alguna otra cosa que te esté impidiendo ser totalmente libre?"
    },
    
    # ---- ESPADAS ----
    "Caballero de Espadas": {
        "nombre": "Caballero de Espadas",
        "palabras_clave": "Fuego de aire, resolución, ambición, poder de razonamiento flexible, pasión",
        "descripcion": "Estás ahora en buenas condiciones para hacer planes y para fijarte metas y alcanzarlas. El Caballero sabe lo que quiere y no parará hasta conseguirlo. Su considerable poder de concentración es comparable al del conductor de un coche de carreras.",
        "pregunta": "¿Sabes cuál es tu meta? ¿Qué pasará una vez que la hayas alcanzado?"
    },
    
    "Reina de Espadas": {
        "nombre": "Reina de Espadas",
        "palabras_clave": "Agua de aire, destrucción de viejas máscaras, claridad, razón, intelecto, objetividad",
        "descripcion": "Te encuentras en un proceso de alejamiento progresivo de tus viejos papeles y modos de comportamiento. Los reconocimientos que resultan de ello pueden ser dolorosos, pero las recompensas serán grandes. La claridad que alcances te liberará.",
        "pregunta": "¿Cuáles son los papeles en los que más te gusta esconderte?"
    },
    
    "Príncipe de Espadas": {
        "nombre": "Príncipe de Espadas",
        "palabras_clave": "Aire de aire, intuición, pensamiento creativo, liberarse de ideas restrictivas",
        "descripcion": "Libérate de todo lo que restrinja la libertad de tu espíritu. Pero expresa tus ideas y planes de una manera inteligible para los demás. Acepta las críticas con modestia. El requisito imprescindible para los procesos de pensamiento inspirados es la libertad sin límites.",
        "pregunta": "¿Qué doctrinas, emociones o relaciones dejas que te limiten?"
    },
    
    "Princesa de Espadas": {
        "nombre": "Princesa de Espadas",
        "palabras_clave": "Tierra de aire, transición de nubes oscuras al sol, victoria sobre sentimientos",
        "descripcion": "Tus ideas y opiniones confusas a veces pueden dinamitar los 'altares sagrados'. Ten cuidado de no quedarte enterrado en los escombros. No te dejes controlar por tus estados de ánimo. Permanece fiel a tus ideas. La Princesa representa a una persona muy rebelde que no tiene miedo de las convenciones establecidas.",
        "pregunta": "¿Cuáles son los 'viejos altares' en tu vida? ¿Tienes valor para romper con ellos?"
    },
    
    # ---- OROS ----
    "Caballero de Oros": {
        "nombre": "Caballero de Oros",
        "palabras_clave": "Fuego de tierra, médico, sanador, inversiones financieras, cosecha, esfuerzo",
        "descripcion": "Es hora de que utilices tus capacidades para servir. Tus proyectos son ambiciosos y exigen que te dediques a ellos con toda tu energía. Si haces el esfuerzo, recibirás una gran recompensa. El Caballero personifica el dominio de la salud y de la abundancia material.",
        "pregunta": "¿Hay esfuerzos en tu vida que preferirías evitar?"
    },
    
    "Reina de Oros": {
        "nombre": "Reina de Oros",
        "palabras_clave": "Agua de tierra, fertilidad, corporalidad, nutrición, desprenderse del pasado",
        "descripcion": "Ha sido una larga marcha hasta ahora, y has llegado a un entorno fértil. Puedes relajarte y dedicar tiempo a ti mismo y a las necesidades de tu cuerpo. La Reina cuida su cuerpo. Sabe perfectamente cuánto cuidado necesita su cuerpo, templo del alma.",
        "pregunta": "¿Cómo has descuidado tu cuerpo y tu aspecto físico? ¿Te animas, te cuidas y sabes disfrutar?"
    },
    
    "Príncipe de Oros": {
        "nombre": "Príncipe de Oros",
        "palabras_clave": "Aire de tierra, gran energía en asuntos materiales, imperturbabilidad, actividad física",
        "descripcion": "Es hora de actuar. Puedes experimentar cosas importantes. Con una voluntad infalible, nada puede pararte, nada puede romper tu voluntad de hierro para alcanzar tu meta. Es precisamente en los asuntos materiales más importantes en los que demuestras tu imperturbabilidad.",
        "pregunta": "¿Qué actividad te gusta? ¿Cómo podrás desarrollar tu personalidad?"
    },
    
    "Princesa de Oros": {
        "nombre": "Princesa de Oros",
        "palabras_clave": "Tierra de tierra, embarazo, Madre Tierra, nacimiento, revitalización, armonía",
        "descripcion": "Algo nuevo va a entrar en tu vida. Debes estar preparado. El vientre hinchado de la Princesa indica su embarazo. En sentido figurado, también puede ser madre de una nueva identidad, idea o concepto. La mezcla armoniosa de las características masculinas y femeninas dentro de nosotros produce la renovación.",
        "pregunta": "¿Qué te gustaría cambiar en preparación para algo nuevo?"
    },
    
    # ============================================
    # ARCANOS MENORES (BASTOS) - 10 CARTAS (As-10)
    # ============================================
    
    "As de Bastos": {
        "nombre": "As de Bastos",
        "palabras_clave": "Fuego, energía creativa, fuerza dinámica, transformación",
        "descripcion": "Estás lleno de poder y de energía. Haz todo lo que puedas para averiguar dónde y cómo quieres y puedes usarlos. El As de Bastos simboliza el poder de la energía dinámica que fluye libremente sin restricciones ni temores. Una vez eliminados los obstáculos, la renovación de todas las áreas de la vida puede empezar.",
        "pregunta": "¿Hacia qué dirección te sientes más atraído? ¿Cuál será el mejor marco para realizar tus ideales?"
    },
    
    "Dos de Bastos - Dominio": {
        "nombre": "Dos de Bastos - Dominio",
        "palabras_clave": "Marte en Aries, energía beligerante, pionero, control o dominio de la situación",
        "descripcion": "Escucha a tu alma. Si está en contacto con tu corazón, sin duda dominarás la situación. Confía en tu energía. No aceptes precipitadamente ningún compromiso. La naturaleza del dominio se basa en la fuerza. Se trata de un estado de concentración que permite a la persona andar valientemente por nuevos caminos.",
        "pregunta": "¿Qué tareas o situaciones representan un reto para ti?"
    },
    
    "Tres de Bastos - Virtud": {
        "nombre": "Tres de Bastos - Virtud",
        "palabras_clave": "Sol en Aries, virtud, integridad, honradez, autoconfianza, nuevo comienzo",
        "descripcion": "Como en el Dos de Bastos, el tema es la orientación interior. Esto ocurre ahora sin ningún esfuerzo, sino que surge de tu propia confianza. Cuerpo, mente y alma están en armonía. Esta situación da lugar a la cristalización de una integridad que no conoce los compromisos espurios.",
        "pregunta": "¿Qué tareas o situaciones que requieran toda tu energía te quedan por realizar?"
    },
    
    "Cuatro de Bastos - Consumación": {
        "nombre": "Cuatro de Bastos - Consumación",
        "palabras_clave": "Venus en Aries, consumación, unificación, satisfacción plena, nuevos comienzos",
        "descripcion": "Algo bello se está desarrollando en tus relaciones. Tal vez se manifieste al criticarse abiertamente el statu quo en el curso de una discusión. Esto debe aclararse para que pueda haber una nueva unificación, un nuevo comienzo. El círculo se cierra. Las contradicciones se encuentran y se unen en el centro.",
        "pregunta": "¿Estás dispuesto a aceptar a tu compañero con todas sus diferencias? ¿Qué áreas deben aclararse?"
    },
    
    "Cinco de Bastos - Conflicto": {
        "nombre": "Cinco de Bastos - Conflicto",
        "palabras_clave": "Saturno en Leo, inhibición, deseo insatisfecho, miedo, esfuerzo inútil",
        "descripcion": "La resignación es un peligro inminente en una situación como ésta. Saturno sólo nos recuerda que las cosas deben tomarse paso a paso. No te desanimes. Si has sacado esta carta, significa que estás preparado para enfrentarte a la situación y solucionarla.",
        "pregunta": "¿Hay algún obstáculo para el logro de tus objetivos que parezca insuperable?"
    },
    
    "Seis de Bastos - Victoria": {
        "nombre": "Seis de Bastos - Victoria",
        "palabras_clave": "Júpiter en Leo, victoria, éxito, triunfo",
        "descripcion": "Haz lo que tenías pensado hacer. Ahora es el momento del éxito. Cuando hemos buscado lo suficiente, cuando hemos hecho todos los esfuerzos necesarios, el avance se produce de repente y obtenemos la victoria sin darnos cuenta. Nos embarga un sentimiento exaltado de fuerza.",
        "pregunta": "¿Qué quieres lograr? ¿Qué significa para ti la victoria?"
    },
    
    "Siete de Bastos - Valentía": {
        "nombre": "Siete de Bastos - Valentía",
        "palabras_clave": "Marte en Leo, impacto, coraje, valor, voluntad de arriesgarse",
        "descripcion": "La lealtad a uno mismo también implica defender la propia realidad ante la resistencia masiva. Confía en tu fuerza. Debes hacer valer tu postura incondicionalmente en esta situación. La valentía tiene su origen en nuestras propias experiencias vitales. Muestra la capacidad de aprender del pasado.",
        "pregunta": "¿Estás preparado para aceptar todas las consecuencias?"
    },
    
    "Ocho de Bastos - Rapidez": {
        "nombre": "Ocho de Bastos - Rapidez",
        "palabras_clave": "Mercurio en Sagitario, comunicación clara, directa y rápida, superación de malentendidos",
        "descripcion": "Ha llegado la hora de comunicar tu posición clara y firmemente. Si eres cándido y te respetas a ti mismo desaparecerán los malentendidos. El obstáculo puede transformarse al declarar uno su punto de vista inequívoca y directamente. Los malentendidos dejan paso a la claridad.",
        "pregunta": "¿Hay personas con las que no te atreves a expresar tu opinión?"
    },
    
    "Nueve de Bastos - Fuerza": {
        "nombre": "Nueve de Bastos - Fuerza",
        "palabras_clave": "Sol en Sagitario, fuerza a través de la unificación de energía consciente e inconsciente",
        "descripcion": "Estás descubriendo tus verdaderas fuerzas. Confía en tu guía interior. Podrías incluso unirte a un grupo de autoconocimiento que te ayudará a desarrollar tu potencial. El reconocimiento del potencial que hasta ahora permanecía latente libera energía que se ve como nueva y extraordinaria.",
        "pregunta": "¿Eres consciente del miedo que sientes de tu propia fuerza?"
    },
    
    "Diez de Bastos - Opresión": {
        "nombre": "Diez de Bastos - Opresión",
        "palabras_clave": "Saturno en Sagitario, emoción reprimida, energía contenida, separación",
        "descripcion": "Seas o no consciente de que estás reprimiendo tu energía, hay mucho que te gustaría expresar, experimentar, disfrutar y celebrar. ¡Atrévete a expresar tu fuego interior! La ansiedad con respecto a nuestra propia fuerza y vitalidad surge por el miedo al rechazo, la desaprobación y el castigo.",
        "pregunta": "¿En qué situación reprimes tu fuerza o te olvidas de tu alegría de vivir?"
    },
    
    # ============================================
    # ARCANOS MENORES (COPAS) - 10 CARTAS (As-10)
    # ============================================
    
    "As de Copas": {
        "nombre": "As de Copas",
        "palabras_clave": "Agua, amor desbordante, claridad emocional, profundo amor a uno mismo",
        "descripcion": "Estás en contacto estrecho con el amor que todo lo engloba; te llena y tú lo compartes voluntariamente. El As de Copas es el equivalente femenino del As de Bastos; abierto, receptivo, dedicado, portador de la fuerza transformadora del ofrecimiento de amor.",
        "pregunta": "¿Cómo expresas tu amor?"
    },
    
    "Dos de Copas - Amor": {
        "nombre": "Dos de Copas - Amor",
        "palabras_clave": "Venus en Cáncer, amor recibido, relaciones felices, intercambio emocional",
        "descripcion": "Tu voluntad de recibir amor te hace atractivo. Cede ante ti mismo, ante los demás, ante la vida. Cuando uno se quiere a sí mismo, se vuelve atractivo para los demás. La voluntad de aceptarse a uno mismo demuestra la capacidad de entregarse completamente a otra persona.",
        "pregunta": "¿Con quién te gustaría compartir tu amor?"
    },
    
    "Tres de Copas - Abundancia": {
        "nombre": "Tres de Copas - Abundancia",
        "palabras_clave": "Mercurio en Cáncer, generoso intercambio de sentimientos de amor",
        "descripcion": "Tienes algo muy valioso que compartir. Permanece abierto a personas con las que puedas compartir tus sentimientos especiales. Ellas son un regalo; no necesitas buscarlas. Cuando nos incorporamos al ciclo del amor, dando y recibiéndolo, vivimos en la abundancia de la vida en todos los ámbitos.",
        "pregunta": "¿Hay alguien a quien no hayas expresado tu amor abiertamente?"
    },
    
    "Cuatro de Copas - Lujo": {
        "nombre": "Cuatro de Copas - Lujo",
        "palabras_clave": "Luna en Cáncer, amor, ternura, cuidados, riqueza emocional",
        "descripcion": "Recibes mucho amor y atención de otras personas. Disfrútalo sin volverte dependiente de ellas. El peligro radica en que las emociones pueden volverse independientes y cobrar una indisciplinada vida propia. En los buenos tiempos uno debe estar doblemente alerta.",
        "pregunta": "¿Hay alguna relación que te resulte asfixiante?"
    },
    
    "Cinco de Copas - Decepción": {
        "nombre": "Cinco de Copas - Decepción",
        "palabras_clave": "Marte en Escorpio, expectativas frustradas, equilibrio perdido, relación problemática",
        "descripcion": "Tus expectativas, demasiado altas, fueron truncadas, o el miedo a sufrir una decepción está creciendo dentro de ti. Ahora tienes que aprender de esta situación. Detrás de cada decepción hay un engaño a uno mismo. La suave voz de alarma interna llevaba demasiado tiempo callada.",
        "pregunta": "¿En qué área de tu vida temes sufrir una decepción?"
    },
    
    "Seis de Copas - Placer": {
        "nombre": "Seis de Copas - Placer",
        "palabras_clave": "Sol en Escorpio, lujuria, placer, felicidad en las relaciones sexuales",
        "descripcion": "Deberías disfrutar ahora de todo lo que te da la vida. Ésta es la mejor expresión de tu gratitud. Se ha superado el miedo a la decepción. El cuerpo y los sentidos se han limpiado y están listos para una reunión feliz con una persona amada. La recompensa por haber tomado el riesgo es una profunda purificación.",
        "pregunta": "¿Sigues albergando sentimientos de culpabilidad que no te dejan disfrutar al máximo del placer?"
    },
    
    "Siete de Copas - Corrupción": {
        "nombre": "Siete de Copas - Corrupción",
        "palabras_clave": "Venus en Escorpio, hiperactividad, desagrado, saciedad",
        "descripcion": "Es hora de que abras los ojos y aceptes la realidad, que puede ser dolorosa. Lo único que puede liberarte es el reconocimiento y la percepción de tu propia realidad interior. Has intentado esconder viejas heridas pero tus trucos no han funcionado.",
        "pregunta": "¿Hay alguna decepción en tu vida que no hayas superado todavía?"
    },
    
    "Ocho de Copas - Indolencia": {
        "nombre": "Ocho de Copas - Indolencia",
        "palabras_clave": "Saturno en Piscis, estancamiento, inhibición, congestión emocional, pereza",
        "descripcion": "Ahora es el momento de prestarte más atención a ti mismo, de fijarte unos límites claros y de decir 'NO'. Has gastado ya demasiada energía en personas que no te aportan nada. Las llenaste de tu energía pero eran como pozos sin fondo.",
        "pregunta": "¿En quién te hace pensar este texto? ¿Estás preparado para mantenerte firme?"
    },
    
    "Nueve de Copas - Felicidad": {
        "nombre": "Nueve de Copas - Felicidad",
        "palabras_clave": "Júpiter en Piscis, éxtasis, amor desbordante, profunda felicidad, bendición",
        "descripcion": "Primero, ábrete a la felicidad en lo más profundo de tu ser. Sé feliz tú mismo y automáticamente atraerás la felicidad. Ten fe en tus emociones y en tu derecho natural a ser feliz. La calidad de esta felicidad es muestra de que existe una gran profundidad que no es resultado de un placer superficial.",
        "pregunta": "¿Dónde buscas y dónde encuentras la verdadera felicidad?"
    },
    
    "Diez de Copas - Saciedad": {
        "nombre": "Diez de Copas - Saciedad",
        "palabras_clave": "Marte en Piscis, satisfacción, culminación, aspecto radiante, gratitud",
        "descripcion": "Deja que vayan desarrollándose las cosas. Todo te vendrá en el momento oportuno. Las diez Copas forman la figura del Árbol de la Vida. Todo está en su lugar, ordenado en perfecta armonía. La imagen muestra la plenitud interior profunda.",
        "pregunta": "¿Por qué cosas estás agradecido?"
    },
    
    # ============================================
    # ARCANOS MENORES (ESPADAS) - 10 CARTAS (As-10)
    # ============================================
    
    "As de Espadas": {
        "nombre": "As de Espadas",
        "palabras_clave": "Aire, claridad espiritual, pensamiento original, poder intelectual, inspiración divina",
        "descripcion": "La claridad es un requisito maravilloso para todo lo que haces. A veces aprendes cosas que otros barrerían debajo de la alfombra, pero tú las llamas por su nombre. Por esta misma razón, debes ser responsable. Asegúrate de que siempre comunicas tus intenciones con compasión.",
        "pregunta": "¿Qué cosas apoyan y qué cosas empañan la claridad?"
    },
    
    "Dos de Espadas - Paz": {
        "nombre": "Dos de Espadas - Paz",
        "palabras_clave": "Luna en Libra, paz interior, poder de decisión, decisiones sobre relaciones",
        "descripcion": "La paz interior es un don muy especial. Debes disfrutarla sin intentar nunca aferrarte a ella. Las inspiraciones e ideas que nacen en este momento son extraordinarias. Deberías recordarlas como una guía para los momentos en que falten la claridad y la organización.",
        "pregunta": "¿Qué parte de tu vida es especialmente importante para ti?"
    },
    
    "Tres de Espadas - Aflicción": {
        "nombre": "Tres de Espadas - Aflicción",
        "palabras_clave": "Saturno en Libra, preocupaciones, duda, ambigüedad, depresión",
        "descripcion": "Esta carta presenta el reto de tomar decisiones claras e inequívocas. Es lo único que restaurará el equilibrio perdido. La lección que debe aprenderse aquí no es otra que la de dominar el pensamiento negativo. Los lamentos y las expectativas escépticas deben reconocerse como fuerzas que nos separan.",
        "pregunta": "¿Qué decisiones te resultan difíciles de tomar?"
    },
    
    "Cuatro de Espadas - Tregua": {
        "nombre": "Cuatro de Espadas - Tregua",
        "palabras_clave": "Júpiter en Libra, paz, equilibrio, claridad, purificación espiritual",
        "descripcion": "Posees la suficiente claridad interior para ocuparte felizmente de tus asuntos. Asegúrate de que te sientes absolutamente cómodo al hacerlo. Las preocupaciones se han superado. La claridad del As de Espadas se ha recuperado; vuelve a verse el brillo del azul.",
        "pregunta": "¿Tiendes a evitar la falta de armonía y los conflictos subliminales?"
    },
    
    "Cinco de Espadas - Derrota": {
        "nombre": "Cinco de Espadas - Derrota",
        "palabras_clave": "Venus en Acuario, miedo a la derrota, miedo a las experiencias dolorosas",
        "descripcion": "El hecho de que hayas sacado esta carta demuestra que ya estás listo para percibir tu miedo a la derrota. Con este conocimiento puedes liberar la energía que está reprimida por el miedo. Al entender las raíces del miedo, podemos desarmarlo y abandonarlo.",
        "pregunta": "¿Qué es lo que asocias con la 'derrota'?"
    },
    
    "Seis de Espadas - Ciencia": {
        "nombre": "Seis de Espadas - Ciencia",
        "palabras_clave": "Mercurio en Acuario, capacidad de analizar, asociar ideas, comprensión global",
        "descripcion": "Posees la capacidad de percibir las cosas de manera diferente. Tu inteligencia integra aspectos muy distintos. La capacidad de análisis añade claridad a las perspectivas futuras. Éstas no sólo se ven claramente, sino que también pueden comunicarse de manera inteligible.",
        "pregunta": "¿Cuáles son las 'rutinas familiares' en tu vida?"
    },
    
    "Siete de Espadas - Inutilidad": {
        "nombre": "Siete de Espadas - Inutilidad",
        "palabras_clave": "Luna en Acuario, desánimo, abatimiento, volubilidad, angustia existencial",
        "descripcion": "Tus temores no tienen nada que ver con la realidad. Despierta y abre los ojos ante ella. La gran espada de la claridad está siendo saboteada y dañada por seis espadas pequeñas. Las espadas pequeñas son los pensamientos negativos que impiden el éxito.",
        "pregunta": "¿En qué aspectos de tu vida te perjudicas con tus propias ideas negativas?"
    },
    
    "Ocho de Espadas - Interferencia": {
        "nombre": "Ocho de Espadas - Interferencia",
        "palabras_clave": "Júpiter en Géminis, falta de resistencia, exceso de introspección",
        "descripcion": "Deja que las cosas se resuelvan solas. No debes empezar nada nuevo mientras sigas teniendo dudas con respecto a la decisión que has de tomar. Júpiter promete oportunidades imprevistas con un final feliz. El problema que ahora parece insuperable se resolverá solo.",
        "pregunta": "¿Entre qué alternativas te sientes indeciso?"
    },
    
    "Nueve de Espadas - Crueldad": {
        "nombre": "Nueve de Espadas - Crueldad",
        "palabras_clave": "Marte en Géminis, crueldad hacia uno mismo, autoacusaciones, autocastigo",
        "descripcion": "La carta ilustra tu tendencia a menospreciarte cruelmente. Debes reconocer este comportamiento y darte cuenta de sus causas para poder deshacerte de él. Por regla general, esta carta indica crueldad hacia uno mismo. Ilustra la tendencia a gastar una gran cantidad de energía en menospreciarse a uno mismo.",
        "pregunta": "¿Quién solía juzgarte en el pasado? ¿Cómo te juzgas a ti mismo?"
    },
    
    "Diez de Espadas - Ruina": {
        "nombre": "Diez de Espadas - Ruina",
        "palabras_clave": "Sol en Géminis, miedo a la locura, pensamientos negativos",
        "descripcion": "El primer paso consiste en reconocer que tienes miedo a la locura y a la ruina. El segundo es entender la energía negativa que se esconde detrás de este miedo. La negatividad en el plano mental es la más fácil de superar, suponiendo que quieras superarla. Esta carta ilustra la energía destructiva del pensamiento pesimista.",
        "pregunta": "¿Qué es lo que más temes?"
    },
    
    # ============================================
    # ARCANOS MENORES (OROS/DISCOS) - 10 CARTAS (As-10)
    # ============================================
    
    "As de Oros": {
        "nombre": "As de Oros",
        "palabras_clave": "Tierra, riqueza interior y exterior, gran éxito, unión de cuerpo y alma",
        "descripcion": "El As de Oros refleja tu disposición para llevar una vida plena, tanto interna como externamente. Has cumplido todos los requisitos. Cede ante la plenitud de la vida y abre tus alas. El símbolo del As de Oros tiene forma de cruz, indicando unión vertical y horizontal, concurrencia de lo interno y lo externo.",
        "pregunta": "¿Qué aspectos de tu vida te gustaría enriquecer?"
    },
    
    "Dos de Oros - Cambio": {
        "nombre": "Dos de Oros - Cambio",
        "palabras_clave": "Júpiter en Capricornio, cambio, transformación, progreso continuo",
        "descripcion": "La vida está sujeta constantemente a cambios que nos permiten crecer, nos abren horizontes y nos enriquecen la vida. Confía en tus cambios. Una larga serpiente, símbolo de renovación, adopta la forma del número 8, signo del infinito. Esto indica cambios continuos.",
        "pregunta": "¿Qué cambios internos y externos esperas que ocurran en tu vida?"
    },
    
    "Tres de Oros - Trabajos": {
        "nombre": "Tres de Oros - Trabajos",
        "palabras_clave": "Marte en Capricornio, trabajo, esfuerzo, progreso gradual, obligación para con uno mismo",
        "descripcion": "Algo te exige estar preparado para trabajar durante un tiempo prolongado. Esfuérzate al máximo: ¡vale la pena! Esta carta indica una completa implicación en un asunto con respecto al cual uno siente una obligación interna. Uno está absolutamente dispuesto a asumir una gran actividad.",
        "pregunta": "¿En qué cosas sigues sin esforzarte todo lo que deberías?"
    },
    
    "Cuatro de Oros - Poder": {
        "nombre": "Cuatro de Oros - Poder",
        "palabras_clave": "Sol en Capricornio, manifestación, integridad, carácter, peligro de rigidez",
        "descripcion": "El significado de la carta depende de las circunstancias del individuo que la haya sacado. Puede ser una advertencia para que la persona muestre un carácter más fuerte e íntegro, o un reto a que subordine los principios a la vida y a las emociones del corazón. Los cuatro oros están representados en forma cuadrada como las cuatro torres esquineras de una fortaleza.",
        "pregunta": "¿Te asemejas en tu vida a una fortaleza rígida? ¿O necesitas más organización?"
    },
    
    "Cinco de Oros - Preocupación": {
        "nombre": "Cinco de Oros - Preocupación",
        "palabras_clave": "Mercurio en Tauro, preocupaciones, lamentos, pesimismo, angustia existencial",
        "descripcion": "Si sacas esta carta significa que estás preparado para ver tu situación en términos realistas. Se te está ofreciendo la oportunidad de liberarte iniciando la confrontación que se vuelve ahora necesaria. Sólo la comunicación clara y abierta hará posible el progreso. La situación ha llegado a un punto muerto.",
        "pregunta": "¿En qué aspectos no eres lo suficientemente claro y decidido?"
    },
    
    "Seis de Oros - Éxito": {
        "nombre": "Seis de Oros - Éxito",
        "palabras_clave": "Luna en Tauro, manifestación externa del estado interior, éxito, transformación",
        "descripcion": "Mantente abierto al éxito. El éxito es consecuencia de nuestros pensamientos y acciones. Pero también es un don de vida, y puedes aprender a aceptarlo con gratitud y modestia. El éxito verdadero llega cuando has aprendido a servir. Esta es una carta de mediación para cualquier tipo de proyecto.",
        "pregunta": "¿Qué significa para ti el 'éxito'?"
    },
    
    "Siete de Oros - Fracaso": {
        "nombre": "Siete de Oros - Fracaso",
        "palabras_clave": "Saturno en Tauro, inhibición, resignación, vacilación, miedo al fracaso",
        "descripcion": "Tus acciones se ven truncadas por expectativas graves y temerosas, cuyo contenido y calidad deberías examinar. Las experiencias de fracaso tienen que ver principalmente con los negocios, los asuntos económicos, las áreas relacionadas con el cuerpo y la salud física o la angustia existencial en general.",
        "pregunta": "¿Qué aspectos de tu vida te crean preocupaciones?"
    },
    
    "Ocho de Oros - Prudencia": {
        "nombre": "Ocho de Oros - Prudencia",
        "palabras_clave": "Sol en Virgo, florecimiento de la riqueza interior y exterior, sabiduría, prudencia",
        "descripcion": "Lo que está intentando desarrollarse dentro de ti es de una belleza exquisita y de una ternura extraordinaria. Dale la protección y la alimentación que necesita ahora. No hace falta usar la fuerza. Todo se desarrollará a su debido tiempo. El árbol florece en todo su esplendor.",
        "pregunta": "¿Te das a ti mismo la protección y la alimentación que necesitas para desarrollarte?"
    },
    
    "Nueve de Oros - Ganancia": {
        "nombre": "Nueve de Oros - Ganancia",
        "palabras_clave": "Venus en Virgo, progreso, ganancia, unificación del amor, la sabiduría y la creatividad",
        "descripcion": "Cuando el amor invada tu conocimiento y tu creatividad ganarás experiencia en todas las áreas de la vida. Cuanto más te impliques, más aprenderás. Los tres oros en el centro simbolizan la unificación del amor, la sabiduría y la creatividad. La fuerza central vinculante es el amor.",
        "pregunta": "¿Sabes cuál es tu mayor objetivo en la vida?"
    },
    
    "Diez de Oros - Riqueza": {
        "nombre": "Diez de Oros - Riqueza",
        "palabras_clave": "Mercurio en Virgo, riqueza interior y exterior, comunicar la riqueza interna",
        "descripcion": "Cada persona en tu vida es producto de tu capacidad de atracción y cada acontecimiento, producto de tu creatividad. Eres el creador de tu propia realidad. Pon tu creatividad al servicio del amor. Las monedas están colocadas para formar el Árbol de la Vida. Esto indica que la verdadera riqueza se expresa en todos los ámbitos de la vida.",
        "pregunta": "¿Eres consciente de tu riqueza interior? ¿La compartes magnánimamente?"
    }
}

# Lista de nombres de todas las cartas para facilitar la selección aleatoria
lista_de_cartas = list(cartas_del_tarot.keys())

# Verificar que tenemos 80 cartas (22 Mayores + 16 Figuras + 42 Menores = 80)
print(f"Total de cartas cargadas: {len(lista_de_cartas)}")
