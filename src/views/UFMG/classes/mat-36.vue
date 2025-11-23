<script setup lang="ts">
import { ref } from "vue";

const code = "mat-36";
const title = "Matemática: Função Exponencial";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-1">
<ul class="org-ul">
<li>Matemática: Função Exponencial</li>
<li>Parte 2 (Equações, Gráficos e Crescimento)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgeaebb8e" class="outline-4">
<h4 id="orgeaebb8e"><span class="section-number-4">5.1.1.</span> Revisão: Função Exponencial Parte 1</h4>
<div class="outline-text-4" id="text-5-1-1">
<p>
Na Aula 34, estudamos:
</p>
<ul class="org-ul">
<li>Potenciação e propriedades</li>
<li>Equações exponenciais simples (bases iguais)</li>
<li>Inequações básicas</li>
<li>Gráfico introdutório</li>
</ul>

<p>
<b>Nesta aula:</b> Equações mais complexas, gráficos detalhados e aplicações.
</p>
</div>
</div>

<div id="outline-container-orga4153bf" class="outline-4">
<h4 id="orga4153bf"><span class="section-number-4">5.1.2.</span> Definição de Função Exponencial</h4>
<div class="outline-text-4" id="text-5-1-2">
<p>
<b>Função Exponencial:</b>
</p>

<pre class="example" id="orga4829dd">
f(x) = a^x
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li><b>a:</b> base (a &gt; 0 e a ≠ 1)</li>
<li><b>x:</b> expoente (variável)</li>
</ul>

<p>
<b>Por que a &gt; 0 e a ≠ 1?</b>
</p>
<ul class="org-ul">
<li><b>a &gt; 0:</b> evitar resultados indefinidos (ex: (-2)^(1/2))</li>
<li><b>a ≠ 1:</b> pois 1^x = 1 (constante, não exponencial)</li>
</ul>

<p>
<b>Forma geral:</b>
</p>

<pre class="example" id="orgb17c08d">
f(x) = b · a^(cx + d) + e
</pre>

<p>
Mas começamos com a forma básica: f(x) = a^x
</p>
</div>
</div>

<div id="outline-container-org467627f" class="outline-4">
<h4 id="org467627f"><span class="section-number-4">5.1.3.</span> Propriedades da Função Exponencial</h4>
<div class="outline-text-4" id="text-5-1-3">
<p>
<b>1. Domínio:</b> D(f) = ℝ (todos os reais)
</p>

<p>
<b>2. Imagem:</b> Im(f) = ℝ₊* = (0, +∞)
</p>
<ul class="org-ul">
<li>Função sempre positiva: f(x) &gt; 0 para todo x</li>
</ul>

<p>
<b>3. Intercepto com eixo y:</b>
</p>
<ul class="org-ul">
<li>Quando x = 0: f(0) = a⁰ = 1</li>
<li>Sempre passa pelo ponto <b>(0, 1)</b></li>
</ul>

<p>
<b>4. Não intercepta eixo x:</b>
</p>
<ul class="org-ul">
<li>Nunca f(x) = 0 (sempre positiva)</li>
<li>Eixo x é <b>assíntota horizontal</b></li>
</ul>

<p>
<b>5. Injetora:</b>
</p>
<ul class="org-ul">
<li>Se a^x₁ = a^x₂, então x₁ = x₂</li>
<li>Cada valor de y corresponde a único valor de x</li>
</ul>

<p>
<b>6. Monotonia (crescimento):</b>
</p>
<ul class="org-ul">
<li><b>a &gt; 1:</b> estritamente crescente</li>
<li><b>0 &lt; a &lt; 1:</b> estritamente decrescente</li>
</ul>
</div>
</div>

<div id="outline-container-org88632f6" class="outline-4">
<h4 id="org88632f6"><span class="section-number-4">5.1.4.</span> Gráficos Detalhados</h4>
<div class="outline-text-4" id="text-5-1-4">
<pre class="example" id="orgcea966f">
GRÁFICOS DA FUNÇÃO EXPONENCIAL: f(x) = aˣ

Caso 1: a &gt; 1 (CRESCENTE)        Caso 2: 0 &lt; a &lt; 1 (DECRESCENTE)

     y                                y
     │                                │
   4 │         ╱                    4 │╲
     │        ╱                       │ ╲
   3 │       ╱                      3 │  ╲
     │      ╱                         │   ╲
   2 │     ╱                        2 │    ╲
     │    ╱                           │     ╲
   1 ├───●─────────── x             1 ├──────●──── x
     │  (0,1)                         │     (0,1)
