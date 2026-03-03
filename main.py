# main.py
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from tarot_data import cartas_del_tarot, lista_de_cartas

# ============================================
# CONFIGURACIÓN
# ============================================
# IMPORTANTE: Reemplaza con el token de tu bot de Telegram
BOT_TOKEN = "YOUR_TOKEN_HERE"  # <--- PON AQUÍ TU TOKEN

# Configuración de logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Estado para el ejercicio de adivinación
user_exercise_state = {}

# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def obtener_carta_aleatoria():
    """Selecciona una carta al azar del diccionario."""
    nombre_carta = random.choice(lista_de_cartas)
    return cartas_del_tarot[nombre_carta]

def obtener_carta_por_nombre(nombre):
    """Obtiene una carta por su nombre exacto."""
    if nombre in cartas_del_tarot:
        return cartas_del_tarot[nombre]
    return None

def formatear_mensaje_carta(carta_data):
    """Toma los datos de una carta y devuelve un mensaje bonito."""
    mensaje = f"🃏 *{carta_data['nombre']}*\n\n"
    mensaje += f"*Palabras Clave:* {carta_data['palabras_clave']}\n\n"
    mensaje += f"*Interpretación:* {carta_data['descripcion']}\n\n"
    mensaje += f"*Pregunta para reflexionar:* {carta_data['pregunta']}"
    return mensaje

def obtener_arcanos_mayores():
    """Devuelve la lista de Arcanos Mayores."""
    return [nombre for nombre in lista_de_cartas if nombre[0].isdigit() or nombre.startswith('0.')]

# ============================================
# MANEJADORES DE COMANDOS PRINCIPALES
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Mensaje de bienvenida."""
    await update.message.reply_text(
        "🌌 *Bienvenido al Oráculo de Thoth* 🌌\n\n"
        "Soy un bot de Tarot basado en *El Libro de Thoth* de Aleister Crowley\n"
        "y en *Tarot, el espejo del alma* de Gerd B. Ziegler.\n\n"
        "*Comandos disponibles:*\n\n"
        "🔮 *Lecturas:*\n"
        "/thoth - Menú principal de lecturas\n"
        "/carta_del_dia - Carta única para hoy\n"
        "/tres_cartas - Tirada de 3 cartas (Pasado, Presente, Futuro)\n"
        "/cinco_cartas - Tirada de 5 cartas (visión profunda)\n"
        "/ocho_cartas - Tirada de 8 cartas (análisis complejo)\n\n"
        "🧘 *Sabiduría:*\n"
        "/ley - Fragmento del Liber AL vel Legis\n"
        "/libertad - Reflexión sobre la libertad\n"
        "/40 - El número 40 en la tradición\n"
        "/nagual - El guardián del umbral\n"
        "/angel - El Santo Ángel Guardián\n\n"
        "🎴 *Ejercicio:*\n"
        "/ejercicio_arcanos - Entrena tu intuición con Arcanos Mayores\n"
        "/pista - Pista para el ejercicio\n\n"
        "Que la sabiduría de Thoth te acompañe. ✨",
        parse_mode='Markdown'
    )

async def thoth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /thoth - Menú de lecturas."""
    await update.message.reply_text(
        "🔮 *Lecturas del Tarot de Thoth* 🔮\n\n"
        "Elige el tipo de lectura:\n\n"
        "• /carta_del_dia - Una carta para tu día\n"
        "• /tres_cartas - Pasado, Presente, Futuro\n"
        "• /cinco_cartas - Visión profunda de 5 cartas\n"
        "• /ocho_cartas - Análisis complejo de 8 cartas\n\n"
        "Para comenzar un ejercicio de adivinación:\n"
        "• /ejercicio_arcanos - Entrena tu percepción",
        parse_mode='Markdown'
    )

# ============================================
# LECTURAS DE TAROT
# ============================================

async def carta_del_dia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /carta_del_dia - Una carta al azar."""
    carta = obtener_carta_aleatoria()
    mensaje = formatear_mensaje_carta(carta)
    await update.message.reply_text(mensaje, parse_mode='Markdown')

async def tres_cartas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tirada de tres cartas (Pasado, Presente, Futuro)."""
    cartas = [obtener_carta_aleatoria() for _ in range(3)]
    
    mensaje = "🔮 *Tirada de Tres Cartas* 🔮\n\n"
    mensaje += f"*Pasado:* **{cartas[0]['nombre']}**\n"
    mensaje += f"➡️ {cartas[0]['palabras_clave']}\n\n"
    mensaje += f"*Presente:* **{cartas[1]['nombre']}**\n"
    mensaje += f"➡️ {cartas[1]['palabras_clave']}\n\n"
    mensaje += f"*Futuro:* **{cartas[2]['nombre']}**\n"
    mensaje += f"➡️ {cartas[2]['palabras_clave']}\n\n"
    mensaje += "Para más detalles de cada carta, consulta con /carta_del_dia o escribe el nombre exacto."
    
    await update.message.reply_text(mensaje, parse_mode='Markdown')

