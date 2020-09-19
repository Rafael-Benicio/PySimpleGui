import PySimpleGUI as sg

layout=[[sg.SystemTray.notify('Notification Title', 'This is the notification message')]]

sg.Window('Not',layout).read()