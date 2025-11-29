import ccxt  # 암호화폐 거래소 트레이딩 라이브러리
import time  # 시간 표준 라이브러리

"""Bithumb IOTA/KRW 자동 거래 봇.

@description
- 이 스크립트는 Bithumb 거래소에서 IOTA/KRW 거래 쌍에 대한 자동 거래를 
수행합니다.
- 미리 설정된 여러 개의 계정 정보를 사용하여 각 계정에 대해 지정된 
수량만큼 시장가 매수 주문을 실행한 후 즉시 동일한 수량으로 시장가 
매도 주문을 실행합니다.
- [주요 기능]:
    - 다중 계정 지원(`info` 리스트에 여러 계쩡의 API 키와 시크릿 설정 
    가능).
    - 시장가 주문(`ccxt` 라이브러리를 사용하여 시장가 매수 및 매도 
    주문 생성).
    - 순차적 거래(설정된 계정 순서에 따라 순차적으로 매매 실행).
- [주의사항]:
    - `info` 리스트에 유효한 Bithumb API 키와 시크릿을 입력해야 합니다.
    - `ticker` 변수에 거래를 원하는 거래 쌍을 설정합니다.
    - `amount` 변수에 거래할 수량을 지정합니다.
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

for i, account in enumerate(info):  # 정의된 모든 계정에 대해 거래를 실행
    exchange = ccxt.bithumb(account)  # Bithumb 거래소 API 접속 객체

    exchange.load_markets()  # 현재 시장가를 `current_price` 변수에 저장

    """@remarks
여기서부터 주석 추가 예정
    """

    current_price = exchange.fetch_order_book(ticker, limit=1)["asks"][0][0]
    amount = 5000

    exchange.create_order(ticker, type="market", side="buy", amount=amount)

    print(f"[{i + 1}번째 계정] 매수 완료: {ticker} {amount}개")

    time.sleep(0.5)

    exchange.create_order(ticker, type="market", side="sell", amount=amount)

    print(f"[{i + 1}번째 계정] 매도 완료: {ticker} {amount}개")
