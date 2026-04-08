te = float(input("Quanto tempo vc demorou? (horas): "))
ve = float(input("Qual a valocidade média? (km/h): "))

d = te * ve
lu = d/12

print("Informações recebidas:\n Velocidade - ", ve,"km\n","Tempo - ", te,"h")
print("Litros usados: ", lu)
print("Distancia percorrida: ", d)