async def cinco_cartas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tirada de cinco cartas."""
    cartas = [obtener_carta_aleatoria() for _ in range(5)]
    
    mensaje = "🔮 *Tirada de Cinco Cartas* 🔮\n"
    mensaje += "Interpreta estas cartas en el contexto de tu pregunta.\n\n"
    
    posiciones = [
        "Situación actual",
        "Desafío",
        "Ayuda disponible",
        "Fuerza interior",
        "Resultado potencial"
    ]
    
    for i, carta in enumerate(cartas):
        mensaje += f"*{i+1}. {posiciones[i]}:* **{carta['nombre']}**\n"
        mensaje += f"   _{carta['palabras_clave']}_\n\n"
    
    await update.message.reply_text(mensaje, parse_mode='Markdown')

async def ocho_cartas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tirada de ocho cartas."""
    cartas = [obtener_carta_aleatoria() for _ in range(8)]
    
    mensaje = "🔮 *Tirada de Ocho Cartas* 🔮\n"
    mensaje += "Una visión amplia de tu situación.\n\n"
    
    posiciones = [
        "Tú", "Relaciones", "Trabajo", "Espiritualidad",
        "Pasado", "Presente", "Futuro", "Consejo"
    ]
    
    for i, carta in enumerate(cartas):
        mensaje += f"*{i+1}. {posiciones[i]}:* {carta['nombre']}\n"
    
    await update.message.reply_text(mensaje, parse_mode='Markdown')

# ============================================
# EJERCICIO DE ADIVINACIÓN
# ============================================

async def ejercicio_arcanos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inicia un ejercicio de adivinación con Arcanos Mayores."""
    user_id = update.effective_user.id
    
    # Obtener Arcanos Mayores
    arcanos_mayores = obtener_arcanos_mayores()
    
    if not arcanos_mayores:
        await update.message.reply_text("Error: No se encontraron Arcanos Mayores.")
        return
    
    # Seleccionar carta objetivo
    carta_objetivo_nombre = random.choice(arcanos_mayores)
    
    # Guardar estado
    user_exercise_state[user_id] = {
        'carta_objetivo': carta_objetivo_nombre,
        'intentos': 0
    }
    
    await update.message.reply_text(
        "🧘‍♂️ *Ejercicio de Adivinación* 🧘‍♀️\n\n"
        "He elegido mentalmente un *Arcana Mayor*.\n"
        "Tu tarea es adivinar cuál es.\n\n"
        "*Instrucciones:*\n"
        "• Escribe el *nombre exacto* de la carta que crees que es\n"
        "• Usa /pista si necesitas ayuda\n"
        "• El ejercicio termina cuando aciertes\n\n"
        "Que comience el juego... 🎴",
        parse_mode='Markdown'
    )

async def pista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Da una pista sobre la carta del ejercicio."""
    user_id = update.effective_user.id
    
    if user_id not in user_exercise_state:
        await update.message.reply_text("Primero inicia el ejercicio con /ejercicio_arcanos.")
        return
    
    carta_objetivo_nombre = user_exercise_state[user_id]['carta_objetivo']
    carta_data = cartas_del_tarot[carta_objetivo_nombre]
    
    await update.message.reply_text(
        f"🔎 *Pista:*\n\n"
        f"*Palabras Clave:* {carta_data['palabras_clave']}",
        parse_mode='Markdown'
    )

async def manejar_respuesta_ejercicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja los mensajes de texto para el ejercicio."""
    user_id = update.effective_user.id
    texto_usuario = update.message.text.strip()
    
    # Si no está en ejercicio, ignorar
    if user_id not in user_exercise_state:
        return
    
    carta_objetivo_nombre = user_exercise_state[user_id]['carta_objetivo']
    
    # Comparación insensible a mayúsculas/minúsculas
    if texto_usuario.lower() == carta_objetivo_nombre.lower():
        carta_data = cartas_del_tarot[carta_objetivo_nombre]
        await update.message.reply_text(
            f"🎉 *¡Correcto!* Has adivinado la carta.\n\n"
            f"{formatear_mensaje_carta(carta_data)}",
            parse_mode='Markdown'
        )
        # Terminar ejercicio
        del user_exercise_state[user_id]
    else:
        user_exercise_state[user_id]['intentos'] += 1
        intentos = user_exercise_state[user_id]['intentos']
        await update.message.reply_text(
            f"❌ No es esa carta. Sigue intentando. (Intento #{intentos})\n\n"
            f"Recuerda: escribe el *nombre exacto* (ej: 'XIII. La Muerte')"
        )

# ============================================
# COMANDOS DE SABIDURÍA
# ============================================

async def ley(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /ley - Fragmento del Liber AL."""
    await update.message.reply_text(
        "📜 *Liber AL vel Legis*\n\n"
        "'El amor es la ley, el amor bajo voluntad.'\n"
        "— Capítulo I, verso 57\n\n"
        "'Cada hombre y cada mujer es una estrella.'\n"
        "— Capítulo I, verso 3\n\n"
        "'¡Haz tu voluntad: tal será la totalidad de la Ley!'\n"
        "— Capítulo I, verso 40",
        parse_mode='Markdown'
    )

