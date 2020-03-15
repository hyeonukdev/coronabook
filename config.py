import os

TELEGRAM_TOKEN = '766379120:AAE_vH5kMUgGwMpoxgDK1vmOOcebeX69Pfc'
CHAT_ID = '-413959477'

if not TELEGRAM_TOKEN or not CHAT_ID:
    raise Exception('TELEGRAM_TOKEN, CHAT_ID 확인필요')

if __name__ == "__main__":
    print(TELEGRAM_TOKEN)
    print(CHAT_ID)
