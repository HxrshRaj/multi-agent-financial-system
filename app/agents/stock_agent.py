import random

class StockAgent:
    async def get_stock_price(self, symbol: str):
        # simulate fetching stock data
        price = round(random.uniform(100, 500), 2)
        
        return {
            "symbol": symbol,
            "price": price,
            "source": "StockAgent"
        }