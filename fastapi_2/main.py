from typing import Optional, Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import create_tables
from contextlib import asynccontextmanager
from schemas import *
from router import router as tasks_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")




app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)








