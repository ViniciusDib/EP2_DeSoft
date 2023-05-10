def afundados (frota, tabuleiro):
    contador = 0

    for tipo, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                if tabuleiro[linha][coluna] == 'X':
                    continua = True

                else:
                    continua = False
                    break

            if continua:
                contador += 1
    
    return contador
