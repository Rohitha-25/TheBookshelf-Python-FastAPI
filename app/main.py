from fastapi import FastAPI
from app.database import engine, base
from app.controller import book_controller

base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Management API")

app.include_router(book_controller.router)