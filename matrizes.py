vazio = " "
matriz_y = 35
matriz_x = 95
matriz = []

def iniciar_matriz(matriz_y, matriz_x, vazio, matriz):
    '''
        função que inicia a matriz de controle
    '''
    for i in range(matriz_y):
        matriz.append([])
        for j in range(matriz_x):
            matriz[i].append(vazio)

def limpar_tela(matriz_y, matriz_x, vazio, matriz):
    '''
        função que limpa a tela do jogo apagando todos os valores
        da matriz de controle
    '''
    for i in range(matriz_y):
        for j in range(matriz_x):
            matriz[i][j] = vazio

def desenhar_tela(matriz_y, matriz_x, matriz):
    '''
        função que desenha a tela do jogo imprimindo uma sequencia de
        linhas de strings com conteúdo da matriz de controle do jogo
    '''
    separador = "\033[90m█\033[0m" * (matriz_x + 2)  # Ajusta o separador para incluir as paredes
    print(separador)
    tela = ''
    for i in range(matriz_y):
        linha = '\033[90m█\033[0m'  # Adiciona a parede esquerda
        for j in range(matriz_x):
            linha += matriz[i][j]
        linha += '\033[90m█\033[0m'  # Adiciona a parede direita
        tela += linha + '\n'
    print(tela, end="")
    print(separador)