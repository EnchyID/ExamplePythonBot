import telebot
from telebot import TeleBot, types

bot = telebot.TeleBot("1395527061:AAEMPOUJm5-dl3B_wZE1H0JVdaPcUa8BD2E")

print("[Bot] Berjalan dengan baik!")

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(
        chat_id = message.chat.id, 
        text = "Selamat Datang Di @FrogasBot, " + message.chat.first_name, 
        reply_markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(text = "Konfirmasi!", callback_data = "cb_yes"), types.InlineKeyboardButton(text = "Bukan Saya!", callback_data = "cb_no"))
    )

@bot.message_handler(commands = ["send"])
def send(message):
	bot.reply_to(message, "Silakan ketik pesan lewat terminal anda!")
	id = input("Kepada nomor: ")
	args = input("Ketik Pesan: ")
	bot.send_message(chat_id = id, text = "Pesan dari " + message.chat.first_name + "\n" + args)
    
@bot.callback_query_handler(func = lambda call: True)
def iq_callback(query):
	data = query.data
	message = query.message
	if data == "cb_yes" :
		bot.answer_callback_query(query.id)
		bot.edit_message_text(
            text = "Berhasil!", 
            chat_id = message.chat.id, 
            message_id = message.message_id
        )
    
bot.polling()
