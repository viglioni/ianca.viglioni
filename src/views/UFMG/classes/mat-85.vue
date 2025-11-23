<script setup lang="ts">
import { ref } from "vue";

const code = "mat-85";
const title = "Matemática: Fórmulas Essenciais";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-5">
<ul class="org-ul">
<li>Matemática: Fórmulas Essenciais</li>
<li>Folha de Consulta</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org3df6e0e" class="outline-4">
<h4 id="org3df6e0e"><span class="section-number-4">5.5.1.</span> </h4>
<div class="outline-text-4" id="text-5-5-1">
<pre class="example" id="org5e5f5ec">
    ╔════════════════════════════════════════════════════════════╗
    ║         FÓRMULAS ESSENCIAIS
- GUIA RÁPIDO                  ║
    ╚════════════════════════════════════════════════════════════╝
    
    MATEMÁTICA:
    ┌──────────────────────────────────────────────────────────┐
    │ Função Afim:      f(x) = ax + b                          │
    │ • Raiz: x = -b/a                                         │
    │ • Crescente se a &gt; 0, Decrescente se a &lt; 0              │
    └──────────────────────────────────────────────────────────┘
    
    ┌──────────────────────────────────────────────────────────┐
    │ Função Quadrática: f(x) = ax² + bx + c                   │
    │ • Δ = b²
- 4ac                                           │
    │ • x = (-b ± √Δ) / 2a                                     │
    │ • xᵥ = -b/2a    yᵥ = -Δ/4a                              │
    │ • Concavidade ∪ se a &gt; 0, ∩ se a &lt; 0                    │
    └──────────────────────────────────────────────────────────┘
    
    ┌──────────────────────────────────────────────────────────┐
    │ Geometria:                                                │
    │ • Triângulo: A = (b×h)/2                                 │
    │ • Pitágoras: a² + b² = c²                                │
    │ • Círculo: A = πr²,  C = 2πr                            │
    └──────────────────────────────────────────────────────────┘
    
    FÍSICA:
    ┌──────────────────────────────────────────────────────────┐
    │ MRU:              S = S₀ + vt                            │
    │ MRUV:             v = v₀ + at                            │
    │                   S = S₀ + v₀t + at²/2                   │
    │                   v² = v₀² + 2aΔS                        │
    │ Newton:           F = ma                                  │
    │ Hidrostática:     P = ρgh (Stevin)                       │
    │                   F₁/A₁ = F₂/A₂ (Pascal)                 │
    │                   E = ρVg (Arquimedes)                   │
    └──────────────────────────────────────────────────────────┘
    
    QUÍMICA:
    ┌──────────────────────────────────────────────────────────┐
    │ Densidade:        d = m/V                                 │
    │ Mol:              n = m/M                                 │
    │                   N = n × 6,02×10²³                       │
    │ Camadas:          K L M N O P Q                          │
    │ Subcamadas:       s p d f (2 6 10 14 elétrons)          │
    └──────────────────────────────────────────────────────────┘
</pre>
</div>
</div>

<div id="outline-container-org61f01e1" class="outline-4">
<h4 id="org61f01e1"><span class="section-number-4">5.5.2.</span> Objetivo</h4>
<div class="outline-text-4" id="text-5-5-2">
<p>
Compilar TODAS as fórmulas essenciais de Matemática em uma folha de consulta rápida.
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org8a09951" class="outline-3">`;

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
