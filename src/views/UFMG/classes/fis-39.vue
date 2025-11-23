<script setup lang="ts">
import { ref } from "vue";

const code = "fis-39";
const title = "Física: Plano Inclinado";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-2">
<ul class="org-ul">
<li>Física: Plano Inclinado</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-org360dec9" class="outline-4">
<h4 id="org360dec9"><span class="section-number-4">6.2.1.</span> Introdução</h4>
<div class="outline-text-4" id="text-6-2-1">
<p>
<b>Plano inclinado:</b> superfície plana formando ângulo θ com a horizontal.
</p>

<p>
<b>Exemplos:</b> rampas, ladeiras, escorregadores
</p>

<p>
<b>Importância:</b> Combina conceitos de forças, decomposição vetorial, atrito.
</p>
</div>
</div>

<div id="outline-container-orgc4eae48" class="outline-4">
<h4 id="orgc4eae48"><span class="section-number-4">6.2.2.</span> Forças no Plano Inclinado</h4>
<div class="outline-text-4" id="text-6-2-2">
<pre class="example" id="orgc8f3ed9">
        N ↑ (normal)
       /|
      / |
   [m]  |
    / | \\
   /  |  \\ F_at (atrito, se houver)
  /   |   \\
 /    ↓    \\
/     P     \\ θ
──────────────
</pre>

<p>
<b>Forças atuantes:</b> 1. <b>Peso (P):</b> vertical, para baixo (P = mg) 2. <b>Normal (N):</b> perpendicular ao plano 3. <b>Atrito (F_at):</b> paralelo ao plano, opõe movimento
</p>
</div>
</div>

<div id="outline-container-orga6d46af" class="outline-4">
<h4 id="orga6d46af"><span class="section-number-4">6.2.3.</span> Decomposição do Peso</h4>
<div class="outline-text-4" id="text-6-2-3">
<p>
Como o peso é vertical mas o plano é inclinado, decompomos P:
</p>

<p>
<b>Componentes do peso:</b>
</p>

<pre class="example" id="org411b3a6">
P_x = P sen(θ) = mg sen(θ)  (paralela ao plano, "desce")
P_y = P cos(θ) = mg cos(θ)  (perpendicular ao plano)
</pre>

<p>
<b>Diagrama:</b>
</p>

<pre class="example" id="org3213323">
  P_y
   ↑
   |
   |___P_x →
  /θ
 /
/ P
</pre>

<p>
<b>Memorização:</b>
</p>
<ul class="org-ul">
<li><b>P_x (paralela):</b> sen(θ)</li>
<li>“sobe” com θ</li>
<li><b>P_y (perpendicular):</b> cos(θ)</li>
<li>“desce” com θ</li>
</ul>
</div>
</div>

<div id="outline-container-org7509e2d" class="outline-4">
<h4 id="org7509e2d"><span class="section-number-4">6.2.4.</span> Força Normal no Plano Inclinado</h4>
<div class="outline-text-4" id="text-6-2-4">
<p>
<b>Equilíbrio perpendicular ao plano:</b>
</p>

<p>
Não há movimento perpendicular → ΣF_perp = 0
</p>

<p>
*N
</p>
<ul class="org-ul">
<li>P_y = 0*</li>
</ul>

<pre class="example" id="org66d2b47">
N = P_y = P cos(θ) = mg cos(θ)
</pre>

<p>
<b>Importante:</b> N ≠ P (diferente da superfície horizontal!)
</p>

<p>
<b>Observação:</b> Quanto maior θ, menor N.
</p>
</div>
</div>

<div id="outline-container-org8b726e9" class="outline-4">
<h4 id="org8b726e9"><span class="section-number-4">6.2.5.</span> Casos de Movimento</h4>
<div class="outline-text-4" id="text-6-2-5">
</div>
<div id="outline-container-orgfb081f2" class="outline-5">
<h5 id="orgfb081f2"><span class="section-number-5">6.2.5.1.</span> Caso 1: Plano Inclinado SEM Atrito</h5>
<div class="outline-text-5" id="text-6-2-5-1">
<p>
<b>Forças paralelas ao plano:</b>
</p>
<ul class="org-ul">
<li>P_x (desce)</li>
</ul>

<p>
<b>2ª Lei de Newton (paralelo ao plano):</b>
</p>

