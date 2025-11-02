import numpy as np

def simplex(matriz):
    matriz[0, :-1] *= -1
    numLinhas, numColunas = matriz.shape
    numVariaveis = numColunas - 1
    iteracao = 0

    while True:
        print(f"\n=== ITERACAO {iteracao} ===")
        print(matriz)
        z = matriz[0, :-1]
        if all(c <= 0 for c in z):
            print("\n✅ Solucao otima encontrada!")
            break

        variavelEntrando = next(i for i, v in enumerate(z) if v == max(z))

        print(f"➡️ Variavel que entra: x{variavelEntrando + 1}")
        cPivo = matriz[1:, variavelEntrando]
        termosB = matriz[1:, -1]
        razoes = []
        for i in range(len(cPivo)):
            if cPivo[i] > 0:
                razoes.append(termosB[i] / cPivo[i])
            else:
                razoes.append(np.inf)

        menor = min(r for r in razoes if r != np.inf)
        indices = [i for i, r in enumerate(razoes) if r == menor]
        linhaPivoIdx = indices[0] + 1 

        print(f"↩️ Variavel que sai: linha {linhaPivoIdx}")
        pivo = matriz[linhaPivoIdx, variavelEntrando]
        matriz[linhaPivoIdx, :] /= pivo

        for i in range(numLinhas):
            if i != linhaPivoIdx:
                fator = matriz[i, variavelEntrando]
                matriz[i, :] -= fator * matriz[linhaPivoIdx, :]

        iteracao += 1
    print("\n=== MATRIZ FINAL ===")
    print(matriz)
    print("\n=== SOLUCAO ===")
    base = []
    for j in range(numVariaveis):
        coluna = matriz[:, j]
        if np.count_nonzero(coluna[1:]) == 1 and coluna[0] == 0:
            i = np.where(coluna == 1)[0][0]
            base.append((f"x{j+1}", matriz[i, -1]))
        else:
            base.append((f"x{j+1}", 0.0))

    for var, val in base:
        print(f"{var} = {val}")
    print(f"Z = {matriz[0, -1]}")
