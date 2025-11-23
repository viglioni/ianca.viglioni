<script setup lang="ts">
import { ref } from "vue";

const code = "mat-62";
const title = "Matemática: Revisão de Funções Exponenciais e Logarítmicas";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-7-1">
<ul class="org-ul">
<li>Matemática: Revisão de Funções Exponenciais e Logarítmicas</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgb386a51" class="outline-4">
<h4 id="orgb386a51"><span class="section-number-4">7.1.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-7-1-1">
<p>
Consolidar os principais conceitos de funções exponenciais e logarítmicas estudados durante as férias, preparando para questões da prova.
</p>
</div>
</div>

<div id="outline-container-org8c4509b" class="outline-4">
<h4 id="org8c4509b"><span class="section-number-4">7.1.2.</span> Função Exponencial</h4>
<div class="outline-text-4" id="text-7-1-2">
<ul class="org-ul">
<li>Revisão Rápida</li>
</ul>
<p>
<b>Definição:</b>
</p>

<pre class="example" id="org44262ec">
f(x) = aˣ, onde a &gt; 0 e a ≠ 1
</pre>

<p>
<b>Características principais:</b>
</p>

<p>
<b>Se a &gt; 1:</b> função <b>crescente</b>
</p>
<ul class="org-ul">
<li>x aumenta → f(x) aumenta</li>
<li>Exemplo: f(x) = 2ˣ</li>
</ul>

<p>
<b>Se 0 &lt; a &lt; 1:</b> função <b>decrescente</b>
</p>
<ul class="org-ul">
<li>x aumenta → f(x) diminui</li>
<li>Exemplo: f(x) = (1/2)ˣ</li>
</ul>

<p>
<b>Propriedades fundamentais:</b>
</p>

<pre class="example" id="orgc42aa77">
a⁰ = 1
a¹ = a
aˣ · aʸ = aˣ⁺ʸ
aˣ / aʸ = aˣ⁻ʸ
(aˣ)ʸ = aˣʸ
a⁻ˣ = 1/aˣ
</pre>

<p>
<b>Gráfico:</b>
</p>
<ul class="org-ul">
<li>Passa sempre por (0, 1)</li>
<li>Nunca toca o eixo x (assíntota horizontal)</li>
<li>Domínio: ℝ (todos os reais)</li>
<li>Imagem: ℝ₊* (reais positivos)</li>
</ul>
</div>
</div>

<div id="outline-container-org244aaaa" class="outline-4">
<h4 id="org244aaaa"><span class="section-number-4">7.1.3.</span> Equações Exponenciais</h4>
<div class="outline-text-4" id="text-7-1-3">
<ul class="org-ul">
<li>Revisão</li>
</ul>
<p>
<b>Estratégia principal:</b> igualar as bases
</p>

<p>
<b>Método:</b> 1. Transformar para mesma base 2. Igualar os expoentes 3. Resolver a equação resultante
</p>

<p>
<b>Exemplo 1:</b>
</p>

<pre class="example" id="orgbf1056d">
2ˣ = 16
2ˣ = 2⁴
x = 4
</pre>

<p>
<b>Exemplo 2:</b>
</p>

<pre class="example" id="orgaf0732c">
4ˣ = 8
(2²)ˣ = 2³
2²ˣ = 2³
2x = 3
x = 3/2
</pre>

<p>
<b>Exemplo 3:</b>
</p>

<pre class="example" id="orgea26568">
9ˣ⁺¹ = 27ˣ
(3²)ˣ⁺¹ = (3³)ˣ
3²⁽ˣ⁺¹⁾ = 3³ˣ
2(x+1) = 3x
2x + 2 = 3x
x = 2
</pre>

<p>
<b>Exemplo 4 (substituição):</b>
</p>

<pre class="example" id="org9c7536d">
4ˣ
- 5·2ˣ + 4 = 0
(2²)ˣ
- 5·2ˣ + 4 = 0
(2ˣ)²
- 5·2ˣ + 4 = 0

Faça 2ˣ = y:
y²
- 5y + 4 = 0
(y
- 4)(y
- 1) = 0
y = 4 ou y = 1

Se 2ˣ = 4 → x = 2
Se 2ˣ = 1 → x = 0

S = {0, 2}
</pre>
</div>
</div>

