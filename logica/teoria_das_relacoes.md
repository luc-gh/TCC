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