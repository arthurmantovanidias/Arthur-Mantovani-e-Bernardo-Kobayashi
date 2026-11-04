from funcoes import (
    preenche_frota,
    posicao_valida,
    posiciona_frota,
    faz_jogada,
    afundados,
    monta_tabuleiros,
)


frota = {}
navios = {
    'porta-aviões': [4, 1],
    'navio-tanque': [3, 2],
    'contratorpedeiro': [2, 3],
    'submarino': [1, 4],
}

# O jogador posiciona a própria frota.
for nome_navio in navios:
    tamanho, quantidade = navios[nome_navio]
    for i in range(quantidade):
        valido = False
        while not valido:
            print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}')
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if nome_navio == 'submarino':
                orientacao = 'vertical'
            else:
                escolha = int(input('Orientação: [1] Vertical [2] Horizontal '))
                if escolha == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)
            if not valido:
                print('Esta posição não está válida!')
            else:
                frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)

# Posicionamento fixo do oponente indicado no exercício.
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)
quantidade_navios = sum(len(navios) for navios in frota_oponente.values())

# Exibe os dois tabuleiros antes da primeira jogada.
print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

jogando = True
while jogando:
    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))

    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))

    if tabuleiro_oponente[linha][coluna] in ('X', '-'):
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)
    if afundados(frota_oponente, tabuleiro_oponente) == quantidade_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
