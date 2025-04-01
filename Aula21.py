# EXERCÍCIOS DE FIXAÇÃO

# 1. adicione o número 50 ao final da lista
lista_numero = [10, 20, 30, 40]
lista_numero.append(50)
print(lista_numero)

# 2. Adicione "laranja" ao índice 1 na lista
lista_fruta = ["maça", "banana", "uva"]
lista_fruta.insert(1, "laranja")
print(lista_fruta)

# 3. remova "cachorro" da lista
lista_animais = ["cachorro", "gato", "pássaro", "cachorro"]
lista_animais.remove("cachorro")
print(lista_animais)

# 4. Remova o elemento de índice 2 da lista e mostre o elemento removido
lista_nomes = ["Alice", "Bob", "Charlie", "David"]
valor_removido = lista_nomes.pop (2)
print(lista_nomes)
print(valor_removido)

# 5. Econtre o índice da primeira ocorreência de 'azul' na lista
lista_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'azul']
índice_azul = lista_cores.index('azul')
print(índice_azul)

# 6. Conte quantas vezes o numero 2 aparece na lista
lista_numero_repetidos = [1, 2, 3, 2, 4, 2, 5, 2]
quantidade_de_dois = lista_numero_repetidos.count(2)
print(quantidade_de_dois)

# 7. Ordene a lista em ordem crecente
lista_desordenada = [50, 20, 80, 10, 40]
lista_desordenada.sort()
print(lista_desordenada)


