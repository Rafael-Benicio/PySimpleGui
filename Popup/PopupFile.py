import PySimpleGUI as sg
text = sg.popup_get_file('Please enter a file name')
sg.popup('Results', 'The value returned from popup_get_file', text)