import PySimpleGUI as sg

layout = [[sg.InputText('Default text')]]

sg.Window('Input',layout).read()