import PySimpleGUI as sg


def count_words(text):
    text = text.strip()
    if not text:
        return 0
    words = text.split()
    return len (words)

layout = [
[sg.Text('Írj be egy szöveget:')],
[sg.Multiline(size=(50, 5), key='-Text-' ) ] ,
[sg.Button('Szavak megszámolása'), sg.Exit('Bezárás')]
]

window = sg.Window('Szavak számolója' , layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Bezárás':
        break
    elif event == 'Szavak megszámolása':
        text_input = values['-Text-']
        word_count = count_words(text_input)
        sg.popup(f'A szavak mennyisége: {word_count}')

window.close()