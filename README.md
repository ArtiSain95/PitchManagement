# Pitch Health Monitoring System
The Pitch Health Monitoring System is a FastAPI-based web application designed to manage and monitor the health of sports pitches. It utilizes MongoDB for data storage and provides endpoints to perform CRUD operations on pitch data, track maintenance needs, and update pitch health based on environmental conditions.

## Project Structure

The project follows a modular structure for better organization and maintainability:

```plaintext
|-- PitchManagement
    |-- main.py
    |-- models.py
    |-- crud.py
    |-- database.py
    |-- weather.py
    |-- requirements.txt
```

- `main.py`: Contains the FastAPI application and routes.
- `models.py`: Defines the Pydantic data models used in the project.
- `crud.py`: Implements CRUD operations and business logic.
- `database.py`: Manages the MongoDB connection and database setup.
- `weather.py`: Fetch external weather data from a public API such as OpenWeatherMap.
- `requirements.txt`: Lists project dependencies and clear instructions for running the application locally.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/pitch-health-monitoring.git
    cd pitch-health-monitoring
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    ```bash
    uvicorn main:app --reload
    ```

    The application will be running at `http://127.0.0.1:8000`.

## MongoDB Configuration

Ensure you have MongoDB installed and running locally. The application uses MongoDB to store pitch data. Update the MongoDB connection string in `database.py` accordingly.

## API Documentation

Access the API documentation at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc` for an interactive API documentation.

## Endpoints

- **POST /pitches/**: Create a new pitch.
- **GET /pitches/**: Get all pitches.
- **GET /pitches/maintenance/**: Get pitches that need maintenance.
- **GET /pitches/replacement/**: Get pitches that need turf replacement.

# Fetch external weather data

This script allows you to retrieve weather information for a specific location using the OpenWeatherMap API.

## Usage

1. **Get API Key:**
    - Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) by signing up for a free account OR you can simplee use my API key `aaf06032e59c3fdc9ba082ef8667400`

2. **Navigate to Script Directory:**
    - Open a terminal or command prompt and navigate to the directory where the script (`weather.py`) is located.

3. **Run the Script:**
    - Execute the script with the following command:
        ```bash
        python weather.py --location <LOCATION_NAME> --api_key <YOUR_API_KEY>
        ```
        Replace `<LOCATION_NAME>` with the name of the location for which you want to retrieve weather information and `<YOUR_API_KEY>` with the API key obtained in Step 1.
        
        sample command to run:
        ```bash
        python weather.py --location Mumbai --api_key aaf06032e59c3fdc9ba082ef86674001
        ```

4. **View Weather Information:**
    - The script will fetch weather information from the OpenWeatherMap API and display the results in JSON format.

Note: Ensure that you have an active internet connection and the provided location name and API key are valid. The script uses the `requests` library to make API requests.


## ***Additional Point

- While the provided specifications do not explicitly require an API endpoint for updating the health condition of a pitch, we may need to update this information in the future. 
In such cases, we can implement a  separate PUT API endpoint to update an existing resource.
- Additionally, to ensure the reliability and maintainability of the codebase, we could consider adding unit tests. Unit tests help verify the correctness of individual components and catch regressions when making changes.
- Furthermore, Dockerization could be beneficial for easier deployment and scalability of the application. Docker allows for encapsulating the application and its dependencies into containers, making it simpler to manage across different environments. Integrating Docker into the project setup could enhance its portability and facilitate deployment processes.