from flask import Blueprint, request
from sqlalchemy.orm import Session

from server.core import method, status
from server.database import provide_session

from . import services as task_services
from .schemas import ReadTask, CreateTask, UpdateTask, InternalUpdateTask
from .repositories import get_task_or_404


tasks = Blueprint('tasks', __name__, url_prefix='/tasks/')


@tasks.route('/')
@provide_session
def get_tasks_list(session: Session):
    return [
        ReadTask(**task.__dict__).model_dump()
        for task in task_services.get_tasks(session)
    ]


@tasks.route('/', methods=[method.POST])
@provide_session
def create_task(session: Session):
    task_data = CreateTask(**request.get_json())
    created_task = task_services.create_task(session, task_data)
    return (
        ReadTask(**created_task.__dict__).model_dump(),
        status.HTTP_201_CREATED,
        {'Location': f'/tasks/{created_task.id}'},
    )


@tasks.route('/<string:task_id>/')
@provide_session
def retrieve_task(session: Session, task_id: str):
    task = get_task_or_404(session, task_id)
    return ReadTask(**task.__dict__).model_dump()


@tasks.route('/<string:task_id>/', methods=[method.PUT])
@provide_session
def update_task(session: Session, task_id: str):
    task = get_task_or_404(session, task_id)

    task_data = UpdateTask(**request.get_json())
    internal_task_data = InternalUpdateTask(**task_data.model_dump())

    updated_task = task_services.update_task(session, task, internal_task_data)
    return ReadTask(**updated_task.__dict__).model_dump()


@tasks.route('/<string:task_id>/', methods=[method.DELETE])
def delete_task(session: Session, task_id: str):
    task = get_task_or_404(session, task_id)
    task_services.delete_task(session, task)
    return '', status.HTTP_204_NO_CONTENT
