from abc import ABC, abstractmethod

class DataSource(ABC):

    # O constructor define o que as subclasses irão herdar servindo como um DNA das subclasses.

    @abstractmethod # Obriga toda classe a criar seu proprio init e não so herdar o que a superclasse ja tem pronto
    def __init__(self, connection_str:str) -> None:
        self.connection = connection_str
        self.is_connected = False

    # Os abstract methods irão definir os metodos herdado atuando junto ao contructor como parte do DNA

    @abstractmethod
    def connect(self):
        print("Conectando...")
        self.is_connected = True

    @abstractmethod
    def disconect(self):
        print("Desconectando...")
        self.is_connected = False

    @abstractmethod
    def fetch_data(self, valor):
        print("Procurando valores...")
        print(f"valor: {valor} encontrado")

class PostgresSource(DataSource):
    def __init__(self, connection_str, schema) -> None:
        super().__init__(connection_str) # Sem o super() a classe pode herdar os metodos, mas nao os atributos. Bug silencioso
        self.schema = schema

    def connect(self):
        print("Conectando...")
        self.is_connected = True

    def disconect(self):
        print("Desconectando...")
        self.is_connected = False

