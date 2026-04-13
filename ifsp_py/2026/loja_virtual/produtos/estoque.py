from produtos.produto_compra import Produto_Compra

class Estoque():
    def __init__(self):
        self.__itens = []

    def validar_funcionario(self, funcionario):
        if funcionario.esta_ativo is False:
            return False
        else:
            return True
        
    def tem_estoque(self, produto):
        for i in self.__itens:
            if i.produto.nome == produto.nome:
                return True
        return False


    def adicionar_estoque(self, funcionario, produto, quantidade):
        if self.validar_funcionario(funcionario):
            for i in self.__itens:
                if i.produto.nome == produto.nome:
                    i.quantidade+= quantidade
                    return
            item = Produto_Compra(produto, quantidade)
            self.__itens.append(item)
        else:
            print("Funcionario nao esta ativo, volte mais tarde")

    def remover_estoque(self, funcionario, produto, quantidade):      
        if self.validar_funcionario(funcionario) and self.tem_estoque(produto) is True:
            for i in self.__itens:
                if i.produto.nome == produto.nome:
                    if quantidade is None:
                        self.__itens.remove(i)    
                    else:
                        i.quantidade -= quantidade

                        if i.quantidade <= 0:
                            self.__itens.remove(i)
                    break
        else:
            print("Item nao esta no estoque")
    def limpar_estoque(self, funcionario):
        if self.validar_funcionario(funcionario):
            self.__itens.clear()

    def mostrar(self):
        if len(self.__itens) == 0:
            print("Estoque nao contem nada")
            return False
        
        print("\nEstoque contem:\n")
        for i in self.__itens:
            print(f"Item: {i.produto.nome} - Quantidade: {i.quantidade}")
        print("\n")