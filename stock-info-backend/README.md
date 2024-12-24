
# Stock Info Backend

This is a backend system that retrieves real-time stock information using the Finnhub API.

## How to Run the Application

### Step 1: Install Dependencies
Before running the application, you need to install all required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

### Step 2: Build the Docker Image
To build the Docker image, run the following command:

```bash
docker build -t stock-info-backend .
```

### Step 3: Run the Docker Container
After building the image, you can run the container using the following command:

```bash
docker run -p 8080:8000 stock-info-backend
```

### Step 4: Access the Application
Once the container is running, the application will be exposed on port 8080 on your local machine. You can access it via the browser at:

```bash
http://127.0.0.1:8080
```

### API Key
Make sure to add your API key to the code so that the application can make requests to the Finnhub API. If you have your API key, use the following:

```python
API_KEY = "ctipj5pr01qgfbsv64f0ctipj5pr01qgfbsv64fg"
```

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

```bash
pytest
```

This will run the test suite, ensuring that all functions are working as expected.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
