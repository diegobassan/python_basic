# Criacao da lista
lista = [1, 2, 3, 4]

# Acessar Lista
print (lista)

# Ultimo elemento da lista, passar menos um
print (lista[-1])

# Tamanho da lista
print (len(lista))

# Unir duas listas
lista2 = [5, 6, 7, 8]
lista.extend(lista2)
print (lista)

# Inserir elemento na lista
lista.append(9)

# Inserir elemento em uma posicao na lista
lista.insert(0, 'Zero')
print (lista)
