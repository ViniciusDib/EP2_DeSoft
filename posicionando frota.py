def afundados(frotas, tabuleiro):
    afundados = 0
    for ship in frotas:
        for posicao in frotas[ship]:
            afundado = True
            for coord in posicao:
                if tabuleiro[coord[0]][coord[1]] != "X":
                    afundado = False
                    break
            if afundado:
                afundados += 1
    return afundados

import random

def define_posicoes (linha, coluna, orientacao, tamanho):
    lista = []

    if orientacao == 'vertical':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha+i)
            posicao.append(coluna)
            lista.append(posicao)

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha)
            posicao.append(coluna+i)
            lista.append(posicao)


    return lista

def faz_jogada(tabuleiro , linha , coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    else:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro


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


def posiciona_frota(frota):

    tabuleiro = [[0 for i in range(10)] for j in range(10)]
    
    for tipo, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro
#


def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota


nomes = ["porta-aviões" , "navio-tanque" , "navio-tanque" , "contratorpedeiro" ,"contratorpedeiro" , "contratorpedeiro" , "submarino","submarino","submarino","submarino"]
tamanhos = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
frota = {}
for i in range(10):
    condic = False
    while condic == False:
        print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(nomes[i] , tamanhos[i]))
        linha2 = int(input("Linha: "))
        coluna2 = int(input("Coluna: "))

        if nomes[i] == "submarino":
            orientacao2 = 1
            tamanho2 = 1
        else:
            orientacao2 = int(input("[1] Vertical [2] Horizontal >"))
            tamanho2 = tamanhos[i]
        orientacao = ""
        if orientacao2 == 1:
            orientacao = "vertical"
        elif orientacao2 == 2:
            orientacao = "horizontal"
        CouE = posicao_valida(frota , linha2 , coluna2 , orientacao , tamanho2)
        if CouE == False:
            print("Esta posição não está válida!")
        else:
            condic = True
    preenche_frota(frota , nomes[i] , linha2 , coluna2 , orientacao , tamanhos[i])

print(frota)
