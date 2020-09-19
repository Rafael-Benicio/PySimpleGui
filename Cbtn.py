import PySimpleGUI as sg

def CBtn(button_text):
    return sg.Button(button_text, button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))

layout= [[CBtn('OI rafael')]]

sg.Window('Cbtn',layout).read()

