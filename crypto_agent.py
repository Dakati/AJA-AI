import ccxt
import time
import csv
from datetime import datetime

# ============================================================
# AJA AI - CRYPTO OPPORTUNITY SCORER
# PAPER MODE ONLY - NO REAL TRADING
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

# Minimum profit required before considering an opportunity
MIN_NET_PROFIT_USDT = 2.00

# Minimum score required for WATCH
WATCH_SCORE = 70

CSV_FILE = "crypto_scan_history.csv"


def get_orderbook(exchange_name, exchange, symbol):
    try:
        orderbook = exchange.fetch_order_book(symbol, limit=10)

        if not orderbook["bids"] or not orderbook["asks"]:
            return None

        bid_price = orderbook["bids"][0][0]
        bid_amount = orderbook["bids"][0][1]

        ask_price = orderbook["asks"][0][0]
        ask_amount = orderbook["asks"][0][1]

        return {
            "bid": bid_price,
            "bid_amount": bid_amount,
            "ask": ask_price,
            "ask_amount": ask_amount
        }

    except Exception:
        return None


def calculate_profit(buy_price, sell_price, capital):

    effective_buy = buy_price * (1 + SLIPPAGE_PERCENT / 100)
    effective_sell = sell_price * (1 - SLIPPAGE_PERCENT / 100)

    asset_amount = capital / effective_buy

    revenue = asset_amount * effective_sell

    buy_fee = capital * (TRADING_FEE_PERCENT / 100)
    sell_fee = revenue * (TRADING_FEE_PERCENT / 100)

    net_profit = revenue - sell_fee - capital - buy_fee

    return net_profit


def calculate_score(net_profit, spread_percent, liquidity):

    score = 0

    # Profit score
    if net_profit >= 20:
        score += 40
    elif net_profit >= 10:
        score += 30
    elif net_profit >= 5:
        score += 20
    elif net_profit >= MIN_NET_PROFIT_USDT:
        score += 10

    # Spread score
    if spread_percent >= 1.0:
        score += 30
    elif spread_percent >= 0.5:
        score += 20
    elif spread_percent >= 0.2:
        score += 10

    # Liquidity score
    if liquidity == "GOOD":
        score += 30
    elif liquidity == "MEDIUM":
        score += 15

    return min(score, 100)


def save_result(
    symbol,
    buy_exchange,
    sell_exchange,
    net_profit,
    score,
    decision
):

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
                "Net Profit",
                "Score",
                "Decision"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            symbol,
            buy_exchange,
            sell_exchange,
            TEST_CAPITAL_USDT,
            round(net_profit, 4),
            score,
            decision
        ])


def scan_symbol(symbol):

    market_data = {}

    for name, exchange in EXCHANGES.items():

        data = get_orderbook(
            name,
            exchange,
            symbol
        )

        if data:
            market_data[name] = data

    if len(market_data) < 2:
        print(f"\n{symbol}: insufficient market data")
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

    buy_liquidity = market_data[buy_exchange]["ask_amount"]
    sell_liquidity = market_data[sell_exchange]["bid_amount"]

    minimum_liquidity = min(
        buy_liquidity,
        sell_liquidity
    )

    if minimum_liquidity > 1:
        liquidity = "GOOD"
    elif minimum_liquidity > 0.1:
        liquidity = "MEDIUM"
    else:
        liquidity = "LOW"

    spread_percent = (
        (sell_price - buy_price)
        / buy_price
    ) * 100

    net_profit = calculate_profit(
        buy_price,
        sell_price,
        TEST_CAPITAL_USDT
    )

    score = calculate_score(
        net_profit,
        spread_percent,
        liquidity
    )

    if buy_exchange == sell_exchange:
        decision = "REJECT"

    elif net_profit < MIN_NET_PROFIT_USDT:
        decision = "REJECT"

    elif liquidity == "LOW":
        decision = "REJECT"

    elif score >= WATCH_SCORE:
        decision = "WATCH"

    else:
        decision = "REJECT"

    print("\n" + "-" * 55)
    print(symbol)

    print(
        f"Buy  : {buy_exchange} @ "
        f"${buy_price:,.6f}"
    )

    print(
        f"Sell : {sell_exchange} @ "
        f"${sell_price:,.6f}"
    )

    print(
        f"Spread       : {spread_percent:.3f}%"
    )

    print(
        f"Net Profit   : "
        f"${net_profit:,.2f}"
    )

    print(
        f"Liquidity    : {liquidity}"
    )

    print(
        f"Opportunity Score : {score}/100"
    )

    print(
        f"Decision     : {decision}"
    )

    if decision == "WATCH":
        print("🟢 PAPER OPPORTUNITY")
        print("⚠️ Do NOT place a real order.")

    else:
        print("🔴 REJECT")

    save_result(
        symbol,
        buy_exchange,
        sell_exchange,
        net_profit,
        score,
        decision
    )


def scan_market():

    print("\n" + "=" * 65)
    print("AJA AI - OPPORTUNITY SCORER")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 65)

    for symbol in SYMBOLS:
        scan_symbol(symbol)

    print("\nScan completed.")
    print(f"History: {CSV_FILE}")
    print("=" * 65)


if __name__ == "__main__":

    while True:

        scan_market()

        print("\nNext scan in 60 seconds...")
        time.sleep(60)
