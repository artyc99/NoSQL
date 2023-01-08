from . import elastic_connection
from ..models.library import Book

__ELASTIC_CONNECTION = elastic_connection


def insert_book(book: Book):
    result = __ELASTIC_CONNECTION.index(index='books', id=str(book.book_id), body=book.to_dict())

    return result['result']


def get_book(description: str):
    result = __ELASTIC_CONNECTION.search(
        index='books',
        body={
            'query': {
                "description": description
            }
        }
    )

    return result


def update_book(book_id, book):
    result = __ELASTIC_CONNECTION.update(index='books', id=book_id,
                                         body=book.to_dict())

    return {'result': True}


def delete_book(book_id: str):
    __ELASTIC_CONNECTION.delete(index='books', id=book_id)

    return True
