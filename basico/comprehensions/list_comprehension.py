mochila = [
    {"nome": "pocao de cura","tipo": "pocao","poder": 80},
    {"nome": "espada de madeira", "tipo": "arma", "poder": 15},
    {"nome": "pergaminho de fogo", "tipo": "magia", "poder": 95},
    {"nome": "pocao de mana", "tipo": "pocao", "poder": 40},
    {"nome": "escudo de cobre", "tipo": "defesa", "poder": 25},
    {"nome": "amuleto do dragão", "tipo": "acessório", "poder": 100},
    {"nome": "pocao de invisibilidade", "tipo": "pocao", "poder": 60}
]

# Nivel 1
iventario = [item["nome"] for item in mochila]
pocoes = [item["nome"] for item in mochila if item["tipo"] == "pocao"]
poderosos = [item["nome"] for item in mochila if item["poder"] >= 50]

# Nivel 2
poderosos2 = [item["nome"].upper() if item["poder"] >= 50 else item["nome"].lower() for item in mochila]
magias_pocoes = [item["nome"] for item in mochila if item["poder"] > 50 and item["tipo"] == "magia" or item["tipo"] == "pocao"]

# Nivel 3
nome_poder = {item["nome"] : item["poder"] for item in mochila}
tipos_itens = {item["tipo"] for item in mochila}
mais_poderosos = {item["nome"] : item["poder"] for item in mochila}
mais_poderosos = sorted(mais_poderosos, key=mais_poderosos.get)