# ToDo List OOP

A simple command-line ToDo List application developed with **Python** and **Object-Oriented Programming (OOP)**.

This project is a refactored version of a basic ToDo application. It uses classes, JSON for data persistence, environment variables for configuration, and `argparse` for command-line interaction.

---

## Features

- Add new tasks
- Display all tasks
- Delete tasks by ID
- Mark tasks as completed
- Automatically record task creation date and time
- Store tasks in a JSON file
- Load existing tasks when the application starts
- Save changes automatically
- Use `.env` for configuration
- Object-Oriented project structure
- Command-line interface using `argparse`

---

## Project Structure

```text
TODO_LIST_OOP/
│
├── data/
│   └── tasks.json
│
├── utils/
│   ├── __init__.py
│   ├── storage.py
│   ├── tasks.py
│   └── todolist.py
│
├── .env
├── .env.example
├── .gitignore
├── .venv/
├── main.py
├── project_structure.txt
├── QUICKSTART.md
├── README.md
└── Requirements.txt
```

---

## Architecture

The project is divided into separate components, with each component having a specific responsibility.

```text
                    main.py
                       │
                       ▼
                   TodoList
                  /        \
                 ▼          ▼
              Task       Storage
                            │
                            ▼
                       tasks.json
```

### `main.py`

The main entry point of the application.

It uses Python's `argparse` module to handle command-line commands:

- `list`
- `add`
- `delete`
- `done`

---

### `utils/tasks.py`

Contains the `Task` class.

The `Task` class represents a single task and stores:

- `id`
- `title`
- `created_at`
- `status`

It also provides:

- A string representation of a task
- A method for converting the task into a dictionary

---

### `utils/todolist.py`

Contains the `TodoList` class.

The class manages the collection of tasks and provides methods for:

- Displaying tasks
- Adding tasks
- Deleting tasks
- Updating task status
- Renumbering tasks after deletion

---

### `utils/storage.py`

Contains the `Storage` class.

This class is responsible for persistent data storage.

It:

- Loads tasks from the JSON file
- Saves tasks to the JSON file
- Reads the JSON file location from the `.env` configuration

---

### `data/tasks.json`

This file stores the application's task data in JSON format.

Example:

```json
[
    {
        "id": 1,
        "title": "Study Python",
        "created_at": "2026-09-24 12:30",
        "status": false
    },
    {
        "id": 2,
        "title": "Go to gym",
        "created_at": "2026-09-24 13:00",
        "status": true
    }
]
```

---

## Requirements

- Python 3.x
- `python-dotenv`

The project also uses `argparse`, `json`, `pathlib`, and `datetime`, which are part of the Python standard library.

Dependencies are listed in:

```text
Requirements.txt
```

---

## Installation

### 1. Clone the Repository

```powershell
git clone https://github.com/patriot1234/Todo_manager.git
```

### 2. Open the Project Directory

```powershell
cd Todo_manager
```

> Replace `Todo_manager` with the actual directory name if necessary.

### 3. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal should display something similar to:

```text
(.venv)
```

### 5. Install Dependencies

```powershell
pip install -r Requirements.txt
```

---

## Configuration

The application uses a `.env` file to configure the location of the JSON storage file.

Example:

```env
TASKS_FILE=data/tasks.json
```

The repository also contains `.env.example`, which can be used as a template for the local `.env` file.

The `.env` file should remain local and should not be committed to the repository.

---

## Usage

The application is controlled through command-line arguments.

### Show All Tasks

```powershell
python main.py list
```

Example output:

```text
1       Study Python    2026-09-24 12:30       False
2       Go to gym       2026-09-24 13:00       True
```

---

### Add a Task

To add a task, provide an ID and a title:

```powershell
python main.py add 1 "Study Python"
```

Additional task information can also be provided:

```powershell
python main.py add 1 "Study Python" --houre "14:30" --status False
```

After successfully adding a task:

```text
Task added successfully.
```

---

### Delete a Task

Delete a task using its ID:

```powershell
python main.py delete 1
```

After successful deletion:

```text
Task deleted successfully.
```

The remaining tasks are automatically renumbered.

---

### Mark a Task as Completed

Use the `done` command followed by the task ID:

```powershell
python main.py done 2
```

After successfully updating the task:

```text
Task updated successfully.
```

The task status becomes:

```text
True
```

---

## Task Model

Each task contains four main properties:

| Property | Description |
|---|---|
| `id` | Unique identifier of the task |
| `title` | Task title |
| `created_at` | Date and time when the task was created |
| `status` | Completion status of the task |

Example:

```python
Task(
    id=1,
    title="Study Python",
    created_at="2026-09-24 12:30",
    status=False
)
```

Before being saved to the JSON file, a task is converted into a dictionary:

```python
{
    "id": 1,
    "title": "Study Python",
    "created_at": "2026-09-24 12:30",
    "status": False
}
```

---

## Object-Oriented Design

The application separates different responsibilities into different classes.

| Component | Responsibility |
|---|---|
| `Task` | Represents a single task |
| `TodoList` | Manages the collection of tasks |
| `Storage` | Handles JSON file storage |
| `main.py` | Handles command-line arguments |

This separation makes the code easier to understand, maintain, and extend.

---

## Data Persistence

Tasks are stored permanently in:

```text
data/tasks.json
```

When the application starts, existing tasks are loaded from the JSON file.

When a task is:

- Added
- Deleted
- Updated

the changes are saved back to the JSON file.

The storage path is configurable through:

```env
TASKS_FILE=data/tasks.json
```

This means the storage location can be changed without modifying the Python source code.

---

## Environment and Generated Files

The following files and directories are local or generated files:

```text
.env
.venv/
__pycache__/
```

They should not be committed to the Git repository.

The `.env.example` file is included to show the required environment configuration without exposing the local `.env` file.

---

## Example Workflow

A typical workflow can be:

```powershell
# Display current tasks
python main.py list

# Add a new task
python main.py add 3 "Learn Python"

# Display tasks again
python main.py list

# Mark task as completed
python main.py done 3

# Delete a task
python main.py delete 3
```

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- `argparse`
- `json`
- `pathlib`
- `datetime`
- `python-dotenv`
- Git
- GitHub

---

## Learning Objectives

This project was developed to practice and demonstrate:

- Python classes and objects
- Object-Oriented Programming
- Separation of responsibilities
- Working with JSON files
- File handling
- Environment variables
- Command-line interfaces
- Virtual environments
- Project structure and organization
- Git and GitHub
- Refactoring an existing Python project

---

## Future Improvements

Possible future improvements include:

- Better input validation
- Improved error handling
- Task search and filtering
- Task priorities
- Task categories
- Due dates
- Advanced sorting
- Unit testing
- Improved command-line output

---

## Author

**Ali mazaheri**

A Python OOP learning project focused on building a structured and maintainable command-line Todo List application.