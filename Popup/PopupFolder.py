import PySimpleGUI as sg

text = sg.popup_get_folder('Please enter a folder name')
sg.popup('Results', 'The value returned from popup_get_folder', text)