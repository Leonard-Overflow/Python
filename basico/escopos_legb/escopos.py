import numpy as np # Dentro do global

def funcao1(): # Dentro do global
    print("funcao 1") # Dentro do local de funcao1(quando executada)

def funcao2(): # Dentro do global. Serve de enclousing para funcao3
    valor = 10 # Dentro do local de funcao2(quando executada)
    def funcao3(mensagem): # Dentro do local de funcao2 e a closure que guarda a cell de memória(que guarda a variavel valor)
        nonlocal valor # Avisa ao interpretador que valor está fora da função
        print(valor + mensagem) # Escopo local de funcao3(quando executada)
    return funcao3 # Dentro de local da funcao2

# Todos dentro de global
funcao1()
variavel = funcao2()
variavel(5)
