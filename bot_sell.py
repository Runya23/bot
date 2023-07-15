import telebot
from telebot import types

TOKEN = '6323655965:AAFslqevr7HRylg4cvjxhfa1IDpwicqZwo0'

bot = telebot.TeleBot(TOKEN)

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Начнем')
keyboard.add(btn1)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте, я Ваш бот-консультант', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def check_answer(message):
    chat_id = message.chat.id
    if message.text == 'Начнем':
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Оформление заказа')
        btn2 = types.KeyboardButton('Оплата')
        btn3 = types.KeyboardButton('Сроки доставки')
        btn4 = types.KeyboardButton('Связаться с менеджером')
        btn5 = types.KeyboardButton('Стоимость доставки')
        keyboard1.add(btn1, btn2, btn3, btn4, btn5)   
        bot.send_message(chat_id, 'Выберите тему вопроса', reply_markup=keyboard1)
        
    elif message.text == 'Сроки доставки':
        bot.send_message(chat_id, f'Доставка занимает 10-12 рабочих дней')
    elif message.text == 'Оформление заказа':
        bot.send_message(chat_id, f'Отправьте ссылку товара')
    elif message.text == 'Стоимость доставки':
        bot.send_message(chat_id, f'Доставка от 150 сом\n\nДоставка свыше 2000 сом бесплатно\n\nДоставка регионы 300 сом')
    elif message.text == 'Оплата':
        bot.send_message(chat_id, f'Наши реквизиты:\n\nОптима:4169 5577 3456 7899\n\nMBank 0700-766-345')
    elif message.text == 'Связаться с менеджером':
        bot.send_message(chat_id, f'Менеджер свяжется с вами в течение получаса. Ожидайте звонка')

bot.polling()

