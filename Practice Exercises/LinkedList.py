from collections import deque

# Linked List
# Part 1: Extend the Linked List

class Node:
    """Single node in a linked list"""

    def __init__(self, value):
        self.value = value  # The data this node holds
        self.next = None  # Reference to the next node(none = end of chain)
        self.prev = None

    def __repr__(self):
        return f"Node ({self.value})"


class LinkedList:
    """A single linked list"""

    def __init__(self):
        self.head = None  # List starts empty

    def insert_start(self, value):
        """Add a new node at the front of the list. O(1) time"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        """Add a new node at the end of the list. O(n)"""
        new_node = Node(value)
        if self.head is None:  # if the list is empty, new node is the head.
            self.head = new_node
            return
        current = self.head
        while current.next:  # Walk to the last node
            current = current.next
        current.next = new_node  # Last node now points to the new node.

    def display(self):
        """Prints the list in a readable format"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print("->".join(elements) + "-> None")

    def search(self, target):
        """Find a value in the list. Return True/False. O(n) time"""
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
        return False

    def delete(self):
        """Remove the first node with a given value. Return True/False. O(n) time"""
        current = self.head
        if current is None:
            return False
        self.head = current.next
        return True

    def length(self):
        """Return the number of nodes in the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        py_list = []
        current = self.head
        while current:
            py_list.append(current.value)
            current = current.next
        return py_list


my_list = LinkedList()
print("-------Test--------")
my_list.insert_start(3)
my_list.insert_start(2)
my_list.insert_start(1)
my_list.insert_end(4)


my_list.display()
print("------Search------")
print(my_list.search(3))
print(my_list.search(9))
print("------Delete-------")
my_list.display()
print(my_list.delete())  # Comment out from print Delete to print Test to test empty linked list
my_list.display()
print("-------Length------")
print(my_list.length())
my_list.insert_end(4)
my_list.insert_end(5)
my_list.display()
print(my_list.length())
print("---------List---------")
print(my_list.to_list())

#Part 2: Stack Bracket Validator
def is_balanced(text):
    """Return True if all brackets in text are properly matched. Handles: (), [], {} """
    brackets = ["(",")","{", "}", "[", "]"]
    only_brackets = ""
    for char in text:
        if char in brackets:
            only_brackets += char
    while "()" in only_brackets or "[]" in only_brackets or "{}" in only_brackets:
        only_brackets = only_brackets.replace("()", "")
        only_brackets = only_brackets.replace("[]", "")
        only_brackets = only_brackets.replace("{}", "")
    if only_brackets == "":
        return True
    else:
        return False

# Tests:
print(is_balanced("()"))           # True
print(is_balanced("({[]})"))       # True
print(is_balanced("(]"))           # False
print(is_balanced("([)]"))         # False
print(is_balanced("hello (world)")) # True

#Part 3 Queue Task Processor
class TaskProcessor:
    def __init__(self):
        self.queue = deque()

    def add_task(self, name):
        self.queue.append(name)

    def process_next(self):
        if len(self.queue) > 0:
            return self.queue.popleft()

# ----- Tests -----
processor = TaskProcessor()

print("--- Adding tasks ---")
processor.add_task("Check oil")
processor.add_task("Refuel unit 12")
processor.add_task("Load bank test")

print("--- Processing ---")
print(processor.process_next())   # Check oil        (first in, first out)
print(processor.process_next())   # Refuel unit 12
print(processor.process_next())   # Load bank test
print(processor.process_next())   # None             (queue is empty)

print("--- Mixed adds and processing ---")
processor.add_task("Inspect wiring")
processor.add_task("Replace filter")
print(processor.process_next())   # Inspect wiring
processor.add_task("Update logs")
print(processor.process_next())   # Replace filter   (still older than Update logs)
print(processor.process_next())   # Update logs
print(processor.process_next())   # None



