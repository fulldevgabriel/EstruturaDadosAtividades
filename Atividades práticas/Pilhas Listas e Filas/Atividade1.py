# 1. Criar o Catálogo
catalogo_magico = []

# 2. Função para adicionar livro
def adicionar_livro(catalogo, livro):
    catalogo.append(livro)

# Adicionando livros ao catálogo
adicionar_livro(catalogo_magico, "O Feitiço da Lua Crescente")
adicionar_livro(catalogo_magico, "A Jornada do Unicórnio Perdido")
adicionar_livro(catalogo_magico, "Segredos da Floresta Encantada")

# 3. Visualizar o Catálogo
print("Catálogo Mágico:")
print(catalogo_magico)

# 4. Buscar Livro por Posição
def buscar_livro(catalogo, indice):
    if 0 <= indice < len(catalogo):
        return catalogo[indice]
    else:
        return "Índice inválido."

livro_encontrado = buscar_livro(catalogo_magico, 1)
print("\nLivro na posição 1:")
print(livro_encontrado)

# 5. Remover Livro
catalogo_magico.remove("A Jornada do Unicórnio Perdido")

# 6. Visualizar Catálogo Atualizado
print("\nCatálogo Mágico Atualizado:")
print(catalogo_magico)

# 7. Verificar Presença de Livro
def verificar_livro(catalogo, livro):
    return livro in catalogo

livro_verificado = "Segredos da Floresta Encantada"
presenca = verificar_livro(catalogo_magico, livro_verificado)
print(f"\nO livro '{livro_verificado}' está no catálogo?")
print(presenca)
