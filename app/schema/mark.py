from pydantic import BaseModel

class MarksCreate(BaseModel):
    subject: str
    score: int
    student_id: int         


class MarksResponse(MarksCreate):
    id: int

    class Config:
        from_attributes = True