import PySimpleGUI as sg

import helper_functions
from logger import logger

text_field_desc = sg.Text("Add some todo")
text_field = sg.InputText(key="todo")
add_button = sg.Button("Add")

window = sg.Window("My todo app",
                   [[text_field_desc, text_field, add_button]])
while True:
    event, value = window.read()
    logger.info(f"Event was occurred:\nevent: {event}\nvalue: {value['todo']}")
    if event == 'Add':
        todos = helper_functions.get_todos_from_file()
        todos.append(value['todo'])
        helper_functions.save_todos(todos)
    elif event == sg.WIN_CLOSED:
        break

window.close()
