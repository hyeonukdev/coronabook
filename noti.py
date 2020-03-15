from config import TELEGRAM_TOKEN, CHAT_ID
import requests as rq
import telegram

# bot_token
my_token = '766379120:AAE_vH5kMUgGwMpoxgDK1vmOOcebeX69Pfc'

# bot chat_id indivisual 770967266
# bot caht_id group -1001287771752
CHAT_ID = '-1001287771752'

bot = telegram.Bot(token=my_token)

updates = bot.getUpdates()


def send(t):
    bot.sendMessage(CHAT_ID, t, parse_mode=telegram.ParseMode.HTML)
    # rq.post('https://api.telegram.org/bot766379120:AAE_vH5kMUgGwMpoxgDK1vmOOcebeX69Pfc/sendMessage?chat_id=%s&text=%s'%(chat_id, t))
    # https://api.telegram.org/bot766379120:AAE_vH5kMUgGwMpoxgDK1vmOOcebeX69Pfc/getUpdates
