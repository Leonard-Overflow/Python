# Listas
numeros = [1,2,3,4,5,6,7,8,9,10]

quadrados = [n**2 for n in numeros]
quadrados_com_filtro = [n**2 for n in range(11) if n <= 5 and n > 0]

print(quadrados)
print(quadrados_com_filtro)

