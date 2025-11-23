<script setup lang="ts">
import { ref } from "vue";

const code = "mat-11";
const title = "Matemática: Expressões Algébricas, Produtos Notáveis e Fatoração";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-1">
<ul class="org-ul">
<li>Matemática: Expressões Algébricas, Produtos Notáveis e Fatoração</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-orged3c6d7" class="outline-4">
<h4 id="orged3c6d7"><span class="section-number-4">3.1.1.</span> O que são Expressões Algébricas?</h4>
<div class="outline-text-4" id="text-3-1-1">
<p>
<b>Expressão algébrica</b> é uma combinação de números, letras (variáveis) e operações matemáticas (+, -, ×, ÷, potenciação, radiciação).
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>2x + 3</li>
<li>x²</li>
<li>5x + 6</li>
<li>3ab</li>
<li>2a + b</li>
<li>(x + y)²</li>
</ul>

<p>
<b>Termos:</b>
</p>
<ul class="org-ul">
<li><b>Variável:</b> Letra que representa um número desconhecido (x, y, a, b, etc.)</li>
<li><b>Coeficiente:</b> Número que multiplica a variável</li>
<li><b>Termo:</b> Parte da expressão separada por + ou</li>
<li>- <b>Monômio:</b> Expressão com um único termo</li>
<li><b>Polinômio:</b> Expressão com dois ou mais termos</li>
</ul>
</div>
</div>

<div id="outline-container-orga0a262d" class="outline-4">
<h4 id="orga0a262d"><span class="section-number-4">3.1.2.</span> Monômios</h4>
<div class="outline-text-4" id="text-3-1-2">
<p>
<b>Definição:</b> Expressão algébrica com apenas um termo.
</p>

<p>
<b>Estrutura:</b> coeficiente × parte literal
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>5x (coeficiente 5, parte literal x)</li>
<li>-3x² (coeficiente -3, parte literal x²)</li>
<li>2ab³ (coeficiente 2, parte literal ab³)</li>
<li>7 (monômio constante)</li>
</ul>

<p>
<b>Grau do monômio:</b> Soma dos expoentes das variáveis.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>5x → grau 1</li>
<li>3x² → grau 2</li>
<li>2x³y² → grau 5 (3+2)</li>
<li>-4a²b³c → grau 6 (2+3+1)</li>
</ul>
</div>
</div>

<div id="outline-container-org32cff0e" class="outline-4">
<h4 id="org32cff0e"><span class="section-number-4">3.1.3.</span> Operações com Monômios</h4>
<div class="outline-text-4" id="text-3-1-3">
</div>
<div id="outline-container-orgea70474" class="outline-5">
<h5 id="orgea70474"><span class="section-number-5">3.1.3.1.</span> Adição e Subtração</h5>
<div class="outline-text-5" id="text-3-1-3-1">
<p>
<b>Regra:</b> Só podemos somar/subtrair monômios <b>semelhantes</b> (mesma parte literal).
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Semelhantes (podem somar/subtrair):</b>
</p>
<ul class="org-ul">
<li>3x + 5x = 8x</li>
<li>7x²</li>
<li>2x² = 5x²</li>
<li>4ab + 3ab</li>
<li>ab = 6ab</li>
</ul>

<p>
<b>Não semelhantes (NÃO podem somar/subtrair):</b>
</p>
<ul class="org-ul">
<li>3x + 5y (não dá para simplificar)</li>
<li>2x² + 3x (não dá para simplificar)</li>
</ul>
</div>
</div>

<div id="outline-container-org5f187b1" class="outline-5">
<h5 id="org5f187b1"><span class="section-number-5">3.1.3.2.</span> Multiplicação</h5>
<div class="outline-text-5" id="text-3-1-3-2">
<p>
<b>Regra:</b> 1. Multiplicar os coeficientes 2. Multiplicar as partes literais (somar os expoentes de mesma base)
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>(3x) · (2x) = 6x²</li>
<li>(2x²) · (4x³) = 8x⁵</li>
<li>(5a) · (2b) = 10ab</li>
<li>(2x²y) · (3xy²) = 6x³y³</li>
</ul>
</div>
</div>

<div id="outline-container-org7b297ae" class="outline-5">
<h5 id="org7b297ae"><span class="section-number-5">3.1.3.3.</span> Divisão</h5>
<div class="outline-text-5" id="text-3-1-3-3">
<p>
<b>Regra:</b> 1. Dividir os coeficientes 2. Dividir as partes literais (subtrair os expoentes de mesma base)
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>12x⁵ ÷ 3x² = 4x³</li>
<li>8x³y² ÷ 2xy = 4x²y</li>
<li>15a⁴ ÷ 5a² = 3a²</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org8eb8be2" class="outline-4">
<h4 id="org8eb8be2"><span class="section-number-4">3.1.4.</span> Polinômios</h4>
<div class="outline-text-4" id="text-3-1-4">
<p>
<b>Definição:</b> Expressão algébrica com dois ou mais termos.
</p>

