class Produto:
    def __init__(self, nome, descricao, preco_unitario):
        self.nome = nome
        self.descricao = descricao
        self.preco_unitario = preco_unitario
    
    def mostrar(self):
        print(f"O produto {self.nome} é um(a) {self.descricao} e custa {self.preco_unitario}")
        