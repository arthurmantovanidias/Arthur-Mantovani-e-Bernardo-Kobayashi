def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in novas_posicoes:
        if posicao[0] < 0 or posicao[0] > 9:
            return False

        if posicao[1] < 0 or posicao[1] > 9:
            return False

    for tipo in frota:
        for navio in frota[tipo]:
            for posicao in navio:
                if posicao in novas_posicoes:
                    return False

    return True