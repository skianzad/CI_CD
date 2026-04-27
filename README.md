# CI/CD Example for app.py

This repository includes a minimal Python app, Docker support, and GitHub Actions CI.

## Files created

- `app.py` - sample Python entrypoint
- `requirements.txt` - dependency list used by CI and Docker
- `tests/test_app.py` - simple pytest coverage
- `Dockerfile` - builds the app in a Python container
- `.dockerignore` - excludes unnecessary files from Docker context
- `.github/workflows/ci.yml` - GitHub Actions workflow that tests and builds the Docker image

## How to use

- Run tests locally: `python -m pytest`
- Build Docker image: `docker build -t myapp:latest .`
