from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(...)
    gpa: float = Field(...)

    class Config:
        json_schema_extra = {
            'example': {
                'full_name': 'Dilshod Bakhtiyorov',
                'email': 'abc@mail.ru',
                'course_of_study': 'computer science',
                'year': 2,
                'gpa': '3.0'
            }
        }


class UpdateStudentModel(BaseModel):
    full_name: Optional[str]
    email: Optional[str]
    course_of_study: Optional[str]
    year: Optional[str]
    gpa: Optional[str]

    class Config:
        json_schema_extra = {
            'example': {
                'full_name': 'Dilshod Bakhtiyorov',
                'email': 'abc@mail.ru',
                'course_of_study': 'computer science',
                'year': 2,
                'gpa': '3.0'
            }
        }


def response_model(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message
    }


def error_response_model(error, code, message):
    return {
        'error': error,
        'code': code,
        'message': message
    }
