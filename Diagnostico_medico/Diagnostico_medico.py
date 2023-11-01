from pyswip import Prolog
prolog = Prolog()
prolog.consult("diagnostico_medico2.pl")

# Defina os sintomas inseridos pelo paciente
sintomas_do_paciente = ["febre", "tosse"]

# Crie uma consulta Prolog com variáveis
consulta = "doenca(D, S), member(S, ["
consulta += ", ".join(f"'{s}'" for s in sintomas_do_paciente)
consulta += "])."

# Execute a consulta
condicoes_possiveis = list(prolog.query(consulta))

# Imprima os resultados
if condicoes_possiveis:
    print("Condições médicas possíveis:")
    for soln in condicoes_possiveis:
        print(soln["D"])
else:
    print("Não foi possível fazer um diagnóstico com os sintomas fornecidos.")


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
