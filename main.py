user_todos = []

while True:
    match input("Type add, show or exit: "):
        case 'add':
            user_todos.append(input("Enter a todo: "))
        case 'show':
            print(user_todos)
        case 'exit':
            break
        case _ :
            print("Your command did not match, please try again")

print("Bye, bye!")
