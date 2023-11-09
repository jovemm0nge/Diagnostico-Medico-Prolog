%% -> Fatos


%% -> Regras

sintoma(febre).
sintoma(tosse).
sintoma(dor_de_cabeca).
sintoma(dor_de_garganta).
sintoma(dor_no_corpo).
sintoma(falta_de_ar).
sintoma(dor_no_peito).
sintoma(fraqueza).
sintoma(indisposicao).
sintoma(palpitacao).
sintoma(vontade_urinar_frequente).
sintoma(queimacao_ao_urinar).
sintoma(urina_turva).
sintoma(dor_na_nuca).
sintoma(tonturas).
sintoma(zumbido_ouvido).
sintoma(visao_embacada).
sintoma(palpitacoes).
sintoma(taquicardia).
sintoma(nauseas).
sintoma(fadiga).
sintoma(sonolencia).
sintoma(desmaio).
sintoma(fome_frequente).
sintoma(sede_constante).
sintoma(mudanca_de_humor).
sintoma(perda_de_peso).
sintoma(diarreia).
sintoma(perda_apetite).
sintoma(colica_severa).
sintoma(barriga_inchada).
sintoma(flatulencia).
sintoma(febre_alta).
sintoma(dor_de_cabeca).
sintoma(dores_no_corpo).
sintoma(dores_nas_articulacoes).
sintoma(calafrios).
sintoma(falta_de_paladar).
sintoma(coriza).
sintoma(dificuldade_respirar).
sintoma(sensacao_aperto_peito).
sintoma(chiado_no_peito).
sintoma(peito_pesado).
sintoma(absdomen_tenso).
sintoma(desconforto_abdominal).
sintoma(dor_muscular).
sintoma(perda_oufato).
sintoma(vertigem).
sintoma(visao_turva).
sintoma(inxaco).
sintoma(vermelhidao_dos_olhos).
sintoma(lacrimejamento_dos_olhos).
sintoma(coceira_nos_olhos).
sintoma(ardencia_nos_olhos).
sintoma(inchaco_nas_palpebras).
sintoma(lesao_avermelhada).
sintoma(vergoes).
sintoma(coceira).
sintoma(inchaco).
sintoma(dor_de_cabeca).
sintoma(suores).
sintoma(irritabilidade).
sintoma(ansiedade).
sintoma(desanimo).
sintoma(cancaco).
sintoma(desmotivacao).
sintoma(boca_seca).
sintoma(bracos_dormentes).
sintoma(tremores).
sintoma(indigestao).
sintoma(asia).
sintoma(dor_estomago).
sintoma(estufamento).
sintoma(manchas_vermelhas).
sintoma(bolhas).
sintoma(mal_estar).
sintoma(febre_baixa).
sintoma(dor_nas_costas).
sintoma(dor_abdominal).
sintoma(manchas_vermelhas_na_boca).
sintoma(homem, disfuncao_eretil).
sintoma(homem, sangue_no_semen).

condicao(cance_de_prostata, [disfuncao_eretil, sangue_no_semen]).
condicao(resfriado, [febre, tosse]).
condicao(gripe, [febre, tosse, dor_de_garganta, fraqueza]).
condicao(pnenomonia, [ febre, dor_de_cabeca, dor_no_corpo, tosse, falta_de_ar, dor_no_peito]).
condicao(anemia, [ fraqueza, indisposicao, falta_de_ar, palpitacao]).
condicao(infeccao_urinaria, [ vontade_urinar_frequente, queimacao_ao_urinar, febre, urina_turva]).
condicao(pressao_alta, [ dor_na_nuca, dor_de_cabeca, tonturas, zumbido_ouvido, visao_embacada, palpitacoes]).
condicao(pressao_baixa, [ tontura, taquicardia, nauseas, fadiga, sonolencia, desmaio]).
condicao(diabetes, [ fome_frequente, sede_constante, fadiga, mudanca_de_humor, vontade_urinar_frequente, perda_de_peso]).
condicao(apendicite, [ diarreia, perda_apetite, colica_severa, febre, barriga_inchada, flatulencia]).
condicao(dengue, [ febre_alta, dor_de_cabeca, dores_no_corpo, dores_nas_articulacoes, perda_de_peso, nausea_vomito]).
condicao(covid, [ febre, tosse, calafrios, dor_de_garganta, dor_de_cabeca, falta_de_paladar, coriza]).
condicao(asma, [ falta_de_ar, dificuldade_respirar, sensacao_aperto_peito, chiado_no_peito, peito_pesado]).
condicao(ascite, [ ganho_de_peso, absdomen_tenso, desconforto_abdominal]).
condicao(bronquite, [ dor_de_garganta, dificuldade_respirar, febre, dor_muscular, perda_oufato]).
condicao(botulismo, [ dor_de_cabeca, vertigem, tontura, sonolencia, visao_turva]).
condicao(caxumba, [ inxaco, febre, dor_de_cabeca]).
condicao(conjutivite, [ vermelhidao_dos_olhos, lacrimejamento_dos_olhos, coceira_nos_olhos, ardencia_nos_olhos, inchaco_nas_palpebras]).
condicao(urticaria, [  lesao_avermelhada, vergoes, coceira, inchaco]).
condicao(xistose, [ febre, dor_de_cabeca, calafrios, suores, fraqueza]).
condicao(depressao, [ irritabilidade, ansiedade, desanimo, cancaco, desmotivacao]).
condicao(crise_de_ansiedade, [ boca_seca, bracos_dormentes, calafrios, suores, tremores]).
condicao(gastrite, [ indigestao, asia, dor_estomago, estufamento]).
condicao(catapora, [manchas_vermelhas, bolhas, mal_estar, cancaco, febre_baixa]).
condicao(variola, [ febre, dor_de_cabeca, dor_nas_costas, dor_abdominal, manchas_vermelhas_na_boca]).