import PySimpleGUI as sg

layout  =[ [sg.Menu(
        [   ['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'],],
            ['&Help', '&About...'],
        ])],
            [sg.Multiline(size=(40,10))]]


sg.Window('menu',layout).read()
