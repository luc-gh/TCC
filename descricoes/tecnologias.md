# Tecnologias de desenvolvimento

Como citado em [jogos](jogos.md), Pygame é uma das alternativas de desenvolvimento escolhidas para este trabalho.  
Pygame é uma biblioteca de desenvolvimento de jogos em Python, que fornece funcionalidades para manipulação de gráficos, som e eventos de entrada.

Ela foi escolhida para o desenvolvimento do jogo Col por ser uma tecnologia de fácil aprendizado e por permitir a implementação rápida de protótipos.
Mas para um estudo dessa magnitude, polimorfismo de desenvolvimento é importante, pois permite explorar diferentes abordagens e 
tecnologias, enriquecendo a análise e compreensão dos conceitos envolvidos.

Portanto, outras tecnologias serão utilizadas para o desenvolvimento de jogos. Tais alternativas foram selecionadas com base nos critérios citados em [jogos](jogos.md):
Baixa complexidade, jogabilidade alta, aplicabilidade conceitual e impacto social.

### Metodologia - COL

O Col, como citado em [jogos](jogos.md), é um jogo onde dois jogadores alternam turnos para colorir vértices de um grafo planar, seguindo regras de coloração.

A metodologia de desenvolvimento envolveu o **Método Iterativo com Prototipagem Rápida de Design**, citado no artigo 
"A formação do conceito de um jogo: Estudo de processos metodológicos para a criação de um game" por Cruz e Garone (2013).  
É um processo simples:

- Repetição: implementar → testar → ajustar.
- Enfatiza a experimentação e o aprendizado direto com o protótipo.
- Muito usado em jogos simples ou em fases iniciais de concepção.

A lógica de jogo original é basicamente a construção de um desenho com figuras geométricas básicas sobrepostas, onde os jogadores podem pintar as áreas desenhadas.  
Mas originalmente, o jogo é jogado em papel e só permite a participação de dois jogadores. Para este trabalho, a implementação foi diferente:

- As figuras foram construídas a partir de polígonos gerados pela biblioteca Pygame;
- Após desenhadas, as figuras foram remodeladas num grafo planar, permitindo a manipulação de vértices, arestas e o mais importante, as faces, que são interpretação visual das áreas desenhadas;
- O jogo foi adaptado para permitir a participação de mais de dois jogadores, aumentando a complexidade e a profundidade do jogo;
- A lógica de coloração foi a mesma, garantir que um jogador não possa colorir uma face que já foi colorida por outro jogador, e que duas faces adjacentes não possam ter a mesma cor.
- Mas para garantir um vencedor, o jogo foi adaptado para que, a cada jogada, fosse verificado o estado do jogo, de modo a eliminar os jogadores que não possuíssem jogadas possíveis, isto é, que não possuíssem faces que pudessem ser coloridas.  
- O jogo termina quando restar apenas um jogador, o vencedor.

No jogo, há algumas características de desenvolvimento, visualização e jogabilidade em destaque:

- O jogo foi desenvolvido e executado usando 7 arquivos Python: [constants.py](../main/src/constants.py), [shapes.py](../main/src/shapes.py), [menu.py](../main/src/menu.py), [graph.py](../main/src/graph.py), [planar_graph_convertion.py](../main/src/planar_graph_convertion.py), [game.py](../main/src/game.py) e [main.py](../main/src/main.py);
- Conforme o jogo, algumas mensagens são exibidas no console, como o estado do jogo, o jogador atual, as jogadas possíveis e o vencedor;
- O jogo permite a participação de 2 a 5 jogadores, cada um com uma cor;
- Há um tempo limite de 30 segundos para cada jogada, aumentando a pressão e a necessidade de decisões rápidas;
- Também há um limite de erros de 3 jogadas inválidas, o que elimina o jogador do jogo;
- Tanto o timer quanto o número de erros são exibidos na tela, para que o jogador possa se planejar;
- Quando apenas um jogador resta, o jogo termina e o vencedor é anunciado.

#### Ideias para melhorias futuras:

- Variar número de jogadores
- Variar número de figuras
- Variar número de times

###  Metodologia - SIM **[DESCARTADO]**

O SIM é um jogo de coloração de arestas, onde os jogadores devem colorir as arestas de um grafo completo $K_6$ de forma que não haja arestas adjacentes com a mesma cor.
Para o desenvolvimento do jogo SIM, será usada a linguagem Java, com o ajuda do framework libGDX.
**libGDX** é um framework de desenvolvimento de jogos em Java, que permite a criação de jogos de multiplataforma, com suporte a gráficos 2D e 3D, som e entrada de usuário.  
Ela tem uma documentação pouco conhecida, porém detalhada o suficiente para auxiliar na construção de um jogo de tais características.

O download do libGDX pode ser feito através do site oficial: [libGDX - Project Generation](https://libgdx.com/wiki/start/project-generation).

Outras referências são:

- [libGDX - Test Game - Repositório do autor, com jogo de teste com bolinha que se move](https://github.com/luc-gh/libGDX_testGame)
- [Hello World - libGDX - Repositório do autor, com implementações básicas](https://github.com/luc-gh/Hello-World_libGDX)
- [Input Data - libGDX - Repositório do autor, com conceito de entrada de dados](https://github.com/luc-gh/Input-Data_libGDX)
- [Graphics - libGDX - Repositório do autor, com conceitos de alterações no estado da tela](https://github.com/luc-gh/Graphics_libGDX)
- [Multiple Screens - libGDX - Repositório do autor, com conceitos do uso de múltiplas telas](https://github.com/luc-gh/Multiple-Screens_libGDX)

---

