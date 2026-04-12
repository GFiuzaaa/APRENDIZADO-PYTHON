from pessoas.pessoa import Pessoa
from produtos.carrinho import Carrinho

class Cliente(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha):
        super().__init__(nome, idade, cpf, email, senha)
        self.__carrinho = Carrinho()

    # getter

    def get_carrinho(self):
        return self.__carrinho
