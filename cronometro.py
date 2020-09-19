import PySimpleGUI as sg
import time

# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.Text('')],
         [sg.Text(size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.Button('Pause', key='button', button_color=('white', '#001480')),
          sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    event, values = window.read(timeout=10)
    current_time = int(round(time.time() * 100)) - start_time
    # --------- Display timer in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))