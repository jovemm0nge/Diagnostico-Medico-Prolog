%% -> Fatos


%% -> Regras




%% -------

sintoma(febre).
sintoma(tosse).
sintoma(espirros).
sintoma(congestao_nasal).
sintoma(dor_de_cabeca).

condicao(gripe, [febre, tosse, dor_de_cabeca]).
condicao(resfriado, [espirros, congestao_nasal, dor_de_cabeca]).
condicao(alergia, [espirros, congestao_nasal]).