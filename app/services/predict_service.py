from app.models.predict_model import PredictRequest, PredictResponse
from app.utils.logger import get_logger

logger = get_logger(__name__)

def make_prediction(data: PredictRequest) -> str:
    # Dummy prediction logic
    return f"Predicted result for '{data.firstname}'"

def make_nameprediction(data: PredictRequest) -> PredictResponse:
    """
    Processes predict data. In this example, it simply returns the input data and string output data.
    """
    logger.info(f"Predict Name called with data: {data}")

    return PredictResponse(
        input=data,
        output="You're a awesome guy!!"
    )
