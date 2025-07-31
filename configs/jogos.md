# Jogos

Os jogos a serem estudados neste trabalho serão escolhidos com base nos critérios a seguir:

- Baixa complexidade: o jogo deve ser simples de implementar e entender
- Jogabilidade alta: profundidade nas decisões, intuitividade para realizar ações e equilíbrio no jogo
- Aplicabilidade conceitual: capacidade de aplicação dos conceitos do estudo na implementação do jogo
- Impacto social: acessibilidade e capacidade de influência do jogo na sociedade

---

### Alternativas de desenvolvimento

- Pygame (Biblioteca - Linguagem Python)
- Cocos2d-x (Game Engine - Linguagens C++, JavaScript, TypeScript & Lua)
- libGDX (Framework - Linguagem Java)
- Godot (Framework - Linguagem GDScript)

### Possibilidades de jogos

| Jogo               | Conceito de Grafos                                                                    | Fase                          |
|--------------------|---------------------------------------------------------------------------------------|-------------------------------|
| **Col**            | Coloração de vértices; Teorema de Ramsey para vizinhança adjacente                    | Implementar                   |
| **Sim**            | Coloração de arestas em $K_6$, Ramsey $R(3,3)=6$                                      | Implementar                   |
| **Minesweeper**    | Grafo de adjacência em grid; busca de componentes seguras (flood-fill)                | Implementar                   |
| **Sudoku**         | Grafo de coloração (vértices = células; arestas = restrições de linha/bloco)          | Implementar                   |
| **Flow Tree**      | Árvores geradoras em grade; caminhos sem ciclos                                       | Analisar implementação pronta |
| **Hashiwokakero**  | Conectividade e árvore geradora mínima; backtracking em tabuleiro de “ilhas e pontes” | Analisar implementação pronta |
| **Connect Four**   | Game tree em grade; detecção de vitória via buscas em grafos                          | Analisar implementação pronta |
| **Carcassonne**    | Grafos planos: conectividade de estradas e cidades ao posicionar peças                | Analisar implementação pronta |
| **Ticket to Ride** | Rotas em grafo ponderado; conectividade e bloqueio estratégico de caminhos            | Jogar / Analisar visualmente  |
| **Pandemic**       | Propagação de epidemias em rede dinâmica; fluxos e contenção em grafos                | Jogar / Analisar visualmente  |
| **Chess**          | Game tree de posições; algoritmos minimax/α–β em grafo de transição de peças          | Jogar / Analisar visualmente  |

Os jogos também podem ter alguns exemplos de aspectos indiretos nos seus protótipos, com relação a [fonte]():

- Máquinas de estados (state machines)  
    Menus, fluxos de jogo e lógica de fases (Flappy Bird, Dino do Chrome e simuladores) são quase sempre implementados como grafos dirigidos de estados e transições.
- Cenas e renderização
    Engines de jogos (pygame, Godot, libGDX) usam internamente scene graphs — árvores onde cada nó é um objeto na cena, definindo hierarquia e transformações.

- Particionamento espacial  
    Para colisões e queries de proximidade, usam-se árvores (quadtrees, k-d trees) ou grafos de vizinhança em grid, acelerando detecção de colisão.

- IA de NPCs / Oponentes  
    Pathfinding em pistas (simulador de corrida) ou navios (Pandemic, Ticket to Ride) recorre a grafos de waypoints e algoritmos de busca como A*.

- Pipeline de simulação  
    No simulador de foguete, o encadeamento de módulos (tanque → bomba → motor) pode ser modelado como grafo de dependências.