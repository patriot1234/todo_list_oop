from datetime import datetime


class Task:
    """Represent a single task in the Todo list."""

    def __init__(self, id: int, title: str, created_at: str = None, status=False):
        """Initialize a task with its ID, title, creation time, and status."""
        self.id = id
        self.title = title
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d  %H:%M")
        self.status = status

    def __str__(self):
        """Return a formatted string representation of the task."""
        return f"{self.id:<8}{self.title:<15}{self.created_at:<25}{self.status}\n"

    def task_dict(self):
        """Return the task data as a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "status": self.status,
        }
