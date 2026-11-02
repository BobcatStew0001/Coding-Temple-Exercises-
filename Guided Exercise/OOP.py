class Task:
    """Represents a single task with a title, priority and a complete status"""

    # Class Variable-Shared across all instances
    VALID_PRIORITIES = ["low", "medium", "high"]

    # CONSTRUCTOR: A special method (__init__) that Python runs automatically
    # every time a new object is created, e.g. Task("Learn OOP").
    # Its job is to set up the object's starting state by creating its attributes.
    # "self" refers to the specific object being built.
    def __init__(self, title, priority="medium"):
        # ATTRIBUTES: Variables that belong to one object (instance), written as self.name.
        # They store the object's data/state, and each Task object gets its own copy.
        self.title = title  # Attribute: the task's name
        self.completed = False  # Attribute: whether the task is done (starts False)
        if priority.lower() not in self.VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of {self.VALID_PRIORITIES}")
        self.priority = priority.lower()  # Attribute: "low", "medium", or "high"

    # METHODS: Functions defined inside a class that describe what an object can DO.
    # They always take "self" first so they can read or change that object's attributes.
    # Called with dot notation, e.g. task1.complete()
    def complete(self):
        # Method: changes this task's "completed" attribute to True
        self.completed = True

    # Special (dunder) method: Python calls __repr__ automatically when the object
    # is printed, and uses the returned string as the object's text representation.
    def __repr__(self):
        status = "✔️" if self.completed else "⭕"
        return f"{status} {self.title} ({self.priority})"


# Quick Test
task1 = Task("Learn OOP", "high")
task2 = Task("Review stretch Challenge", "low")
print(task1)
print(task2)

# Added test: mark a task complete and check that the status icon changes
task1.complete()
print(task1)

# Added test: an invalid priority should raise ValueError
# try:
#     Task("Bad task", "urgent")
# except ValueError as error:
#     print(f"Caught error: {error}")
# from asyncio import Task


class TaskManager:
    """Manages a collection of tasks"""

    def __init__(self):
        self.tasks = []  # Internal list of task objects

    def add_task(self, title, priority="medium"):
        """Create and add a new task. Returns a task"""
        task = Task(title, priority)
        self.tasks.append(task)
        return task

    def complete_task(self, title):
        """Mark a task as completed by title. Return True if found"""
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                return True
        return False

    def get_pending(self):
        """Return a list of all pending tasks"""
        return [tasks for tasks in self.tasks if not tasks.completed]

    def get_by_priority(self, priority):
        """Return a list of all pending tasks with priority"""
        return [task for task in self.tasks if task.priority == priority]

    def summary(self):
        """Return a summary of the tasks"""
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.completed)
        print(f"Tasks Summary: {done}/{total} completed")
        for task in self.tasks:
            print({task})


# ---------------- Tests for TaskManager ----------------
def check(name, test_function):
    """Run one test and print PASS/FAIL so one failure doesn't stop the rest"""
    try:
        test_function()
        print(f"PASS: {name}")
    except AssertionError as error:
        print(f"FAIL: {name} -> {error}")
    except Exception as error:
        print(f"CRASH: {name} -> {type(error).__name__}: {error}")


def build_manager():
    """Make a fresh manager with three tasks for each test"""
    manager = TaskManager()
    manager.add_task("Learn OOP", "high")
    manager.add_task("Review stretch Challenge", "low")
    manager.add_task("Practice loops")  # default priority "medium"
    return manager


def test_add_task():
    manager = build_manager()
    assert len(manager.tasks) == 3, f"expected 3 tasks, got {len(manager.tasks)}"


def test_complete_first_task():
    manager = build_manager()
    result = manager.complete_task("Learn OOP")
    assert result is True, f"expected True, got {result}"
    assert manager.tasks[0].completed is True, "first task was not marked completed"


def test_complete_last_task():
    # The task we want is NOT the first one in the list
    manager = build_manager()
    result = manager.complete_task("Practice loops")
    assert result is True, f"expected True, got {result}"
    assert manager.tasks[2].completed is True, "last task was not marked completed"


def test_complete_missing_task():
    manager = build_manager()
    result = manager.complete_task("Does not exist")
    assert result is False, f"expected False, got {result}"


def test_get_pending():
    manager = build_manager()
    manager.complete_task("Learn OOP")
    pending = manager.get_pending()
    titles = [task.title for task in pending]
    assert titles == ["Review stretch Challenge", "Practice loops"], f"got {titles}"


def test_get_by_priority():
    manager = build_manager()
    high = manager.get_by_priority("high")
    titles = [task.title for task in high]
    assert titles == ["Learn OOP"], f"got {titles}"


check("add_task adds tasks", test_add_task)
check("complete_task finds the first task", test_complete_first_task)
check("complete_task finds a later task", test_complete_last_task)
check("complete_task returns False when missing", test_complete_missing_task)
check("get_pending returns only unfinished tasks", test_get_pending)
check("get_by_priority filters by priority", test_get_by_priority)
