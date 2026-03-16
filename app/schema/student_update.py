from pydantic import BaseModel
from typing import Optional

class StudentUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None
    grade: Optional[str] = None
    email: Optional[str] = None