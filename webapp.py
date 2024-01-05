import streamlit as st
import todo_processing
from logger import logger


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    todo_processing.save_todos(todos)


todos = todo_processing.get_todos_from_file()

st.title("My todo app")

for todo in todos:
    logger.info(f"In {__name__}: checkbox number: {todos.index(todo)}")
    st.checkbox(todo, key=todos.index(todo))

st.text_input(label='', placeholder="Type a new todo", key="new_todo",
              on_change=add_todo())
