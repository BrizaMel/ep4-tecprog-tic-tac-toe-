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
    def verifica_empate(self):
        if self.casas_ocupadas < 64: # ainda pode jogar
            self.disponivel = 1
        else:
            self.disponivel = 0
        return self.disponivel
    def posicao_disponivel(self, matriz, linha, coluna):
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
    def verifica_vitoria(self, num, nome):
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
            return 1
        #verifica verticais "entre matrizes" (verticais das matrizes verticais) (16)
        for i in range(4):
            for j in range(4):
                if(self.matriz1[i][j]==num and self.matriz2[i][j]==num and self.matriz3[i][j]==num and self.matriz4[i][j]==num):
                    return 1
        #verifica diagonais das matrizes verticais (16)
        for i in range(4):
            if(self.matriz1[i][0]==num and self.matriz2[i][1]==num and self.matriz3[i][2]==num and self.matriz4[i][3]==num):
                    return 1
        for i in range(4):
            if(self.matriz4[i][0]==num and self.matriz3[i][1]==num and self.matriz2[i][2]==num and self.matriz1[i][3]==num):
                    return 1
        for j in range(4):
            if(self.matriz1[0][j]==num and self.matriz2[1][j]==num and self.matriz3[2][j]==num and self.matriz4[3][j]==num):
                    return 1
        for j in range(4):
            if(self.matriz4[0][j]==num and self.matriz3[1][j]==num and self.matriz2[2][j]==num and self.matriz1[3][j]==num):
                    return 1
        #verifica diagonais do cubo todo (4)
        if(self.matriz1[0][0]==num and self.matriz2[1][1]==num and self.matriz3[2][2]==num and self.matriz4[3][3]==num):
                return 1
        if(self.matriz1[0][3]==num and self.matriz2[1][2]==num and self.matriz3[2][1]==num and self.matriz4[3][0]==num):
                return 1
        if(self.matriz1[3][3]==num and self.matriz2[2][2]==num and self.matriz3[1][1]==num and self.matriz4[0][0]==num):
                return 1
        if(self.matriz1[3][0]==num and self.matriz2[2][1]==num and self.matriz3[1][2]==num and self.matriz4[0][3]==num):
                return 1
    def imprime_matriz(self):
        print("")
        print("       Matriz 1", end = '')
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
    def __init__(self, nome, XO,tabuleiro):
        self.nome = nome
        self.XO = XO
        self.tabuleiro = tabuleiro
    def jogada(self, matriz, linha, coluna):
        if(matriz == 1):
           self.tabuleiro.matriz1[linha][coluna] = self.XO
        elif(matriz == 2):
            self.tabuleiro.matriz2[linha][coluna] = self.XO
        elif(matriz == 3):
            self.tabuleiro.matriz3[linha][coluna] = self.XO
        elif(matriz == 4):
            self.tabuleiro.matriz4[linha][coluna] = self.XO
            

class Humano(Jogador):
    def realiza_jogada(self):
        matrizes = {1,2,3,4}
        linhas = {0,1,2,3}
        colunas = {0,1,2,3}
        jogadaValida = 0
        while(jogadaValida == 0):
            print("")
            print("----------Por favor jogadore", self.nome,"----------")
            print("")
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
            if(self.tabuleiro.posicao_disponivel(matriz, linha, coluna)):
                self.jogada(matriz, linha, coluna)
                print("")
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
            if(self.tabuleiro.posicao_disponivel(matriz, linha, coluna)):
                self.jogada(matriz, linha, coluna)
                print("")
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
                    if(self.tabuleiro.posicao_disponivel(m, i, j)):
                        self.jogada(m, i, j)
                        ok = 1
                    j += 1
                i += 1
            m += 1
        print("")
        print(self.nome, " (comecru) jogou na matriz ", m, ", linha ", i, " e coluna ", j)

def main():
    novoJogo = 1
    while(novoJogo == 1):
        tabuleiro = Tabuleiro()
        print("Tipos de jogadores disponíveis: ")
        print("(1) Jogador Humano")
        print("(2) Jogador Estabanado")
        print("(3) Jogador Come cru")
        print("")
        possibilidadesTipo = {1, 2, 3}
        primeiro = int(input("Qual o tipo do primeiro jogador? (escolha 1, 2 ou 3):  "))
        print("")
        while(primeiro not in possibilidadesTipo): 
            primeiro = int(input("Tipo de primeiro jogador inexistente. Escolha o tipo 1, 2 ou 3): "))
            print("")
        
        nomeprimeiro= input("Digite o nome do primeiro jogador: ")
        print("")

        segundo = int(input("Qual o tipo do segundo jogador? (escolha 1, 2 ou 3): "))
        print("")
        while(segundo not in possibilidadesTipo):
            segundo = int(input("Tipo de segundo jogador inexistente. Escolha o tipo 1, 2 ou 3):  ")) 
            print("")

        nomesegundo = input("Digite o nome do segundo jogador: ")
        print("")

        if(primeiro == 1):
            jogador1 = Humano(nomeprimeiro, 1,tabuleiro)
        elif(primeiro == 2):
            jogador1 = Estabanado(nomeprimeiro, 1, tabuleiro)
        elif(primeiro == 3):
            jogador1 = Comecru(nomeprimeiro, 1,tabuleiro)
        
        if(segundo == 1):
            jogador2 = Humano(nomesegundo, 2, tabuleiro)
        elif(segundo == 2):
            jogador2 =  Estabanado(nomesegundo, 2, tabuleiro)
        elif(segundo == 3):
            jogador2 = Comecru(nomesegundo, 2, tabuleiro)

        verifica = 0
        print("Que os jogos comecem!")
        print("")

        while(1):

            if(tabuleiro.verifica_empate() == 1):
                tabuleiro.imprime_matriz()
                jogador1.realiza_jogada()
                tabuleiro.casas_ocupadas+=1
                verifica = tabuleiro.verifica_vitoria(1, jogador1.nome)
                if(verifica == 1):
                    tabuleiro.imprime_matriz()
                    print("")
                    print("-------------Jogadore ", jogador1.nome ," ganhou!-------------")
                    break
            else:
                print("Não há mais casas disponíveis. Fim de jogo.")
                print("")
                break

            if(tabuleiro.verifica_empate() == 1):
                tabuleiro.imprime_matriz()
                jogador2.realiza_jogada()
                tabuleiro.casas_ocupadas+=1
                verifica = tabuleiro.verifica_vitoria(2, jogador2.nome)
                if(verifica == 1):
                    tabuleiro.imprime_matriz()
                    print("")
                    print("-------------Jogadore ", jogador2.nome ," ganhou!-------------")
                    break
            else:
                print("Não há mais casas disponíveis. Fim de jogo.")
                print("")
                break
        print("")
        escolha = input("Deseja continuar jogando? Digite 'sim' ou 'nao': ")
        if(escolha == "sim"):
            novoJogo=1
        else:
            novoJogo=0


if __name__ == "__main__":
    main ()




    




    

    

    



