FastAPI Application 

This application is a simple RESTful API built using Python and the FastAPI framework. It demonstrates basic API functionalities including path and query parameters, error handling, and automatic API documentation. The application is containerized using Docker with a multi-stage build process managed by Poetry for dependencies.

The application provides the following API endpoints:

* 'GET /': Returns a "404 Not Found" error by design, indicating the root path is not a primary resource.
* "GET /health": Performs a health check and returns a "200 OK" status with the JSON response "{"status": "healthy"}"
* "GET /hello?VALUE=<name>": Greets the user.
    * If the "VALUE" query parameter is provided (e.g., "/hello?VALUE=World"), it returns a "200 OK" status with a JSON response like "{"message": "Hello World"}".
    * If the "VALUE" query parameter is missing, it returns a "400 Bad Request" error.
* "GET /docs": Serves the interactive Swagger UI API documentation.
* "GET /redoc": Serves the ReDoc API documentation.
* "GET /openapi.json": Provides the raw OpenAPI 3.x schema for the API.

**Install dependencies using Poetry:**
    This will create a virtual environment and install the dependencies specified in `pyproject.toml`.
    poetry install

## How to Build the Application (Docker)

The application is designed to be built and run as a Docker container.

1.  Navigate to the project directory:
    Ensure your terminal is in the `lab1/` directory where the `Dockerfile` is located.

2.  Build the Docker image:
    Execute the following command to build the image. 
    docker build -t fastapi-lab-app .
    

## How to Run the Application (Docker)

Once the Docker image is built, you can run it as a container.

1.  Run the Docker container:
    docker run -d -p 8080:8000 --name fastapi-lab-container fastapi-lab-app

    * `-d`: Runs the container in detached mode.
    * `-p 8080:8000`: Maps port `8080` on your host machine to port `8000` inside the container (where Uvicorn is listening). You can change `8080` to another available port on your host if needed.
    * `--name fastapi-lab-container`: Assigns a friendly name to your running container for easier management.
    * `fastapi-lab-app`: The name of the Docker image you built in the previous step.

2.  Accessing the API:
    Once the container is running, the API will be accessible on your local machine:
    * Health Check: `http://localhost:8080/health`
    * Hello Endpoint: `http://localhost:8080/hello?VALUE=YourName`
    * Swagger Docs: `http://localhost:8080/docs`
    * ReDoc Docs: `http://localhost:8080/redoc`

3.  Stopping the container:
    docker stop fastapi-lab-container

4.  Removing the container (after stopping):
    docker rm fastapi-lab-container

## How to Test the Application

The application includes a suite of tests written using `pytest`. These tests ensure that the API endpoints behave as expected under various conditions, including correct and incorrect inputs.

1.  Ensure local development setup (if not testing against a running Docker instance):
    If you haven't already, set up the local development environment as described in the "Setup and Local Development" section (this primarily involves running `poetry install` to get `pytest` and other dev dependencies).

2.  Run tests using Poetry:
    Navigate to the `lab1/` directory in your terminal and execute:
    
    poetry run pytest -v
    
    * `poetry run`: Executes the command within the Poetry-managed virtual environment.
    * `pytest`: The test runner.
    * `-v`: Enables verbose output, showing details for each test case.