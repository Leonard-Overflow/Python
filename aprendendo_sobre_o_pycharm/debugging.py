from random import randint

num1 = randint(1,  10)
num2 = randint(1, 10)
resultado = num1 + num2
run = True

while run:
    resposta  = input(f"Qual o valor de {num1} + {num2}? ")
    if resposta.isdigit():
        if int(resposta) == resultado:
            print("Correto")
            run = False
        else:
            print("Incorreto")