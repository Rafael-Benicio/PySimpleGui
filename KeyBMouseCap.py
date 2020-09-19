import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

text_elem = sg.Text(size=(18, 1))

layout = [[sg.Text("Press a key or scroll mouse")],
          [text_elem],
          [sg.Button("OK")]]

window = sg.Window("Keyboard Test", layout,  return_keyboard_events=True, use_default_focus=False)

# ---===--- Loop taking in user input --- #
while True:
    event, value = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        print(event, "exiting")
        break
    text_elem.update(event)