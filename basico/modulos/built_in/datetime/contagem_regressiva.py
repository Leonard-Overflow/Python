from datetime import datetime as dt

lista_de_eventos = []

while True:
    resposta = input("O que deseja fazer?\n"
          "1 - Marcar um evento\n"
          "2 - Listar os eventos marcados\n"
          "3 - Sair\n")

    match resposta:
        case "1":
            padrao = "%d/%m/%Y"
            nome = input("Digite o nome do evento: ")
            data = input("Digite a data do evento: ")
            data = dt.strptime(data, padrao)
            tupla_evento = (nome, data)
            if tupla_evento not in lista_de_eventos:
                lista_de_eventos.append(tupla_evento)
            else:
                print("Ja ha um evento nesse dia")
        case "2":
            for i, evento in enumerate(lista_de_eventos):
                print(f"{i} - {evento[0]} na data {evento[1]}\n")
        case "3":
            break
        case _:
            continue