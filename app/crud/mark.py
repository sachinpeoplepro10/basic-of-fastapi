from sqlalchemy.orm import Session
from app.model.mark import Marks
from app.schema.mark import MarksCreate


def create_marks(db: Session, marks: MarksCreate):
    new_marks = Marks(**marks.dict())
    db.add(new_marks)
    db.commit()
    db.refresh(new_marks)
    return new_marks


def get_marks(db: Session):
    return db.query(Marks).all()

def update_marks(db: Session, mark_id: int, data: dict):

    marks = db.query(Marks).filter(Marks.id == mark_id).first()

    if not marks:
        return {"message": "Marks record not found"}

    for key, value in data.items():
        setattr(marks, key, value)

    db.commit()
    db.refresh(marks)

    return marks