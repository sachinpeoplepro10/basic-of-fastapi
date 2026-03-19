from sqlalchemy.orm import Session
from sqlalchemy import func
from app.model.student import Student
from app.model.mark import Marks


# Average score of each student
def student_average_score(db: Session):
    return (
        db.query(
            Student.name,
            func.avg(Marks.score).label("average_score")
        )
        .join(Marks)
        .group_by(Student.id)
        .all()
    )


# Total score of each student
def student_total_score(db: Session):
    return (
        db.query(
            Student.name,
            func.sum(Marks.score).label("total_score")
        )
        .join(Marks)
        .group_by(Student.id)
        .all()
    )


# Top scoring student
def top_student(db: Session):
    return (
        db.query(
            Student.name,
            func.sum(Marks.score).label("total_score")
        )
        .join(Marks)
        .group_by(Student.id)
        .order_by(func.sum(Marks.score).desc())
        .first()
    )


# Subject-wise average
def subject_average(db: Session):
    return (
        db.query(
            Marks.subject,
            func.avg(Marks.score).label("avg_score")
        )
        .group_by(Marks.subject)
        .all()
    )

