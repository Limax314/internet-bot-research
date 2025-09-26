import ccxt
import time

"""
.. module:: bithumb_iota_krw_bot

@remarks
여기서부터 작업 예정

https://www.mycompiler.io/view/JZ8KnKHgyKZ 업로드 예정
"""
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

    exchange.create_order(ticker, type="market", side="buy", amount=amount)

    print(f"[{i + 1}번째 계정] 매수 완료: {ticker} {amount}개")

    time.sleep(0.5)

    exchange.create_order(ticker, type="market", side="sell", amount=amount)

    print(f"[{i + 1}번째 계정] 매도 완료: {ticker} {amount}개")
