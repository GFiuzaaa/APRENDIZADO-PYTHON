from produtos.produto_compra import Produto_Compra

class Carrinho():
    def __init__(self):
        self.__itens = []

    def adicionar(self, produto, quantidade):
        item = Produto_Compra(produto, quantidade)
        self.__itens.append(item)

    def remover(self, produto, quantidade = None):
        
        for i in self.__itens:
            if i.produto.nome == produto.nome:
                if quantidade is None:
                    self.__itens.remove(i)
        
                else:
                    i.quantidade -= quantidade

                    if i.quantidade <= 0:
                        self.__itens.remove(i)
        
                break

    def limpar(self):
        self.__itens.clear()
    
    def total(self):
        valor_total = 0

        for i in self.__itens:
            valor_total += i.subtotal()
        return valor_total

    def mostrar(self):
        print("\nSeu Carrinho contem:\n")
        for i in self.__itens:
            print(f"Item: {i.produto.nome} - Quantidade: {i.quantidade}")
        print("\n")

    
    def get_itens(self):
        return self.__itens
    