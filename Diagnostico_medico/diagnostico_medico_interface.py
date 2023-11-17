import PySimpleGUI as sg
from pyswip import Prolog

prolog = Prolog()
prolog.consult("diagnostico_medico.pl")

sintomas = []
query = list(prolog.query("sintoma(X)"))

for sintoma in query:
    sintomas.append(sintoma["X"].replace("_", " ").capitalize())

# # Defina os sintomas inseridos pelo paciente
# sintomas_do_paciente = ["febre", "tosse"]
#
# # Crie uma consulta Prolog com variáveis
# consulta = "doenca(D, S), member(S, ["
# consulta += ", ".join(f"'{s}'" for s in sintomas_do_paciente)
# consulta += "])."
#
# # Execute a consulta
# condicoes_possiveis = list(prolog.query(consulta))
# # Imprima os resultados
# if condicoes_possiveis:
#     print("Condições médicas possíveis:")
#     for soln in condicoes_possiveis:
#         a = soln["D"]
# else:
#     print("Não foi possível fazer um diagnóstico com os sintomas fornecidos.")

sg.theme('DarkBlue3')  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Dados Pessoais')],
    [sg.Text('Sexo'), sg.Radio('Masculino', "Masc", default=True), sg.Radio('Feminino', "Femi")],
    [
        sg.Text('Data de Nascimento'),
        sg.InputText(key='Date', size=(10, 1)),
        sg.CalendarButton("Selecionar", close_when_date_chosen=True, target="Date", format='%d:%m:%Y', size=(10, 1))
    ],
    [sg.Text('Histórico')],
    [sg.CBox('Possui histórico de doenças cardiacas?')],
    [sg.CBox('Possui histórico de doenças respiratórias?')],
    [sg.CBox('Possui histórico de doenças renais?')],
    [[sg.Combo(['choice 1', 'choice 2'])]],
    [sg.Text('Sintomas')],
    [[sg.Listbox(values=[], size=(30, 6))],
     [sg.VerticalSeparator(pad=20)],
     [sg.Listbox(values=sintomas, size=(30, 6))]],

    [sg.Button('Enviar')],
]

# Create the Window
window = sg.Window('Diagnostico Médico', layout, size=(650, 650))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    if event == 'Ok': sg.popup('Analisando os dados, foi possível chegar no diagnóstico: ',
                               title=("Resultado do Diagnostico"))
    print('Enviado', values[0])
    break

window.close()



