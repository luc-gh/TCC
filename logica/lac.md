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
 \,1. & P \implies Q & Pr  \\ 
 \,2. & Q \implies R & Pr  \\  
 \,3. & R \implies S & Pr  \\
 \,4. & S \implies T & Pr  \\
 \,5. & | \, P & Hip  \\
 \,6. & | \, Q & 1\,,\,5 \,\, MP  \\
 \,7. & | \, R & 2\,,\,6 \,\, MP  \\
 \,8. & | \, S & 3\,,\,7 \,\, MP  \\
 \,9. & | \, T & 4\,,\,8 \,\, MP  \\
 \,10. & P \implies T & 5-9 \,\, HPPC  \\
\end{array}
$$

#### Exemplo 2 (Lógica proposicional)

Dada a proposição $A \implies B$, prove que $(A \lor C) \implies (B \lor C)$.

$$
\{A \implies B\} \models (A \lor C) \implies (B \lor C)
$$
$$
\begin{array}{ l l | l }
 \,1. & A \implies B & Pr  \\ 
 \,2. & | \, A \lor C & Hip  \\  
 \,3. & || \, \neg C & Hip  \\
 \,4. & || \, A & 2\,,\,3 \,\, SD  \\
 \,5. & || \, B & 4\,,\,1 \,\, MP  \\
 \,6. & || \, B \lor C & 5 \,\, I \,\lor  \\
 \,7. & | \, \neg C \implies B \lor C & 3-6 \,\, HPPC  \\
 \,8. & || \, C & Hip  \\
 \,9. & || \, C \lor B & 8 \,\, I \, \lor  \\
 \,10. & | \, C \implies C \lor B & 8-9 \,\, HPPC  \\
 \,11. & | \, C \lor \neg C & 3\,,8\,\,\,\, \top  \\
 \,12. & | \, B \lor C & 7\,,10\,,11\,\, E \, \lor  \\
 \,13. & (A \lor C) \implies (B \lor C) & 2\,,12\,\, HPPC  \\
\end{array}
$$


### Quantificadores lógicos


