from pydantic import BaseModel

class StudentCreate(BaseModel):
    firstname: str
    lastname: str
    age: int
    grade: str
    email: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True