from server.config import DevelopmentConfig
from server.factory import create_app


if __name__ == '__main__':
    app = create_app(DevelopmentConfig())

    app.run()
