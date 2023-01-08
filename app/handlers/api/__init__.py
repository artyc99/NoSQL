from flask import Blueprint, Response

from ..responses import ApiResponse

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('', methods=['GET'])
def info() -> Response:
    return ApiResponse.response200({'test': 'test', 'test2': 'test2'})
