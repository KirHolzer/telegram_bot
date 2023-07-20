import telebot
from data.my_data import Messege
from telebot import types
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Записаться на тренеровку')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Наша студия ')
    btn3 = types.KeyboardButton('Наши тренеры')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, F'Привет, {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Записаться на тренеровку')
def schedule_workout(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton('Понедельник')
    btn2 = types.KeyboardButton('Вторник')
    btn3 = types.KeyboardButton('Среда')
    btn4 = types.KeyboardButton('Четверг')
    btn5 = types.KeyboardButton('Пятница')
    btn6 = types.KeyboardButton('Суббота')
    btn7 = types.KeyboardButton('Воскресенье')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    bot.send_message(message.chat.id, 'Выберите удобный день для тренировки:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Наши тренеры')
def trainers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('CyberFox', url='')
    btn2 = types.InlineKeyboardButton('Оксана', url='https://www.google.com/?hl=ru')
    markup.add(btn1)
    markup.add(btn2)

    bot.send_message(message.chat.id, 'Наши CyberStars', reply_markup=markup)

bot.polling(none_stop=True)

#bot.infinity_polling()