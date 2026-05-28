from collections import namedtuple
from numpy import linalg

ponto = namedtuple('origem', ["x", "y"])

origem = ponto(0, 0)
x = int(input("Digite o valor do x1: "))
y = int(input("Digite o valor do y1: "))
ponto1 = origem._replace(x=x,y=y)

ponto2 = []
x = int(input("Digite o valor do x2: "))
ponto2.append(x)
y = int(input("Digite o valor do y2: "))
ponto2.append(y)
ponto2 = ponto._make(ponto2)

x = int(input("Digite o valor do x3: "))
y = int(input("Digite o valor do y3: "))
ponto3 = ponto(x, y)

metodo_area = input("Qual metodo de calculo de area voce quer usar? S = Simples GA = Geometria Anaitica\n")

area = 0

if metodo_area == "S":
    area = 0.5 * abs(ponto1.x * (ponto2.y - ponto3.y) + ponto2.x * (ponto3.y - ponto1.y) + ponto3.x * (ponto1.y - ponto2.y))
elif metodo_area == "GA":
    matriz = [
        [ponto1.x, ponto1.y, 1],
        [ponto2.x, ponto2.y, 1],
        [ponto3.x, ponto3.y, 1]
    ]
    det = linalg.det(matriz)
    area = det/2
else:
    print("Valor invalido")

print(f"O valor da area e: {area:.2f}")