from abc import ABC, abstractmethod

class Validator(ABC):
    @abstractmethod
    def validate(self, record: dict) -> dict:
        if not isinstance(record, dict):
            raise TypeError("record deve ser um dicionario")
        return record

class NotEmptyMixin(Validator):
    def validate(self, record: dict):
        if "" in record.values() or None in record.values():
            raise TypeError("record nao pode ter valores vazios")
        return super().validate(record)

class TypeCheckMixin(Validator):
    def validate(self, record: dict):
        if not isinstance(record["idade"], int) or isinstance(record["idade"], bool):
            raise TypeError("idade deve ser inteiro")
        elif not isinstance(record["salario"], (int, float) or isinstance(record["idade"], bool)):
            raise TypeError("salario deve ser float")
        return super().validate(record)

class RangeCheckMixin(Validator):
    def validate(self, record: dict):
        if not 18 <= record["idade"] < 90:
            raise TypeError("idade deve estar entre 0 e 127")
        return super().validate(record)

class RecordValidator(NotEmptyMixin, TypeCheckMixin, RangeCheckMixin):
    def __init__(self, tipo: str, departamento: str) -> None:
        self.tipo = tipo
        self.departamento = departamento

    def validate(self, record: dict):
        if record["tipo"] != self.tipo:
            raise TypeError(f"Esse validador nao serve para o tipo!")
        elif record["departamento"] != self.departamento:
            raise TypeError(f"Esse validador nao pertence ao departamento: {record['departamento']}!")
        super().validate(record)
        print("Registro validado. Enviando ao banco...")
        print("Envido com sucesso")

registro_leonardo = {
    "tipo" : "contratacao",
    "departamento" : "engenharia",
    "salario" : 2500.00,
    "idade" : 27
}

registro_rafael = {
    "tipo" : "demissao",
    "departamento" : "rh",
    "salario" : 3000.00,
    "idade" : 31
}

registro_lucas = {
    "tipo" : "contratacao",
    "departamento" : "rh",
    "salario" : 2200.00,
    "idade" : 25
}

validador_demissoes_rh = RecordValidator(tipo="demissao", departamento="rh")
validador_contratacoes_rh = RecordValidator(tipo="contratacao", departamento="rh")
validador_contratacoes_engenharia = RecordValidator(tipo="contratacao", departamento="engenharia")

print(RecordValidator.__mro__)
"""
Os mixins sao executados nessa ordem devido a ordem de injecao na criacao da classe RecordValidator
se a ordem trocasse o __mro__ também mudaria para a nova ordem. A classe Validator e executada por
ultimo, pois o mro organiza todas as classes dependentes de uma para depois executar a superclasse
delas.
"""

# Tudo certo
validador_demissoes_rh.validate(registro_rafael)
validador_contratacoes_rh.validate(registro_lucas)
validador_contratacoes_engenharia.validate(registro_leonardo)

# Valores errados
validador_demissoes_rh.validate(registro_leonardo)