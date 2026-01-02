from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_stub():
    payload = {"features": {"speed_mean": 1.0, "current_std": 0.1}}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "anomaly_score" in body
    assert "latency_ms" in body
