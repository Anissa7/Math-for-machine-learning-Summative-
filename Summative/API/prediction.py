from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, conint, confloat
import joblib
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionInput(BaseModel):
    YEAR_DISPLAY: confloat(gt=1900, lt=2100)
    Numeric: conint(ge=0, le=10000)

# Load model from same directory
model_path = os.path.join(os.path.dirname(__file__), "best_model.pkl")
model = joblib.load(model_path)

@app.post("/predict")
async def get_prediction(data: PredictionInput):
    input_data = [[data.YEAR_DISPLAY, data.Numeric]]
    prediction = model.predict(input_data)
    return {"prediction": round(prediction[0], 2)}
