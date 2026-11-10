class Node:
    """Double node in a linked list"""

    def __init__(self, value):
        self.value = value  # The data this node holds
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"Node ({self.value})"

class LinkedList:
    """A doubly linked list"""

    def __init__(self):
        self.head = None  # List starts empty
        self.tail = None

    def insert_start(self, value):
        """Add a new node at the front of the list. O(1) time"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, value):
        """Add a new node at the end of the list. O(1)"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        """Prints the list in a readable format"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print("->".join(elements) + "-> None")

    def display_reverse(self):
        """Prints the list in reverse order in  a readable format"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev
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
        """Takes no value and removes the first node. Return True/False. O(1) time"""
        current = self.head
        if current is None:
            return False
        self.head = current.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
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

    # ===== Doubly Linked List Tests =====


print("--- insert_start ---")
dll = LinkedList()
dll.insert_start(3)
dll.insert_start(2)
dll.insert_start(1)
dll.display()  # 1->2->3-> None
dll.display_reverse()  # 3->2->1-> None

print("--- insert_end ---")
dll.insert_end(4)
dll.insert_end(5)
dll.display()  # 1->2->3->4->5-> None
dll.display_reverse()  # 5->4->3->2->1-> None

print("--- insert_end on empty list ---")
solo = LinkedList()
solo.insert_end(10)
solo.display()  # 10-> None
solo.display_reverse()  # 10-> None
print(solo.head is solo.tail)  # True (one node is both ends)

print("--- head and tail checks ---")
print(dll.head.value)  # 1
print(dll.tail.value)  # 5
print(dll.head.prev)  # None
print(dll.tail.next)  # None

print("--- delete (front) ---")
print(dll.delete())  # True
dll.display()  # 2->3->4->5-> None
dll.display_reverse()  # 5->4->3->2-> None
print(dll.head.prev)  # None  <- if this prints a Node, the new head's prev wasn't cleared

print("--- delete down to empty ---")
dll.delete()
dll.delete()
dll.delete()
print(dll.delete())  # True  (removes the last node)
print(dll.head)  # None
print(dll.tail)  # None  <- if this prints a Node, tail wasn't reset
print(dll.delete())  # False (already empty)
dll.display()  # -> None
dll.display_reverse()  # -> None
