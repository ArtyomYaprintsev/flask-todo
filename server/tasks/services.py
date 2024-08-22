from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from .models import Task
from .schemas import CreateTask, UpdateTask


def create_task(session: Session, create_task: CreateTask) -> Task:
    task = session.execute(
        insert(Task)
        .values(**create_task.model_dump())
        .returning(Task)
    )
    return task.scalars().one()


def get_tasks(session: Session):
    tasks = session.execute(select(Task))
    return tasks.scalars().all()


def get_task_by_id(session: Session, task_id: str):
    task = session.execute(select(Task).where(Task.id == task_id))
    return task.scalars().first()


def update_task(
    session: Session,
    task: Task,
    update_task: UpdateTask,
) -> Task:
    session.execute(
        update(Task)
        .where(Task.id == task.id)
        .values(**update_task.model_dump(exclude_none=True))
    )
    session.refresh(task)
    return task


def delete_task(session: Session, task_id: str) -> None:
    session.execute(delete(Task).where(Task.id == task_id))
