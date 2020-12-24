# -*- coding: utf-8 -*-
import pytest
import EP4
from EP4 import *



class TestTabuleiro():
    def test_ChecaVitoria(self):
        assert ChecaVitoria() == 1

    def test_ChecaDisponibilidade(self):
        assert ChecaDisponibilidade() == 1

    def test_ChecaEmpate(self):
        assert ChecaEmpate() == 1






def ChecaVitoria():
    tabuleiro_de_teste3 = Tabuleiro()
    for i in range(4):   # Verifica a vitoria em todas as linhas horizontais das matrizes 
        for j in range(4):
            tabuleiro_de_teste3.matriz1[i][j] = 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

        for j in range(4):
            tabuleiro_de_teste3.matriz2[i][j] = 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

        for j in range(4):
            tabuleiro_de_teste3.matriz3[i][j] = 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

        for j in range(4):
            tabuleiro_de_teste3.matriz4[i][j] = 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

        # for j in range(4):
        #     tabuleiro_de_teste3.matriz1[i][j] = 1
        # if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
        #     return 0
        # tabuleiro_de_teste3 = Tabuleiro()
    for j in range(4):   # Verifica a vitoria em todas as linhas verticais das matrizes 
            for i in range(4):
                tabuleiro_de_teste3.matriz1[i][j] = 1
            if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
                return 0
            tabuleiro_de_teste3 = Tabuleiro()

            for i in range(4):
                tabuleiro_de_teste3.matriz2[i][j] = 1
            if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
                return 0
            tabuleiro_de_teste3 = Tabuleiro()

            for i in range(4):
                tabuleiro_de_teste3.matriz3[i][j] = 1
            if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
                return 0
            tabuleiro_de_teste3 = Tabuleiro()

            for i in range(4):
                tabuleiro_de_teste3.matriz4[i][j] = 1
            if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
                return 0
            tabuleiro_de_teste3 = Tabuleiro()

    j = 0
    for i in range(4): # Verifica vitória na diagonal principal da matriz 1
        tabuleiro_de_teste3.matriz1[i][j] == 1
        j += 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

    j = 0
    for i in range(4): # Verifica vitória na diagonal principal da matriz2
        tabuleiro_de_teste3.matriz2[i][j] == 1
        j += 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

    j = 0
    for i in range(4): # Verifica vitória na diagonal principal da matriz3
        tabuleiro_de_teste3.matriz3[i][j] == 1
        j += 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()
    
    j = 0
    for i in range(4): # Verifica vitória na diagonal principal da matriz4
        tabuleiro_de_teste3.matriz2[i][j] == 1
        j += 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()
    
    j = 3
    for i in range(4): # Verifica vitória na diagonal secundária da matriz1
        tabuleiro_de_teste3.matriz1[i][j] == 1
        j -= 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()
    
    j = 3
    for i in range(4): # Verifica vitória na diagonal secundária da matriz2
        tabuleiro_de_teste3.matriz2[i][j] == 1
        j -= 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()
    
    j = 3
    for i in range(4): # Verifica vitória na diagonal secundária da matriz3
        tabuleiro_de_teste3.matriz3[i][j] == 1
        j -= 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()
    
    j = 3
    for i in range(4): # Verifica vitória na diagonal secundária da matriz4
        tabuleiro_de_teste3.matriz4[i][j] == 1
        j -= 1
        if(tabuleiro_de_teste3.verifica_vitoria(1, "teste") == 0):
            return 0
        tabuleiro_de_teste3 = Tabuleiro()

    return 1


def ChecaDisponibilidade():
    tabuleiro_de_teste2 = Tabuleiro()
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste2.matriz1[i][j] = 1
            if(tabuleiro_de_teste2.posicao_disponivel(1,i,j) == 1): #Significa que a posição está disponivel, mas ela não está!
                return 0
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste2.matriz2[i][j] = 1
            if(tabuleiro_de_teste2.posicao_disponivel(2,i,j) == 1):
                return 0
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste2.matriz3[i][j] = 1
            if(tabuleiro_de_teste2.posicao_disponivel(3,i,j) == 1):
                return 0
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste2.matriz4[i][j] = 1
            if(tabuleiro_de_teste2.posicao_disponivel(4,i,j) == 1):
                return 0
    return 1


def ChecaEmpate():
    tabuleiro_de_teste = Tabuleiro()
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste.matriz1[i][j] = 1
            tabuleiro_de_teste.casas_ocupadas+=1
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste.matriz2[i][j] = 1
            tabuleiro_de_teste.casas_ocupadas+=1
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste.matriz3[i][j] = 1
            tabuleiro_de_teste.casas_ocupadas+=1
    for i in range(4):
        for j in range(4):
            tabuleiro_de_teste.matriz4[i][j] = 1
            tabuleiro_de_teste.casas_ocupadas+=1
    if(tabuleiro_de_teste.verifica_empate() == 0): #Retorna 0 se empatar
        return 1
    else:
        return 0   # Tabuleiro Está cheio mas não empatou, ERRO