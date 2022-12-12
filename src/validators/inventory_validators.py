"""
This module would have methods that would validate whether a given book is valid or not.
"""

from src.service.inventory_service_pb2 import CreateBookRequest, GetBookRequest


def validate_create_book_request(request: CreateBookRequest):
    """
    Validates the request received for creating a book in the inventory
    :param request: The request received by RPC
    :return: The invalidation message, if the request is invalid, else None.
    """
    if not request.HasField('bookToCreate'):
        return "The request needs to have a 'bookToCreate' attribute having an object of Book to be added in " \
              "inventory. To get the attributes of Book, refer to the Book message 'library_entities.proto' "

    book_to_create = request.bookToCreate
    if (not book_to_create.HasField('isbn')) or (book_to_create.isbn is None) or (book_to_create.isbn == ""):
        return "The 'isbn' of the book should not be empty. It has to have some string value."

    if (not book_to_create.HasField('title')) or (book_to_create.title is None) or (book_to_create.title == ""):
        return "The 'title' of the book should not be empty. It has to have some string value."

    return None


def validate_get_book_request(request: GetBookRequest):
    """
        Validates the request received for getting a book in the inventory
        :param request: The request received by RPC
        :return: The invalidation message, if the request is invalid, else None.
        """
    if not request.HasField('isbn'):
        return "The request needs to have a 'isbn' attribute specifying the ISBN of the book to fetch from " \
               "inventory."

    return None

