# Lógica aplicada à computação

A lógica proposicional trabalha com cláusulas básicas: 
são sentenças atômicas simples (como P, Q, R) que podem ser apenas verdadeiras (V) ou falsas (F), 
e se combinam por meio de conectivos ($\neg, \land, \lor, \implies, \iff$).  
Não há variáveis ou quantificadores — cada proposição é uma unidade indivisível cujo valor é avaliado diretamente.

Já a lógica de predicados (ou lógica de primeira ordem) permite um nível muito mais expressivo: suas cláusulas utilizam predicados, que são funções que 
recebem variáveis (como $P(x)$ ou $R(x,y))$, e contam com quantificadores como $\forall$ (para todo) e $\exists$ (existe), o que possibilita formular 
afirmações sobre propriedades de objetos e relações entre eles.  
As variáveis podem ser vinculadas a elementos de um domínio, e é isso que a torna capaz de tratar de conceitos como “todos os humanos” ou 
“existe um número primo”, algo inacessível à lógica proposicional.

### Lógica dos predicados

Considere a descrição de proposições, citada no arquivo [logica_proposicional](logica_proposicional.md).  
Um predicado é uma expressão que atribui uma propriedade ou relação a um ou mais objetos. É como uma função que, ao receber objetos 
(ou variáveis que representam objetos), retorna um valor booleano (verdadeiro ou falso). É usado para relacionar proposições, basicamente. Por exemplo, em:

$$C(x): \text{x está claro.}$$

- $C$ é um predicado que expressa a propriedade “está claro”.
- $x$ é uma variável que representa um objeto qualquer do nosso domínio (um texto, uma explicação, um tópico, etc.).
- A expressão $C(x)$ é verdadeira se “x está claro” for verdadeiro, ou seja, se o objeto referenciado por $x$ realmente estiver claro.

No contexto da lógica de predicados, objetos são entidades do nosso universo de discurso, que pode incluir tudo aquilo sobre o qual queremos falar. Eles podem ser:

- Contundentes concretos: como “este livro”, “a lua”.
- Entidades abstratas: como “o conjunto vazio”, “a paz”.
- Fictícios ou hipotéticos: como “unicórnio”, “Saci Pererê”.
- Também podem ser átomos (por exemplo, uma tecla) ou compostos (como um teclado inteiro).

Exemplos de objetos são:

- $C(a)$
- $C(dia)$
- $\neg C(y)$
- $F(\text{"Saci Pererê"})$

### Dedução natural

Dedução Natural é um sistema formal de prova em que construímos argumentos “de dentro para fora”: abrimos hipóteses, aplicamos regras de inferência 
para obter novas fórmulas e, ao encerrar uma hipótese, extraímos as implicações correspondentes.  
As regras de inferência que usamos aqui são as do arquivo 
[inferencias](inferencias.md) — Adição, Simplificação, Conjunção, Modus Ponens, Modus Tollens, Silogismo Disjuntivo e Silogismo Hipotético — mais 
a regra de HPPC (Hipótese Para Prova de Condicional), que explicarei a seguir.

Quando aplicada à lógica proposicional, a dedução natural só lida com proposições atômicas e conectivos ($\neg, \land, \lor, \implies, \iff$). 
Já na lógica de predicados, somam‑se as regras para manipular quantificadores (∀, ∃) e variáveis livres, o que exige cuidados extras de escopo e de 
“variáveis próprias” ao introduzir e eliminar quantificadores, mas mantém a mesma estrutura de assumir hipóteses e aplicar regras.

#### Exemplo 1 (Lógica proposicional)

Suponha que tem-se as premissas $P \implies Q, Q \implies R, R \implies S, S \implies T$ e se quer provar que $P \implies T$. O processo lógico se dá na seguinte ordem:

$$
\{P \implies Q, Q \implies R, R \implies S, S \implies T \} \models P \implies T
$$
$$
\begin{array}{ l l | l }
 \hspace{4px} 1. & P \implies Q & Pr  \\ 
 \hspace{4px} 2. & Q \implies R & Pr  \\  
 \hspace{4px} 3. & R \implies S & Pr  \\
 \hspace{4px} 4. & S \implies T & Pr  \\
 \hspace{4px} 5. & | \hspace{4px}  P & Hip  \\
 \hspace{4px} 6. & | \hspace{4px}  Q & 1 \hspace{4px} , 5 \hspace{6px}  MP  \\
 \hspace{4px} 7. & | \hspace{4px}  R & 2 \hspace{4px} , 6 \hspace{6px}  MP  \\
 \hspace{4px} 8. & | \hspace{4px}  S & 3 \hspace{4px} , 7 \hspace{6px}  MP  \\
 \hspace{4px} 9. & | \hspace{4px}  T & 4 \hspace{4px} , 8 \hspace{6px}  MP  \\
 \hspace{4px} 10. & P \implies T & 5-9 \hspace{6px}  HPPC  \\
