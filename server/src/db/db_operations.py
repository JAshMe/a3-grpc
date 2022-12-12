"""
This module would be used to define various kinds of operations defined on the book db
"""
from server.src.db.mock_inventory_db import book_db
from server.src.errors.ResourceExistsError import ResourceExistsError
from server.src.errors.ResourceNotFoundError import ResourceNotFoundError
from src.service.library_entities_pb2 import Book


def add_book(book_to_add: Book):
    """
    Adds the book in the given book_db, if that book doesn't exist. Raises errors if the book exists.
    :param book_to_add: An object containing {isbn, title, author, genre, pub_year} attributes
    :return: nothing
    :raises: ResourceAlreadyExistsError if the book already exists in db
    """

    if book_to_add.isbn in book_db:
        raise ResourceExistsError("Book with ISBN: " + book_to_add.isbn + " already exists!")

    book_db[book_to_add.isbn] = {
        'isbn': book_to_add.isbn,
        'author': book_to_add.author,
        'title': book_to_add.title,
        'genre': Book.Genre.Name(book_to_add.genre),
        'pub_year': book_to_add.pub_year
    }

    print("Book Created: ", book_to_add)


def get_book(isbn: str):
    """
    Gets the required book from the book_db.
    :param isbn: ISBN of the book whose details are to be fetched
    :return: Book object, if book found.
    :raises: ResourceNotFoundError if the book is not present
    """
    if isbn not in book_db:
        raise ResourceNotFoundError("Book with ISBN: " + isbn + " not found!")

    book = book_db[isbn]
    print("Book found for isbn: ", isbn)
    return Book(
        isbn=book['isbn'],
        title=book['title'],
        author=book['author'],
        pub_year=book['pub_year'],
        genre=book['genre']
    )


