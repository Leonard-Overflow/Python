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
    "variaveis_funcoes" : [[], []],
    "decorators" : []
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
                         "8 - Atualizar configuracoes\n"
                         "9 - Sair\n"))

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
            if resposta == "global" and len(escopos.maps) == 3:
                print(escopos.maps[1])
            elif resposta == "global" and len(escopos.maps) > 3:
                print(escopos.maps[2])
            elif resposta == "built-in" and len(escopos.maps) == 3:
                print(escopos.maps[2])
            elif resposta == "built-in" and len(escopos.maps) > 3:
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
            elif resposta == "computador":
                lib = input("Digite o comando de instalacao\n")
                if lib.startswith("pip install "):
                    lib = lib[12::].strip().lower()
                    if lib in Builtin["bibliotecas_instaladas"]:
                        print(f"A biblioteca {lib} ja esta instalada.")
                    else:
                        print("instalando...")
                        Builtin["bibliotecas_instaladas"].append(lib)
                        sleep(1)
                        print("Biblioteca instalada.")
                else:
                    print("Erro. Use o comando pip install para instalar")
            else:
                print("Insira uma resposta valida!")
        case 4:
            pass
        case 5:
            nome = input("Insira o nome da funcao: ")
            parametros = []
            while True:
                parametro = input("Insira o nome do parametro(enter para parar): ").strip().lower()
                if parametro == "":
                    break
            parametros.append(parametro)
            retorno = input("Qual o retorno da funcao?\n").lower().strip()
            parametros = ", ".join(parametros)
            lambda_str = f"lambda {parametros}: {retorno}"
            funcao = eval(lambda_str)
            Global["variaveis_funcoes"][1].append(funcao)
        case 6:
            nome = input("Qual o nome da variavel?\n").lower().strip()
            tipo = input("Qual o tipo da variavel?\n").lower().strip()

            match tipo:
                case "string":
                    valor = input("Insira o valor da variavel?\n").lower().strip()
                case "int":
                    try:
                        valor = int(input("Insira o valor da variavel?\n"))
                    except ValueError:
                        raise("Insira um valor valido!")
                case "float":
                    try:
                        valor = float(input("Insira o valor da variavel?\n"))
                    except ValueError:
                        raise("Insira um valor valido!")
                case _:
                    raise ValueError("Insira um tipo valido!")

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