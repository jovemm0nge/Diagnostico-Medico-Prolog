from pyswip import Prolog
prolog = Prolog()
prolog.consult("diagnostico_medico3.pl")

sintomas = list(prolog.query("sintoma(X)"))
print(sintomas)

a = []
# Imprima os resultados
if sintomas:
    print("Condições médicas possíveis:")
    for soln in sintomas:
        a.append(soln["X"])
else:
    print("Não foi possível fazer um diagnóstico com os sintomas fornecidos.")

print(a)