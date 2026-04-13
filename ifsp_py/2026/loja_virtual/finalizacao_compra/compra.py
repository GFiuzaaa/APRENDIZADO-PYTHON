class Compra():
    def __init__(self, cliente, metodo_pagamento, entrega, estoque):
        self.cliente = cliente
        self.metodo_pagamento = metodo_pagamento
        self.entrega = entrega
        self.estoque = estoque

    def calcular_total(self):
        valor_carrinho = self.cliente.get_carrinho().total()
        valor_frete = self.entrega.calcular_frete()

        return valor_carrinho + valor_frete
    
    def validar(self):
        for i in self.cliente.get_carrinho().get_itens():
            if not self.estoque.tem_estoque(i.produto):
                print(f"{i.produto.nome} nao esta no estoque")
                return False
        return True
    
    def finalizar(self):
        if self.validar():
            valor_final = self.calcular_total()
            self.metodo_pagamento.pagar(valor_final)
            print("Compra Finalizada")
        else:
            print("Nao foi possivel finalizar a compra")