<p>
<b>Tipos especiais:</b>
</p>
<ul class="org-ul">
<li><b>Binômio:</b> 2 termos (x + 3, a</li>
<li>b)</li>
<li><b>Trinômio:</b> 3 termos (x² + 2x + 1)</li>
</ul>

<p>
<b>Grau do polinômio:</b> Maior grau entre seus termos.
</p>

<p>
<b>Exemplo:</b> P(x) = 3x⁴
</p>
<ul class="org-ul">
<li>2x³ + x</li>
<li>5</li>

<li>Termos: 3x⁴, -2x³, x, -5</li>
<li>Graus: 4, 3, 1, 0</li>
<li><b>Grau do polinômio: 4</b></li>
</ul>
</div>
</div>

<div id="outline-container-org7a574c6" class="outline-4">
<h4 id="org7a574c6"><span class="section-number-4">3.1.5.</span> Operações com Polinômios</h4>
<div class="outline-text-4" id="text-3-1-5">
</div>
<div id="outline-container-orgdace03d" class="outline-5">
<h5 id="orgdace03d"><span class="section-number-5">3.1.5.1.</span> Adição e Subtração</h5>
<div class="outline-text-5" id="text-3-1-5-1">
<p>
<b>Regra:</b> Somar/subtrair termos semelhantes.
</p>

<p>
<b>Exemplo 1:</b> (3x² + 2x
</p>
<ul class="org-ul">
<li>1) + (x²</li>
<li>5x + 3)</li>
</ul>

<p>
= 3x² + x² + 2x
</p>
<ul class="org-ul">
<li>5x</li>
<li>1 + 3 = 4x²</li>
<li>3x + 2</li>
</ul>

<p>
<b>Exemplo 2:</b> (5x² + 3x
</p>
<ul class="org-ul">
<li>2)</li>
<li>(2x²</li>
<li>x + 4)</li>
</ul>

<p>
= 5x² + 3x
</p>
<ul class="org-ul">
<li>2</li>
<li>2x² + x</li>
<li>4 = 3x² + 4x</li>
<li>6</li>
</ul>

<p>
<b>Atenção:</b> Ao subtrair, troque todos os sinais do segundo polinômio!
</p>
</div>
</div>

<div id="outline-container-org7740c7b" class="outline-5">
<h5 id="org7740c7b"><span class="section-number-5">3.1.5.2.</span> Multiplicação</h5>
<div class="outline-text-5" id="text-3-1-5-2">
<p>
<b>Regra:</b> Multiplicar cada termo do primeiro polinômio por cada termo do segundo (propriedade distributiva).
</p>

<p>
<b>Exemplo 1:</b> Monômio × Polinômio 2x · (3x²
</p>
<ul class="org-ul">
<li>5x + 1)</li>
</ul>

<p>
= 2x · 3x² + 2x · (-5x) + 2x · 1 = 6x³
</p>
<ul class="org-ul">
<li>10x² + 2x</li>
</ul>

<p>
<b>Exemplo 2:</b> Binômio × Binômio (x + 3)(x + 2)
</p>

<p>
= x · x + x · 2 + 3 · x + 3 · 2 = x² + 2x + 3x + 6 = x² + 5x + 6
</p>

<p>
<b>Exemplo 3:</b> Binômio × Trinômio (x + 2)(x²
</p>
<ul class="org-ul">
<li>3x + 1)</li>
</ul>

<p>
= x · x² + x · (-3x) + x · 1 + 2 · x² + 2 · (-3x) + 2 · 1 = x³
</p>
<ul class="org-ul">
<li>3x² + x + 2x²</li>
<li>6x + 2 = x³</li>
<li>x²</li>
<li>5x + 2</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org7c6460f" class="outline-4">
<h4 id="org7c6460f"><span class="section-number-4">3.1.6.</span> Produtos Notáveis</h4>
<div class="outline-text-4" id="text-3-1-6">
<p>
<b>Produtos notáveis</b> são multiplicações de expressões algébricas que aparecem com frequência e têm fórmulas prontas.
</p>
</div>
</div>

<div id="outline-container-orgc9ea74e" class="outline-4">
<h4 id="orgc9ea74e"><span class="section-number-4">3.1.7.</span> 1. Quadrado da Soma</h4>
<div class="outline-text-4" id="text-3-1-7">
<p>
<b>(a + b)² = a² + 2ab + b²</b>
</p>

<p>
<b>Em palavras:</b> “O quadrado do primeiro, mais duas vezes o primeiro vezes o segundo, mais o quadrado do segundo”
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>(x + 3)²</b> = x² + 2 · x · 3 + 3² = x² + 6x + 9
</p>

