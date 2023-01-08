from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...database.library import get_books

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('', methods=['GET'])
def get_all() -> Response:
    test = get_books()
    print(request.args)
    return ApiResponse.response200({'test': 'test', 'test2': 'test2'})


@book.route('', methods=['POST'])
def add() -> Response:
    # test = get_books()
    print(request.json)
    return ApiResponse.response200({'test': 'test', 'test2': 'test2'})


@book.route('<book_id>', methods=['PUT'])
def update(book_id) -> Response:
    # test = get_books()
    print(request.json, request.args)
    return ApiResponse.response200({'test': 'test', 'test2': 'test2'})


@book.route('<book_id>', methods=['DELETE'])
def delete(book_id) -> Response:
    # test = get_books()
    print(request.json, request.args)
    return ApiResponse.response200({'test': 'test', 'test2': 'test2'})
