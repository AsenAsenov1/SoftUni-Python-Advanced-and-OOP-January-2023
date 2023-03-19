class Book:

    def __init__(self, content):
        self.content = content


class Formatter:
    @staticmethod
    def format(book):
        return book.content


class Printer:
    @staticmethod
    def get_book(book, formatter):
        return formatter.format(book)


book = Book("book")
formatter = Formatter()
printer = Printer()

print(printer.get_book(book, formatter))
