import json

while True:
    escolha = input("Escolha uma opcao\n"
                  "1 - Cadastrar\n"
                  "2 - Visualizar\n"
                  "3 - Atualizar\n"
                  "4 - Remover\n"
                  "5 - Sair")

    match escolha:
        case "1":
            with open("cadastro.json", "r", encoding="utf-8") as file:
                user = json.load(file)

            nome = input("Qual o username: ")
            user["nome"].append(nome)
            senha = input("Qual a senha do usuario: ")
            user["senha"].append(senha)

            with open("users.json", "w", encoding="utf-8") as file:
                json.dump("cadastro.json", file, indent=4, ensure_ascii=False)

            del user # Otimizar a memoria RAM

        case "2":
            with open("cadastro.json", "r", encoding="utf-8") as file:
                user = json.load(file)

            print(f"{"USUARIO:^30"}\n")
            for i, nome in enumerate(user["nome"], start=1):
                print(f"{i}. {nome: >30}")

            del user
        case "3":
            pass # Atualizar os dados do JSON se não existir lançar aviso
        case "4":
            pass # Apagar um dado do JSON
        case "5":
            break
        case _:
            print("Opcao invalida!")