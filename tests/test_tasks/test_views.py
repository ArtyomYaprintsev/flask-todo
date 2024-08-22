import json
import pytest
from flask.testing import FlaskClient
from sqlalchemy.orm import Session
from pydantic import ValidationError

from server.core import status
from server.tasks.models import Task
from server.tasks.schemas import BaseTask, ReadTask


BASE_URL = '/tasks/'


def _insert_task(session: Session, task: Task) -> BaseTask:
    session.add(task)
    session.commit()
    session.refresh(task)
    return BaseTask(**task.__dict__)


@pytest.fixture(name='task')
def create_task(session: Session) -> BaseTask:
    return _insert_task(session, Task(header='General task'))


@pytest.fixture(name='tasks_list')
def create_tasks_list(session: Session) -> list[BaseTask]:
    return [
        _insert_task(session, Task(header=f'task-#{index + 1}'))
        for index in range(5)
    ]


def test_get_tasks_list(client: FlaskClient, tasks_list: list[BaseTask]):
    response = client.get(BASE_URL)

    assert response.status_code == status.HTTP_200_OK

    data = json.loads(response.data)
    assert len(data) == len(tasks_list)

    # Validate each task is ReadTask instance
    try:
        converted_data = [ReadTask.model_validate(task) for task in data]
    except ValidationError:
        raise AssertionError('Received invalid tasks')

    initial_task_ids = set(task.id for task in tasks_list)
    received_task_ids = set(task.id for task in converted_data)

    assert initial_task_ids == received_task_ids


def test_get_task(client: FlaskClient, task: BaseTask):
    response = client.get(BASE_URL + str(task.id) + '/')

    assert response.status_code == status.HTTP_200_OK

    data = json.loads(response.data)

    converted_data = ReadTask.model_validate(data)
    assert data == ReadTask.model_validate(task)
