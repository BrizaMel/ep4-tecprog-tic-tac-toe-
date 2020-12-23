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
    def verifica(self, num, nome):
        #verifica linhas de cada matriz horizontal (16)
        for i in range(4):
            v1=0; v2=0; v3=0; v4=0
            for j in range(4):
                if(self.matriz1[i][j]==num):
                    v1+=1
                if(self.matriz2[i][j]==num):
                    v2+=1
                if(self.matriz3[i][j]==num):
                    v3+=1
                if(self.matriz4[i][j]==num):
                    v4+=1
            if(v1==4 or v2==4 or v3==4 or v4==4):
                print("")
                print("-------------Jogadore ", nome ," ganhou!-------------")
                print("")
                return 1
        #verifica colunas de cada matriz horizontal (16)
        for j in range(4):
            v1=0; v2=0; v3=0; v4=0
            for i in range(4):
                if(self.matriz1[i][j]==num):
                    v1+=1
                if(self.matriz2[i][j]==num):
                    v2+=1
                if(self.matriz3[i][j]==num):
                    v3+=1
                if(self.matriz4[i][j]==num):
                    v4+=1
            if(v1==4 or v2==4 or v3==4 or v4==4):
                print("")
                print("-------------Jogadore ", nome ," ganhou!-------------")
                print("")
                return 1
        #verifica diagonais de cada matriz horizontal (8)
        v1=0; v2=0; v3=0; v4=0; j=0
        for i in range(4):
            if(self.matriz1[i][j]==num):
                v1+=1
            if(self.matriz2[i][j]==num):
                v2+=1
            if(self.matriz3[i][j]==num):
                v3+=1
            if(self.matriz4[i][j]==num):
                v4+=1
            j+=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("")
            print("-------------Jogadore ", nome ," ganhou!-------------")
            print("")
            return 1
        #verifica diagonais de cada matriz horizontal (8)
        v1=0; v2=0; v3=0; v4=0; j=3
        for i in range(4):
            if(self.matriz1[i][j]==num):
                v1+=1
            if(self.matriz2[i][j]==num):
                v2+=1
            if(self.matriz3[i][j]==num):
                v3+=1
            if(self.matriz4[i][j]==num):
                v4+=1
            j-=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("")
            print("-------------Jogadore ", nome ," ganhou!-------------")
            print("")
            return 1
        v1=0; v2=0; v3=0; v4=0; j=3
        for i in range(4):
            j-=1
            if(self.matriz1[i][j]==num):
                v1+=1
            if(self.matriz2[i][j]==num):
                v2+=1
            if(self.matriz3[i][j]==num):
                v3+=1
            if(self.matriz4[i][j]==num):
                v4+=1
        if(v1==4 or v2==4 or v3==4 or v4==4):
            print("")
            print("-------------Jogadore ", nome ," ganhou!-------------")
            print("")
            return 1
        #verifica verticais "entre matrizes" (verticais das matrizes verticais) (16)
        for i in range(4):
            for j in range(4):
                if(self.matriz1[i][j]==num and self.matriz2[i][j]==num and self.matriz3[i][j]==num and self.matriz4[i][j]==num):
                    print("")
                    print("-------------Jogadore ", nome ," ganhou!-------------")
                    print("")
                    return 1
        #verifica diagonais das matrizes verticais (16)
        for i in range(4):
            if(self.matriz1[i][0]==num and self.matriz2[i][1]==num and self.matriz3[i][2]==num and self.matriz4[i][3]==num):
                    print("")
                    print("-------------Jogadore ", nome ," ganhou!-------------")
                    print("")
                    return 1
        for i in range(4):
            if(self.matriz4[i][0]==num and self.matriz3[i][1]==num and self.matriz2[i][2]==num and self.matriz1[i][3]==num):
                    print("")
                    print("-------------Jogadore ", nome ," ganhou!-------------")
                    print("")
                    return 1
        for j in range(4):
            if(self.matriz1[0][j]==num and self.matriz2[1][j]==num and self.matriz3[2][j]==num and self.matriz4[3][j]==num):
                    print("")
                    print("-------------Jogadore ", nome ," ganhou!-------------")
                    print("")
                    return 1
        for j in range(4):
            if(self.matriz4[0][j]==num and self.matriz3[1][j]==num and self.matriz2[2][j]==num and self.matriz1[3][j]==num):
                    print("")
                    print("-------------Jogadore ", nome ," ganhou!-------------")
                    print("")
                    return 1
        #verifica diagonais do cubo todo (4)
        if(self.matriz1[0][0]==num and self.matriz2[1][1]==num and self.matriz3[2][2]==num and self.matriz4[3][3]==num):
                print("")
                print("-------------Jogadore ", nome ," ganhou!-------------")
                print("")
                return 1
        if(self.matriz1[0][3]==num and self.matriz2[1][2]==num and self.matriz3[2][1]==num and self.matriz4[3][0]==num):
                print("")
                print("-------------Jogadore ", nome ," ganhou!-------------")
                print("")
                return 1
        if(self.matriz1[3][3]==num and self.matriz2[2][2]==num and self.matriz3[1][1]==num and self.matriz4[0][0]==num):
                print("")
                print("-------------Jogadore ", nome ," ganhou!-------------")
                print("")
                return 1
        if(self.matriz1[3][0]==num and self.matriz2[2][1]==num and self.matriz3[1][2]==num and self.matriz4[0][3]==num):
                print("")
                print("-------------Jogadore ", nome ," ganhou!-------------")
                print("")
                return 1

    def imprimematriz(self):
        print("")
        print("       Matriz 1", end='')
        print("                   ", end='')
        print("   Matriz 2")
        print("   __0___1___2___3_", end='') 
        print("           ", end='')
        print("    __0___1___2___3_")
        for i in range(4):
            print(i, " ", end='')
            for j in range(4):
                if(self.matriz1[i][j] == 1):
                    print("|_x_", end='')
                elif(self.matriz1[i][j] == 2):
                    print("|_o_", end='')
                elif(self.matriz1[i][j] == 0):  
                    print("|___", end='')
            print("|", end='')
            print("           ", end='')
            print(i, " ", end='')
            for j in range(4):
                if(self.matriz2[i][j] == 1):
                    print("|_x_", end='')
                elif(self.matriz2[i][j] == 2):
                    print("|_o_", end='')
                elif(self.matriz2[i][j] == 0): 
                    print("|___", end='')
            print("|")
        print("  ")
        print("       Matriz 3", end='')
        print("                    ", end='')
        print("   Matriz 4")
        print("   __0___1___2___3_", end='') 
        print("           ", end='')
        print("    __0___1___2___3_")
        for i in range(4):
            print(i, " ", end='')
            for j in range(4):
                if(self.matriz3[i][j] == 1):
                    print("|_x_", end='')
                elif(self.matriz3[i][j] == 2):
                    print("|_o_", end='')
                elif(self.matriz3[i][j] == 0): 
                    print("|___", end='')
            print("|", end='')
            print("           ", end='')
            print(i, " ", end='')
            for j in range(4):
                if(self.matriz4[i][j] == 1):
                    print("|_x_", end='')
                elif(self.matriz4[i][j] == 2):
                    print("|_o_", end='')
                elif(self.matriz4[i][j] == 0): 
                    print("|___", end='')
            print("|")
        print("")

        
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

