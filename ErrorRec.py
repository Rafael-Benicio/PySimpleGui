import PySimpleGUI as sg

def main():
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)

    layout = [  [sg.Text('My Window')],
                [sg.Input(k='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window['-O U T'].update(values['-IN-'])
    window.close()

def func():

    main()

func()