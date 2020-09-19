import PySimpleGUI as sg

layout = [[sg.Image(r'/home/rafael/Documentos/Programa/Python/PySimpleGui/Img/heroes.png')],]


window=sg.Window('Img', layout)
while True:
    event, values = window.read()
    if event==sg.WINDOW_CLOSED:
        break

window.close()