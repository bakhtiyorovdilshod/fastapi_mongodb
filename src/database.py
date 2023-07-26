import motor.motor_asyncio

MONGO_DETAILS = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.fastapi_mongo_db

student_collection = database.get_collection('students_collection')