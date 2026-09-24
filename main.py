import argparse

from utils.storage import Storage
from utils.tasks import Task
from utils.todolist import TodoList

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(dest="command", required=True)


# List command
list_parser = subparser.add_parser("list")


# Add command
add_parser = subparser.add_parser("add")
add_parser.add_argument("id", type=int)
add_parser.add_argument("title", type=str)
add_parser.add_argument("--houre", type=str)
add_parser.add_argument("--status", type=bool)


# Delete command
delete_parser = subparser.add_parser("delete")
delete_parser.add_argument("task", type=int)


# Done command
done_parser = subparser.add_parser("done")
done_parser.add_argument("task_id", type=int)


args = parser.parse_args()

todo = TodoList()


if args.command == "list":
    todo.show_tasks()

elif args.command == "add":
    task = Task(args.id, args.title, args.houre, args.status)
    todo.add_tasks(task)
    print("Task added successfully.")

elif args.command == "delete":
    todo.delete_task(args.task)
    print("Task deleted successfully.")

elif args.command == "done":
    todo.task_status_update(True, args.task_id)
    print("Task updated successfully.")
