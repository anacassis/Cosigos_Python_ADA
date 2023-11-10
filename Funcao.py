# Função
def saudacao():
    print('Seja bem Vindo')
    print('Olá, é um prazer')

saudacao()


# Função com parametro

def saudacao(nome):
    print(f'Seja bem Vindo {nome}')
    print('Olá, é um prazer')

saudacao('Clara')


def saudacao(nome,curso):
    print(f'Seja bem Vindo {nome}')
    print(f'Olá, é um prazer {curso}')

saudacao('Clara','Dados')


# Função com parametros Default

def saudacao(nome,curso='Python'):
    print(f'Seja bem Vindo {nome}')
    print(f'Olá, é um prazer {curso}')

saudacao('Clara',"""'dados'""")


# Função com retorno

def soma(n1, n2):
    return n1 + n2

resultado = soma(5,528)

print(resultado)


def calculadora(n1, n2, operacao = '+'):
    if operacao == '+':
        return n1 + n2
    elif operacao == '-':
        return n1 - n2

res = calculadora( 1,3269,'-')
print(res)