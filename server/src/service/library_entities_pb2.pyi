from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "pub_year", "title"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    FICTION_ADVENTURE: Book.Genre
    FICTION_ROMANTIC: Book.Genre
    FICTION_THRILLER: Book.Genre
    GENRE_FIELD_NUMBER: _ClassVar[int]
    HISTORY: Book.Genre
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PHILOSOPHY: Book.Genre
    PUB_YEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.Genre
    isbn: str
    pub_year: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.Genre, str]] = ..., pub_year: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventory_number", "status"]
    class IssueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.IssueStatus
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.IssueStatus
    book: Book
    inventory_number: int
    status: InventoryItem.IssueStatus
    def __init__(self, inventory_number: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.IssueStatus, str]] = ...) -> None: ...

class ResponseStatus(_message.Message):
    __slots__ = ["code", "details", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    message: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
