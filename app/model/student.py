from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base 

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(Integer)
    grade = Column(String(10))
    email = Column(String(100))
    mark = relationship("Marks", back_populates="student")
    
