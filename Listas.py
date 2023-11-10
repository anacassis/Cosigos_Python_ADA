#antes
nota1 = 7.9
nota2 = 9.8
nota3 = 5.2


#Com Listas

notas = [7.9,9.7,5.2]


# Criando lista

lista = []
lista = list()
lista = ["Carol", '12536','1.2']
lista_de_lista = [10,[1,2,3]]


# Indexação e Slices (Fatiamento)

lista = [10,'Carol',3.154555,True]

print(lista[0])
print(lista[-1])


# Slices

lista2 = [10,50,36,25.35,'oi',23,'é']

print(lista2[0:3])
print(lista2[3:6])
print(lista2[3:])
print(lista2[2:6:3]) #pulando de 2 em 2 mas finaliza na posição 6


# Iteração com for

for elemento in lista : #Para cada elemento ele passa em cada emento da lista 
    print(elemento)
    

# Utilkizando indeces
# quantidade de elementos dentro de uma lista

print(len(lista))

for i in range(len(lista)):
    print(lista[i])
    
    

# > Métodos de Lista 

lista = [ 1, 3, 12, 8, 2 ]


# append sempre no final

lista.append(3)
print(lista)


# insert escolhe qual a posição e o elemento

lista.insert(2,10) # --> primeira a posição depois o valor

print(lista)


# extend juntar listas

lista02 = [1,3,4]

lista.extend(lista02) 

print(lista)


# POP -- Remover elementos (ele é removido o ultimo elemento se voce nao definir a posição)

lista.pop(1)

print(lista)


# Remove -- reemove o valor -- se tiver mais de um valor ele remove o primeiro q encontrar

lista.remove(12)
print(lista)


# Count

print(f'Quantidade de 2 na lista: ', lista.count(2))


# Index

print(f'indice do elemento 12 na lista: ', lista.index(10))
print(lista)


# Sort -- ordena a lista

lista.sort() #ordem decrecente lista.sort(reverse = True)
print(lista)

# > Funções

# Len 

print(len(lista))

#sum

print(sum(lista))

# MAX e MIN

print(min(lista))

print(max(lista))
