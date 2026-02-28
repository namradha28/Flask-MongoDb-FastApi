from fastapi import FastAPI
from database import collection
from models import Student
from bson import ObjectId

app = FastAPI()

# Helper function
def student_serializer(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "email": student["email"],
        "course": student["course"]
    }

@app.post("/students/")
def create_student(student: Student):
    result = collection.insert_one(student.dict())
    new_student = collection.find_one({"_id": result.inserted_id})
    return student_serializer(new_student)

@app.get("/students/")
def get_students():
    students = []
    for student in collection.find():
        students.append(student_serializer(student))
    return students

@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    collection.delete_one({"_id": ObjectId(student_id)})
    return {"message": "Deleted successfully"}