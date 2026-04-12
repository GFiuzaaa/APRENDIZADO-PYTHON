from tipos_de_entrega.entrega import Entrega
class Entrega_Expressa(Entrega):
    def calcular_frete(self):
        frete = 25
        print(f"O frete é igual a {frete}")
        return frete