<div id="outline-container-org8f710e9" class="outline-4">
<h4 id="org8f710e9"><span class="section-number-4">7.1.4.</span> Função Logarítmica</h4>
<div class="outline-text-4" id="text-7-1-4">
<ul class="org-ul">
<li>Revisão Rápida</li>
</ul>
<p>
<b>Definição:</b>
</p>

<pre class="example" id="org7b46992">
logₐ b = x  ⟺  aˣ = b

onde a &gt; 0, a ≠ 1, b &gt; 0
</pre>

<p>
<b>Leitura:</b> “logaritmo de b na base a”
</p>

<p>
<b>Significado:</b> “a que expoente devo elevar a base a para obter b?”
</p>

<p>
<b>Exemplos:</b>
</p>

<pre class="example" id="org8e975f3">
log₂ 8 = 3  (pois 2³ = 8)
log₁₀ 100 = 2  (pois 10² = 100)
log₅ 1 = 0  (pois 5⁰ = 1)
log₃ 3 = 1  (pois 3¹ = 3)
</pre>

<p>
<b>Casos especiais:</b>
</p>

<pre class="example" id="orgbeb37fe">
logₐ 1 = 0  (sempre!)
logₐ a = 1  (sempre!)
logₐ aˣ = x
a^(logₐ x) = x
</pre>
</div>
</div>

<div id="outline-container-org769ec67" class="outline-4">
<h4 id="org769ec67"><span class="section-number-4">7.1.5.</span> Propriedades dos Logaritmos</h4>
<div class="outline-text-4" id="text-7-1-5">
<p>
<b>1. Logaritmo do produto:</b>
</p>

<pre class="example" id="orgd712546">
logₐ (b · c) = logₐ b + logₐ c
</pre>

<p>
<b>2. Logaritmo do quociente:</b>
</p>

<pre class="example" id="org37cbab0">
logₐ (b/c) = logₐ b
- logₐ c
</pre>

<p>
<b>3. Logaritmo da potência:</b>
</p>

<pre class="example" id="org3519a15">
logₐ bⁿ = n · logₐ b
</pre>

<p>
<b>4. Mudança de base:</b>
</p>

<pre class="example" id="orgd708716">
logₐ b = log_c b / log_c a
</pre>

<p>
<b>Caso particular (base 10):</b>
</p>

<pre class="example" id="org54150a6">
logₐ b = log b / log a
</pre>

<p>
<b>5. Inversão de base:</b>
</p>

<pre class="example" id="org4a1caaa">
logₐ b = 1 / log_b a
</pre>
</div>
</div>

<div id="outline-container-orgbcdafe4" class="outline-4">
<h4 id="orgbcdafe4"><span class="section-number-4">7.1.6.</span> Equações Logarítmicas</h4>
<div class="outline-text-4" id="text-7-1-6">
<ul class="org-ul">
<li>Revisão</li>
</ul>
<p>
<b>Condição de existência:</b>
</p>
<ul class="org-ul">
<li>Logaritmando &gt; 0</li>
<li>Base &gt; 0 e ≠ 1</li>
</ul>

<p>
<b>Exemplo 1:</b>
</p>

<pre class="example" id="org34680a7">
log₂ x = 5
x = 2⁵
x = 32
</pre>

<p>
<b>Exemplo 2:</b>
</p>

<pre class="example" id="orgc61f53f">
log₃ (x
- 1) = 2
x
- 1 = 3²
x
- 1 = 9
x = 10

Verificação: x
- 1 = 10
- 1 = 9 &gt; 0 ✓
</pre>

<p>
<b>Exemplo 3:</b>
</p>

<pre class="example" id="org0d1c157">
log x + log (x
- 3) = 1  (base 10)
log [x(x
- 3)] = 1
x(x
- 3) = 10¹
x²
- 3x = 10
x²
- 3x
- 10 = 0
(x
- 5)(x + 2) = 0
x = 5 ou x = -2

Verificação:
x = 5: log 5 e log 2 existem ✓
x = -2: log(-2) não existe ✗

S = {5}
</pre>

<p>
<b>Exemplo 4 (mesma base):</b>
</p>

<pre class="example" id="orgae11bc0">
log₂ x = log₂ (3x
- 4)
x = 3x
- 4
-2x = -4
x = 2

