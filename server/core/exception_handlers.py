from pydantic_core import ValidationError

from . import status
from .exceptions import BaseException


def handle_pydantic_validation_error(err: ValidationError):
    data = {
        'detail': [
            {
                'loc': error['loc'],
                'msg': error['msg'],
                'type': error['type'],
            }
            for error in err.errors()
        ],
    }

    return data, status.HTTP_400_BAD_REQUEST


def handle_base_exception(err: BaseException):
    data = {'detail': err.message}

    return data, err.status_code
