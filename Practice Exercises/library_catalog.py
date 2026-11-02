class Book:
    """Manages a collection of Books"""
    def __init__(self, title, author, year, checked_out = False):
        self.title = title
        self.author = author
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be positive")
        self.year = year
        self.checked_out = checked_out

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