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
    update.message.reply_text(name_planet)
    

    if name_planet.lower() == 'mars':
        planet = ephem.Mars()
    elif name_planet.lower() == 'venus':
        planet = ephem.Venus()
    elif name_planet.lower() == 'mercury':
        planet = ephem.Mercury()
    elif name_planet.lower() == 'saturn':
        planet = ephem.Saturn()
    elif name_planet.lower() == 'jupiter':
        planet = ephem.Jupiter()
    elif name_planet.lower() == 'uranus':
        planet = ephem.Uranus()
    elif name_planet.lower() == 'moon':
        planet = ephem.Moon()
    elif name_planet.lower() == 'neptune':
        planet = ephem.Neptune()
    elif name_planet.lower() == 'pluto':
        planet = ephem.Pluto()
        print(datetime.today())
        planet.compute(datetime.today())
        update.message.reply_text(ephem.constellation(planet))
        print(ephem.constellation(planet))
    else:
        update.message.reply_text('Неизвестная планета.')

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