<p>
<b>(2x + 5)²</b> = (2x)² + 2 · 2x · 5 + 5² = 4x² + 20x + 25
</p>

<p>
<b>(a + b)²</b> = a² + 2ab + b²
</p>

<p>
<b>Erro comum:</b> (a + b)² ≠ a² + b² <b>Correto:</b> (a + b)² = a² + 2ab + b²
</p>
</div>
</div>

<div id="outline-container-orga15d53b" class="outline-4">
<h4 id="orga15d53b"><span class="section-number-4">3.1.8.</span> 2. Quadrado da Diferença</h4>
<div class="outline-text-4" id="text-3-1-8">
<p>
*(a
</p>
<ul class="org-ul">
<li>b)² = a²</li>
<li>2ab + b²*</li>
</ul>

<p>
<b>Em palavras:</b> “O quadrado do primeiro, menos duas vezes o primeiro vezes o segundo, mais o quadrado do segundo”
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
*(x
</p>
<ul class="org-ul">
<li>2)²* = x²</li>
<li>2 · x · 2 + 2² = x²</li>
<li>4x + 4</li>
</ul>

<p>
*(3x
</p>
<ul class="org-ul">
<li>4)²* = (3x)²</li>
<li>2 · 3x · 4 + 4² = 9x²</li>
<li>24x + 16</li>
</ul>

<p>
*(a
</p>
<ul class="org-ul">
<li>b)²* = a²</li>
<li>2ab + b²</li>
</ul>

<p>
<b>Observação:</b> Note que o último termo é sempre positivo!
</p>
</div>
</div>

<div id="outline-container-org3c1de81" class="outline-4">
<h4 id="org3c1de81"><span class="section-number-4">3.1.9.</span> 3. Produto da Soma pela Diferença</h4>
<div class="outline-text-4" id="text-3-1-9">
<p>
*(a + b)(a
</p>
<ul class="org-ul">
<li>b) = a²</li>
<li>b²*</li>
</ul>

<p>
<b>Em palavras:</b> “O quadrado do primeiro menos o quadrado do segundo”
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
*(x + 5)(x
</p>
<ul class="org-ul">
<li>5)* = x²</li>
<li>5² = x²</li>
<li>25</li>
</ul>

<p>
*(2x + 3)(2x
</p>
<ul class="org-ul">
<li>3)* = (2x)²</li>
<li>3² = 4x²</li>
<li>9</li>
</ul>

<p>
*(7 + y)(7
</p>
<ul class="org-ul">
<li>y)* = 7²</li>
<li>y² = 49</li>
<li>y²</li>
</ul>

<p>
<b>Aplicação prática:</b> Cálculo mental!
</p>

<p>
<b>Exemplo:</b> 103 × 97 = (100 + 3)(100
</p>
<ul class="org-ul">
<li>3) = 100²</li>
<li>3² = 10000</li>
<li>9 = 9991</li>
</ul>
</div>
</div>

<div id="outline-container-orgdf30491" class="outline-4">
<h4 id="orgdf30491"><span class="section-number-4">3.1.10.</span> 4. Cubo da Soma</h4>
<div class="outline-text-4" id="text-3-1-10">
<p>
<b>(a + b)³ = a³ + 3a²b + 3ab² + b³</b>
</p>

<p>
<b>Exemplo:</b> (x + 2)³ = x³ + 3x²(2) + 3x(2²) + 2³ = x³ + 6x² + 12x + 8
</p>
</div>
</div>

<div id="outline-container-org3aca3c8" class="outline-4">
<h4 id="org3aca3c8"><span class="section-number-4">3.1.11.</span> 5. Cubo da Diferença</h4>
<div class="outline-text-4" id="text-3-1-11">
<p>
*(a
</p>
<ul class="org-ul">
<li>b)³ = a³</li>
<li>3a²b + 3ab²</li>
<li>b³*</li>
</ul>

<p>
<b>Exemplo:</b> (x
</p>
<ul class="org-ul">
<li>1)³ = x³</li>
<li>3x²(1) + 3x(1²)</li>
<li>1³ = x³</li>
<li>3x² + 3x</li>
<li>1</li>
</ul>
</div>
</div>

<div id="outline-container-org632c13f" class="outline-4">
<h4 id="org632c13f"><span class="section-number-4">3.1.12.</span> Resumo dos Produtos Notáveis</h4>
<div class="outline-text-4" id="text-3-1-12">
<pre class="example" id="org8147eb4">
(a + b)² = a² + 2ab + b²

(a
- b)² = a²
- 2ab + b²

(a + b)(a
- b) = a²
- b²

(a + b)³ = a³ + 3a²b + 3ab² + b³

(a
- b)³ = a³
- 3a²b + 3ab²
- b³
</pre>
</div>
</div>

