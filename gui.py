import PySimpleGUI as sg

text_field_desc = sg.Text("Add some todo")
text_field = sg.InputText()
add_button = sg.Button("Add")

window = sg.Window("My todo app", [[text_field_desc, text_field, add_button]])
window.read()
window.close()
