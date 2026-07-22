from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @property
    @abstractmethod
    def taxa_percentual(self) -> float:
        """Cada metodo de pagamento tem uma fixa definida em sua subclasse"""
        pass

    def calcular_valor_final(self, valor: float) -> float:
        return valor*(self.taxa_percentual/100)

class Pix(MetodoPagamento):
    @property
    def taxa_percentual(self) -> float:
        return 0

class CartaoCredito(MetodoPagamento):
    @property
    def taxa_percentual(self) -> float:
        return 3.5

class Boleto(MetodoPagamento):
    @property
    def taxa_percentual(self) -> float:
        return 1.2

pix = Pix()
# pix.taxa_percentual = 5 Nao funciona, pois nao tem setter

# metodo = MetodoPagamento() Nao funciona, pois e impossivel instanciar interfaces