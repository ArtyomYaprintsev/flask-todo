from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field


class BaseTask(BaseModel):
    id: str
    header: str
    description: str = ''
    is_completed: bool = False
    created_at: datetime
    updated_at: datetime


class ReadTask(BaseTask):
    pass


class CreateTask(BaseModel):
    header: str = Field(max_length=100, min_length=5)
    description: str = Field(max_length=255, default='')


class UpdateTask(BaseModel):
    header: str | None = Field(max_length=100, min_length=5, default=None)
    description: str | None = Field(max_length=255, default=None)
    is_completed: bool | None = None


class InternalUpdateTask(UpdateTask):
    updated_at: datetime = Field(default_factory=datetime.now)
