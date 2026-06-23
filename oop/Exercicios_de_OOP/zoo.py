class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self) -> None:
        print("Som do animal")

class Cachorro(Animal):
    def emitir_som(self) -> None:
        print("Au Au")

class Gato(Animal):
    def emitir_som(self) -> None:
        print("Miau")

def sonorizar(animal: Animal):
    animal.emitir_som()

doguinho = Cachorro("Sabrina", 4)
gato = Gato("Adriano Vinagrette", 5)

sonorizar(doguinho)
sonorizar(gato)