from typing import Annotated

from fastapi import APIRouter, Depends
from repository import *
from fastapi_2.repository import TasksRepository
from schemas import *

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)





@router.post("/tasks")
async def add_tast(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id =await TasksRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("/tasks")
async def get_tasks() -> list[STask]:
   tasks = await TasksRepository.find_all()
   return tasks



