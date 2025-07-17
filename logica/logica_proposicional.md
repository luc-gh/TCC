# Lógica proposicional

A *lógica* pode ser dividida em duas subáreas gerais: 

- A **lógica dedutiva**, baseada em observações;
- A **lógica indutiva**, que não possui baseamento visual.

A lógica proposicional é um formalismo matemático que nos permite abstrair a estrutura de um argumento, eliminando a ambiguidade da linguagem natural. 
Ou seja, ela se compõe com os princípios da lógica dedutiva.  
Esse formalismo é composto por:

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

Uma proposição ou premissa é uma declaração afirmativa à qual se pode associar um valor
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

|           Símbolo            |                  Significado                  | Natureza                       |
|:----------------------------:|:---------------------------------------------:|--------------------------------|
|            $\bot$            |                *FALSO (false)*                | Constante ou **Valor-verdade** |
|            $\top$            |              *VERDADEIRO (true)*              | Constante ou **Valor-verdade** |
|            $\neg$            |                   não (not)                   | Operador lógico **unário**     |
|           $\land$            | e (and) $\text{ ou }$ conjunção (conjunction) | Operador lógico                |
|            $\lor$            | ou (or) $\text{ ou }$ disjunção (disjunction) | Operador lógico                |
|           $\oplus$           |              ou exclusivo (xor)               | Operador lógico                |
|      $A,a,B,b,C,c, ...$      |                  proposições                  | Símbolo proposicional          |
| $\alpha, \beta, \gamma, ...$ |                   fórmulas                    | *Fórmula bem-formada*          |
|          $\implies$          |                    implica                    | Operador lógico                |
|            $\iff$            |          bi-implica ou equivalente a          | Operador lógico                |

> Uma fórmula bem formulada é uma fórmula sintaticamente correta.
> 1. $A...Z$ ou $a...z$ são fórmulas bem formuladas.
> 2. Se $\alpha$ é uma fórmula bem formulada, $\neg \alpha$ também é.
> 3. Se $\alpha$ e $\beta$ são fórmulas bém formuladas, então $\alpha \land \beta$, $\alpha \lor \beta$, $\alpha \implies \beta$ e $\alpha \iff \beta\,$ também são.
> 
> Um operador unário é aquele que se refere a um único elemento, apenas.

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
- $\neg p \implies r$
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

> OBS: no uso do operador $\implies$, os termos que compõem a fórmula tem nomes especiais que serão úteis adiante.  
> Na **implicação** $$a \implies b$$ 
> - $a$ é denominada **_hipótese_**, que é aquilo que se propõe.
> - e $b$ é denominada **_tese_**, que é aquilo que se conclui.
> 
> Já a operação $\iff$ consiste na prática junção de duas implicações de ordem inversa, onde ambas as fórmulas envolvidas são tanto hipóteses quanto teses:
> $$ (A \implies B) \land (B \implies A) \equiv A \iff B $$

### Problemas de satisfatibilidade

Algumas fórmulas, por coincidência ou não, acabam gerando tabelas cujos valores-verdade assumem apenas valores verdadeiros.  
Quando isso acontece, a fórmula em questão é denominada **tautologia** e é chamada também de <u>*fórmula válida*</u>.

No caso totalmente oposto, quando todos os valores assumem a constante falsa, a fórmula é denominada **contradição**. Além disso,
é dito que a fórmula, nesse caso, é <u>*insatisfatível*</u>.

E quando há uma mistura entre valores verdadeiros e falsos nos resultados da tabela, a fórmula é chamada de **contingência**.  
Para esses casos, duas denominações descritivas também são aceitas:

- Fórmula <u>*satisfatível*</u>: que admite ao menos uma interpretação verdadeira (um valor-verdade, dentre os possíveis, é verdadeiro)
- Fórmula <u>*inválida*</u>: onde ao menos uma possibilidade é falsa.

Na seção seguinte as tabelas que mostram outros conceitos serão exemplos dos 3 casos.

### Leis lógicas, Leis de De Morgan, Lei do terceiro excluído e outros valores para constantes

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

Além desse princípio lógico, outras 3 fórmulas são tratadas como leis lógicas, pois são tautologias claras e absolutas:

$$
\neg \neg A \equiv A \hspace{100px} A \implies B \equiv \neg A \lor B \hspace{100px} A \implies B \implies C \equiv A \implies (B \implies C)
$$

Mais a frente serão citadas as regras de precedência.

Com isso em vista, para a lógica proposicional, as leis de De Morgan (1806-1871) são inferências que se estabelecem como variações de uma mesma expressão, 
envolvendo os operadores $\lor$ e $\land$. As duas regras são:

$$
\neg (X \lor Y) \iff (\neg X) \land (\neg Y) \,\,\,\,\,\text{ }\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, \neg (X \land Y) \iff (\neg X) \lor (\neg Y)
$$

Basta criar a tabela-verdade para a primeira expressão, já a segunda é praticamente igual, para comprovar a teoria. Vamos considerar as constantes verdadeiro e falso com os termos V e F:

| $X$ | $Y$ | $\neg X$ | $\neg Y$ | $X \lor Y$ | $\neg (X \lor Y)$ | $(\neg X) \land (\neg Y)$ | $\neg (X \lor Y) \iff (\neg X) \land (\neg Y)$ |
|:---:|:---:|:--------:|:--------:|:----------:|:-----------------:|:-------------------------:|:----------------------------------------------:|
|  F  |  F  |    V     |    V     |     F      |         V         |             V             |                       V                        |
|  F  |  V  |    V     |    F     |     V      |         F         |             F             |                       V                        |
|  V  |  F  |    F     |    V     |     V      |         F         |             F             |                       V                        |
|  V  |  V  |    F     |    F     |     V      |         F         |             F             |                       V                        |

A fórmula final é uma tautologia, logo, as expressões que se comparam com o sinal $\iff$ são equivalentes.

### Sintaxe, formalização, propriedades e ordem de precedência

A análise sintática de expressões lógicas consiste em verificar se as fórmulas usadas são bem formuladas ou não.
Por exemplo, fórmulas como as citadas a seguir não podem ser consideradas como válidas para qualquer análise ou proposição lógica, pois não
têm nenhum sentido lógico aplicado ou significado coerente:

$$
A \neg \neg B \hspace{90px} A \lor \land \,B \hspace{90px} A \lor B \neg C \hspace{90px} \implies A \hspace{90px} B \Longleftarrow \Longleftarrow A \hspace{90px} A \neg \land B \lor C
$$

Já as fórmulas a seguir são exemplos de fórmulas bem formuladas:

$$
A \implies \neg B \hspace{90px} D \Longleftarrow C \hspace{90px} \neg \neg G \implies F
$$
$$
M \implies \neg \neg \neg C \lor B \hspace{90px} T \iff \neg S \hspace{90px} A \lor B \implies \neg(C \iff D)
$$

A formalização consiste na conversão de expressões léxicas num idioma humano para formalismos lógicos. Por exemplo:  
Em *"Faz calor, mas visto o casaco."*, *"Faz calor"* pode ser associado com o símbolo $C$ e *"mas visto o casaco"* com símbolo $D$. 
E dessa forma, a expressão se tornaria: $C \land D$, já que ambas as coisas são tratadas como verdades.

Listando exemplos:

- "Chove somente se molha a rua." <br> ↳ $C:$ "Chove" | $M:$ "molha a rua." $\, \therefore \, M \implies C$. <br> <br>
- "Se o chão está molhado então choveu e não há cobertura." <br> ↳ $A:$ "o chão está molhado" | $B:$ "choveu" | $C:$ "há cobertura." $\, \therefore \, A \implies B \land \neg C$. <br> <br>
- "Você vai à praia ou não gosta de biscoito." <br> ↳ $V:$ "Você vai à praia" | $G:$ "Você gosta de biscoito" $\, \therefore \, V \lor \neg G$. <br> <br>
- "T é um triângulo se e somente se T é um polígono de 3 lados." <br> ↳ $E:$ "T é um triângulo" | $P:$ "T é um polígono de 3 lados" $\, \therefore \, E \iff P$. <br> <br>
- "T é um triângulo se T é um polígono de 3 lados." <br> ↳ $E:$ "T é um triângulo" | $P:$ "T é um polígono de 3 lados" $\, \therefore \, P \implies E$. <br> <br>
- "Se Denis jogar na loteria, então ele ficará rico ou desiludido." <br> ↳ $L:$ "Denis joga na loteria" | $R:$ "Denis fica rico" | $D:$ "Denis fica desiludido" $\, \therefore \, L \implies R \lor D$. <br> <br>

Para todas essas expressões, a ordem de precedência dos operadores é: $\neg, \land, \lor, \implies, \iff$, lendo as expressões em conjunto da direita para a esquerda.  
Veja alguns exemplos a seguir:

> 1. $$A \implies \neg B \implies B \implies \neg B \hspace{15px}\equiv\hspace{15px} A \implies ((\neg B) \implies (B \implies (\neg B))) $$
>
> 2. $$\neg B \iff C \implies D \hspace{15px}\equiv\hspace{15px} (\neg B) \iff (C \implies D)$$
>
> 3. $$\neg A \iff \neg A \land \neg B \implies A \implies \neg B \equiv \neg A \iff ((\neg A \land \neg B) \implies (A \implies \neg B))$$

Além disso, as seguintes propriedades são aplicáveis quanto aos operadores:

- *Comutativa*: $A \lor B \equiv B \lor A$ (válida também para $\land$ e $\iff$)
- *Associativa*: $(A \land B) \land C \equiv A \land (B \land C)$ (válida também para $\lor$ e $\iff$)
- *Distributiva*: $$A \land (B \lor C) \equiv (A \land B) \lor (A \land C)$$ $$A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)$$

Esses princípios serão usados principalmente nas deduções naturais e na lógica dos predicados, mais a frente (nos arquivos seguintes).