<div id="outline-container-org2b930ca" class="outline-4">
<h4 id="org2b930ca"><span class="section-number-4">3.1.13.</span> Fatoração</h4>
<div class="outline-text-4" id="text-3-1-13">
<p>
<b>Fatoração</b> é o processo inverso da multiplicação: transformar uma soma/subtração em um produto.
</p>

<p>
<b>Por que fatorar?</b>
</p>
<ul class="org-ul">
<li>Simplificar expressões</li>
<li>Resolver equações</li>
<li>Facilitar cálculos</li>
<li>Encontrar raízes de funções</li>
</ul>
</div>
</div>

<div id="outline-container-org618d0b5" class="outline-4">
<h4 id="org618d0b5"><span class="section-number-4">3.1.14.</span> Casos de Fatoração</h4>
</div>
<div id="outline-container-orga99e6db" class="outline-4">
<h4 id="orga99e6db"><span class="section-number-4">3.1.15.</span> 1. Fator Comum em Evidência</h4>
<div class="outline-text-4" id="text-3-1-15">
<p>
<b>Regra:</b> Identificar o fator que aparece em todos os termos e colocá-lo em evidência.
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>6x + 9</b> = 3(2x + 3) → fator comum: 3
</p>

<p>
*4x²
</p>
<ul class="org-ul">
<li>8x* = 4x(x</li>
<li>2) → fator comum: 4x</li>
</ul>

<p>
*3x³ + 6x²
</p>
<ul class="org-ul">
<li>9x* = 3x(x² + 2x</li>
<li>3) → fator comum: 3x</li>
</ul>

<p>
<b>ax + ay</b> = a(x + y) → fator comum: a
</p>

<p>
<b>Método:</b> 1. Identificar o maior fator comum (MDC dos coeficientes e menor expoente das variáveis comuns) 2. Dividir cada termo pelo fator comum 3. Escrever como produto
</p>
</div>
</div>

<div id="outline-container-orgfae1bbb" class="outline-4">
<h4 id="orgfae1bbb"><span class="section-number-4">3.1.16.</span> 2. Agrupamento</h4>
<div class="outline-text-4" id="text-3-1-16">
<p>
<b>Regra:</b> Agrupar termos que têm fatores comuns.
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>ax + bx + ay + by</b> = x(a + b) + y(a + b) = (a + b)(x + y)
</p>

<p>
<b>2x + 2y + mx + my</b> = 2(x + y) + m(x + y) = (x + y)(2 + m)
</p>

<p>
<b>x³ + x² + x + 1</b> = x²(x + 1) + 1(x + 1) = (x + 1)(x² + 1)
</p>
</div>
</div>

<div id="outline-container-org2fe2568" class="outline-4">
<h4 id="org2fe2568"><span class="section-number-4">3.1.17.</span> 3. Trinômio Quadrado Perfeito</h4>
<div class="outline-text-4" id="text-3-1-17">
<p>
<b>Regra:</b> Reconhecer os produtos notáveis de quadrado.
</p>

<p>
<b>Forma:</b> a² + 2ab + b² = (a + b)² <b>Forma:</b> a²
</p>
<ul class="org-ul">
<li>2ab + b² = (a</li>
<li>b)²</li>
</ul>

<p>
<b>Como identificar:</b> 1. Primeiro e último termos são quadrados perfeitos 2. Termo do meio = 2 × √(primeiro) × √(último)
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>x² + 6x + 9</b>
</p>
<ul class="org-ul">
<li>x² é quadrado de x</li>
<li>9 é quadrado de 3</li>
<li>6x = 2 · x · 3 ✓</li>
<li><i>[Ver resposta 45 no final do documento]</i></li>
</ul>

<p>
*x²
</p>
<ul class="org-ul">
<li>10x + 25*</li>
<li>x² é quadrado de x</li>
<li>25 é quadrado de 5</li>
<li>10x = 2 · x · 5 ✓</li>
<li><i>[Ver resposta 46 no final do documento]</i></li>
</ul>

<p>
<b>4x² + 12x + 9</b>
</p>
<ul class="org-ul">
<li>4x² é quadrado de 2x</li>
<li>9 é quadrado de 3</li>
<li>12x = 2 · 2x · 3 ✓</li>
<li><i>[Ver resposta 47 no final do documento]</i></li>
</ul>
</div>
</div>

<div id="outline-container-org9c8be6e" class="outline-4">
<h4 id="org9c8be6e"><span class="section-number-4">3.1.18.</span> 4. Diferença de Quadrados</h4>
<div class="outline-text-4" id="text-3-1-18">
<p>
<b>Regra:</b> a²
</p>
<ul class="org-ul">
<li>b² = (a + b)(a</li>
<li>b)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<p>
*x²
</p>
<ul class="org-ul">
<li>25* = x²</li>
<li>5² = (x + 5)(x</li>
<li>5)</li>
</ul>

