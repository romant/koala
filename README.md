# Koala Time Service

This repository contains a minimal Python application that serves the current UTC time. The app uses Flask and can be deployed to Cloud Foundry.

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

The service will be available at `http://localhost:8080/` and returns a JSON payload with the current time.

## Deploying to Cloud Foundry

Ensure you are logged in to your Cloud Foundry instance and run:

```bash
cf push
```

Cloud Foundry reads `manifest.yml` and deploys the app using the Python buildpack.
