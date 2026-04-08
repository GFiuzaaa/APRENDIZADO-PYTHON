"""7)- Ler um valor inteiro positivo ou negativo e exibir o número lido como sendo um valor
positivo, ou seja, o programa devera exibir o modulo de um número fornecido. 
Lembrese de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1."""

n = int(input("Digite o numero: "))

if n < 0:
    print("Modulo: ", n*-1)
else:
    print("Modulo: ", n)