%% -> Fatos

sintoma(gripe, febre).
sintoma(gripe, tosse).
sintoma(gripe, dor_de_garganta).
sintoma(resfriado, tosse).
sintoma(resfriado, nariz_entupido).

doenca(D, S) :- sintoma(D, S).