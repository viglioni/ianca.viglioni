<script setup lang="ts">
import { ref } from "vue";

const code = "fis-58";
const title = "Física: Revisão de Cinemática (MRU, MRUV, Queda Livre, Lançamentos)";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-2">
<ul class="org-ul">
<li>Física: Revisão de Cinemática (MRU, MRUV, Queda Livre, Lançamentos)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org76b774d" class="outline-4">
<h4 id="org76b774d"><span class="section-number-4">5.2.1.</span> Conceitos Fundamentais de Cinemática</h4>
<div class="outline-text-4" id="text-5-2-1">
<p>
<b>Cinemática:</b> estuda o movimento sem considerar suas causas (forças)
</p>

<p>
<b>Grandezas fundamentais:</b>
</p>

<p>
<b>Posição (s):</b> localização no espaço (m)
</p>

<p>
<b>Deslocamento (Δs):</b>
</p>

<pre class="example" id="org3bc0225">
Δs = s_final
- s_inicial
</pre>

<p>
<b>Velocidade (v):</b> taxa de variação da posição
</p>

<pre class="example" id="org67b7feb">
v = Δs / Δt
</pre>

<ul class="org-ul">
<li>Unidade SI: m/s</li>
<li>Conversão: km/h ÷ 3,6 = m/s</li>
</ul>

<p>
<b>Aceleração (a):</b> taxa de variação da velocidade
</p>

<pre class="example" id="org31e395a">
a = Δv / Δt
</pre>

<ul class="org-ul">
<li>Unidade SI: m/s²</li>
</ul>
</div>
</div>

<div id="outline-container-orgab031a1" class="outline-4">
<h4 id="orgab031a1"><span class="section-number-4">5.2.2.</span> Movimento Retilíneo Uniforme (MRU)</h4>
<div class="outline-text-4" id="text-5-2-2">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Velocidade <b>constante</b></li>
<li>Aceleração = 0</li>
<li>Trajetória <b>retilínea</b></li>
</ul>

<p>
<b>Equação horária:</b>
</p>

<pre class="example" id="org517e0dc">
s = s₀ + vt
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>s = posição final (m)</li>
<li>s₀ = posição inicial (m)</li>
<li>v = velocidade (m/s)</li>
<li>t = tempo (s)</li>
</ul>

<p>
<b>Gráficos:</b>
</p>

<p>
<b>s × t:</b> reta inclinada
</p>
<ul class="org-ul">
<li>Inclinação = velocidade</li>
</ul>

<p>
<b>v × t:</b> reta horizontal
</p>
<ul class="org-ul">
<li>v = constante</li>
</ul>

<p>
<b>Exemplo:</b> Carro a 20 m/s, parte de s₀ = 10 m. Posição em t = 5 s? s = 10 + 20×5 = 10 + 100 = 110 m
</p>
</div>
</div>

<div id="outline-container-org9fbe31d" class="outline-4">
<h4 id="org9fbe31d"><span class="section-number-4">5.2.3.</span> Movimento Retilíneo Uniformemente Variado (MRUV)</h4>
<div class="outline-text-4" id="text-5-2-3">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Aceleração <b>constante</b> (≠ 0)</li>
<li>Velocidade <b>varia uniformemente</b></li>
<li>Trajetória <b>retilínea</b></li>
</ul>

<p>
<b>Equações:</b>
</p>

<p>
<b>1. Velocidade em função do tempo:</b>
</p>

<pre class="example" id="org494ef30">
v = v₀ + at
</pre>

<p>
<b>2. Posição em função do tempo:</b>
</p>

<pre class="example" id="orgefbf0b2">
s = s₀ + v₀t + ½at²
</pre>

<p>
<b>3. Equação de Torricelli (sem tempo):</b>
</p>

<pre class="example" id="org2a304af">
v² = v₀² + 2aΔs
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>v = velocidade final (m/s)</li>
<li>v₀ = velocidade inicial (m/s)</li>
<li>a = aceleração (m/s²)</li>
<li>t = tempo (s)</li>
<li>Δs = deslocamento (m)</li>
</ul>

<p>
<b>Gráficos:</b>
</p>

