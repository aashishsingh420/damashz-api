Damashz API Service

Backend service for Media Usage Tracker.

Responsibilities:
- JWT validation
- OAuth token storage
- Usage calculation
- Background worker



Damashz API – Technical Documentation
1. Technology Stack

Python 3.12

FastAPI

SQLAlchemy 2.0

PostgreSQL

Pydantic v2

Uvicorn

Docker

GHCR

2. Application Architecture
3. Project Structure
app/
├── api/
│   ├── deps.py
│   └── routes_users.py
├── core/
│   └── config.py
├── db/
│   ├── base.py
│   └── session.py
├── models/
├── schemas/
└── main.py
4. Database Layer

Engine:

create_engine(settings.database_url)

Session:

SessionLocal = sessionmaker(...)

Dependency injection:

get_db()
5. Startup Behavior

On application startup:

Base.metadata.create_all(bind=engine)

Creates tables if missing.

6. Available Endpoints
Health Check
GET /health

Response:

{
  "status": "ok",
  "app": "Damashz API",
  "version": "0.1.0"
}
Database Check
GET /db-check

Performs:

SELECT 1

Verifies database connectivity.

Create User
POST /users/

Body:

{
  "keycloak_id": "kc001",
  "email": "test@example.com"
}
List Users
GET /users/

Returns all users.

7. Containerization

Dockerfile:

Based on python:3.12

Installs requirements.txt

Copies app

Runs uvicorn

Image:

ghcr.io/aashishsingh420/damashz-api
8. Environment Variables

Configured via:

ConfigMap

Secret

Includes:

DATABASE_URL

APP_NAME

APP_VERSION

9. Future Enhancements

Keycloak JWT validation

OAuth token storage

Background worker (CronJob)

Migrations via Alembic

Structured logging

Health probes

Resource limits

Ingress exposure

Horizontal Pod Autoscaling

10. Operational Validation

To verify inside cluster:

kubectl exec -it <api-pod> -n damashz -- curl localhost:8000/health
System Summary

You now have:

CI/CD automation

Container registry integration

GitOps reconciliation

Stateful database

Declarative infrastructure

Version-controlled deployment

This is production-grade architecture running locally.
