<script setup lang="ts">
import { ref } from "vue";

const code = "mat-32";
const title = "Matemática: Função Quadrática";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-1">
<ul class="org-ul">
<li>Matemática: Função Quadrática</li>
<li>Parte 3 (Inequações e Sistemas)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org7ace537" class="outline-4">
<h4 id="org7ace537"><span class="section-number-4">3.1.1.</span> Revisão: Função Quadrática</h4>
<div class="outline-text-4" id="text-3-1-1">
<p>
Já estudamos:
</p>
<ul class="org-ul">
<li><b>Parte 1 (Aula 26):</b> Definição, gráfico, raízes (Bhaskara), vértice</li>
<li><b>Parte 2 (Aula 30):</b> Zeros, máximo/mínimo, estudo do sinal básico</li>
</ul>

<p>
<b>Nesta aula:</b> Inequações mais complexas e sistemas envolvendo função quadrática.
</p>
</div>
</div>

<div id="outline-container-org8a48785" class="outline-4">
<h4 id="org8a48785"><span class="section-number-4">3.1.2.</span> Inequações do 2º Grau</h4>
<div class="outline-text-4" id="text-3-1-2">
<ul class="org-ul">
<li>Aprofundamento</li>
</ul>
</div>
<div id="outline-container-org05d231b" class="outline-5">
<h5 id="org05d231b"><span class="section-number-5">3.1.2.1.</span> Inequações-Produto</h5>
<div class="outline-text-5" id="text-3-1-2-1">
<p>
<b>Formato:</b> (ax² + bx + c)(dx² + ex + f) &gt; 0 (ou &lt;, ≥, ≤)
</p>

<p>
<b>Método:</b> 1. Estudar o sinal de cada fator separadamente 2. Fazer quadro de sinais 3. Multiplicar os sinais 4. Responder conforme pedido
</p>

<p>
<b>Exemplo:</b> (x²
</p>
<ul class="org-ul">
<li>4)(x²</li>
<li>9) ≤ 0</li>
</ul>

<p>
<b>Passo 1: Estudar cada fator</b>
</p>

<p>
<b>Fator 1:</b> x²
</p>
<ul class="org-ul">
<li>4</li>
<li>Raízes: x = ±2</li>
<li>a = 1 &gt; 0 (∪)</li>
<li>Sinal: + |</li>
<li>| + -2 2</li>
</ul>

<p>
<b>Fator 2:</b> x²
</p>
<ul class="org-ul">
<li>9</li>
<li>Raízes: x = ±3</li>
<li>a = 1 &gt; 0 (∪)</li>
<li>Sinal: + |</li>
<li>| + -3 3</li>
</ul>

<p>
<b>Passo 2: Quadro de sinais</b>
</p>

<pre class="example" id="org2230292">
        -3   -2    2    3
x²-4:   +    +  0  -  0  +  +
x²-9:   +  0
-    -    -  0  +
────────────────────────────────
Produto: + 0
-  0  +  0  - 0  +
</pre>

<p>
<b>Passo 3: Produto ≤ 0</b> (negativo ou zero)
</p>

<p>
Intervalos: [-3, -2] ∪ [2, 3]
</p>

