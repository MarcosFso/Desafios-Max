
import numpy as np


# EXEMPLO 1 - Sistema 2x2



print("EXEMPLO 1 - Sistema 2x2")
# Define a matriz dos coeficientes A e o vetor B
A = np.array([[2, 3], [4, -1]])
B = np.array([8, 7])

# Verifica o determinante para garantir que A é invertível
det = np.linalg.det(A)
print(f"Determinante de A: {det:.2f}")

# Calcula a inversa de A
try:
    A_inversa = np.linalg.inv(A)

    # Calcula X = A⁻¹ * B
    X = np.dot(A_inversa, B)

    # Exibe a solução
    print("\nSolução do sistema:")
    print(f"x = {X[0]:.2f}")
    print(f"y = {X[1]:.2f}")

    # Verificação
    print("\nVerificação:")
    print(f"2x + 3y = 2({X[0]:.2f}) + 3({X[1]:.2f}) = {2*X[0] + 3*X[1]:.2f}")
    print(f"4x - y = 4({X[0]:.2f}) - {X[1]:.2f} = {4*X[0] - X[1]:.2f}")
except np.linalg.LinAlgError:
    print("Erro: A matriz A é singular (não invertível).")





# EXEMPLO 2 - Sistema 3x3

print("EXEMPLO 2 - Sistema 3x3")
# Define a matriz dos coeficientes A e o vetor B
A = np.array([[2, 1, 2], [1, 2, 3], [3, 1, 4]])
B = np.array([7, 7, 11])

# Verifica o determinante para garantir que A é invertível
det = np.linalg.det(A)
print(f"Determinante de A: {det:.2f}")

# Resolve o sistema diretamente
try:
    X = np.linalg.solve(A, B)

    # Taxas de produção
    x = X[0]  # Itens por trabalhador
    y = X[1]  # Itens por máquina
    z = X[2]  # Itens por hora

    # Exibe a solução
    print("\nTaxas de produção:")
    print(f"x = {x:.2f} itens por trabalhador")
    print(f"y = {y:.2f} itens por máquina")
    print(f"z = {z:.2f} itens por hora")

    # Calcula produção com 4 trabalhadores, 2 máquinas e 3 horas
    producao = 4 * x + 2 * y + 3 * z
    print(f"\nProdução com 4 trabalhadores, 2 máquinas e 3 horas: {producao:.2f} itens")

    # Verificação
    print("\nVerificação:")
    print(f"2x + y + 2z = 2({x:.2f}) + {y:.2f} + 2({z:.2f}) = {2*x + y + 2*z:.2f}")
    print(f"x + 2y + 3z = {x:.2f} + 2({y:.2f}) + 3({z:.2f}) = {x + 2*y + 3*z:.2f}")
    print(f"3x + y + 4z = 3({x:.2f}) + {y:.2f} + 4({z:.2f}) = {3*x + y + 4*z:.2f}")
except np.linalg.LinAlgError:
    print("Erro: A matriz A é singular (não invertível).")





# DESAFIO - ENTRADA DO USUÁRIO

print("DESAFIO - Entrada do Usuário")
# Inicializa a matriz A e o vetor B
A = []
B = []

# Lê a matriz A (3x3)
print("Digite os coeficientes da matriz A (3x3):")
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

# Lê o vetor B (3x1)
print("\nDigite os termos independentes (B):")
for i in range(3):
    valor = float(input(f"B[{i}]: "))
    B.append(valor)

# Converte para arrays NumPy
A = np.array(A)
B = np.array(B)

# Verifica se a matriz é invertível
try:
    if np.abs(np.linalg.det(A)) < 1e-10:  # Determinante próximo de zero
        print("Erro: A matriz A não é invertível (determinante zero). O sistema não tem solução única.")
    else:
        # Resolve o sistema
        X = np.linalg.solve(A, B)

        # Exibe a matriz A
        print("\nMatriz A:")
        for i in range(3):
            for j in range(3):
                print(f"{A[i][j]:.0f}", end=" ")
            print()

        # Exibe o vetor B
        print("\nVetor B:")
        print(B)

        # Exibe a solução
        print("\nSolução:")
        print(f"x = {X[0]:.2f}")
        print(f"y = {X[1]:.2f}")
        print(f"z = {X[2]:.2f}")
except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular ou mal-condicionada).")





# EXERCÍCIO 1 - Produção com 2 recursos

print("EXERCÍCIO 1 - Produção com 2 recursos")
# Define a matriz dos coeficientes A e o vetor B
A = np.array([[5, 3], [8, 2]])
B = np.array([110, 100])

# Resolve o sistema
X = np.linalg.solve(A, B)

# Taxas de produção
x = X[0]  # Itens por trabalhador
y = X[1]  # Itens por máquina

# Exibe a solução
print("Taxas de produção:")
print(f"x = {x:.2f} itens por trabalhador por dia")
print(f"y = {y:.2f} itens por máquina por dia")

# Calcula produção com 10 trabalhadores e 4 máquinas
producao = 10 * x + 4 * y
print(f"\nProdução com 10 trabalhadores e 4 máquinas: {producao:.2f} itens")

