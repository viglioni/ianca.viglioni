<script setup lang="ts">
import { ref } from "vue";

const code = "fis-17";
const title = "Física: Movimento Circular";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-2">
<ul class="org-ul">
<li>Física: Movimento Circular</li>
<li>75min</li>
</ul>
</div>
<div id="outline-container-org221739b" class="outline-4">
<h4 id="org221739b"><span class="section-number-4">4.2.1.</span> O que é Movimento Circular?</h4>
<div class="outline-text-4" id="text-4-2-1">
<p>
<b>Movimento Circular</b> é o movimento de um corpo que descreve uma trajetória circular ou curva. É um dos movimentos mais comuns na natureza e na tecnologia: rodas, engrenagens, planetas, elétrons, etc.
</p>

<p>
<b>Características principais:</b>
</p>
<ul class="org-ul">
<li>Trajetória: circunferência ou arco de círculo</li>
<li>Direção da velocidade: sempre tangente à trajetória</li>
<li>Pode ser uniforme (velocidade constante) ou variado</li>
</ul>
</div>
</div>

<div id="outline-container-orgdfe482d" class="outline-4">
<h4 id="orgdfe482d"><span class="section-number-4">4.2.2.</span> Movimento Circular Uniforme (MCU)</h4>
<div class="outline-text-4" id="text-4-2-2">
<p>
No <b>MCU</b>, o corpo percorre arcos iguais em tempos iguais. A <b>velocidade escalar</b> é constante, mas a <b>velocidade vetorial</b> muda constantemente de direção.
</p>

<p>
<b>Propriedades do MCU:</b>
</p>
<ul class="org-ul">
<li>Velocidade escalar constante: |v| = constante</li>
<li>Velocidade vetorial varia (direção muda)</li>
<li>Existe aceleração centrípeta (direcionada ao centro)</li>
</ul>
</div>
</div>

<div id="outline-container-orgb0907df" class="outline-4">
<h4 id="orgb0907df"><span class="section-number-4">4.2.3.</span> Grandezas Angulares</h4>
<div class="outline-text-4" id="text-4-2-3">
</div>
<div id="outline-container-orgb367e0c" class="outline-5">
<h5 id="orgb367e0c"><span class="section-number-5">4.2.3.1.</span> Posição Angular (θ)</h5>
<div class="outline-text-5" id="text-4-2-3-1">
<p>
Ângulo que o raio vetor forma com uma referência.
</p>

<p>
<b>Unidades:</b>
</p>
<ul class="org-ul">
<li><b>Radiano (rad):</b> unidade SI</li>
<li><b>Grau (°):</b> 360° = 2π rad</li>
<li><b>Volta completa:</b> 2π rad = 360°</li>
</ul>

<p>
<b>Conversão:</b>
</p>
<ul class="org-ul">
<li>180° = π rad</li>
<li>1 rad ≈ 57,3°</li>
<li>θ (rad) = θ (graus) × π/180</li>
</ul>
</div>
</div>

<div id="outline-container-orgf0df313" class="outline-5">
<h5 id="orgf0df313"><span class="section-number-5">4.2.3.2.</span> Deslocamento Angular (Δθ)</h5>
<div class="outline-text-5" id="text-4-2-3-2">
<p>
Variação da posição angular. Δθ = θ_final
</p>
<ul class="org-ul">
<li>θ_inicial</li>
</ul>
</div>
</div>

<div id="outline-container-org303cd1a" class="outline-5">
<h5 id="org303cd1a"><span class="section-number-5">4.2.3.3.</span> Velocidade Angular (ω)</h5>
<div class="outline-text-5" id="text-4-2-3-3">
<p>
Taxa de variação da posição angular.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org7eaa3b4">
ω = Δθ/Δt
</pre>

<p>
<b>Unidades:</b>
</p>
<ul class="org-ul">
<li>rad/s (SI)</li>
<li>rpm (rotações por minuto)</li>
<li>rps (rotações por segundo)</li>
</ul>

<p>
<b>No MCU:</b> ω = constante
</p>

