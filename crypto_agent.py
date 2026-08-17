import ccxt
import time

# Public market-data only.
# No API keys and no real-money trading.

EXCHANGES = {
    "Binance": ccxt.binance(),
    "Bybit": ccxt.bybit(),
    "OKX": ccxt.okx(),
}

SYMBOL = "BTC/USDT"


def get_price(exchange_name, exchange):
    try:
        ticker = exchange.fetch_ticker(SYMBOL)
        return ticker["last"]
    except Exception as e:
        print(f"{exchange_name}: unavailable - {e}")
        return None


def scan_market():
    prices = {}

    print("\n" + "=" * 50)
    print("AJA AI CRYPTO MARKET SCANNER")
    print("=" * 50)

    for name, exchange in EXCHANGES.items():
        price = get_price(name, exchange)

        if price is not None:
            prices[name] = price
            print(f"{name:10} : ${price:,.2f}")

    if len(prices) >= 2:
        highest_exchange = max(prices, key=prices.get)
        lowest_exchange = min(prices, key=prices.get)

        highest = prices[highest_exchange]
        lowest = prices[lowest_exchange]

        difference = highest - lowest
        percentage = (difference / lowest) * 100

        print("\n--- Opportunity Scan ---")
        print(f"Lowest : {lowest_exchange} ${lowest:,.2f}")
        print(f"Highest: {highest_exchange} ${highest:,.2f}")
        print(f"Spread : ${difference:,.2f}")
        print(f"Spread %: {percentage:.3f}%")

        if percentage > 0.50:
            print("⚠️ POSSIBLE OPPORTUNITY - CHECK FEES & SLIPPAGE")
        else:
            print("No significant spread detected.")

    print("=" * 50)


if __name__ == "__main__":
    while True:
        scan_market()
        print("\nNext scan in 60 seconds...")
        time.sleep(60)
