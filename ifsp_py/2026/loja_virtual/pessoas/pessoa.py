from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, idade, cpf, email, senha):
        self._nome = nome
        self._idade = idade
        self.__cpf = cpf
        self._email = email
        self.__senha = senha

    # getters

    def get_cpf(self):
        return self.__cpf
    
    def get_senha(self):
        return self.__senha
    
    # setters

    def set_cpf(self, num_cpf):
        if(len(num_cpf) <= 0 or len(num_cpf) == 11):
            print(f"O cpf deve conter 11 digitos, o seu possui: {num_cpf}")
        else:
            self.__cpf = num_cpf

    def set_senha(self, num_senha):
        if(len(num_senha < 0)):
            print("Sua senha está sem caracteres, digite novamente:")
        else:
            self.__senha = num_senha
    