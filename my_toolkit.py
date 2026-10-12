import numbers


# Create a file called my_toolkit.py containing the following functions. Each function must include a docstring explaining what it does.

#Function 1: Calculate_average(numbers) — Takes a list of numbers, returns the average. Returns 0 if the list is empty.

#Function 2: Find_max_and_min(numbers) — Takes a list of numbers, returns a tuple (max_value, min_value).
    #Do NOT use the built-in max() and min() — implement the logic yourself with a loop.

#Function 3: Count_occurrences(items, target) — Takes a list and a target value, returns how many times the target appears in the list.
    #Do NOT use the built-in .count() method.

#Function 4: Is_palindrome(text) — Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces).
    #Examples: "racecar" → True, "hello" → False, "A man a plan a canal Panama" → True.

#Function 5: Create_report(title, scores) — Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally.
    #Returns a formatted string report (NOT a print — a return).

#I did my own testing after each function before moving on to the next one, and included the required test at the end

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Function 1:

def calculate_average(numbers):
    """Returns the average of all numbers in a list, Returns 0 on an empty list"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print("--Test Function 1--")
print(calculate_average(number_list))
print(calculate_average([]))
print(calculate_average([0, 5, 10]))



#Function 2:
def find_max_and_min(numbers):
    """Returns the maximum and minimum values in a list in the form of a tuple. Returns 0 on an empty list"""
    if len(numbers) == 0:
        return 0, 0
    max_value =numbers[0]
    min_value =numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    return(max_value, min_value)

print("--Test Function 2--")
print(find_max_and_min(number_list))
print(find_max_and_min([-5, -2, -9]))
print(find_max_and_min([7]))
print(find_max_and_min([]))

#Function 3

def count_occurrences(items, target):
    """Counts the occurrences of target in a list. Returns 0 on an empty list"""
    if len(items) == 0:
        return 0
    occurrences = 0
    for item in items:
        if item == target:
            occurrences += 1

    return occurrences

print("--Test Function 3--")
print(count_occurrences([1, 2, 2, 3, 2], 2))
print(count_occurrences(["a", "b", "a"], "a"))
print(count_occurrences([1, 2, 3], 5))
print(count_occurrences([], 1))

# Function 4

def is_palindrome(text):
    """Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces)"""
    text = text.lower().replace(' ', '')
    reversed_text = text[::-1].lower()
    if text == reversed_text:
        return True
    return False

print("--Test Function 4--")
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Racecar"))

#Function 5

def create_report(title, scores):
    """Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally.
    Returns the report as a formatted string."""
    total_avg = calculate_average(scores)
    overall_max, overall_min = find_max_and_min(scores)
    return (f'=== {title} ===\n'
            f'Average: {total_avg:.2f}\n'
            f'Highest: {overall_max}\n'
            f'Lowest: {overall_min}')

print("--Test Function 5--")
print(create_report("Midterm Scores", [88, 95, 72, 81, 85]))
print(create_report("Empty Class", []))

print("--Required Testing--")
test_scores = [85, 92, 78, 95, 88, 70, 93]
if __name__ == '__main__':
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))
