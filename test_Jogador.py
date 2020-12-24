# -*- coding: utf-8 -*-
import pytest
import EP4
from EP4 import *


class testeJogador():
    def testeJogador(self):
        assert testeJogadaValida() == 1


def testeJogadaValida():
    tabuleiro_de_teste4 = Tabuleiro()
    jogadorTeste = Humano("jogador", 1, tabuleiro_de_teste4)
    for m in range(4):
        for i in range(4):
            for j in range(4):
                jogadorTeste.jogada(m+1, i, j)

        for i in range(4):
            for j in range(4):
                if(tabuleiro_de_teste4.matriz1[i][j] != 1 or tabuleiro_de_teste4.matriz2[i][j] != 1 or tabuleiro_de_teste4.matriz3[i][j] != 1 or tabuleiro_de_teste4.matriz4[i][j] != 1):
                    return 0
        return 1