import numpy as np

def ler_arquivo(arquivo_txt):
    with open(arquivo_txt, 'r') as f:
        linhas = f.readlines()
    matriz = [list(map(float, linha.split())) for linha in linhas]
    return np.array(matriz, dtype=float)
