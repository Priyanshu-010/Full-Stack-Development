def get_stock_price(symbol: str):
    fake_prices = {
        "BTC": 60000,
        "ETH": 3000,
        "AAPL": 180
    }
    return fake_prices.get(symbol.upper(), "Not found")