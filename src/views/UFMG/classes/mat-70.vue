<script setup lang="ts">
import { ref } from "vue";

const code = "mat-70";
const title = "Matemática: Revisão Final";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-1">
<ul class="org-ul">
<li>Matemática: Revisão Final</li>
<li>Função Exponencial e Logarítmica</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-org785ebbb" class="outline-4">
<h4 id="org785ebbb"><span class="section-number-4">3.1.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-3-1-1">
<p>
Consolidar completamente exponenciais e logaritmos para a prova.
</p>
</div>
</div>

<div id="outline-container-org2226063" class="outline-4">
<h4 id="org2226063"><span class="section-number-4">3.1.2.</span> PARTE 1: Função Exponencial</h4>
<div class="outline-text-4" id="text-3-1-2">
<p>
<b>Definição:</b>
</p>

<pre class="example" id="org493f473">
f(x) = aˣ, onde a &gt; 0 e a ≠ 1
</pre>

<p>
<b>Propriedades das Potências:</b>
</p>

<pre class="example" id="org5085aaa">
a⁰ = 1
a¹ = a
aˣ · aʸ = aˣ⁺ʸ
aˣ / aʸ = aˣ⁻ʸ
(aˣ)ʸ = aˣʸ
(a·b)ˣ = aˣ · bˣ
a⁻ˣ = 1/aˣ
</pre>

<p>
<b>Gráfico e comportamento:</b>
</p>

<p>
<b>Se a &gt; 1:</b> função CRESCENTE
</p>
<ul class="org-ul">
<li>x aumenta → f(x) aumenta</li>
<li>Exemplo: f(x) = 2ˣ</li>
</ul>

<p>
<b>Se 0 &lt; a &lt; 1:</b> função DECRESCENTE
</p>
<ul class="org-ul">
<li>x aumenta → f(x) diminui</li>
<li>Exemplo: f(x) = (1/2)ˣ</li>
</ul>

<p>
<b>Características do gráfico:</b>
</p>
<ul class="org-ul">
<li>Passa sempre por (0, 1)</li>
<li>Nunca toca o eixo x (assíntota y = 0)</li>
<li>Domínio: ℝ</li>
<li>Imagem: ℝ₊* (y &gt; 0)</li>
</ul>
</div>
</div>

<div id="outline-container-org5f01ed7" class="outline-4">
<h4 id="org5f01ed7"><span class="section-number-4">3.1.3.</span> Equações Exponenciais</h4>
<div class="outline-text-4" id="text-3-1-3">
<p>
<b>Estratégia principal:</b> igualar as bases
</p>

<p>
<b>Método:</b> 1. Escrever tudo com a mesma base 2. Igualar os expoentes 3. Resolver a equação resultante
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Tipo 1: Bases iguais diretas</b>
</p>

<pre class="example" id="org8edd235">
2ˣ = 32
2ˣ = 2⁵
x = 5
</pre>

<p>
<b>Tipo 2: Redução à mesma base</b>
</p>

<pre class="example" id="orgedbb2e4">
4ˣ = 64
(2²)ˣ = 2⁶
2²ˣ = 2⁶
2x = 6
x = 3
</pre>

<p>
<b>Tipo 3: Bases diferentes</b>
</p>

<pre class="example" id="org708e007">
9ˣ⁺¹ = 27ˣ
(3²)ˣ⁺¹ = (3³)ˣ
3²⁽ˣ⁺¹⁾ = 3³ˣ
2(x+1) = 3x
2x + 2 = 3x
x = 2
</pre>

<p>
<b>Tipo 4: Substituição</b>
</p>

<pre class="example" id="org73e8bf4">
4ˣ
- 5·2ˣ + 4 = 0
(2²)ˣ
- 5·2ˣ + 4 = 0
(2ˣ)²
- 5·2ˣ + 4 = 0

Faça y = 2ˣ:
y²
- 5y + 4 = 0
(y-4)(y-1) = 0
y = 4 ou y = 1

Se 2ˣ = 4 → x = 2
Se 2ˣ = 1 → x = 0

S = {0, 2}
</pre>
</div>
</div>

