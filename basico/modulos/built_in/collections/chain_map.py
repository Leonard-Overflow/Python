from collections import ChainMap
from time import sleep

Local = {
    "numeros" : [],
    "operacoes" : ["soma", "subtracao"],
    "resultado" : 0
}

Global = {
    "nome" : "calculadora",
    "tipo" : "python",
    "bibliotecas_instaladas" : ["numpy", "pandas", "keras", "tensorflow"],
    "variaeis_funcoes" : [[], []]
}

Builtin = {
    "versao" : 3.13,
    "bibliotecas_instaladas" : ["numpy", "pandas", "matplotlib", "keras", "tensorflow", "django", "streamlit"],
    "gerenciador_de_pacotes" : "Pip"
}

escopos = ChainMap(Local, Global, Builtin)

while True:
    print("-- Calculadora --")
    resposta = int(input("O que deseja fazer?\n"
                         "1 - Realizar uma conta\n"
                         "2 - Verifciar configuracoes\n"
                         "3 - Instalar novas bibliotecas\n"
                         "4 - Criar um decorator\n"
                         "5 - Criar uma funcao\n"
                         "6 - Criar uma variavel\n"
                         "7 - Executar funcao\n"
                         "8 - Atualizar configuracao\n"
                         "9 - Sair"))

    match resposta:
        case 1:
            while True:
                try:
                    numero = float(input("Digite um numero: "))
                    escopos.maps[0]["numeros"].append(numero)
                except ValueError:
                    break

            operacao = input("Qual operacao vai ocorrer com os numeros?\n").lower().strip()

            if operacao not in escopos.maps[0]["operacoes"]:
                print("Operacao invalida!")
            elif operacao == "soma":
                print(sum(escopos.maps[0]["numeros"]))
            elif operacao == "subtracao":
                for i in range(len(escopos.maps[0]["numeros"]) - 1):
                    if escopos.maps[0]["numeros"][i + 1] in escopos.maps[0]["numeros"]:
                        Local["resultado"] = escopos.maps[0]["numeros"][i] - escopos.maps[0]["numeros"][i + 1]
                    else:
                        break
                print(Local["resultado"])
        case 2:
            resposta = input("Voce deseja ver as configuracoes? do global ou do bulit-in?\n")
            if resposta == "global" and len(escopos) == 3:
                print(escopos.maps[1])
            elif resposta == "global" and len(escopos) > 3:
                print(escopos.maps[2])
            elif resposta == "built-in" and len(escopos) == 3:
                print(escopos.maps[2])
            elif resposta == "built-in" and len(escopos) > 3:
                print(escopos.maps[3])
        case 3:
            resposta = input("Onde deseja instalar a biblioteca, no projeto ou no computador?\n")
            if resposta == "projeto":
                lib = input("Digite o nome da biblioteca: ")
                if lib in Global["bibliotecas_instaladas"]:
                    print(f"A biblioteca {lib} ja esta instalada.")
                else:
                    print("instalando...")
                    Global["bibliotecas_instaladas"].append(lib)
                    sleep(3)
                    print("Biblioteca instalada.")
            else:
                lib = input("Digite o nome da biblioteca: ")
                if lib in Builtin["bibliotecas_instaladas"]:
                    print(f"A biblioteca {lib} ja esta instalada.")
                else:
                    print("instalando...")
                    Builtin["bibliotecas_instaladas"].append(lib)
                    sleep(3)
                    print("Biblioteca instalada.")
        case 4:
            pass
        case 5:
            pass
        case 6:
            nome = input("Qual o nome da variavel?\n").lower().strip()
            valor = float(input("Digite o valor da variavel: "))
            tupla_da_variavel = (nome, valor)
            Global["variaveis_funcoes"][0].append(tupla_da_variavel)
        case 7:
            pass
        case 8:
            pass
        case 9:
            break
        case _:
            print("opcao invalida!")