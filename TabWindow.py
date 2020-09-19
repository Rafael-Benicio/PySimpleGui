import PySimpleGUI as sg

tab1_layout =  [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

layout = [[
            sg.TabGroup([[
                    sg.Tab('Tab 1', tab1_layout),
                    sg.Tab('Tab 2', tab2_layout)
                ]])],
            [sg.Button('Read')]]

sg.Window('Tab',layout).read()