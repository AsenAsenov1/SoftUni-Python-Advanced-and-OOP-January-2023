class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page: int):
        if page >= 0 and isinstance(page, int):
            self.page = page

    def __str__(self):
        return f'Book title: "{self.title}"\nAuthor: {self.author}'


class Library:
    def __init__(self, books: list):
        self.books = books

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book


book_1 = Book("Game Of Thrones", "G. Martin")
book_2 = Book("Hobbit", "J. R. R. Tolkien")
books_list = [book_1, book_2]
library = Library(books_list)

print(library.find_book("Game Of Thrones"))

book_2.turn_page(5)
print(book_2.page)

book_2.turn_page(53)
print(book_2.page)

book_2.turn_page(3.5)
print(book_2.page)
