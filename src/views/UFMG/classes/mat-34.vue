<script setup lang="ts">
import { ref } from "vue";

const code = "mat-34";
const title = "Matemática: Função Exponencial";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-1">
<ul class="org-ul">
<li>Matemática: Função Exponencial</li>
<li>Parte 1 (Potenciação e Propriedades)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orga277fe2" class="outline-4">
<h4 id="orga277fe2"><span class="section-number-4">4.1.1.</span> Introdução: Crescimento Exponencial</h4>
<div class="outline-text-4" id="text-4-1-1">
<p>
<b>Problemas que envolvem crescimento/decrescimento muito rápido:</b>
</p>
<ul class="org-ul">
<li>População de bactérias (duplica a cada hora)</li>
<li>Juros compostos (dinheiro cresce exponencialmente)</li>
<li>Desintegração radioativa (decaimento exponencial)</li>
</ul>

<p>
Esses fenômenos são modelados por <b>funções exponenciais</b>.
</p>
</div>
</div>

<div id="outline-container-orgbc32ffd" class="outline-4">
<h4 id="orgbc32ffd"><span class="section-number-4">4.1.2.</span> Revisão: Potenciação</h4>
<div class="outline-text-4" id="text-4-1-2">
</div>
<div id="outline-container-org61e8917" class="outline-5">
<h5 id="org61e8917"><span class="section-number-5">4.1.2.1.</span> Definição</h5>
<div class="outline-text-5" id="text-4-1-2-1">
<p>
<b>Potência:</b> a^n (a elevado a n)
</p>
<ul class="org-ul">
<li><b>Base:</b> a</li>
<li><b>Expoente:</b> n</li>
<li><b>Resultado:</b> potência</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>2³ = 2 × 2 × 2 = 8</li>
<li>5² = 5 × 5 = 25</li>
<li>10⁴ = 10.000</li>
</ul>
</div>
</div>

<div id="outline-container-org58fefe4" class="outline-5">
<h5 id="org58fefe4"><span class="section-number-5">4.1.2.2.</span> Casos Especiais</h5>
<div class="outline-text-5" id="text-4-1-2-2">
<p>
<b>Expoente zero:</b>
</p>

<pre class="example" id="org865857c">
a⁰ = 1  (para a ≠ 0)
</pre>

<p>
Exemplos: 5⁰ = 1, 100⁰ = 1
</p>

<p>
<b>Expoente um:</b>
</p>

<pre class="example" id="orgf3892b8">
a¹ = a
</pre>

<p>
<b>Expoente negativo:</b>
</p>

<pre class="example" id="org78b47e8">
a^(-n) = 1/a^n
</pre>

<p>
Exemplos:
</p>
<ul class="org-ul">
<li>2^(-3) = 1/2³ = 1/8</li>
<li>5^(-2) = 1/5² = 1/25</li>
</ul>

<p>
<b>Expoente fracionário:</b>
</p>

<pre class="example" id="org7752e1a">
a^(m/n) = ⁿ√(a^m)
</pre>

<p>
Exemplos:
</p>
<ul class="org-ul">
<li>4^(1/2) = √4 = 2</li>
<li>8^(2/3) = ³√(8²) = ³√64 = 4</li>
<li>27^(1/3) = ³√27 = 3</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgd9a8e2e" class="outline-4">
<h4 id="orgd9a8e2e"><span class="section-number-4">4.1.3.</span> Propriedades da Potenciação</h4>
<div class="outline-text-4" id="text-4-1-3">
</div>
<div id="outline-container-orga56cae5" class="outline-5">
<h5 id="orga56cae5"><span class="section-number-5">4.1.3.1.</span> 1. Multiplicação de Mesma Base</h5>
<div class="outline-text-5" id="text-4-1-3-1">
<pre class="example" id="org12bb46e">
a^m × a^n = a^(m+n)
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>2³ × 2² = 2^(3+2) = 2⁵ = 32</li>
<li>x⁴ × x³ = x⁷</li>
</ul>

