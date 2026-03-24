from fastapi import FastAPI
from app.agents.stock_agent import StockAgent
from app.agents.sentiment_agent import SentimentAgent
from app.agents.resolver_agent import ResolverAgent

app = FastAPI()

stock_agent = StockAgent()
sentiment_agent = SentimentAgent()
resolver_agent = ResolverAgent()

@app.get("/")
async def root():
    return {"message": "Multi-Agent Financial System Running"}

@app.get("/analyze/{symbol}")
async def analyze(symbol: str):
    stock_data = await stock_agent.get_stock_price(symbol)
    sentiment_data = await sentiment_agent.analyze_sentiment(symbol)
    
    final_result = await resolver_agent.resolve(stock_data, sentiment_data)

    return {
        "stock_data": stock_data,
        "sentiment_data": sentiment_data,
        "final_analysis": final_result
    }