from app.models.library import Book


def mongo_parse(item):
    return Book(title=item['title'], description=item['description'], book_id=item['_id'])