# Verificação
print("\nVerificação:")
print(f"5x + 3y = 5({x:.2f}) + 3({y:.2f}) = {5*x + 3*y:.2f}")
print(f"8x + 2y = 8({x:.2f}) + 2({y:.2f}) = {8*x + 2*y:.2f}")





# EXERCÍCIO 2 - Produção com 3 recursos

print("EXERCÍCIO 2 - Produção com 3 recursos")
# Define a matriz dos coeficientes A e o vetor B
A = np.array([[4, 2, 3], [3, 3, 2], [5, 1, 4]])
B = np.array([150, 140, 160])

# Verifica se a matriz é invertível
try:
    det = np.linalg.det(A)
    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante zero).")
    else:
        # Resolve o sistema
        X = np.linalg.solve(A, B)

        # Taxas de produção
        x = X[0]  # Itens por trabalhador
        y = X[1]  # Itens por máquina
        z = X[2]  # Itens por hora

        # Exibe a matriz A
        print("Matriz A:")
        for i in range(3):
            for j in range(3):
                print(f"{A[i][j]:.0f}", end=" ")
            print()

        # Exibe o vetor B
        print("\nVetor B:")
        print(B)

        # Exibe a solução
        print("\nTaxas de produção:")
        print(f"x = {x:.2f} itens por trabalhador")
        print(f"y = {y:.2f} itens por máquina")
        print(f"z = {z:.2f} itens por hora")

        # Calcula produção com 6 trabalhadores, 3 máquinas e 5 horas
        producao = 6 * x + 3 * y + 5 * z
        print(f"\nProdução com 6 trabalhadores, 3 máquinas e 5 horas: {producao:.2f} itens")

        # Verificação
        print("\nVerificação:")
        print(f"4x + 2y + 3z = 4({x:.2f}) + 2({y:.2f}) + 3({z:.2f}) = {4*x + 2*y + 3*z:.2f}")
        print(f"3x + 3y + 2z = 3({x:.2f}) + 3({y:.2f}) + 2({z:.2f}) = {3*x + 3*y + 2*z:.2f}")
        print(f"5x + y + 4z = 5({x:.2f}) + {y:.2f} + 4({z:.2f}) = {5*x + y + 4*z:.2f}")
except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular).")





# EXERCÍCIO 3 - Padaria

print("EXERCÍCIO 3 - Padaria")
# Define a matriz dos coeficientes A e o vetor B (para farinha)
A = np.array([[50, 20], [30, 30]])
B = np.array([30, 12])

# Verifica se a matriz é invertível
try:
    det = np.linalg.det(A)
    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante zero).")
    else:
        # Resolve o sistema
        X = np.linalg.solve(A, B)

        # Quantidades
        x = X[0]  # kg de farinha por pão
        y = X[1]  # kg de açúcar por bolo

        # Exibe a solução
        print("Quantidades por unidade:")
        print(f"x = {x:.2f} kg de farinha por pão")
        print(f"y = {y:.2f} kg de açúcar por bolo")

        # Calcula consumo para 40 pães e 25 bolos
        farinha = 40 * x + 25 * y
        acucar = 40 * x + 25 * y  # Supondo mesma proporção para simplificação
        print(f"\nConsumo para 40 pães e 25 bolos:")
        print(f"Farinha: {farinha:.2f} kg")
        print(f"Açúcar: {acucar:.2f} kg")

        # Verificação
        print("\nVerificação:")
        print(f"50x + 20y = 50({x:.2f}) + 20({y:.2f}) = {50*x + 20*y:.2f}")
        print(f"30x + 30y = 30({x:.2f}) + 30({y:.2f}) = {30*x + 30*y:.2f}")
except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular).")





# EXERCÍCIO 4 - Mistura Química

print("EXERCÍCIO 4 - Mistura Química")
# Define a matriz dos coeficientes A e o vetor B (para ingrediente X)
A = np.array([[60, 40], [50, 30]])
B = np.array([26, 20])

# Verifica se a matriz é invertível
try:
    det = np.linalg.det(A)
    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante zero).")
    else:
        # Resolve o sistema
        X = np.linalg.solve(A, B)

        # Quantidades
        x = X[0]  # Unidades de X por litro de A
        y = X[1]  # Unidades de X por litro de B

        # Exibe a solução
        print("Quantidades de ingrediente X:")
        print(f"x = {x:.2f} unidades por litro de A")
        print(f"y = {y:.2f} unidades por litro de B")

        # Calcula unidades de X para 70 litros de A e 50 litros de B
        unidades_x = 70 * x + 50 * y
        print(f"\nUnidades de X em 70 litros de A e 50 litros de B: {unidades_x:.2f} unidades")

        # Verificação
        print("\nVerificação:")
        print(f"60x + 40y = 60({x:.2f}) + 40({y:.2f}) = {60*x + 40*y:.2f}")
        print(f"50x + 30y = 50({x:.2f}) + 30({y:.2f}) = {50*x + 30*y:.2f}")
except np.linalg.LinAlgError:
    print("Erro: Não foi possível resolver o sistema (matriz singular).")