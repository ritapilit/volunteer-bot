from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

TOKEN = "8710152214:AAE-PQ6PTSt9AA2gOj7ATFH-XIjGhM-uLWY"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        ["📚 Получить бесплатный гайд"],
        ["💬 Записаться на консультацию"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Привет! 🌱\n\n"
        "Я Рита.\n\n"
        "Помогаю найти волонтерство в Германии и пройти путь от поиска программы до получения оффера.\n\n"
        "В бесплатном гайде ты узнаешь:\n\n"
        "✅ Где искать волонтерство\n"
        "✅ Какие программы подходят гражданам РФ\n"
        "✅ Что дают волонтерам\n"
        "✅ Нужен ли немецкий язык\n"
        "✅ Какие документы понадобятся\n\n"
        "Выбери нужный пункт 👇",
        reply_markup=reply_markup
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "📚 Получить бесплатный гайд":

        await update.message.reply_text(
            "Отправляю тебе бесплатный гайд 📚"
        )

        with open("guide.pdf", "rb") as pdf:
            await update.message.reply_document(pdf)

        await update.message.reply_text(
            "Если после прочтения захочешь получить персональную подборку программ под свою ситуацию, нажми кнопку:\n\n"
            "💬 Записаться на консультацию"
        )

    elif text == "💬 Записаться на консультацию":

        await update.message.reply_text(
            "Напиши мне в Telegram 👇\n\n"
            "👉 https://t.me/ritaa_pilit\n\n"
            "В сообщении укажи:\n"
            "• возраст\n"
            "• гражданство\n"
            "• уровень немецкого\n"
            "• когда хочешь уехать\n\n"
            "И я помогу подобрать подходящие программы 🌱"
        )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))

print("Бот запущен ✅")

app.run_polling()
