from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...elastic.library import get_book
from ...hazlecast import map

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('', methods=['POST'])
def get_all() -> Response:
    result = {}
    hz = map.get(request.json['description'])
    if hz:
        result = hz
    else:
        result = {'res': get_book(request.json['description'])}
        map.put(request.json['description'], result)
    return ApiResponse.response200(result)
