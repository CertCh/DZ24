class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author

book = Book("1984", "My D")
print(book.get_title())  
print(book.get_author())  
