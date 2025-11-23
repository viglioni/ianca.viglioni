<script setup lang="ts">
import { ref } from "vue";

const code = "fis-66";
const title = "Física: Revisão Final";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-3">
<ul class="org-ul">
<li>Física: Revisão Final</li>
<li>Hidrostática Completa</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgf21d0c1" class="outline-4">
<h4 id="orgf21d0c1"><span class="section-number-4">2.3.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-2-3-1">
<p>
Consolidar todos os conceitos de Hidrostática: pressão, densidade, Stevin, Pascal, Arquimedes e Torricelli.
</p>
</div>
</div>

<div id="outline-container-orgbb9ffb6" class="outline-4">
<h4 id="orgbb9ffb6"><span class="section-number-4">2.3.2.</span> 1. Conceitos Fundamentais</h4>
<div class="outline-text-4" id="text-2-3-2">
<p>
<b>Densidade (ρ):</b>
</p>

<pre class="example" id="org8cee926">
ρ = m/V

Unidades:
kg/m³ (SI)
g/cm³ (comum)

Conversão: 1 g/cm³ = 1000 kg/m³
</pre>

<p>
<b>Dados importantes:</b>
</p>

<pre class="example" id="org8810dac">
ρ_água = 1000 kg/m³ = 1 g/cm³
ρ_gelo = 920 kg/m³ = 0,92 g/cm³
ρ_mercúrio = 13.600 kg/m³ = 13,6 g/cm³
</pre>

<p>
<b>Pressão (P):</b>
</p>

<pre class="example" id="org63890f6">
P = F/A

Unidades:
Pa (pascal) = N/m² (SI)
atm (atmosfera)
mmHg (milímetro de mercúrio)

Conversões:
1 atm = 101.325 Pa ≈ 10⁵ Pa
1 atm = 760 mmHg
</pre>

<p>
<b>Pressão atmosférica:</b>
</p>

<pre class="example" id="org0b2e566">
P_atm ≈ 1 atm = 101.325 Pa
</pre>
</div>
</div>

<div id="outline-container-org46b99a3" class="outline-4">
<h4 id="org46b99a3"><span class="section-number-4">2.3.3.</span> 2. Teorema de Stevin (Lei Fundamental da Hidrostática)</h4>
<div class="outline-text-4" id="text-2-3-3">
<p>
<b>Enunciado:</b> “A diferença de pressão entre dois pontos de um fluido em equilíbrio é igual ao produto da densidade, gravidade e diferença de altura.”
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org1a39ccb">
P = P_atm + ρgh

ou

ΔP = ρgΔh
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>P = pressão total no ponto</li>
<li>P_atm = pressão atmosférica</li>
<li>ρ = densidade do fluido</li>
<li>g = gravidade (10 m/s²)</li>
<li>h = profundidade</li>
</ul>

<p>
<b>Consequências:</b>
</p>

<p>
<b>1. Mesma profundidade, mesma pressão:</b>
</p>
<ul class="org-ul">
<li>Pontos à mesma altura têm mesma pressão</li>
</ul>

<p>
<b>2. Paradoxo hidrostático:</b>
</p>
<ul class="org-ul">
<li>Pressão não depende da forma do recipiente</li>
<li>Depende apenas de ρ, g, h</li>
</ul>

<p>
<b>3. Vasos comunicantes:</b>
</p>
<ul class="org-ul">
<li>Líquido fica no mesmo nível</li>
</ul>

<p>
<b>Exemplo rápido:</b> Pressão a 5 m de profundidade na água:
</p>

<pre class="example" id="org99f252c">
P = P_atm + ρgh
P = 10⁵ + 1000 × 10 × 5
P = 10⁵ + 50.000
P = 150.000 Pa = 1,5 × 10⁵ Pa
</pre>
</div>
</div>

