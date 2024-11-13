#bot1
import random
import telebot
bot = telebot.TeleBot('')
from telebot import types

first = ["Невероятные скидки на", "Вам сегодня повезло! Скидка на", "Отличные новости, сегодня скидка на"]
second = ["Видеокарты", "Процессоры", "Материнские платы", "Мониторы"]
number = ["15% для Вас", "20% для Вас", "25% для Вас"]
third = ["при первой покупке!", "при покупке от 1000 рублей!", "при регистрации чека на нашем сайте!"]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
 if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, что Вас сегодня интересует?")
    
    keyboard = types.InlineKeyboardMarkup()
    key_Komplect = types.InlineKeyboardButton(text='Комплектующие', callback_data='layer1')
    keyboard.add(key_Komplect)
    key_Sredstva = types.InlineKeyboardButton(text='Средства ухода и защиты', callback_data='layer1')
    keyboard.add(key_Sredstva)
    key_Ustroysva = types.InlineKeyboardButton(text='Устройства ввода и вывода', callback_data='layer1')
    keyboard.add(key_Ustroysva)
    bot.send_message(message.from_user.id, text='Выберите категорию товара', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "layer1":
        mgs = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(number) + ' ' + random.choice(third)
    bot.send_message(call.message.chat.id, mgs)
    
@bot.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
 await bot.send_message(web_app_message.chat.id, DISC[f'{web_app_message.web_app_data}'])

DISC = {
    '1': 'Материнская плата является связующим звеном всех комплектующих компьютера', 
    '2': 'Жёсткий диск является памятью компьютера'
}

bot.polling(none_stop=True, interval=0)