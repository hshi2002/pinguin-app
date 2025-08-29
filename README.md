# 🐧 Pinguin Application

A simple Flask + MongoDB web application that lets you manage and
monitor "ping objects".\
The app provides a REST API and a basic frontend, all containerized with
Docker.

------------------------------------------------------------------------

## 📦 Features

-   REST API for managing objects:
    -   `GET /api/objects` → list all objects
    -   `POST /api/objects` → add a new object
    -   `DELETE /api/objects/<host>` → remove an object by host
-   Health check endpoint: `GET /api/health`
-   Basic web UI (`/`)
-   Containerized with **Docker** and served via **Gunicorn**

------------------------------------------------------------------------

## 🚀 Getting Started

### Prerequisites

-   [Docker](https://docs.docker.com/get-docker/)
-   [Docker Compose](https://docs.docker.com/compose/)

### Run locally

Clone the repo and start the stack:

``` bash
git clone https://github.com/<your-username>/pinguin-application.git
cd pinguin-application
docker compose up --build
```

The app will be available at: - Frontend → <http://localhost:8080>\
- API → <http://localhost:8080/api>

------------------------------------------------------------------------

## 🔗 Example API Usage

### Health check

``` bash
curl http://localhost:8080/api/health
```

### Add an object

``` bash
curl -X POST http://localhost:8080/api/objects   -H "Content-Type: application/json"   -d '{"name":"MyHost","host":"8.8.8.8","interval":30}'
```

### List objects

``` bash
curl http://localhost:8080/api/objects
```

### Delete an object

``` bash
curl -X DELETE http://localhost:8080/api/objects/8.8.8.8
```

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Flask** (Python)
-   **MongoDB**
-   **Gunicorn**
-   **Docker & Docker Compose**
-   **Nginx** (reverse proxy)

------------------------------------------------------------------------

## 📌 Future Improvements

-   Add authentication
-   Better frontend with drag & drop for objects
-   CI/CD pipeline with GitHub Actions
-   E2E tests using Postman or Pytest

------------------------------------------------------------------------

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