class Humano(Jogador):
    def realiza_jogada(self):
        matrizes = {1,2,3,4}
        linhas = {0,1,2,3}
        colunas = {0,1,2,3}
        jogadaValida = 0
        while(jogadaValida == 0):
            print("")
            print("Por favor jogadore", self.nome)
            matriz = int(input("Escolha uma matriz(1, 2, 3 ou 4): "))
            linha = int(input("Escolha uma linha(0, 1, 2 ou 3): "))
            coluna = int(input("Escolha uma coluna(0, 1, 2 ou 3): "))

            while( matriz not in matrizes ):
                print("Desculpe, o número de matriz que você digitou é invalido, tente novamente.")
                matriz = int(input("Digite um número de matriz válido(1 a 4): "))
            while( linha not in linhas ):
                print("Desculpe, o número de linha que você digitou é invalido, tente novamente.")
                linha = int(input("Digite um número de linha válido(0 a 3): "))
            while( coluna not in colunas ):
                print("Desculpe, o número de coluna que você digitou é invalido, tente novamente.")
                coluna = int(input("Digite um número de coluna válido(0 a 3) "))

            if(tabuleiro.posicaodisponivel(matriz, linha, coluna)):
                self.jogada(matriz, linha, coluna)
                print(self.nome, " (humano) jogou na matriz ", matriz, ", linha ", linha, " e coluna ", coluna)
                jogadaValida = 1
            else:
                print("Essa posição já está ocupada, escolha outra.")


