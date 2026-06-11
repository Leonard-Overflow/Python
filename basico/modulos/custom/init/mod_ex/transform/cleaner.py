# Gerado pelo claude
from ._validators import _is_valid_record, _cast_valor

class Cleaner:
    """Remove registros inválidos e normaliza tipos."""

    def clean(self, data: list[dict]) -> list[dict]:
        validos = [r for r in data if _is_valid_record(r)]
        return [_cast_valor(r) for r in validos]