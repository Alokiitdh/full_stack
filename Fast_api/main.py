
from fastapi import FastAPI
from models import Students

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome Alok's Students Database"


student = [
    Students(rollno=1, name="Alok", grade=6, college_name="ABC"),
    Students(rollno=2, name="Abhishek", grade=9, college_name="DEF"),
    Students(rollno=3, name="Sumit", grade=3, college_name="DFD"),
    Students(rollno=4, name="Jangu", grade=7, college_name="DFC"),
    Students(rollno=5, name="Priya", grade=8, college_name="LMN"),
    Students(rollno=6, name="Ravi", grade=5, college_name="OPQ"),
    Students(rollno=7, name="Sneha", grade=10, college_name="XYZ"),
    Students(rollno=8, name="Karan", grade=4, college_name="PQR"),
    Students(rollno=9, name="Meena", grade=2, college_name="JKL"),
    Students(rollno=10, name="Rahul", grade=1, college_name="TUV")
]

@app.get("/students")
def all_students():
    return student

@app.get("/students/{rollno}")
def student_by_rollno(rollno :int):
    for stud in student:
        if stud.rollno == rollno:
            return stud
    return "Data not available"

@app.post("/students")
def add_student(stud:Students):
    student.append(stud)
    return f"Data successfully added : {stud}"

@app.put("/students")
def update_student(roll_num:int, stud: Students):# we are searching the data based on roll number and then updating it , the schema should be prvided as Student
    for i in range(len(student)):
        if student[i].rollno == roll_num:
            student[i] = stud
            return "Data Modified succesfullly"
    return "Error-Check roll number care fully"

@app.delete("/students")
def delete_data(roll_no: int):
    for i in range(len(student)):
        if student[i].rollno == roll_no:
            del student[i]
            return "Data deletion is succesful"
    return "Error - Please enter correct rollno"








