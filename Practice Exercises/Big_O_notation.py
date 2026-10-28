import time
import random
#List of books for testing
famous_books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"title": "Pride and Prejudice", "author": "Jane Austen"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
]
# Function A
def get_first(data):
    return data[0]
#This is Constant Time O(1), Because it is accessing the data by the index.

# Function B
def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count
#This is Linear Time O(n), It will scale with the size of the input.
# If you were looking for a title of a book in a stack of books it would look at every
# title to find the one you are looking for in the stack. Double the input double the work

# Function C
def all_pairs(data):
    pairs = []
    for i in range(len(data)):
        for j in range(len(data)):
            pairs.append((data[i], data[j]))
    return pairs
#This is Quadratic Time O(n2) This is similar but different to Linear time.
# It looks at each piece of data in but it also compares it to every other item.
# So if you were looking for a title of a book it
# look would compare the title you are looking for to every
# other title in the stack of books. Double the input, Quadruple the work.

# Function D
def mystery(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
#This uses Logarithmic O(log n).
# This is complicated with the stack of books.
# If you have a stack of 100 books in alphabetical order
# it would start in the middle of the stack. If you are looking for
# To Kill a Mockingbird and the middle of the stack
# landed on Robinson Crusoe. R is before
# T so it would discard the everything up to the R
# and then start over with the second cut and so on and so on. This is how binary works.

# Function E
def process(data):
    total = sum(data)           # Line 1
    sorted_data = sorted(data)  # Line 2
    first = data[0]             # Line 3
    return total, sorted_data, first
#This is Linearithmic, Time O(n log n), it is n * log n and is the O(n) and O(log n) combined.
#This function has 3 steps and the slowest is sorted, sorted being the slowest is the one
#that sets the speed for the function.

def books(book_list, title):
    for book in book_list:
        if book["title"] == title:
            return book["author"]
    return "Title not found"

def same_author_pairs(book_list):
    pairs = []
    for i in range(len(book_list)):
        for j in range(i + 1, len(book_list)):
            book = book_list[i]
            other_book = book_list[j]
            if book["author"] == other_book["author"]:
                pairs.append((book["title"], other_book["title"]))
    return pairs

#Testing the function to make sure it runs correctly
print(books(famous_books, "1984"))
print(books(famous_books, "The Great Gatsby"))
print(books(famous_books, "To Kill a Mockingbird"))
print(books(famous_books, "The Hobbit"))
print(books(famous_books, "Star Wars"))

# Test with one shared author added
test_books = famous_books + [
    {"title": "The Silmarillion", "author": "J.R.R. Tolkien"}
]
print(same_author_pairs(test_books))
print(same_author_pairs(famous_books))

def make_books(size): #To change the sizes for testing
    book_list = []
    for i in range(size):
        book_list.append({"title": f"Book {i}", "author": f"Author {i}"})
    return book_list


def benchmark(func, *args): #To perform O(n) testing.
    start = time.perf_counter()
    func(*args)
    end = time.perf_counter()
    return end - start


sizes = [1000, 5000, 10000, 20000]

for size in sizes:
    data = make_books(size)

    # Worst case: title isn't in the list, so every book gets checked
    t1 = benchmark(books, data, "Missing Title")
    t2 = benchmark(books, data, "Missing Title")
    t3 = benchmark(books, data, "Missing Title")
    average = (t1 + t2 + t3) / 3

    print(f"n={size:>6}   Books: {average:.6f}s")

    t1 = benchmark(same_author_pairs, data)
    t2 = benchmark(same_author_pairs, data)
    t3 = benchmark(same_author_pairs, data)
    average = (t1 + t2 + t3) / 3

    print(f"n={size:>6}   Pairs: {average:.6f}s")
