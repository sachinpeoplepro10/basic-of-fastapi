from pydantic import BaseModel, Field
from typing import List

class MarksUpdateItem(BaseModel):
    subject: SubjectEnum
    score: int = Field(..., ge=0, le=100)

class MarksBulkUpdate(BaseModel):
    student_id: int
    marks: List[MarksUpdateItem]

    class Config:
        schema_extra = {
            "example": {
                "student_id": 1,
                "marks": [
                    {"subject": "Math", "score": 100},
                    {"subject": "English", "score": 90},
                    {"subject": "Science", "score": 85}
                ]
            }
        }