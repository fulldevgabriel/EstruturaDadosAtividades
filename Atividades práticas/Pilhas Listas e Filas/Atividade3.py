# 1. Criar a Pilha
# Inicializamos a torre de cristais como uma lista vazia
torre_de_cristais = []

# 2. Função para empilhar cristal
def empilhar_cristal(pilha, cristal):
    """
    Adiciona um cristal ao topo da pilha.
    """
    pilha.append(cristal)
    print(f"Cristal '{cristal}' adicionado à torre.")

# Adicionando os cristais à torre
empilhar_cristal(torre_de_cristais, "Cristal do Passado")
empilhar_cristal(torre_de_cristais, "Cristal do Presente")
empilhar_cristal(torre_de_cristais, "Cristal do Futuro")

# 3. Visualizar a Pilha
# Imprime a pilha para ver a ordem dos cristais (o topo está no final da lista)
print("\nTorre de Cristais (do início até o topo):")
print(torre_de_cristais)

# 4. Função para desempilhar cristal
def desempilhar_cristal(pilha):
    """
    Remove e retorna o cristal do topo da pilha.
    """
    if pilha:  # Verifica se a pilha não está vazia
        cristal = pilha.pop()
        print(f"\nCristal utilizado no ritual: {cristal}")
        return cristal
    else:
        print("\nA torre de cristais está vazia! Nenhum cristal para usar.")
        return None

# Utilizando o cristal do topo
desempilhar_cristal(torre_de_cristais)

# 5. Função para verificar se a pilha está vazia
def pilha_vazia(pilha):
    """
    Retorna True se a pilha estiver vazia, caso contrário False.
    """
    return len(pilha) == 0

# Verificando se a pilha ainda tem cristais
print("\nA torre de cristais está vazia?", pilha_vazia(torre_de_cristais))

# 6. Ver Pilha Restante
print("\nTorre de Cristais após o ritual:")
print(torre_de_cristais)

# 7. Desempilhar Cristais Restantes
print("\nUtilizando os cristais restantes:")

while not pilha_vazia(torre_de_cristais):
    desempilhar_cristal(torre_de_cristais)

# Verifica se a pilha está vazia ao final
print("\nA torre de cristais está vazia?", pilha_vazia(torre_de_cristais))
