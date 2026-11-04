def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        l = posicao[0]
        c = posicao[1]

        if l < 0 or l >= 10 or c < 0 or c >= 10:
            return False

        for nome_navio in frota:
            for navio in frota[nome_navio]:
                if posicao in navio:
                    return False

    return True
