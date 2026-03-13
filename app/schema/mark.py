from pydantic import BaseModel

class MarksBase(BaseModel):
    subject: str
    score: int

class MarksCreate(MarksBase):
    pass

class MarksResponse(MarksBase):
    id: int
    student_id: int

    class Config:
        from_attributes = True
