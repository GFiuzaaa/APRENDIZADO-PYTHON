from metodos_de_pagamento.metodo_pagamento import Metodo_Pagamento

class Boleto(Metodo_Pagamento):
    def pagar(self, valor):
        print(f"Cliente pagou R$ {valor} via Boleto")
