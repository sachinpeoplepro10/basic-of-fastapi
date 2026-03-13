from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schema.student import StudentCreate, StudentResponse
from app.crud import student as crud_student

router = APIRouter(prefix="/students", tags=["students"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create student
@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud_student.create_student(db, student)

# Read all students
@router.get("/", response_model=list[StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return crud_student.get_students(db)

# Read one student
@router.get("/{id}", response_model=StudentResponse)
def read_student(id: int, db: Session = Depends(get_db)):
    student = crud_student.get_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Update student
@router.put("/{id}", response_model=StudentResponse)
def update_student(id: int, student_update: StudentCreate, db: Session = Depends(get_db)):
    student = crud_student.update_student(db, id, student_update)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Delete student
@router.delete("/{id}")
def delete_student(id: int, db: Session = Depends(get_db)):
    student = crud_student.delete_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"status": "deleted successfully"}
