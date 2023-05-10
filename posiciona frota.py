def posiciona_frota(frota):

    tabuleiro = [[0 for i in range(10)] for j in range(10)]
    
    for tipo, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro
#
#
