import os
import time
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict, Optional

app = FastAPI(title="Baggage Sorting MLOps API", version="0.1.0")

MODEL_VERSION = os.getenv("MODEL_VERSION", "stub")


class PredictRequest(BaseModel):
    features: Dict[str, float] = Field(..., description="Precomputed PLC-like features for one time window")


class PredictResponse(BaseModel):
    anomaly_score: float
    is_anomaly: bool
    model_version: str
    latency_ms: float


@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    t0 = time.time()

    # TODO: replace with real model inference
    score = 0.25
    is_anomaly = score >= 0.5

    latency_ms = (time.time() - t0) * 1000
    return PredictResponse(
        anomaly_score=score,
        is_anomaly=is_anomaly,
        model_version=MODEL_VERSION,
        latency_ms=round(latency_ms, 3),
    )
