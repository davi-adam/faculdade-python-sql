# Exercício 4 - Identificar Boletos Vencidos
#
# No setor de cobrança de um banco digital, relatórios diários listam todos
# os boletos vencidos para envio de notificações automáticas. Percorra uma
# lista de datas de vencimento e classifique cada boleto como vencido,
# vence hoje ou dentro do prazo. Ao final, exiba o total de vencidos.

data_atual = "2025-08-12"

boletos = [
    "2025-08-05",
    "2025-08-12",
    "2025-08-15",
    "2025-08-01"
]

total_vencidos = 0

for i, vencimento in enumerate(boletos):
    if vencimento < data_atual:
        situacao = "vencido"
        total_vencidos += 1
    elif vencimento == data_atual:
        situacao = "vence hoje"
    else:
        situacao = "dentro do prazo"
    
    print(f"Boleto: {i + 1} | Vencimento: {vencimento} | Situação: {situacao}")

print(f"\nTotal de boletos vencidos: {total_vencidos}")