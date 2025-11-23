<script setup lang="ts">
import { ref } from "vue";

const code = "mat-38";
const title = "Matemática: Função Logarítmica";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-1">
<ul class="org-ul">
<li>Matemática: Função Logarítmica</li>
<li>Parte 1 (Definição e Logaritmo Decimal/Natural)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgdaf6775" class="outline-4">
<h4 id="orgdaf6775"><span class="section-number-4">6.1.1.</span> Introdução: O Problema Inverso</h4>
<div class="outline-text-4" id="text-6-1-1">
<p>
<b>Problema:</b> Resolver 2^x = 8 é fácil (x = 3).
</p>

<p>
<b>Mas e 2^x = 5?</b> Não conseguimos escrever 5 como potência de 2!
</p>

<p>
<b>Solução:</b> Usar <b>logaritmos</b>.
</p>
</div>
</div>

<div id="outline-container-org873b005" class="outline-4">
<h4 id="org873b005"><span class="section-number-4">6.1.2.</span> Definição de Logaritmo</h4>
<div class="outline-text-4" id="text-6-1-2">
<p>
<b>Logaritmo</b> é o expoente ao qual devemos elevar a base para obter um número.
</p>

<p>
<b>Definição formal:</b>
</p>

<pre class="example" id="org62df6e1">
log_a b = x  ⟺  a^x = b
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li><b>a:</b> base (a &gt; 0, a ≠ 1)</li>
<li><b>b:</b> logaritmando (b &gt; 0)</li>
<li><b>x:</b> logaritmo</li>
</ul>

<p>
<b>Lê-se:</b> “Logaritmo de b na base a é igual a x”
</p>

<p>
<b>Significado:</b> “a elevado a x é igual a b”
</p>
</div>
</div>

<div id="outline-container-org3b92f96" class="outline-4">
<h4 id="org3b92f96"><span class="section-number-4">6.1.3.</span> Exemplos Básicos</h4>
<div class="outline-text-4" id="text-6-1-3">
<p>
<b>Exemplo 1:</b> log₂ 8 = ?
</p>

<p>
“2 elevado a quanto dá 8?” 2³ = 8 <b>log₂ 8 = 3</b>
</p>

<p>
<b>Exemplo 2:</b> log₅ 125 = ?
</p>

<p>
5³ = 125 <b>log₅ 125 = 3</b>
</p>

<p>
<b>Exemplo 3:</b> log₁₀ 100 = ?
</p>

<p>
10² = 100 <b>log₁₀ 100 = 2</b>
</p>

<p>
<b>Exemplo 4:</b> log₃ (1/9) = ?
</p>

<p>
3^x = 1/9 = 1/3² = 3⁻² <b>log₃ (1/9) = -2</b>
</p>

<p>
<b>Exemplo 5:</b> log₄ 2 = ?
</p>

<p>
4^x = 2 (2²)^x = 2 2^(2x) = 2¹ 2x = 1 <b>log₄ 2 = 1/2</b>
</p>
</div>
</div>

<div id="outline-container-orgc81482a" class="outline-4">
<h4 id="orgc81482a"><span class="section-number-4">6.1.4.</span> Casos Especiais</h4>
<div class="outline-text-4" id="text-6-1-4">
</div>
<div id="outline-container-orgc2d0b90" class="outline-5">
<h5 id="orgc2d0b90"><span class="section-number-5">6.1.4.1.</span> 1. Logaritmo de 1</h5>
<div class="outline-text-5" id="text-6-1-4-1">
<pre class="example" id="orgfbcdd40">
log_a 1 = 0  (para qualquer a)
</pre>

<p>
<b>Por quê?</b> a⁰ = 1
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log₅ 1 = 0</li>
<li>log₁₀ 1 = 0</li>
</ul>
</div>
</div>

<div id="outline-container-orgb5deba3" class="outline-5">
<h5 id="orgb5deba3"><span class="section-number-5">6.1.4.2.</span> 2. Logaritmo da Base</h5>
<div class="outline-text-5" id="text-6-1-4-2">
<pre class="example" id="org84dc706">
log_a a = 1  (para qualquer a)
</pre>

