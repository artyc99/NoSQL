from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...database.library import get_books, insert_book, delete_book, get_book, update_book
from ...models.library import Book
from ...parsers.book import request_parse

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('', methods=['GET'])
@book.route('<book_id>', methods=['GET'])
def get_all(book_id: str = '') -> Response:
    if book_id:
        response = get_book(book_id)
    else:
        response = get_books()
    return ApiResponse.response200(response)


@book.route('', methods=['POST'])
def add() -> Response:
    data = request.json
    test = insert_book(Book(
        title=data['title'],
        description=data['description']
    ))
    return ApiResponse.response200({'result': test})


@book.route('<book_id>', methods=['PUT', 'UPDATE'])
def update(book_id) -> Response:
    # test = get_books()
    print(request.json, request.args)
    return ApiResponse.response200(update_book(book_id, request_parse(request.json)))


@book.route('<book_id>', methods=['DELETE'])
def delete(book_id) -> Response:
    return ApiResponse.response200({'result': delete_book(book_id)})
