import logging
import os

logging.basicConfig(filename="../logs.log",
                    format='%(asctime)s %(message)s',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# logger.addHandler(logging.StreamHandler(sys.stdout))


def show_todos():
    if user_todos:
        print("There are Your todos: ")
        for i, todo in enumerate(user_todos):
            print(f"{i + 1}. {todo}", end='')
        return True
    else:
        print("You don't have any todos.")
        return False


def is_todo_number_correct(number):
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
            logger.info("Directory '%s' created successfully" % new_directory_name)
            with open(path, "w") as file:
                file.close()
        except OSError as error:
            logger.info("Directory '%s' can not be created" % new_directory_name)
            logger.error(error.strerror)
        return []
    return todos


def save_todos(todos, path='./data/todos.txt'):
    with open(path, "w") as file:
        file.writelines(todos)


user_todos = get_todos_from_file()
logger.info(f"Current directory is: {os.getcwd()}")


def operating_on_todo(task_number, operation_type='edit'):
    print(f"Todo number {task_number}: {user_todos[task_number - 1]}", end='')
    want_modify = input(f"Are you sure you want to {operation_type}? y/n: ")
    if want_modify == 'y':
        if operation_type == 'edit':
            new_todo = input("Type new todo description: ") + '\n'
            user_todos[task_number - 1] = new_todo
            save_todos(user_todos)
        elif operation_type == 'complete':
            user_todos.pop(task_number - 1).strip('\n')
            save_todos(user_todos)
        print("Todo was updated")
    elif want_modify == 'n':
        print("Todo was not updated")
    else:
        print("Wrong value, try again")


while True:
    user_input = input("Type add, edit, complete, show or exit: ")
    if 'add' in user_input:
        user_todos.append(user_input[4:] + '\n')
        print(f"TODO: {user_input[4:]} was added")
        save_todos(user_todos)

    elif 'show' in user_input:
        show_todos()

    elif 'edit' in user_input:
        if user_todos:
            try:
                todo_number = int(user_input[5:])
            except ValueError:
                todo_number = int(input("Please type the correct number of todo You want to edit: "))
            todo_number = is_todo_number_correct(todo_number)
            operating_on_todo(todo_number)

    elif 'complete' in user_input:
        if user_todos:
            try:
                todo_number = int(user_input[9:])
            except ValueError:
                todo_number = int(input("Please type the correct number of todo You want to complete:"))
            todo_number = is_todo_number_correct(todo_number)
            operating_on_todo(todo_number, operation_type='complete')

    elif 'exit' in user_input:
        break

    else:
        print("Your command did not match, please try again")

print("Bye, bye!")

# fixme:
#  2. User can add empty task if type for example "add "
