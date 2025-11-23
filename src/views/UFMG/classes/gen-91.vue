<script setup lang="ts">
import { ref } from "vue";

const code = "gen-91";
const title = "Geral: Aula 91";
const subject = "geral";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-3">
<ul class="org-ul">
<li>Flash Review Química</li>
<li>45min</li>
</ul>
</div>
<div id="outline-container-orgb531d89" class="outline-4">
<h4 id="orgb531d89"><span class="section-number-4">6.3.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-6-3-1">
<p>
Revisão ultra-rápida dos conceitos MAIS importantes de Química. Você já sabe tudo!
</p>

<hr />
</div>
</div>

<div id="outline-container-org492caa7" class="outline-4">
<h4 id="org492caa7"><span class="section-number-4">6.3.2.</span> ⚡ TOP 10 CONCEITOS DE QUÍMICA</h4>
<div class="outline-text-4" id="text-6-3-2">
<ol class="org-ol">
<li><b>Estrutura Atômica</b></li>
</ol>

<pre class="example" id="orgfdb299d">
Z = prótons
A = prótons + nêutrons
N = A − Z
</pre>

<ol class="org-ol">
<li value="2"><b>Isótopos vs Isóbaros</b></li>
</ol>

<pre class="example" id="org256a965">
Isótopos: mesmo Z
Isóbaros: mesmo A
</pre>

<ol class="org-ol">
<li value="3"><b>Eletronegatividade</b></li>
</ol>

<pre class="example" id="org9733810">
F &gt; O &gt; N &gt; Cl
(Flúor é o MAIS!)
</pre>

<ol class="org-ol">
<li value="4"><b>Ligações</b></li>
</ol>

<pre class="example" id="org35c7d6d">
Metal + Não-metal = IÔNICA
Não-metal + Não-metal = COVALENTE
Metal + Metal = METÁLICA
</pre>

<ol class="org-ol">
<li value="5"><b>Mol</b></li>
</ol>

<pre class="example" id="org1b202c7">
n = m/M
1 mol = 6,02 × 10²³
</pre>

<ol class="org-ol">
<li value="6"><b>Volume Molar</b></li>
</ol>

<pre class="example" id="org6b49100">
V = n × 22,4 L (CNTP)
</pre>

<ol class="org-ol">
<li value="7"><b>Lei de Lavoisier</b></li>
</ol>

<pre class="example" id="org8fbc6ed">
m_reagentes = m_produtos
</pre>

<ol class="org-ol">
<li value="8"><b>pH</b></li>
</ol>

<pre class="example" id="org2fd69fa">
pH + pOH = 14
pH &lt; 7: ácido
pH &gt; 7: básico
</pre>

<ol class="org-ol">
<li value="9"><b>Funções</b></li>
</ol>

<pre class="example" id="org6e3c402">
Ácido: H⁺
Base: OH⁻
Sal: cátion + ânion
</pre>

<ol class="org-ol">
<li value="10"><b>Massas Molares</b></li>
</ol>

<pre class="example" id="org0af4cb9">
H = 1, C = 12, O = 16, Na = 23, Cl = 35,5
H₂O = 18, CO₂ = 44
</pre>

<hr />
</div>
</div>

<div id="outline-container-org0edf991" class="outline-4">
<h4 id="org0edf991"><span class="section-number-4">6.3.3.</span> 🎯 LEMBRETE RÁPIDO</h4>
<div class="outline-text-4" id="text-6-3-3">
<p>
<b>Modelos Atômicos:</b>
</p>

<pre class="example" id="orgba734e8">
Dalton → Thomson → Rutherford → Bohr → Atual
</pre>

<p>
<b>Famílias:</b>
</p>

<pre class="example" id="org432f349">
Grupo 1: Alcalinos
Grupo 17: Halogênios
Grupo 18: Gases Nobres
</pre>

<p>
<b>Propriedades Periódicas:</b>
</p>

<pre class="example" id="orga260bad">
Raio: ↑ família, ← período
Eletronegatividade: ↓ família, → período
</pre>

<hr />

<p>
<b>Você arrasou nos estudos! Acredite!</b> ✅
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org3f740c8" class="outline-3">`;

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
