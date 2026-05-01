from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
if __name__ == "__main__":
    b1 = Book("1984", "George Orwell", 328)
    print(b1)
