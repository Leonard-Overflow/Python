from collections import Counter

frase = "python collections"
lista_de_pedidos = ["frango", "bacon com cheddar", "peperoni",
                    "calabresa", "calabresa", "frango",
                    "frango", "bacon com cheddar", "frango"]

letras = Counter(frase)
pedidos = Counter(lista_de_pedidos)
print(letras["l"])
print(pedidos)

# Métodos

print(pedidos.most_common(2))
print(list(pedidos.elements()))
print(letras)
letras.update("fox")
print(letras)
letras.subtract("over")
print(letras)

# Operações

lista1 = ["a", "a", "a", "b", "a", "b", "b", "e", "a", "a", "c", "a", "a", "c", "a", "d", "d",]
lista2 = ["z", "z", "z", "y", "y", "w", "w", "z", "y", "y", "z", "w", "w", "x", "x", "a", "a",]

lista_1 = Counter(lista1)
lista_2 = Counter(lista2)
soma = lista_1 + lista_2
sub = lista_1 - lista_2

e = lista_1 & lista_2 # Mínimo de cada chave
ou = lista_1 | lista_2 # Máximo de cada chave

print(e)
print(ou)
print(lista_1)
print(lista_2)
print(soma)
print(sub)

mult = lista1*2
print(len(mult))