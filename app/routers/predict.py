from fastapi import APIRouter
from app.models.predict_model import PredictRequest, PredictResponse
from app.services.predict_service import make_prediction, make_nameprediction

router = APIRouter()

@router.post("/predict")
def predict(request: PredictRequest):
    prediction = make_prediction(request)
    return {"input": request, "prediction": prediction}

@router.post("/predictname", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = make_nameprediction(request)
    return prediction
