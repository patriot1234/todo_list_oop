from utils.tasks import Task
from utils.storage import Storage

class TodoList:
    """Manage a collection of tasks and their statuses."""
    def __init__(self):
        """Initialize the todo list and load existing tasks."""
        storage = Storage()
        self.tasks=storage.load()


    def show_tasks(self):
         """Display all tasks in the todo list."""
         for item in self.tasks:
            print(item)



    def add_tasks(self , object):
        """Add a new task to the todo list and save it."""
        storage = Storage()

        self.tasks.append(object.task_dict())
        storage.save(self.tasks)



    def delete_task(self, id_task):
        """Delete a task from the todo list using its ID."""
        storage = Storage()
        for item in self.tasks:
            if item["id"]==id_task:
                self.tasks.remove(item)
                break
        storage.save(self.tasks)

    def task_status(self, task_number , status):
        """Update the completion status of a task using its ID."""
        storage = Storage()
        for item in self.tasks:
            if item["id"] == task_number:
                item["status"] = status
        storage.save(self.tasks)


        

