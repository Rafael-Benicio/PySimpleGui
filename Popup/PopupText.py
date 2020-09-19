import PySimpleGUI as sg
text = sg.popup_get_text('Title', 'Please input something')
sg.popup('Results', 'The value returned from PopupGetText', text)