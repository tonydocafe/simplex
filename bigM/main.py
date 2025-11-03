import sys
from leitor import ler_arquivo
from m_grande import resolver

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 main.py entrada.txt")
        return

    tipo, A, b, sinais, c = ler_arquivo(sys.argv[1])

    resultado = resolver(tipo, A, b, sinais, c, metodo="m-grande")

    if resultado.success:
        print("\n✅ Solução encontrada:")
        print("x =", resultado.x)
        print("Valor ótimo =", -resultado.fun if tipo == "max" else resultado.fun)
    else:
        print("\n❌ Problema não resolvido:", resultado.message)

if __name__ == "__main__":
    main()
