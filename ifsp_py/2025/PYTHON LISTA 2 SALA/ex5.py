"""5)- Ler 3 valores (A, B e C) e exibir os valores dispostos em ordem crescente."""

n1 = float(input("Informe o valor 1: "))
n2 = float(input("Informe o valor 2: "))
n3 = float(input("Informe o valor 3: "))

ord = sorted(n1, n2, n3)

print("Valores ordenados: ", ord)