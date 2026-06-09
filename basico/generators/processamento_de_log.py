def ler_arquivo(arquivo):
    with open(arquivo) as arquivo:
        for linha in arquivo:
            if "INFO" in linha:
                continue
            partes = linha.split(" ", 2)

            yield {
                "data": partes[0],
                "tipo" : partes[1],
                "mensagem" : partes[2]
            }

def contador_de_log(arquivo):
    log_limpo = ler_arquivo(arquivo)
