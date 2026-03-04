## Description

This project demonstrates a FastAPI application that performs seeding and authentication using a MariaDB database.

## Technology Stack

- **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server:** [Uvicorn](https://uvicorn.dev/)
- **Database:** [MariaDB](https://hub.docker.com/_/mariadb)
- **Deployment:** [Docker](https://www.docker.com/)

## Installation and Setup

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Steps

1.  **Clone the repository**
    ```bash
    git clone https://github.com/kayljiyan/fastapi-mariadb
    cd fastapi-mariadb
    ```
2.  **Edit the compose.yaml and Dockerfile to your preference**
3.  **Build the project using Docker Compose**
    ```bash
    docker compose up --build -d
    ```

Navigate to the [Docs](http://127.0.0.1:8000/docs) to access the interactive documentation
