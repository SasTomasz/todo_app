import PySimpleGUI as sg

import helper_functions
from logger import logger

text_field_desc = sg.Text("Add some todo")
text_field = sg.InputText(key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
todos = helper_functions.get_todos_from_file()
list_box = sg.Listbox(todos,
                      enable_events=True,
                      key="todos_list",
                      size=(58, 10))
exit_button = sg.Button("Exit")
info_field = sg.Text(key='info')

window = sg.Window("My todo app",
                   layout=[[text_field_desc, text_field, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, info_field]])
while True:
    event, value = window.read()
    logger.info(f"Event was occurred:\nevent: {event}\nvalue: {value}")
    if event == 'Add':
        if value['todo']:
            todos.append(value['todo'] + '\n')
            helper_functions.save_todos(todos)
            window['todos_list'].update(todos)
            window['info'].update('')
        else:
            window['info'].update("Please write some todo's name")
    elif event == 'Edit':
        todo_index = todos.index(value['todos_list'][0])
        todos[todo_index] = value['todo'] + '\n'
        helper_functions.save_todos(todos)
        window['todos_list'].update(todos)
    elif event == 'todos_list':
        window['todo'].update(value['todos_list'][0])
    elif event == 'Complete':
        completed_todo = value['todos_list'][0]
        todos.remove(completed_todo)
        helper_functions.save_todos(todos)
        window['todo'].update(value='')
        window['todos_list'].update(todos)
    elif event == 'Exit':
        break
    elif event == sg.WIN_CLOSED:
        break

window.close()

# TODO
#  Fix this errors:
#  * User can tap Complete button when nothing is selected what produce an IndexError
#  * User can tap Edit button when nothing is selected what produce an IndexError

