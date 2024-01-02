import os

import constants
import todo_processing
from logger import logger

user_todos = todo_processing.get_todos_from_file()
logger.info(f"Current directory is: {os.getcwd()}")

while True:
    user_input = input("Type add, edit, complete, show or exit: ")
    if user_input.startswith('add'):
        if user_input[4:] == '':
            user_input += f' {input("Please type some task description: ")}'
        user_todos.append(user_input[4:] + '\n')
        print(f"TODO: {user_input[4:]} was added")
        todo_processing.save_todos(user_todos)

    elif user_input.startswith('show'):
        todo_processing.show_todos(user_todos)

    elif user_input.startswith('edit'):
        if user_todos:
            try:
                todo_number = int(user_input[5:])
            except ValueError:
                todo_number = int(input(
                    "Please type the correct number of todo You want to edit: "))
            todo_number = todo_processing.is_todo_number_correct(todo_number,
                                                                 user_todos)
            todo_processing.edit_todo(todo_number, user_todos)
        else:
            print(constants.NO_TODOS)

    elif user_input.startswith('complete'):
        if user_todos:
            try:
                todo_number = int(user_input[9:])
            except ValueError:
                todo_number = int(input(
                    "Please type the correct number of todo You want to complete: "))
            todo_number = todo_processing.is_todo_number_correct(todo_number,
                                                                 user_todos)
            todo_processing.complete_todo(todo_number, user_todos)
        else:
            print(constants.NO_TODOS)

    elif user_input.startswith('exit'):
        break

    else:
        print("Your command did not match, please try again")

print("Bye, bye!")
