from typing import List
from app.schema.student import StudentBasic
from app.schema.mark import MarksResponse

class StudentResponse(StudentBasic):
    marks: List[MarksResponse] = []