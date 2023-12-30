import PySimpleGUI as sg

import helper_functions
import time
from logger import logger

clock = sg.Text('', key='clock')
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

window = sg.Window("My todo app", font='Helvetica 20',
                   layout=[[clock],
                           [text_field_desc, text_field, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]])
while True:
    event, value = window.read(timeout=200)
    window['clock'].update(time.strftime('%A, %m-%d-%Y %H:%M:%S'))
    logger.info(f"Event was occurred:\nevent: {event}\nvalue: {value}")
    if event == 'Add':
        if value['todo']:
            todos.append(value['todo'] + '\n')
            helper_functions.save_todos(todos)
            window['todos_list'].update(todos)
            window['info'].update('')
        else:
            sg.Popup("Please write some todo's name", font='Helvetica 20')
    elif event == 'Edit':
        try:
            todo_index = todos.index(value['todos_list'][0])
            todos[todo_index] = value['todo'] + '\n'
            helper_functions.save_todos(todos)
            window['todos_list'].update(todos)
        except IndexError:
            sg.Popup("Please select some todo", font='Helvetica 20')

    elif event == 'todos_list':
        window['todo'].update(value['todos_list'][0])
    elif event == 'Complete':
        try:
            completed_todo = value['todos_list'][0]
            todos.remove(completed_todo)
            helper_functions.save_todos(todos)
            window['todo'].update(value='')
            window['todos_list'].update(todos)
        except IndexError:
            sg.Popup("Please select some todo", font='Helvetica 20')
    elif event == 'Exit':
        break
    elif event == sg.WIN_CLOSED:
        break

window.close()

# TODO
#  * Fix stop clock when popup shows
