# Multi-Agent Financial Intelligence System

An AI-inspired multi-agent system that simulates financial data analysis by combining multiple independent agents into a unified decision-making pipeline.

##  Features

- Multi-agent architecture (Stock Agent, Sentiment Agent, Resolver Agent)
- Asynchronous FastAPI backend
- Parallel execution using asyncio for improved performance
- Modular and scalable project structure
- Docker-based containerization

##  CI/CD & Deployment

- Dockerfile included for containerization and scalable deployment
- Designed to integrate with CI/CD pipelines (e.g., GitHub Actions) for automated testing and deployment

##  Architecture

The system consists of three independent agents:

1. **StockAgent**
   - Simulates stock price retrieval

2. **SentimentAgent**
   - Generates sentiment analysis for financial assets

3. **ResolverAgent**
   - Combines outputs from all agents
   - Produces final BUY / SELL / HOLD decision

##  Performance Optimization

- Implemented `asyncio.gather()` to execute agents concurrently
- Improves response efficiency by parallelizing independent tasks

## 🛠 Tech Stack

- Python
- FastAPI
- AsyncIO
- Docker
- CI/CD (GitHub Actions - planned integration)


## 📂 Project Structure

```
app/
 ├── agents/
 │    ├── stock_agent.py
 │    ├── sentiment_agent.py
 │    ├── resolver_agent.py
 ├── main.py
tests/
 ├── test_api.py
```
## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Then open:
http://127.0.0.1:8000/analyze/AAPL

##  Future Improvements

- Integration with real financial APIs
- ML-based sentiment analysis
- CI/CD pipeline with GitHub Actions
- Cloud deployment (AWS/GCP)

---

## 👨‍💻 Author

Harsh Raj
