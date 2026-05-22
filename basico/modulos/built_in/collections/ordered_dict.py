from collections import OrderedDict
from datetime import datetime

class Cache:
    def __init__(self):
        self.cache: OrderedDict[int, tuple[str, datetime]] = OrderedDict()
        self.posicao = 1

    def visitar(self, site):
        for chave, valor in self.cache.keys() and self.cache.values[0]:
            if valor == site:

                del self.cache[]

        self.cache[self.posicao] = (site, datetime.now())
        self.cache.move_to_end(self.posicao)
        self.posicao += 1