# multi-agent-financial-system
# Multi-Agent Financial Intelligence System

An AI-inspired multi-agent system that simulates financial data analysis by combining multiple independent agents into a unified decision-making pipeline.

##  Features

- Multi-agent architecture (Stock Agent, Sentiment Agent, Resolver Agent)
- Asynchronous FastAPI backend
- Parallel execution using asyncio for improved performance
- Modular and scalable project structure
- Docker-ready deployment setup

##  Architecture

The system consists of three independent agents:

1. **StockAgent**
   - Simulates stock price retrieval

2. **SentimentAgent**
   - Generates sentiment analysis for financial assets

3. **ResolverAgent**
   - Combines outputs from all agents
   - Produces final BUY / SELL / HOLD decision

## ⚡ Performance Optimization

- Implemented `asyncio.gather()` to execute agents concurrently
- Reduces response latency and improves throughput

## 🛠 Tech Stack

- Python
- FastAPI
- AsyncIO
- Docker (containerization ready)

## 📂 Project Structure
app/
├── agents/
│ ├── stock_agent.py
│ ├── sentiment_agent.py
│ ├── resolver_agent.py
├── main.py

## ▶ How to Run

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

Then open:
http://127.0.0.1:8000/analyze/AAPL

 Future Improvements
Real-time financial API integration
ML-based sentiment analysis
Database integration
CI/CD pipeline with GitHub Actions
👨‍💻 Author

Harsh Raj
