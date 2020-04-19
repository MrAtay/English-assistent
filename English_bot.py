from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import Englishbot.settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='English_bot.log')

def greet_user(bot, update):
    text = 'Привет! Я могу повторять ваши сообщения'
    logging.info(text)
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {0}!\nВы написали: {1}".format(update.message.chat.first_name, update.message.text)
    print(update.message)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.first_name,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(Englishbot.settings.API_KEY)
    
    logging.info('Бот запускается')
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
