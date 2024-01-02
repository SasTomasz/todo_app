import os

from logger import logger
from constants import NO_TODOS


def show_todos(user_todos: list[str]):
    """
    Show user todos listed in separate lines. If user don't have any todos
    print information about it
    :param user_todos: list of user todos
    :return: True if user has todos or False otherwise
    :rtype: bool
    """
    if user_todos:
        print("There are Your todos: ")
        for i, todo in enumerate(user_todos):
            print(f"{i + 1}. {todo}", end='')
        return True
    else:
        print(NO_TODOS)
        return False


def is_todo_number_correct(number: int, user_todos: list[str]):
    """
    Check is there a task with particular number and if a number is positive.
    If not program ask user to type correct number.
    :param list[str] user_todos: list of user todos
    :param int number: A task id
    :return: Correct task number
    :rtype: int
    """
    while number > len(user_todos) or number <= 0:
        number = int(input("Please type correct number: "))
    return number


def get_todos_from_file(path='./data/todos.txt'):
    try:
        with open(path, "r") as file:
            todos = file.readlines()
    except FileNotFoundError:
        current_directory = os.getcwd()
        new_directory_name = "data"
        path = os.path.join(current_directory, new_directory_name)
        try:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory {new_directory_name} created successfully")
            with open(path, "w") as file:
                file.close()
        except OSError as error:
            logger.info(f"Directory {new_directory_name} can not be created")
            logger.error(error.strerror)
        return []
    return todos


def save_todos(todos, path='./data/todos.txt'):
    with open(path, "w") as file:
        file.writelines(todos)


def edit_todo(task_number: int, user_todos: list[str]):
    """
    Edit existing todo. Func finishes with new version of the task list save on
    the machine
    :param task_number: todo user want to edit
    :param user_todos: list of all user todos
    """
    print(f"Todo number {task_number}: {user_todos[task_number - 1]}", end='')
    want_modify = input(f"Are you sure you want to edit? y/n: ")
    if want_modify == 'y':
        new_todo = input("Type new todo description: ") + '\n'
        user_todos[task_number - 1] = new_todo
        save_todos(user_todos)
        print("Todo was updated")
    elif want_modify == 'n':
        print("Todo was not updated")
    else:
        print("Wrong value, try again")


def complete_todo(task_number: int, user_todos: list[str]):
    """
    Remove existing todo from list. Func finishes with new version of the task
    list save on the machine
    :param task_number: number of todo user want to edit
    :param user_todos: list of all user todos
    """
    print(f"Todo number {task_number}: {user_todos[task_number - 1]}", end='')
    want_modify = input(f"Are you sure you want to complete? y/n: ")
    if want_modify == 'y':
        user_todos.pop(task_number - 1).strip('\n')
        save_todos(user_todos)
        print("Todo was updated")
    elif want_modify == 'n':
        print("Todo was not updated")
    else:
        print("Wrong value, try again")
