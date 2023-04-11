import telebot
from config import token  # из файла config.py забираем нашу переменную с токеном
from telebot import types  # для работы с кнопками

# Создаем экземпляр бота
bot = telebot.TeleBot(token)


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Приветствуем Вас! Напишите: /go.')


@bot.message_handler(commands=["go"])
def inlinebutton_message(message):
    start_markup = telebot.types.InlineKeyboardMarkup()

    # первый ряд (две кнопки)
    btn1 = types.InlineKeyboardButton('Написать нам сообщение', callback_data='1')
    start_markup.row(btn1)

    # второй ряд (одна кнопка)
    btn2 = types.InlineKeyboardButton('Запись на посещение автосервиса', callback_data='2')
    start_markup.row(btn2)

    # третий ряд (две кнопки)
    btn3 = types.InlineKeyboardButton('Расчет стоимости выполнения работ', callback_data='3')
    start_markup.row(btn3)

    # четвертый ряд (две кнопки)
    btn4 = types.InlineKeyboardButton('Наши контакты', callback_data='4')
    start_markup.row(btn4)

    # пятый ряд (одна кнопка)
    btn5 = types.InlineKeyboardButton('Помощь в эвакуации авто', callback_data='5')
    start_markup.row(btn5)

    # шестой ряд (одна кнопка)
    btn6 = types.InlineKeyboardButton('Вернуться назад', callback_data='6')
    start_markup.row(btn6)

    bot.send_message(message.chat.id, 'InlineKeyboardButton', reply_markup=start_markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data in '1':
        bot.send_message(callback.message.chat.id, 'Опишите подробно свой вопрос')
    elif callback.data == '2':
        bot.send_message(callback.message.chat.id, '☎  Оставьте Ваш номер телефона для связи')
    elif callback.data in '3':
        bot.send_message(callback.message.chat.id, '''Для того, чтобы узнать расчёт стоимости выполнения работ 
ответьте на несколько вопросов: 
Какая у вас марка и модель авто
Введите объём двигателя
Выберите тип трансмиссии
Введите год выпуска авто
Введите пробег авто
Какие работы вы хотели бы произвести?''')

    elif callback.data in '4':
        bot.send_message(callback.message.chat.id, '''Адрес: г.Минск, ул.Бородинская 2Б, тел.+37529-674-21-23
Работаем как с физ. так и юр. лицами
Отчетные документы, заказ-наряд, чек.''')
    elif callback.data == '5':
        bot.send_message(callback.message.chat.id, 'Эвакуатор можно заказать у наших партнеров по тел. +37529-674-21-23')
    elif callback.data == '6':
        bot.send_message(callback.message.chat.id, 'Кнопка на доработке')


# Запускаем бота
bot.polling(none_stop=True, interval=0)

















