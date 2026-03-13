from pydantic import BaseModel

class StudentBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    grade: str
    email: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True   # allows reading SQLAlchemy objects directly