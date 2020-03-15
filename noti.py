from config import TELEGRAM_TOKEN, CHAT_ID
import requests as rq
import telegram

my_token = 'TELEGRAM_TOKEN'

bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()


def send(t):
    bot.sendMessage(CHAT_ID, t, parse_mode=telegram.ParseMode.HTML)
   