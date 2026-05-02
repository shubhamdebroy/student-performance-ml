# Smart Student Performance Predictor & Recommender System

## Project Overview

This project is an end-to-end Machine Learning system designed to:

- Predict student academic performance (score / grade)
- Handle real-world challenges like imbalanced data
- Provide insights into factors affecting performance

The goal was not just to build a model, but to understand **how real ML systems behave with imperfect data**.

---

## Objectives

- Build a complete ML pipeline from scratch
- Work with real-world dataset (Kaggle)
- Understand model limitations
- Handle class imbalance
- Compare multiple ML models
- Learn deployment-ready practices

---

## Dataset

- Source: Kaggle – _Students Performance in Exams_
- Size: ~1000 samples
- Features:
  - Gender
  - Race/Ethnicity
  - Parental education
  - Lunch type
  - Test preparation course
  - Scores (Math, Reading, Writing)

### Key Challenge

The dataset lacked strong predictive features like:

- Study hours
- Learning habits
- Consistency

This became a **major limitation affecting model performance**

---

## Workflow

### 1. Data Understanding

- Explored dataset using Pandas
- Visualized relationships
- Identified categorical vs numerical features

---

### 2. Feature Engineering

- Created `average_score`
- Converted scores → grades (A, B, C, D, F)
- Applied encoding techniques:
  - One-hot encoding
  - Ordinal encoding (for education)

---

### 3. Model Building

#### Regression Models

- Linear Regression
- Ridge Regression
- Random Forest Regressor

Observation:

- Linear Regression performed best
- Complex models did not improve results

---

#### Classification Models

- Logistic Regression
- Random Forest Classifier

---

### 4. Handling Class Imbalance

The dataset was imbalanced:

- Few A grades
- Many C, D, F grades

Techniques used:

- Class Weighting (`class_weight='balanced'`)
- SMOTE (Synthetic Minority Oversampling)

---

### 5. Model Evaluation

Metrics used:

- Accuracy
- Precision
- Recall
- F1-score

### Key Insight :

> Accuracy alone is misleading in imbalanced datasets

---

### 6. Pipeline Implementation

Used `sklearn.pipeline` to:

- Automate preprocessing
- Avoid data leakage
- Ensure consistency

---

## Results & Observations

- Best Accuracy: ~42% (baseline)
- Balanced Model Accuracy: ~39%
- Logistic Regression outperformed Random Forest

---

## Prediction & Rule-Based Recommendation System

The final system takes student input and provides:

- Predicted grade (A, B, C, D, F)
- Personalized recommendations based on input features

### Example :

Input:

- Test Preparation: None
- Lunch: Free/Reduced
- Parental Education: High School

Output:

- Predicted Grade: C
- Recommendations:
  - Complete a test preparation course
  - Ensure proper nutrition
  - Seek academic guidance

---

## API Usage

### Endpoint:

POST /predict

### Example Input:

{
"gender": "male",
"race_ethnicity": "group C",
"parental_level_of_education": "bachelor's degree",
"lunch": "standard",
"test_preparation_course": "none"
}

### Example Output:

{
"predicted_grade": "A",
"probabilities": {
"A": 0.52,
"B": 0.21,
"C": 0.09,
"D": 0.12,
"F": 0.02
},
"recommendations": ["Complete a test preparation course"]
}

---

### Important Finding

> More complex models do not guarantee better performance

---

## Limitations

- Dataset lacks strong predictive features
- Weak correlation between inputs and target
- High class overlap (B vs C vs D)

---

## What I Learned

- Difference between Regression vs Classification
- Importance of Feature Engineering
- Handling Imbalanced Data (SMOTE, class_weight)
- Why simple models sometimes outperform complex ones
- Importance of proper ML pipeline
- Debugging real-world ML errors
- Model evaluation beyond accuracy

---

## Tech Stack

- Python
- NumPy, Pandas
- Matplotlib, Seaborn
- Scikit-learn
- Imbalanced-learn
- Jupyter Notebook

---

## Future Improvements

- Add real behavioral features (study hours, habits)
- Try advanced models (XGBoost)

---

## Conclusion

This project demonstrates that:

> Machine Learning is not just about models, but about understanding data, limitations, and making informed decisions.

---

Dataset sourced from Kaggle – Students Performance (for educational purposes).

---

## Author

Shubham Debroy
