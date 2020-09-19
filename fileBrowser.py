import PySimpleGUI as sg

layout= [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]

event, values = sg.Window("Search file's way",layout).read(close=True)
