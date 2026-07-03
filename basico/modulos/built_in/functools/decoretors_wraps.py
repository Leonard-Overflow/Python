from functools import wraps

def decorator_certo(func):
    @wraps(func) # Mantem os metadados da funcao
    def wrapper(*args, **kwargs):
        print("antes da execucao")
        return func(*args, **kwargs)
    return wrapper

def decorator_errado(func):
    def wrapper(*args, **kwargs):
        print("antes da execucao")
        return func(*args, **kwargs)
    return wrapper

@decorator_certo
def soma(a, b):
    return a + b

@decorator_errado
def sub(a, b):
    return a - b

print(soma.__name__)
print(sub.__name__)