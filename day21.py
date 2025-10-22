

class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.books = []

    def write_book(self, title, year):
        book = Book(title, year, self)
        self.books.append(book)
        return book

    def bibliography(self):
        if not self.books:
            return f"{self.name} has not written any books yet"
        return [book.title for book in self.books]

    def __str__(self):
        return f"{self.name} (born {self.birth_year})"




class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_info(self):
        return f"{self.title} in {self.year} by {self.author.name}"

    def __str__(self):
        return f"'{self.title}' {self.year} by {self.author.name}"

author1 = Author("jiggy", 2007)
book1 = author1.write_book("jiggy bio", 2009)
book2 = author1.write_book("why i love derin", 2025)

print(book1.get_info())
print(author1.bibliography())
print(book2)
print(author1)



