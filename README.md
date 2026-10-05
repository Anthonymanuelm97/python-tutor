# Python Tutor

A conversational Python learning application built to practice object-oriented programming, modular project structure, input validation, error handling, Git workflows, and AI-assisted development.

The application acts as a simple Python tutor that can explain programming concepts, quiz the student, track progress, remember conversation history, and handle invalid numeric input without crashing.

## Features

- Conversational command-line interface
- Python concept explanations
- Topic-based quizzes
- Text and numeric answer validation
- Progress tracking
- Conversation history
- Error handling with `try/except`
- Modular project structure
- Direct module self-testing
- Git-based development history

## Topics

The tutor currently supports the following topics:

- Variables
- Lists
- Dictionaries
- Functions
- Classes
- Git

Each topic contains:

- a short explanation
- a quiz question
- a correct answer
- an answer type

## Quiz System

The tutor supports both text and numeric answers.

Text answers are normalized before comparison by ignoring capitalization and unnecessary spaces.

Numeric answers are converted to integers before comparison.

Example:

```text
You: quiz list
What is the index of the first item in a Python list? 0
Python Tutor: Correct!
```

If the user enters text when a number is required, the program handles the error without crashing:

```text
You: quiz list
What is the index of the first item in a Python list? zero
Python Tutor: Please enter a number.
```

Invalid numeric input is not stored as an attempted topic.

## Progress Tracking

Quiz results are stored by topic.

Example:

```text
You: quiz git
What does Git track over time? changes to files
Python Tutor: Correct!

You: progress
Python Tutor: You answered 1 out of 1 attempted topics correctly.
```

If the same topic is attempted again, its previous result is updated instead of creating a duplicate entry.

## Conversation History

Every student message and tutor response is stored during the session.

When the user exits the program, the complete conversation history is displayed.

Example:

```text
--- Conversation History ---
student: hello
tutor: Hello! What would you like to learn about Python?
student: explain class
tutor: A class is a blueprint for creating objects.
student: exit
tutor: Goodbye! Happy learning.
```

## Project Structure

```text
python-tutor/
│
├── tutor.py
├── conversation.py
├── main.py
├── pyproject.toml
├── .python-version
├── .gitignore
└── README.md
```

### `tutor.py`

Contains the `PythonTutor` class and the main application logic:

- topic data
- concept explanations
- quizzes
- progress tracking
- conversation history
- input error handling

It also contains a small self-test that runs only when `tutor.py` is executed directly.

### `conversation.py`

Contains the conversation loop that handles user interaction with the tutor.

### `main.py`

Acts as the main entry point of the application.

It creates a `PythonTutor` instance and starts the conversation.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Anthonymanuelm97/python-tutor.git
```

Move into the project directory:

```bash
cd python-tutor
```

Synchronize the project environment:

```bash
uv sync
```

Run the full application:

```bash
uv run main.py
```

Run the `PythonTutor` self-test:

```bash
uv run tutor.py
```

The self-test should display:

```text
Running tutor.py directly - self-test:
Hello! What would you like to learn about Python?
```

## Example Session

```text
Welcome to the Python Tutor! Type 'exit' to end the conversation.

You: hello
Python Tutor: Hello! What would you like to learn about Python?

You: explain class
Python Tutor: A class is a blueprint for creating objects.

You: quiz list
What is the index of the first item in a Python list? 0
Python Tutor: Correct!

You: quiz list
What is the index of the first item in a Python list? zero
Python Tutor: Please enter a number.

You: quiz git
What does Git track over time? push
Python Tutor: Incorrect. The correct answer was: changes to files.

You: progress
Python Tutor: You answered 1 out of 2 attempted topics correctly.

You: exit
Python Tutor: Goodbye! Happy learning.
```

## Error Handling

Numeric quiz answers are protected using `try/except ValueError`.

If a value cannot be converted to an integer, the application returns:

```text
Please enter a number.
```

instead of terminating the program.

The invalid attempt is also not stored in the student's progress.

## Validation

The completed application was tested end-to-end with:

- greetings and goodbye messages
- concept explanations
- correct text answers
- incorrect text answers
- correct numeric answers
- invalid numeric input
- progress tracking
- conversation history
- module separation
- direct execution of `tutor.py`
- full execution through `main.py`

The final acceptance test confirmed that an invalid numeric answer does not crash the application or incorrectly affect progress tracking.

## What I Practiced

This project was built as part of my AI Builder learning path.

The project focused on both Python development and working effectively with an AI coding assistant.

I practiced:

- designing a program before writing code
- creating Python classes and methods
- using instance attributes with `self`
- working with dictionaries and lists
- maintaining application state
- validating text and numeric input
- handling exceptions with `try/except`
- debugging a real `ValueError`
- separating responsibilities into modules
- using `__name__ == "__main__"`
- writing and refining prompts for an AI coding assistant
- reviewing AI-generated code instead of accepting it automatically
- testing features before committing them
- using Git commits to document project evolution

## Development Approach

The application was built incrementally.

Each major feature was implemented and tested separately before being committed to Git:

1. Initial project setup
2. Tutor design
3. Base class and conversation history
4. Concept explanations
5. Quiz functionality
6. Progress tracking
7. Conversation loop
8. Numeric input error handling
9. Project modularization
10. Final acceptance testing

This creates a Git history that documents how the project evolved from an initial design into a complete working application.

## Technologies

- Python
- uv
- Git
- GitHub
- Visual Studio Code
- GitHub Copilot

## Project Status

Completed as a learning and portfolio project.