from fastapi import FastAPI
from app import model
from app.schema import StudentInput
from app.model import predict, recommend, get_probabilities

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Student Performance Prediction API!"}

@app.post("/predict")
def predict_student(data: StudentInput):
    student_dict = data.dict()
    grade = predict(student_dict)
    probs_dict = get_probabilities(student_dict)
    recs = recommend(student_dict)

    return {
        "predicted_grade": grade,
        "probabilities": probs_dict,
        "recommendations": recs
    }

# The model outputs class probabilities, and the final prediction is the class with the highest probability. This helps in understanding prediction confidence.