from collections import OrderedDict
from datetime import datetime

class Cache:
    def __init__(self):
        self.cache: OrderedDict[str, datetime] = OrderedDict()

    def visitar(self):
        site = input("Pesquisar: ")

        self.cache[site] = datetime.now()
        self.cache.move_to_end(site)

    def limpar(self):
        self.cache.clear()

    def excluir_site(self):
        while True:
            site = input("Insira a url do site a ser removido: ")
            if site in self.cache:
                self.cache.pop(site)
                break
            else:
                print("Site nao existe")


    def exibir(self):
        print("\n--- Histórico ---")
        for i, (url, data) in enumerate(self.cache.items(), start=1):
            print(f"[{i}] {url:<35} {data.strftime('%d/%m/%Y %H:%M:%S')}\n")

cache = Cache()

while True:
    print("O que deseja fazer?")
    print("1 - Pesquisar")
    print("2 - Limpar historico")
    print("3 - Excluir um site do historico")
    print("4 - Exibir historico")
    print("5 - Sair")
    escolha = int(input("Escolha: "))

    match escolha:
        case 1:
            cache.visitar()
        case 2:
            cache.limpar()
        case 3:
            cache.excluir_site()
        case 4:
            cache.exibir()
        case 5:
            break
        case _:
            print("opcao invalida")