<div id="outline-container-org0f3d56b" class="outline-4">
<h4 id="org0f3d56b"><span class="section-number-4">3.1.4.</span> PARTE 2: Logaritmo</h4>
<div class="outline-text-4" id="text-3-1-4">
<p>
<b>Definição:</b>
</p>

<pre class="example" id="org09d00c5">
logₐ b = x ⟺ aˣ = b

Onde:
a &gt; 0, a ≠ 1 (base)
b &gt; 0 (logaritmando)
x ∈ ℝ (logaritmo)
</pre>

<p>
<b>Significado:</b> “A que expoente devo elevar a base a para obter b?”
</p>

<p>
<b>Casos especiais:</b>
</p>

<pre class="example" id="org0c6d3b0">
logₐ 1 = 0 (sempre!)
logₐ a = 1 (sempre!)
logₐ aˣ = x
a^(logₐ x) = x
</pre>

<p>
<b>Exemplos básicos:</b>
</p>

<pre class="example" id="org7da4ece">
log₂ 8 = 3 (pois 2³ = 8)
log₁₀ 100 = 2 (pois 10² = 100)
log₅ 1 = 0 (pois 5⁰ = 1)
log₃ 3 = 1 (pois 3¹ = 3)
log₂ ¼ = -2 (pois 2⁻² = ¼)
</pre>
</div>
</div>

<div id="outline-container-orgf56625c" class="outline-4">
<h4 id="orgf56625c"><span class="section-number-4">3.1.5.</span> Propriedades dos Logaritmos</h4>
<div class="outline-text-4" id="text-3-1-5">
<p>
<b>1. Produto:</b>
</p>

<pre class="example" id="org65f4a81">
logₐ (b · c) = logₐ b + logₐ c
</pre>

<p>
<b>2. Quociente:</b>
</p>

<pre class="example" id="org87526a3">
logₐ (b/c) = logₐ b
- logₐ c
</pre>

<p>
<b>3. Potência:</b>
</p>

<pre class="example" id="orgfdf2791">
logₐ bⁿ = n · logₐ b
</pre>

<p>
<b>4. Mudança de base:</b>
</p>

<pre class="example" id="org63ca800">
logₐ b = log_c b / log_c a

Caso particular (base 10):
logₐ b = log b / log a
</pre>

<p>
<b>5. Inversão de base:</b>
</p>

<pre class="example" id="orgebd620b">
logₐ b · log_b a = 1
logₐ b = 1 / log_b a
</pre>

<p>
<b>Exemplos de aplicação:</b>
</p>

<p>
<b>Exemplo 1:</b>
</p>

<pre class="example" id="org5d268f6">
log₂ 8 + log₂ 4 = log₂ (8·4) = log₂ 32 = log₂ 2⁵ = 5
</pre>

<p>
<b>Exemplo 2:</b>
</p>

<pre class="example" id="orgef2220a">
log 100
- log 10 = log (100/10) = log 10 = 1
</pre>

<p>
<b>Exemplo 3:</b>
</p>

<pre class="example" id="org57a6ce0">
log₅ 125 = log₅ 5³ = 3 · log₅ 5 = 3 · 1 = 3
</pre>

<p>
<b>Exemplo 4: Mudança de base:</b>
</p>

<pre class="example" id="org8765f72">
log₂ 10 = log 10 / log 2 = 1 / log 2 ≈ 1 / 0,301 ≈ 3,32
</pre>
</div>
</div>

<div id="outline-container-org370b412" class="outline-4">
<h4 id="org370b412"><span class="section-number-4">3.1.6.</span> Equações Logarítmicas</h4>
<div class="outline-text-4" id="text-3-1-6">
<p>
<b>Estratégia:</b> 1. Usar propriedades para simplificar 2. Aplicar definição de logaritmo 3. Verificar condição de existência (logaritmando &gt; 0)
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Tipo 1: Direto</b>
</p>

<pre class="example" id="orge24348f">
log₂ x = 5
x = 2⁵
x = 32

Verificação: x &gt; 0 ✓
</pre>

<p>
<b>Tipo 2: Usar propriedades</b>
</p>

