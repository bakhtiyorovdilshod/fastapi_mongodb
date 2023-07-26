from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from src.student.routers.student import router as student_router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}

app.include_router(student_router, tags=["Student"], prefix="/student")

# app endpoints

# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
