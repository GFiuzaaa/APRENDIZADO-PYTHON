nc = 20
n = int(input("Numero digitado: "))

if n <= nc:
    n = nc - n
else:
    n = n - nc

if n >= 0:
    print("Reposta: ", n)