─────┼──────────────                ─────┼──────────
     0                                    0

Propriedades Comuns:
• Sempre passa por (0, 1)
• Sempre f(x) &gt; 0 (acima do eixo x)
• Domínio: ℝ (todos os reais)
• Imagem: (0, +∞) (apenas positivos)
• NÃO tem raízes (não corta eixo x)

Se a &gt; 1:                       Se 0 &lt; a &lt; 1:
• Função CRESCENTE              • Função DECRESCENTE
• x → +∞, f(x) → +∞            • x → +∞, f(x) → 0
• x → -∞, f(x) → 0             • x → -∞, f(x) → +∞
</pre>
</div>

<div id="outline-container-orga5272cc" class="outline-5">
<h5 id="orga5272cc"><span class="section-number-5">5.1.4.1.</span> Caso 1: a &gt; 1 (Função Crescente)</h5>
<div class="outline-text-5" id="text-5-1-4-1">
<p>
<b>Exemplos:</b> f(x) = 2^x, f(x) = 3^x, f(x) = 10^x
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Cresce rapidamente para x &gt; 0</li>
<li>Aproxima-se de 0 para x → -∞</li>
<li>Passa por (0, 1)</li>
</ul>

<p>
<b>Tabela (f(x) = 2^x):</b>
</p>

<pre class="example" id="org90bf1ca">
x  | -3  | -2  | -1  |  0  |  1  |  2  |  3  
f(x)| 1/8 | 1/4 | 1/2 |  1  |  2  |  4  |  8
</pre>

<p>
<b>Gráfico:</b>
</p>

<pre class="example" id="org8527f33">
    |
  8 |           •
  4 |         •
  2 |       •
  1 |•─────•─────────
1/2 |  •
1/4 | •
    |•________________
   -3  -1  0  1  2  3
</pre>

<p>
<b>Quanto maior a base, mais “vertical” a curva:</b>
</p>
<ul class="org-ul">
<li>10^x cresce mais rápido que 2^x</li>
</ul>
</div>
</div>

<div id="outline-container-org9ccbe64" class="outline-5">
<h5 id="org9ccbe64"><span class="section-number-5">5.1.4.2.</span> Caso 2: 0 &lt; a &lt; 1 (Função Decrescente)</h5>
<div class="outline-text-5" id="text-5-1-4-2">
<p>
<b>Exemplos:</b> f(x) = (1/2)^x, f(x) = (1/3)^x
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Decresce rapidamente para x &gt; 0</li>
<li>Aproxima-se de 0 para x → +∞</li>
<li>Passa por (0, 1)</li>
</ul>

<p>
<b>Tabela (f(x) = (1/2)^x):</b>
</p>

<pre class="example" id="orgc7503f3">
x  | -3  | -2  | -1  |  0  |  1  |  2  |  3
f(x)|  8  |  4  |  2  |  1  | 1/2 | 1/4 | 1/8
</pre>

<p>
<b>Gráfico:</b>
</p>

<pre class="example" id="org6461cb7">
    |
  8 |•
  4 | •
  2 |  •
  1 |───•─────•
1/2 |       •  
1/4 |         •
    |___________•____
   -3  -1  0  1  2  3
</pre>

<p>
<b>Relação importante:</b>
</p>

<pre class="example" id="orgf048a19">
(1/a)^x = a^(-x)
</pre>

<p>
Então: f(x) = (1/2)^x é reflexão de g(x) = 2^x em relação ao eixo y
</p>
</div>
</div>
</div>

<div id="outline-container-orgecbbf95" class="outline-4">
<h4 id="orgecbbf95"><span class="section-number-4">5.1.5.</span> Equações Exponenciais Avançadas</h4>
<div class="outline-text-4" id="text-5-1-5">
</div>
<div id="outline-container-orga153dc6" class="outline-5">
<h5 id="orga153dc6"><span class="section-number-5">5.1.5.1.</span> Técnica 1: Substituição</h5>
<div class="outline-text-5" id="text-5-1-5-1">
<p>
<b>Quando aparece a mesma base com expoentes relacionados.</b>
</p>

<p>
<b>Exemplo 1:</b> 4^x
</p>
<ul class="org-ul">
<li>2^x</li>
<li>2 = 0</li>
</ul>

<p>
<b>Observar:</b> 4^x = (2²)^x = 2^(2x) = (2^x)²
</p>

<p>
<b>Substituição:</b> y = 2^x
</p>

