"""
This module has an Inventory Client class which will encapsulate the gRPC client for the API.
It would be responsible for connecting with the Inventory System that serves information via gRPC.
It will connect and exchange data with the gRPC server.
"""
import grpc

from errors.BadArgumentError import BadArgumentError
from errors.ResourceNotFoundError import ResourceNotFoundError
from service.inventory_service_pb2 import GetBookRequest
from service.inventory_service_pb2_grpc import LibraryInventoryStub


class LibraryInventoryClient:
    """
    Encapsulating Class to exchange data with gRPC server of Inventory System
    """
    def __init__(self, grpc_server_address, grpc_server_port):
        self.server_address = grpc_server_address
        self.server_port = grpc_server_port

        # create an insecure channel for connection with gRPC server with given address and port
        self.channel = grpc.insecure_channel(grpc_server_address + ':' + grpc_server_port)

        # create the stub that would facilitate the RPC call to the server via given channel
        self.stub = LibraryInventoryStub(self.channel)

    def get_book_details(self, isbn):
        """
        Method to get details of the book with given isbn. It will fetch the data from gRPC server hosted by
        Inventory System
        :param isbn: string.
        :return: Book object defined in the protocol buffers. If any error, then returns None
        """
        try:
            print("Fetching data for ISBN: " + isbn + " from gRPC Server..")
            get_book_req = GetBookRequest(isbn=isbn)
            get_book_resp = self.stub.GetBook(get_book_req)
        except grpc.RpcError as err:
            print("gRPC ERROR: [" + err.code().name + "]: Couldn't fetch data for ISBN: " + isbn + " from gRPC Server..")
            if grpc.StatusCode.NOT_FOUND == err.code():
                raise ResourceNotFoundError(err.details())
            if grpc.StatusCode.INVALID_ARGUMENT == err.code():
                raise BadArgumentError(err.details())
        else:
            print("Fetched data for ISBN: " + isbn + " from gRPC Server..")
            return get_book_resp.book
