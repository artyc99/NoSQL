from typing import TypeVar, Generic, Dict

from bson import ObjectId

__BookType = TypeVar('__BookType')


class Book(Generic[__BookType]):
    def __init__(self, title: str = '', description: str = '', book_id: ObjectId = None):
        # If id is '' ~~ item not in database

        self.book_id: ObjectId
        self.title: str = title
        self.description: str = description

        if book_id is not None:
            self.book_id = book_id

    def to_dict_with_id(self) -> Dict:
        return {
            '_id': self.book_id,
            'title': self.title,
            'description': self.description
        }

    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'description': self.description
        }
