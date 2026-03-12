from fastapi import FastAPI
from app.api.routers import student
from app.api.routers import employee
from app import models
from app.db.session import engine

app = FastAPI(title="FastAPI + Neon PostgreSQL + JWT")

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(student.router)

# include router of employee
app.include_router(employee.router)
