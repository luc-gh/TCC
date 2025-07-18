# Provas    

Provas são sequências de argumentos lógicos que, a partir de hipóteses ou axiomas, estabelecem a verdade de uma proposição de forma rigorosa.  
Na matemática discreta e na lógica aplicada à computação, as provas garantem a correção de teoremas, algoritmos e especificações, dando confiança na construção 
de sistemas e na derivação de propriedades sobre estruturas finitas ou infinitas.

### Prova direta

Consiste em assumir diretamente a premissa $P$ e , por dedução lógica e manipulação de definições, chegar à conclusão $Q$, 
especialmente útil para implicações do tipo $P \implies Q$. No caso de universais $\forall x (P(x) \implies Q(x))$, escolhe-se um $x$ arbitrário e procede-se da mesma forma.

> **Exemplo**
> 
> Provar: "Se $n$ é par, então $n^2$ é par."
> 
> _Prova_: Seja $n$ inteiro arbitrário e suponha $n = 2k$.  
> Então: $n^2 = (2k)^2 = 4k^2 = 2 (2k^2)$, que é par.

### Prova por Contraposição

A contrapositiva de $P \implies Q$ é $\neg Q \implies \neg P$, logicamente equivalente ao original. Provar a contrapositiva é, em essência, uma prova direta 
aplicada à forma invertida e negada da implicação, às vezes mais simples de manipular.

> **Exemplo**
> 
> Provar: “Se $x^2$ é par, então $x$ é par.
> 
> _Prova por contraposição_: Demonstra-se “Se $x$ não é par, então $x^2$ não é par.”  
> Suponha que $x$ é ímpar, então $x = 2k+1$ e $x^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, que é ímpar.  
> Logo, $x^2$ não é par, e assim a proposição original vale.

### Prova por Contradição

Chamada também de proof by contradiction ou reductio ad absurdum, assume-se $\neg P$ e mostra-se que isso leva a uma contradição lógica (por exemplo, $Q \land \neg Q$).  
Conclui-se então que $P$ deve ser verdadeiro.

> **Exemplo**
> 
> Teorema: “Há infinitos números primos.”  
> 
> _Prova_: Suponha, para fins de contradição, que existam apenas finitamente muitos primos e seja $P$ o maior deles.  
> Considere $N = p! +1$. Então $N$ não é divisível por nenhum primo $x \leq p$, logo sua fatoração contém um primo maior que $p$, contradizendo a maximalidade de $P$.  
> Portanto, existem infinitos primos.

### Prova por Exaustão (Análise de Casos)

Também chamada de proof by cases, divide-se a afirmação em um número finito de casos exaustivos e prova-se cada um separadamente.  
É uma forma de prova direta, mas pode tornar-se impraticável se o número de casos for muito grande.

> **Exemplo**
> 
> 