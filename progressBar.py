import PySimpleGUI as sg

# layout the window
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]

# create the window`
window = sg.Window('Custom Progress Meter', layout)
progress_bar = window['progressbar']
# loop that would normally do something useful
for i in range(1000):
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event == sg.WIN_CLOSED:
        break
  # update bar with loop value +1 so that bar eventually reaches the maximum
    progress_bar.UpdateBar(i + 1)
# done with loop... need to destroy the window as it's still open
window.close()