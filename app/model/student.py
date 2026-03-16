from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    grade = Column(String)
    email = Column(String, unique=True, index=True)
    

    marks = relationship("Marks", back_populates="student")