<p>
<b>Conversões:</b>
</p>
<ul class="org-ul">
<li>1 rpm = 2π/60 rad/s ≈ 0,105 rad/s</li>
<li>1 rps = 2π rad/s ≈ 6,28 rad/s</li>
</ul>
</div>
</div>

<div id="outline-container-orgce7c5e3" class="outline-5">
<h5 id="orgce7c5e3"><span class="section-number-5">4.2.3.4.</span> Período (T)</h5>
<div class="outline-text-5" id="text-4-2-3-4">
<p>
Tempo para completar uma volta completa.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgd4b6f32">
T = 2π/ω
</pre>

<p>
<b>Unidade:</b> segundos (s)
</p>
</div>
</div>

<div id="outline-container-orga318f7e" class="outline-5">
<h5 id="orga318f7e"><span class="section-number-5">4.2.3.5.</span> Frequência (f)</h5>
<div class="outline-text-5" id="text-4-2-3-5">
<p>
Número de voltas por unidade de tempo.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgf350ac6">
f = 1/T
f = ω/2π
</pre>

<p>
<b>Unidades:</b>
</p>
<ul class="org-ul">
<li>Hz (hertz) = 1/s = 1 volta/segundo</li>
<li>rpm (rotações por minuto)</li>
</ul>

<p>
<b>Relação:</b>
</p>

<pre class="example" id="orgc2cff58">
f × T = 1
</pre>
</div>
</div>
</div>

<div id="outline-container-orgaa8f6b6" class="outline-4">
<h4 id="orgaa8f6b6"><span class="section-number-4">4.2.4.</span> Relação entre Grandezas Lineares e Angulares</h4>
<div class="outline-text-4" id="text-4-2-4">
</div>
<div id="outline-container-org6e71d38" class="outline-5">
<h5 id="org6e71d38"><span class="section-number-5">4.2.4.1.</span> Arco Percorrido (s)</h5>
<div class="outline-text-5" id="text-4-2-4-1">
<pre class="example" id="orga200fa7">
s = θ × R
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>s: comprimento do arco (m)</li>
<li>θ: ângulo em radianos (rad)</li>
<li>R: raio da trajetória (m)</li>
</ul>
</div>
</div>

<div id="outline-container-org4104a3b" class="outline-5">
<h5 id="org4104a3b"><span class="section-number-5">4.2.4.2.</span> Velocidade Linear (v)</h5>
<div class="outline-text-5" id="text-4-2-4-2">
<pre class="example" id="org3c44cd1">
v = ω × R
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>v: velocidade linear (m/s)</li>
<li>ω: velocidade angular (rad/s)</li>
<li>R: raio (m)</li>
</ul>

<p>
<b>Para uma volta completa:</b>
</p>

<pre class="example" id="org2052cd3">
v = 2πR/T
v = 2πRf
</pre>
</div>
</div>
</div>

<div id="outline-container-orgca40ae0" class="outline-4">
<h4 id="orgca40ae0"><span class="section-number-4">4.2.5.</span> Aceleração Centrípeta (a_cp)</h4>
<div class="outline-text-4" id="text-4-2-5">
<p>
No MCU, existe aceleração mesmo com velocidade escalar constante, pois a <b>direção</b> da velocidade muda.
</p>

<p>
<b>Aceleração Centrípeta:</b>
</p>
<ul class="org-ul">
<li><b>Direção:</b> sempre apontando para o centro</li>
<li><b>Módulo:</b> constante no MCU</li>
</ul>

<p>
<b>Fórmulas:</b>
</p>

<pre class="example" id="org2b768d4">
a_cp = v²/R
a_cp = ω²R
a_cp = 4π²R/T²
a_cp = 4π²Rf²
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>a_cp: aceleração centrípeta (m/s²)</li>
<li>v: velocidade linear (m/s)</li>
<li>R: raio (m)</li>
<li>ω: velocidade angular (rad/s)</li>
<li>T: período (s)</li>
<li>f: frequência (Hz)</li>
</ul>
</div>
</div>

