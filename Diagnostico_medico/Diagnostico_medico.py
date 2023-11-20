from pyswip import Prolog
prolog = Prolog()
prolog.consult("diagnostico_medico.pl")

# Defina os sintomas inseridos pelo paciente
sintomas_do_paciente = ["febre", "dor_de_cabeca"]

# Crie uma consulta Prolog com variáveis
consulta = "condicao(D, S), subset(" + str(sintomas_do_paciente) + ", S)."

# Execute a consulta
condicoes_possiveis = list(prolog.query(consulta))
a = []
# Imprima os resultados
if condicoes_possiveis:
    print("Diagnósticos médicos possíveis:")
    for soln in condicoes_possiveis:
        a.append(soln["D"])
else:
    print("Não foi possível fazer um diagnóstico com os sintomas fornecidos.")

print(a)


# print(list(prolog.query("sintoma(gripe, X)")) == [{'X': 'febre'}, {'X': 'tosse'}, {'X': 'dor_de_garganta'}])
#
# # for soln in prolog.query("sintoma(X,Y)"):
# #     print(soln["X"], "é sintoma de", soln["Y"])
#
# sintomas = []
#
# for soln in prolog.query("sintoma(gripe,X)"):
#     print(soln["X"], "é sintoma de gripe")
#     sintomas.append(soln["X"])
#
# print(sintomas)
