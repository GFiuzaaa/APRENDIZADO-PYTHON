class Compra():
    def __init__(self, cliente, metodo_pagamento, entrega):
        self.cliente = cliente
        self.metodo_pagamento = metodo_pagamento
        self.entrega = entrega

    def calcular_total(self):
        valor_carrinho = self.cliente.get_carrinho().total()
        valor_frete = self.entrega.calcular_frete()

        return valor_carrinho + valor_frete
    
    def finalizar(self):
        valor_final = self.calcular_total()
        self.metodo_pagamento.pagar(valor_final)
        print("Compra Finalizada")