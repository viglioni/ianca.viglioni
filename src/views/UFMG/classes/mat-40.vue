<script setup lang="ts">
import { ref } from "vue";

const code = "mat-40";
const title = "Matemática: Função Logarítmica";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-7-1">
<ul class="org-ul">
<li>Matemática: Função Logarítmica</li>
<li>Parte 2 (Propriedades e Equações)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org20947ad" class="outline-4">
<h4 id="org20947ad"><span class="section-number-4">7.1.1.</span> Revisão: Logaritmos Parte 1</h4>
<div class="outline-text-4" id="text-7-1-1">
<p>
Na Aula 38, estudamos:
</p>
<ul class="org-ul">
<li>Definição: log_a b = x ⟺ a^x = b</li>
<li>Casos especiais: log_a 1 = 0, log_a a = 1</li>
<li>Logaritmo decimal (log) e natural (ln)</li>
<li>Condições de existência</li>
</ul>

<p>
<b>Nesta aula:</b> Propriedades operatórias e equações logarítmicas.
</p>
</div>
</div>

<div id="outline-container-org72076f5" class="outline-4">
<h4 id="org72076f5"><span class="section-number-4">7.1.2.</span> Propriedades Operatórias dos Logaritmos</h4>
<div class="outline-text-4" id="text-7-1-2">
</div>
<div id="outline-container-orgc8d5530" class="outline-5">
<h5 id="orgc8d5530"><span class="section-number-5">7.1.2.1.</span> 1. Logaritmo do Produto</h5>
<div class="outline-text-5" id="text-7-1-2-1">
<pre class="example" id="org3d60ade">
log_a (b · c) = log_a b + log_a c
</pre>

<p>
<b>“Logaritmo do produto = soma dos logaritmos”</b>
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log₂ (8 × 4) = log₂ 8 + log₂ 4 = 3 + 2 = 5</li>
<li>log (100 × 10) = log 100 + log 10 = 2 + 1 = 3</li>
</ul>

<p>
<b>Aplicação:</b> log₅ 50 = log₅ (5 × 10) = log₅ 5 + log₅ 10 = 1 + log₅ 10
</p>
</div>
</div>

<div id="outline-container-org8bc7c4d" class="outline-5">
<h5 id="org8bc7c4d"><span class="section-number-5">7.1.2.2.</span> 2. Logaritmo do Quociente</h5>
<div class="outline-text-5" id="text-7-1-2-2">
<pre class="example" id="orgaea9a95">
log_a (b/c) = log_a b
- log_a c
</pre>

<p>
<b>“Logaritmo do quociente = diferença dos logaritmos”</b>
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log₂ (16/4) = log₂ 16</li>
<li>log₂ 4 = 4</li>
<li>2 = 2</li>
<li>log (1000/10) = log 1000</li>
<li>log 10 = 3</li>
<li>1 = 2</li>
</ul>
</div>
</div>

<div id="outline-container-orge50139b" class="outline-5">
<h5 id="orge50139b"><span class="section-number-5">7.1.2.3.</span> 3. Logaritmo da Potência</h5>
<div class="outline-text-5" id="text-7-1-2-3">
<pre class="example" id="org8a1a965">
log_a (b^n) = n · log_a b
</pre>

<p>
<b>“Logaritmo da potência = expoente × logaritmo”</b>
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log₂ (8³) = 3 · log₂ 8 = 3 × 3 = 9</li>
<li>log (100²) = 2 · log 100 = 2 × 2 = 4</li>
<li>log₃ (√9) = log₃ (9^(1/2)) = (1/2) · log₃ 9 = (1/2) × 2 = 1</li>
</ul>
</div>
</div>

<div id="outline-container-org495d128" class="outline-5">
<h5 id="org495d128"><span class="section-number-5">7.1.2.4.</span> 4. Mudança de Base</h5>
<div class="outline-text-5" id="text-7-1-2-4">
<pre class="example" id="org7a537df">
log_a b = (log_c b) / (log_c a)
</pre>

<p>
<b>Casos particulares:</b>
</p>

<p>
<b>Para base 10:</b>
</p>

<pre class="example" id="orgf38a73d">
log_a b = (log b) / (log a)
</pre>

<p>
<b>Para base e:</b>
</p>

<pre class="example" id="org788edba">
log_a b = (ln b) / (ln a)
</pre>

<p>
<b>Consequência importante:</b>
</p>

<pre class="example" id="org121ec6f">
log_a b = 1 / log_b a
</pre>

