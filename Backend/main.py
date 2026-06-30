from fastapi import FastAPI
from pydantic import BaseModel
from  predictor import predict_diseases

app=FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0"
)

#input schema matching training features
 
class HeartDiseaseInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalach: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
    
    
@app.get("/health")
def health_check():
    return {
        "status":"ok"
    }
  
     
#heart disease prediction

@app.post("/predict_heart_diseases")
def predict_disease(input_data:HeartDiseaseInput):
    result = predict_diseases(input_data.model_dump())
    return {
        "prediction":result["prediction"],
        "probability":round(result["probability"],4),
        'diagnosis':(
            "Heart Disease Detected"
            if result['prediction']==1
            else "No Heart Disease Detected"
        )
        
    }
    
     


