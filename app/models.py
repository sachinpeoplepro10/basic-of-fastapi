from sqlalchemy import Column, Integer, String
from app.db.session import Base 

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(Integer)
    grade = Column(String(10))
    email = Column(String(100))

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    job_title = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

