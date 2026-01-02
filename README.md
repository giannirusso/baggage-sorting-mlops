# baggage-sorting-mlops

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-success)
![API](https://img.shields.io/badge/API-FastAPI-green)
![MLOps](https://img.shields.io/badge/MLOps-MLflow%20%7C%20CI%2FCD-brightgreen)
![CI](https://github.com/<YOUR_GITHUB_USERNAME>/baggage-sorting-mlops/actions/workflows/ci.yml/badge.svg)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

Production-style MLOps project for **anomaly detection** and **throughput optimization** in an industrial baggage sorting context using **PLC-like sensor signals**.  
Includes an end-to-end pipeline approach: data generation, ETL, feature engineering, model training, MLflow tracking, CI-tested API inference, and Dockerized deployment.

## Overview
This repository is designed to replicate a real-world MLOps workflow (without using proprietary/production data):
- synthetic PLC-like time-series generation (missing samples, noise, drift, anomalies)
- ETL: raw → cleaned → feature-ready datasets
- feature engineering with rolling-window statistics
- baseline model training + evaluation (Precision, Recall, F1)
- experiment tracking & model versioning with MLflow
- FastAPI inference service (`/predict`) packaged with Docker
- CI workflow with automated tests

## Quickstart (Docker)
Start MLflow + API:

```bash
docker compose up --build
```


API docs: http://localhost:8000/docs
MLflow UI: http://localhost:5000

API
Endpoints:
```bash
GET /health
POST /predict
```
Example request:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"features": {"speed_mean": 1.0, "current_std": 0.1}}'
```

## Status

This project is actively being built. The current repository includes a production-style skeleton (API, Docker, MLflow, CI). Next steps add full data + training pipelines.
