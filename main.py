user_todos = []

while True:
    match input("Type add, show or exit: ").strip():
        case 'add':
            user_todos.append(input("Enter a todo: "))
        case 'show':
            for todo in user_todos:
                print('*', todo)
        case 'exit':
            break
        case _:
            print("Your command did not match, please try again")

print("Bye, bye!")
