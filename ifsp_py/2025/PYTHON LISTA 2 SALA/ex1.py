"""1- Ler 3 valores referentes a 3 notas de um aluno e exibir uma mensagem dizendo que
ele foi aprovado, se o valor da média for maior ou igual a 6.0. Se o aluno não foi
aprovado, exibir mensagem informando essa condição. Exibir junto com uma das
mensagens, o valor da média para qualquer condição."""""


n1 = float(input("Informe o valor da 1a prova: "))
n2 = float(input("Informe o valor da 2a prova: "))
n3 = float(input("Informe o valor da 3a prova: "))

me = (n1 + n2 + n3) / 3


if me >= 6.0:
    print("Voce foi aprovado! Media: '%.2f'" %(me))
else:
    print("Voce foi reprovado! Media: '%.2f'" %(me))
