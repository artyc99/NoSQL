from flask import Flask


class HandlersRegistrator:
    def __init__(self, flask_obj: Flask) -> None:
        from .api import api as api_info_handler
        flask_obj.register_blueprint(api_info_handler)
