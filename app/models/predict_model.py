from pydantic import BaseModel

class PredictRequest(BaseModel):
    firstname: str
    lastname: str


class PredictResponse(BaseModel):
    input: PredictRequest
    output: str