import PySimpleGUI as sg
from pyswip import Prolog

prolog = Prolog()
prolog.consult("diagnostico_medico.pl")

sintomas = ["ABC", "BDF", "SDC"]
selecionados = []

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
    [sg.Text('--------------------------------------------------------------------------------------')],
    [sg.Text('Sexo'), sg.Radio('Masculino', 1, "Masc", key='-SEXM-'), sg.Radio('Feminino', 1,"Femi", key='-SEXF-')],
    [
        sg.Text('Data de Nascimento'),
        sg.InputText(key='Date', size=(10, 1)),
        sg.CalendarButton("Selecionar", close_when_date_chosen=True, target="Date", format='%d/%m/%Y', size=(10, 1))
    ],
    [sg.Text('')],
    [sg.Text('Histórico')],
    [sg.Text('--------------------------------------------------------------------------------------')],
    [sg.Text('Possui histórico de doenças cardiacas?'), sg.Radio('Sim', 2, "SimCardiaco", key="-SCARD-"), sg.Radio('Não', 2,"NaoCardicas", key="-NCARD-")],
    [sg.Text('Possui histórico de doenças respiratórias?'), sg.Radio('Sim', 3, "SimRespiratorias", key="-SRESP-"), sg.Radio('Não', 3,"NaoRespiratorias", key="-NRESP-")],
    [sg.Text('Possui histórico de doenças renais?'), sg.Radio('Sim', 4, "SimRenais", key="-SRENAL-"), sg.Radio('Não', 4,"NaoRenais", key="-NRENAL-")],
    [sg.Text('')],
    [sg.Text('Sintomas')],
    [sg.Text('--------------------------------------------------------------------------------------')],
    [[sg.Listbox(values=[], size=(30, 6))],
    [sg.Listbox(values=sintomas, size=(30, 6))]],
    [sg.Text('--------------------------------------------------------------------------------------')],
    [sg.Text('')],
    [sg.Button('Enviar')],
    [sg.Listbox(values=sintomas,
                enable_events=True,
                auto_size_text=True,
                size=(10, 10),
                key="Sintomas")],
    ]

# Create the Window
window = sg.Window('Diagnostico Médico', layout, size=(650, 800))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    # if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    if event == 'Ok': sg.popup('Analisando os dados, foi possível chegar no diagnóstico: ',
                               title=("Resultado do Diagnostico")
                               )
    print('Enviado', values[0])
    print(values)
    break

while True:
    event, values = window.Read()
    if not event:
        break
    if event == 8:

        print(values.Sintomas)


window.close()



