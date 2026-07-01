# Exercício 3 - Reorganizar Fila de Pedidos
#
# Equipes de compras de um marketplace precisam reorganizar a fila de pedidos
# quando chegam solicitações com despacho prioritário. Se prioridade_urgente
# for True, insira o pedido urgente no início da lista. Senão, substitua o
# pedido indicado, se existir. Testar três cenários distintos.

# Cenário A - prioridade urgente
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = True
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
elif pedido_a_substituir in pedidos:
    pedidos[pedidos.index(pedido_a_substituir)] = pedido_urgente
else:
    print("Pedido a substituir não encontrado na fila.")

print("Fila final (Cenário A):", pedidos)

# Cenário B - não urgente, pedido existe
pedidos = ["P123", "P456", "P789"]
prioridade_urgente = False

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
elif pedido_a_substituir in pedidos:
    pedidos[pedidos.index(pedido_a_substituir)] = pedido_urgente
else:
    print("Pedido a substituir não encontrado na fila.")

print("Fila final (Cenário B):", pedidos)

# Cenário C = não urgente, pedido não existe

pedidos = ["P123", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = False

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
elif pedido_a_substituir in pedidos:
    pedidos[pedidos.index(pedido_a_substituir)] = pedido_urgente
else:
    print("Pedido a substituir não encontrado na fila.")

print("Fila final (Cenário C):", pedidos)