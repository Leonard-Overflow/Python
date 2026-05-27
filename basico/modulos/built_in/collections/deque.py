from collections import deque
import os

lista_de_tarefas = ["Limpar casa", "Lavar louça", "Tirar lixo", "Varrer o quintal", "Ir ao mercado"]
deque_tarefas = deque(lista_de_tarefas)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    largura = 32
    print("--- Tarefas ---".center(largura))

    anterior = deque_tarefas[-1]
    atual = deque_tarefas[0]
    posterior = deque_tarefas[1]

    print("-" * largura)
    print(f"{anterior}".center(largura))
    print("-" * largura)

    print("=" * largura)
    print(f"{atual}".center(largura))
    print("=" * largura)

    print("-" * largura)
    print(f"{posterior}".center(largura))
    print("-" * largura)

    print("Escolha uma opcao")
    resposta = input("1- subir\n"
                     "2 - descer\n"
                     "3 - sair\n")

    match resposta:
        case "1":
            deque_tarefas.rotate(-1)
        case "2":
            deque_tarefas.rotate(1)
        case "3":
            break