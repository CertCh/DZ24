
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# Пример использования классов
book1 = Book("1984", "George Orwell")
book2 = Book("Hello", "Aldous Huxley")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.remove_book(book1)

found_book = library.find_book_by_title("Hello")
if found_book:
    print(found_book.get_author())  
else:
    print("Книга не найдена")
