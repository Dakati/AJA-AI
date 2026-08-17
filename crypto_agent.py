import ccxt
import time
import csv
from datetime import datetime

# ============================================================
# AJA AI - MULTI-COIN PAPER PROFIT SCANNER
# Public market data only. NO real-money trading.
# ============================================================

EXCHANGES = {
    "Binance": ccxt.binance(),
    "Bybit": ccxt.bybit(),
}

SYMBOLS = [
    "BTC/USDT",
    "ETH/USDT",
    "SOL/USDT",
    "XRP/USDT",
]

TRADING_FEE_PERCENT = 0.10
SLIPPAGE_PERCENT = 0.05

TEST_CAPITAL_USDT = 1000.00
MIN_NET_PROFIT_USDT = 2.00

CSV_FILE = "crypto_scan_history.csv"


def get_orderbook(exchange_name, exchange, symbol):
    try:
        orderbook = exchange.fetch_order_book(symbol, limit=5)

        if not orderbook["bids"] or not orderbook["asks"]:
            return None, None

        best_bid = orderbook["bids"][0][0]
        best_ask = orderbook["asks"][0][0]

        return best_bid, best_ask

    except Exception as e:
        print(f"{exchange_name} {symbol}: unavailable")
        return None, None


def calculate_profit(buy_price, sell_price, capital):

    effective_buy = buy_price * (1 + SLIPPAGE_PERCENT / 100)
    effective_sell = sell_price * (1 - SLIPPAGE_PERCENT / 100)

    asset_amount = capital / effective_buy

    gross_revenue = asset_amount * effective_sell

    buy_fee = capital * (TRADING_FEE_PERCENT / 100)
    sell_fee = gross_revenue * (TRADING_FEE_PERCENT / 100)

    net_profit = gross_revenue - sell_fee - capital - buy_fee

    return net_profit


def save_result(symbol, buy_exchange, sell_exchange, net_profit):

    file_exists = False

    try:
        with open(CSV_FILE, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Time",
                "Pair",
                "Buy Exchange",
                "Sell Exchange",
                "Capital",
                "Estimated Net Profit"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            symbol,
            buy_exchange,
            sell_exchange,
            TEST_CAPITAL_USDT,
            round(net_profit, 4)
        ])


def scan_symbol(symbol):

    market_data = {}

    for name, exchange in EXCHANGES.items():

        bid, ask = get_orderbook(
            name,
            exchange,
            symbol
        )

        if bid is not None and ask is not None:

            market_data[name] = {
                "bid": bid,
                "ask": ask
            }

    if len(market_data) < 2:
        return

    buy_exchange = min(
        market_data,
        key=lambda x: market_data[x]["ask"]
    )

    sell_exchange = max(
        market_data,
        key=lambda x: market_data[x]["bid"]
    )

    buy_price = market_data[buy_exchange]["ask"]
    sell_price = market_data[sell_exchange]["bid"]

    net_profit = calculate_profit(
        buy_price,
        sell_price,
        TEST_CAPITAL_USDT
    )

    print(f"\n{symbol}")
    print(f"Buy  : {buy_exchange} @ ${buy_price:,.6f}")
    print(f"Sell : {sell_exchange} @ ${sell_price:,.6f}")
    print(f"Net  : ${net_profit:,.2f}")

    save_result(
        symbol,
        buy_exchange,
        sell_exchange,
        net_profit
    )

    if (
        buy_exchange != sell_exchange
        and net_profit >= MIN_NET_PROFIT_USDT
    ):
        print("⚠️ PAPER OPPORTUNITY")
        print("DO NOT TRADE AUTOMATICALLY")


def scan_market():

    print("\n" + "=" * 65)
    print("AJA AI - MULTI-COIN PAPER SCANNER")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 65)

    for symbol in SYMBOLS:
        scan_symbol(symbol)

    print("\nScan completed.")
    print(f"History saved to: {CSV_FILE}")
    print("=" * 65)


if __name__ == "__main__":

    while True:

        scan_market()

        print("\nNext scan in 60 seconds...")
        time.sleep(60)
