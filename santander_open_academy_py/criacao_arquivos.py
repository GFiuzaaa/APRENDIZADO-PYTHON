"""Arquivo com exemplo de leitura e escrita em arquivos em Python"""

#criacao e escrita em um arquivo
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()
arquivo = open("dados.txt", "r")

