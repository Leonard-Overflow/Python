from collections import OrderedDict
from datetime import datetime

class Cache:
    def __init__(self):
        self.cache: OrderedDict[str, datetime] = OrderedDict()

    def visitar(self, site):
        if site in self.cache:
            self.cache.move_to_end(site)
        else:
            self.cache[site] = datetime.now()