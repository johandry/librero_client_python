# Librero Client in Python

This python package is to use the Librero API easily without the need to import gRPC and Buf Connect generated packages.

## Instalation

```bash
pip install librero_client
```

## Use 

```python
import librero_client as lc

def main():
  address = 'localhost:3100'
  with lc.LibreroClient(address) as client:
    print("== Create Books ==")
    book = client.CreateBook(title="Python Programming", url="http://example.com/python", tags=["programming", "python"])
    print("Book 1 Created: " + lc.BookStr(book))
    print("== Get Books ==")
    list = client.GetBookList()
    print("Books: ")
    for i, book in enumerate(list, start=1):
      print(f"Book {i}: " + lc.BookStr(book))

if __name__ == "__main__":
  main()
```
