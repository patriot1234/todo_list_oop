from utils.tasks import Task
from utils.storage import Storage


class TodoList:
    """Manage a collection of tasks and their statuses."""

    def __init__(self):
        """Initialize the todo list and load existing tasks."""
        storage = Storage()
        self.tasks = storage.load()

    def show_tasks(self):
        """Display all tasks in the todo list."""
        for item in self.tasks:
            task = Task(item["id"], item["title"], item["created_at"], item["status"])
            print(task)

    def sort_tasks(self):
        """Sort tasks by time and renumber them."""
        for index, item in enumerate(self.tasks, start=1):
            item["id"] = index

    def add_tasks(self, object):
        """Add a new task to the todo list and save it."""
        storage = Storage()
        self.tasks.append(object.task_dict())
        storage.save(self.tasks)

    def delete_task(self, id_task):
        """Delete a task from the todo list using its ID."""
        storage = Storage()
        for item in self.tasks:
            if item["id"] == id_task:
                self.tasks.remove(item)
                break

        self.sort_tasks()
        storage.save(self.tasks)

    def task_status_update(self, status, task_number):
        """Update the completion status of a task using its ID."""
        storage = Storage()
        for item in self.tasks:
            if item["id"] == task_number:
                item["status"] = True
        storage.save(self.tasks)