<p>
<b>Por quê?</b> a¹ = a
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log₇ 7 = 1</li>
<li>log₁₀ 10 = 1</li>
</ul>
</div>
</div>

<div id="outline-container-org56a0011" class="outline-5">
<h5 id="org56a0011"><span class="section-number-5">6.1.4.3.</span> 3. Potência da Base</h5>
<div class="outline-text-5" id="text-6-1-4-3">
<pre class="example" id="org38886c2">
log_a (a^n) = n
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log₂ (2⁵) = 5</li>
<li>log₃ (3⁻²) = -2</li>
</ul>
</div>
</div>

<div id="outline-container-org9187fdd" class="outline-5">
<h5 id="org9187fdd"><span class="section-number-5">6.1.4.4.</span> 4. Base Elevada ao Logaritmo</h5>
<div class="outline-text-5" id="text-6-1-4-4">
<pre class="example" id="orgb2b9b3a">
a^(log_a b) = b
</pre>

<p>
<b>Exemplo:</b> 2^(log₂ 5) = 5
</p>
</div>
</div>
</div>

<div id="outline-container-org57fe0bf" class="outline-4">
<h4 id="org57fe0bf"><span class="section-number-4">6.1.5.</span> Condições de Existência</h4>
<div class="outline-text-4" id="text-6-1-5">
<p>
<b>Para log_a b existir:</b>
</p>

<ol class="org-ol">
<li><b>a &gt; 0 e a ≠ 1</b> (base positiva e diferente de 1)</li>
<li><b>b &gt; 0</b> (logaritmando positivo)</li>
</ol>

<p>
<b>Consequências:</b>
</p>
<ul class="org-ul">
<li>log₂ (-4): NÃO existe (logaritmando negativo)</li>
<li>log₁ 5: NÃO existe (base = 1)</li>
<li>log₋₂ 8: NÃO existe (base negativa)</li>
<li>log₂ 0: NÃO existe (logaritmando = 0)</li>
</ul>
</div>
</div>

<div id="outline-container-org2deda3f" class="outline-4">
<h4 id="org2deda3f"><span class="section-number-4">6.1.6.</span> Logaritmo Decimal (Base 10)</h4>
<div class="outline-text-4" id="text-6-1-6">
<p>
<b>Logaritmo decimal:</b> log₁₀ b
</p>

<p>
<b>Notação simplificada:</b>
</p>

<pre class="example" id="org1421839">
log b = log₁₀ b
</pre>

<p>
Quando a base não aparece, é base 10!
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>log 100 = log₁₀ 100 = 2 (pois 10² = 100)</li>
<li>log 1000 = 3 (pois 10³ = 1000)</li>
<li>log 0,01 = -2 (pois 10⁻² = 0,01)</li>
</ul>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Escala Richter (terremotos)</li>
<li>pH (acidez)</li>
<li>Decibéis (som)</li>
<li>Ordens de grandeza</li>
</ul>
</div>
</div>

<div id="outline-container-org74572bd" class="outline-4">
<h4 id="org74572bd"><span class="section-number-4">6.1.7.</span> Logaritmo Natural (Base e)</h4>
<div class="outline-text-4" id="text-6-1-7">
<p>
<b>Número de Euler:</b>
</p>

<pre class="example" id="org157b65c">
e ≈ 2,718281828...
</pre>

<p>
<b>Logaritmo natural:</b> log_e b
</p>

<p>
<b>Notação:</b>
</p>

<pre class="example" id="org58f1852">
ln b = log_e b
</pre>

<p>
<b>Lê-se:</b> “ene de b” ou “logaritmo natural de b”
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>ln e = 1 (pois e¹ = e)</li>
<li>ln e² = 2</li>
<li>ln 1 = 0</li>
</ul>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Crescimento populacional</li>
<li>Juros compostos contínuos</li>
<li>Decaimento radioativo</li>
<li>Cálculo (derivadas, integrais)</li>
</ul>

<p>
<b>Por que “natural”?</b> Aparece naturalmente em problemas de crescimento/decaimento contínuo.
</p>
</div>
</div>

<div id="outline-container-org45001d6" class="outline-4">
<h4 id="org45001d6"><span class="section-number-4">6.1.8.</span> Relação entre Logaritmo e Exponencial</h4>
<div class="outline-text-4" id="text-6-1-8">
<p>
<b>Funções inversas:</b>
</p>

