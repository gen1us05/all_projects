import os
import telebot
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'salom'])
def send_welcome(message):
    bot.reply_to(message, f"{message.from_user}Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if message.json.text[0] == 'salom':
        bot.reply_to(f"salom {message.from_user.first_name}")
    else:
        bot.reply_to(message, f"Hi {message.from_user.first_name}, what's up")

if __name__ == "__main__":

    bot.infinity_polling()
