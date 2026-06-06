from datetime import datetime

lista_de_eventos = []

while True:
    opcao = input("O que deseja fazer?\n"
                  "1 - Inserir evento\n"
                  "2 - Ver a lista de eventos\n"
                  "3 - Sair\n"
                  "")
    match opcao:
        case "1":
            data = input("Insira a data do evento: ")
            padrao = "%d/%m/%Y"
            data = datetime.strptime(data, padrao)
            if data not in lista_de_eventos:
                lista_de_eventos.append(data)
            else:
                print("Essa data ja possui um evento")
        case "2":
            lista_de_eventos.sort()
            print("Eventos")
            for i, evento in enumerate(lista_de_eventos, start=1):
                print(f"[{i}] {evento.strftime('%d/%m/%Y'):<20}")
        case "3":
            break