"""4)- Ler três valores para os lados de um triangulo, considerando lados como: A, B e C.
Verificar se os lados fornecidos formam realmente um triangulo, e se essa condição for
verdadeira, indicar qual o tipo do triangulo formado: isósceles, escaleno ou equilátero.
Triangulo é uma forma geométrica (polígono) composta de 3 lados, onde cada lado é
menor que a soma dos dois outros lados.
REGRA BÁSICA: Será um triangulo quando A<B+C, quando B<A+C e quando C<A+B.
Um triangulo é isósceles quando possui 2 lados iguais e um diferente, sendo A==B ou
A==C ou B==C; é escaleno quando possui todos os lados diferentes, sendo A<>B e
B<>C e é equilátero quando possui todos os lados iguais, sendo A==B e B==C.
Ler 3 valores para os lados de um triangulo: A, B e C.
Verificar se cada lado é menor que a soma dos dois outros lados. Se sim, saber se A=B
e se B=C, sendo verdade exibir, o triangulo é equilátero, se não verificar A=B ou se
A=C ou se B=C, sendo verdade exibir o triangulo é isósceles, caso contrário, o
triangulo é escaleno.
Caso os lados não se caracterizem um triangulo, exibir mensagem informando a
ocorrência."""""

A = float(input("Informe o valor do 1o lado: "))
B = float(input("Informe o valor da 2o lado: "))
C = float(input("Informe o valor da 3o lado: "))

if A<B+C and B<A+C and C<A+B:
    if A==B or A==C or B==C:
        print("É isósceles")
    elif  A == B and B ==C:
        print("É equilatero")
    else:
        print("É escaleno")
else:
    print("Não é triângulo")