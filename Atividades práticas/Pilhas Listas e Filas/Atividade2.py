from collections import deque

# 1. Criar a Fila
fila_de_pedidos = deque()

# 2. Adicionar Pedidos
def adicionar_pedido(fila, pedido):
    fila.append(pedido)

# 4. Processar Pedido
def processar_pedido(fila):
    return fila.popleft()

# 5. Verificar Fila Vazia
def fila_vazia(fila):
    return len(fila) == 0

# Adicionando pedidos
adicionar_pedido(fila_de_pedidos, "Martelo Encantado")
adicionar_pedido(fila_de_pedidos, "Pinça Teleportadora")
adicionar_pedido(fila_de_pedidos, "Chave de Fenda Sônica")

# 6. Processar um pedido
pedido = processar_pedido(fila_de_pedidos)
print("Pedido processado:", pedido)

# Visualizar fila restante
print("Fila restante:", fila_de_pedidos)

# Verificar se a fila ainda tem pedidos
print("Fila vazia?", fila_vazia(fila_de_pedidos))

# 7. Processar pedidos restantes
while not fila_vazia(fila_de_pedidos):
    pedido = processar_pedido(fila_de_pedidos)
    print("Pedido processado:", pedido)

# Verificar novamente se fila está vazia
print("Fila vazia?", fila_vazia(fila_de_pedidos))
