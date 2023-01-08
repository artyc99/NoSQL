from flask import Blueprint, Response, request

from ..responses import ApiResponse
from ...database.library import get_books, insert_book, delete_book, get_book, update_book
from ...hazlecast import Cash
from ...models.library import Book
from ...parsers.book import request_parse

book = Blueprint('book', __name__, url_prefix='/book')


@book.route('', methods=['GET'])
@book.route('<book_id>', methods=['GET'])
def get_all(book_id: str = '') -> Response:
    cash = Cash()
    buff = cash.get()
    if book_id:
        hz = buff.get(book_id)
        if hz:
            response = hz
        else:
            response = get_book(book_id)
            buff.put(book_id, response)
    else:
        hz = buff.get('')
        if hz:
            response = hz
        else:
            response = get_books()
            buff.put(book_id, response)

    cash.close()
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
    cash = Cash()
    buff = cash.get()
    result = update_book(book_id, request_parse(request.json))
    buff.remove(book_id)
    buff.put(book_id, result)
    cash.close()
    return ApiResponse.response200(result)


@book.route('<book_id>', methods=['DELETE'])
def delete(book_id) -> Response:
    cash = Cash()
    buff = cash.get()
    buff.remove(book_id)
    cash.close()
    return ApiResponse.response200({'result': delete_book(book_id)})
