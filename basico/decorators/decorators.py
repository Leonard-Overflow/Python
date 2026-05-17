import math

def baskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("Sem resultados reais para a equacao!")
    else:
        resultado_1 = ((-b + math.sqrt(delta))) / (2 * a)
        resultado_2 = ((-b - math.sqrt(delta))) / (2 * a)

        print(f"Os resultados da equacao sao {resultado_1} e {resultado_2}")

def decorator(func):
    def wrapper(*args, **kwargs):
        a = args[0]
        b = args[1]
        c = args[2]
        print(f"O coeficiente A = {a}")
        print(f"O coeficiente B = {b}")
        print(f"O coeficiente C = {c}")
        func(*args, **kwargs)
        print("Operacao realizado com sucesso")
    return wrapper

formula = decorator(baskara)

formula(1, 3, -7)