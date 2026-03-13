from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schema.employee import Employee, EmployeeCreate
from app.crud import employee as crud_employee

router = APIRouter(prefix="/employees", tags=["employees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model= Employee)
def create_employee(emp_detail:EmployeeCreate, db:Session =Depends(get_db)):
    return crud_employee.create_employee(db, emp_detail)


@router.get("/", response_model=list[Employee])
def get_all_employees(db: Session = Depends(get_db)):
    return crud_employee.get_employees(db)
