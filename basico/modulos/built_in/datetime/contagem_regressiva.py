import datetime as dt

futuro = dt.date(2026, 9, 12)
presente = dt.date(2026, 8, 21)
passado= dt.date(2026, 8, 20)
lista_de_eventos = [("Futuro", futuro), ("Presente", presente), ("Passado", passado)]

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
            data.replace("/", "-")
            data = dt.datetime.strptime(data, padrao).date()
            tupla_evento = (nome, data)
            if tupla_evento not in lista_de_eventos:
                lista_de_eventos.append(tupla_evento)
            else:
                print("Ja ha um evento nesse dia")
        case "2":
            for evento in lista_de_eventos:

                delta = evento[1] - dt.date.today()

                if evento[1] == dt.date.today():
                    print(f"O evento {evento[0]} e hoje!!!")
                elif delta.total_seconds() > 0:
                    print(f" {evento[0]} : faltam {delta.days} dia(s) para o evento")
                else:
                    print(f"O evento: {evento[0]} ja passou")
        case "3":
            break
        case _:
            continue