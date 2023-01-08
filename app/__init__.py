from flask import Flask


from .handlers import HandlersRegistrator


class FlaskApplication:

    def __init__(self) -> None:
        self.__flaskApp = Flask(__name__)

        self.__register_blueprints()

    def __configurate(self) -> None:
        pass

    def __register_blueprints(self) -> None:
        HandlersRegistrator(self.__flaskApp)

    def run(self) -> None:
        self.__flaskApp.run(host='0.0.0.0', port=5000)