<div id="outline-container-orgedc1450" class="outline-4">
<h4 id="orgedc1450"><span class="section-number-4">2.3.4.</span> 3. Princípio de Pascal</h4>
<div class="outline-text-4" id="text-2-3-4">
<p>
<b>Enunciado:</b> “A variação de pressão aplicada em um ponto de um fluido em equilíbrio transmite-se integralmente a todos os pontos do fluido.”
</p>

<p>
<b>Aplicação: Prensa Hidráulica</b>
</p>

<pre class="example" id="org51caed6">
P₁ = P₂

F₁/A₁ = F₂/A₂

F₂ = F₁ × (A₂/A₁)
</pre>

<p>
<b>Ganho mecânico:</b>
</p>

<pre class="example" id="org0f08d0f">
GM = F₂/F₁ = A₂/A₁
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org896e0ac">
A₁ = 5 cm², F₁ = 20 N
A₂ = 100 cm²

F₂ = 20 × (100/5) = 20 × 20 = 400 N

Ganho de 20 vezes!
</pre>

<p>
<b>Observação importante:</b>
</p>
<ul class="org-ul">
<li>Ganha-se força, mas não energia</li>
<li>Se êmbolo pequeno desce muito, grande sobe pouco</li>
</ul>
</div>
</div>

<div id="outline-container-orgd9ad3e7" class="outline-4">
<h4 id="orgd9ad3e7"><span class="section-number-4">2.3.5.</span> 4. Princípio de Arquimedes (Empuxo)</h4>
<div class="outline-text-4" id="text-2-3-5">
<p>
<b>Enunciado:</b> “Todo corpo mergulhado em um fluido recebe uma força vertical para cima (empuxo) igual ao peso do fluido deslocado.”
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org67e5dab">
E = ρ_fluido × V_deslocado × g

ou

E = m_fluido × g
</pre>

<p>
*Flutuação
</p>
<ul class="org-ul">
<li>Três casos:*</li>
</ul>

<p>
<b>1. Afunda (E &lt; P):</b>
</p>

<pre class="example" id="org91aa44f">
ρ_corpo &gt; ρ_fluido
</pre>

<p>
<b>2. Flutua (E = P):</b>
</p>

<pre class="example" id="org8b0beaf">
ρ_corpo &lt; ρ_fluido

Fração submersa:
f = ρ_corpo / ρ_fluido
</pre>

<p>
<b>3. Equilíbrio (E = P, totalmente imerso):</b>
</p>

<pre class="example" id="orge29bb18">
ρ_corpo = ρ_fluido
</pre>

<p>
<b>Peso aparente:</b>
</p>

<pre class="example" id="orgbe5a4aa">
P_aparente = P_real
- E
</pre>

<p>
*Exemplo
</p>
<ul class="org-ul">
<li>Gelo na água:*</li>
</ul>

<pre class="example" id="org8a7bd54">
ρ_gelo = 920 kg/m³
ρ_água = 1000 kg/m³

f = 920/1000 = 0,92 = 92%

92% do gelo fica submerso
</pre>
</div>
</div>

<div id="outline-container-org308d021" class="outline-4">
<h4 id="org308d021"><span class="section-number-4">2.3.6.</span> 5. Teorema de Torricelli</h4>
<div class="outline-text-4" id="text-2-3-6">
<p>
<b>Enunciado:</b> “A velocidade de saída de um fluido por um orifício é igual à velocidade que um corpo teria em queda livre da altura h.”
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgaae9eb3">
v = √(2gh)
</pre>

<p>
<b>Vazão:</b>
</p>

<pre class="example" id="org5ba6ead">
Q = A × v = A × √(2gh)

Unidade: m³/s ou L/s
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org6099559">
Orifício a h = 5 m de profundidade:
v = √(2 × 10 × 5) = √100 = 10 m/s
</pre>
</div>
</div>

