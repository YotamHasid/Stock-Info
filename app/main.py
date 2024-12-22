import httpx
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

API_URL = "http://127.0.0.1:8080"
app = FastAPI()

# API key for Finnhub.io (כמו שהיה לך קודם)
API_KEY = "ctipj5pr01qgfbsv64f0ctipj5pr01qgfbsv64fg"
BASE_URL = "https://finnhub.io/api/v1/quote"

# מודל לתשובה על מניה
class StockResponse(BaseModel):
    symbol: str
    price: float
    change_percent: float
    volume: int

# פונקציה לקבלת מניה לפי סימול
@app.get("/stock/{symbol}", response_model=StockResponse)
async def get_stock(symbol: str):
    params = {
        'symbol': symbol,
        'token': API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            # בדיקה אם השדה 'v' קיים
            volume = data.get('v', 0)  # אם השדה לא קיים, ישתמש בערך 0
            return StockResponse(
                symbol=symbol.upper(),
                price=data['c'],  # מחיר נוכחי
                change_percent=data['dp'],  # אחוז שינוי במחיר
                volume=volume  # כמות המסחר או 0 אם לא קיים
            )


# פונקציה להשוואת מניות
@app.post("/stocks/compare")
async def compare_stocks(symbols: List[str]):
    stocks = []
    
    for symbol in symbols:
        stock_data = await get_stock(symbol)
        if "error" not in stock_data:
            stocks.append(stock_data.dict())
    
    highest = max(stocks, key=lambda x: x["price"])
    lowest = min(stocks, key=lambda x: x["price"])

    return {
        "highest": highest,
        "lowest": lowest
    }

# פונקציה לקבלת ממוצע מחיר של מניות
@app.post("/stocks/average")
async def get_average_price(symbols: List[str]):
    total_price = 0
    count = 0

    for symbol in symbols:
        stock_data = await get_stock(symbol)
        if "error" not in stock_data:
            total_price += stock_data.price
            count += 1

    average_price = total_price / count if count > 0 else 0
    return {"average_price": average_price}

@app.get("/")
def read_root():
    return {"message": "המערכת פועלת בהצלחה!"}
