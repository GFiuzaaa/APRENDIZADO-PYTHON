"""Arquivo com exemplos de listas de compressão"""

n = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in n if x % 2 == 0]
print(quadrados)
