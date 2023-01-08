from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...elastic.library import get_book

search = Blueprint('search', __name__, url_prefix='/search')


@search.route('', methods=['POST'])
def get_all() -> Response:
    return ApiResponse.response200({'res': get_book(request.json['description'])})
git