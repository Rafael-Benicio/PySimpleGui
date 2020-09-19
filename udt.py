import PySimpleGUI as sg

layout = [ [sg.Text('My layout', key='-TEXT-')],
           [sg.Button('Read')]]

window = sg.Window('My new window', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window['-TEXT-'].update('My new text value')