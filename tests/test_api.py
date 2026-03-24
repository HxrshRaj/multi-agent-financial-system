from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_endpoint():
    response = client.get("/analyze/AAPL")
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert "stock_data" in data
    assert "sentiment_data" in data
    assert "final_analysis" in data