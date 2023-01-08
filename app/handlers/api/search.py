from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...elastic.library import get_book
from ...hazlecast import Cash

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('', methods=['POST'])
def get_all() -> Response:
    result = {}
    cash = Cash()
    buf = cash.get()
    hz = buf.get(request.json['description'])
    if hz:
        result = hz
    else:
        result = {'res': get_book(request.json['description'])}
        buf.put(request.json['description'], result)

    cash.close()
    return ApiResponse.response200(result)
