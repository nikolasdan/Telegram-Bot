import os
import telebot
from telebot.apihelper import API_URL
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey!")



bot.polling()