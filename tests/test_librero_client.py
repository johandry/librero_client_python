import unittest
import os, subprocess
from librero_client.client import LibreroClient as lc

LIBRERO_PORT = '3100'

class TestModule(unittest.TestCase):
  def setUp(self):
    # Start server
    self.server_process = None
    serverPath = '../librero/bin/librero'
    if not os.path.exists(serverPath):
      return
    env = dict(os.environ)
    env['LIBRERO_LOG_LEVEL'] = 'DEBUG'
    env['LIBRERO_PORT'] = LIBRERO_PORT
    p = subprocess.Popen([serverPath], env=env)
    self.server_process = p
    self.address = 'localhost:'+LIBRERO_PORT
    return super().setUp()
  
  def tearDown(self):
    # Stop server
    if not self.server_process:
      return
    self.server_process.terminate()

    return super().tearDown()

  def test_create_book(self):
    with lc.LibreroClient(self.address) as client:
      book = client.CreateBook(title="Python Programming", url="http://example.com/python", tags=["programming", "python"])
      self.assertEqual({
        "id": 1, 
        "title": "Python Programming", 
        "url": "http://example.com/python", 
        "tags": ["programming", "python"],
        }, book)
      self.assertEqual(f"Book ID: {book.id}, Title: '{book.title}', URL: '{book.url}', Tags: {book.tags}", lc.BookStr(book))
    pass

if __name__ == "__main__":
  unittest.main()
