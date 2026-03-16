from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud import mark as marks_crud
from app.schema.mark import MarksCreate
from app.schema.marks_update import MarksUpdate

router = APIRouter(prefix="/marks", tags=["Marks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create(marks: MarksCreate, db: Session = Depends(get_db)):
    return marks_crud.create_marks(db, marks)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return marks_crud.get_marks(db)

@router.put("/marks/{student_id}")
def update_marks(
    student_id: int,
    data: MarksUpdate,
    db: Session = Depends(get_db)
):
    return marks_crud.update_marks(
        db,
        student_id,
        data.dict(exclude_unset=True)
    )