import sys
from simplex.leitor import ler_arquivo
from simplex.simplex_basico import simplex

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 main.py <arquivo_matriz>")
        return
    nome_arquivo = sys.argv[1]
    matriz = ler_arquivo(nome_arquivo)
    simplex(matriz)

if __name__ == "__main__":
    main()
