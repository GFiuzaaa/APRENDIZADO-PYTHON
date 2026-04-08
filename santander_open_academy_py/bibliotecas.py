"""Utilizando bibliotecas em Python"""
import math

#Fornece funções matemáticas, como
# sqrt()
# (raiz quadrada),
# sin() (seno)
# cos() (cosseno),
# entre outras.

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

#importando apenas a função sqrt da biblioteca math

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0


import random

#Oferece funções para gerar números aleatórios, como 
#random() (número aleatório entre 0 e 1),
#randint() (número inteiro aleatório em um intervalo),
#entre outras.

x = random.randint(1, 100)
print(x)

#Permite trabalhar com datas e horas, como
#datetime.now() (data e hora atual),
#datetime.date() (data),
#datetime.time() (hora),
#entre outras.

import datetime

data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual
