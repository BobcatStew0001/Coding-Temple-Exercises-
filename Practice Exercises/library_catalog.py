class Book:
    """Manages a collection of Books"""
    def __init__(self, title, author, year, checked_out = False, pages = 0):
        self.title = title
        self.author = author
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be positive")
        self.year = year
        self.checked_out = checked_out
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Pages must be positive")
        self.pages = pages

    def check_out(self):
        """Checks books out of the collection"""
        if self.checked_out == False:
            self.checked_out = True
            return(f"Here is {self.title}, I hope you enjoy")

        else:
            return (f"Sorry, {self.title} is currently checked out")

    def return_book(self):
        """Returns the book to the collection"""
        if self.checked_out == True:
            self.checked_out = False
            return(f"Thank you for returning {self.title}, I hope you enjoyed it.")
        else:
            return (f"Sorry, {self.title} is currently not checked out")

    def __repr__(self):
        """Prints the book to the console"""
        title = self.title
        author = self.author
        if(self.checked_out == True):
            status = "Unavailable"
        else:
            status = "Available"
        return(f"{title}\n{author}\n{status}")

    def __eq__(self, other):
        """Compares two books by title and author"""
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False


    def __lt__(self, other):
        """Checks to see if one title comes before the other title"""
        if self.title.lower() < other.title.lower():
            return True
        else:
            return False

    def __len__(self):
        """Checks length of books by pages"""
        return(self.pages)

    def __contains__(self, item):
        """Looks for words inside the title"""
        return item.lower() in self.title.lower()


class EBook(Book):
    """Manages a collection of EBooks"""
    def __init__(self, title, author, year, file_size_mb = 0):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        self.counter = 0


    def check_out(self):
        """Checks ebooks out of the collection"""
        self.counter += 1
        return(f"There are currently {self.counter} copies of {self.title} checked out")

    def return_book(self):
        """Returns the ebooks to the collection"""
        if self.counter > 0:
            self.counter -= 1
            return (f"There are currently {self.counter} copies of {self.title} checked out")
        else:
            return(f"There are currently no copies of {self.title} checked out")

    def __repr__(self):
        base = super().__repr__()
        file_size = self.file_size_mb
        return(f"{base}\n{file_size} MB")

class Catalog:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the catalog"""
        self.books.append(book)
        return(f"{book.title} added to catalog")

    def search_by_author(self, author):
        """Searches for books by the author"""
        book_by_author = []
        for book in self.books:
            if book.author == author:
                book_by_author.append(book)
        if(len(book_by_author) > 0):
            return(book_by_author)
        else:
            return("Sorry, no book found with that author")

    def search_by_title(self, title):
        """Searches for books by the title"""
        book_by_title = []
        for book in self.books:
            if title.lower() in book.title.lower():
                book_by_title.append(book)
        if(len(book_by_title) > 0):
            return(book_by_title)
        else:
            return("Sorry, no book found with that title")

    def get_available(self):
        """Gets available books"""
        book_available = []
        for book in self.books:
            if book.checked_out == False:
                book_available.append(book)
        return(book_available)

    def summary(self):
        """Prints summary of the catalog"""
        total = len(self.books)
        available = len(self.get_available())
        if available > 0:
            print(f"{total} book(s) and {available} are available")
        else:
            print(f"{total} book(s) and none are available")

print("********* TESTING CODE *********")
catalog = Catalog()
catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()

print("********* TESTING CODE *********")
print("__________________________________")
print("        STRETCH CHALLENGE")

book_one = Book("AI Engineering", "Chip Huyen", 2025, pages=652)
book_two = Book("Clean Code", "Robert Martin", 2008, pages=464)
book_three = Book("Python Crash Course", "Eric Matthes", 2019, pages=544)

# Same title and author as book_one, to test __eq__
book_copy = Book("AI Engineering", "Chip Huyen", 2025)

# Deliberately OUT of alphabetical order so sorted() has work to do
books = [book_three, book_one, book_two]

# __lt__ via sorted()
print("Original order:", books)
print("Sorted order:  ", sorted(books))

print(book_one == book_copy)  # True: same title and author
print(book_one == book_two)  # False: different books

# __len__
print(len(book_one))  # 652

# __contains__
print("engineering" in book_one)  # True: lowercase still matches "Engineering"
print("Python" in book_one)  # False: not in "AI Engineering"