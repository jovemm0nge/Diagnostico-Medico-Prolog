sintoma(sintoma, febricula).
sintoma(sintoma, tosse).
sintoma(sintoma, dor_de_cabeca).
sintoma(sintoma, fraqueza).

tem_sintoma(Paciente, Sintoma) :- sintoma(Sintoma).

    sintoma(Paciente, febricula).
    sintoma(Paciente, tosse).
    sintoma(Paciente, dor_de_cabeca).
    sintoma(Paciente,  ).

    sintoma(colera, diarreia).
    sintoma(colera, febre).
    sintoma(colera, intestino_sensivel).
    sintoma(colera, fraqueza).

doenca_provavel(Paciente, pnenomonia) :- 
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, dor_de_cabeca),
    tem_sintoma(Paciente, dor_no_corpo),
    tem_sintoma(Paciente, tosse),
    tem_sintoma(Paciente, falta_de_ar),
    tem_sintoma(Paciente, dor_no_peito).

doenca_provavel(Paciente, anemia) :- 
    tem_sintoma(Paciente, fraqueza),
    tem_sintoma(Paciente, indisposicao),
    tem_sintoma(Paciente, falta_de_ar),
    tem_sintoma(Paciente, palpitacao).

doenca_provavel(Paciente, infeccao_urinaria) :- 
    tem_sintoma(Paciente, vontade_urinar_frequente),
    tem_sintoma(Paciente, queimacao_ao_urinar),
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente,  ).

doenca_provavel(Paciente, pressao_alta) :- 
    tem_sintoma(Paciente, dor_na_nuca),
    tem_sintoma(Paciente, dor_de_cabeca),
    tem_sintoma(Paciente, tonturas),
    tem_sintoma(Paciente, zumbido_ouvido),
    tem_sintoma(Paciente, visao_embacada),
    tem_sintoma(Paciente, palpitacoes).

doenca_provavel(Paciente, pressao_baixa) :- 
    tem_sintoma(Paciente, tontura),
    tem_sintoma(Paciente, taquicardia),
    tem_sintoma(Paciente, nauseas),
    tem_sintoma(Paciente, fadiga),
    tem_sintoma(Paciente, sonolencia),
    tem_sintoma(Paciente, desmaio).

doenca_provavel(Paciente, diabetes) :- 
    tem_sintoma(Paciente, fome_frequente),
    tem_sintoma(Paciente, sede_constante),
    tem_sintoma(Paciente, fadiga,
    tem_sintoma(Paciente,  ),
    tem_sintoma(Paciente,  ),
    tem_sintoma(Paciente, vontade_urinar_frequente),
    tem_sintoma(Paciente, perda_de_peso).

doenca_provavel(Paciente, apendicite) :- 
    tem_sintoma(Paciente, diarreia),
    tem_sintoma(Paciente, perda_apetite),
    tem_sintoma(Paciente, colica_severa,
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, barriga_inchada),
    tem_sintoma(Paciente,  ).


doenca_provavel(Paciente, dengue) :- 
    tem_sintoma(Paciente, febre_alta),
    tem_sintoma(Paciente, dor_de_cabeca),
    tem_sintoma(Paciente, dores_no_corpo),
    tem_sintoma(Paciente, dores_nas_articulacoes),
    tem_sintoma(Paciente, perda_de_peso),
    tem_sintoma(Paciente, nausea_vomito).


doenca_provavel(Paciente, covid) :- 
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, tosse),
    tem_sintoma(Paciente, calafrios),
    tem_sintoma(Paciente, dor_de_garganta),
    tem_sintoma(Paciente, dor_de_cabeca),
    tem_sintoma(Paciente, falta_de_paladar),
    tem_sintoma(Paciente, coriza).


doenca_provavel(Paciente, asma) :- 
    tem_sintoma(Paciente, falta_de_ar),
    tem_sintoma(Paciente, dificuldade_respirar),
    tem_sintoma(Paciente,  ),
    tem_sintoma(Paciente,  ),
    tem_sintoma(Paciente, peito_pesado).

doenca_provavel(Paciente, ascite) :- 
    tem_sintoma(Paciente, ganho_de_peso),
    tem_sintoma(Paciente, absdomen_tenso),
    tem_sintoma(Paciente, desconforto_abdominal).

doenca_provavel(Paciente, bronquite) :- 
    tem_sintoma(Paciente, dor_de_garganta),
    tem_sintoma(Paciente, dificuldade_respirar),
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, dor_muscular),
    tem_sintoma(Paciente, perda_oufato).

doenca_provavel(Paciente, botulismo) :- 
    tem_sintoma(Paciente, dor_de_cabeça),
    tem_sintoma(Paciente, vertigem),
    tem_sintoma(Paciente, tontura),
    tem_sintoma(Paciente, sonolencia),
    tem_sintoma(Paciente, visao_turva).

doenca_provavel(Paciente, caxumba) :- 
    tem_sintoma(Paciente, inxaço),
    tem_sintoma(Paciente, dor_glandulas_salivares),
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, dor_de_cabeca).

doenca_provavel(Paciente, conjutivite) :- 
    tem_sintoma(Paciente, vermelhidão_dos_olhos),
    tem_sintoma(Paciente, lacrimejamento_dos_olhos),
    tem_sintoma(Paciente, coceira_nos_olhos),
    tem_sintoma(Paciente, ardencia_nos_olhos),
    tem_sintoma(Paciente, inchaco_nas_palpebras).

doenca_provavel(Paciente, urticaria) :- 
    tem_sintoma(Paciente, lesao_avermelhada),
    tem_sintoma(Paciente, vergoes),
    tem_sintoma(Paciente, coceira),
    tem_sintoma(Paciente, inchaco).

doenca_provavel(Paciente, xistose) :- 
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, dor_de_cabeça),
    tem_sintoma(Paciente, calafrios),
    tem_sintoma(Paciente, suores),
    tem_sintoma(Paciente, fraqueza).

doenca_provavel(Paciente, depressao) :- 
    tem_sintoma(Paciente, irritabilidade),
    tem_sintoma(Paciente, ansiedade),
    tem_sintoma(Paciente, desanimo),
    tem_sintoma(Paciente, cancaco),
    tem_sintoma(Paciente, desmotivacao).

doenca_provavel(Paciente, crise_de_ansiedade) :- 
    tem_sintoma(Paciente, boca_seca),
    tem_sintoma(Paciente, bracos_dormentes),
    tem_sintoma(Paciente, calafrios),
    tem_sintoma(Paciente, suores),
    tem_sintoma(Paciente, tremores).

doenca_provavel(Paciente, gastrite) :- 
    tem_sintoma(Paciente, indigestao),
    tem_sintoma(Paciente, asia),
    tem_sintoma(Paciente, dor_estomago),
    tem_sintoma(Paciente, estufamento).

doenca_provavel(Paciente, catapora) :- 
    tem_sintoma(Paciente, manchas_vermelhas),
    tem_sintoma(Paciente, bolhas),
    tem_sintoma(Paciente, mal_estar),
    tem_sintoma(Paciente, cancaco),
    tem_sintoma(Paciente, febre_baixa).

doenca_provavel(Paciente, variola) :- 
    tem_sintoma(Paciente, febre),
    tem_sintoma(Paciente, dor_de_cabeça),
    tem_sintoma(Paciente, dor_nas_costas),
    tem_sintoma(Paciente, dor_abdominal),
    tem_sintoma(Paciente, manchas_vermelhas_na_boca).
