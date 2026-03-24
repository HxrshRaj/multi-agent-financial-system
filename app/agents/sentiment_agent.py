import random

class SentimentAgent:
    async def analyze_sentiment(self, symbol: str):
        sentiments = ["positive", "neutral", "negative"]
        score = round(random.uniform(-1, 1), 2)

        return {
            "symbol": symbol,
            "sentiment": random.choice(sentiments),
            "score": score,
            "source": "SentimentAgent"
        }