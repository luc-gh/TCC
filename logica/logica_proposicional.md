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

### Formalização de argumentos

Podemos usar a lógica proposicional para formalizar um argumento. No processo de formalização, devemos reconhecer as 
proposições e conectivos que compõem o argumento, de modo que possamos expressá‑lo usando fórmulas bem‑formadas.

Como exemplo, vamos formalizar o seguinte argumento:

1. Se o time joga bem, ganha o campeonato.
2. Se o time não joga bem, o técnico é culpado.
3. Se o time ganha o campeonato, os torcedores ficam contentes.
4. Os torcedores não estão contentes.
5. Logo, o técnico é culpado.

Primeiro, associamos a cada proposição um símbolo proposicional distinto:

- $p$ : “o time joga bem”
- $q$ : “o time ganha o campeonato”
- $r$ : “o técnico é culpado”
- $s$ : “os torcedores ficam contentes”

Em seguida, usando esses símbolos, escrevemos as fórmulas correspondentes às sentenças do argumento:

- $p \implies q$
- $\neg p \implies q$
- $q \implies s$
- $\neg s$
- $r$ 

Finalmente, podemos representar todo o argumento de forma abreviada:

$$
\{ p \implies q, \neg p \implies r, q \implies s, \neg s \} \models r
$$

sendo que a notação “$\Delta \models \phi $” estabelece que a fórmula $\phi$ é uma consequência lógica do conjunto de fórmulas $\Delta$.

### Tabela verdade

A tabela-verdade é uma ferramenta sistemática para verificar como o valor de uma fórmula lógica varia conforme as combinações de proposições de valor verdadeiro e falso de suas variáveis.

Na prática, ela é uma tabela que resume a validade de todas as combinações de símbolos ou fórmulas que compõem uma fórmula geral.  
Por exemplo, leve conta a expressão $\neg a \,\lor\, b \implies c$. A tabela-verdade para essa fórmula é:

|  $a$   |  $b$   |  $c$   | $\neg a$ <br> _"<u>não</u> a"_ | $\neg a \,\lor\, b$ <br> _"não a <u>ou</u> b"_ | $\neg a \,\lor\, b \implies c$ <br> _"não a ou b, <u>então</u> c"_ |
|:------:|:------:|:------:|:------------------------------:|:----------------------------------------------:|:------------------------------------------------------------------:|
| $\bot$ | $\bot$ | $\bot$ |             $\top$             |                     $\top$                     |                               $\bot$                               |                                |                                          |
| $\bot$ | $\bot$ | $\top$ |             $\top$             |                     $\top$                     |                               $\top$                               |                                |                                          |
| $\bot$ | $\top$ | $\bot$ |             $\top$             |                     $\top$                     |                               $\bot$                               |                                |                                          |
| $\bot$ | $\top$ | $\top$ |             $\top$             |                     $\top$                     |                               $\top$                               |                                |                                          |
| $\top$ | $\bot$ | $\bot$ |             $\bot$             |                     $\bot$                     |                               $\top$                               |
| $\top$ | $\bot$ | $\top$ |             $\bot$             |                     $\bot$                     |                               $\bot$                               |
| $\top$ | $\top$ | $\bot$ |             $\bot$             |                     $\top$                     |                               $\bot$                               |
| $\top$ | $\top$ | $\top$ |             $\bot$             |                     $\top$                     |                               $\top$                               |

Observe atentamente a lógica para os operadores $\implies$ e $\iff$. No caso acima, a expressão $\neg a \,\lor\, b \implies c$ 
só assume o valor verdadeiro quando a expressão à direita, chamada _consequência_, é resultado direto (assume o mesmo valor) da expressão à esquerda.  
Ou seja, até quando ambas assumem o valor $\bot$, a expressão por completo será verdade, pois **é verdade afirmar** que **algo falso** leva a **uma consequência falsa**.

### Tautologia, Contradição & Contingência

Algumas fórmulas, por coincidência ou não, acabam gerando tabelas cujos valores-verdade assumem apenas valores verdadeiros.  
Quando isso acontece, a fórmula em questão é denominada **tautologia**. 

No caso totalmente oposto, quando todos os valores assumem a constante falsa, a fórmula é denominada **contradição**.  
E quando há uma mistura entre valores verdadeiros e falsos nos resultados da tabela, a fórmula é chamada de **contingência**.

Na seção seguinte as tabelas que mostram outros conceitos serão exemplos dos 3 casos.

### Leis de De Morgan, Lei do terceiro excluído e outros valores para constantes

Nas tabelas-verdade, pode-se utilizar outros símbolos para representar as valores "verdadeiro" e "falso".  
Os símbolos $\top$ e $\bot$ são formais, mas pouco usados já que não são tão triviais.

Em muitos contextos, "verdadeiro" pode ser representado com as letras "V" ou "T" e também o valor 1.  
E "falso", de modo similar, pelos símbolos "F" ou o valor 0.

Vamos usar de exemplo a **lei do terceiro excluído** (do latim _tertium non datur_), que diz que 
para qualquer proposição, ou esta proposição é verdadeira, ou sua negação é verdadeira. Ou seja, seja $A$ uma proposição.
$A$ pode ser verdadeiro. Se não for, $\neg A$ tem que ser verdadeiro, pois não existe uma terceira opção. Na tabela-verdade, isso se verifica assim:

|  $A$   | $\neg A$ | $\,$ | $A$ | $\neg A$ | $\,$ | $A$ | $\neg A$ | 
|:------:|:--------:|:----:|:---:|:--------:|:----:|:---:|:--------:|
| $\top$ |  $\bot$  | $\,$ |  V  |    F     | $\,$ |  1  |    0     | 
| $\bot$ |  $\top$  | $\,$ |  F  |    V     | $\,$ |  0  |    1     | 

Observe que o uso de diferentes representações dos valores-verdade não altera o sentido dos conceitos aplicados.

Com isso em vista, para a lógica proposicional, as leis de De Morgan (1806-1871) são inferências que se estabelecem como variações de uma mesma expressão, 
envolvendo os operadores $\lor$ e $\land$. As duas regras são:

$$
\neg (X \lor Y) \iff (\neg X) \land (\neg Y) \,\,\,\,\,\text{ }\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \neg (X \land Y) \iff (\neg X) \lor (\neg Y)
$$



