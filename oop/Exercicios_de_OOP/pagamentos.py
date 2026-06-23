from abc import ABC, abstractmethod

class FormaPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass

class CartaoCredito(FormaPagamento):
    def processar_pagamento(self, valor: float):
        print(f"O valor final foi cobrado no cartao de credito. {valor} + {valor*0.05} de taxa")
        return valor*1.05

class Pix(FormaPagamento):
    def processar_pagamento(self, valor: float):
        codigo = "sh821r#%fs$(*h2hqod21hd09h0w11*(*%&$"
        print(f"Copia e cola {codigo}\n")
        return valor*0.9

compra1 = CartaoCredito()
compra2 = Pix()

print("--- Testando Cartão ---")
print(compra1.processar_pagamento(100.0))

print("\n--- Testando Pix ---")
print(compra2.processar_pagamento(100.0))