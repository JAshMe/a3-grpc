import library_entities_pb2 as _library_entities_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookRequest(_message.Message):
    __slots__ = ["bookToCreate"]
    BOOKTOCREATE_FIELD_NUMBER: _ClassVar[int]
    bookToCreate: _library_entities_pb2.Book
    def __init__(self, bookToCreate: _Optional[_Union[_library_entities_pb2.Book, _Mapping]] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["result", "status"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    result: str
    status: _library_entities_pb2.ResponseStatus
    def __init__(self, result: _Optional[str] = ..., status: _Optional[_Union[_library_entities_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: _library_entities_pb2.Book
    status: _library_entities_pb2.ResponseStatus
    def __init__(self, book: _Optional[_Union[_library_entities_pb2.Book, _Mapping]] = ..., status: _Optional[_Union[_library_entities_pb2.ResponseStatus, _Mapping]] = ...) -> None: ...
