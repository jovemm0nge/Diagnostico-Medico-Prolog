import PySimpleGUI as sg

sg.theme('DarkBlue3')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text('Histórico')],
            [sg.CBox('Possui histórico de doenças cardiacas?')],
            [sg.CBox('Possui histórico de doenças respiratórias?')],
            [sg.CBox('Possui histórico de doenças renais?')],
            [[sg.Combo(['choice 1', 'choice 2'])]],
            [sg.Text('Sintomas')],
            [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))], [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]],
            [sg.Button('Ok'), sg.Button('Cancel')],
         ]



# Create the Window
window = sg.Window('Diagnostico Médico', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Enviado', values[0])

window.close()