from metodos_de_pagamento.metodo_pagamento import Metodo_Pagamento

class Cartao_Credito(Metodo_Pagamento):
    def pagar(self, valor):
        print(f"Cliente pagou R$ {valor} via cartao de credito")
