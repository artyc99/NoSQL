from typing import TypeVar, Generic, Dict

__BookType = TypeVar('__BookType')


class Book(Generic[__BookType]):
    def __init__(self, title: str = '', description: str = '', url: str = ''):
        # If id is '' ~~ item not in database
        self.id: str = ''
        self.title: str = title
        self.description: str = description

    def to_dict(self) -> Dict:
        return {
            '_id': self.id,
            'title': self.title,
            'description': self.description
        }
