from sqlalchemy.orm import Session
from app.model.student import Student
from app.schema.student import StudentCreate


def create_student(db: Session, student: StudentCreate):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if student:
        db.delete(student)
        db.commit()

    return student

def update_student(db: Session, student_id: int, data: dict):

    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        return {"message": "Student not found"}

    for key, value in data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student