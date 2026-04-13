from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.model.mark import Marks
from app.model.student import Student
from app.schema.mark import MarksCreate
from app.schema.marks_update import MarksUpdate
from app.schema.marksbulkupdate import MarksBulkUpdate
from sqlalchemy import func

def create_marks(db: Session, marks: MarksCreate):
    new_marks = Marks(**marks.dict())
    db.add(new_marks)
    db.commit()
    db.refresh(new_marks)
    return new_marks


def get_marks(db: Session):
    return db.query(Marks).all()

def update_marks(db: Session, student_id: int, data: dict):

    marks = db.query(Marks).filter(Marks.student_id == student_id).first()

    if not marks:
        return {"message": "Marks record not found"}

    for key, value in data.items():
        setattr(marks, key, value)

    db.commit()
    db.refresh(marks)

    return marks


def update_student_and_marks(db: Session, data: MarksBulkUpdate):

    # 🔍 1. Validate student
    student = db.query(Student).filter(Student.id == data.student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # ✏️ 2. Update name
    student.name = data.name

    # 🔁 3. Update / Insert marks (your logic kept same)
    for item in data.marks:

        mark = db.query(Marks).filter(
            Marks.student_id == data.student_id,
            func.lower(Marks.subject) == item.subject.value.lower()
        ).first()

        if mark:
            # UPDATE
            mark.score = item.score
        else:
            # INSERT
            db.add(Marks(
                student_id=data.student_id,
                subject=item.subject.value,
                score=item.score
            ))

    db.commit()

    return {
        "student_id": data.student_id,
        "name": student.name,
        "message": "Student and marks updated successfully"
    }