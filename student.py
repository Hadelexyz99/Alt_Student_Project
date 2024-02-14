# Create a FastAPI project with the following specifications:
# A Student resource. Each student will have:
# Id (int)
# Name(str)
# Age (int)
# Sex (str)
# Height (float)
# For data storage, use an in-memory storage (Python dictionary)
# Create endpoints to do the following:
# Create a Student resource
# Retrieve a Student resource (one Student and many Students)
# Update a Student resource
# Delete a Student resource
# Push your project to a public git repository and post you submission here
# Goodluck!

# NOTE: You are not required to use Pydantic type enforcement. Just basic Python.

from fastapi import FastAPI

app = FastAPI()


students = {}

class Student:
    def __init__(self, name, age, sex, height):
        self.name  = name
        self.age = age
        self.sex = sex 
        self.height = height

@app.get("/")
def home():
    return {"welcome": "This is a student resource api"}

@app.post("/students")
def create_student(name: str, age: int, sex: str, height: float):
    student_id = len(students) + 1
    student = Student(name,age,sex,height)
    students[student_id] = student
    return {"Message": "Student created successfully", "data": student}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_students_by_id(student_id: int):
    if student_id in students:
        student = students[student_id]
        return {"Message": "Student found", "data": student}
    else:
        return {"Message": "student not found"}
    
@app.put("/students/{id}")
def update_student(student_id: int,name: str, age: int, sex: str, height: float):
    if student_id in students:
        student = students[student_id]
        student.name = name
        student.age = age
        student.sex = sex
        student.height = height
        return {"Message": "Student updated successfully", "data": student}
    else:
        return "Student not found"
    
@app.delete("/students/{id}")
def delete_student(student_id: int):
    # student = students.get(student_id)
    # del students[student_id]
    if student_id in students:
        del students[student_id]
        return {"Message": "Student deleted successfully"}
    else:
        return {"No student with this details exist"}
    
