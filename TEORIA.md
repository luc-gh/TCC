# Relações entre Conceitos Teóricos e Implementações no Projeto Jogo Col

## Introdução

O jogo Col representa uma implementação prática de múltiplos conceitos da matemática discreta e ciência da computação. Este documento estabelece as conexões diretas entre os fundamentos teóricos descritos no diretório `logica/` e suas aplicações concretas no código-fonte da pasta `src/`. O jogo é formalizado como um problema de coloração de faces em grafos planares, onde dois ou mais jogadores alternam turnos pintando regiões adjacentes com cores distintas.

> **Fig. 1**: Interface do Jogo Col  
> ![Fluxo do Jogo](main/assets/COL.png)

---

## 1. Lógica Proposicional e Validação de Jogadas

### Fundamentos Teóricos

A lógica proposicional modela cada estado do jogo através de proposições atômicas do tipo $P_{i,c}$: "a face $i$ está colorida com a cor $c$". O conjunto de proposições verdadeiras em um instante $t$ define o estado global do jogo:

$$\Gamma_t = \{P_{i,c} \mid \text{face } i \text{ possui cor } c \text{ no tempo } t\}$$

A restrição fundamental do jogo Col é expressa pela fórmula:
$$\forall (i,j) \in \text{Adjacentes}, \forall c \in \text{Cores}: \neg(P_{i,c} \land P_{j,c})$$

### Implementação Prática

```python
# game.py - Verificação de restrição lógica proposicional
for j, other in enumerate(graph.faces):
    if j == idx or other['color'] is None:
        continue
    # Extrai arestas das faces para detectar adjacência
    ov = other['vertices']
    edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) for i in range(len(ov)))
    # Aplica a restrição: ¬(P_{i,c} ∧ P_{j,c})
    if edges_f & edges_o and other['color'] == cor:
        bloqueado = True
        break
```

O algoritmo implementa a negação da conjunção, verificando que faces adjacentes (que compartilham arestas) não podem ter a mesma cor simultaneamente.

---

## 2. Inferências e Regras de Dedução

### Fundamentos Teóricos

O sistema de turnos utiliza regras de inferência para determinar jogadas válidas e condições de vitória. As principais regras aplicadas são:

1. **Modus Ponens**: Se $P_{jogador\_atual}$ (é a vez do jogador) e $\exists i: \text{MovimentoVálido}(i)$ então $\text{JogadaPossível}$
2. **Modus Tollens**: Se $\neg \text{JogadaPossível}$ então $\neg P_{jogador\_atual}$ (jogador é eliminado)
3. **Silogismo Disjuntivo**: Se $\text{JogadorAtivo}(A) \lor \text{JogadorAtivo}(B)$ e $\neg \text{JogadorAtivo}(A)$ então $\text{JogadorAtivo}(B)$

### Implementação Prática

```python
# game.py - Aplicação de regras de inferência
def player_can_move(idx):
    cor = constants.PLAYER_COLORS[idx]
    for face in graph.faces:
        if face['color'] is not None: continue
        # Verifica premissa: face disponível
        verts = face['vertices']
        edges_f = set(tuple(sorted((verts[i], verts[(i+1)%len(verts)]))) for i in range(len(verts)))
        blocked = False
        for other in graph.faces:
            if other is face or other['color'] is None: continue
            ov = other['vertices']
            edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) for i in range(len(ov)))
            # Aplica Modus Tollens: se bloqueado, nega a jogada
            if edges_f & edges_o and other['color'] == cor:
                blocked = True; break
        if not blocked:
            return True  # Conclusão: movimento possível
    return False

# Eliminação por Modus Tollens
for p in play.active_players.copy():
    if not player_can_move(p):
        play.active_players.remove(p)  # ¬JogadaPossível → ¬JogadorAtivo
```

---

## 3. Lógica de Predicados e Quantificadores

### Fundamentos Teóricos

