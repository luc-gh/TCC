# Relações

### Relação

Dado um conjunto $S$, uma relação $\rho$ é qualquer subconjunto de $S \times S$; isto é, um conjunto de pares ordenados 
cuja presença indica que os elementos estão “relacionados” segundo algum critério.  
Em geral, uma relação pode ainda ser definida entre conjuntos diferentes $S$ e $T$, como $\rho \subseteq S \times T$.

> #### Exemplo 
> Relação “menor que” em $\mathbb{N}$:
> $$\{(1,2),(1,3),(2,3),\dots\} \subseteq \mathbb{N} \times \mathbb{N}$$

### Relação Binária

É uma relação definida entre dois conjuntos (ou entre um conjunto e ele mesmo). Formalmente, $\rho \subseteq S \times T$.  
Pode-se caracterizá‑la por enumeração de pares, por fórmula relacional ou por compreensão de conjunto.

> #### Exemplo 
> Em $S=\{1,2\}, T=\{2,3\}$, a relação “soma é ímpar” é $$\{(1,2),(2,3)\}$$

### Relação N‑ária

Generaliza-se a $n$-ária definindo $\rho \subseteq S_1 \times S_2 \times \dots \times S_n$. Uma tupla $(s_1, s_2, \dots, s_n)$ 
pertence à relação se satisfizer um predicado sobre esses $n$ elementos.

> #### Exemplo
> Em $A=\{1,2\},B=\{2\},C=\{2, 3\}$, a relação $\rho(x,y,z) \iff x = y = z$ tem $\{(2,2,2)\}$.

### Relação Unária
Caso especial com $n=1$: um subconjunto particular de $S$ que identifica elementos que satisfazem uma propriedade.

> #### Exemplo
> Conjunto dos pares em $\mathbb{N}: \{x \in \mathbb{N} \hspace{5px}\vert\hspace{5px} x \text{ é par} \}$

### Tipos Segundo Cardinalidade

Classifica-se $\rho \subseteq S \times T$ em:

- Um‑para‑um (injetora): cada $s \in S$ e $t \in T$ aparece no máximo uma vez.
- Um‑para‑muitos: algum $s$ emparelha-se com vários $t$.
- Muitos‑para‑um: vários $s$ emparelham-se com mesmo $t$.
- Muitos‑para‑muitos: combinação de ambos.

> #### Exemplo
> O conjunto $\{(2,4), (3,4), (5,2)\}$ é “muitos‑para‑um” em $S=\{2,3,5\}, T=\{2,4\}$.


Para $\rho, \sigma \subseteq S^2$, definem‑se:

- **União:** $x (\rho \cup \sigma) y \;\iff\; x \rho y \;\lor\; x \sigma y$.
- **Interseção:** $x (\rho \cap \sigma) y \;\iff\; x \rho y \;\land\; x \sigma y$.
- **Complemento:** $x \rho' y \;\iff\; \neg\bigl(x \rho y\bigr)$.
- **Composição:** $\rho \circ \sigma \;=\; \{(x, z) \mid \exists\,y:\; x \sigma y \;\land\; y \rho z\}$.

> **Exemplo**  
> Se $\sigma = \{(1,2)\} \text{ e } \rho = \{(2,3)\}$,  
> então $\rho \circ \sigma = \{(1,3)\}$.

### Relação Inversa (Conversa)

A conversa de $\rho\subseteq S\times T$ é
$$
\rho^{-1}=\{(y,x)\mid (x,y)\in\rho\}.
$$

> **Exemplo**  
> Inversa de “é filho de” é “é pai/mãe de”.

---

### Propriedades Fundamentais

Em $\rho\subseteq S^2$:

- Reflexiva: $\forall x\in S:\;x\rho x$.
- Irreflexiva: $\forall x:\;\neg(x\rho x)$.
- Simétrica: $x\rho y\;\Rightarrow\;y\rho x$.
- Anti‑simétrica: $x\rho y\land y\rho x\;\Rightarrow\;x=y$.
- Assimétrica: $x\rho y\;\Rightarrow\;\neg(y\rho x)$.
- Transitiva: $x\rho y\land y\rho z\;\Rightarrow\;x\rho z$.

