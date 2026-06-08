mochila = [
    {"nome": "pocao de Cura","tipo": "pocao","poder": 80},
    {"nome": "espada de Madeira", "tipo": "arma", "poder": 15},
    {"nome": "pergaminho de Fogo", "tipo": "magia", "poder": 95},
    {"nome": "pocao de Mana", "tipo": "pocao", "poder": 40},
    {"nome": "escudo de Cobre", "tipo": "defesa", "poder": 25},
    {"nome": "amuleto do Dragão", "tipo": "acessório", "poder": 100},
    {"nome": "pocao de Invisibilidade", "tipo": "pocao", "poder": 60}
]

apenas_pocoes = [x["nome"] for x in mochila if x["tipo"] == "pocao"]
itens_poderosos = [y["nome"] + " - [EPICO]" for y in mochila if y["poder"] > 50]
descarte = [z["nome"] + " - guardar" if z["poder"] >= 40 else z["nome"] + " - vender" for z in mochila]

print("Pocoes")
for item in apenas_pocoes:
    print(item)
print("\n")

print("Itens poderosos")
for item in itens_poderosos:
    print(item)
print("\n")

print("Descarte")
for item in descarte:
    print(item)