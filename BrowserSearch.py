import PySimpleGUI as sg

layout=[
    [sg.CalendarButton('Calendrio')],
    [sg.ColorChooserButton('Cor Escolhe')],
    [sg.InputText(),sg.FileBrowse()],
    [sg.InputText(),sg.FilesBrowse()],
    [sg.InputText(),sg.FileSaveAs()],
    [sg.InputText(),sg.FolderBrowse()]
]

sg.Window('Choose', layout).read()