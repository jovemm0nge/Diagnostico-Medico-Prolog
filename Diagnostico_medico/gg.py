from random import choice
import PySimpleGUI as sg

sg.theme("DarkBlue")
sg.set_options(font=('Courier New', 12))

data = [
    'Ronald Reagan', 'Abraham Lincoln', 'George Washington', 'Andrew Jackson',
    'Thomas Jefferson', 'Harry Truman', 'John F. Kennedy', 'George H. W. Bush',
    'George W. Bush', 'John Quincy Adams', 'Garrett Walker', 'Bill Clinton',
    'Jimmy Carter', 'John Adams', 'Theodore Roosevelt', 'Frank Underwood',
    'Woodrow Wilson',
]

layout = [
    [sg.Listbox(data, size=(max(map(len, data))+2, 10), key='LISTBOX')]
]

window = sg.Window('Title', layout, finalize=True)
listbox = window['LISTBOX']

while True:
    event, values = window.read(timeout=500)
    if event == sg.WIN_CLOSED:
        break
    if event == '__TIMEOUT__':
        index = choice(range(len(data)))
        listbox.update(set_to_index=[index], scroll_to_index=index)

window.close()