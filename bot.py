from datatime import datatime
import telebot
from pycbrf import ExchangeRates

bot = telebot.Telebot('config.token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('USD')
    itembtn2 = telebot.types.KeyboardButton('EUR')
    itembtn3 = telebot.types.KeyboardButton('RUB')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(chat_id=message.chat.id, text="<b>Hello! Choose the currency to see Exchange Rates! </b>", reply_markup=markup, parse_mode="html")

@bot.message.handler(content_types=['text'])
def message(message):
    message_norm = message.text.strip().lower()

    if message_norm in ['usd', 'eur','rub']:
        rates = ExchangeRates(datetime.now())
        bot.send_message(chat_id=message.chat.id, text=f"<b>{message_norm.upper()} rate is {float(rates[message_norm.upper()].rate)}</b>, parse_mode="html")

bot.polling(none_stop=True)