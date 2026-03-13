from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base 

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    department = Column(String(50), nullable=False)
    job_title = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