<p>
<b>Regra:</b> Mantém a base, soma os expoentes.
</p>
</div>
</div>

<div id="outline-container-orgdbe00c3" class="outline-5">
<h5 id="orgdbe00c3"><span class="section-number-5">4.1.3.2.</span> 2. Divisão de Mesma Base</h5>
<div class="outline-text-5" id="text-4-1-3-2">
<pre class="example" id="orgbd6b7ba">
a^m / a^n = a^(m-n)
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>5⁷ / 5⁴ = 5^(7-4) = 5³ = 125</li>
<li>x⁸ / x³ = x⁵</li>
</ul>

<p>
<b>Regra:</b> Mantém a base, subtrai os expoentes.
</p>
</div>
</div>

<div id="outline-container-orgdc52203" class="outline-5">
<h5 id="orgdc52203"><span class="section-number-5">4.1.3.3.</span> 3. Potência de Potência</h5>
<div class="outline-text-5" id="text-4-1-3-3">
<pre class="example" id="org544dcc4">
(a^m)^n = a^(m×n)
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>(2³)² = 2^(3×2) = 2⁶ = 64</li>
<li>(x²)⁵ = x^(2×5) = x¹⁰</li>
</ul>

<p>
<b>Regra:</b> Mantém a base, multiplica os expoentes.
</p>
</div>
</div>

<div id="outline-container-org8fe5dad" class="outline-5">
<h5 id="org8fe5dad"><span class="section-number-5">4.1.3.4.</span> 4. Potência de Produto</h5>
<div class="outline-text-5" id="text-4-1-3-4">
<pre class="example" id="org5407cf5">
(a × b)^n = a^n × b^n
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>(2 × 3)² = 2² × 3² = 4 × 9 = 36</li>
<li>(xy)³ = x³y³</li>
</ul>
</div>
</div>

<div id="outline-container-org3e4f49f" class="outline-5">
<h5 id="org3e4f49f"><span class="section-number-5">4.1.3.5.</span> 5. Potência de Quociente</h5>
<div class="outline-text-5" id="text-4-1-3-5">
<pre class="example" id="orgb8b1a47">
(a/b)^n = a^n / b^n
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>(2/3)² = 2²/3² = 4/9</li>
<li>(x/y)⁴ = x⁴/y⁴</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgd442818" class="outline-4">
<h4 id="orgd442818"><span class="section-number-4">4.1.4.</span> Equações Exponenciais Simples</h4>
<div class="outline-text-4" id="text-4-1-4">
<p>
<b>Equação exponencial:</b> incógnita no expoente.
</p>

<p>
<b>Formato:</b> a^x = b
</p>
</div>

<div id="outline-container-org7125112" class="outline-5">
<h5 id="org7125112"><span class="section-number-5">4.1.4.1.</span> Método 1: Bases Iguais</h5>
<div class="outline-text-5" id="text-4-1-4-1">
<p>
Se conseguirmos escrever ambos os lados com a mesma base:
</p>

<pre class="example" id="orgb95b324">
a^x = a^y  →  x = y
</pre>

<p>
<b>Exemplo 1:</b> 2^x = 8
</p>

<p>
8 = 2³
</p>

<p>
2^x = 2³
</p>

<p>
<b>x = 3</b>
</p>

<p>
<b>Exemplo 2:</b> 5^(x+1) = 25
</p>

<p>
25 = 5²
</p>

<p>
5^(x+1) = 5²
</p>

<p>
x + 1 = 2
</p>

<p>
<b>x = 1</b>
</p>

<p>
<b>Exemplo 3:</b> 3^(2x) = 1/9
</p>

<p>
1/9 = 1/3² = 3^(-2)
</p>

<p>
3^(2x) = 3^(-2)
</p>

<p>
2x = -2
</p>

<p>
<b>x = -1</b>
</p>

<p>
<b>Exemplo 4:</b> 4^x = 32
</p>

<p>
Bases diferentes, mas podem ser escritas como potências de 2:
</p>

<p>
4 = 2² 32 = 2⁵
</p>

<p>
(2²)^x = 2⁵
</p>

