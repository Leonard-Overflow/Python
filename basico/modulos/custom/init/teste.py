from mod_ex.extract import CSVReader, JSONReader   # ✅ deve funcionar
from mod_ex.extract import BaseReader              # deve funcionar (acesso direto)
# mas BaseReader NÃO deve aparecer em:
import mod_ex.extract as ex
print(ex.__all__)                 # ['CSVReader', 'JSONReader']
