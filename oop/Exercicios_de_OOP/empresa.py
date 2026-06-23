class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        print(self.salario_base)

class Gerente(Funcionario):
    def calcular_salario(self):
        print(self.salario_base + 2000)

class Vendedor(Funcionario):
    def __init__(self, nome: str, salario_base: float, valor_vendas: float) -> None:
        super().__init__(nome, salario_base)
        self.vendas = valor_vendas

    def calcular_salario(self):
        print(self.salario_base + self.vendas*0.1)

lista = [Gerente("Roberto", 3500), Vendedor("Francis", 2000, 4500)]

for item in lista:
    item.calcular_salario()