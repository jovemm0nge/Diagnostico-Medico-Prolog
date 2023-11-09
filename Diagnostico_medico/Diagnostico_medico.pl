%% -> Fatos


%% -> Regras

sintoma(febricula, febre).
sintoma(tosse_seca, tosse).
sintoma(dor_leve_cabeca, dor_de_cabeca).
sintoma(dor_garganta, dor_de_garganta).

condicao(resfriado, [febre, tosse]).
condicao(gripe, [febre, tosse, dor_de_garganta]).
condicao(ruim, [tosse, dor_de_garganta]).