<p>
y²
</p>
<ul class="org-ul">
<li>y</li>
<li>2 = 0</li>
</ul>

<p>
(y
</p>
<ul class="org-ul">
<li>2)(y + 1) = 0</li>
</ul>

<p>
y = 2 ou y = -1
</p>

<p>
<b>Voltar para x:</b>
</p>

<p>
2^x = 2 → x = 1 ✓
</p>

<p>
2^x = -1 → impossível (2^x &gt; 0) ✗
</p>

<p>
<i>[Ver resposta 25 no final do documento]</i>
</p>

<p>
<b>Exemplo 2:</b> 9^x
</p>
<ul class="org-ul">
<li>4·3^x + 3 = 0</li>
</ul>

<p>
9^x = (3²)^x = (3^x)²
</p>

<p>
<b>Substituição:</b> y = 3^x
</p>

<p>
y²
</p>
<ul class="org-ul">
<li>4y + 3 = 0</li>
</ul>

<p>
(y
</p>
<ul class="org-ul">
<li>1)(y</li>
<li>3) = 0</li>
</ul>

<p>
y = 1 ou y = 3
</p>

<p>
3^x = 1 = 3⁰ → x = 0 3^x = 3 = 3¹ → x = 1
</p>

<p>
<i>[Ver resposta 26 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orga6cf1bd" class="outline-5">
<h5 id="orga6cf1bd"><span class="section-number-5">5.1.5.2.</span> Técnica 2: Bases Diferentes mas Relacionadas</h5>
<div class="outline-text-5" id="text-5-1-5-2">
<p>
<b>Exemplo:</b> 2^(x+1) + 2^(x-1) = 5
</p>

<p>
<b>Fatorar usando propriedades:</b>
</p>

<p>
2^(x+1) = 2·2^x 2^(x-1) = 2^x/2
</p>

<p>
2·2^x + 2^x/2 = 5
</p>

<p>
Multiplicar por 2:
</p>

<p>
4·2^x + 2^x = 10
</p>

<p>
5·2^x = 10
</p>

<p>
2^x = 2 = 2¹
</p>

<p>
<b>x = 1</b>
</p>
</div>
</div>

<div id="outline-container-org9155a96" class="outline-5">
<h5 id="org9155a96"><span class="section-number-5">5.1.5.3.</span> Técnica 3: Logaritmo (introdução)</h5>
<div class="outline-text-5" id="text-5-1-5-3">
<p>
Para equações como 2^x = 5, precisaremos de logaritmos (próximas aulas).
</p>
</div>
</div>
</div>

<div id="outline-container-orge0c1c7d" class="outline-4">
<h4 id="orge0c1c7d"><span class="section-number-4">5.1.6.</span> Inequações Exponenciais Avançadas</h4>
<div class="outline-text-4" id="text-5-1-6">
<p>
<b>Exemplo 1:</b> 2^(2x)
</p>
<ul class="org-ul">
<li>5·2^x + 4 ≤ 0</li>
</ul>

<p>
<b>Substituição:</b> y = 2^x (y &gt; 0)
</p>

<p>
y²
</p>
<ul class="org-ul">
<li>5y + 4 ≤ 0</li>
</ul>

<p>
<b>Raízes:</b> (y
</p>
<ul class="org-ul">
<li>1)(y</li>
<li>4) = 0 y = 1 ou y = 4</li>
</ul>

<p>
<b>Estudo do sinal:</b> a = 1 &gt; 0 (parábola ∪)
</p>

<pre class="example" id="orgdf7ce3d">
\\____/
1    4
</pre>

<p>
y²
</p>
<ul class="org-ul">
<li>5y + 4 ≤ 0: <b>1 ≤ y ≤ 4</b></li>
</ul>

<p>
<b>Voltar para x:</b>
</p>

<p>
1 ≤ 2^x ≤ 4
</p>

<p>
2⁰ ≤ 2^x ≤ 2²
</p>

<p>
<b>0 ≤ x ≤ 2</b>
</p>

<p>
<i>[Ver resposta 27 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org14bc120" class="outline-4">
<h4 id="org14bc120"><span class="section-number-4">5.1.7.</span> Aplicações: Crescimento e Decaimento Exponencial</h4>
<div class="outline-text-4" id="text-5-1-7">
</div>
<div id="outline-container-orgf2c93c6" class="outline-5">
<h5 id="orgf2c93c6"><span class="section-number-5">5.1.7.1.</span> Aplicação 1: Crescimento Populacional</h5>
<div class="outline-text-5" id="text-5-1-7-1">
<p>
Uma população de bactérias dobra a cada hora. Inicialmente há 100 bactérias.
</p>

<p>
<b>Modelo:</b>
</p>

<pre class="example" id="org482b216">
P(t) = P₀ · 2^t
P(t) = 100 · 2^t
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>P(t): população após t horas</li>
<li>P₀ = 100: população inicial</li>
<li>Base 2: dobra a cada hora</li>
</ul>

<p>
<b>a) Quantas bactérias após 5 horas?</b>
</p>

<p>
P(5) = 100 · 2⁵ = 100 · 32 = 3.200 bactérias
</p>

<p>
<b>b) Quando atinge 12.800 bactérias?</b>
</p>