<p>
Se f(x) = a^x (exponencial) Então f⁻¹(x) = log_a x (logarítmica)
</p>

<p>
<b>Propriedade fundamental:</b>
</p>

<pre class="example" id="org86f793f">
y = a^x  ⟺  x = log_a y
</pre>

<p>
<b>Consequências:</b>
</p>
<ul class="org-ul">
<li>log_a (a^x) = x</li>
<li>a^(log_a x) = x</li>
</ul>
</div>
</div>

<div id="outline-container-orga6fb559" class="outline-4">
<h4 id="orga6fb559"><span class="section-number-4">6.1.9.</span> Gráfico da Função Logarítmica (Introdução)</h4>
<div class="outline-text-4" id="text-6-1-9">
<p>
<b>Função:</b> f(x) = log_a x
</p>
</div>

<div id="outline-container-org92860ac" class="outline-5">
<h5 id="org92860ac"><span class="section-number-5">6.1.9.1.</span> Caso 1: a &gt; 1</h5>
<div class="outline-text-5" id="text-6-1-9-1">
<p>
<b>Exemplo:</b> f(x) = log₂ x
</p>

<pre class="example" id="orgd0a71d9">
x    | 1/4 | 1/2 | 1  | 2  | 4  | 8
log₂x| -2  | -1  | 0  | 1  | 2  | 3
</pre>

<p>
<b>Gráfico:</b>
</p>

<pre class="example" id="org7f2096e">
   |
 3 |           •
 2 |       •
 1 |   • 
 0 |─•─────────
-1 | •
-2 |•
   |____________
     1  2  4  8
</pre>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Crescente</b></li>
<li>Passa por (1, 0)</li>
<li>Eixo y é assíntota vertical</li>
<li>Domínio: x &gt; 0</li>
<li>Imagem: ℝ</li>
</ul>
</div>
</div>

<div id="outline-container-org4526582" class="outline-5">
<h5 id="org4526582"><span class="section-number-5">6.1.9.2.</span> Caso 2: 0 &lt; a &lt; 1</h5>
<div class="outline-text-5" id="text-6-1-9-2">
<p>
<b>Exemplo:</b> f(x) = log_(1/2) x
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Decrescente</b></li>
<li>Passa por (1, 0)</li>
<li>Eixo y é assíntota</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgcfb3f8b" class="outline-4">
<h4 id="orgcfb3f8b"><span class="section-number-4">6.1.10.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-6-1-10">
</div>
<div id="outline-container-orgcb1a7ee" class="outline-5">
<h5 id="orgcb1a7ee"><span class="section-number-5">6.1.10.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-6-1-10-1">
<p>
Calcule: a) log₅ 25 b) log₃ 27 c) log₁₀ 0,001
</p>

<p>
<b>Soluções:</b>
</p>

<ol class="org-ol">
<li>5^x = 25 = 5² → <b>x = 2</b></li>

<li>3^x = 27 = 3³ → <b>x = 3</b></li>

<li>10^x = 0,001 = 1/1000 = 10⁻³ → <b>x = -3</b></li>
</ol>
</div>
</div>

<div id="outline-container-orgbae021d" class="outline-5">
<h5 id="orgbae021d"><span class="section-number-5">6.1.10.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-6-1-10-2">
<p>
Determine o valor de log₄ 8.
</p>

<p>
<b>Solução:</b>
</p>

<p>
4^x = 8 (2²)^x = 2³ 2^(2x) = 2³ 2x = 3 <b>x = 3/2</b>
</p>
</div>
</div>

<div id="outline-container-org986c659" class="outline-5">
<h5 id="org986c659"><span class="section-number-5">6.1.10.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-6-1-10-3">
<p>
Calcule: log₇ 1 + log₇ 7 + log₇ 49
</p>

<p>
<b>Solução:</b>
</p>

<p>
log₇ 1 = 0 log₇ 7 = 1 log₇ 49 = log₇ (7²) = 2
</p>

<p>
Soma: 0 + 1 + 2 = <b>3</b>
</p>
</div>
</div>

