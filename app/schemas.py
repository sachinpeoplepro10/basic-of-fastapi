from pydantic import BaseModel

class StudentBase(BaseModel):
    firstname: str
    lastname: str
    age: int
    grade: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    class Config:
      from_attributes = True

from pydantic import BaseModel

class EmployeeBase(BaseModel):
    name: str
    department: str
    job_title: str
    email: str

class EmployeeCreate(EmployeeBase):
    pass   # used for POST requests (no id required)

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True   # allows ORM -> Pydantic conversion


