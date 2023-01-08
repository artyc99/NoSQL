from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...database.library import get_books, insert_book, delete_book
from ...models.library import Book

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('', methods=['GET'])
@book.route('<book_id>', methods=['GET'])
def get_all(book_id: str = '') -> Response:
    if book_id:
        response = {}
    else:
        response = get_books()
    return ApiResponse.response200(response)


@book.route('', methods=['POST'])
def add() -> Response:
    test = insert_book(Book())
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
    return ApiResponse.response200({'result': delete_book(None)})
