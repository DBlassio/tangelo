from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the trained model
with open('./data/rf_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

#Input
class Data(BaseModel):
    Gender: object
    Car: object
    Realty: object
    Mobile: int
    Work_phone: int
    Phone: int
    Email: int
    education_type: object
    income_type: object
    Family_status: object
    Housing_type: object
    Occupation_type: object
    Count_family_members: float
    Years_Employed: float
    Age: float
    children_count: float
    income_amount: float

#Output
@app.post("/predict/")
async def data_endpoint(items: list[Data]):
    predictions = []
    for item in items:
        df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
        y_hat = model.predict(df)  
        prediction = int(y_hat[0])
        predictions.append(prediction)

    return {"predictions": predictions}