import telebot
from telebot import types

regions = {'01':'Астана',
   '02':'Алматы',
   '03':'Ақмола облысы',
   '04':'Ақтөбе облысы',
   '05':'Алматы облысы',
   '06':'Атырау облысы',
   '07':'Батыс-Қазақстан облысы',
   '08':'Жамбыл обылысы',
   '09':'Қарағанды облысы',
   '10':'Қостанай облысы',
   '11':'Қызылорда облысы',
   '12':'Манғыстау облысы',
   '13':'Түркістан облысы',
   '14':'Павлодар облысы',
   '15':'Солтүстік-Қазақстан облысы',
   '16':'Шығыс-Қазақстан облысы',
   '17':'Шымкент',
   '18':'Абай обылысы',
   '19':'Жетісу обылысы',
   '20':'Ұлытау обылысы'}

api = "6769765002:AAGYb0llSWO1VhYWHaFjZd99Z0fNZRE1Uwk"
lang = "KZ"
bot = telebot.TeleBot(api)
@bot.message_handler(commands=["start"])
def send_w(message):
   global lang
   if lang == "RU":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("👋")
      btn2 = types.KeyboardButton("Тілді өзгерту")
      btn3 = types.KeyboardButton("Узнать регион по индексу")
      markup.add(btn1,btn2, btn3)
      bot.send_message(message.chat.id,"Здравствуйте пользователь, наш бот определяет регион по индексу номера автомобиля, например: (01) и узнает абонента по номеру телефона, например: (+777)😇".format(message.from_user), reply_markup=markup)
   elif lang == "KZ":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("👋")
      btn2 = types.KeyboardButton("Тілді өзгерту")
      btn3 = types.KeyboardButton("Узнать регион по индексу")
      markup.add(btn1,btn2,btn3)
      bot.send_message(message.chat.id,"Сәлем қолданушы, біздің бот көлік номеріндегі индексі арқылы өңірді анықтап береді Мысалы:(01) жәнеде телефон номердің абонентін анықтап береді Мысалы:(+777)😇".format(message.from_user), reply_markup=markup)

@bot.message_handler(func=lambda a:True)
def send_welcome(message):
   global lang
   if len(message.text) == 1:
      message.text = "0" + message.text
   if lang == "KZ":
      if message.text == "Тілді өзгерту":
         markup = types.ReplyKeyboardMarkup()
         btn1 = types.KeyboardButton("RU🇷🇺")
         btn2 = types.KeyboardButton("KZ🇰🇿")
         markup.add(btn1,btn2)
         bot.send_message(message.chat.id, text="Тілді таңданыз".format(message.from_user), reply_markup=markup)
         if message.text == "RU🇷🇺":
            lang = "RU"
         elif message.text == "KZ🇰🇿":
            lang = "KZ"
      if message.text == "Индекс арқылы регион анықтау":
         if message.text in regions:
            bot.reply_to(message,regions[message.text])
         else:
            bot.reply_to(message,"Ондай регион жоқ")
   elif lang == "RU":
      if message.text == "Изменить язык":
         markup = types.ReplyKeyboardMarkup()
         btn1 = types.KeyboardButton("RU🇷🇺")
         btn2 = types.KeyboardButton("KZ🇰🇿")
         markup.add(btn1, btn2)
         bot.send_message(message.chat.id, text="Выберите язык".format(message.from_user), reply_markup=markup)
         if message.text == "RU🇷🇺":
            lang = "RU"
         elif message.text == "KZ🇰🇿":
            lang = "KZ"
      if message.text == "Узнать регион по индексу":
         if message.text in regions:
            bot.reply_to(message, regions[message.text])
         else:
            bot.reply_to(message, "Такого региона нету")
   with open("monitoring.txt", "a", encoding="utf-8") as f:
      f.write(str(message) + "\n")

bot.infinity_polling()