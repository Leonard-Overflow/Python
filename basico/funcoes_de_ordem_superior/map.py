# Retorna qualquer coisa, serve apenas para transformar o valor do iteravel

folha_de_pagamento = {
    "Marcos" : 4500,
    "Rafael" : 3500,
    "Daniel" : 2000,
    "Pedro" : 4500,
    "Leonardo" : 3500
}

# Com funcao anonima

salarios_com_aumento = [x for x in list(map(lambda a: a + 200, folha_de_pagamento.values()))]
print(salarios_com_aumento)

# Com funcao pre-escrita
def somar_listas(lista1, lista2):
    return lista1 + lista2

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]
soma = list(map(somar_listas, lista_1, lista_2)) # duas listas -> funcao recebe 2 parametros
print(soma)

# map() retorna um obj map e calcula os valores conforme itera sobre o iteravel. Processamento lazy, so demanda