async def liber(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /libertad - Reflexión sobre la libertad."""
    await update.message.reply_text(
        "🕊️ *Sobre la Libertad*\n\n"
        "La verdadera libertad no consiste en hacer lo que uno quiere,\n"
        "sino en ser lo que uno es.\n\n"
        "Cuando actúas desde tu centro más profundo,\n"
        "cuando tu voluntad se alinea con tu verdadera naturaleza,\n"
        "entonces eres libre.\n\n"
        "'La palabra de la Ley es Θελημα.'\n"
        "(Liber AL, I, 39)",
        parse_mode='Markdown'
    )

async def cuarenta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /40 - Significado del número 40."""
    await update.message.reply_text(
        "40 *El Número de la Realización*\n\n"
        "• 40 días en el desierto\n"
        "• 40 años de travesía\n"
        "• 40 días del diluvio\n"
        "• 40 semanas de gestación\n\n"
        "El 40 simboliza un *ciclo completo de transformación*,\n"
        "el período necesario para que lo viejo muera\n"
        "y lo nuevo nazca.\n\n"
        "En la Cábala, 40 es el valor de la letra *Mem* (מים),\n"
        "la letra del Agua, la disolución y el renacimiento.",
        parse_mode='Markdown'
    )

async def nagual(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /nagual - El guardián del umbral."""
    await update.message.reply_text(
        "🐆 *El Nagual*\n\n"
        "El Nagual es el *guardián del umbral*,\n"
        "el aspecto desconocido y salvaje de nuestro ser.\n\n"
        "Representa:\n"
        "• Lo que está más allá de la razón\n"
        "• La parte indomable del espíritu\n"
        "• El guía hacia lo impersonal\n"
        "• La conciencia que trasciende el ego\n\n"
        "En la tradición tolteca, el Nagual es el soñador,\n"
        "el que ve más allá de la ilusión.",
        parse_mode='Markdown'
    )

async def angel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /angel - El Santo Ángel Guardián."""
    await update.message.reply_text(
        "👼 *El Santo Ángel Guardián*\n\n"
        "Tu Santo Ángel Guardián es tu *Yo Superior*,\n"
        "la estrella que eres en esencia.\n\n"
        "El objetivo de la Gran Obra es el\n"
        "*Conocimiento y Conversación* con Él.\n\n"
        "No es un ser externo, sino tu propia naturaleza divina,\n"
        "tu voluntad más profunda manifestándose.\n\n"
        "'Busca y encontrarás; toca y se te abrirá.'",
        parse_mode='Markdown'
    )

# ============================================
# MANEJADOR DE ERRORES
# ============================================

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja errores del bot."""
    logger.warning(f"Error: {context.error}")
    try:
        if update and update.effective_message:
            await update.effective_message.reply_text(
                "⚠️ Ocurrió un error interno. Por favor, intenta de nuevo."
            )
    except:
        pass

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main() -> None:
    """Inicia el bot."""
    
    # Verificar token
    if BOT_TOKEN == "YOUR_TOKEN_HERE":
        print("❌ ERROR: Debes reemplazar 'YOUR_TOKEN_HERE' con el token de tu bot en main.py")
        return
    
    # Crear aplicación
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("thoth", thoth))
    
    # Lecturas
    application.add_handler(CommandHandler("carta_del_dia", carta_del_dia))
    application.add_handler(CommandHandler("tres_cartas", tres_cartas))
    application.add_handler(CommandHandler("cinco_cartas", cinco_cartas))
    application.add_handler(CommandHandler("ocho_cartas", ocho_cartas))
    
    # Ejercicio
    application.add_handler(CommandHandler("ejercicio_arcanos", ejercicio_arcanos))
    application.add_handler(CommandHandler("pista", pista))
    
    # Sabiduría
    application.add_handler(CommandHandler("ley", ley))
    application.add_handler(CommandHandler("libertad", liber))
    application.add_handler(CommandHandler("40", cuarenta))
    application.add_handler(CommandHandler("nagual", nagual))
    application.add_handler(CommandHandler("angel", angel))
    
    # Manejador para respuestas del ejercicio (debe ir después de los comandos)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_respuesta_ejercicio))
    
    # Manejador de errores
    application.add_error_handler(error_handler)
    
    # Iniciar bot
    print("🤖 Bot de Tarot Thoth iniciado...")
    print("Presiona Ctrl+C para detener")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
