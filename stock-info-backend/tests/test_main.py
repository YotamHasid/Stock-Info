from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_stock():
    response = client.get("/stock/MSFT")
    assert response.status_code == 200
    assert response.json()["symbol"] == "MSFT"
    assert "price" in response.json()  # לוודא שהמחיר נמצא בתגובה
    assert "change_percent" in response.json()  # לוודא שאחוז השינוי נמצא בתגובה
    assert "volume" in response.json()  # לוודא שכמות המסחר נמצאת בתגובה


def test_get_average_price():
    # בודק ממוצע מחיר של מספר מניות (כולל MSFT)
    response = client.post("/stocks/average", json=["MSFT", "TSLA", "GOOG"])
    
    # בודק שהממוצע מחושב כראוי
    assert response.status_code == 200
    assert "average_price" in response.json()

def test_compare_stocks():
    # מבצע השוואת מניות (כולל MSFT)
    response = client.post("/stocks/compare", json=["MSFT", "TSLA", "GOOG"])
    
    # בודק שהתשובה כוללת מניות עם מחירים גבוהים ונמוכים
    assert response.status_code == 200
    assert "highest" in response.json()
    assert "lowest" in response.json()
    assert "price" in response.json()["highest"]
    assert "price" in response.json()["lowest"]
