"""6)- Ler 3 valores (A, B e C) e calcular a equação de segundo grau, exibindo as duas
raízes, se para os valores informados for possível efetuar o referido cálculo."""

n1 = float(input("Informe o valor 1: "))
n2 = float(input("Informe o valor 2: "))
n3 = float(input("Informe o valor 3: "))

ord = sorted([n1, n2, n3], reverse = True)

print("Valores ordenados: ", ord)