import telebot
from telebot.types import
token="8525363907:AAFb3kZ2d6kXjakZi_atGCixoqHbmibcmB8"
bot=telebot.TeleBot (token)
@bot.message_handler(commands=[' start'])
def send (message) :
    markup=InlineKeyboardMarkup()
    about_button= InlineKeyboardButton("خصم 4 قنوات ممارسات فخمين بالفيسات🥵🔥1️⃣ ممارسات مشاهير تويتر بالفيسات 7000فيديو ‏2️⃣ قناه حصريات فخمين بالفيسات 3500فيديو 3️⃣قناه ممارسات بالفيسات 2600💦4️⃣قناه ممارساتي وخناثي🤦🏻‍♂️",callback='about')
    button1=InlineKeyboardButton("نبذه عن القنوات",callback_data="clarification")
    markup.add (about_button,button1)
    bot.send_message(message.chat.id,"اختر من الخيارات التالية",reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def call(call) :
    if call.data== "about":
        bot.send_photo(call.message.chat.id ,open=("pic/gay.jpg","rb"))
    elif call.data== "clarification":
        bot.send_(call.message.chat.id ,"نبذه عن القنوات")
print("البوت شغال")
bot.polling()