<pre class="example" id="orgc1e6b52">
log x + log (x-3) = 1  (base 10)
log [x(x-3)] = 1
x(x-3) = 10¹
x²
- 3x = 10
x²
- 3x
- 10 = 0
(x-5)(x+2) = 0

x = 5 ou x = -2

Verificar condições:
x &gt; 0 e x-3 &gt; 0 → x &gt; 3

Solução: x = 5 ✓
(x = -2 não serve)
</pre>

<p>
<b>Tipo 3: Mesma base</b>
</p>

<pre class="example" id="org9f2c834">
log₂ (x+1) = log₂ (2x-3)

x + 1 = 2x
- 3
4 = x
x = 4

Verificar: x+1 &gt; 0 e 2x-3 &gt; 0
4+1 = 5 &gt; 0 ✓
2(4)-3 = 5 &gt; 0 ✓

Solução: x = 4
</pre>
</div>
</div>

<div id="outline-container-orgdf8aa2e" class="outline-4">
<h4 id="orgdf8aa2e"><span class="section-number-4">3.1.7.</span> Inequações</h4>
<div class="outline-text-4" id="text-3-1-7">
<p>
<b>Exponencial:</b>
</p>

<pre class="example" id="org12d7504">
Se a &gt; 1: aˣ &gt; aʸ ⟺ x &gt; y
Se 0 &lt; a &lt; 1: aˣ &gt; aʸ ⟺ x &lt; y (inverte!)
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org012ef55">
2ˣ &gt; 8
2ˣ &gt; 2³
x &gt; 3 (pois base 2 &gt; 1)
</pre>

<p>
<b>Logarítmica:</b>
</p>

<pre class="example" id="orge0db205">
Se a &gt; 1: logₐ x &gt; logₐ y ⟺ x &gt; y
Se 0 &lt; a &lt; 1: logₐ x &gt; logₐ y ⟺ x &lt; y (inverte!)
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orge0d576c">
log₂ x &gt; 3
x &gt; 2³
x &gt; 8
</pre>
</div>
</div>

<div id="outline-container-orge300fce" class="outline-4">
<h4 id="orge300fce"><span class="section-number-4">3.1.8.</span> Função Logarítmica</h4>
<div class="outline-text-4" id="text-3-1-8">
<p>
<b>Definição:</b>
</p>

<pre class="example" id="orga1c7730">
f(x) = logₐ x
</pre>

<p>
<b>Características:</b>
</p>

<p>
<b>Se a &gt; 1:</b> CRESCENTE
</p>
<ul class="org-ul">
<li>Passa por (1, 0)</li>
<li>Domínio: x &gt; 0</li>
<li>Imagem: ℝ</li>
</ul>

<p>
<b>Se 0 &lt; a &lt; 1:</b> DECRESCENTE
</p>
<ul class="org-ul">
<li>Passa por (1, 0)</li>
<li>Domínio: x &gt; 0</li>
<li>Imagem: ℝ</li>
</ul>

<p>
<b>Relação com exponencial:</b>
</p>

<pre class="example" id="orgb3c6d9a">
f(x) = aˣ e g(x) = logₐ x são INVERSAS

Reflexão pela reta y = x
</pre>
</div>
</div>

<div id="outline-container-org59adcd7" class="outline-4">
<h4 id="org59adcd7"><span class="section-number-4">3.1.9.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-3-1-9">
</div>
<div id="outline-container-org36932e9" class="outline-5">
<h5 id="org36932e9"><span class="section-number-5">3.1.9.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-3-1-9-1">
<p>
Calcule: a) 2⁵ b) 2⁻³ c) (1/2)²
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orge777b21">
a) 32
b) 1/8
c) 1/4
</pre>
</div>
</div>

<div id="outline-container-org9aa34b2" class="outline-5">
<h5 id="org9aa34b2"><span class="section-number-5">3.1.9.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-3-1-9-2">
<p>
Resolva: 3ˣ = 81
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orge542204">
3ˣ = 3⁴
x = 4
</pre>
</div>
</div>

