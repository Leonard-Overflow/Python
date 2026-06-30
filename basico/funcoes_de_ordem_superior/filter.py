folha_de_pagamento = {
    "Marcos" : 4500,
    "Rafael" : 3500,
    "Daniel" : 2000,
    "Pedro" : 4500,
    "Leonardo" : 3500
}

gerentes = [x for x in list(filter(lambda a: a > 4000, folha_de_pagamento.values()))]

print(gerentes)