<div id="outline-container-org65834a8" class="outline-4">
<h4 id="org65834a8"><span class="section-number-4">4.2.6.</span> Movimento Circular Uniformemente Variado (MCUV)</h4>
<div class="outline-text-4" id="text-4-2-6">
<p>
Quando a velocidade angular varia uniformemente.
</p>

<p>
<b>Aceleração Angular (α):</b>
</p>

<pre class="example" id="orgfd7016d">
α = Δω/Δt
</pre>

<p>
<b>Funções do MCUV:</b>
</p>

<pre class="example" id="orgc2394db">
ω = ω₀ + αt
θ = θ₀ + ω₀t + αt²/2
ω² = ω₀² + 2αΔθ
</pre>

<p>
<b>Analogia com MUV:</b> | Linear (MUV) | Angular (MCUV) | |---------&#x2013;&#x2014;|-----------&#x2013;&#x2014;| | s (posição) | θ (posição angular) | | v (velocidade) | ω (vel. angular) | | a (aceleração) | α (acel. angular) | | v = v₀ + at | ω = ω₀ + αt | | s = s₀ + v₀t + at²/2 | θ = θ₀ + ω₀t + αt²/2 |
</p>

<p>
<b>No MCUV também existe:</b>
</p>
<ul class="org-ul">
<li>Aceleração centrípeta (varia com ω)</li>
<li>Aceleração tangencial: a_t = α × R</li>
</ul>
</div>
</div>

<div id="outline-container-org7abf3bc" class="outline-4">
<h4 id="org7abf3bc"><span class="section-number-4">4.2.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-2-7">
</div>
<div id="outline-container-org684e680" class="outline-5">
<h5 id="org684e680"><span class="section-number-5">4.2.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-2-7-1">
<p>
Um CD gira a 120 rpm. Calcule: a) A frequência em Hz b) O período c) A velocidade angular em rad/s
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li>f = 120 rpm = 120/60 = 2 Hz</li>

<li>T = 1/f = 1/2 = 0,5 s</li>

<li>ω = 2πf = 2π(2) = 4π rad/s ≈ 12,56 rad/s</li>
</ol>

<p>
<i>[Ver resposta 68 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgdea87a1" class="outline-5">
<h5 id="orgdea87a1"><span class="section-number-5">4.2.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-2-7-2">
<p>
Uma roda de raio 0,5 m gira com velocidade angular de 10 rad/s. Determine: a) A velocidade linear de um ponto na periferia b) A aceleração centrípeta
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li>v = ωR = 10 × 0,5 = 5 m/s</li>

<li>a_cp = ω²R = (10)² × 0,5 = 100 × 0,5 = 50 m/s²</li>
</ol>

<p>
Ou: a_cp = v²/R = 25/0,5 = 50 m/s²
</p>

