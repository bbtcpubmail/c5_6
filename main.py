import telebot
from config import BOT_TOKEN
from extensions import Exchanger, ExchangeException

# Create Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)


# Обрабатываем команды '/start' or '/help'.
@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.reply_to(message, f"Welcome, {message.from_user.first_name}.\n"
                          f"Type /help for Help))")


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.reply_to(message, """
/help - this help
/start - start bot
/values - list of supported currencies
For converting currency type:
{CHAR_CODE_BASE} {CHAR_CODE_TARGET} {AMOUNT}
    """)


@bot.message_handler(commands=['values'])
def handle_list_currencies(message):
    bot.reply_to(message, Exchanger.get_currencies())


@bot.message_handler(content_types=['text'])
def handle_cur_exchange(message):
    try:
        text = Exchanger.parse_message(message)
    except ExchangeException as e:
        bot.reply_to(message, e)
    else:
        bot.reply_to(message, text)


# run telebot
bot.polling(none_stop=True)



