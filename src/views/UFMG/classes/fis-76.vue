<script setup lang="ts">
import { ref } from "vue";

const code = "fis-76";
const title = "Física: Revisão Geral";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-2">
<ul class="org-ul">
<li>Física: Revisão Geral</li>
<li>Todos os Conceitos</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org6ea83ca" class="outline-4">
<h4 id="org6ea83ca"><span class="section-number-4">4.2.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-4-2-1">
<p>
Revisão abrangente de TODOS os tópicos de Física: Cinemática, Dinâmica e Hidrostática.
</p>
</div>
</div>

<div id="outline-container-orgd36170b" class="outline-4">
<h4 id="orgd36170b"><span class="section-number-4">4.2.2.</span> BLOCO 1: Cinemática</h4>
<div class="outline-text-4" id="text-4-2-2">
<ul class="org-ul">
<li>Revisão Rápida (30min)</li>
</ul>
<p>
<b>Conceitos fundamentais:</b>
</p>

<pre class="example" id="org6d600ef">
Posição (S): localização
Velocidade (v): v = ΔS/Δt
Aceleração (a): a = Δv/Δt

Conversão: km/h ↔ m/s (÷ ou × 3,6)
</pre>

<p>
<b>MRU (Movimento Retilíneo Uniforme):</b>
</p>

<pre class="example" id="orgee97cee">
v = constante
a = 0

S = S₀ + vt
</pre>

<p>
<b>MRUV (Movimento Retilíneo Uniformemente Variado):</b>
</p>

<pre class="example" id="org7fef55a">
a = constante

Equações:
v = v₀ + at
S = S₀ + v₀t + at²/2
v² = v₀² + 2aΔS  (Torricelli)
</pre>

<p>
<b>Queda Livre (v₀ = 0, a = g):</b>
</p>

<pre class="example" id="orgacb0725">
v = gt
h = gt²/2
v² = 2gh
</pre>

<p>
<b>Lançamento Vertical:</b>
</p>

<pre class="example" id="org5eb924c">
h_máx = v₀²/(2g)
t_subida = v₀/g
t_total = 2v₀/g
</pre>

<p>
<b>Exercício integrador:</b>
</p>

<pre class="example" id="org05c9884">
Um carro a 20 m/s freia com a = -4 m/s². 
a) Quanto tempo até parar?
b) Qual a distância percorrida?

a) v = v₀ + at
   0 = 20 + (-4)t
   4t = 20
   t = 5 s

b) v² = v₀² + 2aΔS
   0 = 20² + 2(-4)ΔS
   0 = 400
- 8ΔS
   ΔS = 50 m
</pre>
</div>
</div>

<div id="outline-container-org4b0b19c" class="outline-4">
<h4 id="org4b0b19c"><span class="section-number-4">4.2.3.</span> BLOCO 2: Dinâmica</h4>
<div class="outline-text-4" id="text-4-2-3">
<ul class="org-ul">
<li>Leis de Newton (30min)</li>
</ul>
<p>
<b>1ª Lei (Inércia):</b>
</p>

<pre class="example" id="org490fcf5">
F_R = 0 → velocidade constante (MRU ou repouso)
</pre>

<p>
<b>2ª Lei (Fundamental):</b>
</p>

<pre class="example" id="orgdd96e18">
F_R = m × a

Unidade: Newton (N)
1 N = 1 kg·m/s²
</pre>

<p>
<b>3ª Lei (Ação e Reação):</b>
</p>

<pre class="example" id="orgd17335d">
Forças iguais, opostas, em corpos diferentes
</pre>

<p>
<b>Força Peso:</b>
</p>

<pre class="example" id="org3756b2d">
P = m × g

Onde g = 10 m/s² (Terra)
</pre>

<p>
<b>Força Normal:</b>
</p>

<pre class="example" id="orgfdede5b">
Superfície horizontal: N = P = mg
</pre>

<p>
<b>Força de Atrito:</b>
</p>

<pre class="example" id="orgaeee018">
F_at = μ × N

μ = coeficiente de atrito
</pre>

<p>
<b>Problema modelo:</b>
</p>

<pre class="example" id="org5cbae79">
Um bloco de 5 kg está sobre superfície horizontal com μ = 0,3.
Qual a força de atrito máxima?

N = mg = 5 × 10 = 50 N
F_at = 0,3 × 50 = 15 N
</pre>

