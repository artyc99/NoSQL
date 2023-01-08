from bson import ObjectId

from . import mongo_db_connection
from ..models.library import Book
from ..parsers.book import mongo_parse

__MONGO_DB_CONNECTION = mongo_db_connection


def insert_book(book: Book):
    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            __MONGO_DB_CONNECTION['api']['library'].insert_one(book.to_dict(), session=db_session)


def get_books():
    results = []

    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            results = [mongo_parse(item).to_dict_with_id() for item in __MONGO_DB_CONNECTION['api']['library'].find()]
            # print([item for item in __MONGO_DB_CONNECTION['api']['library'].find()])
    return {'results': results}


def delete_book(book_id):
    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            __MONGO_DB_CONNECTION['api']['library'].delete_one({'_id': book_id})

    return True
