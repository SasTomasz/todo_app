import streamlit as st
import todo_processing
from logger import logger

checkboxes = []


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    todo_processing.save_todos(todos)
    st.session_state.new_todo = ""


def complete_todo():
    key_list = [x for i, x in enumerate(st.session_state)
                if x.startswith("checkbox_")]

    for key in key_list:
        if st.session_state[key]:
            todo_index = int(key.strip("checkbox_"))
            todos.pop(todo_index)
            todo_processing.save_todos(todos)


todos = todo_processing.get_todos_from_file()

st.title("My todo app")

for idx, todo in enumerate(todos):
    checkboxes.append(st.checkbox(todo, key=f"checkbox_{idx}",
                                  on_change=complete_todo))

st.text_input(label='New todo', placeholder="Type a new todo", key="new_todo",
              on_change=add_todo)


