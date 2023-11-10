

variavel = 0

for variavel  in range(10):
    print(variavel)
    
    
for variavel  in range(1,10):
    print(variavel)
    

#For com variáveis de 3 em 3
for variavel  in range(1,12,3):
    print(variavel)
    


for i in range(3):
    nota = float(input(f'Digite sua nota{i}: '))
    if i == 0:
        contador = 0
        contador += nota
    else:
        contador += nota
        
print(contador/3)