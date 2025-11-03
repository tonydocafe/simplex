import numpy as np

def ler_arquivo(caminho):
    with open(caminho, 'r') as f:
        linhas = [l.strip() for l in f.readlines() if l.strip()]

    tipo = linhas[0].lower()  #max ou min
    c = np.array(list(map(float, linhas[1].split())))

    A, b, sinais = [], [], []
    for linha in linhas[2:]:
        partes = linha.split()
        *coef, sinal, valor = partes
        A.append(list(map(float, coef)))
        sinais.append(sinal)
        b.append(float(valor))

    return tipo, np.array(A), np.array(b), sinais, c
