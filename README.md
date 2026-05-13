# Incident Intelligence Platform

Enterprise-oriented AI-powered incident intelligence platform designed to assist operational teams with incident analysis, prioritization, and intelligent resolution workflows.

---

## Current Capabilities

- Structured enterprise incident dataset
- FastAPI backend initialization
- Incident retrieval API
- Swagger API documentation
- Modular project structure
- Structured Swagger API documentation
- Categorized REST endpoints
- Operational incident intelligence analysis
- Severity-based operational risk evaluation
- Incident summary generation service

---

## Tech Stack

- Python
- FastAPI
- Pandas
- OpenAI (planned integration)
- Conda Environment

---

## API Endpoints

### Incident Intelligence Summary

```http
GET /incidents/summary
```

Returns:
- total incidents
- active operational incidents
- severity distribution
- calculated operational risk level

### Health Check

```http
GET /
```

### Fetch Incidents

```http
GET /incidents
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Application runs at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Project Structure

```text
incident-intelligence-platform/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── models/
│   ├── datasets/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Status

Initial backend foundation completed.
AI intelligence workflows are currently under development.


---

## Architecture Notes

The platform follows a modular backend architecture:

- `datasets/` → operational incident datasets
- `services/` → business and intelligence logic
- `main.py` → API routing layer

This separation improves maintainability and scalability for future AI workflow integration.