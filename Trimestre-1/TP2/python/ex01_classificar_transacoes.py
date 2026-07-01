# Exercício 1 - Classificar Transações Bancárias
#
# Analistas de fraude bancária precisam automatizar a classificação de
# movimentações suspeitas. Defina ANO_2_DIGITOS com os dois últimos dígitos
# do seu ano de nascimento. Se VALOR_TRANSACAO for maior que 1000 * ANO_2_DIGITOS
# e TIPO_TRANSACAO for "transferência", exiba "Alerta: verificar origem da
# transferência". Se TIPO_TRANSACAO for "saque", exiba "Alerta: confirmar com
# o cliente". Caso contrário, exiba "Transação normal".

ANO_2_DIGITOS = 5
limite = 1000 * ANO_2_DIGITOS

VALOR_TRANSACAO = 6000
TIPO_TRANSACAO = "transferência"

if VALOR_TRANSACAO > limite and TIPO_TRANSACAO == "transferência":
    print("Alerta: verificar origem da transferência")
elif TIPO_TRANSACAO == "saque":
    print("Alerta: confirmar com o cliente")
else:
    print("Transação normal")