<p>
<i>[Ver resposta 69 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org423de05" class="outline-5">
<h5 id="org423de05"><span class="section-number-5">4.2.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-2-7-3">
<p>
Um satélite completa uma órbita circular de raio 7000 km em 90 minutos. Calcule sua velocidade linear.
</p>

<p>
<b>Solução:</b>
</p>

<p>
T = 90 min = 90 × 60 = 5400 s R = 7000 km = 7 × 10⁶ m
</p>

<p>
v = 2πR/T = 2π(7 × 10⁶)/5400 v = 14π × 10⁶/5400 v ≈ 8148 m/s ≈ 8,15 km/s
</p>

<p>
<i>[Ver resposta 70 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1379af4" class="outline-5">
<h5 id="org1379af4"><span class="section-number-5">4.2.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-2-7-4">
<p>
(UFMG) Uma roda gigante tem 10 m de raio e completa uma volta em 40 s. A aceleração centrípeta de um passageiro é aproximadamente:
</p>

<p>
<b>Solução:</b>
</p>

<p>
R = 10 m T = 40 s
</p>

<p>
a_cp = 4π²R/T² = 4π²(10)/(40)² a_cp = 40π²/1600 = π²/40 a_cp ≈ 9,87/40 ≈ 0,25 m/s²
</p>

<p>
<i>[Ver resposta 71 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org12091d7" class="outline-4">
<h4 id="org12091d7"><span class="section-number-4">4.2.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-2-8">
<ol class="org-ol">
<li><b>Sempre converta rpm para rad/s ou Hz</b> quando necessário</li>
<li><b>Radianos:</b> θ deve estar em radianos em s = θR</li>
<li><b>Período e frequência:</b> f = 1/T (são inversamente proporcionais)</li>
<li><b>Velocidade no MCU:</b> v = ωR (relaciona linear e angular)</li>
<li><b>Aceleração centrípeta:</b> sempre aponta para o centro, existe mesmo com v constante</li>
<li><b>MCU vs MCUV:</b> MCU tem ω constante; MCUV tem α constante</li>
<li><b>Unidades:</b> cuidado com km → m, min → s, rpm → rad/s</li>
<li><b>Analogia MUV-MCUV:</b> todas as equações são análogas</li>
</ol>
</div>
</div>

<div id="outline-container-org17730e4" class="outline-4">
<h4 id="org17730e4"><span class="section-number-4">4.2.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-2-9">
<p>
<b>Grandezas Angulares:</b>
</p>
<ul class="org-ul">
<li>θ: posição angular (rad)</li>
<li>ω: velocidade angular (rad/s)</li>
<li>α: aceleração angular (rad/s²)</li>
<li>T: período (s)</li>
<li>f: frequência (Hz)</li>
</ul>

<p>
<b>Relações:</b>
</p>
<ul class="org-ul">
<li>f = 1/T</li>
<li>ω = 2πf = 2π/T</li>
<li>1 volta = 2π rad = 360°</li>
</ul>

<p>
<b>Linear ↔ Angular:</b>
</p>
<ul class="org-ul">
<li>s = θR</li>
<li>v = ωR</li>
<li>a_t = αR</li>
</ul>

<p>
<b>Aceleração Centrípeta (MCU):</b>
</p>
<ul class="org-ul">
<li>a_cp = v²/R</li>
<li>a_cp = ω²R</li>
<li>Direção: para o centro</li>
</ul>
</div>
</div>

<div id="outline-container-orgc897e49" class="outline-4">
<h4 id="orgc897e49"><span class="section-number-4">4.2.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-2-10">
<pre class="example" id="org1f8a21c">
Velocidade Angular:
ω = Δθ/Δt
ω = 2π/T = 2πf

Período e Frequência:
T = 1/f
f = 1/T

Conversões:
1 volta = 2π rad = 360°
1 rpm = 2π/60 rad/s

Relação Linear-Angular:
s = θR (θ em radianos)
v = ωR

Aceleração Centrípeta:
a_cp = v²/R
a_cp = ω²R
a_cp = 4π²R/T²

MCUV:
ω = ω₀ + αt
θ = θ₀ + ω₀t + αt²/2
ω² = ω₀² + 2αΔθ
</pre>
</div>
</div>

<div id="outline-container-org18188c1" class="outline-4">
<h4 id="org18188c1"><span class="section-number-4">4.2.11.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-2-11">
<pre class="example" id="org1c1a2f8">
┌─────────────────┬─────────────┬────────────┐
│   Grandeza      │   Símbolo   │  Unidade   │
├─────────────────┼─────────────┼────────────┤
│ Pos. Angular    │      θ      │   rad      │
│ Vel. Angular    │      ω      │   rad/s    │
│ Acel. Angular   │      α      │   rad/s²   │
│ Período         │      T      │     s      │
│ Frequência      │      f      │    Hz      │
└─────────────────┴─────────────┴────────────┘

Relações MCU:
        ω
       ↗ ↖
      /   \\
     f  -  T
    (f = 1/T)

Aceleração Centrípeta:
     ↑ v
    ← • → a_cp (sempre para o centro)
     ↓
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 75 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>conceitos fundamentais de cinemática)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org2e9bfe5" class="outline-3">`;

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
