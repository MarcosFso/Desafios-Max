from utils.random_matrix import metodo_random, metodo_numpy


def main():
    # Imprime a matriz gerada pelo método random
    print("Método 1 — random nativo:")
    matriz = metodo_random()
    for linha in matriz:
        print(linha)

    # Imprime a matriz gerada pelo método NumPy
    print("\nMétodo 2 — NumPy:")
    matriz = metodo_numpy()
    print(matriz)


if __name__ == "__main__":
    main()