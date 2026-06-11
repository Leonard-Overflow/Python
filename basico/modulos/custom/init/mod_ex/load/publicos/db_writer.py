# Gerado pelo claude
class DBWriter:
    """Simula escrita em banco de dados."""

    def write(self, data: dict, table: str = "resultados") -> None:
        print(f"[DBWriter] Gravando em '{table}': {data}")