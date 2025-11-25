import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8525363907:AAFb3kZ2d6kXjakZi_atGCixoqHbmibcmB8"
bot = telebot.TeleBot(TOKEN)

# ▼ زر إرسال فيديو
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("نبذه عن القنوات")
    keyboard.add(btn)
    bot.send_message(message.chat.id, "اختر:", reply_markup=keyboard)


# ▼ عند الضغط على الزر
@bot.message_handler(func=lambda msg: msg.text == " نبذه عن القنوات")
def ask_for_video(message):
    bot.send_message(message.chat.id, "....أرسل الفيديو الآن من المعرض.")


# ▼ استقبال الفيديو
@bot.message_handler(content_types=['video'])
def receive_video(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded = bot.download_file(file_info.file_path)

    # حفظ الفيديو
    with open("received_video.mp4", "wb") as f:
        f.write(downloaded)

    bot.reply_to(message, "✔ تم استلام الفيديو!")


bot.infinity_polling()