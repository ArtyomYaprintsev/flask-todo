from functools import wraps
from flask import Flask, current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, scoped_session


SESSION_APP_KEY = 'session_factory'


def get_session_factory(app: Flask) -> scoped_session[Session]:
    if SESSION_APP_KEY not in app.extensions:
        engine = create_engine(
            app.config.get('DATABASE_URL', ''),
            echo=app.config.get('SQLALCHEMY_ECHO', False),
        )
        session_factory = scoped_session(
            sessionmaker(
                bind=engine,
                autocommit=False,
                autoflush=False,
            )
        )
        app.extensions[SESSION_APP_KEY] = session_factory

    return app.extensions[SESSION_APP_KEY]


def provide_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session_factory = get_session_factory(current_app)
        session = session_factory()
        try:
            response = func(*args, **kwargs, session=session)
            session.commit()
            return response
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    return wrapper
