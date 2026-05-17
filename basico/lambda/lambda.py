import random

lista_de_numeros = []

for i in range(10):
    valor = random.randint(0, 11)
    lista_de_numeros.append(valor)

media = lambda lista: sum(lista) / len(lista)
quadrados = lambda lista: list(map(lambda valor:valor**2, lista))
listar = lambda lista, i = 2: list(map(lambda valor:valor*i, lista))
pares =  lambda lista: list(map(lambda valor: "par" if valor % 2 == 0 else "impar", lista))

print(lista_de_numeros)
print(media(lista_de_numeros))
print(quadrados(lista_de_numeros))
print(listar(lista_de_numeros))
print(pares(lista_de_numeros))
