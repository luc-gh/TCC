# Lógica proposicional

A lógica proposicional é um formalismo matemático que nos permite abstrair a estrutura de um argumento, eliminando a ambiguidade da linguagem natural. Esse formalismo é composto por:

1. **Uma linguagem formal**, na qual as proposições são expressas por símbolos e conectivos lógicos.
2. **Um conjunto de regras de inferência**, que nos permitem analisar um argumento de forma precisa e decidir sua validade.

Informalmente, um argumento é uma sequência de premissas seguida de uma conclusão. Dizemos que um argumento é **válido** quando sua conclusão é uma consequência necessária de suas premissas.

**Exemplo:**

1. Sempre que chove, o trânsito fica congestionado.
2. Está chovendo muito.
3. Logo, o trânsito deve estar congestionado.

Esse argumento é válido porque, dadas as premissas, a conclusão decorre inevitavelmente delas.

---

### Proposição

Uma proposição é uma declaração afirmativa à qual se pode associar um valor
verdadeiro ou falso, mas não ambos.

Ou seja, ela não precisa ser verdadeira para ser considerada uma proposição válida.  
O que importa é que ela esteja rotulada e que tenha potencial para ser verdadeira ou falsa.

As proposições são consideradas _atômicas_.  
Isso significa que elas são indivisíveis: para o próprio sistema lógico, 
ou para um programa de computador, elas são simplesmente um fragmento opaco de verdade
(ou falsidade) rotulado como “A” ou qualquer outro símbolo. 

Podem-se definir e rotular proposições, mas nenhuma têm conexão com as outras, de forma imediata.  
Para relacioná-las, usam-se os chamados **operadores lógicos**, também chamados de **conectivos lógicos**, 
com os quais se pode construir construções compostas a partir de múltiplas proposições.

Para usá-los de maneira matemática, são introduzidos também as constantes $\bot$ (*falso*) e $\top$ (*verdadeiro*)
e os símbolos proposicionais (i.e., letras do alfabeto latino, possivelmente indexadas). Dessa forma, 
a sintaxe da lógica proposicional constitui-se de:

|           Símbolo            |                  Significado                  | Natureza              |
|:----------------------------:|:---------------------------------------------:|-----------------------|
|            $\bot$            |                *FALSO (false)*                | Constante             |
|            $\top$            |              *VERDADEIRO (true)*              | Constante             |
|            $\neg$            |                   não (not)                   | Operador lógico       |
|           $\land$            | e (and) $\text{ ou }$ conjunção (conjunction) | Operador lógico       |
|            $\lor$            | ou (or) $\text{ ou }$ disjunção (disjunction) | Operador lógico       |
|           $\oplus$           |              ou exclusivo (xor)               | Operador lógico       |
|      $A,a,B,b,C,c, ...$      |                  proposições                  | Símbolo proposicional |
| $\alpha, \beta, \gamma, ...$ |                   fórmulas                    | Fórmula bem-formada   |
|          $\implies$          |                    implica                    | Operador lógico       |
|            $\iff$            |          bi-implica ou equivalente a          | Operador lógico       |



