import PySimpleGUI as sg

sg.theme('Dark Brown 1')

headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]

input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

layout = header + input_rows

window = sg.Window('Table Simulation', layout, font='Courier 12')
while True:
    event, values = window.read(timeout=1)
    if event ==sg.WIN_CLOSED:
        break

window.close()