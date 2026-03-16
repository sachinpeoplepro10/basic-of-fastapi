from fastapi import FastAPI
from app.db.session import engine, Base   # ✅ import Base from session
from app.model import student, employee, mark   # ✅ import your models so tables are registered


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
from app.api.routers import student as student_router
from app.api.routers import employee as employee_router
from app.api.routers import mark as mark_router
from app.api.routers import analytics_routers as service_router

app.include_router(student_router.router)
app.include_router(employee_router.router)
app.include_router(mark_router.router)
app.include_router(service_router.router)
