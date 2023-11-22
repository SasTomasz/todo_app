user_todos = []


def show_todos():
    for todo in user_todos:
        print(str(user_todos.index(todo) + 1) + '.', todo)


while True:
    match input("Type add, edit, show or exit: ").strip():
        case 'add':
            user_todos.append(input("Enter a todo: "))
        case 'show':
            show_todos()
        case 'edit':
            print("There are Your todos: ")
            show_todos()
            todo_number = int(input("What todo number do You want to edit?: "))
            new_todo = input("Type new todo description: ")
            user_todos[todo_number - 1] = new_todo
            print("Todo was updated \nThis is Your new todos:")
            show_todos()
        case 'exit':
            break
        case _:
            print("Your command did not match, please try again")

print("Bye, bye!")
