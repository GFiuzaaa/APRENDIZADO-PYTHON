"""Exemplo de tratamento de exceções em Python"""

try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")

#except

try:
    # Código que pode gerar uma exceção
    numero = int("abc")  # Valor inválido para conversão
    resultado = 10 / 0  # Divisão por zero
    print(resultado)

except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")


#finally: bloco de código que sempre será executado,
#independentemente de ocorrer ou não uma exceção.

arquivo = None
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    if arquivo:
        arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção


#exceção personalizada: é possível criar suas próprias 
# classes de exceção para lidar com situações específicas em seu código.

def funcao():
    numero = -1

    if numero < 0:
        raise Exception("Número não pode ser negativo")

try:
    funcao()
except Exception as e:
    print(f"Erro: {e}")
