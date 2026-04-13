from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.crud import mark as marks_crud
from app.schema.mark import MarksCreate
from app.schema.marks_update import MarksUpdate
from app.schema.marksbulkupdate import MarksBulkUpdate

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


@router.put("/bulk-update")
def bulk_update_marks(
    data: MarksBulkUpdate,
    db: Session = Depends(get_db)
):
    return marks_crud.update_student_and_marks(db, data)

@router.put("/students/{student_id}")
def update_mark(
    student_id: int,
    data: MarksUpdate,   # ya dict bhi le sakte ho
    db: Session = Depends(get_db)
    ):
    return marks_crud.update_marks(
        db,
        student_id,
        data.dict(exclude_unset=True)
    )