<p>
*9x²
</p>
<ul class="org-ul">
<li>16* = (3x)²</li>
<li>4² = (3x + 4)(3x</li>
<li>4)</li>
</ul>

<p>
*a²
</p>
<ul class="org-ul">
<li>b²* = (a + b)(a</li>
<li>b)</li>
</ul>

<p>
*49
</p>
<ul class="org-ul">
<li>y²* = 7²</li>
<li>y² = (7 + y)(7</li>
<li>y)</li>
</ul>
</div>
</div>

<div id="outline-container-org969bd23" class="outline-4">
<h4 id="org969bd23"><span class="section-number-4">3.1.19.</span> 5. Trinômio do Tipo x² + Sx + P</h4>
<div class="outline-text-4" id="text-3-1-19">
<p>
<b>Forma:</b> x² + Sx + P
</p>

<p>
<b>Fatoração:</b> (x + a)(x + b)
</p>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>S = soma (a + b)</li>
<li>P = produto (a · b)</li>
</ul>

<p>
<b>Método:</b> 1. Encontrar dois números que:
</p>
<ul class="org-ul">
<li><b>Somados</b> dão o coeficiente de x</li>
<li><b>Multiplicados</b> dão o termo independente 2. Escrever como (x + a)(x + b)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>x² + 7x + 12</b>
</p>

<p>
Procurar dois números que:
</p>
<ul class="org-ul">
<li>Somam 7</li>
<li>Multiplicam 12</li>
</ul>

<p>
Números: 3 e 4
</p>
<ul class="org-ul">
<li>3 + 4 = 7 ✓</li>
<li>3 · 4 = 12 ✓</li>
</ul>

<p>
<i>[Ver resposta 48 no final do documento]</i>
</p>

<p>
*x²
</p>
<ul class="org-ul">
<li>5x + 6*</li>
</ul>

<p>
Procurar dois números que:
</p>
<ul class="org-ul">
<li>Somam -5</li>
<li>Multiplicam 6</li>
</ul>

<p>
Números: -2 e -3
</p>
<ul class="org-ul">
<li>(-2) + (-3) = -5 ✓</li>
<li>(-2) · (-3) = 6 ✓</li>
</ul>

<p>
<i>[Ver resposta 49 no final do documento]</i>
</p>

<p>
*x² + x
</p>
<ul class="org-ul">
<li>12*</li>
</ul>

<p>
Procurar dois números que:
</p>
<ul class="org-ul">
<li>Somam 1</li>
<li>Multiplicam -12</li>
</ul>

<p>
Números: 4 e -3
</p>
<ul class="org-ul">
<li>4 + (-3) = 1 ✓</li>
<li>4 · (-3) = -12 ✓</li>
</ul>

<p>
<i>[Ver resposta 50 no final do documento]</i>
</p>

<p>
*x²
</p>
<ul class="org-ul">
<li>7x + 10*</li>
</ul>

<p>
Números: -5 e -2
</p>
<ul class="org-ul">
<li>(-5) + (-2) = -7 ✓</li>
<li>(-5) · (-2) = 10 ✓</li>
</ul>

