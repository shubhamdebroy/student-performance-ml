import joblib
import pandas as pd

#load the model
model = joblib.load("models/student_performance_model.pkl")

#columns used during training
columns = ['test_preparation_done', 'lunch_quality', 'gender_female', 'gender_male', 'race/ethnicity_group A', 'race/ethnicity_group B', 'race/ethnicity_group C', 'race/ethnicity_group D', 'race/ethnicity_group E', "parental_level_of_education_associate's degree", "parental_level_of_education_bachelor's degree", 'parental_level_of_education_high school', "parental_level_of_education_master's degree", 'parental_level_of_education_some college', 'parental_level_of_education_some high school', 'lunch_free/reduced', 'lunch_standard', 'test_preparation_course_completed', 'test_preparation_course_none']


def predict(student_data):
    student_df = pd.DataFrame([student_data])
    student_encoded_df = pd.get_dummies(student_df)
    student_encoded_df = student_encoded_df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(student_encoded_df)[0]
    
    return prediction

def recommend(student):
    recs = []

    if student["test_preparation_course"] == "none":
        recs.append("Complete a test preparation course")

    if student["lunch"] == "free/reduced":
        recs.append("Ensure proper nutrition")

    if student["parental_level_of_education"] in ["high school", "some high school"]:
        recs.append("Seek academic guidance")

    if len(recs) == 0:
        recs.append("Keep up the good work")

    return recs

def get_probabilities(student_data):
    student_df = pd.DataFrame([student_data])
    student_encoded_df = pd.get_dummies(student_df)
    student_encoded_df = student_encoded_df.reindex(columns=columns, fill_value=0)

    probs = model.predict_proba(student_encoded_df)[0]
    classes = model.classes_
    
    print("Probabilities:", probs)
    print("Classes:", classes)
    
    prob_dict = dict(zip(classes, probs))
    return prob_dict
