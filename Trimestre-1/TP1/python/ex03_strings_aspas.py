# Exercício 3 - Manipulação de Strings com Aspas e Quebras de Linha
#
# Uma equipe de engenharia documental precisa formatar relatórios em texto
# contendo títulos, aspas e quebras de linha. Crie:
# - msg_aspas_simples com a frase: Projeto 'Davi' em execução.
# - msg_aspas_duplas com a frase: Aluno "Davi" aprovado no teste.
# - relatorio_triplo com três linhas (título, descrição e status)
#   utilizando aspas triplas.
# Imprima as três strings como seriam exibidas em um relatório.

msg_aspas_simples = 'Projeto \'Davi\' em execução.'
msg_aspas_duplas  = "Aluno \"Davi\" aprovado no teste."
relatorio_triplo = """
Título:         Relatório de Progresso
Descrição:      Acompanhamento do aluno Davi Santos no ciclo atual.
Status:         Aprovado
"""

print(msg_aspas_simples)
print(msg_aspas_duplas)
print(relatorio_triplo)