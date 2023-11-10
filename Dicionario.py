# Criando Dicionários

dicionario = {}
dicionario = dict
dicionario = {'Nome': 'Ana','Idade':'26','Altura':'1.70'}

print(dicionario['Idade'])
print(dicionario['Nome'])


# Adicionando elementos no dic

dicionario['programador']= True
print(dicionario)


# Iterando sobre um dicionario

for variavel in dicionario:
    print(variavel, dicionario[variavel])

# Testando a existencia de uma chave

print('peso' in dicionario)


# Exemplo de um dicionário
dicionario = {'a': 1, 'b': 2, 'c': 3}

# Loop for para iterar pelas chaves do dicionário
for variavel in dicionario:
    # Imprime a chave e o valor associado a essa chave
    print(variavel, dicionario[variavel])
