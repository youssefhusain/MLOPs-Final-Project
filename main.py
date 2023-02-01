from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
import numpy as np
import joblib
import time

model = None
scaler = None

class LandmarkRequest(BaseModel):
    landmarks: list[list[float]] 

app = FastAPI(title="Hand API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

GESTURE_TO_ACTION_MAPPING = {
    7: "up",     
    0: "down",    
    12: "left",    
    16: "right"   
}

@app.on_event("startup")
def load_artifacts():
    global model, scaler
    try:
        model = joblib.load("model/gesture_model.pkl")
        #scaler = joblib.load("model/scale.pkl")
    except Exception as e:
        raise RuntimeError(f"Error loading model artifacts: {e}")

@app.post("/predict")
def predict_action(data: LandmarkRequest):
    start_time = time.time()
    if not data.landmarks or not all(len(pt) == 2 for pt in data.landmarks):
        raise HTTPException(status_code=400, detail="Each landmark must contain exactly two values (x, y).")
    try:
        flat_input = np.array(data.landmarks).flatten().reshape(1, -1)
        scaled_input = flat_input
        #scaler.transform(flat_input)

        pred_class_index = model.predict(scaled_input)[0]

        action = GESTURE_TO_ACTION_MAPPING.get(pred_class_index, "unknown_action")

        return {"predicted_class_index": int(pred_class_index), "action": action}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
