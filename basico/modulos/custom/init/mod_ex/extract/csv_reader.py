# Gerado pelo claude
from ._base import BaseReader

class CSVReader(BaseReader):
    """Lê arquivos CSV e retorna lista de dicionários."""

    def read(self, source: str) -> list[dict]:
        if not self.validate_source(source):
            raise ValueError(f"Fonte inválida: {source}")
        # Simulação — em produção usaria csv.DictReader
        print(f"[CSVReader] Lendo: {source}")
        return [{"id": 1, "valor": 100}, {"id": 2, "valor": 200}]