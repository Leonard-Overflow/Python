from abc import ABC, abstractmethod

"""
Heidelbergensis = Interface(o que todas as especies descendentes vao ter)
Sapiens, Neanderthalenesis, Denisovensis(especie que segue o ancestral, mas com adicao de algo)
"""

class Heidelbergensis(ABC):
    def __init__(self, cerebro, bipedalismo: bool, anatomia_das_maos):
        self.cerebro_grande = cerebro
        self.bipedalismo = bipedalismo
        self.anatomia_das_maos = anatomia_das_maos

    @abstractmethod
    def uso_controle_do_fogo(self):
        pass

    @abstractmethod
    def producao_de_ferramentas(self):
        pass

    @abstractmethod
    def linguagem_complexa(self):
        pass

class Homo_Sapiens(Heidelbergensis):
    def __init__(self, cerebro, bipedalismo, anatomia_das_maos, testa_reta):
        super().__init__(cerebro, bipedalismo, anatomia_das_maos)
        self.testa_reta = testa_reta

    def producao_de_ferramentas(self):
        print("Construindo ferramentas")

    def linguagem_complexa(self):
        print("Falando alguma coisa complexa")

    def uso_controle_do_fogo(self):
        print("Construindo uma fogueira")

    def mostrando_a_testa(self):
        print("Olha minha testa")

class Homo_Neanderthalensis(Heidelbergensis):
    def __init__(self, cerebro, bipedalismo, anatomia_das_maos, falta_de_queixo):
        super().__init__(cerebro, bipedalismo, anatomia_das_maos)
        self.queixo_faltante = falta_de_queixo

    def producao_de_ferramentas(self):
        print("Construindo ferramentas")

    def linguagem_complexa(self):
        print("Falando alguma coisa complexa")

    def uso_controle_do_fogo(self):
        print("Construindo uma fogueira")

    def falta_de_queixo(self):
        print("CADE MEU QUEIO!?")

class Homo_Denisovensis(Heidelbergensis):
    def __init__(self, cerebro, bipedalismo, anatomia_das_maos, dentoes):
        super().__init__(cerebro, bipedalismo, anatomia_das_maos)
        self.dentes = dentoes

    def producao_de_ferramentas(self):
        print("Construindo ferramentas")

    def linguagem_complexa(self):
        print("Falando alguma coisa complexa")

    def uso_controle_do_fogo(self):
        print("Construindo uma fogueira")

    def mostrar_dentes(self):
        print("Oia meus dentao!")