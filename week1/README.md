# Week 1 - Python Fundamentals

This week focuses on basic Python syntax, data structures, modules, file handling, and a small command-line project.

## Project: Student Management CLI

The CLI lets a user manage student records from the terminal. Records are stored as JSON so the data survives between runs.

## Features

- Add a student with name, age, and department
- List all students
- Search for a student by name
- Remove a student by name
- Update an existing student record
- Save and load records from `data/students.json`

## Files

```text
week1/
├── main.py              # Terminal menu and input handling
├── models.py            # Student dictionary creation
├── storage.py           # JSON loading and saving
├── student_manager.py   # Add/list/search/remove/update logic
├── notes.txt            # Learning notes
└── data/                # Local week-specific data folder
```

## Run It

From the repository root:

```bash
python week1/main.py
```

## Concepts Practiced

- Functions
- Imports between local modules
- Lists and dictionaries
- JSON file persistence
- Basic validation with loops and exceptions
- Separating responsibilities across files

## Next Improvements

- Add automated tests
- Wrap the menu loop in a `main()` function
- Normalize formatting with a standard formatter
- Improve type hints and return values
- Move all runtime data into one consistent data folder
