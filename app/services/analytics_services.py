from sqlalchemy.orm import Session
from sqlalchemy import func
from app.model.student import Student
from app.model.mark import Marks


def student_average(db: Session):
    results = (
        db.query(
            Student.firstname,
            func.avg(Marks.score).label("average_score")
        )
        .join(Marks, Marks.student_id == Student.id)
        .group_by(Student.id, Student.firstname)
        .all()
    )

    return [
        {"firstname": r.firstname, "average_score": float(r.average_score)}
        for r in results
    ]


def top_student(db: Session):
    result = (
        db.query(
            Student.firstname,
            func.sum(Marks.score).label("total_score")
        )
        .join(Marks, Marks.student_id == Student.id)
        .group_by(Student.id, Student.firstname)
        .order_by(func.sum(Marks.score).desc())
        .first()
    )

    if not result:
        return None

    return {
        "firstname": result.firstname,
        "total_score": result.total_score
    }


def subject_average(db: Session):
    results = (
        db.query(
            Marks.subject,
            func.avg(Marks.score).label("avg_score")
        )
        .group_by(Marks.subject)
        .all()
    )

    return [
        {"subject": r.subject, "avg_score": float(r.avg_score)}
        for r in results
    ]


def highest_score_by_subject(db: Session):

    subquery = (
        db.query(
            Marks.subject,
            func.max(Marks.score).label("highest_score")
        )
        .group_by(Marks.subject)
        .subquery()
    )

    results = (
        db.query(
            Student.firstname,
            Marks.subject,
            Marks.score
        )
        .join(Student, Student.id == Marks.student_id)
        .join(
            subquery,
            (Marks.subject == subquery.c.subject) &
            (Marks.score == subquery.c.highest_score)
        )
        .all()
    )

    return [
        {
            "student_name": r.firstname,
            "subject": r.subject,
            "highest_score": r.score
        }
        for r in results
    ]

def lowest_score_by_subject(db: Session):

    subquery = (
        db.query(
            Marks.subject,
            func.min(Marks.score).label("lowest_score")
        )
        .group_by(Marks.subject)
        .subquery()
    )

    results = (
        db.query(
            Student.firstname,
            Marks.subject,
            Marks.score
        )
        .join(Student, Student.id == Marks.student_id)
        .join(
            subquery,
            (Marks.subject == subquery.c.subject) &
            (Marks.score == subquery.c.lowest_score)
        )
        .all()
    )

    return [
        {
            "student_name": r.firstname,
            "subject": r.subject,
            "lowest_score": r.score
        }
        for r in results
    ]