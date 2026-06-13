class Formatacao_simples:
    def formatar(self, nivel:str, mensagem:str):
        return f"{nivel.upper()}: {mensagem}"

class Formatacao_JSON:
    def formatar(self, nivel: str, mensagem: str):
        return (f'"nivel" : "{nivel.upper()}", "mensagem" : "{mensagem}"')

class Formatacao_csv:
    def formatar(self, nivel:str, mensagem:str):
        return f"{nivel.upper()}, {mensagem}"

def simple_factory(tipo:str):
    formatos = {
        "simples": Formatacao_simples,
        "json": Formatacao_JSON,
        "csv": Formatacao_csv
    }

    formato = formatos.get(tipo)
    if formato is None:
        raise ValueError(f"O tipo {tipo} nao e aceito. Os tipos disponiveis sao: {list(formatos.keys())}")

    return formato()

if __name__ == "__main__":
    mensagem = "arquivo processado"
    nivel = "INFO"

    plain = simple_factory("simples")
    json_ = simple_factory("json")
    csv_  = simple_factory("csv")

    print(plain.formatar(nivel, mensagem))
    print(json_.formatar(nivel, mensagem))
    print(csv_.formatar(nivel, mensagem))

    # Deve lançar ValueError
    try:
        simple_factory("xml")
    except ValueError as e:
        print(f"Erro esperado: {e}")