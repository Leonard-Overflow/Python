import math



def meu_decorator(func):
    def wrapper(*args, **kwargs):
        a, b, c = args
        print(f"O coeficiente A = {a}")
        print(f"O coeficiente B = {b}")
        print(f"O coeficiente C = {c}")
        func(*args, **kwargs)
        print("Operacao realizado com sucesso")
    return wrapper

@meu_decorator
def baskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Sem resultados reais para a equacao!")
    else:
        resultado_1 = ((-b + math.sqrt(delta))) / (2 * a)
        resultado_2 = ((-b - math.sqrt(delta))) / (2 * a)

        print(f"Os resultados da equacao sao {resultado_1} e {resultado_2}")

baskara(1, 3, -7)