# Stock-Info

This is a full-stack web application designed to provide real-time stock market data. The backend is built using **FastAPI** and serves as an API that provides various stock-related data such as price, volume, and comparisons. The application is containerized using Docker, and it is easy to deploy and test using Docker and Docker Compose.

## Features

- **Backend (FastAPI)**: Handles all the business logic and provides RESTful API endpoints for stock data.
- **Frontend (React)**: Displays stock data, enables comparisons, and integrates with the backend to show the user real-time stock information.
- **Dockerized**: The application is containerized for easy deployment and testing.

### Clone the Repository
Clone the repository to your local machine:

Copy code
git clone https://github.com/YotamHasid/stock-info-backend.git
cd stock-info-backend

### Access the Application
Once the containers are running, you can access the frontend in your browser:

Frontend: Open http://localhost:3000 to view the web application.
Backend API: Open http://localhost:8000/docs to interact with the API using Swagger.

#### How to Run the Application

#### Step 1: Install Dependencies
Before running the application, you need to install all required dependencies. You can do this by running:

pip install -r requirements.txt

#### Step 2: Build the Docker Image
To build the Docker image, run the following command:

docker build -t stock-info-backend .


#### Step 3: Run the Docker Container
After building the image, you can run the container using the following command:

docker run -p 8080:8000 stock-info-backend


#### Step 4: Access the Application
Once the container is running, the application will be exposed on port 8080 on your local machine. You can access it via the browser at:

http://127.0.0.1:8080


### API Key
Make sure to add your API key to the code so that the application can make requests to the Finnhub API. If you have your API key, use the following:

```python
API_KEY = "ctipj5pr01qgfbsv64f0ctipj5pr01qgfbsv64fg"


### Dockerfile
This project includes a Dockerfile to easily build and run the application in a containerized environment. The Dockerfile contains all the necessary steps to install dependencies, copy the project files, and start the FastAPI server.

### API Endpoints
The system provides several API endpoints, including:

1. **GET `/stock/{symbol}`**
   - Retrieves the stock information for the given symbol.

2. **POST `/stocks/average`**
   - Calculates and returns the average stock price for a list of symbols.

3. **POST `/stocks/compare`**
   - Compares multiple stocks and returns the highest and lowest stock based on price.

### Testing the Application
You can test the application using the `/docs` endpoint to access the automatically generated Swagger UI for API documentation. From there, you can test all the API functions.

To run automated tests on the application, use the following command:
pytest

This will run the test suite, ensuring that all functions are working as expected.

### Testing with Docker
You can run the backend tests inside the Docker container by using the following command:
docker-compose exec backend pytest

### License
This project is licensed under the MIT License - see the LICENSE file for details.

