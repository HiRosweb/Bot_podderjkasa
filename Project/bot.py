from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = os.environ['TOKEN']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветственное сообщение с кнопками."""
    reply_keyboard = [["Норм", "Не очень"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет, как дела?", reply_markup=markup)

async def handle_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Реагирует на ответы пользователя."""
    text = update.message.text
    if text == "Норм":
        await update.message.reply_text("Удачи", reply_markup=ReplyKeyboardRemove())
    elif text == "Не очень":
        await update.message.reply_text("Все получится", reply_markup=ReplyKeyboardRemove())
    else:
        await update.message.reply_text("Пожалуйста, выберите вариант из кнопок.")

def main() -> None:
    """Запускает бота."""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_reply))

    print("Бот запущен!")
    application.run_polling()

if __name__ == "__main__":
    main()