O jogo utiliza predicados para expressar propriedades relacionais:

- $\text{Adjacente}(i,j)$: faces $i$ e $j$ compartilham pelo menos uma aresta
- $\text{Colorida}(i,c)$: face $i$ possui cor $c$
- $\text{Disponível}(i)$: face $i$ não foi colorida

A condição de fim de jogo é formalizada como:
$$\forall p \in \text{JogadoresAtivos}: \neg\exists i: (\text{Disponível}(i) \land \text{MovimentoVálido}(p,i))$$

### Implementação Prática

```python
# game.py - Quantificadores universais e existenciais
def qualquer_pode_jogar(graph: Graph):
    # ∃ jogador: ∃ face: MovimentoVálido(jogador, face)
    for i, cor in enumerate(constants.PLAYER_COLORS):
        for face in graph.faces:
            if i >= constants.temporary_number_of_players:
                break
            if face['color'] is not None:  # ¬Disponível(face)
                continue
            # ... verificação de bloqueio ...
            if not bloqueado:
                return True  # ∃ movimento válido
    return False  # ∀ jogadores: ¬∃ movimento válido
```

---

## 4. Álgebra de Conjuntos e Operações

### Fundamentos Teóricos

O estado do jogo é modelado através de conjuntos disjuntos:

- $F_c = \{i \mid \text{face } i \text{ tem cor } c\}$ para cada cor $c$
- $F_{\text{livres}} = \{i \mid \text{face } i \text{ não colorida}\} = V \setminus \bigcup_{c} F_c$

A adjacência entre faces é determinada pela interseção de conjuntos de arestas:
$$\text{Adjacente}(i,j) \iff E_i \cap E_j \neq \emptyset$$

onde $E_i$ é o conjunto de arestas da face $i$.

### Implementação Prática

```python
# game.py - Operações de conjuntos para detectar adjacência
# Conjunto de arestas da face clicada
edges_f = set(tuple(sorted((f_verts[i], f_verts[(i+1)%len(f_verts)]))) 
              for i in range(len(f_verts)))

# Conjunto de arestas da face comparada
edges_o = set(tuple(sorted((ov[i], ov[(i+1)%len(ov)]))) 
              for i in range(len(ov)))

# Interseção para detectar adjacência: E_i ∩ E_j ≠ ∅
if edges_f & edges_o and other['color'] == cor:
    bloqueado = True
```

```python
# planar_graph_convertion.py - União e diferença de conjuntos
vertices_set = set()
for seg in segments:
    vertices_set.update([seg[0], seg[1]])  # União de vértices
vertices = list(vertices_set)

# Construção de conjuntos de adjacência
adj = {i: [] for i in range(len(vertices))}
for a, b in edges:
    ia, ib = vid[a], vid[b]
    adj[ia].append(ib)  # Relação simétrica
    adj[ib].append(ia)
```

---

## 5. Teoria das Relações e Matriz de Adjacência

### Fundamentos Teóricos

A relação de adjacência $R_A \subseteq V \times V$ é:
- **Simétrica**: $(i,j) \in R_A \iff (j,i) \in R_A$
- **Anti-reflexiva**: $\forall i: (i,i) \notin R_A$
- **Binária**: cada par de faces ou é adjacente ou não é

A matriz de adjacência $M$ codifica esta relação: $M_{ij} = 1$ se $(i,j) \in R_A$, $0$ caso contrário.

### Implementação Prática

```python
# planar_graph_convertion.py - Construção da relação de adjacência
def detect_faces(vertices, edges):
    # Constrói dicionário de adjacência (relação simétrica)
    vid = {v: i for i, v in enumerate(vertices)}
    adj = {i: [] for i in range(len(vertices))}
    
    for a, b in edges:
        ia, ib = vid[a], vid[b]
        adj[ia].append(ib)  # (ia, ib) ∈ R_A
        adj[ib].append(ia)  # (ib, ia) ∈ R_A (simetria)
```

