from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = 'product_review'

    class Config:
        schema_extra = {
            'example': {
                'name': 'test_name',
                'product': 'Abc course',
                'rating': 5.1,
                'review': 'Excellent course',
                'date': datetime.now()
            }
        }


class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[str]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        schema_extra = {
            'example': {
                'name': 'Dilshod Bakhtiyorov',
                'product': 'Abc course',
                'rating': 5.1,
                'review': 'Excellent course!',
                'date': datetime.now()

            }
        }

