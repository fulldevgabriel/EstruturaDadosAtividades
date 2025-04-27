<h1 align='center'>Instruções para atividade do dia 15/04</h1>

## Atividade Prática: Explorando Pilhas, Filas e Listas em Mundos Fantásticos

**Objetivo:** Consolidar o entendimento e a aplicação de pilhas, filas e listas através de problemas práticos com temas distintos e criativos.

**Instruções:** Para cada cenário abaixo, implemente a estrutura de dados solicitada em Python, seguindo os passos indicados e comentando seu código.

**Tema 1: A Biblioteca Mágica (Listas)**

Em uma biblioteca mágica, os livros não seguem uma ordem alfabética tradicional. Em vez disso, são organizados de acordo com a ordem em que foram devolvidos. A bibliotecária precisa de sua ajuda para gerenciar o catálogo de livros.

**Tarefas:**

1.  **Criar o Catálogo:** Inicialize uma lista vazia chamada `catalogo_magico`.
2.  **Adicionar Livros:** Implemente uma função `adicionar_livro(catalogo, livro)` que adicione o `livro` ao final da lista `catalogo`. Adicione os seguintes livros ao catálogo: "O Feitiço da Lua Crescente", "A Jornada do Unicórnio Perdido", "Segredos da Floresta Encantada".
3.  **Visualizar o Catálogo:** Imprima o `catalogo_magico` para verificar a ordem dos livros.
4.  **Buscar Livro por Posição:** Implemente uma função `buscar_livro(catalogo, indice)` que retorne o livro presente no `indice` fornecido. Busque o livro na posição 1 (lembre-se que a indexação começa em 0) e imprima o resultado.
5.  **Remover Livro:** Um leitor devolveu "A Jornada do Unicórnio Perdido" e ele deve ser removido do catálogo. Utilize o método apropriado para remover o livro da lista.
6.  **Visualizar Catálogo Atualizado:** Imprima novamente o `catalogo_magico` para ver o catálogo após a remoção.
7.  **Verificar Presença:** Implemente uma função `verificar_livro(catalogo, livro)` que retorne `True` se o `livro` estiver no `catalogo` e `False` caso contrário. Verifique se o livro "Segredos da Floresta Encantada" ainda está no catálogo.

---

**Tema 2: A Fila de Atendimento dos Gnomos Artesãos (Filas)**

Em uma oficina de gnomos artesãos, os pedidos de ferramentas mágicas são processados na ordem em que chegam. Ajude o mestre gnome a gerenciar a fila de pedidos.

**Tarefas:**

1.  **Criar a Fila:** Inicialize uma fila vazia chamada `fila_de_pedidos`. Utilize a estrutura `deque` do módulo `collections`.
2.  **Adicionar Pedidos:** Implemente uma função `adicionar_pedido(fila, pedido)` que adicione o `pedido` ao final da `fila`. Adicione os seguintes pedidos: "Martelo Encantado", "Pinça Teleportadora", "Chave de Fenda Sônica".
3.  **Visualizar a Fila:** Imprima a `fila_de_pedidos` para verificar a ordem dos pedidos.
4.  **Processar Pedido:** Implemente uma função `processar_pedido(fila)` que remova e retorne o primeiro pedido da `fila`. Processe o próximo pedido na fila e imprima qual pedido foi atendido.
5.  **Verificar Fila Vazia:** Implemente uma função `fila_vazia(fila)` que retorne `True` se a `fila` estiver vazia e `False` caso contrário. Verifique se a fila ainda possui pedidos após o processamento.
6.  **Visualizar Fila Restante:** Imprima a `fila_de_pedidos` novamente para ver os pedidos restantes.
7.  **Processar Pedidos Restantes:** Processe os pedidos restantes na fila, um por um, e imprima cada pedido atendido. Verifique se a fila está vazia ao final.

---

**Tema 3: A Torre de Cristais dos Magos do Tempo (Pilhas)**

Os magos do tempo armazenam seus poderosos cristais em uma torre, onde o último cristal adicionado é o primeiro a ser utilizado em seus rituais. Ajude a gerenciar a pilha de cristais.

**Tarefas:**

1.  **Criar a Pilha:** Inicialize uma lista vazia chamada `torre_de_cristais`.
2.  **Empilhar Cristal:** Implemente uma função `empilhar_cristal(pilha, cristal)` que adicione o `cristal` ao topo da `pilha`. Adicione os seguintes cristais: "Cristal do Passado", "Cristal do Presente", "Cristal do Futuro".
3.  **Visualizar a Pilha:** Imprima a `torre_de_cristais` para verificar a ordem dos cristais (o topo estará no final da lista).
4.  **Desempilhar Cristal:** Implemente uma função `desempilhar_cristal(pilha)` que remova e retorne o cristal do topo da `pilha`. Utilize o cristal do topo para um ritual e imprima qual cristal foi utilizado.
5.  **Verificar Pilha Vazia:** Implemente uma função `pilha_vazia(pilha)` que retorne `True` se a `pilha` estiver vazia e `False` caso contrário. Verifique se a pilha ainda possui cristais após a utilização.
6.  **Visualizar Pilha Restante:** Imprima a `torre_de_cristais` novamente para ver os cristais restantes.
7.  **Desempilhar Cristais Restantes:** Utilize os cristais restantes da pilha, um por um, e imprima cada cristal utilizado. Verifique se a pilha está vazia ao final.

---

**Entrega:**

Compartilhe o código Python implementado para cada um dos temas. Certifique-se de que o código esteja bem comentado, explicando cada passo da implementação e o uso das estruturas de dados.

## 🔗 Caso queira visualizar diretamente pelo o Google Colab:

👉 [Acesse Aqui!](https://colab.research.google.com/drive/1mALAlt2cf9VE44wit1u0JhkL52vlHqpR?usp=sharing)