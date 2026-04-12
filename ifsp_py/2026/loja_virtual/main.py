from pessoas.cliente import Cliente
from produtos.produto import Produto
from metodos_de_pagamento.cartao_credito import Cartao_Credito
from tipos_de_entrega.entrega_expressa import Entrega_Expressa
from finalizacao_compra.compra import Compra

fiuza = Cliente("Guilherme Fiuza", 16, "123456789" , "fiuza@gmail .com", "12345678")


mouse = Produto("Mouse", "mouse confortavel e sem fio", 100)
mouse.mostrar()

teclado = Produto("Teclado", "teclado RGB e mecanico", 200)
teclado.mostrar()

monitor = Produto("Monitor", "monitor 24 polegadas 144hz", 550)
monitor.mostrar()

fiuza.get_carrinho().adicionar(teclado, 2)
fiuza.get_carrinho().adicionar(mouse, 1)
fiuza.get_carrinho().adicionar(monitor, 3)

fiuza.get_carrinho().remover(teclado, 1)
fiuza.get_carrinho().remover(mouse)

pagamento = Cartao_Credito()
entrega = Entrega_Expressa()

nova_compra = Compra(fiuza, pagamento, entrega)
nova_compra.finalizar()
