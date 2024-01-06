import telebot
import requests
import json

# Подключение
bot = telebot.TeleBot('6840296569:AAGuz7W67cXWpg6tyaN8PWNEhnq5ijz0LRg')
API = '3d9de74844d28377e81415151cbe6a66'


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Привет {message.from_user.first_name}!\nНапиши свой город!')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

    if weather.status_code == 200:
        data = json.loads(weather.text)
        temperature = data["main"]["temp"]
        bot.send_message(message.chat.id, f'Сегодня погода {temperature}°C')
    else:
        bot.send_message(message.chat.id, 'Не удалось получить данные о погоде. Пожалуйста, уточните город.')


bot.polling(none_stop=True)
