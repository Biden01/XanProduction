import telebot
from telebot import types

regions_kk = {'01': 'Астана',
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
regions_ru = {'01': 'Астана',
    '02':'Алматы',
    '03':'Акмолинская область',
    '04':'Актюбинская область',
    '05':'Алматинская область',
    '06':'Атырауская область',
    '07':'Западно-Казахстанская область',
    '08':'Жамбылская область',
    '09':'Карагандинская область',
    '10':'Костанайская область',
    '11':'Кызылординская область',
    '12':'Мангистауская область',
    '13':'Туркестанская область',
    '14':'Павлодарская область',
    '15':'Северо-Казахстанская область',
    '16':'Восточно-Казахстанская область',
    '17':'Шымкент',
    '18':'Абайская область',
    '19':'Жетісу',
    '20':'Улытауская область'}
abonent = {'+700':'АЛТЕЛ',
   '+701':'ACTIV',
   '+702':'ACTIV',
   '+705':'Beeline(Билайн)',
   '+707':'Tele2',
   '+708':'АЛТЕЛ',
   '+747':'Tele2',
   '+751':'«Казахтелеком» (передача данных)',
   '+760':'«Казахтелеком» (Спутниковая сеть Кулан)',
   '+761':'«Казахтелеком»',
   '+762':'АО «NURSAT»',
   '+763':'АО «Арна»',
   '+764':'«2 Day Telecom»',
   '+771':'Beeline(Билайн)',
   '+775':'АКТИФ',
   '+776':'Beeline(Билайн)',
   '+777':'Beeline(Билайн)',
   '+778':'ACTIV',
   '+997':'Код номер Казахстана',
   '+73':'Российская Федерация',
   '700':'АЛТЕЛ',
   '701':'ACTIV',
   '702':'ACTIV',
   '705':'Beeline(Билайн)',
   '707':'Tele2',
   '708':'АЛТЕЛ',
   '747':'Tele2',
   '751':'«Казахтелеком» (передача данных)',
   '760':'«Казахтелеком» (Спутниковая сеть Кулан)',
   '761':'«Казахтелеком»',
   '762':'АО «NURSAT»',
   '763':'АО «Арна»',
   '764':'«2 Day Telecom»',
   '771':'Beeline(Билайн)',
   '775':'АКТИФ',
   '776':'Beeline(Билайн)',
   '777':'Beeline(Билайн)',
   '778':'АКТИФ',
   '997':'Код номер Казахстана',
   '73':'Российская Федерация'}

api = "6769765002:AAGYb0llSWO1VhYWHaFjZd99Z0fNZRE1Uwk"
bot = telebot.TeleBot(api)
do = ""
lang = ""

@bot.message_handler(commands=["start"])
def send_welcome(message):
   if message.from_user.language_code == "ru":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Узнать абонента по номеру телефона")
      btn2 = types.KeyboardButton("Узнать регион по индексу")
      markup.add(btn1, btn2)
      bot.send_message(message.chat.id, text=f"Привет {message.chat.username}, наш бот определяет регион по индексу номера автомобиля, например: (01) и узнает абонента по номеру телефона, например: (+777)😇".format(message.from_user), reply_markup=markup)
      bot.register_next_step_handler(message, do_ru)

   elif message.from_user.language_code == "kk":
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Абонентті телефон нөмірі арқылы табу")
      btn2 = types.KeyboardButton("Индекс арқылы регион анықтау")
      markup.add(btn1, btn2)
      bot.send_message(message.chat.id, text=f"Сәлем {message.chat.username}, біздің бот көлік номеріндегі индексі арқылы өңірді анықтап береді Мысалы:(01) жәнеде телефон номердің абонентін анықтап береді Мысалы:(+777)😇".format(message.from_user), reply_markup=markup)
      bot.register_next_step_handler(message, do_ru)


def do_ru(message):
   global do, lang
   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   btn1 = types.KeyboardButton("Меню")
   markup.add(btn1)
   @bot.message_handler()
   def all(message):
      if message.from_user.language_code == "ru":
         if len(message.text) == 1 and do == "index_ru":
            message.text = "0" + message.text
         if message.text in regions_ru and do == "index_ru":
            bot.reply_to(message, regions_ru[message.text])
         elif message.text not in regions_ru and do == "index_ru" and message.text != "Меню":
            bot.reply_to(message, "Такого региона нету")
         if message.text[:4] in abonent and do == "index_number_ru":
            bot.reply_to(message, text=f"{abonent[message.text[:4]]}")
         elif message.text[:4] not in abonent and do == "index_number_ru" and message.text != "Меню":
            bot.reply_to(message, "Неправильно введен номер")
      elif message.from_user.language_code == "kk":
         if len(message.text) == 1 and do == "index_kk":
            message.text = "0" + message.text
         if message.text in regions_kk and do == "index_kk":
            bot.reply_to(message, regions_kk[message.text])
         elif message.text not in regions_kk and do == "index_kk" and message.text != "Меню":
            bot.reply_to(message, "Ондай регион жоқ")
         if message.text[:4] in abonent and do == "index_number_kk":
            bot.reply_to(message, abonent[message.text])
         elif message.text[:4] not in abonent and do == "index_number_kk" and message.text != "Меню":
            bot.reply_to(message, "Енгізілген нөмер қате")
      if message.text == "Меню" and message.from_user.language_code == "ru":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton("Узнать абонента по номеру телефона")
         btn2 = types.KeyboardButton("Узнать регион по индексу")
         markup.add(btn1,btn2)
         bot.send_message(message.chat.id,text=f"Привет {message.chat.username}, наш бот определяет регион по индексу номера автомобиля, например: (01) и узнает абонента по номеру телефона, например: (+777)😇".format(message.from_user), reply_markup=markup)
         bot.register_next_step_handler(message, do_ru)
      elif message.text == "Меню" and message.from_user.language_code == "kk":
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         btn1 = types.KeyboardButton("Абонентті телефон нөмірі арқылы табу")
         btn2 = types.KeyboardButton("Индекс арқылы регион анықтау")
         markup.add(btn1, btn2)
         bot.send_message(message.chat.id,text=f"Сәлем {message.chat.username}, біздің бот көлік номеріндегі индексі арқылы өңірді анықтап береді Мысалы:(01) жәнеде телефон номердің абонентін анықтап береді Мысалы:(+777)😇".format(message.from_user), reply_markup=markup)
         bot.register_next_step_handler(message, do_ru)
   if message.text == "Узнать регион по индексу":
      do = "index_ru"
      bot.send_message(message.chat.id, text="Напишите регион", reply_markup=markup)
   if message.text == "Индекс арқылы регион анықтау":
      do = "index_kk"
      bot.send_message(message.chat.id, text="Регион жазыныз", reply_markup=markup)
   if message.text == "Узнать абонента по номеру телефона":
      do = "index_number_ru"
      bot.send_message(message.chat.id, "Напишите номер телефона",reply_markup=markup)
   if message.text == "Абонентті телефон нөмірі арқылы табу":
      do = "index_number_kk"
      bot.send_message(message.chat.id, "Телефон нөмер жазыңыз",reply_markup=markup)


bot.infinity_polling()