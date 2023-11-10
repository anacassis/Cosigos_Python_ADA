idade = int(input('Qual sua idade? '))

if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você nao é maior de idade')
    
    
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2
print(media)

if media >= 7:
    print('Você foi aprovado')
elif media >= 4 and media <=6:
    print('Recuperação')
else: 
    print('Reprovado')