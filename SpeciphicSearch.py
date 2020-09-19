import PySimpleGUI as sg

layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]

sg.Window('chose',layout).read()