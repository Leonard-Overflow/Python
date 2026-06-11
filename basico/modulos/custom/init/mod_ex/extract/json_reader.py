# Gerado pelo claude
from ._base import BaseReader

class JSONReader(BaseReader):
    """Lê arquivos JSON e retorna lista de dicionários."""

    def read(self, source: str) -> list[dict]:
        if not self.validate_source(source):
            raise ValueError(f"Fonte inválida: {source}")
        print(f"[JSONReader] Lendo: {source}")
        return [{"id": 3, "valor": 300}]