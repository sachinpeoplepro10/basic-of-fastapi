from pydantic import BaseModel
from typing import Optional

class MarksUpdate(BaseModel):
    subject: Optional[str] = None
    score: Optional[int] = None
    student_id: Optional[int] = None