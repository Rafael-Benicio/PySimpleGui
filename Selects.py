import PySimpleGUI as sg

layout = [[sg.Combo(['choice 1', 'choice 2','oi'], key='-COM-')]]
layout += [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]
layout += [[sg.Slider(range=(1,100),
         default_value=50,
         size=(20,15),
         orientation='horizontal',
         font=('Helvetica', 12))]]
layout +=  [[sg.Radio('My first Radio!', "RADIO1", default=True), sg.Radio('My second radio!', "RADIO1")]]
layout +=  [[sg.Checkbox('My first Checkbox!', default=True), sg.Checkbox('My second Checkbox!')]]
layout +=  [[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('Volume level')]]


window=sg.Window('Combo', layout)

while True:
    window.read()
    if event == sg.WINDOW_CLOSED:
        break
    
    print(event, values)

window.close()
    

