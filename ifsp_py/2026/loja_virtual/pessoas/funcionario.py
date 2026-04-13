from pessoas.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha):
        super().__init__(nome, idade, cpf, email, senha)
        self._ativo = True

    def ativar(self):
        self._ativo = True
        print("Funcionario ativo!")

    def desativar(self):
        self._ativo = False
        print("Funcionario desativado!")

    def esta_ativo(self):
        return self._ativo