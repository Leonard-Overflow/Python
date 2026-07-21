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

        for i in valor:
            if not isinstance(i, tipos_validos[self.tipo_dado]):
                raise ValueError("A coluna possui um tipo invalido")

        self._valores = valor

    @abstractmethod
    def resumo_estatistico(self):
        pass

class ColunaNumerica(ColunaDataset):
    def __init__(self, valores):
        self.valores = valores

    @property
    def tipo_dado(self):
        return "float ou int"

    def resumo_estatistico(self):
        minimo = min(self.valores)
        maximo = max(self.valores)
        media = sum(self.valores) / len(self.valores)

        dict_informacoes = {
            "maximo": maximo,
            "minimo": minimo,
            "media": media,
        }

        return dict_informacoes

class ColunaCatgorica(ColunaDataset):
    def __init__(self, valores):
        self.valores = valores

    @property
    def tipo_dado(self):
        return "str"

    def resumo_estatistico(self):
