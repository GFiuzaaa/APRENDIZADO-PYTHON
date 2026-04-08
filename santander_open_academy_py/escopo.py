def funcao():
    variavel_local = "Local"  # Variável local, acessível apenas dentro desta função
    print(variavel_local)  # Acessível dentro da função


variavel_global = "Global"  # Variável global, acessível em todo o programa


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime "Local"
funcao2()  # Imprime "Global"
print(variavel_global)  # Imprime "Global"
#print(variavel_local) - Gera um erro, a variável não está definida neste escopo.
