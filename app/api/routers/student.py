from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud import student as student_crud
from app.schema.student import StudentCreate
from app.schema.student_update import StudentUpdate

router = APIRouter(prefix="/students", tags=["Students"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create(student: StudentCreate, db: Session = Depends(get_db)):
    return student_crud.create_student(db, student)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return student_crud.get_students(db)

@router.put("/students/{student_id}")
def update_student(
    student_id: int,
    data: StudentUpdate,
    db: Session = Depends(get_db)
):
    return student_crud.update_student(
        db,
        student_id,
        data.dict(exclude_unset=True)
    )