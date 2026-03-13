from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
# from app.db.session import get_db
from app.schema.mark import MarksCreate, MarksResponse
from app.crud import mark as crud_mark

router = APIRouter(prefix="/mark",tags=["mark"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MarksResponse)
def create_marks(marks: MarksCreate, student_id: int, db: Session = Depends(get_db)):
    return crud_mark.create_marks(db, marks, student_id)

@router.get("/marks/", response_model=list[MarksResponse])
def read_marks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_mark.get_marks(db, skip=skip, limit=limit)

@router.get("/students/{student_id}/marks/", response_model=list[MarksResponse])
def read_marks_by_student(student_id: int, db: Session = Depends(get_db)):
    return crud_mark.get_marks_by_student(db, student_id)

@router.delete("/marks/{marks_id}")
def delete_marks(marks_id: int, db: Session = Depends(get_db)):
    marks = crud_mark.delete_marks(db, marks_id)
    if not marks:
        raise HTTPException(status_code=404, detail="Marks not found")
    return {"detail": "Marks deleted successfully"}
