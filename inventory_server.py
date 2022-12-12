# Main class to define the grpc server
from concurrent import futures
import grpc

import service.inventory_service_pb2_grpc as inventory_service_grpc
from service.library_entities_pb2 import *
from db import db_operations
from errors.ResourceNotFoundError import ResourceNotFoundError
from errors.ResourceExistsError import ResourceExistsError
from service.inventory_service_pb2 import CreateBookResponse, GetBookResponse
from validators.inventory_validators import validate_create_book_request, validate_get_book_request


# This class provides an implementation of methods of the LibraryInventory service


class LibraryInventoryServicer(inventory_service_grpc.LibraryInventoryServicer):

    """Implements the functionality defined by the proto service"""
    def CreateBook(self, request, context):
        """
        RPC Method to Create a book in the inventory, after performing validations on the book.
        :param request: Contains the 'book' attribute that gives book to be created
        :param context: Servicer context used to set the status code and response details
        :return: CreateBookResponse containing the result (book created or not) and the ResponseStatus
        """
        validation_msg = validate_create_book_request(request)
        if validation_msg is not None:  # means there is some issue with the request.
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(validation_msg)

            status = ResponseStatus(
                code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                message=grpc.StatusCode.INVALID_ARGUMENT.name + ": " + validation_msg
            )

            return CreateBookResponse(result="Book not created.", status=status)

        try:
            db_operations.add_book(request.bookToCreate)
        except ResourceExistsError as err:
            print("Couldn't add the book. Exception: ", err)

            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(str(err))

            status = ResponseStatus(
                code=grpc.StatusCode.ALREADY_EXISTS.value[0],
                message=grpc.StatusCode.ALREADY_EXISTS.name + ": " + str(err)
            )

            return CreateBookResponse(result="Book not created.", status=status)
        else:
            return CreateBookResponse(result="Book with isbn: " + request.bookToCreate.isbn + " created.")

    def GetBook(self, request, context):
        validation_msg = validate_get_book_request(request)
        if validation_msg is not None:  # means there is some issue with the request.
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details(validation_msg)

            status = ResponseStatus(
                code=grpc.StatusCode.INVALID_ARGUMENT.value[0],
                message=grpc.StatusCode.INVALID_ARGUMENT.name + ": " + validation_msg,
            )

            return GetBookResponse(status=status)

        try:
            book: Book = db_operations.get_book(request.isbn)
        except ResourceNotFoundError as err:
            print("Couldn't find the book. Exception: ", err)

            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(str(err))

            status = ResponseStatus(
                code=grpc.StatusCode.ALREADY_EXISTS.value[0],
                message=grpc.StatusCode.ALREADY_EXISTS.name + ": " + str(err),
            )

            return GetBookResponse(status=status)
        else:
            return GetBookResponse(book=book)


def serve():
    # create a grpc server with 10 threads in its pool, to service various rpcs
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # add the LibraryInventoryServicer to the grpc server
    inventory_service_grpc.add_LibraryInventoryServicer_to_server(LibraryInventoryServicer(), server)

    # start server
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started listening at: localhost:50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

