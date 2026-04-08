"""Arquivo com eemplo de função"""

def multiplicacao(a, b):
    """Função que multiplica dois números"""
    return a * b

def soma(a, b):
    """Função que soma dois números"""
    return a + b

def subtracao(a, b):
    """Função que subtrai dois números"""
    return a - b

def divisao(a, b): 
    """Função que divide dois números"""
    return a/b


print(multiplicacao(5, 6))
print(soma(10, 5))
print(subtracao(50, 30))
print(divisao(40, 4))


#lambda: função anônima, ou seja, sem nome.
# É usada para criar funções simples e rápidas,
# geralmente em uma única linha de código.

soma_lambda = lambda x, y: x + y
print(soma_lambda(3, 4))
