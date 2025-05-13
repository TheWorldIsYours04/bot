import logging
import settings
from telegram.ext import Application, CommandHandler, MessageHandler, filters

logging.basicConfig(filename="bot.log", level=logging.INFO)

async def greet_user(update, context):
    print("Вызван /start")
    await update.message.reply_text("Здравствуй, пользователь")

async def talk_to_me(update, context):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():
    mybot = Application.builder().token(settings.API_KEY).build()

    mybot.add_handler(CommandHandler("start", greet_user))
    mybot.add_handler(MessageHandler(filters.TEXT, talk_to_me))

    logging.info("Бот стартовал")  # Используем logging.info() вместо logging.INFO()

    mybot.run_polling()

if __name__ == '__main__':
    main()