import telebot
from config import BOT_TOKEN

# Create Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)

# Обрабатываем команды '/start' or '/help'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.reply_to(message, f"Welcome, {message.from_user.first_name}.\n"
                          f"Type \help for Help))")


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.reply_to(message, """
/help - this help
/start - start bot
/list - list of supported currencies
For converting currency type:
{CHAR_CODE_SOURCE} {CHAR_CODE_DEST} {AMOUNT}
    """)


@bot.message_handler(commands=['list'])
def handle_start_help(message):
    bot.reply_to(message, '')






# run telebot
bot.polling(none_stop=True)



