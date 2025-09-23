import ccxt
import time

# https://www.mycompiler.io/view/JZ8KnKHgyKZ 업로드 예정
info = [
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
]

ticker = "IOTA/KRW"

for i, account in enumerate(info):
    exchange = ccxt.bithumb(account)

    exchange.load_markets()

    current_price = exchange.fetch_order_book(ticker, limit=1)["asks"][0][0]
    amount = 5000  # current_price + 1

    exchange.create_order()