Verificação:
x = 2 &gt; 0 ✓
3x
- 4 = 2 &gt; 0 ✓

S = {2}
</pre>
</div>
</div>

<div id="outline-container-orga10d73c" class="outline-4">
<h4 id="orga10d73c"><span class="section-number-4">7.1.7.</span> Relação entre Exponencial e Logaritmo</h4>
<div class="outline-text-4" id="text-7-1-7">
<p>
<b>Funções inversas:</b>
</p>

<pre class="example" id="org4c72618">
f(x) = aˣ ⟺ f⁻¹(x) = logₐ x
</pre>

<p>
<b>Consequências:</b>
</p>

<pre class="example" id="orgdb90afa">
logₐ (aˣ) = x
a^(logₐ x) = x
</pre>

<p>
<b>Gráficos são simétricos em relação à reta y = x</b>
</p>
</div>
</div>

<div id="outline-container-org3608aba" class="outline-4">
<h4 id="org3608aba"><span class="section-number-4">7.1.8.</span> Exercícios de Revisão Integrada</h4>
<div class="outline-text-4" id="text-7-1-8">
</div>
<div id="outline-container-orge74e344" class="outline-5">
<h5 id="orge74e344"><span class="section-number-5">7.1.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-7-1-8-1">
<p>
Resolva: 3ˣ⁺¹ = 81
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org0f6535d">
3ˣ⁺¹ = 3⁴
x + 1 = 4
x = 3
</pre>

