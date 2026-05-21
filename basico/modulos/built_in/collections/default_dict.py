from collections import defaultdict
import time

def verifica_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcao(*args, **kwargs)
        fim = time.time()
        tempo = fim - inicio
        infromacoes = [funcao.__name__, tempo]
        return infromacoes
    return wrapper

def loop_for(valor):
    for i in range(valor):
        print(i)

def loop_quadrado(valor):
    for i in range(valor):
        print(i**2)

def loop_cubico(valor):
    for i in range(valor):
        print(i**3)

for_decorartor = verifica_tempo(loop_for)
quadrado_decorator = verifica_tempo(loop_quadrado)
cubico_decorator = verifica_tempo(loop_cubico)

resultado_for = for_decorartor(100)
resultado_quadrado = quadrado_decorator(100)
resultado_cubico = cubico_decorator(100)

lista_de_resultados = [resultado_for, resultado_quadrado, resultado_cubico]

meta_tempo = 0.0003

dic_rapidos = defaultdict(list)
dic_lentos = defaultdict(list)

for result in lista_de_resultados:
    if result[1] < meta_tempo:
        dic_rapidos[result[0]].append(result)
    else:
        dic_lentos[result[0]].append(result)

print(resultado_for[1])
print(resultado_quadrado[1])
print(resultado_cubico[1])

print(dic_rapidos)
print(dic_lentos)