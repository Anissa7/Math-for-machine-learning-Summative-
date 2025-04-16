from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PredictionInput(BaseModel):
    YEAR_DISPLAY: float
    Numeric: int

@app.post("/predict")
async def get_prediction(data: PredictionInput):
    # 🧪 Simple example prediction logic
    result = data.YEAR_DISPLAY + data.Numeric
    return {"prediction": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
