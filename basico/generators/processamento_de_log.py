def ler_logs(arquivo):
    with open(arquivo, "r") as arquivo:
        for linha in arquivo:
            partes = tuple(linha.split(' ', 2))
            yield partes

def filtro_de_nivel(gen, nivel):
    for retorno in gen:
        if retorno[1] == nivel:
            yield retorno
        else:
            continue

def duplicatas(gen):
    dict_duplicatas = {}

    for retorno in gen:
        if retorno[2] not in dict_duplicatas:
            dict_duplicatas[retorno[2]] = 1
        else:
            dict_duplicatas[retorno[2]] += 1

    return dict_duplicatas

leitura = ler_logs("logs_exercicio.txt")
filtro = filtro_de_nivel(leitura, "ERROR")
duplicatas = duplicatas(filtro)

for item in duplicatas.items():
    print(item)