<p>
<i>[Ver resposta 51 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf3ee388" class="outline-4">
<h4 id="orgf3ee388"><span class="section-number-4">3.1.20.</span> 6. Diferença de Cubos</h4>
<div class="outline-text-4" id="text-3-1-20">
<p>
*a³
</p>
<ul class="org-ul">
<li>b³ = (a</li>
<li>b)(a² + ab + b²)*</li>
</ul>

<p>
<b>Exemplo:</b> x³
</p>
<ul class="org-ul">
<li>8 = x³</li>
<li>2³ = (x</li>
<li>2)(x² + 2x + 4)</li>
</ul>
</div>
</div>

<div id="outline-container-orgb936b02" class="outline-4">
<h4 id="orgb936b02"><span class="section-number-4">3.1.21.</span> 7. Soma de Cubos</h4>
<div class="outline-text-4" id="text-3-1-21">
<p>
*a³ + b³ = (a + b)(a²
</p>
<ul class="org-ul">
<li>ab + b²)*</li>
</ul>

<p>
<b>Exemplo:</b> x³ + 27 = x³ + 3³ = (x + 3)(x²
</p>
<ul class="org-ul">
<li>3x + 9)</li>
</ul>
</div>
</div>

<div id="outline-container-orgc87f42e" class="outline-4">
<h4 id="orgc87f42e"><span class="section-number-4">3.1.22.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-1-22">
</div>
<div id="outline-container-org0afac96" class="outline-5">
<h5 id="org0afac96"><span class="section-number-5">3.1.22.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-1-22-1">
<p>
Desenvolva (2x + 3)²
</p>

<p>
<b>Solução:</b> (2x + 3)² = (2x)² + 2(2x)(3) + 3² = 4x² + 12x + 9
</p>
</div>
</div>

<div id="outline-container-orgdd131b7" class="outline-5">
<h5 id="orgdd131b7"><span class="section-number-5">3.1.22.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-1-22-2">
<p>
Desenvolva (x
</p>
<ul class="org-ul">
<li>5)(x + 5)</li>
</ul>

<p>
<b>Solução:</b> (x
</p>
<ul class="org-ul">
<li>5)(x + 5) = x²</li>
<li>5² = x²</li>
<li>25</li>
</ul>
</div>
</div>

<div id="outline-container-org4ac18f3" class="outline-5">
<h5 id="org4ac18f3"><span class="section-number-5">3.1.22.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-1-22-3">
<p>
Fatore: 3x² + 6x
</p>

<p>
<b>Solução:</b> Fator comum: 3x 3x² + 6x = 3x(x + 2)
</p>
</div>
</div>

<div id="outline-container-orgad60c4d" class="outline-5">
<h5 id="orgad60c4d"><span class="section-number-5">3.1.22.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-1-22-4">
<p>
Fatore: x²
</p>
<ul class="org-ul">
<li>16</li>
</ul>

<p>
<b>Solução:</b> Diferença de quadrados: x²
</p>
<ul class="org-ul">
<li>16 = x²</li>
<li>4² = (x + 4)(x</li>
<li>4)</li>
</ul>
</div>
</div>

<div id="outline-container-org0e88a39" class="outline-5">
<h5 id="org0e88a39"><span class="section-number-5">3.1.22.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-3-1-22-5">
<p>
Fatore: x² + 8x + 16
</p>

<p>
<b>Solução:</b> Trinômio quadrado perfeito:
</p>
<ul class="org-ul">
<li>x² (quadrado de x)</li>
<li>16 (quadrado de 4)</li>
<li>8x = 2 · x · 4 ✓</li>
</ul>

<p>
x² + 8x + 16 = (x + 4)²
</p>
</div>
</div>

<div id="outline-container-org4a52c34" class="outline-5">
<h5 id="org4a52c34"><span class="section-number-5">3.1.22.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-3-1-22-6">
<p>
Fatore: x²
</p>
<ul class="org-ul">
<li>5x</li>
<li>6</li>
</ul>

<p>
<b>Solução:</b> Procurar dois números que somam -5 e multiplicam -6:
</p>
<ul class="org-ul">
<li>Números: -6 e 1</li>
<li>(-6) + 1 = -5 ✓</li>
<li>(-6) · 1 = -6 ✓</li>
</ul>

<p>
x²
</p>
<ul class="org-ul">
<li>5x</li>
<li>6 = (x</li>
<li>6)(x + 1)</li>
</ul>
</div>
</div>

<div id="outline-container-orgb53cf8f" class="outline-5">
<h5 id="orgb53cf8f"><span class="section-number-5">3.1.22.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-3-1-22-7">
<p>
Simplifique: (x + 3)²
</p>
<ul class="org-ul">
<li>(x</li>
<li>3)²</li>
</ul>

<p>
<b>Solução:</b> Método 1 (desenvolver): (x + 3)²
</p>
<ul class="org-ul">
<li>(x</li>
<li>3)² = (x² + 6x + 9)</li>
<li>(x²</li>
<li>6x + 9) = x² + 6x + 9</li>
<li>x² + 6x</li>
<li>9 = 12x</li>
</ul>

<p>
Método 2 (diferença de quadrados): (x + 3)²
</p>
<ul class="org-ul">
<li>(x</li>
<li>3)² = [(x+3) + (x-3)][(x+3)</li>
<li>(x-3)] = [2x][6] = 12x</li>
</ul>
</div>
</div>

<div id="outline-container-orgf5f9a70" class="outline-5">
<h5 id="orgf5f9a70"><span class="section-number-5">3.1.22.8.</span> Exercício 8</h5>
<div class="outline-text-5" id="text-3-1-22-8">
<p>
Calcule 52² usando produtos notáveis.
</p>

<p>
<b>Solução:</b> 52² = (50 + 2)² = 50² + 2(50)(2) + 2² = 2500 + 200 + 4 = 2704
</p>
</div>
</div>

<div id="outline-container-org1e5c703" class="outline-5">
<h5 id="org1e5c703"><span class="section-number-5">3.1.22.9.</span> Exercício 9</h5>
<div class="outline-text-5" id="text-3-1-22-9">
<p>
Calcule 98 × 102 usando produtos notáveis.
</p>

<p>
<b>Solução:</b> 98 × 102 = (100
</p>
<ul class="org-ul">
<li>2)(100 + 2) = 100²</li>
<li>2² = 10000</li>
<li>4 = 9996</li>
</ul>
</div>
</div>

<div id="outline-container-org265572b" class="outline-5">
<h5 id="org265572b"><span class="section-number-5">3.1.22.10.</span> Exercício 10</h5>
<div class="outline-text-5" id="text-3-1-22-10">
<p>
Fatore completamente: 2x³ + 8x² + 8x
</p>

<p>
<b>Solução:</b> Passo 1: Fator comum 2x³ + 8x² + 8x = 2x(x² + 4x + 4)
</p>

<p>
Passo 2: Trinômio quadrado perfeito x² + 4x + 4 = (x + 2)²
</p>

<p>
<b>Resposta final:</b> 2x(x + 2)²
</p>
</div>
</div>
</div>

<div id="outline-container-orgc6be765" class="outline-4">
<h4 id="orgc6be765"><span class="section-number-4">3.1.23.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-3-1-23">
</div>
<div id="outline-container-org315d03b" class="outline-5">
<h5 id="org315d03b"><span class="section-number-5">3.1.23.1.</span> Simplificação de Frações Algébricas</h5>
<div class="outline-text-5" id="text-3-1-23-1">
<p>
<b>Exemplo:</b> Simplifique: (x²
</p>
<ul class="org-ul">
<li>9)/(x² + 6x + 9)</li>
</ul>

<p>
<b>Solução:</b> Numerador: x²
</p>
<ul class="org-ul">
<li>9 = (x + 3)(x</li>
<li>3) Denominador: x² + 6x + 9 = (x + 3)²</li>
</ul>

<p>
= (x + 3)(x
</p>
<ul class="org-ul">
<li>3) / (x + 3)² = (x</li>
<li>3) / (x + 3)</li>
</ul>
</div>
</div>

<div id="outline-container-orgacf8e63" class="outline-5">
<h5 id="orgacf8e63"><span class="section-number-5">3.1.23.2.</span> Resolução de Equações</h5>
<div class="outline-text-5" id="text-3-1-23-2">
<p>
<b>Exemplo:</b> Resolva: x²
</p>
<ul class="org-ul">
<li>5x + 6 = 0</li>
</ul>

<p>
<b>Solução:</b> Fatorando: (x
</p>
<ul class="org-ul">
<li>2)(x</li>
<li>3) = 0</li>
</ul>

<p>
Para o produto ser zero, um dos fatores deve ser zero: x
</p>
<ul class="org-ul">
<li>2 = 0 → x = 2 ou x</li>
<li>3 = 0 → x = 3</li>
</ul>

<p>
<i>[Ver resposta 52 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org58241ea" class="outline-4">
<h4 id="org58241ea"><span class="section-number-4">3.1.24.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-1-24">
<ol class="org-ol">
<li><b>Produtos notáveis:</b> Memorize as 5 fórmulas principais</li>
<li><b>Quadrado da soma/diferença:</b> O último termo é sempre positivo!</li>
<li><b>Diferença de quadrados:</b> Resultado não tem termo do meio</li>
<li><b>Fatoração:</b> Sempre comece procurando fator comum</li>
<li><b>Trinômio x² + Sx + P:</b> Procure dois números que somam S e multiplicam P</li>
<li><b>Verificação:</b> Multiplique de volta para conferir a fatoração</li>
<li><b>Sinais:</b> Preste muita atenção aos sinais, principalmente ao subtrair polinômios</li>
</ol>
</div>
</div>

<div id="outline-container-org4acefdd" class="outline-4">
<h4 id="org4acefdd"><span class="section-number-4">3.1.25.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-1-25">
<p>
<b>Produtos Notáveis:</b>
</p>
<ul class="org-ul">
<li>(a + b)² = a² + 2ab + b²</li>
<li>(a</li>
<li>b)² = a²</li>
<li>2ab + b²</li>
<li>(a + b)(a</li>
<li>b) = a²</li>
<li>b²</li>
</ul>

<p>
<b>Fatoração:</b>
</p>
<ul class="org-ul">
<li><b>Fator comum:</b> ax + ay = a(x + y)</li>
<li><b>Diferença de quadrados:</b> a²</li>
<li>b² = (a + b)(a</li>
<li>b)</li>
<li><b>Trinômio quadrado perfeito:</b> a² ± 2ab + b² = (a ± b)²</li>
<li><b>Trinômio x² + Sx + P:</b> procure números que somam S e multiplicam P</li>
</ul>

<p>
<b>Erros comuns a evitar:</b>
</p>
<ul class="org-ul">
<li>(a + b)² ≠ a² + b² → correto: a² + 2ab + b²</li>
<li>(a</li>
<li>b)² ≠ a²</li>
<li>b² → correto: a²</li>
<li>2ab + b²</li>
</ul>
</div>
</div>

<div id="outline-container-org674dd45" class="outline-4">
<h4 id="org674dd45"><span class="section-number-4">3.1.26.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-1-26">
<pre class="example" id="org9eec437">
Produtos Notáveis:

(a + b)² = a² + 2ab + b²
(a
- b)² = a²
- 2ab + b²
(a + b)(a
- b) = a²
- b²
(a + b)³ = a³ + 3a²b + 3ab² + b³
(a
- b)³ = a³
- 3a²b + 3ab²
- b³

Fatoração:

Fator comum: ax + ay = a(x + y)
Diferença de quadrados: a²
- b² = (a + b)(a
- b)
Trinômio quadrado perfeito: a² ± 2ab + b² = (a ± b)²
Diferença de cubos: a³
- b³ = (a
- b)(a² + ab + b²)
Soma de cubos: a³ + b³ = (a + b)(a²
- ab + b²)
</pre>
</div>
</div>

<div id="outline-container-org3b2cd05" class="outline-4">
<h4 id="org3b2cd05"><span class="section-number-4">3.1.27.</span> Tabela de Fatoração Rápida</h4>
<div class="outline-text-4" id="text-3-1-27">
<pre class="example" id="org2f14825">
┌─────────────────────────┬────────────────────────┐
│      Expressão          │      Fatoração         │
├─────────────────────────┼────────────────────────┤
│ x²
- 4                  │ (x + 2)(x
- 2)         │
│ x²
- 9                  │ (x + 3)(x
- 3)         │
│ x²
- 16                 │ (x + 4)(x
- 4)         │
│ x²
- 25                 │ (x + 5)(x
- 5)         │
│ x² + 2x + 1             │ (x + 1)²               │
│ x²
- 2x + 1             │ (x
- 1)²               │
│ x² + 4x + 4             │ (x + 2)²               │
│ x²
- 4x + 4             │ (x
- 2)²               │
│ x² + 6x + 9             │ (x + 3)²               │
│ x²
- 6x + 9             │ (x
- 3)²               │
└─────────────────────────┴────────────────────────┘
</pre>
</div>
</div>

<div id="outline-container-org48df986" class="outline-4">
<h4 id="org48df986"><span class="section-number-4">3.1.28.</span> Estratégia de Resolução</h4>
<div class="outline-text-4" id="text-3-1-28">
<p>
<b>Ao fatorar, siga esta ordem:</b>
</p>

<ol class="org-ol">
<li><b>Fator comum em evidência</b> (sempre tente primeiro!)</li>
<li><b>Diferença de quadrados</b> (a²</li>
<li>b²)</li>
<li><b>Trinômio quadrado perfeito</b> (a² ± 2ab + b²)</li>
<li><b>Trinômio x² + Sx + P</b> (procure dois números)</li>
<li><b>Agrupamento</b> (se tiver 4 termos)</li>
<li><b>Diferença/soma de cubos</b> (menos comum)</li>
</ol>

<p>
<b>Sempre verifique multiplicando de volta!</b>
</p>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para equações e funções)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgee48853" class="outline-3">`;

</script>

<template>
  <div class="class-container">
    <div class="class-header">
      <h1 class="class-title">{{ title }}</h1>
      <div class="class-meta">
        <span class="class-code">{{ code }}</span>
        <span class="class-subject">{{ subject }}</span>
      </div>
    </div>

    <div class="class-content">
      <section class="class-section">
        <h2>Temas</h2>
        <ul>
          <li v-for="theme in themes" :key="theme">{{ theme }}</li>
        </ul>
      </section>

            <section class="class-section">
        <h2>Conteúdo</h2>
        <div class="lesson-content" v-html="lessonContent"></div>
      </section>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.class-container {
  @apply min-h-screen bg-repeat p-8;
  background-image: url("/ufmg.plano.bg.jpg");
  background-color: #f5f1e8;
}

.class-header {
  @apply mb-8 text-center;
}

.class-title {
  @apply text-4xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.class-meta {
  @apply flex gap-4 justify-center;
}

.class-code,
.class-subject {
  @apply px-4 py-2 rounded font-bold;
  font-family: "Merriweather", serif;
  background: #1a5560;
  color: #f5f1e8;
}

.class-content {
  @apply max-w-4xl mx-auto bg-white/80 backdrop-blur-sm rounded-lg p-8 shadow-lg;
}

.class-section {
  @apply mb-8;
}

.class-section h2 {
  @apply text-2xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.class-section ul {
  @apply list-disc list-inside;
  font-family: "Merriweather", serif;
}

.class-section li {
  @apply mb-2;
  color: #2d4f56;
}

.class-section p {
  font-family: "Merriweather", serif;
  color: #2d4f56;
  line-height: 1.8;
}
</style>
