class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}>"

    @classmethod
    def hardcover(cls, name, weight):
        # return Book(name, Book.TYPES[0], weight + 100)
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        # return Book(name, Book.TYPES[1], weight + 50)
        return cls(name, cls.TYPES[1], weight + 50)

    @staticmethod
    def static_method():
        # this method can stay outside the class without any problem
        print("Calling static_method")


book = Book.hardcover("Neuromancer", 200)
book2 = Book.paperback("Monalisa Overdrive", 200)
book3 = Book.static_method()

print(book)
print(book2)
print(book3)