<p>
<b>v × t:</b> reta inclinada
</p>
<ul class="org-ul">
<li>Inclinação = aceleração</li>
<li>Área sob a reta = deslocamento</li>
</ul>

<p>
<b>a × t:</b> reta horizontal
</p>
<ul class="org-ul">
<li>a = constante</li>
</ul>

<p>
<b>Exemplo:</b> Carro parte do repouso (v₀ = 0) com a = 2 m/s². Velocidade em t = 10 s? v = 0 + 2×10 = 20 m/s
</p>
</div>
</div>

<div id="outline-container-org15340e9" class="outline-4">
<h4 id="org15340e9"><span class="section-number-4">5.2.4.</span> Queda Livre</h4>
<div class="outline-text-4" id="text-5-2-4">
<p>
<b>Caso especial de MRUV:</b>
</p>
<ul class="org-ul">
<li>a = g = 10 m/s² (gravidade, para baixo)</li>
<li>v₀ = 0 (solta do repouso)</li>
<li>Movimento <b>vertical</b></li>
</ul>

<p>
<b>Equações (queda livre):</b>
</p>

<pre class="example" id="orge4f0de9">
v = gt
h = ½gt²
v² = 2gh
</pre>

<p>
<b>Onde h é a altura</b>
</p>

<p>
<b>Exemplo:</b> Objeto cai de 20 m. Velocidade ao chegar no chão? v² = 2×10×20 = 400 v = 20 m/s
</p>

<p>
<b>Tempo de queda:</b> h = ½gt² 20 = ½×10×t² 20 = 5t² t² = 4 t = 2 s
</p>
</div>
</div>

<div id="outline-container-org4185cf6" class="outline-4">
<h4 id="org4185cf6"><span class="section-number-4">5.2.5.</span> Lançamento Vertical</h4>
<div class="outline-text-4" id="text-5-2-5">
<p>
<b>Para cima:</b>
</p>
<ul class="org-ul">
<li>v₀ ≠ 0 (lançado)</li>
<li>a = -g = -10 m/s² (gravidade freia)</li>
<li>Sobe até v = 0 (altura máxima)</li>
<li>Depois cai</li>
</ul>

<p>
<b>Equações:</b>
</p>

<pre class="example" id="org5593297">
v = v₀
- gt
h = v₀t
- ½gt²
v² = v₀²
- 2gh
</pre>

<p>
<b>Altura máxima:</b> v = 0 no ponto mais alto
</p>

<pre class="example" id="org32628a5">
h_máx = v₀² / (2g)
</pre>

<p>
<b>Tempo de subida:</b>
</p>

<pre class="example" id="org77b568f">
t_subida = v₀ / g
</pre>

<p>
<b>Tempo total (subida + descida):</b>
</p>

<pre class="example" id="orga7027b5">
t_total = 2v₀ / g
</pre>

<p>
<b>Exemplo:</b> Bola lançada para cima com v₀ = 30 m/s. Altura máxima? h_máx = 30² / (2×10) = 900 / 20 = 45 m
</p>

<p>
Tempo de subida: t = 30 / 10 = 3 s
</p>
</div>
</div>

<div id="outline-container-orge8be0e0" class="outline-4">
<h4 id="orge8be0e0"><span class="section-number-4">5.2.6.</span> Lançamento Horizontal</h4>
<div class="outline-text-4" id="text-5-2-6">
<p>
<b>Movimento composto:</b>
</p>
<ul class="org-ul">
<li><b>Horizontal:</b> MRU (v_x = constante)</li>
<li><b>Vertical:</b> queda livre (a_y = g)</li>
</ul>

<p>
<b>Equações:</b>
</p>

<p>
<b>Horizontal (x):</b>
</p>

<pre class="example" id="orge0814ad">
x = v₀t
</pre>

<p>
<b>Vertical (y):</b>
</p>

<pre class="example" id="orgf570548">
y = ½gt²
v_y = gt
</pre>

<p>
<b>Tempo de queda:</b> depende da altura
</p>

<pre class="example" id="orgde48674">
t = √(2h/g)
</pre>

<p>
<b>Alcance:</b>
</p>

<pre class="example" id="org6dccf70">
A = v₀ × √(2h/g)
</pre>

