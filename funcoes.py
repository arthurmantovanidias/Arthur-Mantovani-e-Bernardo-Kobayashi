def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])
    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in posicoes:
        l, c = posicao
        if l < 0 or l >= 10 or c < 0 or c >= 10:
            return False
        for nome_navio in frota:
            for navio in frota[nome_navio]:
                if posicao in navio:
                    return False
    return True


def posiciona_frota(frota):
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for linha, coluna in navio:
                tabuleiro[linha][coluna] = 1
    return tabuleiro


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro


def afundados(frota, tabuleiro):
    quantidade = 0
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            afundou = True
            for linha, coluna in navio:
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
                    break
            if afundou:
                quantidade += 1
    return quantidade


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    cabecalho = '   ' + '  '.join(str(numero) for numero in range(10))
    texto = cabecalho + '      ' + cabecalho + '\n'
    texto += '_' * 31 + '      ' + '_' * 31 + '\n'

    for linha in range(10):
        jogador_info = '  '.join(str(item) for item in tabuleiro_jogador[linha])
        oponente_info = '  '.join(
            str(item) if item in ('X', '-') else '0'
            for item in tabuleiro_oponente[linha]
        )
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
