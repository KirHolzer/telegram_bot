import telebot
from data.my_data import Messege

bot = telebot.TeleBot('')

@bot.message_handler(commands = ['start'])
def main(messege):
    bot.send_message(messege.chat.id, Messege.greeting_messege)

bot.polling(none_stop=True)
#bot.infinity_polling()