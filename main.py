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

while True:
    match input("Type add, edit, complete, show or exit: ").strip():
        case 'add':
            user_todos.append(input("Enter a todo: ") + '\n')
            save_todos(user_todos)
        case 'show':
            show_todos()
        case 'edit':
            show_todos()
            if user_todos:
                todo_number = int(input("What todo number do You want to edit?: "))
                todo_number = is_todo_number_correct(todo_number)
                new_todo = input("Type new todo description: ") + '\n'
                user_todos[todo_number - 1] = new_todo
                save_todos(user_todos)
                print("Todo was updated")
                show_todos()
        case 'complete':
            show_todos()
            if user_todos:
                todo_number = int(input("What todo number do You want to complete?: "))
                todo_number = is_todo_number_correct(todo_number)
                completed_todo = user_todos.pop(todo_number - 1).strip('\n')
                save_todos(user_todos)
                print(f"TASK {completed_todo}, was completed")
                show_todos()
        case 'exit':
            break
        case _:
            print("Your command did not match, please try again")

print("Bye, bye!")
