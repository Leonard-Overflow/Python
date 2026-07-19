from abc import ABC, abstractmethod

class ColunaDataset(ABC):
    """
    Representa a interface que uma coluna de um dataset deve seguir
    """

    @property
    @abstractmethod
    def tipo_dado(self):
        pass

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, valor):
        tipos_validos = {
            "int": int,
            "float": float,
            "str": str
        }
        tipo = self.tipo_dado

        for i in valor:
            if not isinstance(i, tipos_validos[tipo]):
                raise ValueError("A coluna possui um tipo invalido")

        self._valores = valor