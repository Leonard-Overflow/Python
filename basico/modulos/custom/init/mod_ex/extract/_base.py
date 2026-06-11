# Gerado pelo claude
# Classe base — NÃO deve ser importável diretamente de `mod_ex` ou `mod_ex.extract`
class BaseReader:
    def read(self, source: str) -> list[dict]:
        raise NotImplementedError

    def validate_source(self, source: str) -> bool:
        return bool(source and isinstance(source, str))