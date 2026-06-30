class SerializarMixin:
    def serialize(self):
        # Cria um dicionario com base no dicionario de atributos do objeto desde que sejam atributos publicos
        return {
            chave : valor
            for chave, valor in self.__dict__.items()
            if not chave.startswith('_')
        }

# Usuario nao "e um" ou "possui um" ele apenas ganha o metodo do mixin
class Usuario (SerializarMixin):
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self._senha = senha