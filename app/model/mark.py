from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base 


class Marks(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(50), nullable=False)
    score = Column(Integer, nullable=False)

    # Foreign key to Student
    student_id = Column(Integer, ForeignKey("students.id"))

    # Relationship back to Student
    student = relationship("Student", back_populates="mark")

