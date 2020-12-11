#!/usr/bin/python 

class Tabuleiro: 
    def __init__(self):
        for i in range(4):
            for j in range(4):
                self.matriz1[i][j] = 0
                self.matriz2[i][j] = 0
                self.matriz3[i][j] = 0
                self.matriz4[i][j] = 0
        
        self.casas_ocupadas = 0
        
    def disponibilidade(self):
        if self.casas_ocupadas < 64: # ainda pode jogar 
            self.disponivel = 1
        else:
            self.disponivel = 0
        return self.disponivel 
    
    
class Jogador:
    def __init__(self, nome, X_ou_O):
        self.nome = nome 
        self.X_ou_O = X_ou_O

    def casa_disponivel(self, matriz, linha, coluna):
        if matriz[linha][coluna] == 0:
            return 1 
        else:
            return 0
    
    def jogada(self, matriz, linha, coluna):
        if casa_disponivel(matriz, linha, coluna):
            matriz[linha][coluna] = X_ou_O
            print("Próximo jogador")
        else:
            print("Casa não disponível!")
        

    


    
    
    
        
    

        
        