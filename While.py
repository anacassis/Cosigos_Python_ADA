import random

numero = random.randint(1,5)

numero_esco = int(input('Qual numero de 1 até 100 você escolhe? '))

while numero_esco != numero:
    
    numero_esco = int(input('Qual numero de 1 até 100 você escolhe? '))
    
    while numero_esco > 100:
        print("Digite novamente: ")
        numero_esco = int(input('Qual numero de 1 até 100 você escolhe? '))
    else:
        numero = random.randint(1,5)
        print(f'Seu numero foi {numero_esco} e o correto era {numero}')

print("Você acerto !!") 


#Contador 

contador = 0

while contador <9:
    print(contador)
    contador += 1