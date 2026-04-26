from utils.matrizes import ( criar_matriz_aleatoria, somar_matrizes, medias_por_linha, calcular_determinante, transpor_e_multiplicar)


def exibir_matriz(titulo: str, matriz: list) -> None:
    print(f"\n{titulo}")
    for linha in matriz:
        print(" ", linha)

def main():


    print("\n1. Matriz 3x3 preenchida com números aleatórios:")
    matriz_aleatoria = criar_matriz_aleatoria(3, 3)
    exibir_matriz("Matriz aleatória:", matriz_aleatoria)


    vendas_semana1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    vendas_semana2 = [[5, 15, 25], [35, 45, 55], [65, 75, 85]]
    total_vendas = somar_matrizes(vendas_semana1, vendas_semana2)
    exibir_matriz("2. Semana 1:", vendas_semana1)
    exibir_matriz("     Semana 2:", vendas_semana2)
    exibir_matriz("     Total (soma):", total_vendas)


    notas_alunos = [
        [8.5, 7.0, 9.0, 6.5],
        [6.0, 8.5, 7.5, 9.0],
        [5.5, 6.5, 7.0, 8.0],
    ]
    medias = medias_por_linha(notas_alunos)
    exibir_matriz("3. Notas dos alunos:", notas_alunos)
    print("\n  Médias por aluno:")
    for i, media in enumerate(medias, start=1):
        print(f"    Aluno {i}: {media:.2f}")


    coeficientes = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    det = calcular_determinante(coeficientes)
    exibir_matriz("4. Matriz de coeficientes:", coeficientes)
    print(f"\n  Determinante: {det:.2f}")
    if det != 0:
        print(" Sistema tem solução única (det ≠ 0).")
    else:
        print("Sistema não tem solução única (det = 0).")


    estoque = [[10, 20], [5, 15]]
    precos = [[2.0], [3.0]]
    totais = transpor_e_multiplicar(estoque, precos)
    exibir_matriz("5. Estoque (2 produtos x 2 períodos):", estoque)
    exibir_matriz("     Preços por período:", precos)
    exibir_matriz("     Totais (transposta × preços):", totais)


if __name__ == "__main__":
    main()