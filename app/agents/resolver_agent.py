class ResolverAgent:
    async def resolve(self, stock_data: dict, sentiment_data: dict):
        
        price = stock_data["price"]
        sentiment = sentiment_data["sentiment"]
        score = sentiment_data["score"]

        # simple decision logic
        if sentiment == "positive" and score > 0:
            decision = "BUY"
        elif sentiment == "negative" and score < 0:
            decision = "SELL"
        else:
            decision = "HOLD"

        return {
            "symbol": stock_data["symbol"],
            "price": price,
            "sentiment": sentiment,
            "score": score,
            "decision": decision,
            "source": "ResolverAgent"
        }