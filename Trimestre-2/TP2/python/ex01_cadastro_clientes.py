# Exercício 1 - Cadastro Inicial de Clientes
#
# O setor de onboarding do SJ90 registra novos clientes em dicionário
# local antes de enviar à API central. Crie atualizar_clientes() que
# adicione cliente novo, atualize existente ou remova se saldo negativo.
# Retorne e imprima o dicionário atualizado.

clientes = {
    501: {"nome": "Ana Costa",      "cidade": "Rio de Janeiro", "saldo": 1250.75},
    502: {"nome": "Bruno Lima",     "cidade": "São Paulo",      "saldo": 980.40},
    503: {"nome": "Carla Nunes",    "cidade": "Belo Horizonte", "saldo": 870.30},
    504: {"nome": "Diego Santos",   "cidade": "Curitiba",       "saldo": -10.00},
    505: {"nome": "Elaine Martins", "cidade": "Recife",         "saldo": 1530.25}
}

def atualizar_clientes(clientes, id, nome, cidade, saldo):
    if saldo < 0:
        clientes.pop(id, None)
    else:
        clientes[id] = {"nome": nome, "cidade": cidade, "saldo": saldo}
    return clientes

atualizar_clientes(clientes, 506, "Fábio Mendes", "Fortaleza", 720.00)
atualizar_clientes(clientes, 502, "Bruno Lima",   "São Paulo",  1180.90)
atualizar_clientes(clientes, 504, "Diego Santos", "Curitiba",  -50.00)

for id, dados in clientes.items():
    print(f"ID {id}: {dados}")