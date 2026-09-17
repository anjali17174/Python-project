from idlelib import tooltip

import functions
import FreeSimpleGUI as sg

lable = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "enter a to-do")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[lable],[input_box, add_button]])
window.read()
window.close()