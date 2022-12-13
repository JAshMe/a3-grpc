"""
Module to fetch the book titles from the Inventory Service
"""
from inventory_client import LibraryInventoryClient


def get_book_titles(grpc_client: LibraryInventoryClient, isbns: [str]):
    """
    Method to get the book titles for given isbns. It gets the titles of these books from Inventory Services.
    It skips the isbns, for which the book is not present in the inventory
    :param grpc_client: Client that would make the gRPC call to the Inventory server
    :param isbns: List of string. Each element corresponds to an isbn of a book
    :return: List of string. Each element corresponds to title of the book for given isbn.
    """
    titles = []
    print("Getting titles for ISBNs: " + str(isbns))
    for isbn in isbns:
        try:
            # get the details of book from grpc client
            print("Getting details for ISBN:" + isbn)
            book = grpc_client.get_book_details(isbn)
        except Exception as ex:  # if book not found, or any other call failure
            print("ERROR: ", ex)
            print("Skipping the ISBN: ", isbn)
        else:
            # extract out the title and add that title to the list
            titles.append(book.title)

    return titles


if __name__ == '__main__':
    # instantiate the client
    inventory_client = LibraryInventoryClient('localhost', '50051')
    # calling the get_book_titles for some isbns
    book_titles = get_book_titles(inventory_client, ['ISBN852', 'ISBN963'])
    # printing those titles
    print(book_titles)

