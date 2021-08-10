class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Elden Ring", 120)
book2 = Book("GOT", 520)
book_shelf = BookShelf(book, book2)
print(book_shelf)
