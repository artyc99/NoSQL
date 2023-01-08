from bson import ObjectId

from . import mongo_db_connection
from ..models.library import Book
from ..parsers.book import mongo_parse
from ..elastic import library as el_s

__MONGO_DB_CONNECTION = mongo_db_connection


def insert_book(book: Book):
    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            book.book_id = __MONGO_DB_CONNECTION['api']['library'].insert_one(book.to_dict(), session=db_session).inserted_id

    if book.book_id:
        el_s.insert_book(book)

    return mongo_parse(book).to_dict_with_id()


def get_books():
    results = []

    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            results = [mongo_parse(item).to_dict_with_id() for item in __MONGO_DB_CONNECTION['api']['library'].find()]
    return {'results': results}


def get_book(book_id: str):
    result = {}

    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            mongo_result = __MONGO_DB_CONNECTION['api']['library'].find_one({'_id': ObjectId(book_id)})

            if mongo_result:
                result = mongo_parse(mongo_result).to_dict_with_id()
    return {'result': result}


def update_book(book_id, book):
    result = {}

    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            mongo_result = __MONGO_DB_CONNECTION['api']['library'].find_one_and_update(
                {"_id": ObjectId(book_id)},
                {
                    "$set":
                    {
                        "title": book.title,
                        'description': book.description
                    }
                }, upsert=True
            )

            if mongo_result:
                result = mongo_parse(mongo_result).to_dict_with_id()

                update_book(book_id, book)

    return {'result': result}


def delete_book(book_id: str):
    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            __MONGO_DB_CONNECTION['api']['library'].delete_one({'_id': ObjectId(book_id)})

            delete_book(book_id)

    return True
