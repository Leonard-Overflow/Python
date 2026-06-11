# Geraado pelo claude
# Helpers internos — NÃO devem aparecer na API pública
def _is_valid_record(record: dict) -> bool:
    return "id" in record and "valor" in record

def _cast_valor(record: dict) -> dict:
    return {**record, "valor": float(record["valor"])}