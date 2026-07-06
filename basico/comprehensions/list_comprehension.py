mochila = [
    {"nome": "pocao de Cura","tipo": "pocao","poder": 80},
    {"nome": "espada de Madeira", "tipo": "arma", "poder": 15},
    {"nome": "pergaminho de Fogo", "tipo": "magia", "poder": 95},
    {"nome": "pocao de Mana", "tipo": "pocao", "poder": 40},
    {"nome": "escudo de Cobre", "tipo": "defesa", "poder": 25},
    {"nome": "amuleto do Dragão", "tipo": "acessório", "poder": 100},
    {"nome": "pocao de Invisibilidade", "tipo": "pocao", "poder": 60}
]

# Nivel 1
iventario = [item["nome"] for item in mochila]
pocoes = [item["tipo"] for item in mochila if item["tipo"] == "pocao"]
poderosos = [item["poder"] for item in mochila if item["poder"] >= 50]
