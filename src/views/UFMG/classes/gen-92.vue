<script setup lang="ts">
import { ref } from "vue";

const code = "gen-92";
const title = "Geral: Aula 92";
const subject = "geral";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-4">
<ul class="org-ul">
<li>Flash Review Humanas (História/Geografia/Filosofia/Sociologia)</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-org9a3cad2" class="outline-4">
<h4 id="org9a3cad2"><span class="section-number-4">6.4.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-6-4-1">
<p>
Revisão express de Humanas. Conceitos-chave apenas!
</p>

<hr />
</div>
</div>

<div id="outline-container-org1cfbc56" class="outline-4">
<h4 id="org1cfbc56"><span class="section-number-4">6.4.2.</span> ⚡ HISTÓRIA</h4>
<div class="outline-text-4" id="text-6-4-2">
<ul class="org-ul">
<li>ESSENCIAL</li>
</ul>
<p>
<b>Grandes Navegações:</b>
</p>

<pre class="example" id="org7b886e0">
1500: Cabral → Brasil
1534: Capitanias Hereditárias
1548: Governo-Geral
</pre>

<p>
<b>Plantation:</b>
</p>

<pre class="example" id="org9878a18">
Monocultura + Latifúndio + Escravidão + Exportação
</pre>

<p>
<b>Períodos:</b>
</p>

<pre class="example" id="orge93dc41">
Antiguidade: Grécia (democracia) + Roma
Idade Média: Feudalismo, Igreja
Moderna: Renascimento, Absolutismo
</pre>

<hr />
</div>
</div>

<div id="outline-container-org99b3dae" class="outline-4">
<h4 id="org99b3dae"><span class="section-number-4">6.4.3.</span> ⚡ GEOGRAFIA</h4>
<div class="outline-text-4" id="text-6-4-3">
<ul class="org-ul">
<li>ESSENCIAL</li>
</ul>
<p>
<b>Coordenadas:</b>
</p>

<pre class="example" id="org382b0cc">
Latitude: 0-90° N/S
Longitude: 0-180° L/O
</pre>

<p>
<b>Clima:</b>
</p>

<pre class="example" id="orgb902e09">
↑ Latitude → ↓ Temperatura
↑ Altitude → ↓ Temperatura (6°C/1000m)
</pre>

<p>
<b>Placas Tectônicas:</b>
</p>

<pre class="example" id="orgd8ec964">
Divergente: afastam
Convergente: colidem (montanhas)
Transformante: deslizam (terremotos)
</pre>

<p>
<b>Climas Brasil:</b>
</p>

<pre class="example" id="org17e4e7d">
Equatorial: Amazônia (quente, úmido)
Tropical: Centro (quente, chuva verão)
Semi-árido: Sertão (seco)
Subtropical: Sul (4 estações)
</pre>

<hr />
</div>
</div>

<div id="outline-container-orgea5297c" class="outline-4">
<h4 id="orgea5297c"><span class="section-number-4">6.4.4.</span> ⚡ FILOSOFIA</h4>
<div class="outline-text-4" id="text-6-4-4">
<ul class="org-ul">
<li>ESSENCIAL</li>
</ul>
<p>
<b>Origem:</b>
</p>

<pre class="example" id="org1d8ca58">
Grécia, século VI a.C.
Mito → Logos
</pre>

<p>
<b>Filósofos:</b>
</p>

<pre class="example" id="org6f27df9">
Sócrates: "Conhece-te a ti mesmo"
Platão: Mundo das Ideias
Aristóteles: Lógica, silogismo
</pre>

<hr />
</div>
</div>

<div id="outline-container-orgf1b633d" class="outline-4">
<h4 id="orgf1b633d"><span class="section-number-4">6.4.5.</span> ⚡ SOCIOLOGIA</h4>
<div class="outline-text-4" id="text-6-4-5">
<ul class="org-ul">
<li>ESSENCIAL</li>
</ul>
<p>
<b>Origem:</b>
</p>

<pre class="example" id="orgec578d4">
Século XIX
Revolução Industrial + Francesa
</pre>

<p>
<b>Fundadores:</b>
</p>

<pre class="example" id="org8853b9c">
Comte: Positivismo
Marx: Luta de classes
Durkheim: Fato social
Weber: Ação social
</pre>

<p>
<b>Conceitos:</b>
</p>

<pre class="example" id="org390cfd7">
Etnocentrismo: julgar outras culturas
Cultura: valores, costumes aprendidos
</pre>

<hr />

<p>
<b>Você tem conhecimento de sobra!</b> ✅
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org873c371" class="outline-3">`;

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
