"""8)- Ler 3 números inteiros e exibir os números que são divisíveis por 2 e 3."""

n1 = float(input("Informe o valor 1: "))
n2 = float(input("Informe o valor 2: "))
n3 = float(input("Informe o valor 3: "))

if n1 % 2 == 0 and n1 % 3 == 0:
    print(n1, "é divisivel por 2 e 3")
else:
    print(n1, "não é divisivel por 2 e 3")

if n2 % 2 == 0 and n2 % 3 == 0:
    print(n2, "é divisivel por 2 e 3")
else:
    print(n2, "não é divisivel por 2 e 3")

if n3 % 2 == 0 and n3 % 3 == 0:
    print(n3, "é divisivel por 2 e 3")
else:
    print(n3, "não é divisivel por 2 e 3")