class Estabanado(Jogador):
    def realiza_jogada(self):
        jogadaValida = 0
        while(jogadaValida == 0):
            matriz = randint(1,4)
            linha = randint(0,3)
            coluna = randint(0, 3)
            if(tabuleiro.posicaodisponivel(matriz, linha, coluna)):
                self.jogada(matriz, linha, coluna)
                print(self.nome, " (estabanado) jogou na matriz ", matriz, ", linha ", linha, " e coluna ", coluna)
                jogadaValida = 1

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
        print(self.nome, " (comecru) jogou na matriz ", matriz, ", linha ", linha, " e coluna ", coluna)

def main():
    print("Tipos de jogadores disponíveis: ")
    print("(1) Jogador Humano")
    print("(2) Jogador Estabanado")
    print("(3) Jogador Come cru")
    possibilidadesTipo = {1, 2, 3}
    primeiro = input("Qual o tipo do primeiro jogador? (escolha 1, 2 ou 3) ")
    while(primeiro not in possibilidadesTipo): 
        primeiro = int(input("Tipo de primeiro jogador inexistente. Escolha o tipo 1, 2 ou 3: "))
    
    nomeprimeiro= input("Digite o nome do primeiro jogador: ")

    segundo = input("Qual o tipo do segundo jogador? (escolha 1, 2 ou 3 ")
    while(segundo not in possibilidadesTipo):
        segundo = int(input("Tipo de segundo jogador inexistente. Escolha o tipo 1, 2 ou 3: ")) 

    nomesegundo = input("Digite o nome do segundo jogador: ")

    if(primeiro == 1):
        jogador1 = Humano(nomeprimeiro, 1)
    elif(primeiro == 2):
        jogador1 = Estabanado(nomeprimeiro, 1)
    elif(primeiro == 3):
        jogador 1 = Comecru(nomeprimeiro, 1)
    
    if(segundo == 1):
        jogador2 = Humano(nomesegundo, 2)
    elif(segundo == 2):
        jogador2 =  Estabanado(nomesegundo, 2)
    elif(segundo == 3):
        jogador 2 = Comecru(nomesegundo, 2)

    tabuleiro = Tabuleiro()
    verifica = 0
    print("Que os jogos comecem!")

    while(1):

        if(tabuleiro.disponibilidade() == 1):
            tabuleiro.imprimematriz()
            jogador1.realiza_jogada()
            verifica = tabuleiro.verifica(1, jogador1)
            if(verifica == 1):
                break
        else:
            print("Não há mais casas disponíveis. Fim de jogo.")
            break

        if(tabuleiro.disponibilidade() == 1):
            tabuleiro.imprimematriz()
            jogador2.realiza_jogada()
            verifica = tabuleiro.verifica(2, jogador2)
            if(verifica == 1):
                break
        else:
            print("Não há mais casas disponíveis. Fim de jogo.")
            break
        
main()



    

    

    



