"""
Module to unit test the get_book_titles method using mocks
"""
import unittest
from unittest import mock

from client.get_book_titles import get_book_titles
from client.inventory_client import LibraryInventoryClient
from errors.ResourceNotFoundError import ResourceNotFoundError
from service.library_entities_pb2 import Book


class GetBookTitleUsingMockTestCase(unittest.TestCase):
    """
    Class to have methods that test various aspects of get_book_tiles function using mock client
    """

    def setUp(self):
        """
        To set up common fixtures
        """
        self.isbns = ['ISBN123', 'ISBN456']
        self.books = [Book(
            isbn='ISBN123',
            title='Mock Tripwire',
            author='Lee Child',
            genre='FICTION_ADVENTURE',
            pub_year=1987
        ), Book(
            isbn='ISBN456',
            title='Mock Egyptian Civilization',
            author='Mike Henry',
            genre='HISTORY',
            pub_year=1960
        )]
        self.titles = ['Mock Tripwire', 'Mock Egyptian Civilization']

    @mock.patch.object(LibraryInventoryClient, 'get_book_details')
    def test_get_book_title_no_error(self, mock_grpc_get_book_details):
        """
        Should return the expected book title list when there are no errors
        """
        # setting up the mock to return
        mock_grpc_get_book_details.side_effect = self.books

        # creating the client with mocked method
        inventory_client = LibraryInventoryClient("test", "test")

        # calling the method to test
        actual_titles = get_book_titles(inventory_client, self.isbns)

        # performing the verification
        mock_grpc_get_book_details.call_count = len(self.isbns)
        # specifying expected calls for the method
        expected_calls = [mock.call(self.isbns[0]), mock.call(self.isbns[1])]
        # verifying the calls are made as per specific order
        mock_grpc_get_book_details.assert_has_calls(expected_calls, any_order=False)

        # verifying the output
        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")

    @mock.patch.object(LibraryInventoryClient, 'get_book_details')
    def test_get_book_title_some_book_not_found(self, mock_grpc_get_book_details):
        """
            Should return the book titles which are present and skip the absent ones
        """
        self.isbns = ['ISBN123', 'ISBN12345678', 'ISBN456']

        def side_effect(isbn: str):
            if isbn == self.isbns[0]:
                return self.books[0]
            elif isbn == self.isbns[2]:
                return self.books[1]
            else:
                raise ResourceNotFoundError("Book Not Present")

        # setting up the mock with the fake calls
        mock_grpc_get_book_details.side_effect = side_effect

        # creating client with the mocked method
        inventory_client = LibraryInventoryClient("test","test")

        # calling the method to test
        actual_titles = get_book_titles(inventory_client, self.isbns)

        # performing the verification
        mock_grpc_get_book_details.call_count = len(self.isbns)
        # specifying expected calls for the method
        expected_calls = [mock.call(self.isbns[0]), mock.call(self.isbns[1]), mock.call(self.isbns[2])]
        # verifying the calls are made as per specific order
        mock_grpc_get_book_details.assert_has_calls(expected_calls, any_order=False)

        # verifying the output
        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")


class GetBookTitleUsingLiveTestCase(unittest.TestCase):
    """
    Class to have methods that test various aspects of get_book_tiles function using live client
    """

    def setUp(self):
        """
        To set up common fixtures and objects
        """
        self.isbns = ['ISBN123', 'ISBN456']
        self.titles = ['Tripwire', 'Egyptian Civilization']

        # creating a live client
        self.inventory_client = LibraryInventoryClient("localhost", "50051")

    def test_get_book_title_no_error(self):
        """
        Should return the expected book title list when there are no errors
        """

        # calling the method to test
        actual_titles = get_book_titles(self.inventory_client, self.isbns)

        # verifying the output
        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")

    def test_get_book_title_some_book_not_found(self):
        """
            Should return the book titles which are present and skip the absent ones
        """
        self.isbns = ['ISBN123', 'ISBN12345678', 'ISBN456']

        # calling the method to test
        actual_titles = get_book_titles(self.inventory_client, self.isbns)

        # verifying the output
        self.assertEqual(self.titles, actual_titles, "The titles are not as expected.")




