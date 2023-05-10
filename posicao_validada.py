def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes (linha, coluna, orientacao, tamanho)

    if orientacao == 'vertical' and 10 - linha < tamanho:
        return False
    
    if orientacao == 'horizontal' and 10 - coluna < tamanho:
        return False
    

    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        for tipo, posicoes in frota.items():
            for posicao in posicoes:
                for linha_frota, coluna_frota in posicao:
                    if linha == linha_frota and coluna == coluna_frota:
                        return False
                    
    return True