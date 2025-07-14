# Indicadores de inferência

Vamos revisar alguns conceitos antes de ir para inferências:

- Hipóteses: são as premissas iniciais de um argumento, ou seja, proposições assumidas como verdadeiras para servir de ponto de partida ao raciocínio dedutivo.
- Tese: é a conclusão que se deseja demonstrar; trata-se da proposição que se busca justificar a partir das hipóteses.
- Silogismo: modo clássico de argumento dedutivo composto por duas premissas (maior e menor) e uma conclusão, seguindo o modelo aristotélico de “Todo A é B; C é A; logo, C é B”.

Tendo isso em vista, regras de inferência são regras lógicas que criam justificativas plausíveis para os passos de derivação que levam a uma conclusão, a partir de uma série de hipóteses.  
Isto é, as inferências são fórmulas que se tornam "princípios" verdadeiros, podendo serem simplificados como verdade conforme os passos de uma derivação.

Isso ocorre porque cada regra (como Modus Ponens, Modus Tollens, Silogismo Disjuntivo etc.) pode ser expressa como uma tautologia — proposição sempre verdadeira.
Entretanto, nunca se pode inferir uma conclusão inválida, se isto for assegurado. E, além disso, muitas das regras de inferência são redundantes, então usar uma ou outra como
recurso de derivação não gera problemas.

Na prática, as regras de inferência são definidas na tabela a seguir, onde:

$$
\frac{P \hspace{50px} P \implies Q}{\therefore Q} \hspace{25px}\text{(Modus Ponens)} 
$$

- $P$ é a primeira premissa ou **proposição**
- $P \implies Q$ é a segunda **proposição**
- A barra horizontal é só notação gráfica para separar as premissas da conclusão
- $Q$ é a conclusão, apresentada após o símbolo de "portanto" ($\therefore$)
- O texto à direita, no caso "Modus Ponens", é o nome da regra, mas o espaço à direita também pode ser usado para indicar restrições como “$\alpha$ não ocorre em $\Delta$” ou condições de escopo de variáveis

A seguir, a tabela apresenta todas as regras de inferência:

|                                 Regra                                  |                      Tautologia associada                       |    Nome da regra     | Explicação                                                                                                                                                                                                                                                                           |
|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|:--------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   $$\frac{p}{\therefore p \lor q}$$                    |                     $$p \implies p \lor q$$                     |        Adição        | Se uma hipótese é verdadeira, <br> a disjunção também é                                                                                                                                                                                                                              |
|                   $$\frac{p \land q}{\therefore p}$$                   |                   $$(p \land q) \implies p$$                    |    Simplificação     | Se a conjunção de hipóteses é verdade, <br> a conclusão também é                                                                                                                                                                                                                     |
|                $$p$$ $$\frac{q}{\therefore p \land q}$$                |            $$((p) \land (q)) \implies (p \land q)$$             |      Conjunção       | Se ambas as hipóteses são verdadeiras, <br> a conjunção também é                                                                                                                                                                                                                     |
|             $$p$$ $$\frac{ p \implies q }{\therefore q}$$              |             $$[p \land (p \implies q)] \implies q$$             |     Modus Ponens     | Se uma proposição condicional é verdadeira <br> e a sua antecedente também é verdadeira, <br> então a sua consequente também é verdadeira                                                                                                                                            |
|         $$\neg q$$ $$\frac{p \implies q}{\therefore \neg p}$$          |        $$[\neg q \land (p \implies q)] \implies \neg p$$        |    Modus Tollens     | Se uma proposição condicional é verdadeira <br> e a sua consequente é falsa, <br> então a sua antecedente também é falsa.                                                                                                                                                            |
|   $$p \implies q$$ $$\frac{q \implies r}{\therefore p \implies r}$$    | $$[(p \implies q) \land (q \implies r)] \implies p \implies r$$ | Silogismo hipotético | Se uma proposição condicional é verdadeira <br> e outra proposição condicional, *cuja antecedente coincide com a consequente da primeira*, também é verdadeira, <br> então a proposição condicional que liga o antecedente da primeira à consequente da segunda também é verdadeira. |
| $$p \lor q$$ $$\frac{\hspace{5px}\neg p \hspace{20px}}{\therefore q}$$ |           $$[(p \lor q) \land (\neg p)] \implies q$$            | Silogismo disjuntivo | Se uma proposição disjuntiva é verdadeira <br> e um dos seus disjuntos é falso, <br> então o outro disjunto deve ser verdadeiro.                                                                                                                                                     |