<p>
100 · 2^t = 12.800
</p>

<p>
2^t = 128 = 2⁷
</p>

<p>
t = 7 horas
</p>
</div>
</div>

<div id="outline-container-org98943df" class="outline-5">
<h5 id="org98943df"><span class="section-number-5">5.1.7.2.</span> Aplicação 2: Decaimento Radioativo</h5>
<div class="outline-text-5" id="text-5-1-7-2">
<p>
Uma substância radioativa tem meia-vida de 10 anos (metade se desintegra a cada 10 anos).
</p>

<p>
<b>Modelo:</b>
</p>

<pre class="example" id="orgdbd04bf">
M(t) = M₀ · (1/2)^(t/10)
</pre>

<p>
Se M₀ = 800g:
</p>

<p>
<b>a) Massa após 30 anos?</b>
</p>

<p>
M(30) = 800 · (1/2)^(30/10) = 800 · (1/2)³ = 800 · 1/8 = 100g
</p>

<p>
<b>b) Quando resta 100g?</b>
</p>

<p>
800 · (1/2)^(t/10) = 100
</p>

<p>
(1/2)^(t/10) = 1/8 = (1/2)³
</p>

<p>
t/10 = 3
</p>

<p>
t = 30 anos
</p>
</div>
</div>

<div id="outline-container-orgad73078" class="outline-5">
<h5 id="orgad73078"><span class="section-number-5">5.1.7.3.</span> Aplicação 3: Juros Compostos</h5>
<div class="outline-text-5" id="text-5-1-7-3">
<p>
Capital inicial de R$ 1.000 aplicado a 10% ao ano (juros compostos).
</p>

<p>
<b>Modelo:</b>
</p>

<pre class="example" id="org1629200">
M(t) = C · (1 + i)^t
M(t) = 1000 · (1,1)^t
</pre>

<p>
<b>Após 5 anos:</b>
</p>

<p>
M(5) = 1000 · (1,1)⁵ ≈ 1000 · 1,61 ≈ R$ 1.610
</p>
</div>
</div>
</div>

<div id="outline-container-org9160753" class="outline-4">
<h4 id="org9160753"><span class="section-number-4">5.1.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-1-8">
</div>
<div id="outline-container-org3b3e803" class="outline-5">
<h5 id="org3b3e803"><span class="section-number-5">5.1.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-1-8-1">
<p>
Resolva: 5^(2x)
</p>
<ul class="org-ul">
<li>25 = 0</li>
</ul>

<p>
<b>Solução:</b>
</p>

<p>
5^(2x) = 25 = 5²
</p>

<p>
2x = 2
</p>

<p>
<b>x = 1</b>
</p>
</div>
</div>

<div id="outline-container-org8c36149" class="outline-5">
<h5 id="org8c36149"><span class="section-number-5">5.1.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-1-8-2">
<p>
Determine o conjunto solução: 3^x &gt; 27
</p>

<p>
<b>Solução:</b>
</p>

<p>
3^x &gt; 3³
</p>

<p>
Base 3 &gt; 1 (crescente) → mantém sinal
</p>

<p>
<b>x &gt; 3</b>
</p>

<p>
<b>S = (3, +∞)</b>
</p>
</div>
</div>

<div id="outline-container-orgf782153" class="outline-5">
<h5 id="orgf782153"><span class="section-number-5">5.1.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-1-8-3">
<p>
Resolva: 2^(x+2) + 2^x = 20
</p>

<p>
<b>Solução:</b>
</p>

<p>
2^(x+2) = 2² · 2^x = 4 · 2^x
</p>

<p>
4·2^x + 2^x = 20
</p>

<p>
5·2^x = 20
</p>

<p>
2^x = 4 = 2²
</p>

