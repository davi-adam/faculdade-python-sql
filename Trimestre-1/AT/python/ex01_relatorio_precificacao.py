# Exercício 1 - Operações Aritméticas com Inteiros e Floats
#
# Analistas de planejamento de compras precisam padronizar cálculos de custo
# unitário, descontos e impostos em relatórios automatizados. Crie uma função
# gerar_relatorio() que receba os dados da tabela, aplique as fórmulas de
# valor bruto, desconto, base tributável, imposto, total líquido, lotes
# fechados e sobras, e exiba um relatório estruturado.

def gerar_relatorio(preco_unitario, quantidade, percentual_desconto, percentual_imposto, tamanho_lote):
    valor_bruto = preco_unitario * quantidade
    valor_desconto = valor_bruto * (percentual_desconto / 100)
    base_tributavel = valor_bruto - valor_desconto
    valor_imposto = base_tributavel * (percentual_imposto / 100)
    total_liquido = base_tributavel + valor_imposto
    lotes_fechados = quantidade // tamanho_lote
    sobras = quantidade % tamanho_lote

    print("### Relatório de Cálculos de Precificação")
    print(f"| {'Etapa':<18} | {'Resultado':<9} |")
    print(f"| {'-'*18} | {'-'*9} |")
    print(f"| {'Valor bruto':<18} | {valor_bruto:<9.2f} |")
    print(f"| {'Valor do desconto':<18} | {valor_desconto:<9.2f} |")
    print(f"| {'Base tributável':<18} | {base_tributavel:<9.2f} |")
    print(f"| {'Valor do imposto':<18} | {valor_imposto:<9.2f} |")
    print(f"| {'Total líquido':<18} | {total_liquido:<9.2f} |")
    print(f"| {'Lotes fechados':<18} | {lotes_fechados:<9} |")
    print(f"| {'Sobras':<18} | {sobras:<9} |")

gerar_relatorio(
    preco_unitario       = 12.50,
    quantidade           = 47,
    percentual_desconto  = 10,
    percentual_imposto   = 15,
    tamanho_lote         = 12
)