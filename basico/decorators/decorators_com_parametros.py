from functools import wraps

def backup(db_backups):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Fazendo backup no banco de dados: {db_backups}")
            func(*args, **kwargs)
            print("Operacao realizada com sucesso. Deletando backup...")
        return wrapper
    return decorator

@backup("Banco de backup")
def calcular_media():
    print("Acessando a tabela...")
    print("Calculando...")
    print("A media e 10")

calcular_media()