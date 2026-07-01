# Exercício 3 - Operações entre Conjuntos de Clientes
#
# O time de marketing do SJ90 identifica clientes em campanhas simultâneas.
# Implemente funções separadas para calcular: clientes em todas as campanhas,
# em pelo menos duas, exclusivos de cada uma e total único combinado.

campanha_credito_rapido     = {1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1010, 1012}
campanha_invest_plus        = {1005, 1006, 1009, 1010, 1011, 1012, 1013, 1014}
campanha_cashback_fidelidade = {1001, 1003, 1005, 1011, 1015, 1016, 1017, 1018}

def clientes_em_todas(a, b, c):
    return a & b & c

def clientes_em_duas_ou_mais(a, b, c):
    return (a & b) | (a & c) | (b & c)

def exclusivos(campanha, outras):
    return campanha - outros if isinstance(outros, set) else campanha.difference(*outros)

todas       = clientes_em_todas(campanha_credito_rapido, campanha_invest_plus, campanha_cashback_fidelidade)
duas_ou_mais = clientes_em_duas_ou_mais(campanha_credito_rapido, campanha_invest_plus, campanha_cashback_fidelidade)
total_unico = campanha_credito_rapido | campanha_invest_plus | campanha_cashback_fidelidade

print(f"Clientes em todas as campanhas: {todas}")
print(f"Clientes em pelo menos duas campanhas: {duas_ou_mais}")
print(f"Clientes exclusivos:")
print(f"  - Crédito Rápido:       {campanha_credito_rapido - campanha_invest_plus - campanha_cashback_fidelidade}")
print(f"  - Invest+:              {campanha_invest_plus - campanha_credito_rapido - campanha_cashback_fidelidade}")
print(f"  - Cashback Fidelidade:  {campanha_cashback_fidelidade - campanha_credito_rapido - campanha_invest_plus}")
print(f"Total de clientes únicos: {len(total_unico)}")