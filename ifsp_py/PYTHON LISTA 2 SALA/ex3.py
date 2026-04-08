"""3)- Ler dois valores numéricos e exibir a diferença do maior para o menor."""

n1 = float(input("Informe o valor do 1o valor: "))
n2 = float(input("Informe o valor da 2o valor: "))

if n1 > n2:
    print("N1 é maior, diferença: ", n1-n2)
else:
    print("N2 é maior, Diferença: ", n2-n1)