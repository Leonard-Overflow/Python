# Gerado pelo claude
class Aggregator:
    """Agrega registros somando valores por id."""

    def aggregate(self, data: list[dict]) -> dict:
        total = sum(r["valor"] for r in data)
        return {"total": total, "registros": len(data)}