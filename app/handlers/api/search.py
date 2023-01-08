from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...elasticsearch import es

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('', methods=['POST'])
def get_all() -> Response:
    # test = get_books()
    print(request.args, request.json)
    return ApiResponse.response200({'test': 'test', 'test2': 'test2'})
