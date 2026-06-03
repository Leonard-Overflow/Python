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
    "variaveis_funcoes" : [[], []]
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
                         "4 - Criar uma funcao\n"
                         "5 - Criar uma variavel\n"
                         "6 - Executar funcao\n"
                         "7 - Atualizar configuracoes\n"
                         "8 - Sair\n"))

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
            Global["variaveis_funcoes"][1].append((nome, funcao))
        case 5:
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
        case 6:
            print("---Funcoes---")
            for i, (nome, function) in enumerate(Global["variaveis_funcoes"][1]):
                print(f"{i}. {nome}")
            resposta = input("Qual funcao voce quer executar")

            from typing import Callable, Optional
            funcao_encontrada = Optional[Callable] = None
            for nome, funcao in Global["variaveis_funcoes"][1]:
                if resposta == nome:
                    funcao_encontrada = funcao
                    break

            if funcao_encontrada is None:
                print(f"A funcao {resposta} nao existe!")
            else:

                import inspect

                params = inspect.signature(funcao_encontrada).parameters
                argumentos = []

                for param in params:
                    valor = input(f"Insira o valor para '{param}': ")
                    try:
                        valor = float(valor) if "." in valor else int(valor)
                    except ValueError:
                        pass
                    argumentos.append(valor)

                resultado = funcao_encontrada(*argumentos)
                print(f"Resultado da funcao: {resultado}")
        case 7:
            pass
        case 8:
            break
        case _:
            print("opcao invalida!")