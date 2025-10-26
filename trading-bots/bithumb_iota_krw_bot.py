import ccxt  # 암호화폐 거래소 트레이딩 라이브러리

"""
@remarks
여기서부터 주석 추가 예정
"""
import time

"""
.. module:: bithumb_iota_krw_bot.py
    :synopsis: Bithumb IOTA/KRW trading bot

Bithumb 거래소에서 여러 계정을 사용하여 IOTA/KRW 페어에 
대해 지정된 수량만큼 시장가 매수 후 즉시 시장가 매도하는 
스크립트입니다.
"""
info = [
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
    {"apiKey": "", "secret": ""},
]  # API 키와 시크릿을 포함하는 계정 정보

ticker = "IOTA/KRW"  # 거래할 페어

# 정의된 모든 계정에 대해 거래를 실행합니다.
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