<p>
<b>x = 2</b>
</p>
</div>
</div>

<div id="outline-container-org093a6ea" class="outline-5">
<h5 id="org093a6ea"><span class="section-number-5">5.1.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-1-8-4">
<p>
Uma população de 500 bactérias triplica a cada 2 horas. Quantas bactérias após 6 horas?
</p>

<p>
<b>Solução:</b>
</p>

<p>
P(t) = 500 · 3^(t/2)
</p>

<p>
P(6) = 500 · 3^(6/2) = 500 · 3³ = 500 · 27 = 13.500
</p>

<p>
<i>[Ver resposta 28 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org9e91a42" class="outline-4">
<h4 id="org9e91a42"><span class="section-number-4">5.1.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-1-9">
<ol class="org-ol">
<li><b>Sempre passa por (0, 1)</b></li>
<li><b>Sempre positiva:</b> f(x) &gt; 0</li>
<li><b>a &gt; 1:</b> crescente; <b>0 &lt; a &lt; 1:</b> decrescente</li>
<li><b>Substituição:</b> quando aparece (a^x)²</li>
<li><b>Fatorar:</b> 2^(x+1) = 2 · 2^x</li>
<li><b>Crescimento:</b> base &gt; 1</li>
<li><b>Decaimento:</b> base entre 0 e 1</li>
<li><b>Juros compostos:</b> M = C(1+i)^t</li>
</ol>
</div>
</div>

<div id="outline-container-org9988977" class="outline-4">
<h4 id="org9988977"><span class="section-number-4">5.1.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-1-10">
<p>
<b>Função Exponencial:</b>
</p>
<ul class="org-ul">
<li>f(x) = a^x (a &gt; 0, a ≠ 1)</li>
<li>Domínio: ℝ</li>
<li>Imagem: (0, +∞)</li>
<li>Passa por (0, 1)</li>
</ul>

<p>
<b>Comportamento:</b>
</p>
<ul class="org-ul">
<li>a &gt; 1: crescente</li>
<li>0 &lt; a &lt; 1: decrescente</li>
</ul>

<p>
<b>Técnicas de Resolução:</b>
</p>
<ul class="org-ul">
<li>Bases iguais: igualar expoentes</li>
<li>Substituição: y = a^x</li>
<li>Fatorar: usar propriedades</li>
</ul>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Crescimento: P(t) = P₀ · a^t (a &gt; 1)</li>
<li>Decaimento: M(t) = M₀ · a^t (0 &lt; a &lt; 1)</li>
<li>Juros: M = C(1+i)^t</li>
</ul>
</div>
</div>

<div id="outline-container-orga61443c" class="outline-4">
<h4 id="orga61443c"><span class="section-number-4">5.1.11.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-5-1-11">
<pre class="example" id="org5c783bf">
Função Exponencial:
f(x) = a^x  (a &gt; 0, a ≠ 1)

Propriedades:
- D(f) = ℝ
- Im(f) = ℝ₊* = (0, +∞)
- f(0) = 1
- a &gt; 1: crescente
- 0 &lt; a &lt; 1: decrescente

Transformações:
a^(x+n) = a^n · a^x
a^(x-n) = a^x / a^n
(a^m)^x = a^(mx)

Aplicações:
Crescimento: P(t) = P₀ · a^t
Decaimento: M(t) = M₀ · (1/2)^(t/T)  [T = meia-vida]
Juros Compostos: M = C(1 + i)^t
</pre>
</div>
</div>

<div id="outline-container-org5ce6cba" class="outline-4">
<h4 id="org5ce6cba"><span class="section-number-4">5.1.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-1-12">
<pre class="example" id="orga9914eb">
GRÁFICOS:

a &gt; 1 (crescente):     0 &lt; a &lt; 1 (decresc.):
      |                      |
    8 |        •           8 |•
    4 |      •             4 | •
    2 |    •               2 |  •
    1 |──•──               1 |───•──
      |•                     |       •
    ──┼────────           ──┼────────
      
CRESCIMENTO:           DECAIMENTO:
P(t) = P₀ · a^t       M(t) = M₀ · a^t
(a &gt; 1)               (0 &lt; a &lt; 1)

  •                      •
    •                  •
      •              •
        •          •
          •      •

SUBSTITUIÇÃO:
4^x = (2^x)²
9^x = (3^x)²
Se y = a^x, então a^(2x) = y²
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>aplicações são muito cobradas!)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org3618ba0" class="outline-3">`;

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
