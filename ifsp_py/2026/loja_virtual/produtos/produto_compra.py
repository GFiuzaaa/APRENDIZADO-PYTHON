class Produto_Compra:
    def __init__(self, produto, quantia):
        self.produto = produto
        self.quantidade = quantia

    def subtotal(self):
        return self.produto.preco_unitario * self.quantidade
