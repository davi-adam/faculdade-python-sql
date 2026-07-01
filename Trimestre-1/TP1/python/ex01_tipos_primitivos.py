# Exercício 1 - Simulação de Cliente com Tipos de Dados Primitivos
#
# Uma consultoria em análise de crédito está desenvolvendo um modelo que
# processa dados simples de clientes: nome, idade, score e status de
# adimplência. Cada cliente será descrito por variáveis do tipo string,
# int, float e boolean, com dados simulados.
# Crie quatro variáveis com os seguintes dados:
# nome_cliente, idade_cliente = 21, score_credito = 772.4, cliente_ativo = True.
# Imprima cada variável junto ao tipo de dado correspondente,
# utilizando a função type().

nome_cliente = "Davi"
idade_cliente = 21
score_credito = 772.4
cliente_ativo = True

print(nome_cliente, type(nome_cliente))
print(idade_cliente, type(idade_cliente))
print(score_credito, type(score_credito))
print(cliente_ativo, type(cliente_ativo))