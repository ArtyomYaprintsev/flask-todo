"""
HTTP methods
Source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
"""

from __future__ import annotations

__all__ = (
    'HEAD',
    'OPTIONS',
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'PATCH',
)

HEAD = 'HEAD'
OPTIONS = 'OPTIONS'
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
PATCH = 'PATCH'

SAFE_METHODS = (HEAD, OPTIONS, GET)
