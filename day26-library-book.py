# library book


from datetime import datetime, timedelta

from plyer.platforms.win.libs.wifi_defs import available


class Book:
    def __init__(self, title, author, isbn, category=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.available = True
        self.due_date = None

    def check_out(self):
        if self.available:
            self.available = False
            self.due_date = datetime.now() + timedelta(days=14)
            print(f" '{self.title}' checked out. Due date on {self.due_date.date()}.")
        else:
            print(f" '{self.title}' is currently not available")

    def return_book(self):
        if not self.available:
            self.available = True
            self.due_date = None
            print(f" '{self.title}' has been returned.")
        else:
            print(f" '{self.title}' was not checked out.")

    def display_info(self):
        status = "Available" if self.available else f"Checked out (Due: {self.due_date.date()})"
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} |"
              f" Category: {self.category or 'N/A'} | Status: {status}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)
        print(f" '{book.title}' added to {self.name} Library.")

    def remove_book(self, isbn):
        """Remove a book by ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f" '{book.title}' removed from library.")
                return
        print("Book not found.")

    def search_by_title(self, title):
        """Find books by title."""
        results = [b for b in self.books if title.lower() in b.title.lower()]
        return results

    def search_by_author(self, author):
        """Find books by author."""
        results = [b for b in self.books if author.lower() in b.author.lower()]
        return results

    def display_available_books(self):
        """Show all available books."""
        print(f" Available Books in {self.name} Library:")
        available = [b for b in self.books if b.available]
        if not available:
            print("NO books currently available.")
        for book in available:
            book.display_info()

    def display_checked_out_books(self):
        """Show all checked out books."""
        print(f" Checked Out Books in {self.name} Library:")
        checked_out = [b for b in self.books if not b.available]
        if not checked_out:
            print("No books currently checked out.")
        for book in checked_out:
            book.display_info()


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.check_out()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"You don't have '{book.title}' borrowed.")

    def view_borrowed_books(self):
        print(f"\n Books borrowed by {self.name}:")
        if not self.borrowed_books:
            print("None")
        for b in self.borrowed_books:
            b.display_info()

# Example Usage

library = Library("Central City")

book1 = Book("Python Basics", "Derin Ola", "001", "Programming")
book2 = Book("How to stay jiggy", "Jiggy Brain", "002", "Programming")
book3 = Book("Cookbook", "Chef Borah", "003", "Programming")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_available_books()

member1 = Member("Alice", "M001")
member1.borrow_book(book1)
member1.borrow_book(book3)

library.display_checked_out_books()

member1.view_borrowed_books()

member1.return_book(book1)
library.display_available_books()
