# Estrutura filter(funcao, iteravel)

# Com funcao anonima
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = filter(lambda numero : numero % 2 == 0, lista)
print(list(pares))

# Com funcoes pre escrita
def divisivel_tres(numero):
    return numero % 3 == 0

multiplos_tres = filter(divisivel_tres ,lista)
print(list(multiplos_tres))