<p>
<b>Aplicação integrada:</b>
</p>

<pre class="example" id="org8c1ca93">
Força de 60 N puxa bloco de 10 kg com atrito 20 N.
Qual a aceleração?

F_R = F_aplicada
- F_atrito
F_R = 60
- 20 = 40 N

F_R = ma
40 = 10a
a = 4 m/s²
</pre>
</div>
</div>

<div id="outline-container-orga2cc3e6" class="outline-4">
<h4 id="orga2cc3e6"><span class="section-number-4">4.2.4.</span> BLOCO 3: Hidrostática</h4>
<div class="outline-text-4" id="text-4-2-4">
<ul class="org-ul">
<li>Revisão Completa (30min)</li>
</ul>
<p>
<b>Densidade:</b>
</p>

<pre class="example" id="org3f29d07">
ρ = m/V

Dados importantes:
ρ_água = 1000 kg/m³ = 1 g/cm³
ρ_mercúrio = 13600 kg/m³
</pre>

<p>
<b>Pressão:</b>
</p>

<pre class="example" id="org138bf6b">
P = F/A

Unidades:
Pa (N/m²)
atm (1 atm ≈ 10⁵ Pa)
mmHg (1 atm = 760 mmHg)
</pre>

<p>
<b>Teorema de Stevin:</b>
</p>

<pre class="example" id="orgbfa0451">
P = P_atm + ρgh

ou

ΔP = ρgΔh

Pressão aumenta com profundidade!
</pre>

<p>
<b>Princípio de Pascal (Prensa Hidráulica):</b>
</p>

<pre class="example" id="orgdb502a6">
P₁ = P₂

F₁/A₁ = F₂/A₂

F₂ = F₁ × (A₂/A₁)
</pre>

<p>
<b>Princípio de Arquimedes (Empuxo):</b>
</p>

<pre class="example" id="orgc7c0edd">
E = ρ_fluido × V_deslocado × g

Flutuação:
- Afunda: ρ_corpo &gt; ρ_fluido (E &lt; P)
- Flutua: ρ_corpo &lt; ρ_fluido (E = P)
- Fração submersa: f = ρ_corpo/ρ_fluido

Peso aparente:
P_aparente = P_real
- E
</pre>

<p>
<b>Teorema de Torricelli:</b>
</p>

<pre class="example" id="org14e1c05">
v = √(2gh)

Velocidade de saída de fluido
</pre>

<p>
<b>Problema integrado:</b>
</p>

<pre class="example" id="org3ccc011">
Um cubo de 1000 cm³ e massa 800 g é colocado na água.
a) Ele afunda ou flutua?
b) Qual a fração submersa?

a) ρ_cubo = m/V = 800g/1000cm³ = 0,8 g/cm³
   ρ_água = 1 g/cm³
   ρ_cubo &lt; ρ_água → FLUTUA!

b) f = ρ_cubo/ρ_água = 0,8/1 = 0,8 = 80% submerso
</pre>
</div>
</div>

