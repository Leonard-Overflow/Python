import json

while True:
    escolha = input("Escolha uma opcao\n"
                  "1 - Cadastrar\n"
                  "2 - Visualizar\n"
                  "3 - Atualizar\n"
                  "4 - Remover\n"
                  "5 - Sair\n")

    match escolha:
        case "1":
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)

            user_dict = {}
            user_dict["nome"] = input("Qual o nome do usuario: ")
            user_dict["senha"] = input("Qual a senha do usuario: ")
            users.append(user_dict)
            del user_dict

            with open("users.json", "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)

            del users # Otimizar a memoria RAM

        case "2":
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)

            print(f"{"USUARIO": ^30}\n")
            for i, dicionario in enumerate(users, start=1):
                print(f"{i}. {dicionario["nome"]: >30}")

            del users
        case "3":
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)

            while True:
                for i, dicionario in enumerate(users, start=1):
                    print(f"{i}. {dicionario["nome"]: >30}")
                usuario = input("Qual o nome do usuario que sera alterado: ")
                for item in users:
                    if item["nome"] == usuario:
                        item["nome"] = input("Qual o novo nome do usuario: ")
                        item["senha"] = input("Qual a senha do usuario: ")
                        break
                    else:
                        continue
                resposta = input("O usuario nao existe. Deseja sair?(S)")
                if resposta == "S":
                    break
                else:
                    continue
            with open("users.json", "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
            del users
        case "4":
            with open("users.json", "r", encoding="utf-8") as file:
                users = json.load(file)
            while True:
                for i, dicionario in enumerate(users, start=1):
                    print(f"{i}. {dicionario["nome"]: >30}")
                usuario = input("Qual o nome do usuario que sera removido: ")
                for item in users:
                    if item["nome"] == usuario:
                        users.remove(item)
                        break
                    else:
                        continue
                resposta = input("O usuario nao existe. Deseja sair?(S)")
                if resposta == "S":
                    break
                else:
                    continue
            with open("users.json", "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4, ensure_ascii=False)
            del users
        case "5":
            break
        case _:
            print("Opcao invalida!")