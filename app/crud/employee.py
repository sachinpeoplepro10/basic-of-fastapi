from sqlalchemy.orm import Session
from app.model.employee import Employee as EmployeeModel
from app.schema.employee import EmployeeCreate,Employee

# CREATE
def create_employee(db:Session,Employee_detail: EmployeeCreate):
    new_employee = EmployeeModel(**Employee_detail.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

# GET
def get_employees(db: Session):
    return db.query(EmployeeModel).all()




