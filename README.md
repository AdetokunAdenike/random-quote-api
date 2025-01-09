# Random Quote API

A RESTful API that provides random quotes. This project demonstrates backend development with Python (Flask) and CI/CD automation using Jenkins and Docker.

## Features
- **Fetch all quotes**: Retrieve a list of all available quotes.
- **Fetch a random quote**: Get a random quote from the collection.
- **Fetch a specific quote by ID**: Query a specific quote using its unique identifier.

## Technologies Used
- **Python**: Backend logic and API implementation.
- **Flask**: Lightweight web framework for building the API.
- **Jenkins**: CI/CD pipeline automation.
- **Docker**: Containerization for application deployment.

## API Endpoints
| Endpoint               | Method | Description                    |
|------------------------|--------|--------------------------------|
| `/api/quotes`          | `GET`  | Get all quotes                |
| `/api/quotes/random`   | `GET`  | Get a random quote            |
| `/api/quotes/<id>`     | `GET`  | Get a quote by its ID         |

## Getting Started
To set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AdetokunAdenike/random-quote-api.git
   cd random-quote-api

2. **Create a Virtual Environment (Recommended)**:
   ```bash
   python3 -m venv env
   source env/bin/activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the Application**:
   ```bash
   python app.py

5. **Access the API: Open your browser or use a tool like curl or Postman to interact with the API at:
   ```arduino
   http:127.0.0.1:5000

## Running with Docker
To run the application in a Docker container:

1. **Build the Docker Image**:
   ```bash
   docker build -t random-quote-api .

2. **Run the Docker Container**:
   ```bash
   docker run -d -p 5000:5000 random-quote-api

4. **Access the API**: Visit:
   ```arduino
   http://127.0.0.1:5000

## CI/CD Pipeline

- **CI/CD Authomation**: Implemented using jenkins.
- **Pipeline Stages**:
    1. **Checkout Code**: Pulls the latest code from the repository.
    2. **Build Docker Image**: Creates a Docker image of the application.
    3. **Run Unit Tests**: Executes automated tests to ensure code quality.
    4. **Deploy Application**: Deploys the Docker container.

## Testing

To run unit tests:
    ```bash
   pytest

## License

This project is licensed under the <a href="License" >MIT Licence</a>.