<p>
<i>[Ver resposta 88 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org2514e84" class="outline-5">
<h5 id="org2514e84"><span class="section-number-5">7.1.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-7-1-8-2">
<p>
Calcule: log₅ 125
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgd92c6ab">
log₅ 125 = log₅ 5³ = 3
</pre>

<p>
<i>[Ver resposta 89 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org733b3e0" class="outline-5">
<h5 id="org733b3e0"><span class="section-number-5">7.1.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-7-1-8-3">
<p>
Resolva: log₂ (x + 3) + log₂ (x
</p>
<ul class="org-ul">
<li>3) = 4</li>
</ul>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgc4db718">
log₂ [(x + 3)(x
- 3)] = 4
(x + 3)(x
- 3) = 2⁴
x²
- 9 = 16
x² = 25
x = ±5

Verificação:
x = 5: log₂ 8 + log₂ 2 existe ✓
x = -5: log₂ (-2) não existe ✗

S = {5}
</pre>

<p>
<i>[Ver resposta 90 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org38a477b" class="outline-5">
<h5 id="org38a477b"><span class="section-number-5">7.1.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-7-1-8-4">
<p>
Sabendo que log 2 ≈ 0,30, calcule log 8.
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org392fec8">
log 8 = log 2³ = 3 log 2
log 8 = 3 × 0,30 = 0,90
</pre>

<p>
<i>[Ver resposta 91 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org08284e2" class="outline-5">
<h5 id="org08284e2"><span class="section-number-5">7.1.8.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-7-1-8-5">
<p>
Resolva: 2²ˣ
</p>
<ul class="org-ul">
<li>3·2ˣ</li>
<li>4 = 0</li>
</ul>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org250650b">
(2ˣ)²
- 3·2ˣ
- 4 = 0

Faça 2ˣ = y:
y²
- 3y
- 4 = 0
(y
- 4)(y + 1) = 0
y = 4 ou y = -1

Se 2ˣ = 4 → 2ˣ = 2² → x = 2 ✓
Se 2ˣ = -1 → impossível (2ˣ &gt; 0 sempre) ✗

S = {2}
</pre>

<p>
<i>[Ver resposta 92 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgcf2584d" class="outline-5">
<h5 id="orgcf2584d"><span class="section-number-5">7.1.8.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-7-1-8-6">
<p>
Resolva: log₃ x + log₃ (x
</p>
<ul class="org-ul">
<li>8) = 2</li>
</ul>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org6804f8f">
log₃ [x(x
- 8)] = 2
x(x
- 8) = 3²
x²
- 8x = 9
x²
- 8x
- 9 = 0
(x
- 9)(x + 1) = 0
x = 9 ou x = -1

Verificação:
x = 9: 9 &gt; 0 e 9
- 8 = 1 &gt; 0 ✓
x = -1: -1 &lt; 0 ✗

S = {9}
</pre>

<p>
<i>[Ver resposta 93 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3ce65be" class="outline-5">
<h5 id="org3ce65be"><span class="section-number-5">7.1.8.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-7-1-8-7">
<p>
(UFMG) Se log₂ 5 = a, expresse log₂ 20 em função de a.
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org1590a9c">
log₂ 20 = log₂ (4 × 5)
log₂ 20 = log₂ 4 + log₂ 5
log₂ 20 = log₂ 2² + a
log₂ 20 = 2 + a
</pre>

<p>
<i>[Ver resposta 94 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org628163a" class="outline-5">
<h5 id="org628163a"><span class="section-number-5">7.1.8.8.</span> Exercício 8</h5>
<div class="outline-text-5" id="text-7-1-8-8">
<p>
Resolva a inequação: 2ˣ &gt; 8
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgebf5b72">
2ˣ &gt; 2³

Como base 2 &gt; 1 (função crescente):
x &gt; 3

S = {x ∈ ℝ | x &gt; 3} ou (3, +∞)
</pre>

<p>
<i>[Ver resposta 95 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org8021d08" class="outline-5">
<h5 id="org8021d08"><span class="section-number-5">7.1.8.9.</span> Exercício 9</h5>
<div class="outline-text-5" id="text-7-1-8-9">
<p>
Calcule: log₂ 3 · log₃ 4 · log₄ 8
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgab16fd5">
Usando mudança de base:
log₃ 4 = log₂ 4 / log₂ 3
log₄ 8 = log₂ 8 / log₂ 4

Substituindo:
log₂ 3 · (log₂ 4 / log₂ 3) · (log₂ 8 / log₂ 4)
= log₂ 8
= log₂ 2³
= 3
</pre>

<p>
<i>[Ver resposta 96 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf63e595" class="outline-5">
<h5 id="orgf63e595"><span class="section-number-5">7.1.8.10.</span> Exercício 10</h5>
<div class="outline-text-5" id="text-7-1-8-10">
<p>
(UFMG) Resolva: 5ˣ⁺² = 1
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org9424ac6">
5ˣ⁺² = 5⁰
x + 2 = 0
x = -2
</pre>

<p>
<i>[Ver resposta 97 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org66da235" class="outline-4">
<h4 id="org66da235"><span class="section-number-4">7.1.9.</span> Resumo de Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-7-1-9">
<pre class="example" id="orgc142ef8">
EXPONENCIAL:
aˣ · aʸ = aˣ⁺ʸ
aˣ / aʸ = aˣ⁻ʸ
(aˣ)ʸ = aˣʸ
a⁰ = 1
a¹ = a
a⁻ˣ = 1/aˣ

LOGARITMO:
logₐ b = x ⟺ aˣ = b
logₐ 1 = 0
logₐ a = 1
logₐ aˣ = x
a^(logₐ x) = x

PROPRIEDADES:
logₐ (b·c) = logₐ b + logₐ c
logₐ (b/c) = logₐ b
- logₐ c
logₐ bⁿ = n · logₐ b
logₐ b = log_c b / log_c a  (mudança de base)
logₐ b = 1 / log_b a  (inversão)

EQUAÇÕES:
Exponencial: igualar bases → igualar expoentes
Logarítmica: condições + aplicar propriedades
</pre>
</div>
</div>

<div id="outline-container-org1c833fc" class="outline-4">
<h4 id="org1c833fc"><span class="section-number-4">7.1.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-7-1-10">
<ol class="org-ol">
<li><b>Exponencial:</b> sempre tente igualar as bases</li>
<li><b>Logaritmo:</b> verifique condições de existência (logaritmando &gt; 0)</li>
<li><b>Propriedades:</b> produto vira soma, quociente vira subtração</li>
<li><b>Substituição:</b> útil em equações com 2²ˣ e 2ˣ</li>
<li><b>Mudança de base:</b> quando bases diferentes</li>
<li><b>log₁₀ = log</b> (base 10 omitida)</li>
<li><b>ln = log_e</b> (logaritmo natural)</li>
<li><b>Inequações:</b> atenção ao sentido (base &gt; 1 ou 0 &lt; base &lt; 1)</li>
</ol>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>sempre cai!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org96e1429" class="outline-3">`;

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
