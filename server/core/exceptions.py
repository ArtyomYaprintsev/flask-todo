from server.core import status
from server.core.status import HTTP_400_BAD_REQUEST


class BaseException(Exception):
    """Base application exception.

    Receives a message and a status code.
    """

    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ) -> None:
        super().__init__(message, status_code)
        self.message = message
        self.status_code = status_code


class NotFoundException(BaseException):
    def __init__(self, class_name: str) -> None:
        msg = f'{class_name} not found.'
        super().__init__(msg, status.HTTP_404_NOT_FOUND)
