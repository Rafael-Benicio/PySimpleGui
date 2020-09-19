import PySimpleGUI as sg

sg.theme('Dark Blue')  # please make your creations colorful

layout = [  [sg.Text('Filename')],
            [sg.Input(), sg.FileBrowse()], 
            [sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()