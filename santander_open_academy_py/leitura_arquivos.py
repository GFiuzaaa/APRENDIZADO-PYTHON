"""Criando e lendo arquivos em Python"""
#leitura de um arquivo

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
