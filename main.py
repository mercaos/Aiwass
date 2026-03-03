# main.py - VERSIÓN SIMPLIFICADA (SOLO /thoth)
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from tarot_data import cartas_del_tarot, lista_de_cartas

# ============================================
# CONFIGURACIÓN
# ============================================
BOT_TOKEN = "token"  # <--- Reemplaza con tu token

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Estado para el ejercicio
user_exercise_state = {}

# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def obtener_carta_aleatoria():
    nombre_carta = random.choice(lista_de_cartas)
    return cartas_del_tarot[nombre_carta]

def formatear_mensaje_carta(carta_data):
    mensaje = f"🃏 *{carta_data['nombre']}*\n\n"
    mensaje += f"*Palabras Clave:* {carta_data['palabras_clave']}\n\n"
    mensaje += f"*Interpretación:* {carta_data['descripcion']}\n\n"
    mensaje += f"*Pregunta:* {carta_data['pregunta']}"
    return mensaje

def obtener_arcanos_mayores():
    return [nombre for nombre in lista_de_cartas if nombre[0].isdigit() or nombre.startswith('0.')]

# ============================================
# COMANDOS ACTIVOS
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mensaje de bienvenida."""
    await update.message.reply_text(
        "🌌 *Bienvenido al Oráculo de Thoth* 🌌\n\n"
        "Usa /thoth para ver todas las lecturas disponibles.\n\n"
        "Que la sabiduría te acompañe. ✨",
        parse_mode='Markdown'
    )

async def thoth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menú principal de lecturas."""
    await update.message.reply_text(
        "🔮 *Lecturas del Tarot de Thoth* 🔮\n\n"
        "• /carta_del_dia - Una carta para tu día\n"
        "• /tres_cartas - Pasado, Presente, Futuro\n"
        "• /cinco_cartas - Visión profunda de 5 cartas\n"
        "• /ocho_cartas - Análisis complejo de 8 cartas\n\n"
        "🎴 *Ejercicio:*\n"
        "• /ejercicio_arcanos - Entrena tu intuición\n"
        "• /pista - Pista para el ejercicio",
        parse_mode='Markdown'
    )

# ----- LECTURAS -----
async def carta_del_dia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    carta = obtener_carta_aleatoria()
    await update.message.reply_text(formatear_mensaje_carta(carta), parse_mode='Markdown')

async def tres_cartas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cartas = [obtener_carta_aleatoria() for _ in range(3)]
    mensaje = "🔮 *Tirada de Tres Cartas* 🔮\n\n"
    mensaje += f"*Pasado:* **{cartas[0]['nombre']}**\n➡️ {cartas[0]['palabras_clave']}\n\n"
    mensaje += f"*Presente:* **{cartas[1]['nombre']}**\n➡️ {cartas[1]['palabras_clave']}\n\n"
    mensaje += f"*Futuro:* **{cartas[2]['nombre']}**\n➡️ {cartas[2]['palabras_clave']}"
    await update.message.reply_text(mensaje, parse_mode='Markdown')

async def cinco_cartas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cartas = [obtener_carta_aleatoria() for _ in range(5)]
    posiciones = ["Situación", "Desafío", "Ayuda", "Fuerza", "Resultado"]
    mensaje = "🔮 *Tirada de Cinco Cartas* 🔮\n\n"
    for i, carta in enumerate(cartas):
        mensaje += f"*{i+1}. {posiciones[i]}:* **{carta['nombre']}**\n"
    await update.message.reply_text(mensaje, parse_mode='Markdown')

async def ocho_cartas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cartas = [obtener_carta_aleatoria() for _ in range(8)]
    posiciones = ["Tú", "Relaciones", "Trabajo", "Espíritu", "Pasado", "Presente", "Futuro", "Consejo"]
    mensaje = "🔮 *Tirada de Ocho Cartas* 🔮\n\n"
    for i, carta in enumerate(cartas):
        mensaje += f"*{i+1}. {posiciones[i]}:* {carta['nombre']}\n"
    await update.message.reply_text(mensaje, parse_mode='Markdown')

# ----- EJERCICIO -----
async def ejercicio_arcanos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    arcanos = obtener_arcanos_mayores()
    if not arcanos:
        await update.message.reply_text("Error: No hay Arcanos Mayores.")
        return
    
    carta_objetivo = random.choice(arcanos)
    user_exercise_state[user_id] = {'carta_objetivo': carta_objetivo, 'intentos': 0}
    
    await update.message.reply_text(
        "🧘‍♂️ *Ejercicio de Adivinación*\n\n"
        "Elegí un Arcana Mayor mentalmente.\n"
        "Escribe el *nombre exacto* de la carta que crees que es.\n"
        "Usa /pista si necesitas ayuda.\n\n"
        "¡Comienza! 🎴",
        parse_mode='Markdown'
    )

async def pista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_exercise_state:
        await update.message.reply_text("Primero usa /ejercicio_arcanos")
        return
    
    carta = user_exercise_state[user_id]['carta_objetivo']
    data = cartas_del_tarot[carta]
    await update.message.reply_text(
        f"🔎 *Pista:*\n\n{data['palabras_clave']}",
        parse_mode='Markdown'
    )

async def manejar_respuesta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in user_exercise_state:
        return
    
    texto = update.message.text.strip()
    objetivo = user_exercise_state[user_id]['carta_objetivo']
    
    if texto.lower() == objetivo.lower():
        data = cartas_del_tarot[objetivo]
        await update.message.reply_text(
            f"🎉 *¡Correcto!*\n\n{formatear_mensaje_carta(data)}",
            parse_mode='Markdown'
        )
        del user_exercise_state[user_id]
    else:
        user_exercise_state[user_id]['intentos'] += 1
        await update.message.reply_text(
            f"❌ No es esa. Intento #{user_exercise_state[user_id]['intentos']}"
        )

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    if BOT_TOKEN == "TU_TOKEN_AQUI":
        print("❌ ERROR: Debes poner tu token en main.py")
        return
    
    app = Application.builder().token(BOT_TOKEN).build()
    
    # SOLO ESTOS COMANDOS ESTÁN ACTIVOS
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("thoth", thoth))
    app.add_handler(CommandHandler("carta_del_dia", carta_del_dia))
    app.add_handler(CommandHandler("tres_cartas", tres_cartas))
    app.add_handler(CommandHandler("cinco_cartas", cinco_cartas))
    app.add_handler(CommandHandler("ocho_cartas", ocho_cartas))
    app.add_handler(CommandHandler("ejercicio_arcanos", ejercicio_arcanos))
    app.add_handler(CommandHandler("pista", pista))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_respuesta))
    
    print("🤖 Bot de Thoth iniciado (modo simplificado)")
    app.run_polling()

if __name__ == "__main__":
    main()



