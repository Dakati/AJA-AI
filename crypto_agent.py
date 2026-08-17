import ccxt
import time

# ============================================================
# AJA AI - CRYPTO PAPER PROFIT SCANNER
# No API keys. No real-money trading.
# ============================================================

EXCHANGES = {
    "Binance": ccxt.binance(),
    "Bybit": ccxt.bybit(),
}

SYMBOL = "BTC/USDT"

# These are estimates only.
# Change them later after verifying the actual exchange fees.
TRADING_FEE_PERCENT = 0.10
SLIPPAGE_PERCENT = 0.05

TEST_CAPITAL_USDT = 1000.00
MIN_NET_PROFIT_USDT = 2.00


def get_orderbook(exchange_name, exchange):
    try:
        orderbook = exchange.fetch_order_book(SYMBOL, limit=5)

        best_bid = orderbook["bids"][0][0]
        best_ask = orderbook["asks"][0][0]

        return best_bid, best_ask

    except Exception as e:
        print(f"{exchange_name}: unavailable - {e}")
        return None, None


def calculate_profit(buy_price, sell_price, capital):
    # Approximate amount of BTC purchased
    btc_amount = capital / buy_price

    # Estimated slippage on both sides
    effective_buy = buy_price * (1 + SLIPPAGE_PERCENT / 100)
    effective_sell = sell_price * (1 - SLIPPAGE_PERCENT / 100)

    # Recalculate BTC amount using effective buy price
    btc_amount = capital / effective_buy

    gross_revenue = btc_amount * effective_sell

    # Estimated trading fees on buy and sell
    buy_fee = capital * (TRADING_FEE_PERCENT / 100)
    sell_fee = gross_revenue * (TRADING_FEE_PERCENT / 100)

    total_cost = capital + buy_fee
    net_revenue = gross_revenue - sell_fee

    net_profit = net_revenue - total_cost

    return net_profit


def scan_market():

    print("\n" + "=" * 60)
    print("AJA AI - CRYPTO PAPER PROFIT SCANNER")
    print("=" * 60)

    market_data = {}

    for name, exchange in EXCHANGES.items():

        bid, ask = get_orderbook(name, exchange)

        if bid is not None and ask is not None:

            market_data[name] = {
                "bid": bid,
                "ask": ask
            }

            print(
                f"{name:10} | "
                f"Bid: ${bid:,.2f} | "
                f"Ask: ${ask:,.2f}"
            )

    if len(market_data) < 2:
        print("\nNot enough exchange data.")
        return

    # Find cheapest ask (where we could theoretically buy)
    buy_exchange = min(
        market_data,
        key=lambda x: market_data[x]["ask"]
    )

    # Find highest bid (where we could theoretically sell)
    sell_exchange = max(
        market_data,
        key=lambda x: market_data[x]["bid"]
    )

    buy_price = market_data[buy_exchange]["ask"]
    sell_price = market_data[sell_exchange]["bid"]

    print("\n--- PAPER ARBITRAGE CHECK ---")

    print(f"Buy  : {buy_exchange} @ ${buy_price:,.2f}")
    print(f"Sell : {sell_exchange} @ ${sell_price:,.2f}")

    price_difference = sell_price - buy_price

    print(f"Price difference: ${price_difference:,.2f}")

    net_profit = calculate_profit(
        buy_price,
        sell_price,
        TEST_CAPITAL_USDT
    )

    print(f"\nTest capital : ${TEST_CAPITAL_USDT:,.2f}")
    print(f"Estimated net profit: ${net_profit:,.2f}")

    if buy_exchange == sell_exchange:
        print("\nNo cross-exchange opportunity.")

    elif net_profit >= MIN_NET_PROFIT_USDT:
        print("\n⚠️ POSSIBLE PAPER OPPORTUNITY")
        print("Do NOT trade automatically.")
        print("Verify fees, liquidity, withdrawal costs and transfer time.")

    else:
        print("\nNo profitable opportunity after estimated costs.")

    print("=" * 60)


if __name__ == "__main__":

    while True:
        scan_market()

        print("\nNext scan in 60 seconds...")
        time.sleep(60)
