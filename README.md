# Servidor de Matchmaking e Ranking

Projeto acadêmico desenvolvido para a disciplina de Algoritmos e Estruturas de Dados.

O objetivo do sistema é simular um servidor de pareamento de partidas 5v5 para jogos competitivos, gerenciando filas de espera por categoria e atualizando a patente dos jogadores de acordo com suas vitorias e derrotas. O foco principal do projeto é o uso de estruturas de dados fundamentais sem o uso de abstrações prontas.
Estruturas de Dados e Arquitetura

1. Tabela Hash Manual (Buckets)
Função Hash: Converte o ID do jogador (string) em um índice numérico somando os valores ASCII de cada caractere e aplicando o resto da divisão pelo tamanho da tabela.
Tratamento de Colisões: Resolvido através de encadeamento separado (buckets). Cada posição da tabela armazena uma lista com os jogadores que geraram o mesmo índice.
Desempenho: Permite buscar e cadastrar jogadores com tempo médio constante O(1).

2. Filas FIFO por Categoria (collections.deque)
Organização: Cada patente (Tier) possui sua própria fila de espera independente.
Regra de Chegada: Utiliza a estrutura deque para garantir que os jogadores que entraram a mais tempo na fila tenham prioridade de entrada na partida (First-In, First-Out).

3. Hierarquia de Ranking (Enum)
Controle de Elo: Mapeamento do ranking (Unranked a Challenger) encapsulado com métodos de navegação (.proximo() e .anterior()).
Regra de Negocio: Promoção automática a cada 10 vitorias e rebaixamento em caso de sequencia de derrotas, mantendo os limites mínimo e máximo.

Logica do Matchmaking:
- O jogador solicita entrada na fila informando seu ID.
- O sistema busca o jogador na Tabela Hash e identifica seu Tier.
- Se a fila do Tier já possuir 9 ou mais jogadores, o sistema remove os 9 primeiros, adiciona o jogador atual, fecha a partida 5v5 e monta os dois times.
- Se houver menos de 9 jogadores na fila, o jogador é adicionado ao final da fila de espera.

Complexidade Algorítmica (Big-O): 
- Busca na Tabela Hash: O(1) no caso médio / O(k) no pior caso de colisão
- Inserção na Tabela Hash: O(1)
- Entrada na Fila (append): O(1)
- Formação de Partida (popleft): O(1)
- Cancelar Busca na Fila (remove): O(N)
