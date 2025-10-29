from pydantic import BaseModel

class Students(BaseModel):
    rollno: int
    name: str
    grade: int
    college_name: str

