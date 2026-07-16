class Pessoa:
    __slots__ = ("_nome", "_idade") # Define que todas as instancias irao ter esses atributos

    def __init__(self, nome, idade):
        self.nome = nome or "Sem nome"
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @nome.deleter
    def nome(self):
        del self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if isinstance(idade, int) and 0 < idade < 100:
            self._idade = idade
        else:
            raise ValueError("idade deve ser um inteiro")

    @idade.deleter
    def idade(self):
        print("Idade deletada")
        del self._idade

Leonardo = Pessoa(nome="Leonardo", idade=18)