<div id="outline-container-orge7f4b7f" class="outline-5">
<h5 id="orge7f4b7f"><span class="section-number-5">3.1.9.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-3-1-9-3">
<p>
Resolva: 4ˣ⁺¹ = 8ˣ
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgaae5cfe">
(2²)ˣ⁺¹ = (2³)ˣ
2²⁽ˣ⁺¹⁾ = 2³ˣ
2(x+1) = 3x
2x + 2 = 3x
x = 2
</pre>
</div>
</div>

<div id="outline-container-org92bad85" class="outline-5">
<h5 id="org92bad85"><span class="section-number-5">3.1.9.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-3-1-9-4">
<p>
Calcule: a) log₂ 16 b) log₁₀ 1000 c) log₅ 1
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org789fa01">
a) log₂ 16 = log₂ 2⁴ = 4
b) log₁₀ 1000 = log₁₀ 10³ = 3
c) log₅ 1 = 0
</pre>
</div>
</div>

<div id="outline-container-org38f9b99" class="outline-5">
<h5 id="org38f9b99"><span class="section-number-5">3.1.9.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-3-1-9-5">
<p>
Calcule: log₂ 8 + log₂ 4
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgd79cae9">
log₂ (8·4) = log₂ 32 = log₂ 2⁵ = 5

Ou:
log₂ 8 + log₂ 4 = 3 + 2 = 5
</pre>
</div>
</div>

<div id="outline-container-org3f55f43" class="outline-5">
<h5 id="org3f55f43"><span class="section-number-5">3.1.9.6.</span> Questão 6</h5>
<div class="outline-text-5" id="text-3-1-9-6">
<p>
Resolva: log x = 2 (base 10)
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org1b7a58b">
x = 10² = 100
</pre>
</div>
</div>

<div id="outline-container-orgf73fdd3" class="outline-5">
<h5 id="orgf73fdd3"><span class="section-number-5">3.1.9.7.</span> Questão 7</h5>
<div class="outline-text-5" id="text-3-1-9-7">
<p>
Resolva: log₃ (x+2) = 2
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgc81a8f3">
x + 2 = 3²
x + 2 = 9
x = 7
</pre>
</div>
</div>
</div>

<div id="outline-container-org11f4d44" class="outline-4">
<h4 id="org11f4d44"><span class="section-number-4">3.1.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-1-10">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<pre class="example" id="org45b0124">
EXPONENCIAL:
f(x) = aˣ

Propriedades:
a⁰ = 1
aˣ · aʸ = aˣ⁺ʸ
aˣ / aʸ = aˣ⁻ʸ
(aˣ)ʸ = aˣʸ
a⁻ˣ = 1/aˣ

Crescimento:
a &gt; 1: crescente
0 &lt; a &lt; 1: decrescente

LOGARITMO:
logₐ b = x ⟺ aˣ = b

Casos especiais:
logₐ 1 = 0
logₐ a = 1
logₐ aˣ = x

Propriedades:
logₐ (bc) = logₐ b + logₐ c
logₐ (b/c) = logₐ b
- logₐ c
logₐ bⁿ = n · logₐ b

Mudança de base:
logₐ b = log b / log a

Função logarítmica:
f(x) = logₐ x
Domínio: x &gt; 0
Imagem: ℝ
</pre>
</div>
</div>

<div id="outline-container-org2ba70ce" class="outline-4">
<h4 id="org2ba70ce"><span class="section-number-4">3.1.11.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-3-1-11">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei todas as propriedades de potências</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver equações exponenciais por redução de base</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver equações exponenciais por substituição</li>
<li class="off"><code>[&#xa0;]</code> Sei a definição de logaritmo</li>
<li class="off"><code>[&#xa0;]</code> Sei os casos especiais (logₐ 1 = 0, logₐ a = 1)</li>
<li class="off"><code>[&#xa0;]</code> Sei todas as propriedades dos logaritmos</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar mudança de base</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver equações logarítmicas</li>
<li class="off"><code>[&#xa0;]</code> Sei verificar condições de existência</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver inequações exponenciais e logarítmicas</li>
<li class="off"><code>[&#xa0;]</code> Sei esboçar gráficos de exponencial e logaritmo</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio-Alto (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org7c3d9e2" class="outline-3">`;

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
