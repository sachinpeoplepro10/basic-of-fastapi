from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.services import analytics_services
from app.model.student import Student

router = APIRouter(prefix="/analytics", tags=["Analytics"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/student-average")
def get_student_average(db: Session = Depends(get_db)):
    data = analytics_services.student_average(db)
    return data


@router.get("/top-student")
def get_top_student(db: Session = Depends(get_db)):
    data = analytics_services.top_student(db)
    return data


@router.get("/subject-average")
def get_subject_average(db: Session = Depends(get_db)):
    data = analytics_services.subject_average(db)
    return data

# Highest score in each subject
@router.get("/highest-score-by-subject")
def highest_score(db: Session = Depends(get_db)):
    return analytics_services.highest_score_by_subject(db)


# Lowest score in each subject
@router.get("/lowest-score-by-subject")
def lowest_score(db: Session = Depends(get_db)):
    return analytics_services.lowest_score_by_subject(db)

# GET - Single Student
@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        return {"message": "Student not found"}

    return student

