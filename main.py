from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response
import time
from prometheus_client import make_asgi_app, Counter

model = None
scaler = None

class LandmarkRequest(BaseModel):
    landmarks: list[list[float]] 

app = FastAPI(title="Hand API")

# Prometheus metrics
REQUEST_COUNT = Counter(
    'request_count', 'App Request Count',
    ['method', 'endpoint', 'http_status']
)
REQUEST_LATENCY = Histogram(
    'request_latency_seconds', 'Request latency',
    ['method', 'endpoint']
)

GESTURE_TO_ACTION_MAPPING = {
    16: "up",     
    17: "down",    
    4: "left",    
    5: "right"   
}

@app.on_event("startup")
def load_artifacts():
    global model, scaler
    try:
        model = joblib.load("model/gesture_model.pkl")
        scaler = joblib.load("model/scale.pkl")
    except Exception as e:
        raise RuntimeError(f"Error loading model artifacts: {e}")

@app.post("/predict")
def predict_action(data: LandmarkRequest):
    start_time = time.time()
    if not data.landmarks or not all(len(pt) == 2 for pt in data.landmarks):
        REQUEST_COUNT.labels('POST', '/predict', 400).inc()
        raise HTTPException(status_code=400, detail="Each landmark must contain exactly two values (x, y).")
    try:
        flat_input = np.array(data.landmarks).flatten().reshape(1, -1)
        scaled_input = scaler.transform(flat_input)

        pred_class_index = model.predict(scaled_input)[0]

        action = GESTURE_TO_ACTION_MAPPING.get(pred_class_index, "unknown_action")

        REQUEST_COUNT.labels('POST', '/predict', 200).inc()
        REQUEST_LATENCY.labels('POST', '/predict').observe(time.time() - start_time)
        return {"predicted_class_index": int(pred_class_index), "action": action}
    except Exception as e:
        REQUEST_COUNT.labels('POST', '/predict', 500).inc()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")



metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)