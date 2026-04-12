from pessoas.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, email, senha, cargo):
        super().__init__(nome, idade, cpf, email, senha)
        self.cargo = cargo #variavel criada para evitar o erro: "Useless parent or super() delegation in method __init__"

