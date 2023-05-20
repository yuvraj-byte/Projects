import requests
import telegram
import time

# Replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram bot token
bot_token = '6056102103:AAFKdFbKN_k4-f2yCQWrW0GMzJBtnH7Bw0s'

# Replace YOUR_TELEGRAM_CHAT_ID with your actual Telegram chat ID
chat_id = '1001806310999'
bot=telegram.Bot(bot_token)

# Define the symbol you want to get the price of
symbol = 'CFXUSDT'
while True:
# Define the Binance API endpoint for the ticker price of the symbol
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
    data = requests.get(url).json()

    price=data['price']
    print(price)
    def send_msg(text):
        if float(price)<0.29 or float(price)>0.3010:
            url_req="https://api.telegram.org/bot6056102103:AAFKdFbKN_k4-f2yCQWrW0GMzJBtnH7Bw0s/sendMessage?chat_id=@crupdat&text="+"CFX PRICE = "+text
            results = requests.get(url_req)
    send_msg(price) 

    time.sleep(1)