<p>
<i>[Ver resposta 9 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgea13e8c" class="outline-5">
<h5 id="orgea13e8c"><span class="section-number-5">3.1.2.2.</span> Inequações-Quociente</h5>
<div class="outline-text-5" id="text-3-1-2-2">
<p>
<b>Formato:</b> (ax² + bx + c)/(dx² + ex + f) &gt; 0
</p>

<p>
<b>Método:</b> 1. Estudar sinal do numerador 2. Estudar sinal do denominador 3. Quadro de sinais (dividir sinais) 4. <b>IMPORTANTE:</b> Denominador ≠ 0 (excluir raízes do denominador)
</p>

<p>
<b>Exemplo:</b> (x²
</p>
<ul class="org-ul">
<li>1)/(x²</li>
<li>4) ≥ 0</li>
</ul>

<p>
<b>Numerador:</b> x²
</p>
<ul class="org-ul">
<li>1</li>
<li>Raízes: x = ±1</li>
<li>a = 1 &gt; 0</li>
<li>Sinal: + |</li>
<li>| + -1 1</li>
</ul>

<p>
<b>Denominador:</b> x²
</p>
<ul class="org-ul">
<li>4</li>
<li>Raízes: x = ±2 (EXCLUIR da resposta!)</li>
<li>a = 1 &gt; 0</li>
<li>Sinal: + |</li>
<li>| + -2 2</li>
</ul>

<p>
<b>Quadro:</b>
</p>

<pre class="example" id="org682af59">
          -2   -1    1    2
Numer.:   +    + 0  - 0  +    +
Denom.:   + ≠0
-    -    - ≠0 +
────────────────────────────────
Quoc.:    +  ∅
- 0  + 0  -  ∅  +
</pre>

<p>
<b>Quociente ≥ 0:</b> positivo ou zero
</p>

<p>
<i>[Ver resposta 10 no final do documento]</i>
</p>

<p>
<b>Observe:</b> -2 e 2 EXCLUÍDOS (denominador zero), -1 e 1 INCLUÍDOS (numerador zero)
</p>
</div>
</div>

<div id="outline-container-org3d8208d" class="outline-5">
<h5 id="org3d8208d"><span class="section-number-5">3.1.2.3.</span> Inequações Simultâneas</h5>
<div class="outline-text-5" id="text-3-1-2-3">
<p>
<b>Formato:</b> Sistema de inequações
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgfb0c585">
{ x²
- 5x + 6 &lt; 0
{ x²
- 4 ≥ 0
</pre>

<p>
<b>Resolver cada uma:</b>
</p>

<p>
<b>1ª inequação:</b> x²
</p>
<ul class="org-ul">
<li>5x + 6 &lt; 0</li>
<li>Raízes: 2 e 3</li>
<li>a &gt; 0 → negativa entre raízes</li>
<li>S₁ = (2, 3)</li>
</ul>

<p>
<b>2ª inequação:</b> x²
</p>
<ul class="org-ul">
<li>4 ≥ 0</li>
<li>Raízes: -2 e 2</li>
<li>a &gt; 0 → positiva fora raízes (ou nas raízes)</li>
<li>S₂ = (-∞, -2] ∪ [2, +∞)</li>
</ul>

<p>
<b>Interseção S₁ ∩ S₂:</b>
</p>

<pre class="example" id="org9dae6c6">
S₁:    ═══════(───)═══════
              2   3
              
S₂: ══════]       [════════
         -2       2
         
S₁∩S₂:          [─)
                2 3
</pre>

<p>
<i>[Ver resposta 11 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgdc35e33" class="outline-4">
<h4 id="orgdc35e33"><span class="section-number-4">3.1.3.</span> Sistemas de Equações do 2º Grau</h4>
<div class="outline-text-4" id="text-3-1-3">
</div>
<div id="outline-container-org3712d5c" class="outline-5">
<h5 id="org3712d5c"><span class="section-number-5">3.1.3.1.</span> Sistema Linear-Quadrático</h5>
<div class="outline-text-5" id="text-3-1-3-1">
<p>
<b>Formato:</b>
</p>

<pre class="example" id="org3c403c1">
{ y = ax + b         (reta)
{ y = cx² + dx + e   (parábola)
</pre>

<p>
<b>Método:</b> Substituição
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org4357b87">
{ y = 2x + 1
{ y = x²
- 2x + 3
</pre>

<p>
<b>Substituição:</b> 2x + 1 = x²
</p>
<ul class="org-ul">
<li>2x + 3 0 = x²</li>
<li>4x + 2 x²</li>
<li>4x + 2 = 0</li>
</ul>

<p>
<b>Bhaskara:</b> Δ = 16
</p>
<ul class="org-ul">
<li>8 = 8 x = (4 ± √8)/2 = (4 ± 2√2)/2 = 2 ± √2</li>
</ul>

<p>
x₁ = 2 + √2 x₂ = 2
</p>
<ul class="org-ul">
<li>√2</li>
</ul>

<p>
<b>Encontrar y:</b> y₁ = 2(2 + √2) + 1 = 5 + 2√2 y₂ = 2(2
</p>
<ul class="org-ul">
<li>√2) + 1 = 5</li>
<li>2√2</li>
</ul>

<p>
<b>Soluções:</b>
</p>
<ul class="org-ul">
<li>(2 + √2, 5 + 2√2)</li>
<li>(2</li>
<li>√2, 5</li>
<li>2√2)</li>
</ul>

<p>
<b>Interpretação geométrica:</b> Pontos onde a reta intercepta a parábola.
</p>
</div>
</div>

<div id="outline-container-org86bc926" class="outline-5">
<h5 id="org86bc926"><span class="section-number-5">3.1.3.2.</span> Sistema Quadrático-Quadrático</h5>
<div class="outline-text-5" id="text-3-1-3-2">
<p>
<b>Formato:</b>
</p>

<pre class="example" id="org65490c1">
{ y = ax² + bx + c
{ y = dx² + ex + f
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgba28341">
{ y = x²
- 4
{ y = -x² + 2x + 4
</pre>

<p>
<b>Igualando:</b> x²
</p>
<ul class="org-ul">
<li>4 = -x² + 2x + 4 2x²</li>
<li>2x</li>
<li>8 = 0 x²</li>
<li>x</li>
<li>4 = 0</li>
</ul>

<p>
Δ = 1 + 16 = 17 x = (1 ± √17)/2
</p>

<p>
E assim por diante&#x2026;
</p>
</div>
</div>
</div>

<div id="outline-container-org0c57f52" class="outline-4">
<h4 id="org0c57f52"><span class="section-number-4">3.1.4.</span> Aplicações</h4>
<div class="outline-text-4" id="text-3-1-4">
<ul class="org-ul">
<li>Problemas Contextualizados</li>
</ul>
</div>
<div id="outline-container-org232a0a5" class="outline-5">
<h5 id="org232a0a5"><span class="section-number-5">3.1.4.1.</span> Problema 1: Geometria</h5>
<div class="outline-text-5" id="text-3-1-4-1">
<p>
Um retângulo tem perímetro 20 cm e área 24 cm². Quais suas dimensões?
</p>

<p>
<b>Solução:</b>
</p>

<p>
Sejam x e y os lados.
</p>

<pre class="example" id="org4694831">
{ 2x + 2y = 20  →  x + y = 10  →  y = 10
- x
{ xy = 24
</pre>

<p>
Substituindo: x(10
</p>
<ul class="org-ul">
<li>x) = 24 10x</li>
<li>x² = 24 x²</li>
<li>10x + 24 = 0</li>
</ul>

<p>
Fatorando: (x
</p>
<ul class="org-ul">
<li>4)(x</li>
<li>6) = 0 x = 4 ou x = 6</li>
</ul>

<p>
Se x = 4: y = 6 Se x = 6: y = 4
</p>

<p>
<i>[Ver resposta 12 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org0dd343c" class="outline-5">
<h5 id="org0dd343c"><span class="section-number-5">3.1.4.2.</span> Problema 2: Movimento (Física)</h5>
<div class="outline-text-5" id="text-3-1-4-2">
<p>
Um projétil é lançado verticalmente. Sua altura h(t) em metros no tempo t (segundos) é dada por:
</p>

<p>
h(t) = -5t² + 20t + 5
</p>

<ol class="org-ol">
<li>Qual a altura máxima?</li>
<li>Quando atinge o solo (h = 0)?</li>
</ol>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li><b>Altura máxima = yᵥ</b></li>
</ol>

<p>
a = -5, b = 20, c = 5
</p>

<p>
tᵥ = -20/2(-5) = 20/10 = 2 s
</p>

<p>
hᵥ = -5(4) + 20(2) + 5 = -20 + 40 + 5 = 25 m
</p>

<p>
<b>Máxima: 25 m</b> (em t = 2 s)
</p>

<ol class="org-ol">
<li value="2"><b>h = 0:</b></li>
</ol>

<p>
-5t² + 20t + 5 = 0 t²
</p>
<ul class="org-ul">
<li>4t</li>
<li>1 = 0</li>
</ul>

<p>
Δ = 16 + 4 = 20
</p>

<p>
t = (4 ± √20)/2 = (4 ± 2√5)/2 = 2 ± √5
</p>

<p>
t₁ = 2
</p>
<ul class="org-ul">
<li>√5 ≈ -0,24 s (descartado: negativo) t₂ = 2 + √5 ≈ 4,24 s ✓</li>
</ul>

<p>
<i>[Ver resposta 13 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb38520e" class="outline-5">
<h5 id="orgb38520e"><span class="section-number-5">3.1.4.3.</span> Problema 3: Economia</h5>
<div class="outline-text-5" id="text-3-1-4-3">
<p>
Uma empresa descobriu que o lucro L (em mil reais) ao vender x unidades é dado por:
</p>

<p>
L(x) = -x² + 40x
</p>
<ul class="org-ul">
<li>300</li>

<li>Quantas unidades deve vender para lucro máximo?</li>
<li>Qual o lucro máximo?</li>
<li>Para quais quantidades há prejuízo (L &lt; 0)?</li>
</ul>

<p>
<b>Solução:</b>
</p>

<p>
a = -1, b = 40, c = -300
</p>

<ol class="org-ol">
<li><b>xᵥ = -40/2(-1) = 20 unidades</b></li>

<li>*Lᵥ = -(20)² + 40(20)</li>
<li>300* = -400 + 800</li>
<li>300 = 100</li>
</ol>

<p>
<b>Lucro máximo: 100 mil reais</b>
</p>

<ol class="org-ol">
<li value="3"><b>L &lt; 0:</b></li>
</ol>

<p>
Raízes: Δ = 1600
</p>
<ul class="org-ul">
<li>1200 = 400 x = (40 ± 20)/2 x₁ = 10, x₂ = 30</li>
</ul>

<p>
a = -1 &lt; 0 (∩): negativa fora das raízes
</p>

<p>
<b>Prejuízo:</b> x &lt; 10 ou x &gt; 30
</p>

<p>
Mas x ≥ 0 (não há quantidade negativa):
</p>

<p>
<i>[Ver resposta 14 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org1112f5d" class="outline-4">
<h4 id="org1112f5d"><span class="section-number-4">3.1.5.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-1-5">
</div>
<div id="outline-container-orgf1b721c" class="outline-5">
<h5 id="orgf1b721c"><span class="section-number-5">3.1.5.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-1-5-1">
<p>
Resolva: (x
</p>
<ul class="org-ul">
<li>2)(x²</li>
<li>9) &gt; 0</li>
</ul>

<p>
<b>Solução:</b>
</p>

<p>
<b>Fator 1:</b> x
</p>
<ul class="org-ul">
<li>2</li>
<li>Raiz: x = 2</li>
<li>Sinal:</li>
<li>| + 2</li>
</ul>

<p>
<b>Fator 2:</b> x²
</p>
<ul class="org-ul">
<li>9</li>
<li>Raízes: x = ±3</li>
<li>Sinal: + |</li>
<li>| + -3 3</li>
</ul>

<p>
<b>Quadro:</b>
</p>

<pre class="example" id="orge2bec11">
      -3    2    3
x-2:  -  -  -  0 +  +
x²-9: + 0
-    - 0 +
──────────────────────
Prod:
- 0 +  0
- 0 +
</pre>

<p>
<b>Produto &gt; 0:</b> (-3, 2) ∪ (3, +∞)
</p>

<p>
<i>[Ver resposta 15 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3e593ee" class="outline-5">
<h5 id="org3e593ee"><span class="section-number-5">3.1.5.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-1-5-2">
<p>
Resolva: (x²
</p>
<ul class="org-ul">
<li>4)/(x</li>
<li>3) ≤ 0</li>
</ul>

<p>
<b>Solução:</b>
</p>

<p>
<b>Numerador:</b> x²
</p>
<ul class="org-ul">
<li>4</li>
<li>Raízes: ±2</li>
<li>Sinal: + |</li>
<li>| + -2 2</li>
</ul>

<p>
<b>Denominador:</b> x
</p>
<ul class="org-ul">
<li>3</li>
<li>Raiz: 3 (EXCLUIR)</li>
<li>Sinal:</li>
<li>| + 3</li>
</ul>

<p>
<b>Quadro:</b>
</p>

<pre class="example" id="orgf1959fe">
      -2    2    3
Num.: + 0
- 0 +    +
Den.:
-   -   - ≠0 +
──────────────────────
Quo.:
- 0 + 0
-  ∅  +
</pre>

<p>
<b>Quociente ≤ 0:</b> [-2, 2] ∪ (2, 3)
</p>

<p>
Simplificando: [-2, 2] ∪ (2, 3) = [-2, 3)
</p>

<p>
<i>[Ver resposta 16 no final do documento]</i>
</p>

<p>
(3 excluído pois anula denominador)
</p>
</div>
</div>

<div id="outline-container-org69d5f14" class="outline-5">
<h5 id="org69d5f14"><span class="section-number-5">3.1.5.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-1-5-3">
<p>
Determine os pontos de interseção de y = x² e y = 2x + 3.
</p>

<p>
<b>Solução:</b>
</p>

<p>
x² = 2x + 3 x²
</p>
<ul class="org-ul">
<li>2x</li>
<li>3 = 0 (x</li>
<li>3)(x + 1) = 0 x = 3 ou x = -1</li>
</ul>

<p>
<b>Para x = 3:</b> y = 9 <b>Para x = -1:</b> y = 1
</p>

<p>
<i>[Ver resposta 17 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org2155d5a" class="outline-4">
<h4 id="org2155d5a"><span class="section-number-4">3.1.6.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-1-6">
<ol class="org-ol">
<li><b>Inequação-produto:</b> quadro de sinais e multiplicar</li>
<li><b>Inequação-quociente:</b> EXCLUIR raízes do denominador</li>
<li><b>≥ ou ≤:</b> incluir raízes do numerador (não do denominador!)</li>
<li><b>Sistema simultâneo:</b> interseção das soluções</li>
<li><b>Problema contextualizado:</b> montar função a partir do enunciado</li>
<li><b>Máximo/mínimo:</b> sempre vértice (yᵥ)</li>
<li><b>Geometria:</b> cuidado com dimensões positivas</li>
<li><b>Física:</b> tempo negativo não tem sentido (descartar)</li>
</ol>
</div>
</div>

<div id="outline-container-orgcfb16ec" class="outline-4">
<h4 id="orgcfb16ec"><span class="section-number-4">3.1.7.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-1-7">
<p>
<b>Inequação-Produto:</b>
</p>
<ul class="org-ul">
<li>Quadro de sinais</li>
<li>Multiplicar sinais dos fatores</li>
</ul>

<p>
<b>Inequação-Quociente:</b>
</p>
<ul class="org-ul">
<li>Dividir sinais</li>
<li>Denominador ≠ 0 (excluir da resposta)</li>
</ul>

<p>
<b>Sistema Linear-Quadrático:</b>
</p>
<ul class="org-ul">
<li>Substituição</li>
<li>0, 1 ou 2 soluções</li>
</ul>

<p>
<b>Problemas:</b>
</p>
<ul class="org-ul">
<li>Identificar variáveis</li>
<li>Montar equação/sistema</li>
<li>Resolver</li>
<li>Interpretar (descartar soluções sem sentido físico)</li>
</ul>
</div>
</div>

<div id="outline-container-org4d18669" class="outline-4">
<h4 id="org4d18669"><span class="section-number-4">3.1.8.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-1-8">
<pre class="example" id="org4ec1678">
Quadro de Sinais:
1. Encontrar raízes de cada fator
2. Determinar sinal de cada fator
3. Combinar sinais (× para produto, ÷ para quociente)
4. Ler região pedida

Inequação-Quociente:
Numerador = 0: pode incluir (se ≥ ou ≤)
Denominador = 0: SEMPRE excluir (∅)

Sistema de Inequações:
Resolver cada uma → Interseção S₁ ∩ S₂

Aplicações:
- Perímetro retângulo: 2(x + y)
- Área retângulo: xy
- Altura projétil: h(t) = -gt²/2 + v₀t + h₀
</pre>
</div>
</div>

<div id="outline-container-org1c5ab81" class="outline-4">
<h4 id="org1c5ab81"><span class="section-number-4">3.1.9.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-3-1-9">
<pre class="example" id="org6792e0a">
INEQUAÇÃO-PRODUTO: (f₁)(f₂) &gt; 0

        raízes f₁  raízes f₂
f₁:     ─────0────0─────
f₂:     ──0─────────0───
        ───────────────
Prod:   [combinar sinais]

INEQUAÇÃO-QUOCIENTE: f₁/f₂ ≥ 0

Num:    ────0────0────  (pode incluir)
Den:    ──≠0────────≠0  (EXCLUIR sempre)
        ──────────────
Quo:    [dividir sinais]

SISTEMA:
S₁:  ════(────)════
S₂:  ══════[──────)══

S₁∩S₂:    [──)  (interseção)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>inequações sempre caem!)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgc3939e5" class="outline-3">`;

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
