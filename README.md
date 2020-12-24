# EP4-TECPROG
# Jogo da velha em 3D


# integrantes:

Nome: Luiz Carlos Costa da Silva
Nome: Briza Mel Dias de Sousa
Nome: Beatriz Schicchi Zilberman

## Descrição:

    Este é o quarto exercício programa da matéria técnicas em programação.
    Neste EP, é feito um jogo conhecido como "jogo da velha em 3d" ou "tic tac toe
    4d" usando orientação a objeto.

## Tipos de jogadores:

    Neste jogo há 3 tipos de jogadores, sendo eles: O jogador humano (pede um 
    input ao usuário), o estabanado(Joga em uma posição aleatória do tabuleiro)
    e o jogador Comecru(Ele joga na primeira posição disponível que encontrar).

## Como jogar

    Ao executar o programa (mais detalhes serão explicados na sessão como
    executar) será pedido ao usuário para escolher quais o tipos de jogadores
    mencionados na sessão anterior e os nomes deles.
     Caso seja escolhido algum jogador humano, quando chegar a vez dele de jogar
    será pedido para escolher uma matriz (números inteiros de 1 a 4), linha e 
    coluna (números inteiros de 0 a 3). Caso seja digitado um valor fora desse
    intervalo, será pedido ao usuário para digitar um valor válido.
     Caso seja escolhido um jogador do tipo Estabanado ou Comecru ele irão jogar
    automáticamente até a condição de vitória ser cumprida. 

## Como vencer o jogo

     Para vencer o jogo, o jogador deve realizar uma "linha" nas matrizes, ela
    pode ser na mesma matrizes, ou utilizar as 4 ao mesmo tempo, por exemplo, 
    fazer uma coluna usando a lateral do cubo, ou uma diagonal entre os cantos.

## Como instalar

    Este é um jogo criado para python3, portanto é necessário instalar no seu 
    sistema operacional python3 ou usar plataformas de máquina virtual como
    jupyter notebook.

     Para rodar esse EP4 é necessário também instalar a biblioteca NumPy, o tutorial 
    de como instalar como ser conferido neste site: 
    https://numpy.org/install/

     Além disso é necessário instalar o pytest para executar o testes automatizados, 
    o tutorial de como instalar o pytest pode ser conferido neste site:
    https://docs.pytest.org/en/3.0.6/getting-started.html

## Como executar o programa

    Para começar o jogo o usuario deve no terminal executar o programa como
    "python3 EP4", o jogo irá automaticamente começar após este comando.
    
    Para executar os testes basta digitar no terminal "pytest" que ele irá
    executar todos os arquivos de teste no repositório. Caso o usuário deseje
    executar testes individuais, isto é, test_Jogador e test_Tabuleiro será
    necessário digitar respectivamente "pytest test_Jogador" e "pytest_Tabuleiro".

