import telebot
from telebot import types

bot = telebot.TeleBot("7428099155:AAFSpJgGw--H8QmUiRf3fcE_xCQgZAut3pY")


@bot.message_handler(commands=['start'])
def start(message):
    # bot.send_message(message.from_user.id, "Привет, я бот для проверки Веб приложения")
    bot.send_message(message.chat.id, 'Привет, я бот для проверки телеграмм webapps!)', reply_markup=webAppKeyboard())


def webAppKeyboard():  # создание клавиатуры с webapp кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
    webAppTest = types.WebAppInfo("http://localhost:8080")  # создаем webappinfo - формат хранения url
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest)  # создаем кнопку типа webapp
    keyboard.add(one_butt)  # добавляем кнопки в клавиатуру

    return keyboard  # возвращаем клавиатуру


bot.polling(none_stop=True, interval=0)