<pre class="example" id="org40fd18a">
F_R = ma
P_x = ma
mg sen(θ) = ma
a = g sen(θ)
</pre>

<p>
<b>Aceleração:</b>
</p>

<pre class="example" id="org5d0780b">
a = g sen(θ)  (descendo o plano)
</pre>

<p>
<b>Observações:</b>
</p>
<ul class="org-ul">
<li>Aceleração independe da massa!</li>
<li>θ = 0°: a = 0 (horizontal)</li>
<li>θ = 90°: a = g (queda livre)</li>
</ul>
</div>
</div>

<div id="outline-container-org0b83fdd" class="outline-5">
<h5 id="org0b83fdd"><span class="section-number-5">6.2.5.2.</span> Caso 2: Plano Inclinado COM Atrito</h5>
<div class="outline-text-5" id="text-6-2-5-2">
<p>
<b>Forças paralelas:</b>
</p>
<ul class="org-ul">
<li>P_x (desce)</li>
<li>F_at (sobe, opõe movimento)</li>
</ul>

<p>
<b>Atrito:</b> F_at = μN = μ mg cos(θ)
</p>

<p>
<b>2ª Lei (descendo):</b>
</p>

<pre class="example" id="org4ea3af1">
mg sen(θ)
- μ mg cos(θ) = ma
a = g(sen(θ)
- μ cos(θ))
</pre>

<p>
<b>Condição para descer:</b> sen(θ) &gt; μ cos(θ) <b>tan(θ) &gt; μ</b>
</p>

<p>
Se tan(θ) ≤ μ: corpo não desce (atrito segura)
</p>
</div>
</div>

<div id="outline-container-org9c2d46b" class="outline-5">
<h5 id="org9c2d46b"><span class="section-number-5">6.2.5.3.</span> Caso 3: Corpo Empurrado Plano Acima</h5>
<div class="outline-text-5" id="text-6-2-5-3">
<p>
<b>Força aplicada F (paralela ao plano, subindo):</b>
</p>

<p>
<b>Subindo:</b>
</p>

<pre class="example" id="orga1cd1d2">
F
- P_x
- F_at = ma
F
- mg sen(θ)
- μ mg cos(θ) = ma
</pre>
</div>
</div>
</div>