<div id="outline-container-org8e5d67f" class="outline-4">
<h4 id="org8e5d67f"><span class="section-number-4">2.3.7.</span> Questões de Fixação Rápida</h4>
<div class="outline-text-4" id="text-2-3-7">
</div>
<div id="outline-container-org66d1865" class="outline-5">
<h5 id="org66d1865"><span class="section-number-5">2.3.7.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-2-3-7-1">
<p>
Calcule a pressão a 10 m de profundidade na água.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgfaefc2f">
P = ρgh = 1000 × 10 × 10 = 100.000 Pa = 10⁵ Pa
</pre>
</div>
</div>

<div id="outline-container-org732020c" class="outline-5">
<h5 id="org732020c"><span class="section-number-5">2.3.7.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-2-3-7-2">
<p>
Prensa hidráulica: A₁ = 10 cm², A₂ = 50 cm², F₁ = 30 N. Calcule F₂.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgb80b937">
F₂ = 30 × (50/10) = 30 × 5 = 150 N
</pre>
</div>
</div>

<div id="outline-container-org25686dc" class="outline-5">
<h5 id="org25686dc"><span class="section-number-5">2.3.7.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-2-3-7-3">
<p>
Um cubo de 8 cm de aresta e densidade 0,7 g/cm³ é colocado na água. Ele afunda ou flutua? Qual porcentagem fica submersa?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org4715c17">
ρ_cubo = 0,7 g/cm³ &lt; ρ_água = 1 g/cm³
Flutua!
f = 0,7/1 = 0,7 = 70% submerso
</pre>
</div>
</div>

<div id="outline-container-org54defd9" class="outline-5">
<h5 id="org54defd9"><span class="section-number-5">2.3.7.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-2-3-7-4">
<p>
Uma pedra de 80 N no ar “pesa” 50 N dentro d'água. Qual o empuxo?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org14270e4">
P_aparente = P_real
- E
50 = 80
- E
E = 30 N
</pre>
</div>
</div>

<div id="outline-container-orgc9cdce8" class="outline-5">
<h5 id="orgc9cdce8"><span class="section-number-5">2.3.7.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-2-3-7-5">
<p>
Qual a velocidade de saída de água por um orifício a 3,2 m de profundidade?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgaa067a0">
v = √(2gh) = √(2 × 10 × 3,2) = √64 = 8 m/s
</pre>
</div>
</div>
</div>

<div id="outline-container-org9174a88" class="outline-4">
<h4 id="org9174a88"><span class="section-number-4">2.3.8.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-3-8">
<ul class="org-ul">
<li>Resumo Completo</li>
</ul>
<pre class="example" id="orga099726">
DENSIDADE:
ρ = m/V

PRESSÃO:
P = F/A

STEVIN:
P = P_atm + ρgh
ΔP = ρgΔh

PASCAL (Prensa Hidráulica):
F₁/A₁ = F₂/A₂
F₂ = F₁ × (A₂/A₁)

ARQUIMEDES (Empuxo):
E = ρ_fluido × V_deslocado × g
E = m_fluido × g

Flutuação:
- Afunda: ρ_corpo &gt; ρ_fluido
- Flutua: ρ_corpo &lt; ρ_fluido
- Fração submersa: f = ρ_corpo/ρ_fluido

Peso aparente:
P_aparente = P_real
- E

TORRICELLI:
v = √(2gh)

Vazão:
Q = A × v

DADOS:
ρ_água = 1000 kg/m³ = 1 g/cm³
g = 10 m/s²
P_atm = 10⁵ Pa
</pre>
</div>
</div>

<div id="outline-container-org5ef030c" class="outline-4">
<h4 id="org5ef030c"><span class="section-number-4">2.3.9.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-2-3-9">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei calcular densidade</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular pressão hidrostática (Stevin)</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver problemas de prensa hidráulica (Pascal)</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular empuxo</li>
<li class="off"><code>[&#xa0;]</code> Sei determinar se um corpo flutua ou afunda</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular fração submersa</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular peso aparente</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar Torricelli</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular vazão</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgbc4db02" class="outline-3">`;

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
