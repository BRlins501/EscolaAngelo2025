# EXERCÍCIOS

# 1. Na lista pares = [0, 2, 4, 8]
# a) Acrecente o valor 10 ao final da lista.
# b) Acrecente o valor 6 na posição 3.
pares = [0, 2, 4, 8]
pares.append(10)
print(pares)
pares.insert(3, 6)
print(pares)

# 2 Na lista ímpares = [1, 3, 5, 7, 9]
# a) remova o valor 3
# b) Remova o valor da posição (índice) 4
# c) Mostre o valor q será removido da posição (índice)
ímpares = [1, 3, 3, 5, 7, 9]
ímpares.remove(3)
print(ímpares)
valor_removido = ímpares.pop(4)
print(valor_removido)
print(ímpares)

# 3. Na lista Fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
# a) ordene a lista
# b) Coloque o valor reverso na lista Fibonacci
Fibonacci = [8, 1, 0, 5, 13, 1, 3, 2]
Fibonacci.sort()
print(Fibonacci)
Fibonacci.reverse()
print(Fibonacci)

# 4. Na lista pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]
pi = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# a) Busque o elemento que está no índice 5 da lista
print(pi[5])
# b) Imprima o tamanho da lista
print(len(pi))
# c) Imprima o valor máximo da lista
print(max(pi))
# d) Imprima o valor minimo da lista 
print(min(pi))
# e) Imprima apenas o resultado [4, 5 ]
nova_lista = [4, 5]
print(nova_lista)
