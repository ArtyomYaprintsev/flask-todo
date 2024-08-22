from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, validates

from server.database import Base
from server.core.utils import generate_str_code


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[str] = mapped_column(
        sa.String(40),
        primary_key=True,
        default=lambda: generate_str_code(length=5),
    )
    header: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    description: Mapped[str] = mapped_column(
        sa.Text(255),
        default='',
        nullable=False,
    )

    is_completed: Mapped[bool] = mapped_column(sa.Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(
        sa.DateTime,
        default=sa.func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        sa.DateTime,
        default=sa.func.now(),
    )

    @validates('header')
    def validate_header_min_length(self, key: str, value: str) -> str:
        min_length = 5

        if len(value) < min_length:
            raise ValueError(
                f'Task header must be at least {min_length} characters long.',
            )

        return value
