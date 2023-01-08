from . import mongo_db_connection
from ..models.library import Book

__MONGO_DB_CONNECTION = mongo_db_connection


def insert_book(book: Book):
    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            __MONGO_DB_CONNECTION['api']['library'].insert_one(book.to_dict(), session=db_session)


def get_books():
    with __MONGO_DB_CONNECTION.start_session() as db_session:
        with db_session.start_transaction():
            for item in __MONGO_DB_CONNECTION['api']['library'].find():
                print(item)

