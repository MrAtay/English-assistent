import telebot
     
bot = telebot.TeleBot('1097876844:AAFQtOZ527sr43Qt2FjrtnGmnqUOp3XdDBE')

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Hi':
        bot.send_message(message.from_user.id, "Hello! I'm  LearningEnglishBot.\nHow can i help you?")
    elif message.text == 'How are you?':
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    else:
        bot.send_message(message.from_user.id, "Sorry, I don't undertand you.")
bot.polling(none_stop=True, interval=0)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# RUN
bot.polling(none_stop=True, interval=0)

"""
import os
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1097876844:AAFQtOZ527sr43Qt2FjrtnGmnqUOp3XdDBE'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.messege_handler(commands=['start', 'help'])
async def send_welcome(messege: types.Message):
    await messege.reply("Hi!\nI'm Learning English Bot")
    photo,
    caption = 'Cats are here',
    reply_to_message_id = message.message_id
    await message.reply_photo(photo, caption="Cats are here")"""

