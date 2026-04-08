a = int(input("numero 1: "))
b = int(input("numero 2: "))
c = int(input("numero 3: "))


if a>c and a>b:
    maior=a
elif b>a and b>c:
    maior=b
else: 
    maior=c

if a<c and a<b:
    menor=a
elif b<a and b<c:
    menor=b
else: 
    menor=c

meio=(a+b+c)-maior-menor

print("Maior: ", maior, "\nMenor: ", menor, "\nMeio: ", meio)