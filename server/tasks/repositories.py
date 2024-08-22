from sqlalchemy.orm import Session

from server.core import exceptions as exc

from .models import Task
from .services import get_task_by_id


def get_task_or_404(session: Session, task_id: str):
    task = get_task_by_id(session, task_id)

    if task:
        return task

    raise exc.NotFoundException(Task.__name__)
