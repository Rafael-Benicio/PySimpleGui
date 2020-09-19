import PySimpleGUI as sg

layout = [[sg.Text('Click em exit para fechar a janela')],
          [sg.Submit(), sg.Button('Exit')]]

window = sg.Window('Exit', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event, values)

window.close()
