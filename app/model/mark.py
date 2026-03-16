from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base

class Marks(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)
    subject = Column(String)
    score = Column(Integer)

    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="marks")