<p>
<b>Exemplo:</b> Objeto lançado horizontalmente a 20 m/s de altura 5 m.
</p>

<p>
Tempo até o chão: t = √(2×5/10) = √1 = 1 s
</p>

<p>
Alcance: A = 20 × 1 = 20 m
</p>
</div>
</div>

<div id="outline-container-orgba1641e" class="outline-4">
<h4 id="orgba1641e"><span class="section-number-4">5.2.7.</span> Exercícios de Revisão</h4>
<div class="outline-text-4" id="text-5-2-7">
</div>
<div id="outline-container-org582db64" class="outline-5">
<h5 id="org582db64"><span class="section-number-5">5.2.7.1.</span> Exercício 1 (MRU)</h5>
<div class="outline-text-5" id="text-5-2-7-1">
<p>
Um carro a 72 km/h percorre quanto em 10 s?
</p>

<p>
<b>Solução:</b> v = 72 km/h = 72÷3,6 = 20 m/s s = vt = 20×10 = 200 m
</p>

<p>
<i>[Ver resposta 63 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org84b2dff" class="outline-5">
<h5 id="org84b2dff"><span class="section-number-5">5.2.7.2.</span> Exercício 2 (MRUV)</h5>
<div class="outline-text-5" id="text-5-2-7-2">
<p>
Carro parte do repouso com a = 3 m/s². Qual a velocidade em 8 s?
</p>

<p>
<b>Solução:</b> v = v₀ + at = 0 + 3×8 = 24 m/s
</p>

<p>
<i>[Ver resposta 64 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org258eb70" class="outline-5">
<h5 id="org258eb70"><span class="section-number-5">5.2.7.3.</span> Exercício 3 (MRUV)</h5>
<div class="outline-text-5" id="text-5-2-7-3">
<p>
Móvel a 10 m/s acelera a 2 m/s² por 5 s. Qual o deslocamento?
</p>

<p>
<b>Solução:</b> s = v₀t + ½at² s = 10×5 + ½×2×25 s = 50 + 25 = 75 m
</p>

<p>
<i>[Ver resposta 65 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org457576d" class="outline-5">
<h5 id="org457576d"><span class="section-number-5">5.2.7.4.</span> Exercício 4 (Queda Livre)</h5>
<div class="outline-text-5" id="text-5-2-7-4">
<p>
Pedra cai de altura 45 m. Tempo de queda?
</p>

<p>
<b>Solução:</b> h = ½gt² 45 = ½×10×t² 45 = 5t² t² = 9 t = 3 s
</p>

<p>
<i>[Ver resposta 66 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org50cc389" class="outline-5">
<h5 id="org50cc389"><span class="section-number-5">5.2.7.5.</span> Exercício 5 (Lançamento Vertical)</h5>
<div class="outline-text-5" id="text-5-2-7-5">
<p>
Bola lançada para cima com 20 m/s. Altura máxima?
</p>

<p>
<b>Solução:</b> h_máx = v₀²/(2g) = 400/(2×10) = 400/20 = 20 m
</p>

<p>
<i>[Ver resposta 67 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org29955c5" class="outline-5">
<h5 id="org29955c5"><span class="section-number-5">5.2.7.6.</span> Exercício 6 (Torricelli)</h5>
<div class="outline-text-5" id="text-5-2-7-6">
<p>
Móvel parte do repouso e atinge 40 m/s após percorrer 80 m. Qual a aceleração?
</p>

<p>
<b>Solução:</b> v² = v₀² + 2aΔs 40² = 0² + 2×a×80 1600 = 160a a = 10 m/s²
</p>

<p>
<i>[Ver resposta 68 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgab5d3a1" class="outline-4">
<h4 id="orgab5d3a1"><span class="section-number-4">5.2.8.</span> Comparação MRU × MRUV</h4>
<div class="outline-text-4" id="text-5-2-8">
<pre class="example" id="org1857124">
┌─────────────┬──────────┬──────────┐
│             │   MRU    │   MRUV   │
├─────────────┼──────────┼──────────┤
│ Velocidade  │ Constante│  Varia   │
│ Aceleração  │    0     │ Constante│
│ Equação s   │ s₀+vt    │s₀+v₀t+½at²│
│ Gráfico v×t │Horizontal│ Inclinado│
└─────────────┴──────────┴──────────┘
</pre>
</div>
</div>

<div id="outline-container-org1011747" class="outline-4">
<h4 id="org1011747"><span class="section-number-4">5.2.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-2-9">
<ol class="org-ol">
<li><b>MRU:</b> a = 0, v = constante, s = s₀ + vt</li>
<li><b>MRUV:</b> a = constante, 3 equações (v, s, Torricelli)</li>
<li><b>Queda livre:</b> v₀ = 0, a = g = 10 m/s²</li>
<li><b>Lançamento vertical:</b> a = -g (para cima)</li>
<li><b>Altura máxima:</b> v = 0 no topo</li>
<li><b>Torricelli:</b> quando não tem tempo</li>
<li><b>Converter km/h → m/s: ÷3,6</b></li>
<li><b>Gráfico v×t:</b> área = deslocamento</li>
<li><b>g = 10 m/s²</b> (aproximação na prova)</li>
<li><b>Vetor velocidade:</b> sinal indica sentido</li>
</ol>
</div>
</div>

<div id="outline-container-org9f934bc" class="outline-4">
<h4 id="org9f934bc"><span class="section-number-4">5.2.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-2-10">
<p>
<b>MRU:</b>
</p>
<ul class="org-ul">
<li>v = constante</li>
<li>s = s₀ + vt</li>
</ul>

<p>
<b>MRUV:</b>
</p>
<ul class="org-ul">
<li>a = constante</li>
<li>v = v₀ + at</li>
<li>s = s₀ + v₀t + ½at²</li>
<li>v² = v₀² + 2aΔs</li>
</ul>

<p>
<b>Queda Livre:</b>
</p>
<ul class="org-ul">
<li>v₀ = 0, a = g</li>
<li>v = gt</li>
<li>h = ½gt²</li>
<li>v² = 2gh</li>
</ul>

<p>
<b>Lançamento Vertical:</b>
</p>
<ul class="org-ul">
<li>a = -g (para cima)</li>
<li>h_máx = v₀²/(2g)</li>
<li>t_subida = v₀/g</li>
</ul>
</div>
</div>

<div id="outline-container-orga4cbfc7" class="outline-4">
<h4 id="orga4cbfc7"><span class="section-number-4">5.2.11.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-5-2-11">
<pre class="example" id="orgcf05516">
MRU:
s = s₀ + vt
v = Δs / Δt

MRUV:
v = v₀ + at
s = s₀ + v₀t + ½at²
v² = v₀² + 2aΔs

Queda Livre (v₀ = 0, a = g):
v = gt
h = ½gt²
v² = 2gh

Lançamento Vertical (a = -g):
v = v₀
- gt
h = v₀t
- ½gt²
v² = v₀²
- 2gh
h_máx = v₀² / (2g)
t_subida = v₀ / g

Lançamento Horizontal:
x = v₀t  (horizontal, MRU)
y = ½gt² (vertical, queda livre)

Conversão:
km/h ÷ 3,6 = m/s
m/s × 3,6 = km/h

Constantes:
g = 10 m/s² (Terra)
</pre>
</div>
</div>

<div id="outline-container-org459405b" class="outline-4">
<h4 id="org459405b"><span class="section-number-4">5.2.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-2-12">
<pre class="example" id="org84a12fb">
MRU:
  v constante
  ─────────────→
  s = s₀ + vt

MRUV:
  v aumenta
  ───→──→───→
  s = s₀ + v₀t + ½at²

QUEDA LIVRE:
     │
     │ v aumenta
     ↓ (a = g)
     •
  h = ½gt²

LANÇAMENTO VERTICAL:
     ↑ v diminui (a = -g)
     │ v = 0 (h_máx)
     ↓ v aumenta (a = g)
     •

GRÁFICOS:

MRU (v×t):     MRUV (v×t):
  v│             v│   /
   │─────         │  /
   └────t         └─/──t
   
MRU (s×t):     MRUV (s×t):
  s│   /          s│   _/
   │  /            │ _/
   └─/──t          └/───t
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>revisão completa de cinemática!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org954557a" class="outline-3">`;

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
