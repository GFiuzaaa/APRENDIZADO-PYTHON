v = float(input("Informe o valor:  "))
ta = float(input("Informe a taxa: "))
te = float(input("Informe o tempo"))

p = v + (v * (ta/100) * te)

print("Prestação a ser paga: ", p)