exit_str = ""
user_todos = []

while "exit" not in user_todos:
    user_todos.append(input("Add new task: "))

user_todos.pop()
print(user_todos)
