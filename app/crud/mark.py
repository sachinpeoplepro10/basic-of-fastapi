from sqlalchemy.orm import Session
from app.model.mark import Marks
from app.schema.mark import MarksCreate



def create_marks(db: Session, marks: MarksCreate, student_id: int):
    db_marks = Marks(**marks.dict(), student_id=student_id)
    db.add(db_marks)
    db.commit()
    db.refresh(db_marks)
    return db_marks

def get_marks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Marks).offset(skip).limit(limit).all()

def get_marks_by_student(db: Session, student_id: int):
    return db.query(Marks).filter(Marks.student_id == student_id).all()

def delete_marks(db: Session, marks_id: int):
    marks = db.query(Marks).filter(Marks.id == marks_id).first()
    if marks:
        db.delete(marks)
        db.commit()
    return marks
