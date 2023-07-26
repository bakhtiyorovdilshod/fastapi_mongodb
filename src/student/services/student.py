from bson import ObjectId

from src.database import student_collection
from src.helpers import student_helper


class StudentCrudService:
    async def retrieve_students(self):
        students = []
        async for student in student_collection.find():
            students.append(student_helper(student))
        return students

    async def add_student(self, student_data: dict) -> dict:
        student = await student_collection.insert_one(student_data)
        new_student = await student_collection.find_one({"_id": student.inserted_id})
        return student_helper(new_student)

    async def retrieve_student(self, id: str) -> dict:
        student = await student_collection.find_one({"_id": ObjectId(id)})
        if student:
            return student_helper(student)

    async def update_student(self, id:str, data: dict) -> bool:
        if len(data) < 1:
            return False
        student = await student_collection.find_one({"_id": ObjectId(id)})
        if student:
            updated_student = await student_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": data}
            )
            if updated_student:
                return True
            return False

    # Delete a student from the database
    async def delete_student(id: str) -> bool:
        student = await student_collection.find_one({"_id": ObjectId(id)})
        if student:
            await student_collection.delete_one({"_id": ObjectId(id)})
            return True
        return False


student_crud_service = StudentCrudService()
