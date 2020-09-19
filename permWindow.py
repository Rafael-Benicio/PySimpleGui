import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Persistent window')],
          [sg.Input()],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event, values)

window.close()