import pytest
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from server.factory import create_app
from server.config import TestingConfig
from server.database import Base
from server.database.session import SESSION_APP_KEY, get_session_factory


@pytest.fixture(name='app')
def init_flask_app():
    flask_app = create_app(TestingConfig())

    # Init testing database
    engine = create_engine(flask_app.config['DATABASE_URL'])
    Base.metadata.create_all(bind=engine)

    # Relate Flask app with testing database
    session_factory = scoped_session(sessionmaker(bind=engine))
    flask_app.extensions[SESSION_APP_KEY] = session_factory

    with flask_app.app_context():
        yield flask_app


@pytest.fixture(name='session')
def init_db_session(app: Flask):
    session_factory = get_session_factory(app)

    with session_factory() as session:
        yield session


@pytest.fixture(name='client')
def init_test_client(app: Flask):
    return app.test_client()


@pytest.fixture(name='runner')
def init_test_runner(app: Flask):
    return app.test_cli_runner()
