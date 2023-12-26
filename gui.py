import PySimpleGUI as sg

import helper_functions
from logger import logger

text_field_desc = sg.Text("Add some todo")
text_field = sg.InputText(key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
todos = helper_functions.get_todos_from_file()
list_box = sg.Listbox(todos,
                      enable_events=True,
                      key="todos_list",
                      size=(60, 20))

window = sg.Window("My todo app",
                   layout=[[text_field_desc, text_field, add_button],
                           [list_box, edit_button]])
while True:
    event, value = window.read()
    logger.info(f"Event was occurred:\nevent: {event}\nvalue: {value['todo']}")
    if event == 'Add':
        todos.append(value['todo'])
        helper_functions.save_todos(todos)
    elif event == sg.WIN_CLOSED:
        break

window.close()

# TODO
#  * Implement edit button