> **Exemplo**  
> $\le$ em $\mathbb{N}$ é reflexiva, anti‑simétrica e transitiva.

---

### Fecho de uma Relação

Dada $\rho\subseteq S^2$ sem certa propriedade $P$, seu fecho $\rho^*$ é o menor super‑conjunto de $\rho$ que satisfaz $P$:
$$
\rho^*=\bigcap_{\substack{\sigma\supseteq\rho\\\sigma\text{ satisfaz }P}}\sigma.
$$

> **Exemplo**  
> Fecho transitivo de $\{(1,2),(2,3)\}$ em $\{1,2,3\}$ é $\{(1,2),(2,3),(1,3)\}$.

---

### Relação de Equivalência

Relação binária que é reflexiva, simétrica e transitiva. Particiona $S$ em classes de equivalência.

> **Exemplo**  
> Em $X=\{a,b,c\}$,  
> $R=\{(a,a),(b,b),(c,c),(b,c),(c,b)\}$  
> produz as classes $\{a\}$ e $\{b,c\}$.

---

### Ordem Parcial e Total

- **Ordem Parcial:** relação reflexiva, anti‑simétrica e transitiva em $S$ (um poset).  
- **Ordem Total:** ordem parcial que, além disso, satisfaz conectividade forte: para todo $x,y$, $x\rho y$ ou $y\rho x$.

> **Exemplo**  
> $(\mathbb{N},\le)$ é ordem total;  
> $(\mathcal{P}(\{1,2\}),\subseteq)$ é apenas parcial.

---

### Diagrama de Hasse

Representação gráfica de um poset finito, omitindo arestas redundantes (transitivas) e orientando‑as para cima.

> **Exemplo**  
> Diagrama de Hasse de $\{1,2,3,6,12\}$ sob divisibilidade ($\mid$) mostra as relações entre esses números.
````mermaid
graph LR
    12["12"]
    6["6"]
    3["3"]
    2["2"]
    1["1"]

    1 --> 2
    1 --> 3
    2 --> 6
    3 --> 6
    6 --> 12
````


## Teoria dos grupos


## 1. Estruturas Algébricas Básicas

### 1.1 Semigrupo

- **Definição**  
  Um _semigrupo_ é um par $(S, \omicron)$ onde:
  1. **Fechamento**: para todo $a,b \in S$, $a \omicron b \in S$.  
  2. **Associatividade**: para todo $a,b,c \in S$,  
     $(a \omicron b) \omicron c = a \omicron (b \omicron c).$

- **Exemplo**  
  $\{1,2,3,\dots\}$ com a operação $+$ (adição) é semigrupo:
  - Fechamento: $1 + 2 = 3 \in \mathbb{N}$.  
  - Associativo: $(1 + 2) + 3 = 1 + (2 + 3)$.

---

### 1.2 Monóide

- **Definição**  
  Um _monóide_ é um semigrupo que possui um **elemento identidade** $e\in S$ tal que, para todo $a\in S$:
  $
    a \omicron e = e \omicron a = a.
  $

- **Exemplo**  
  $\{1,2,3,\dots\}$ com $\times$ (multiplicação) é um monóide:
  - Fechamento e associatividade vêm de $\mathbb{N}$.  
  - Identidade: $e = 1$, pois $a \times 1 = a$.

---

### 1.3 Grupo

- **Definição**  
  Um _grupo_ é um monóide em que **todo** elemento $a\in G$ possui um **inverso** $a^{-1}\in G$ tal que:
  $
    a \ominus a^{-1} = a^{-1} \ominus a = e,
  $
  onde $e$ é a identidade.  
  Assim, um grupo $(G,\ominus)$ satisfaz:
  1. **Fechamento**  
  2. **Associatividade**  
  3. **Elemento identidade** $e$  
  4. **Inverso** para cada $a\in G$

- **Ordem**  
  - **Ordem do grupo**: número de elementos de $G$.  
  - **Ordem de um elemento** $a$: menor inteiro $n>0$ tal que $a^n = e$.

