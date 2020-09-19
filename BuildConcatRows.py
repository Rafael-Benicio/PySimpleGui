import PySimpleGUI as sg

layout = []
for i in range(1,6):
    layout += [sg.Text(f'{i}. '), sg.In(key=i)],
layout += [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
print(f'{event}')