\end{array}
$$

#### Exemplo 2 (Lógica proposicional)

Dada a proposição $A \implies B$, prove que $(A \lor C) \implies (B \lor C)$.

$$
\{A \implies B\} \models (A \lor C) \implies (B \lor C)
$$
$$
\begin{array}{ l l | l }
  \hspace{4px} 1. & A \implies B & Pr  \\ 
  \hspace{4px} 2. & | \hspace{4px}  A \lor C & Hip  \\  
  \hspace{4px} 3. & || \hspace{4px}  \neg C & Hip  \\
  \hspace{4px} 4. & || \hspace{4px}  A & 2 \hspace{4px}, 3 \, \hspace{4px}  SD  \\
  \hspace{4px} 5. & || \hspace{4px}  B & 4 \hspace{4px}, 1 \, \hspace{4px}  MP  \\
  \hspace{4px} 6. & || \hspace{4px}  B \lor C & 5 \, \hspace{4px}  I  \hspace{4px} \lor  \\
  \hspace{4px} 7. & |  \hspace{4px}  \neg C \implies B \lor C & 3-6 \, \hspace{4px}  HPPC  \\
  \hspace{4px} 8. & || \hspace{4px}  C & Hip  \\
  \hspace{4px} 9. & || \hspace{4px}  C \lor B & 8 \, \hspace{4px}  I  \hspace{4px}  \lor  \\
  \hspace{4px} 10. & | \hspace{4px}  C \implies C \lor B & 8-9 \, \hspace{4px}  HPPC  \\
  \hspace{4px} 11. & | \hspace{4px}  C \lor \neg C & 3 \hspace{4px} ,8\,\,\, \hspace{4px}  \top  \\
  \hspace{4px} 12. & | \hspace{4px} B \lor C & 7 \hspace{4px} ,10 \hspace{4px} , 11 \hspace{4px} E  \hspace{4px}  \lor  \\
  \hspace{4px} 13. & (A \lor C) \implies (B \lor C) & 2\,,12\, \hspace{4px}  HPPC  \\
\end{array}
$$


### Quantificadores lógicos

Em Lógica de Predicados, estendemos a Lógica Proposicional para falar sobre “todos” ou “pelo menos um” elemento de um domínio. Para isso usamos dois operadores:

> #### Universal ($\forall$)
> 
> $$\forall x \ B(x)$$
> 
> Significa “**para todo** $x$ no universo de discurso, a fórmula $B(x)$ é verdadeira”. Onde:
> 
> - Domínio: conjunto de todos os objetos que $x$ pode assumir.
> - Semântica: $\forall x \ B(x)$ é verdadeiro somente se $B(d)$ for verdadeiro para cada $d$ no domínio.

> #### Existencial ($\exists$)
> 
> $$\exists x \ B(x)$$
> 
> Significa “existe pelo menos um $x$ no universo de discurso tal que $B(x)$ é verdadeiro". Onde:
> 
> - Semântica: $\exists x \ B(x)$ é verdadeiro somente se existe algum $d$ no domínio que torne $B(d)$ verdade.

Alguns outros conceitos:

- **Predicado**:
É uma expressão que associa verdadeiro ou falso a cada tupla de argumentos.
 
  Ex.:
  $B(x)$ pode significar “$x$ é par”.

- **Conjunto (ou domínio de discurso)**:
Coleção de objetos sobre os quais as variáveis podem “varrer”.

  Ex.:
  $C = {2, 3, 4, 9, 101, 2000}$

- **Constantes**:
Símbolos que se referem a elementos fixos do domínio.

  Ex.:
  $0, 1, \pi, Alice$

- **Variáveis**:
Símbolos que podem assumir qualquer valor do domínio.

  Ex.:
  $x, y, w$

- **Funções**:
Mapeiam tuplas de elementos do domínio para um elemento do domínio.

  Ex.:
  $$f(x,y) = x + y$$
  $$M(x,y) = x > y$$

> ### Exemplo
> 
> Seja $C$ um conjunto tal que: $$C=\{2,3,4,9,101,2000\}$$
> 
> Dada a função $M(x,y):$ $x$ é maior que $y$ (ou $x>y$), tem-se que:
> 
> - $\forall x \ M(x,10): \bot$ 
> - $\forall w \ M(10,w): \bot $
> - $\exists y \ M(10,y): \top$
> - $\exists x \ M(x,10): \top$
