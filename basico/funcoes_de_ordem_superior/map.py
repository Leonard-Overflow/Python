# Retorna qualquer coisa, serve apenas para transformar o valor do iteravel

folha_de_pagamento = {
    "Marcos" : 4500,
    "Rafael" : 3500,
    "Daniel" : 2000,
    "Pedro" : 4500,
    "Leonardo" : 3500
}

salarios_com_aumento = [x for x in list(map(lambda a: a + 200, folha_de_pagamento.values()))]

print(salarios_com_aumento)