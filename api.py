from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API No-Show XGBoost")

# Charger le modèle
model = joblib.load("best_model_xgboost_smote.pkl")

# Entrée structurée
class PatientFeatures(BaseModel):
    Age: float
    Scholarship: int
    Hipertension: int
    Diabetes: int
    Alcoholism: int
    Handcap: int
    SMS_received: int
    waiting_days: float
    Gender: str
    Neighbourhood: str
    scheduled_weekday: str
    appointment_weekday: str

# Sortie
class PredictionOutput(BaseModel):
    prediction: int
    probability: float

@app.get("/health")
def health():
    return {"status": "API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: PatientFeatures):

    # Convertir en DataFrame 
    df = pd.DataFrame([data.dict()])

    # Prédiction
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    return PredictionOutput(
        prediction=int(pred),
        probability=float(proba)
    )

