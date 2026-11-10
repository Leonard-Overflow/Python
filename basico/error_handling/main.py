# Estrutura basica
# try: enta executar o codigo inicial
# except X as e: chama o tipo do erro de 'e' e e o caminho onde deu errado
# else: e o  caminho onde deu certo
# finally: executa com ou sem erro, com ou sem return

# Funcao extra
# raise define mensagem de error especifica

# Exemplo

arquivo = "vendas.csv"

try:
    with open(arquivo) as arquivo:
        pass
except FileNotFoundError as e:
    print(f"o arquivo {arquivo} nao existe")
else:
    print(f"Modificando arquivo:")
finally:
    print("O arquivo foi aberto a DB foi atualzada com sucesso")