```python
# graph.py - Matriz de adjacência implícita através de interseção de arestas
def _faces_adjacentes(self, face1_idx, face2_idx):
    f1_verts = self.faces[face1_idx]['vertices']
    f2_verts = self.faces[face2_idx]['vertices']
    
    edges1 = set(tuple(sorted((f1_verts[i], f1_verts[(i+1)%len(f1_verts)]))) 
                 for i in range(len(f1_verts)))
    edges2 = set(tuple(sorted((f2_verts[i], f2_verts[(i+1)%len(f2_verts)]))) 
                 for i in range(len(f2_verts)))
    
    return bool(edges1 & edges2)  # M[i][j] = 1 se interseção não-vazia
```

---

## 6. Teoria dos Grafos: Planaridade e Coloração

### Fundamentos Teóricos

O jogo Col opera sobre grafos planares $G = (V,E)$ onde:
- $V$ representa as faces do desenho geométrico
- $E$ representa adjacências entre faces
- A planaridade é garantida pela construção geométrica (sem cruzamento de arestas)

O **Teorema das Quatro Cores** assegura que $\chi(G) \leq 4$ para qualquer grafo planar, mas o jogo impõe restrições mais severas ao permitir apenas 2-4 cores específicas e jogadas alternadas.

> **Fig. 2**: Exemplo de Grafo Planar  
> ![Grafo Planar](main/assets/Planar_graph.png)

### Implementação Prática

```python
# planar_graph_convertion.py - Construção de grafo planar
def extract_segments(shapes):
    """Extrai segmentos garantindo planaridade geométrica"""
    segments = []
    for shape in shapes:
        if shape['type'] == 'polygon':
            vertices = shape['vertices']
            # Adiciona arestas consecutivas (ciclo hamiltoniano)
            for i in range(len(vertices)):
                p1 = vertices[i]
                p2 = vertices[(i + 1) % len(vertices)]
                segments.append((p1, p2))
    return segments

def find_intersections(segments):
    """Detecta interseções preservando planaridade"""
    vertices = set()
    for seg in segments:
        vertices.update([seg[0], seg[1]])
    
    # Adiciona pontos de interseção
    intersections = set()
    for i, seg1 in enumerate(segments):
        for j, seg2 in enumerate(segments[i+1:], i+1):
            intersection = line_intersection(seg1, seg2)
            if intersection:
                intersections.add(intersection)
    
    vertices.update(intersections)
    return list(vertices)
```

```python
# graph.py - Construção e manipulação do grafo de faces
class Graph:
    def __init__(self, formas, area_minima_face=20):
        # Constrói grafo planar a partir de formas geométricas
        segmentos = extract_segments(shapes=self.formas)
        self.vertices = find_intersections(segmentos)
        self.arestas = split_segments(segmentos, self.vertices)
        faces_brutas = detect_faces(self.vertices, self.arestas)
        
        # Filtra faces por área mínima (remove artefatos)
        self.faces = []
        for lista_vertices in faces_brutas:
            area_face = self._calcular_area_poligono(lista_vertices)
            if area_face >= self.area_minima_face:
                self.faces.append({
                    'vertices': lista_vertices,
                    'color': None  # Estado inicial: não colorida
                })
```

---

## 7. Sistema de Turnos e Eliminação de Jogadores

### Fundamentos Teóricos

O sistema de turnos implementa uma máquina de estados finitos onde:
- **Estados**: conjuntos de jogadores ativos $S_t \subseteq \{1,2,\ldots,n\}$
- **Transições**: eliminação por tempo limite ou excesso de strikes
- **Estado final**: $|S_t| \leq 1$ (um ou nenhum jogador restante)

### Implementação Prática