<p>
<b>Exemplos:</b>
</p>

<p>
log₂ 5 = (log 5) / (log 2) ≈ 0,699 / 0,301 ≈ 2,32
</p>

<p>
log₅ 2 = 1 / log₂ 5 ≈ 1 / 2,32 ≈ 0,43
</p>
</div>
</div>
</div>

<div id="outline-container-org3ba11d6" class="outline-4">
<h4 id="org3ba11d6"><span class="section-number-4">7.1.3.</span> Aplicações das Propriedades</h4>
<div class="outline-text-4" id="text-7-1-3">
</div>
<div id="outline-container-org1cd68bf" class="outline-5">
<h5 id="org1cd68bf"><span class="section-number-5">7.1.3.1.</span> Exemplo 1: Simplificar</h5>
<div class="outline-text-5" id="text-7-1-3-1">
<p>
log 2 + log 5
</p>

<p>
<b>Solução:</b> = log (2 × 5) = log 10 = 1
</p>
</div>
</div>

<div id="outline-container-org465893d" class="outline-5">
<h5 id="org465893d"><span class="section-number-5">7.1.3.2.</span> Exemplo 2: Simplificar</h5>
<div class="outline-text-5" id="text-7-1-3-2">
<p>
log₃ 81
</p>
<ul class="org-ul">
<li>log₃ 9</li>
</ul>

<p>
<b>Solução:</b> = log₃ (81/9) = log₃ 9 = log₃ (3²) = 2
</p>
</div>
</div>

<div id="outline-container-orgd33892e" class="outline-5">
<h5 id="orgd33892e"><span class="section-number-5">7.1.3.3.</span> Exemplo 3: Calcular</h5>
<div class="outline-text-5" id="text-7-1-3-3">
<p>
log₂ 5 + log₂ 8
</p>
<ul class="org-ul">
<li>log₂ 10</li>
</ul>

<p>
<b>Solução:</b> = log₂ (5 × 8 / 10) = log₂ (40/10) = log₂ 4 = log₂ (2²) = 2
</p>
</div>
</div>

<div id="outline-container-orgd31e1df" class="outline-5">
<h5 id="orgd31e1df"><span class="section-number-5">7.1.3.4.</span> Exemplo 4: Simplificar</h5>
<div class="outline-text-5" id="text-7-1-3-4">
<p>
2 log 5 + log 4
</p>

<p>
<b>Solução:</b> = log (5²) + log 4 = log 25 + log 4 = log (25 × 4) = log 100 = 2
</p>
</div>
</div>
</div>

<div id="outline-container-org6442a6c" class="outline-4">
<h4 id="org6442a6c"><span class="section-number-4">7.1.4.</span> Equações Logarítmicas</h4>
<div class="outline-text-4" id="text-7-1-4">
<p>
<b>Equação logarítmica:</b> incógnita dentro do logaritmo ou como logaritmo.
</p>
</div>

<div id="outline-container-orgac77d45" class="outline-5">
<h5 id="orgac77d45"><span class="section-number-5">7.1.4.1.</span> Tipo 1: log_a f(x) = k</h5>
<div class="outline-text-5" id="text-7-1-4-1">
<p>
<b>Método:</b> Passar para forma exponencial
</p>

<p>
<b>Exemplo:</b> log₂ (x + 1) = 3
</p>

<p>
2³ = x + 1 8 = x + 1 <b>x = 7</b>
</p>

<p>
<b>Verificação:</b> log₂ (7 + 1) = log₂ 8 = 3 ✓
</p>
</div>
</div>

<div id="outline-container-orgb23ea0d" class="outline-5">
<h5 id="orgb23ea0d"><span class="section-number-5">7.1.4.2.</span> Tipo 2: log_a f(x) = log_a g(x)</h5>
<div class="outline-text-5" id="text-7-1-4-2">
<p>
<b>Método:</b> Igualar argumentos (se bases iguais)
</p>

<p>
<b>Exemplo:</b> log₅ (2x
</p>
<ul class="org-ul">
<li>3) = log₅ (x + 1)</li>
</ul>

<p>
2x
</p>
<ul class="org-ul">
<li>3 = x + 1 x = 4</li>
</ul>

<p>
<b>Verificação de condições:</b> 2x
</p>
<ul class="org-ul">
<li>3 &gt; 0 → x &gt; 3/2 ✓ x + 1 &gt; 0 → x &gt; -1 ✓ x = 4 satisfaz ambas</li>
</ul>

