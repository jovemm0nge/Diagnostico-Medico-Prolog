import PySimpleGUI as sg
from pyswip import Prolog

prolog = Prolog()
prolog.consult("diagnostico_medico.pl")

sintomas = []
sintomas_paciente = []
query = list(prolog.query("sintoma(X)"))

for sintoma in query:
    sintomas.append(sintoma["X"].replace("_", "_").capitalize())

sg.theme('DarkBlue3')  # Add a touch of color
# All the stuff inside your window.
layout = [
    # [sg.Image('PySimpleGUI_Logo.png', expand_x=True, expand_y=True, size=(10, 10))],
    [sg.Text('Dados Pessoais', font=180)],
    [sg.Text('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')],
    [sg.Text('Sexo'), sg.Radio('Masculino', 1, "Masc", key='-SEXM-'), sg.Radio('Feminino', 1,"Femi", key='-SEXF-')],
    [
        sg.Text('Data de Nascimento'),
        sg.InputText(key='-DATE-', size=(10, 1), disabled=True),
        sg.CalendarButton("📆", close_when_date_chosen=True, target="-DATE-", format='%d/%m/%Y', font=4)
    ],
    [sg.Text('')],
    [sg.Text('Histórico', font=180)],
    [sg.Text('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')],
    [sg.Text('Possui histórico de doenças cardiacas?'), sg.Radio('Sim', 2, "SimCardiaco", key="-SCARD-"), sg.Radio('Não', 2,"NaoCardicas", key="-NCARD-")],
    [sg.Text('Possui histórico de doenças respiratórias?'), sg.Radio('Sim', 3, "SimRespiratorias", key="-SRESP-"), sg.Radio('Não', 3,"NaoRespiratorias", key="-NRESP-")],
    [sg.Text('Possui histórico de doenças renais?'), sg.Radio('Sim', 4, "SimRenais", key="-SRENAL-"), sg.Radio('Não', 4,"NaoRenais", key="-NRENAL-")],
    [sg.Text('')],

    [sg.Text('Sintomas', font=180)],
    [sg.Text('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')],
    [
        [sg.Listbox(values=[], size=(40, 10), key='-SINTOMAS_PACIENTE-'),

         sg.Button('<'),
         sg.Button('>'),

         sg.Listbox(values=sintomas, size=(40, 10), key='-SINTOMAS_LISTA-')
         ]
    ],
    [sg.Text('')],
    [sg.Button('Enviar', font=180, size=(200))]
]

# Create the Window
window = sg.Window('Diagnostico Médico', layout, size=(650, 620))

# Event Loop to process "events" and get the "values" of the inputs
selecao_sintoma = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    DATA = values['-DATE-']
    print(DATA)

    if DATA == '':
        print('False')
    elif DATA != '':
        print('True')

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Enviar':
        if DATA == '':
            sg.popup('Preencha o campo DATA antes de enviar.', title='Aviso')
        else:
            # selecao_sintomas = selecao_sintoma

            if not selecao_sintoma:
                sg.popup('Selecione pelo menos um sintoma antes de enviar.', title='Aviso')
            else:
                array_de_strings_lower = [string.lower() for string in sintomas_paciente]
                query = list(prolog.query("condicao(D, S), subset(" + str(array_de_strings_lower) + ", S)."))
                if not query:
                    sg.popup('Base não encontrou nenhum diagnóstico, procure um hospital', title='Aviso')
                else:
                    a = []
                    for soln in query:
                        a.append(soln["D"])

                    condicoes_formatadas = [condicao.replace('_', '_').title() for condicao in a]
                    texto = '\n'.join(condicoes_formatadas)
                    print(texto)
                    sg.popup('Analisando os dados, foi possível chegar no diagnóstico: ' + texto,
                             title="Resultado do Diagnóstico")

    elif event == '<':
        selecao_sintomas = values['-SINTOMAS_LISTA-']
        if selecao_sintomas:
            for sintoma in selecao_sintomas:
                if sintoma not in sintomas_paciente:
                    sintomas_paciente.append(sintoma)
                    selecao_sintoma.append(sintoma)

            window['-SINTOMAS_PACIENTE-'].update(values=sintomas_paciente)

    # elif event == '>':
    #     selecao_sintomas = values['-SINTOMAS_PACIENTE-']
    #     if selecao_sintomas:
    #         sintomas_paciente.pop(sintomas_paciente.index(selecao_sintomas[0]))
    #
    #         window['-SINTOMAS_PACIENTE-'].update(values=sintomas_paciente)

    elif event == '>':
        selecao_sintomas = values['-SINTOMAS_PACIENTE-']
        if selecao_sintomas:
            selecao_sintoma.pop(sintomas_paciente.index(selecao_sintomas[0]))
            sintomas_paciente.pop(sintomas_paciente.index(selecao_sintomas[0]))

            window['-SINTOMAS_PACIENTE-'].update(values=sintomas_paciente)

while True:
    event, values = window.Read()
    if not event:
        break
    if event == 8:
        print(values.Sintomas)

window.close()