<p>
2^(2x) = 2⁵
</p>

<p>
2x = 5
</p>

<p>
<b>x = 5/2</b>
</p>
</div>
</div>

<div id="outline-container-org769af92" class="outline-5">
<h5 id="org769af92"><span class="section-number-5">4.1.4.2.</span> Casos com Soma/Produto no Expoente</h5>
<div class="outline-text-5" id="text-4-1-4-2">
<p>
<b>Exemplo 5:</b> 2^(x+2) = 2^x + 12
</p>

<p>
Não podemos igualar expoentes diretamente!
</p>

<p>
<b>Estratégia:</b> Fatorar
</p>

<p>
2^(x+2) = 2^x × 2² = 4 × 2^x
</p>

<p>
4 × 2^x = 2^x + 12
</p>

<p>
4 × 2^x
</p>
<ul class="org-ul">
<li>2^x = 12</li>
</ul>

<p>
3 × 2^x = 12
</p>

<p>
2^x = 4
</p>

<p>
2^x = 2²
</p>

<p>
<b>x = 2</b>
</p>
</div>
</div>
</div>

<div id="outline-container-org6c15cd6" class="outline-4">
<h4 id="org6c15cd6"><span class="section-number-4">4.1.5.</span> Inequações Exponenciais Simples</h4>
<div class="outline-text-4" id="text-4-1-5">
<p>
<b>Formato:</b> a^x &gt; b (ou &lt;, ≥, ≤)
</p>

<p>
<b>Regra depende da base:</b>
</p>

<p>
<b>Se a &gt; 1:</b> função crescente
</p>
<ul class="org-ul">
<li>a^x &gt; a^y → x &gt; y</li>
</ul>

<p>
<b>Se 0 &lt; a &lt; 1:</b> função decrescente
</p>
<ul class="org-ul">
<li>a^x &gt; a^y → x &lt; y (inverte!)</li>
</ul>

<p>
<b>Exemplo 1:</b> 2^x &gt; 8
</p>

<p>
2^x &gt; 2³
</p>

<p>
Base 2 &gt; 1 (crescente) → mantém sinal
</p>

<p>
<b>x &gt; 3</b>
</p>

<p>
<b>Exemplo 2:</b> (1/2)^x ≥ 4
</p>

<p>
(1/2)^x ≥ (1/2)^(-2)
</p>

<p>
Base 1/2 &lt; 1 (decrescente) → <b>inverte</b> sinal
</p>

<p>
<b>x ≤ -2</b>
</p>
</div>
</div>

<div id="outline-container-org6d8cc91" class="outline-4">
<h4 id="org6d8cc91"><span class="section-number-4">4.1.6.</span> Gráfico da Função Exponencial (Introdução)</h4>
<div class="outline-text-4" id="text-4-1-6">
<p>
<b>Função exponencial:</b> f(x) = a^x (a &gt; 0, a ≠ 1)
</p>
</div>

<div id="outline-container-org8424809" class="outline-5">
<h5 id="org8424809"><span class="section-number-5">4.1.6.1.</span> Caso 1: a &gt; 1 (Crescente)</h5>
<div class="outline-text-5" id="text-4-1-6-1">
<p>
<b>Exemplo:</b> f(x) = 2^x
</p>

<pre class="example" id="org8c48b59">
x  | f(x)
-2 | 1/4
-1 | 1/2
 0 | 1
 1 | 2
 2 | 4
 3 | 8
</pre>

<p>
<b>Gráfico:</b>
</p>

<pre class="example" id="orgc598455">
    |
  8 |         •
  4 |       •
  2 |     •
  1 |   •─────────
1/2 | •
    |______________
    -2  0  2
</pre>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Crescente</b></li>
<li>Passa por (0, 1)</li>
<li>Eixo x é <b>assíntota horizontal</b> (nunca toca)</li>
<li>Sempre positiva (f(x) &gt; 0)</li>
</ul>
</div>
</div>

