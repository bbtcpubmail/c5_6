import telebot
from config import BOT_TOKEN
from extensions import Exchanger

# Create Telegram bot
bot = telebot.TeleBot(BOT_TOKEN)
exchanger = Exchanger()

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
/list - list of supported currencies
For converting currency type:
{CHAR_CODE_BASE} {CHAR_CODE_TARGET} {AMOUNT}
    """)


@bot.message_handler(commands=['list'])
def handle_list_currencies(message):
    bot.reply_to(message, exchanger.currencies)


@bot.message_handler(content_types=['text'])
def handle_cur_exchange(message):
    base_char, target_char, amount = message.text.split()
    bot.reply_to(message, Exchanger.cur_exchange(base_char, target_char, float(amount)))






# run telebot
bot.polling(none_stop=True)



