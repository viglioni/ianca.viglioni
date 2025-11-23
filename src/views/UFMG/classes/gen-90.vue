<script setup lang="ts">
import { ref } from "vue";

const code = "gen-90";
const title = "Geral: Aula 90";
const subject = "geral";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-2">
<ul class="org-ul">
<li>Flash Review Física</li>
<li>45min</li>
</ul>
</div>
<div id="outline-container-org4f6ba9a" class="outline-4">
<h4 id="org4f6ba9a"><span class="section-number-4">6.2.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-6-2-1">
<p>
Revisão ultra-rápida dos conceitos MAIS importantes de Física. Relembre e relaxe!
</p>

<hr />
</div>
</div>

<div id="outline-container-org64ba27d" class="outline-4">
<h4 id="org64ba27d"><span class="section-number-4">6.2.2.</span> ⚡ TOP 10 FÓRMULAS DE FÍSICA</h4>
<div class="outline-text-4" id="text-6-2-2">
<ol class="org-ol">
<li><b>Conversão de Velocidade</b></li>
</ol>

<pre class="example" id="org4bb4f6a">
km/h → m/s: DIVIDIR por 3,6
m/s → km/h: MULTIPLICAR por 3,6
</pre>

<ol class="org-ol">
<li value="2"><b>MRU</b></li>
</ol>

<pre class="example" id="orgfbffd82">
S = S₀ + vt
</pre>

<ol class="org-ol">
<li value="3">*MRUV</li>
<li>Três Equações*</li>
</ol>

<pre class="example" id="orgd6abb38">
v = v₀ + at
S = S₀ + v₀t + (at²)/2
v² = v₀² + 2aΔS
</pre>

<ol class="org-ol">
<li value="4"><b>Queda Livre</b></li>
</ol>

<pre class="example" id="orgd1186e6">
v = gt
h = (gt²)/2
v² = 2gh
</pre>

<ol class="org-ol">
<li value="5"><b>2ª Lei de Newton</b></li>
</ol>

<pre class="example" id="org89f6424">
F = ma
</pre>

<ol class="org-ol">
<li value="6"><b>Peso</b></li>
</ol>

<pre class="example" id="org355b3d7">
P = mg
g = 10 m/s²
</pre>

<ol class="org-ol">
<li value="7"><b>Stevin (Pressão)</b></li>
</ol>

<pre class="example" id="orgecca06e">
P = ρgh
ρ_água = 1000 kg/m³
</pre>

<ol class="org-ol">
<li value="8"><b>Arquimedes (Empuxo)</b></li>
</ol>

<pre class="example" id="org3293f5b">
E = ρ_fluido × V_deslocado × g

Flutua se: ρ_corpo &lt; ρ_fluido
</pre>

<ol class="org-ol">
<li value="9"><b>Pascal (Prensa)</b></li>
</ol>

<pre class="example" id="org868885b">
F₁/A₁ = F₂/A₂
</pre>

<ol class="org-ol">
<li value="10"><b>Torricelli</b></li>
</ol>

<pre class="example" id="org86110bb">
v = √(2gh)
</pre>

<hr />
</div>
</div>

<div id="outline-container-orga46f609" class="outline-4">
<h4 id="orga46f609"><span class="section-number-4">6.2.3.</span> 🎯 LEMBRETE RÁPIDO</h4>
<div class="outline-text-4" id="text-6-2-3">
<p>
<b>Massa vs Peso:</b>
</p>

<pre class="example" id="orga24456b">
Massa: kg (não muda)
Peso: N (força, muda com g)
</pre>

<p>
<b>Densidade:</b>
</p>

<pre class="example" id="orgd069e1e">
ρ = m/V
ρ_água = 1 g/cm³ = 1000 kg/m³
</pre>

<p>
<b>Atrito:</b>
</p>

<pre class="example" id="org10ea6c9">
F_at = μN
</pre>

<hr />

<p>
<b>Você domina isso! Vai dar certo!</b> ✅
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org68448f1" class="outline-3">`;

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