<div id="outline-container-orgbb00965" class="outline-5">
<h5 id="orgbb00965"><span class="section-number-5">4.1.6.2.</span> Caso 2: 0 &lt; a &lt; 1 (Decrescente)</h5>
<div class="outline-text-5" id="text-4-1-6-2">
<p>
<b>Exemplo:</b> f(x) = (1/2)^x
</p>

<pre class="example" id="org89c85c0">
x  | f(x)
-2 | 4
-1 | 2
 0 | 1
 1 | 1/2
 2 | 1/4
</pre>

<p>
<b>Gráfico:</b>
</p>

<pre class="example" id="orge874910">
    |
  4 | •
  2 |  •
  1 |───•─────
1/2 |     •
    |       •
    |______________
    -2  0  2
</pre>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Decrescente</b></li>
<li>Passa por (0, 1)</li>
<li>Eixo x é assíntota</li>
<li>Sempre positiva</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgba40755" class="outline-4">
<h4 id="orgba40755"><span class="section-number-4">4.1.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-1-7">
</div>
<div id="outline-container-org625fc78" class="outline-5">
<h5 id="org625fc78"><span class="section-number-5">4.1.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-1-7-1">
<p>
Calcule: a) 2⁵ b) 3^(-2) c) 16^(1/2)
</p>

<p>
<b>Soluções:</b>
</p>

<ol class="org-ol">
<li>2⁵ = 2 × 2 × 2 × 2 × 2 = 32</li>

<li>3^(-2) = 1/3² = 1/9</li>

<li>16^(1/2) = √16 = 4</li>
</ol>

