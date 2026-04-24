# Aula sobre Listas em Python
# Objetivo: Ensinar os conceitos de listas, iteração, operações e empilhamento

# 1. O que é uma lista?
# Uma lista em Python é uma estrutura de dados ordenada e mutável que pode conter elementos de diferentes tipos (números, strings, outras listas, etc.).
# Sintaxe: lista = [elemento1, elemento2, elemento3]

# Exemplo 1: Criando e exibindo listas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misturado = [1, "texto", 3.14, True]
print("Lista de frutas:", frutas)
print("Lista de números:", numeros)
print("Lista misturada:", misturado)

# 2. Acessando elementos de uma lista
# Usa-se índices (começando do 0) para acessar elementos.
# Índices negativos acessam elementos do final para o início (-1 é o último elemento).

# Exemplo 2: Acessando elementos
print("\nAcessando elementos:")
print("Primeira fruta:", frutas[0])  # maçã
print("Última fruta:", frutas[-1])  # laranja
print("Sublista:", numeros[1:4])   # [2, 3, 4]

# 3. Iterando sobre listas
# Pode-se usar loops (for ou while) para percorrer os elementos de uma lista.

# Exemplo 3: Iterando com for
print("\nIterando com for:")
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Exemplo 4: Iterando com while
print("\nIterando com while:")
indice = 0
while indice < len(frutas):
    print(f"Fruta no índice {indice}: {frutas[indice]}")
    indice += 1

# 4. Operações com listas
# Listas suportam várias operações, como adicionar, remover, concatenar e modificar elementos.

# Exemplo 5: Operações básicas
print("\nOperações com listas:")
# Adicionar elemento
frutas.append("morango")
print("Após append:", frutas)

# Remover elemento
frutas.remove("banana")
print("Após remove:", frutas)

# Modificar elemento
frutas[1] = "kiwi"
print("Após modificação:", frutas)

# Concatenar listas
nova_lista = frutas + ["uva", "manga"]
print("Após concatenação:", nova_lista)

# 5. Empilhamento (usando listas como pilhas)
# Uma pilha é uma estrutura LIFO (Last In, First Out). Em Python, listas podem ser usadas como pilhas com append() e pop().

# Exemplo 6: Implementando uma pilha
print("\nExemplo de pilha:")
pilha = []
pilha.append(1)  # Empilhar
pilha.append(2)
pilha.append(3)
print("Pilha após empilhar:", pilha)

# Desempilhar
ultimo = pilha.pop()
print("Elemento desempilhado:", ultimo)
print("Pilha após desempilhar:", pilha)

# 6. Outras operações úteis
# - len(): retorna o tamanho da lista
# - in: verifica se um elemento está na lista
# - sort(): ordena a lista
# - reverse(): inverte a ordem da lista

# Exemplo 7: Operações adicionais
print("\nOutras operações:")
numeros = [5, 2, 8, 1, 9]
print("Tamanho da lista:", len(numeros))
print("Contém 8?", 8 in numeros)
numeros.sort()
print("Lista ordenada:", numeros)
numeros.reverse()
print("Lista invertida:", numeros)

# 7. Listas aninhadas
# Listas podem conter outras listas, úteis para matrizes ou estruturas complexas.

# Exemplo 8: Lista aninhada
print("\nLista aninhada:")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento [1][2]:", matriz[1][2])  # 6

# 8. Compreensão de listas (List Comprehension)
# Uma forma concisa de criar listas a partir de iterações.

# Exemplo 9: List comprehension
print("\nList comprehension:")
quadrados = [x**2 for x in range(1, 6)]
print("Quadrados de 1 a 5:", quadrados)