"""The Python implementation of the gRPC librero client."""

import grpc
import librero_pb2_grpc
import librero_pb2
from typing import Iterable

class LibreroClient(object):
  stud: librero_pb2_grpc.LibreroServiceStub

  def __init__(self, address: str):
    if address == None:
      raise ValueError("address is required")

    self.address = address
    self.channel = grpc.insecure_channel(address)


  def __enter__(self):
    try:
      grpc.channel_ready_future(self.channel).result(timeout=10)
    except grpc.FutureTimeoutError:
      raise
    else:
      self.stud = librero_pb2_grpc.LibreroServiceStub(self.channel)
    return self.stud

  def __exit__(self, *args):
      self.close()

  def close(self) -> None: 
    self.channel.close()

  def CreateBook(self,
      title: str, 
      url: str | None = ...,
      tags: Iterable[str] | None = ...) -> librero_pb2.Book:
    response = self.stud.CreateBook(librero_pb2.CreateBookRequest(title=title, url=url, tags=tags))
    return response.book

  def GetBook(self,
      id: int | None = ...,
      title: str | None = ...) -> librero_pb2.Book:
    response = self.stud.GetBook(librero_pb2.GetBookRequest(id=id, title=title))
    return response.book

  def GetBookList(self,
      tags: Iterable[str] | None = ...) -> Iterable[librero_pb2.Book]:
    response = self.stud.GetBookList(librero_pb2.GetBookListRequest(tags=tags))
    return response.list

  def GetBookTags(self,
      search: str | None = ...) -> Iterable[str]:
    response = self.stud.GetBookTags(librero_pb2.GetBookTagsRequest(search=search))
    return response.list

  def UpdateBook(self,
      id: int,
      title: str | None = ...,
      url: str | None = ...,
      tags: Iterable[str] | None = ...) -> librero_pb2.Book:
    response = self.stud.UpdateBook(librero_pb2.UpdateBookRequest(id=id, title=title, url=url, tags=tags))
    return response.book

  def DeleteBook(self,
      id: int) -> None:
    return self.stud.DeleteBook(librero_pb2.DeleteBookRequest(id=id))

def book2str(book: librero_pb2.Book) -> str:
  return f"Book ID: {book.id}, Title: '{book.title}', URL: '{book.url}', Tags: {book.tags}"