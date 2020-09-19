import PySimpleGUI as sg

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window 1', layout)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED:
        break
    win1.FindElement('-OUTPUT-').update(vals1[0])

    if ev1 == 'Launch 2'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                win2.close()
                win2_active = False
                win1.UnHide()
                break