#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from random import randint

class Tabuleiro:
    def __init__(self):
        self.matriz1 = np.zeros((4,4))
        self.matriz2 = np.zeros((4,4))
        self.matriz3 = np.zeros((4,4))
        self.matriz4 = np.zeros((4,4))
        self.casas_ocupadas = 0

    def disponibilidade(self):
        if self.casas_ocupadas < 64: # ainda pode jogar
            self.disponivel = 1
        else:
            self.disponivel = 0
        return self.disponivel

    def posicaodisponivel(self, matriz, linha, coluna):
        if(matriz == 1 and self.matriz1[linha][coluna] != 0):
           return 0
        elif(matriz == 2 and self.matriz2[linha][coluna] != 0):
            return 0
        elif(matriz == 3 and self.matriz3[linha][coluna] != 0):
            return 0
        elif(matriz == 4 and self.matriz4[linha][coluna] != 0):
            return 0
        else:
            return 1

    def verifica(self, num):
        v1=0; v2=0; v3=0; v4=0
        for i in range(4):
            for j in range(4):
                if(matriz1[i][j]==num):
                    v1+=1
                if(matriz2[i][j]==num):
                    v2+=1
                if(matriz3[i][j]==num):
                    v3+=1
                if(matriz1[i][j]==num):
                    v4+=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("Jogadore ", num ," ganhou!")
            return num
        v1=0; v2=0; v3=0; v4=0
        for j in range(4):
            for i in range(4):
                if(matriz1[i][j]==num):
                    v1+=1
                if(matriz2[i][j]==num):
                    v2+=1
                if(matriz3[i][j]==num):
                    v3+=1
                if(matriz1[i][j]==num):
                    v4+=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("Jogadore ", num ," ganhou!")
            return num
        v1=0; v2=0; v3=0; v4=0; j=0
        for i in range(4):
            j+=1
            if(matriz1[i][j]==num):
                v1+=1
            if(matriz2[i][j]==num):
                v2+=1
            if(matriz3[i][j]==num):
                v3+=1
            if(matriz1[i][j]==num):
                v4+=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("Jogadore ", num ," ganhou!")
            return num
        v1=0; v2=0; v3=0; v4=0; j=3
        for i in range(4):
            j-=1
            if(matriz1[i][j]==num):
                v1+=1
            if(matriz2[i][j]==num):
                v2+=1
            if(matriz3[i][j]==num):
                v3+=1
            if(matriz1[i][j]==num):
                v4+=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("Jogadore ", num ," ganhou!")
            return num


class Jogador:
    def __init__(self, nome, XO):
        self.nome = nome
        self.XO = XO
    def jogada(self, matriz, linha, coluna):
        if(matriz == 1):
           tabuleiro.matriz1[linha][coluna] = self.XO
        elif(matriz == 2):
            tabuleiro.matriz2[linha][coluna] = self.XO
        elif(matriz == 3):
            tabuleiro.matriz3[linha][coluna] = self.XO
        elif(matriz == 4):
            tabuleiro.matriz4[linha][coluna] = self.XO
        else:
            print("Desculpe, Número de matriz inválido, digite um número entre 1 e 4")


class Humano(Jogador):
    def realiza_jogada(self):
        print("Por favor jogadore", self.nome)
        matriz, linha, coluna = input("Escolha a matriz, linha e coluna separados por espaço: ").split()
        matriz, linha, coluna = int(matriz), int(linha), int(coluna)
        self.jogada(matriz, linha, coluna)


class Estabanado(Jogador):
    def realiza_jogada(self):
        matriz = randint(1,4)
        linha = randint(0,3)
        coluna = randint(0, 3)
        print("Matriz: ",matriz, "linha: ", linha, "coluna: ", coluna)
        self.jogada(matriz, linha, coluna)

class Comecru(Jogador):
    def realiza_jogada(self):
        m = 1
        ok = 0
        while(m<4 and ok== 0):
            i = 0
            j = 0
            while(i < 4 and ok == 0):
                j = 0
                while(j < 4 and ok == 0):
                    if(tabuleiro.posicaodisponivel(m, i, j)):
                        self.jogada(m, i, j)
                        ok = 1
                    j += 1
                i += 1
            m += 1