<p>
<i>[Ver resposta 37 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org77a353d" class="outline-5">
<h5 id="org77a353d"><span class="section-number-5">7.1.4.3.</span> Tipo 3: Equações com Propriedades</h5>
<div class="outline-text-5" id="text-7-1-4-3">
<p>
<b>Exemplo 1:</b> log x + log (x
</p>
<ul class="org-ul">
<li>3) = 1</li>
</ul>

<p>
<b>Solução:</b> log [x(x
</p>
<ul class="org-ul">
<li>3)] = 1 log (x²</li>
<li>3x) = 1</li>
</ul>

<p>
x²
</p>
<ul class="org-ul">
<li>3x = 10¹ x²</li>
<li>3x</li>
<li>10 = 0 (x</li>
<li>5)(x + 2) = 0</li>
</ul>

<p>
x = 5 ou x = -2
</p>

<p>
<b>Verificar condições:</b>
</p>
<ul class="org-ul">
<li>x &gt; 0 ✓ (x = 5) ✗ (x = -2)</li>
<li>x</li>
<li>3 &gt; 0 → x &gt; 3 ✓ (x = 5) ✗ (x = -2)</li>
</ul>

<p>
<i>[Ver resposta 38 no final do documento]</i>
</p>

<p>
<b>Exemplo 2:</b> log₂ x
</p>
<ul class="org-ul">
<li>log₂ (x</li>
<li>1) = 1</li>
</ul>

<p>
log₂ [x/(x
</p>
<ul class="org-ul">
<li>1)] = 1</li>
</ul>

<p>
x/(x
</p>
<ul class="org-ul">
<li>1) = 2¹</li>
</ul>

<p>
x = 2(x
</p>
<ul class="org-ul">
<li>1) x = 2x</li>
<li>2 x = 2</li>
</ul>

<p>
<b>Verificação:</b> x = 2 &gt; 0 ✓, x
</p>
<ul class="org-ul">
<li>1 = 1 &gt; 0 ✓</li>
</ul>

<p>
<i>[Ver resposta 39 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgfed533c" class="outline-5">
<h5 id="orgfed533c"><span class="section-number-5">7.1.4.4.</span> Tipo 4: Substituição</h5>
<div class="outline-text-5" id="text-7-1-4-4">
<p>
<b>Exemplo:</b> (log x)²
</p>
<ul class="org-ul">
<li>3 log x + 2 = 0</li>
</ul>

<p>
<b>Substituição:</b> y = log x
</p>

<p>
y²
</p>
<ul class="org-ul">
<li>3y + 2 = 0 (y</li>
<li>1)(y</li>
<li>2) = 0 y = 1 ou y = 2</li>
</ul>

<p>
<b>Voltar para x:</b> log x = 1 → x = 10¹ = 10 log x = 2 → x = 10² = 100
</p>

<p>
<i>[Ver resposta 40 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org7a18c1b" class="outline-4">
<h4 id="org7a18c1b"><span class="section-number-4">7.1.5.</span> Inequações Logarítmicas</h4>
<div class="outline-text-4" id="text-7-1-5">
<p>
<b>Regra depende da base:</b>
</p>

<p>
<b>Se a &gt; 1:</b> função crescente
</p>

<pre class="example" id="orgd0627aa">
log_a f(x) &gt; log_a g(x)  →  f(x) &gt; g(x)
</pre>

<p>
<b>Se 0 &lt; a &lt; 1:</b> função decrescente
</p>

<pre class="example" id="orgf8360bf">
log_a f(x) &gt; log_a g(x)  →  f(x) &lt; g(x)  (inverte!)
</pre>

<p>
<b>Exemplo 1:</b> log₂ (x + 1) &gt; log₂ 5
</p>

<p>
Base 2 &gt; 1 (crescente) → mantém sinal
</p>

<p>
x + 1 &gt; 5 x &gt; 4
</p>

<p>
<b>Condição:</b> x + 1 &gt; 0 → x &gt; -1
</p>

<p>
<b>Interseção:</b> x &gt; 4
</p>

<p>
<i>[Ver resposta 41 no final do documento]</i>
</p>

<p>
<b>Exemplo 2:</b> log_(1/2) x &lt; log_(1/2) 4
</p>

<p>
Base 1/2 &lt; 1 (decrescente) → <b>inverte</b>
</p>

<p>
x &gt; 4
</p>

<p>
<b>Condição:</b> x &gt; 0
</p>

<p>
<b>Interseção:</b> x &gt; 4
</p>

<p>
<i>[Ver resposta 42 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3a6b721" class="outline-4">
<h4 id="org3a6b721"><span class="section-number-4">7.1.6.</span> Gráfico da Função Logarítmica</h4>
<div class="outline-text-4" id="text-7-1-6">
<pre class="example" id="orgcf6a458">
GRÁFICOS DA FUNÇÃO LOGARÍTMICA: f(x) = logₐ x

Caso 1: a &gt; 1 (CRESCENTE)        Caso 2: 0 &lt; a &lt; 1 (DECRESCENTE)

     y                                y
     │                                │
   2 │     ╱                        2 │     ╲
     │    ╱                           │      ╲
   1 ├───●─────────               1 ├───●────────
     │  (1,0)                         │  (1,0)
─────●──────────── x              ─────●──────────── x
     1│ ╱                              1│  ╲
   -1│╱                             -1 │   ╲
     │                                 │    ╲

Propriedades Comuns:
• Sempre passa por (1, 0)
• Domínio: (0, +∞) (apenas x &gt; 0)
• Imagem: ℝ (todos os reais)
• Assíntota vertical: x = 0 (eixo y)
• NÃO existe log de número ≤ 0

Se a &gt; 1:                       Se 0 &lt; a &lt; 1:
• Função CRESCENTE              • Função DECRESCENTE
• Inversa de aˣ com a &gt; 1      • Inversa de aˣ com 0 &lt; a &lt; 1

SIMETRIA: log e exp são simétricas em relação à reta y = x
</pre>

<p>
<b>f(x) = log_a x</b>
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Domínio:</b> x &gt; 0 (ℝ₊*)</li>
<li><b>Imagem:</b> ℝ (todos os reais)</li>
<li><b>Intercepto com eixo x:</b> (1, 0)</li>
<li>sempre!</li>
<li><b>Assíntota vertical:</b> x = 0 (eixo y)</li>
<li><b>a &gt; 1:</b> crescente</li>
<li><b>0 &lt; a &lt; 1:</b> decrescente</li>
</ul>

<p>
<b>Relação com exponencial:</b>
</p>

<pre class="example" id="org332b286">
Se f(x) = a^x
Então f⁻¹(x) = log_a x
</pre>

<p>
Gráficos são simétricos em relação à reta y = x.
</p>
</div>
</div>

<div id="outline-container-orgddd0b9f" class="outline-4">
<h4 id="orgddd0b9f"><span class="section-number-4">7.1.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-7-1-7">
</div>
<div id="outline-container-org57ff1b5" class="outline-5">
<h5 id="org57ff1b5"><span class="section-number-5">7.1.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-7-1-7-1">
<p>
Simplifique: log₅ 25 + log₅ 5
</p>
<ul class="org-ul">
<li>log₅ 125</li>
</ul>

<p>
<b>Solução:</b> = 2 + 1
</p>
<ul class="org-ul">
<li>3 = 0</li>
</ul>
</div>
</div>

<div id="outline-container-org2ba317d" class="outline-5">
<h5 id="org2ba317d"><span class="section-number-5">7.1.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-7-1-7-2">
<p>
Calcule: log 2 + log 50
</p>

<p>
<b>Solução:</b> = log (2 × 50) = log 100 = 2
</p>
</div>
</div>

<div id="outline-container-org37b4d63" class="outline-5">
<h5 id="org37b4d63"><span class="section-number-5">7.1.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-7-1-7-3">
<p>
Resolva: log₃ (x²
</p>
<ul class="org-ul">
<li>8) = 2</li>
</ul>

<p>
<b>Solução:</b> x²
</p>
<ul class="org-ul">
<li>8 = 3² x²</li>
<li>8 = 9 x² = 17 x = ±√17</li>
</ul>

<p>
<b>Condição:</b> x²
</p>
<ul class="org-ul">
<li>8 &gt; 0 → x² &gt; 8</li>
</ul>

<p>
Ambos √17 e -√17 satisfazem (pois 17 &gt; 8)
</p>

<p>
<i>[Ver resposta 43 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org8c18ef4" class="outline-5">
<h5 id="org8c18ef4"><span class="section-number-5">7.1.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-7-1-7-4">
<p>
Resolva: log x + log (x + 3) = 1
</p>

<p>
<b>Solução:</b> log [x(x + 3)] = 1 x² + 3x = 10 x² + 3x
</p>
<ul class="org-ul">
<li>10 = 0 (x + 5)(x</li>
<li>2) = 0</li>
</ul>

<p>
x = -5 ou x = 2
</p>

<p>
<b>Condições:</b> x &gt; 0: apenas x = 2 ✓ x + 3 &gt; 0: x &gt; -3, ambos satisfazem, mas x = -5 já foi eliminado
</p>

<p>
<i>[Ver resposta 44 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb532042" class="outline-5">
<h5 id="orgb532042"><span class="section-number-5">7.1.7.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-7-1-7-5">
<p>
Calcule log₈ 2.
</p>

<p>
<b>Solução:</b>
</p>

<p>
*Método 1
</p>
<ul class="org-ul">
<li>Definição:* 8^x = 2 (2³)^x = 2¹ 2^(3x) = 2¹ 3x = 1 x = 1/3</li>
</ul>

<p>
*Método 2
</p>
<ul class="org-ul">
<li>Mudança de base:* log₈ 2 = (log 2)/(log 8) = (log 2)/(log 2³) = (log 2)/(3 log 2) = 1/3</li>
</ul>

<p>
<i>[Ver resposta 45 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org2f00828" class="outline-4">
<h4 id="org2f00828"><span class="section-number-4">7.1.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-7-1-8">
<ol class="org-ol">
<li><b>Produto:</b> log(ab) = log a + log b</li>
<li><b>Quociente:</b> log(a/b) = log a</li>
<li>log b</li>
<li><b>Potência:</b> log(a^n) = n log a</li>
<li><b>Mudança de base:</b> log_a b = (log b)/(log a)</li>
<li><b>Equação log_a f = log_a g:</b> f = g (igualar)</li>
<li><b>Inequação e a &gt; 1:</b> mantém sinal</li>
<li><b>Inequação e 0 &lt; a &lt; 1:</b> inverte sinal</li>
<li><b>Sempre verificar condições:</b> logaritmando &gt; 0</li>
</ol>
</div>
</div>

<div id="outline-container-org59df736" class="outline-4">
<h4 id="org59df736"><span class="section-number-4">7.1.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-7-1-9">
<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>Produto: log(ab) = log a + log b</li>
<li>Quociente: log(a/b) = log a</li>
<li>log b</li>
<li>Potência: log(a^n) = n log a</li>
<li>Mudança: log_a b = (log b)/(log a)</li>
</ul>

<p>
<b>Equações:</b>
</p>
<ul class="org-ul">
<li>log_a f(x) = k → a^k = f(x)</li>
<li>log_a f = log_a g → f = g</li>
</ul>

<p>
<b>Inequações:</b>
</p>
<ul class="org-ul">
<li>a &gt; 1: crescente (mantém)</li>
<li>0 &lt; a &lt; 1: decrescente (inverte)</li>
</ul>

<p>
<b>Sempre:</b> verificar condições (&gt; 0)
</p>
</div>
</div>

<div id="outline-container-orgaef80cd" class="outline-4">
<h4 id="orgaef80cd"><span class="section-number-4">7.1.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-7-1-10">
<pre class="example" id="org0872b3f">
Propriedades Operatórias:
log_a (bc) = log_a b + log_a c
log_a (b/c) = log_a b
- log_a c
log_a (b^n) = n · log_a b

Mudança de Base:
log_a b = (log_c b) / (log_c a)
log_a b = (log b) / (log a)  [base 10]
log_a b = (ln b) / (ln a)    [base e]
log_a b = 1 / log_b a

Equação:
log_a f(x) = log_a g(x)  ⟹  f(x) = g(x)

Inequação:
a &gt; 1:     log_a f &gt; log_a g  ⟹  f &gt; g
0 &lt; a &lt; 1: log_a f &gt; log_a g  ⟹  f &lt; g

Condições:
Sempre verificar logaritmando &gt; 0
</pre>
</div>
</div>

<div id="outline-container-org2038cd2" class="outline-4">
<h4 id="org2038cd2"><span class="section-number-4">7.1.11.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-7-1-11">
<pre class="example" id="orgd145811">
PROPRIEDADES:

Produto:      Quociente:
log(a×b)      log(a/b)
  =             =
log a + log b log a
- log b

Potência:
log(a^n) = n·log a

EQUAÇÃO:
log_a f = log_a g
     ↓
    f = g

INEQUAÇÃO:
a &gt; 1 (cresce):   0 &lt; a &lt; 1 (decresce):
log_a f &gt; log_a g log_a f &gt; log_a g
     ↓                 ↓
    f &gt; g             f &lt; g
  (mantém)          (inverte)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>propriedades são muito cobradas!)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orge409ac0" class="outline-3">`;

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