<div id="outline-container-orgcd2be9a" class="outline-5">
<h5 id="orgcd2be9a"><span class="section-number-5">6.1.10.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-6-1-10-4">
<p>
Para quais valores de x existe log₂ (x
</p>
<ul class="org-ul">
<li>3)?</li>
</ul>

<p>
<b>Solução:</b>
</p>

<p>
<b>Condição:</b> logaritmando &gt; 0
</p>

<p>
x
</p>
<ul class="org-ul">
<li>3 &gt; 0 <b>x &gt; 3</b></li>
</ul>
</div>
</div>

<div id="outline-container-orgb9535b2" class="outline-5">
<h5 id="orgb9535b2"><span class="section-number-5">6.1.10.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-6-1-10-5">
<p>
Simplifique: 3^(log₃ 10)
</p>

<p>
<b>Solução:</b>
</p>

<p>
Propriedade: a^(log_a b) = b
</p>

<p>
<b>3^(log₃ 10) = 10</b>
</p>
</div>
</div>
</div>

<div id="outline-container-orgfe180be" class="outline-4">
<h4 id="orgfe180be"><span class="section-number-4">6.1.11.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-6-1-11">
<ol class="org-ol">
<li><b>log_a b = x ⟺ a^x = b</b> (definição!)</li>
<li><b>log_a 1 = 0</b> (sempre)</li>
<li><b>log_a a = 1</b> (sempre)</li>
<li><b>log_a (a^n) = n</b></li>
<li><b>a^(log_a b) = b</b></li>
<li><b>log b = log₁₀ b</b> (base 10)</li>
<li><b>ln b = log_e b</b> (base e)</li>
<li><b>Condições:</b> a &gt; 0, a ≠ 1, b &gt; 0</li>
</ol>
</div>
</div>

<div id="outline-container-org4a1e0c9" class="outline-4">
<h4 id="org4a1e0c9"><span class="section-number-4">6.1.12.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-6-1-12">
<p>
<b>Definição:</b>
</p>
<ul class="org-ul">
<li>log_a b = x ⟺ a^x = b</li>
<li>a: base</li>
<li>b: logaritmando</li>
<li>x: logaritmo</li>
</ul>

<p>
<b>Casos Especiais:</b>
</p>
<ul class="org-ul">
<li>log_a 1 = 0</li>
<li>log_a a = 1</li>
<li>log_a (a^n) = n</li>
<li>a^(log_a b) = b</li>
</ul>

<p>
<b>Bases Especiais:</b>
</p>
<ul class="org-ul">
<li>log b = log₁₀ b (decimal)</li>
<li>ln b = log_e b (natural)</li>
</ul>

<p>
<b>Condições:</b>
</p>
<ul class="org-ul">
<li>a &gt; 0, a ≠ 1</li>
<li>b &gt; 0</li>
</ul>
</div>
</div>

<div id="outline-container-orgce8a704" class="outline-4">
<h4 id="orgce8a704"><span class="section-number-4">6.1.13.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-6-1-13">
<pre class="example" id="org05c1f88">
Definição:
log_a b = x  ⟺  a^x = b

Casos Especiais:
log_a 1 = 0
log_a a = 1
log_a (a^n) = n
a^(log_a b) = b

Logaritmos Especiais:
log b = log₁₀ b  (decimal)
ln b = log_e b   (natural, e ≈ 2,718)

Condições de Existência:
a &gt; 0, a ≠ 1
b &gt; 0
</pre>
</div>
</div>

<div id="outline-container-org088d220" class="outline-4">
<h4 id="org088d220"><span class="section-number-4">6.1.14.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-6-1-14">
<pre class="example" id="org857eaeb">
DEFINIÇÃO:

log_a b = x
     ↓
   a^x = b
   
"a elevado a x dá b"

EXEMPLOS:
log₂ 8 = 3  porque  2³ = 8
log₁₀ 100 = 2  porque  10² = 100

GRÁFICO (a &gt; 1):
    |
  2 |       •
  1 |   •
  0 |─•──────
 -1 | •
    |____________
      1  2  4

- Crescente (a &gt; 1)
- Passa por (1,0)
- Assíntota: x = 0
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>logaritmos são fundamentais!)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orga13b9da" class="outline-3">`;

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