<p>
<i>[Ver resposta 21 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org6c67f2d" class="outline-5">
<h5 id="org6c67f2d"><span class="section-number-5">4.1.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-1-7-2">
<p>
Simplifique: 2⁷ × 2³ / 2⁴
</p>

<p>
<b>Solução:</b>
</p>

<p>
= 2^(7+3) / 2⁴ = 2¹⁰ / 2⁴ = 2^(10-4) = 2⁶ = 64
</p>

<p>
<i>[Ver resposta 22 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org71fdc3a" class="outline-5">
<h5 id="org71fdc3a"><span class="section-number-5">4.1.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-1-7-3">
<p>
Resolva: 3^x = 81
</p>

<p>
<b>Solução:</b>
</p>

<p>
81 = 3⁴
</p>

<p>
3^x = 3⁴
</p>

<p>
<b>x = 4</b>
</p>
</div>
</div>

<div id="outline-container-orgf0c8a7e" class="outline-5">
<h5 id="orgf0c8a7e"><span class="section-number-5">4.1.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-1-7-4">
<p>
Resolva: 2^(x-1) = 1/8
</p>

<p>
<b>Solução:</b>
</p>

<p>
1/8 = 1/2³ = 2^(-3)
</p>

<p>
2^(x-1) = 2^(-3)
</p>

<p>
x
</p>
<ul class="org-ul">
<li>1 = -3</li>
</ul>

<p>
<b>x = -2</b>
</p>
</div>
</div>

<div id="outline-container-org3181621" class="outline-5">
<h5 id="org3181621"><span class="section-number-5">4.1.7.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-4-1-7-5">
<p>
Resolva a inequação: 5^x &lt; 125
</p>

<p>
<b>Solução:</b>
</p>

<p>
125 = 5³
</p>

<p>
5^x &lt; 5³
</p>

<p>
Base 5 &gt; 1 (crescente) → mantém sinal
</p>

<p>
<b>x &lt; 3</b>
</p>

<p>
<i>[Ver resposta 23 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7c061cc" class="outline-5">
<h5 id="org7c061cc"><span class="section-number-5">4.1.7.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-4-1-7-6">
<p>
Simplifique: (x²y³)² / (xy)⁴
</p>

<p>
<b>Solução:</b>
</p>

<p>
= (x²)²(y³)² / x⁴y⁴ = x⁴y⁶ / x⁴y⁴ = x^(4-4) y^(6-4) = x⁰y² = y²
</p>

<p>
<i>[Ver resposta 24 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgd94a59b" class="outline-4">
<h4 id="orgd94a59b"><span class="section-number-4">4.1.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-1-8">
<ol class="org-ol">
<li><b>a⁰ = 1</b> (sempre)</li>
<li><b>a^(-n) = 1/a^n</b> (expoente negativo = inverso)</li>
<li><b>Multiplicação:</b> soma expoentes (mesma base)</li>
<li><b>Divisão:</b> subtrai expoentes</li>
<li><b>(a^{m)}n = a^(m×n)</b></li>
<li><b>Equação a^x = a^y:</b> x = y</li>
<li><b>Inequação e a &gt; 1:</b> mantém sinal</li>
<li><b>Inequação e 0 &lt; a &lt; 1:</b> inverte sinal</li>
<li><b>Gráfico:</b> sempre passa por (0, 1)</li>
</ol>
</div>
</div>

<div id="outline-container-orge20fc6b" class="outline-4">
<h4 id="orge20fc6b"><span class="section-number-4">4.1.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-1-9">
<p>
<b>Potenciação:</b>
</p>
<ul class="org-ul">
<li>a^n = a × a × &#x2026; × a (n vezes)</li>
<li>a⁰ = 1</li>
<li>a^(-n) = 1/a^n</li>
<li>a^(m/n) = ⁿ√(a^m)</li>
</ul>

<p>
<b>Propriedades (mesma base):</b>
</p>
<ul class="org-ul">
<li>a^m × a^n = a^(m+n)</li>
<li>a^m / a^n = a^(m-n)</li>
<li>(a^{m)}n = a^(m×n)</li>
</ul>

<p>
<b>Equação Exponencial:</b>
</p>
<ul class="org-ul">
<li>a^x = a^y → x = y</li>
</ul>

<p>
<b>Inequação:</b>
</p>
<ul class="org-ul">
<li>a &gt; 1: crescente (mantém sinal)</li>
<li>0 &lt; a &lt; 1: decrescente (inverte sinal)</li>
</ul>

<p>
<b>Gráfico:</b>
</p>
<ul class="org-ul">
<li>Passa por (0, 1)</li>
<li>Sempre f(x) &gt; 0</li>
<li>Eixo x é assíntota</li>
</ul>
</div>
</div>

<div id="outline-container-org44a5aaa" class="outline-4">
<h4 id="org44a5aaa"><span class="section-number-4">4.1.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-1-10">
<pre class="example" id="org9ddbf42">
Propriedades de Potenciação:
a^m × a^n = a^(m+n)
a^m / a^n = a^(m-n)
(a^m)^n = a^(mn)
(ab)^n = a^n b^n
(a/b)^n = a^n / b^n

Casos Especiais:
a⁰ = 1
a¹ = a
a^(-n) = 1/a^n
a^(1/n) = ⁿ√a
a^(m/n) = ⁿ√(a^m)

Equação:
a^x = a^y  ⟹  x = y

Inequação:
a &gt; 1:     a^x &gt; a^y  ⟹  x &gt; y
0 &lt; a &lt; 1: a^x &gt; a^y  ⟹  x &lt; y
</pre>
</div>
</div>

<div id="outline-container-orgc3ff995" class="outline-4">
<h4 id="orgc3ff995"><span class="section-number-4">4.1.11.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-1-11">
<pre class="example" id="org5e0b4d0">
PROPRIEDADES:

Multiplicação:    Divisão:
2³ × 2² = 2⁵     2⁵ / 2² = 2³
↑soma expoentes   ↑subtrai

Potência de Potência:
(2³)² = 2⁶
    ↑multiplica

GRÁFICOS:

a &gt; 1 (crescente):   0 &lt; a &lt; 1 (decresc.):
     |                     |
   • |                   • |
  •  |(0,1)        (0,1)|  •
 •───•                 •───• 
     |                     |
─────┼─────           ─────┼─────
     
Sempre &gt; 0           Sempre &gt; 0
Passa por (0,1)      Passa por (0,1)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>função exponencial é muito cobrada!)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org99d49be" class="outline-3">`;

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
