from sqlalchemy.orm import Session
from app.model.student import Student
from app.schema.student import StudentCreate

# CREATE
def create_student(db: Session, student: StudentCreate):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# READ ALL
def get_students(db: Session):
    return db.query(Student).all()

# READ ONE
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# UPDATE
def update_student(db: Session, student_id: int, student_update: StudentCreate):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        for key, value in student_update.dict().items():
            setattr(student, key, value)
        db.commit()
        db.refresh(student)
    return student

# DELETE
def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student




