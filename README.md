# Stock Info Backend

This is a backend service for a stock information system. The backend is built using FastAPI and connects to external APIs (e.g., Finnhub) to fetch stock data. It also includes caching mechanisms to improve performance and reduce the number of external requests.

## ✨ Features

### For Users
- 📈 Get real-time stock data, including price, change percentage, and trading volume.
- 🔍 Compare multiple stocks and find the highest and lowest prices.
- 📊 Calculate the average stock price for a list of stocks.

### General Features
- 🚀 FastAPI for a high-performance backend.
- 🕒 Caching of stock data for faster responses .
- 🧑‍💻 API Documentation available via Swagger UI at `/docs`.

## 🚀 Getting Started

### Docker Setup (Recommended)

1. Ensure you have Docker installed on your machine.
2. Clone this repository to your local machine.
3. Create a `.env` file in the root directory with your `FINNHUB_API_KEY`.

#### Docker Setup

Create a `docker-compose.yml` file in the root directory:

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - FINNHUB_API_KEY=your_api_key_here
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Run the application:
docker-compose up --build

Access the application:
Backend API: http://localhost:8000
API Documentation: http://localhost:8000/docs
Manual Setup
Clone this repository to your local machine.

Create a .env file and add the following:
FINNHUB_API_KEY=your_api_key_here

Install dependencies:
pip install -r requirements.txt

Run the application:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

Access the application:
Backend API: http://localhost:8000
API Documentation: http://localhost:8000/docs

🏗️ Architecture:
Backend
FastAPI: Modern, fast web framework for building APIs with Python.
Pydantic: Data validation using Python type annotations.
HTTPX: HTTP client for making asynchronous requests.

📁 Project Structure:

app/
│
├── main.py         # FastAPI application entry point
├── models.py       # Pydantic models for stock data
├── services.py     # Logic for fetching and caching stock data
└── .env            # Environment variables file (e.g., FINNHUB_API_KEY)

📝 API Documentation:
After running the backend server, visit:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

🛠️ Testing
Run the backend tests using pytest:
pytest

🌟 Contributing:
Fork the repository.
Create your feature branch: git checkout -b feature/AmazingFeature.
Commit your changes: git commit -m 'Add some AmazingFeature'.
Push to the branch: git push origin feature/AmazingFeature.
Open a Pull Request.
👏 Acknowledgments:
FastAPI documentation
Finnhub API documentation
