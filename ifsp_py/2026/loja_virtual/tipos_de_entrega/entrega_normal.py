from tipos_de_entrega.entrega import Entrega
class Entrega_Normal(Entrega):
    def calcular_frete(self):
        frete = 10
        print(f"O frete é igual a {frete}")
        return frete