<div id="outline-container-org77217dc" class="outline-4">
<h4 id="org77217dc"><span class="section-number-4">4.2.5.</span> Problemas Mistos</h4>
<div class="outline-text-4" id="text-4-2-5">
<ul class="org-ul">
<li>Treino Final</li>
</ul>
</div>
<div id="outline-container-org016d027" class="outline-5">
<h5 id="org016d027"><span class="section-number-5">4.2.5.1.</span> Problema 1</h5>
<div class="outline-text-5" id="text-4-2-5-1">
<p>
Um objeto cai de 20 m. Com que velocidade atinge o solo? (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org95d98c1">
v² = 2gh = 2 × 10 × 20 = 400
v = 20 m/s
</pre>
</div>
</div>

<div id="outline-container-org05461ef" class="outline-5">
<h5 id="org05461ef"><span class="section-number-5">4.2.5.2.</span> Problema 2</h5>
<div class="outline-text-5" id="text-4-2-5-2">
<p>
Qual o peso de um astronauta de 80 kg na Lua? (g_Lua = 1,6 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org7d8d37d">
P = mg = 80 × 1,6 = 128 N
</pre>
</div>
</div>

<div id="outline-container-orge0448fd" class="outline-5">
<h5 id="orge0448fd"><span class="section-number-5">4.2.5.3.</span> Problema 3</h5>
<div class="outline-text-5" id="text-4-2-5-3">
<p>
Pressão a 8 m de profundidade na água?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgcc15a12">
P = ρgh = 1000 × 10 × 8 = 80.000 Pa = 8 × 10⁴ Pa
</pre>
</div>
</div>

<div id="outline-container-org03869b0" class="outline-5">
<h5 id="org03869b0"><span class="section-number-5">4.2.5.4.</span> Problema 4</h5>
<div class="outline-text-5" id="text-4-2-5-4">
<p>
Prensa hidráulica: A₁ = 5 cm², A₂ = 25 cm², F₁ = 40 N. Calcule F₂.
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org687eee2">
F₂ = F₁ × (A₂/A₁) = 40 × (25/5) = 40 × 5 = 200 N
</pre>
</div>
</div>

<div id="outline-container-org42934e6" class="outline-5">
<h5 id="org42934e6"><span class="section-number-5">4.2.5.5.</span> Problema 5</h5>
<div class="outline-text-5" id="text-4-2-5-5">
<p>
Velocidade de saída de água em orifício a 5 m de profundidade?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org0fa5727">
v = √(2gh) = √(2 × 10 × 5) = √100 = 10 m/s
</pre>
</div>
</div>
</div>

<div id="outline-container-orgefab738" class="outline-4">
<h4 id="orgefab738"><span class="section-number-4">4.2.6.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-2-6">
<ul class="org-ul">
<li>RESUMO COMPLETO</li>
</ul>
<pre class="example" id="org823e91c">
CINEMÁTICA:
v = ΔS/Δt
a = Δv/Δt

MRU: S = S₀ + vt

MRUV:
v = v₀ + at
S = S₀ + v₀t + at²/2
v² = v₀² + 2aΔS

Queda livre:
v = gt, h = gt²/2, v² = 2gh

Lançamento vertical:
h_máx = v₀²/(2g)

DINÂMICA:
F_R = ma
P = mg
F_at = μN

HIDROSTÁTICA:
ρ = m/V
P = F/A
Stevin: P = P_atm + ρgh
Pascal: F₁/A₁ = F₂/A₂
Arquimedes: E = ρ_fluido × V × g
Torricelli: v = √(2gh)

DADOS:
g = 10 m/s²
ρ_água = 1000 kg/m³ = 1 g/cm³
P_atm = 10⁵ Pa
</pre>
</div>
</div>

<div id="outline-container-org6bc1dcd" class="outline-4">
<h4 id="org6bc1dcd"><span class="section-number-4">4.2.7.</span> Checklist Final</h4>
<div class="outline-text-4" id="text-4-2-7">
<ul class="org-ul">
<li>Física</li>
<li class="off"><code>[&#xa0;]</code> Sei as 3 equações do MRUV e quando usar cada uma</li>
<li class="off"><code>[&#xa0;]</code> Sei converter km/h ↔ m/s</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver queda livre e lançamento vertical</li>
<li class="off"><code>[&#xa0;]</code> Sei as 3 Leis de Newton</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar F = ma</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular peso e diferenciar de massa</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular densidade</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar Stevin (pressão em fluidos)</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver prensa hidráulica (Pascal)</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular empuxo e determinar flutuação</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar Torricelli</li>
</ul>
</div>
</div>

<div id="outline-container-org62a2f62" class="outline-4">
<h4 id="org62a2f62"><span class="section-number-4">4.2.8.</span> Dicas para a Prova de Física</h4>
<div class="outline-text-4" id="text-4-2-8">
<ol class="org-ol">
<li><b>Identifique o tipo de movimento:</b> MRU (v constante) ou MRUV (a constante)</li>
<li><b>Liste dados e incógnita</b> antes de escolher a fórmula</li>
<li><b>Atenção às unidades:</b> sempre use SI (m, s, kg, N)</li>
<li><b>Conversão km/h → m/s:</b> divida por 3,6</li>
<li><b>Queda livre:</b> sempre g = 10 m/s²</li>
<li><b>Hidrostática:</b> ρ_água = 1000 kg/m³ (memorize!)</li>
<li><b>Empuxo:</b> compare densidades para saber se flutua</li>
<li><b>Desenhe diagramas</b> de forças quando necessário</li>
</ol>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto (revisão abrangente) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (TODO o conteúdo!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgd4e021e" class="outline-3">`;

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
