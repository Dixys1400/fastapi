from fastapi_2.database import new_session
from main import STaskAdd
from database import TasksOrm
from sqlalchemy import select
from schemas import STask


class TasksRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()

            return task.id





    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TasksOrm)
            result = await session.execute(query)
            task_model = result.scalars().all()
            task_schemas= [STask.model_validate(task_model) for task_model in task_model]
            return task_schemas















