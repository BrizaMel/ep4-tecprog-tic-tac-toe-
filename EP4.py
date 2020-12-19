#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import numpy as np

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
    
    
class Jogador:
    def __init__(self, nome, XO):
        self.nome = nome 
        self.XO = XO
    def jogada(self, matriz, linha, coluna):
        matriz[linha][coluna] = self.XO
        print("Próximo jogador")
        

class Humano(Jogador):
    def realiza_jogada(self):
        print("Por favor jogadore", self.nome)
        matriz, linha, coluna = input("Escolha a matriz, linha e coluna separados por espaço: ").split()
        matriz, linha, coluna = int(matriz), int(linha), int(coluna)
        if(matriz == 1):
           self.jogada(tabuleiro.matriz1, linha, coluna)
        elif(matriz == 2):
            self.jogada(tabuleiro.matriz2, linha, coluna)
        elif(matriz == 3):
            self.jogada(tabuleiro.matriz3, linha, coluna)
        elif(matriz == 4):
            self.jogada(tabuleiro.matriz4, linha, coluna)
        else:
            print("Desculpe, Número de matriz inválido, digite um número entre 1 e 4")
            

class 



      
    # else:
    #     print("Casa não disponível!")

    # if casa_disponivel(matriz, linha, coluna):

    
    # def casa_disponivel(self, matriz, linha, coluna):
    #     if matriz[linha][coluna] == 0:
    #         return 1 
    #     else:
    #         return 0




    
    
    
        
    

        
        