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
