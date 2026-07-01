# Exercício 2 - Tratar Falhas de Sensores
#
# Supervisores de produção precisam decidir ações diferentes para cada falha
# detectada em um sensor de linha de montagem. Os códigos de falha são:
# F1 (falha de inicialização), F2 (superaquecimento), F3 (oscilação de
# temperatura) e F4 (erro nos sensores ópticos). Se nenhuma condição de
# temperatura for atendida, acionar o engenheiro responsável.

codigo_falha = "F2"
temperatura = 65

if codigo_falha == "F1" and temperatura < 40:
    print("Reiniciar máquina")
elif codigo_falha == "F2" and temperatura > 60:
    print("Verificar conexão elétrica e sistema de refrigeração")
elif codigo_falha == "F3" and 45 <= temperatura <= 55:
    print("Ajustar temperatura da esteira")
elif codigo_falha == "F4":
    print("Realizar diagnóstico dos sensores ópticos")
else:
    print("Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável")