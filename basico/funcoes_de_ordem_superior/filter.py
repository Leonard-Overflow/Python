# Estrutura filter(funcao, iteravel)

# A funcao deve retornar valores truthy(True, 1, "str com alguma coisa", etc) e falsy(0, None, false, etc) para decidir o que filtrar

# Com funcao anonima
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = filter(lambda numero : numero % 2 == 0, lista)
print(list(pares))

# Com funcoes pre escrita
def divisivel_tres(numero):
    return numero % 3 == 0

multiplos_tres = filter(divisivel_tres ,lista)
print(list(multiplos_tres)) # Retorna um obj filter e nao lista ou iteravel. Processamento lazy igual map