<div id="outline-container-orgcc31d22" class="outline-4">
<h4 id="orgcc31d22"><span class="section-number-4">6.2.6.</span> Aplicações</h4>
<div class="outline-text-4" id="text-6-2-6">
</div>
<div id="outline-container-org8582987" class="outline-5">
<h5 id="org8582987"><span class="section-number-5">6.2.6.1.</span> Problema 1</h5>
<div class="outline-text-5" id="text-6-2-6-1">
<p>
Bloco de 10 kg em plano inclinado de 30°, sem atrito. Qual a aceleração? (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
a = g sen(30°) = 10 × 0,5 = 5 m/s²
</p>

<p>
<i>[Ver resposta 32 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org0a71cf1" class="outline-5">
<h5 id="org0a71cf1"><span class="section-number-5">6.2.6.2.</span> Problema 2</h5>
<div class="outline-text-5" id="text-6-2-6-2">
<p>
Mesmo bloco, mesma inclinação, μ = 0,2. Qual a aceleração?
</p>

<p>
<b>Solução:</b>
</p>

<p>
a = g(sen(θ)
</p>
<ul class="org-ul">
<li>μ cos(θ)) a = 10(sen(30°)</li>
<li>0,2 × cos(30°)) a = 10(0,5</li>
<li>0,2 × 0,87) a = 10(0,5</li>
<li>0,174) a = 10 × 0,326 a ≈ 3,26 m/s²</li>
</ul>

<p>
<i>[Ver resposta 33 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org51f62b3" class="outline-5">
<h5 id="org51f62b3"><span class="section-number-5">6.2.6.3.</span> Problema 3</h5>
<div class="outline-text-5" id="text-6-2-6-3">
<p>
Determine a normal de um bloco de 5 kg em plano de 60°. (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
N = mg cos(60°) = 5 × 10 × 0,5 = 25 N
</p>

<p>
<i>[Ver resposta 34 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org3e0a5eb" class="outline-4">
<h4 id="org3e0a5eb"><span class="section-number-4">6.2.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-6-2-7">
</div>
<div id="outline-container-org143d0bc" class="outline-5">
<h5 id="org143d0bc"><span class="section-number-5">6.2.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-6-2-7-1">
<p>
Em um plano inclinado de 45° sem atrito, um corpo de 2 kg tem qual aceleração? (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
a = g sen(45°) = 10 × (√2/2) ≈ 10 × 0,7 = 7 m/s²
</p>

<p>
<i>[Ver resposta 35 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1292bd2" class="outline-5">
<h5 id="org1292bd2"><span class="section-number-5">6.2.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-6-2-7-2">
<p>
(UFMG) Qual a força normal em um corpo de 8 kg em plano de 30°?
</p>

<p>
<b>Solução:</b>
</p>

<p>
N = mg cos(30°) = 8 × 10 × (√3/2) ≈ 80 × 0,87 ≈ 69,6 N
</p>

<p>
<i>[Ver resposta 36 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org1743aa3" class="outline-4">
<h4 id="org1743aa3"><span class="section-number-4">6.2.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-6-2-8">
<ol class="org-ol">
<li><b>Decompor peso:</b> P_x = mg sen(θ), P_y = mg cos(θ)</li>
<li><b>Normal:</b> N = mg cos(θ) (não é igual a P!)</li>
<li><b>Sem atrito:</b> a = g sen(θ)</li>
<li><b>Com atrito:</b> a = g(sen(θ)</li>
<li>μ cos(θ))</li>
<li><b>Ângulos notáveis:</b> saber sen/cos de 30°, 45°, 60°</li>
<li><b>Aceleração independe da massa</b> (sem atrito)</li>
<li><b>Maior θ:</b> maior aceleração, menor normal</li>
</ol>
</div>
</div>

<div id="outline-container-orgc9a8fbe" class="outline-4">
<h4 id="orgc9a8fbe"><span class="section-number-4">6.2.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-6-2-9">
<p>
<b>Decomposição do Peso:</b>
</p>
<ul class="org-ul">
<li>P_x = mg sen(θ) (paralela)</li>
<li>P_y = mg cos(θ) (perpendicular)</li>
</ul>

<p>
<b>Normal:</b>
</p>
<ul class="org-ul">
<li>N = mg cos(θ)</li>
</ul>

<p>
<b>Aceleração:</b>
</p>
<ul class="org-ul">
<li>Sem atrito: a = g sen(θ)</li>
<li>Com atrito: a = g(sen(θ)</li>
<li>μ cos(θ))</li>
</ul>
</div>
</div>

<div id="outline-container-orgfb81561" class="outline-4">
<h4 id="orgfb81561"><span class="section-number-4">6.2.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-6-2-10">
<pre class="example" id="org35eec66">
Plano Inclinado (ângulo θ):

Decomposição do Peso:
P_x = mg sen(θ)  (paralela ao plano)
P_y = mg cos(θ)  (perpendicular)

Normal:
N = mg cos(θ)

Aceleração (sem atrito):
a = g sen(θ)

Atrito:
F_at = μN = μ mg cos(θ)

Aceleração (com atrito):
a = g(sen(θ)
- μ cos(θ))

Ângulos Notáveis:
sen(30°) = 1/2 = 0,5
cos(30°) = √3/2 ≈ 0,87
sen(45°) = cos(45°) = √2/2 ≈ 0,7
sen(60°) = √3/2 ≈ 0,87
cos(60°) = 1/2 = 0,5
</pre>
</div>
</div>

<div id="outline-container-org1dc937f" class="outline-4">
<h4 id="org1dc937f"><span class="section-number-4">6.2.11.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-6-2-11">
<pre class="example" id="org2105aa9">
PLANO INCLINADO:

        N ↑
       /|
      / |
   [m]  |
    /   |
   /    ↓ P_y = mg cos(θ)
  / P_x = mg sen(θ) →
 /      
/ θ     
────────

Decomposição:
        P_y ↑
         |
         |
        θ|___→ P_x
        /
       / P ↓

P_x "desce"
- sen(θ)
P_y "comprime"
- cos(θ)

SEM ATRITO:       COM ATRITO:
a = g sen(θ)      a = g(sen-μcos)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 30 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>aplicação prática de forças!)</li>
</ul>
</div>
</div>
</div>
</div>

<div id="outline-container-org0410175" class="outline-2">`;

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
