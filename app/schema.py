from pydantic import BaseModel

class StudentInput(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str