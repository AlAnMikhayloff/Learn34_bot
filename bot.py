import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import datetime

logging.basicConfig(filename='bot.log', level=logging.INFO)

#PROXY = {'proxy_url': settings.PROXY_URL,
#    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def talk_about_planet(update, context):
    name_planet = update.message.text.split('/planet ')[1]
    update.message.reply_text(name_planet.capitalize())
       
    if name_planet.lower() == 'mars' or 'venus' or 'mercury' or 'saturn' or 'jupiter' or 'uranus' or 'moon' or 'neptune' or 'pluto':
        planet = getattr(ephem, name_planet.capitalize())()
        print(planet)

    else:
        update.message.reply_text('Неизвестная планета.')
    print(datetime.today())
    planet.compute(datetime.today())
    update.message.reply_text(ephem.constellation(planet))
    print(planet, ephem.constellation(planet))

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", talk_about_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, talk_about_planet))

    logging.info('Бот стартовал.')
    mybot.start_polling()
    mybot.idle()
main()