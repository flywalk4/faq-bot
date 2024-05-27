import telebot
import model
import json
import random

bot = telebot.TeleBot('6915195249:AAGUCEkIQIZ0oDGCaCTBhIxV4-yFlnqkqOs')
dialogue = {"greetings":
["Привет", "Ку", "Здравствуйте"],
"goodbye":["Пока", "Всего хорошего", "До свидания"],
"thanks":["спасибо","спасибо большое","благодарю"],
"gratitude":["Пожалуйста","Всегда пожалуйста","Обращайтесь еще"]}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """Здесь вы можете узнать ответы на часто задаваемые вопросы Сбербанка.\n
- Продукты: дебетовые, кредитные карты, кредиты, вклады, переводы, платежи\n
- Онлайн-сервисы: сбербанк онлайн, мобильное приложение, уведомления и выписки\n
- Решение проблем: аресты, безопасность, блокировки, наследство, доверенность, возвраты""")

@bot.message_handler(content_types=['text'])
def message(message):
    print("user", message.text)
    if message.text.lower() in dialogue["greetings"]:
       bot.send_message(message.chat.id, random.choice(dialogue["greetings"]))
    elif message.text.lower() in dialogue["goodbye"]:
       bot.send_message(message.chat.id, random.choice(dialogue["goodbye"]))
    elif message.text.lower() in dialogue["thanks"]:
       bot.send_message(message.chat.id, random.choice(dialogue["gratitude"]))
    else:
       answer = model.faq([message.text])
       conf = answer[1][0][answer[-1][0]]
       print("bot", conf)
       if conf <= 0.15:
         bot.send_message(message.chat.id, "Извините, сформулируйте вопрос по другому")
       else:
         bot.send_message(message.chat.id, answer)

bot.infinity_polling()