- **Exemplo**  
  Conjunto de matrizes invertíveis $N\times N$ sobre um corpo, com multiplicação:
  - Fechamento e associatividade pela multiplicação de matrizes.  
  - Identidade: matriz identidade $I$.  
  - Inverso: cada matriz não‑singular tem inversa.

---

### 2. Grupo Abéliano (Comutativo)

- **Definição**  
  Um _grupo abéliano_ (ou comutativo) é um grupo $(G,\oplus)$ que satisfaz também:
  $$a \oplus b = b \oplus a,\quad \forall\,a,b\in G$$.

- **Exemplo**  
  \((\mathbb{Z}, +)\) é abeliano:
  - Fechamento, associatividade, identidade \(0\), inverso \(-a\).  
  - Comutatividade: \(a + b = b + a\).

---

### 3. Subgrupo e Grupo Cíclico

#### 3.1 Subgrupo

- **Definição**  
  $H$ é um _subgrupo_ de $G$ $(H \le G$) se:
  1. $H \subseteq G$.  
  2. $H$ com a mesma operação de $G$ forma um grupo (fechamento, identidade, inversos e associatividade).

- **Subgrupo Próprio**  
  $H < G$ indica subgrupo que não é todo o $G$.

- **Exemplo**  
  Em $G = \{1,\,i,\,-1,\,-i\}$ (sob $\times$),  
  - $H_1 = \{1\}$ e $H_2 = \{1,-1\}$ são subgrupos.  
  - $H_3 = \{1,i\}$ **não** é subgrupo ($i^{-1} = -i \notin H_3$).

---

#### 3.2 Grupo Cíclico

- **Definição**  
  Um grupo $G$ é _cíclico_ se existe $g\in G$ (gerador) tal que: $G = \{g^n \mid n\in\mathbb{Z}\}$.

- **Observação**  
  Todo grupo cíclico é abeliano, mas o recíproco não é sempre verdadeiro.

- **Exemplo**  
  $G = \{1, -1, i, -i\}$ sob multiplicação é cíclico:  
  - Geradores: $i$ e $-i$ pois  
    $
      i^1 = i,\; i^2 = -1,\; i^3 = -i,\; i^4 = 1.
    $

---

### 4. Exemplos e Contra‑exemplos em \(\mathbb{N}\) e \(\mathbb{Z}\)

| Estrutura  | Símbolo                            | Propriedades                                                        | Fechamento em $\mathbb{N}$? | Inverso em $\mathbb{N}$? |
|------------|------------------------------------|---------------------------------------------------------------------|-----------------------------|--------------------------|
| Semigrupo  | $\mathbb{N}, +$                    | Fechamento, Associatividade                                         | Sim                         | Não (não há inverso)     |
| Monóide    | $\mathbb{N}, \times$               | Fechamento, Associatividade, Identidade ($1$)                       | Sim                         | Não (não há inverso)     |
| Grupo      | $\mathbb{Z}, +$                    | Fechamento, Associatividade, Identidade ($0$), Inverso ($-a$)       | —                           | Sim                      |
| Grupo      | $\mathbb{Z}\setminus\{0\}, \times$ | Não é fechado (por 0), nem tem identidade universal na versão sem 0 | Não                         | Não aplica               |

---

### 5. Resumo das Propriedades

Para um conjunto $G$ com operação $\circ$:

1. **Fechamento**  
   $\forall\,a,b\in G,\;a\circ b\in G$.

2. **Associatividade**  
   $\forall\,a,b,c\in G,\;(a\circ b)\circ c = a\circ(b\circ c)$.

3. **Identidade**  
   $\exists\,e\in G$ tal que \(\forall\,a\in G,\;e\circ a = a\circ e = a\).

4. **Inverso**  
   $\forall\,a\in G,\;\exists\,a^{-1}\in G$ com $a\circ a^{-1} = a^{-1}\circ a = e$.

5. **Comutatividade** (para grupo abeliano)  
   $\forall\,a,b\in G,\;a\circ b = b\circ a$.