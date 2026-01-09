# Text Processing API

A lightweight backend service built with FastAPI that provides deterministic text-processing utilities and exposes basic observability (metrics & logs).
The project is intentionally small and practical — designed to strengthen real Python backend fundamentals.

This is not a toy example and not an ML project.
It focuses on correctness, structure, and production-style tooling.

---

## Goals

- Build a clean, maintainable **Python backend** using FastAPI
- Practice **API design** (request/response schemas, error handling)
- Add **persistence** (store analysis results in a database)
- Write **automated tests** (pytest - unit + integration)
- Containerize the service with **Docker**
- Introduce basic **observability (Prometheus, Loki, Grafana)**

# How to Run the Application

The recommended way to run this project is using **Docker Compose**.  
This ensures the API, database, and observability stack run in a consistent environment.

```bash
docker compose up --build
```

## Available Services

Once running, the following services are available:

| Service          | URL                          |
| ---------------- | ---------------------------- |
| Swagger UI (API) | http://localhost:8000/docs   |
| Health Check     | http://localhost:8000/health |
| Prometheus       | http://localhost:9090        |
| Grafana          | http://localhost:3030        |

### Stopping the Application

```bash
docker compose down
```

or using `-v` to delate data in Docker volumes

```bash
docker compose up -v
```

## API Endpoints

### `GET /health`

- Simple endpoint to verify the service is running.

**Response**

```json
{ "status": "ok" }
```

### `POST /clean_text`

Cleans and normalizes the input text using deterministic rules:

- lowercasing
- removing configured special characters
- collapsing multiple whitespace characters
- trimming leading and trailing spaces

**Request**

```json
{
  "input_string": "Some TEXT!!!   "
}
```

**Response**

```json
{
  "clean_text": "some text"
}
```

Validation rules:

- `input_string` must be non-empty string
- maximum length: 1000 characters

### `POST /analyze`

Performs text analysis and persists the result in the database.

Processing steps:

1. Clean the input text
2. Count words
3. Count sentences (based on . occurrence)
4. Compute most frequent words
5. Compute most frequent characters
6. Save the analysis result to SQLite

**Request**

```json
{
  "input_string": "Hello world. Hello again!"
}
```

**Response**

```json
{
  "words_count": 4,
  "sentence_count": 1,
  "frequent_words": {
    "hello": 2,
    "world": 1,
    "again": 1
  },
  "frequent_chars": {
    "h": 2,
    "e": 2,
    "l": 5,
    "o": 3,
    " ": 3,
    "w": 1,
    "r": 1,
    "d": 1,
    ".": 1,
    "a": 2,
    "g": 1,
    "i": 1,
    "n": 1
  },
  "original_text": "Hello world. Hello again!",
  "clean_text": "hello world. hello again"
}
```

If a database error occurs, the endpoint returns:

```json
{
  "detail": "Database error"
}
```

With HTTP status 500

### `GET /metrics`

Prometheus-compatible metrics endpoint.

Used internally by Prometheus to scrape application metrics (request counts, latency, etc.).
Not intended for direct user interaction.

## Design Decisions & Limitations

- Sentence counting is based on a simple `.` heuristic
- SQLite is used for simplicity and local development
- The project is single-node and not designed for horizontal scaling
- Authentication and authorization are intentionally out of scope
