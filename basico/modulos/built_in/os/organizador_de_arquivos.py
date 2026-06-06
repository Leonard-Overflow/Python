import os

def organizar(pasta:str, tipo:str):
    os.makedirs(tipo, exist_ok=True)
    destino = os.path.join(os.path.dirname(pasta), tipo)
    origem = os.path.join(os.path.dirname(pasta), os.path.basename(pasta))
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(tipo):
            os.rename(os.path.join(origem, arquivo), os.path.join(destino, arquivo))

while True:
    type = input("Digite o tipo de arquivo que sera organizado: ")
    origem = input("Digite o nome do diretorio de origem dos arquivos: ")

    tipos = ["docx", "txt"]

    if origem in os.listdir(os.getcwd()) and type in tipos:
        organizar(origem, type)
        break
    else:
        print("Digite um valor valido")