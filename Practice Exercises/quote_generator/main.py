import random

QUOTES = [
    ("The journey of a thousand miles begins with one step.", "Lao Tzu"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Well done is better than well said.", "Benjamin Franklin"),
    ("Energy and persistence conquer all things.", "Benjamin Franklin"),
    ("Knowing yourself is the beginning of all wisdom.", "Aristotle"),
    ("Luck is what happens when preparation meets opportunity.", "Seneca"),
    ("Go confidently in the direction of your dreams.", "Henry David Thoreau"),
    ("Write it on your heart that every day is the best day in the year.", "Ralph Waldo Emerson"),
    ("The only true wisdom is in knowing you know nothing.", "Socrates"),
    ("Nothing is impossible to a willing heart.", "John Heywood"),
    ("Fall seven times, stand up eight.", "Japanese Proverb"),
]


def get_random_quote():
    return random.choice(QUOTES)


def main():
    quote, author = get_random_quote()
    print(f'"{quote}" — {author}')


if __name__ == "__main__":
    main()
