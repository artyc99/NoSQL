from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...database.library import get_books, insert_book, delete_book, get_book, update_book
from ...hazlecast import map
from ...models.library import Book
from ...parsers.book import request_parse

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('', methods=['GET'])
@book.route('<book_id>', methods=['GET'])
def get_all(book_id: str = '') -> Response:
    if book_id:
        hz = map.get(book_id)
        if hz:
            response = hz
        else:
            response = get_book(book_id)
            map.put(book_id, response)
    else:
        hz = map.get('')
        if hz:
            response = hz
        else:
            response = get_books()
            map.put(book_id, response)
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
    result = update_book(book_id, request_parse(request.json))
    map.remove(book_id)
    map.put(book_id, result)
    return ApiResponse.response200(result)


@book.route('<book_id>', methods=['DELETE'])
def delete(book_id) -> Response:
    map.remove(book_id)
    return ApiResponse.response200({'result': delete_book(book_id)})