```python
# game.py - Máquina de estados para turnos
# Inicialização do conjunto de jogadores ativos
if not hasattr(play, "active_players"):
    play.active_players = list(range(constants.temporary_number_of_players))
    play.turn_pos = 0
    play.strikes = {p: 0 for p in play.active_players}
    play.turn_start_time = pygame.time.get_ticks()

# Transição por timeout (30 segundos)
if remaining <= 0:
    play.strikes[current] += 1
    if play.strikes[current] >= 3:
        play.active_players.remove(current)  # Eliminação
        if play.active_players:
            play.turn_pos %= len(play.active_players)
    else:
        play.turn_pos = (play.turn_pos + 1) % len(play.active_players)

# Transição por jogada inválida
if edges_f & edges_o and other['color'] == cor:
    play.strikes[current] += 1
    if play.strikes[current] >= 3:
        play.active_players.remove(current)  # Eliminação por strikes

# Condição de parada: |S_t| ≤ 1
if len(play.active_players) <= 1:
    play.finished = True
    if len(play.active_players) == 1:
        play.winner = play.active_players[0]
    else:
        play.winner = play.last_player  # Último a jogar antes da eliminação geral
```

---

## 8. Geração Procedimental e Aleatoriedade

### Fundamentos Teóricos

A variabilidade do jogo é garantida pela geração aleatória de formas geométricas, criando diferentes instâncias do problema de coloração. Cada configuração produz um grafo planar único $G_i = (V_i, E_i)$.

### Implementação Prática

```python
# shapes.py - Geração procedimental de formas
def generate_random_shapes(num_shapes, screen_width, screen_height):
    shapes = []
    for _ in range(num_shapes):
        shape_type = random.choice(['rectangle', 'circle', 'polygon'])
        
        if shape_type == 'polygon':
            # Gera polígono convexo aleatório
            center = (random.randint(50, screen_width-50), 
                     random.randint(50, screen_height-50))
            num_vertices = random.randint(3, 8)
            radius = random.randint(30, 80)
            vertices = generate_convex_polygon(center, radius, num_vertices)
            shapes.append({'type': 'polygon', 'vertices': vertices})
    
    return shapes

# menu.py - Reinicialização para nova instância
if event.type == pygame.MOUSEBUTTONDOWN:
    if constants.PLAY_BUTTON.collidepoint(event.pos):
        # Gera novo grafo para cada partida
        formas = generate_random_shapes(constants.NUM_SHAPES, 
                                       constants.SCREEN_WIDTH, 
                                       constants.SCREEN_HEIGHT)
        graph = Graph(formas)
        return True, graph
```

---

## Síntese e Conclusões

O projeto Jogo Col demonstra como conceitos abstratos da matemática discreta se materializam em sistemas computacionais concretos:

1. **Lógica Proposicional** → **Validação de Estados**: Cada jogada é verificada através de fórmulas lógicas implementadas como condicionais no código.

2. **Inferências** → **Sistema de Turnos**: Regras de dedução determinam progressão do jogo e condições de vitória.

3. **Álgebra de Conjuntos** → **Detecção de Adjacência**: Operações de interseção identificam faces vizinhas através de arestas compartilhadas.

4. **Teoria das Relações** → **Representação de Dados**: Relações simétricas modelam a adjacência entre faces no grafo.

5. **Teoria dos Grafos** → **Estrutura de Dados**: Grafos planares organizam o espaço de jogo e suas restrições topológicas.

Cada módulo do código traduz fielmente os conceitos teóricos em algoritmos eficientes, evidenciando a correspondência direta entre formalismo matemático e implementação computacional. A complexidade emerge da interação entre essas camadas conceituais, criando um jogo estratégico fundamentado em sólidas bases teóricas.

> **Fig. 3**: Fluxo de Dados e Conceitos  
> ![Arquitetura](main/assets/flow.gif)

O resultado é um sistema que não apenas implementa as regras do jogo Col, mas serve como demonstração prática da aplicabilidade da matemática discreta em problemas computacionais reais.
