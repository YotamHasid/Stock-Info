import pytest
import httpx
from app.main import API_URL

@pytest.mark.asyncio
async def test_get_stock():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/stock/MSFT")
    assert response.status_code == 200
    data = response.json()
    assert "symbol" in data
    assert "price" in data
    assert "change_percent" in data
    assert "volume" in data

@pytest.mark.asyncio
async def test_compare_stocks():
    payload = ["AAPL", "MSFT", "GOOG"]
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_URL}/stocks/compare", json=payload)
    assert response.status_code == 200
    data = response.json()
    
    # עדכון: לוודא שקיימת כמות מסחר גם ב-highest וגם ב-lowest
    assert "highest" in data
    assert "lowest" in data
    assert "volume" in data["highest"]  # volume נמצא תחת highest
    assert "volume" in data["lowest"]  # volume נמצא תחת lowest

@pytest.mark.asyncio
async def test_get_average_price():
    payload = ["MSFT", "TSLA", "GOOG"]
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_URL}/stocks/average", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "average_price" in data
