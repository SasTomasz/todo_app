user_todos = []


def show_todos():
    if user_todos:
        print("There are Your todos: ")
        for i, todo in enumerate(user_todos):
            print(f"{i + 1}. {todo}")
        return True
    else:
        print("You don't have any todos.")
        return False


def is_todo_number_correct(number):
    while number > len(user_todos) or number == 0:
        number = int(input("Please type correct number: "))
    return number


while True:
    match input("Type add, edit, complete, show or exit: ").strip():
        case 'add':
            user_todos.append(input("Enter a todo: "))
        case 'show':
            show_todos()
        case 'edit':
            show_todos()
            if user_todos:
                todo_number = int(input("What todo number do You want to edit?: "))
                todo_number = is_todo_number_correct(todo_number)
                new_todo = input("Type new todo description: ")
                user_todos[todo_number - 1] = new_todo
                print("Todo was updated")
                show_todos()
        case 'complete':
            show_todos()
            if user_todos:
                todo_number = int(input("What todo number do You want to complete?: "))
                todo_number = is_todo_number_correct(todo_number)
                print(f"TASK {user_todos.pop(todo_number - 1)}, was completed")
                show_todos()
        case 'exit':
            break
        case _:
            print("Your command did not match, please try again")

print("Bye, bye!")
