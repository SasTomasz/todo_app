import streamlit as st
import todo_processing

todos = todo_processing.get_todos_from_file()

st.title("My todo app")

for todo in todos:
    st.checkbox(todo)

new_todo = st.text_input(label="New todo", placeholder="Type a new todo")
todos.append(new_todo + '\n')
todo_processing.save_todos(todos)
print(new_todo)
# TODO
#   * Fix problem with saving new todo. It show on list after the next one is enter


