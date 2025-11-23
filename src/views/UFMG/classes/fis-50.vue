<script setup lang="ts">
import { ref } from "vue";

const code = "fis-50";
const title = "Física: Princípio de Pascal, Teorema de Stevin e Princípio de Arquimedes";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-2">
<ul class="org-ul">
<li>Física: Princípio de Pascal, Teorema de Stevin e Princípio de Arquimedes</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgd4e282c" class="outline-4">
<h4 id="orgd4e282c"><span class="section-number-4">3.2.1.</span> Revisão: Hidrostática Básica</h4>
<div class="outline-text-4" id="text-3-2-1">
<p>
<b>Pressão hidrostática (Lei de Stevin):</b>
</p>

<pre class="example" id="orge3d8a1c">
P = ρgh
</pre>

<p>
<b>Pressão total:</b>
</p>

<pre class="example" id="org3d000fc">
P_total = P_atm + ρgh
</pre>
</div>
</div>

<div id="outline-container-orgd0753e8" class="outline-4">
<h4 id="orgd0753e8"><span class="section-number-4">3.2.2.</span> Teorema de Stevin (Aprofundamento)</h4>
<div class="outline-text-4" id="text-3-2-2">
<p>
<b>Enunciado:</b> “A diferença de pressão entre dois pontos de um fluido em equilíbrio é igual ao produto da densidade do fluido pela aceleração da gravidade e pela diferença de profundidade.”
</p>

<pre class="example" id="orgb8ce156">
ΔP = P₂
- P₁ = ρg(h₂
- h₁) = ρgΔh
</pre>

<p>
<b>Consequências:</b>
</p>

<p>
<b>1. Vasos comunicantes:</b>
</p>
<ul class="org-ul">
<li>Líquidos em recipientes conectados ficam no <b>mesmo nível</b></li>
<li>Mesma profundidade → mesma pressão</li>
</ul>

<p>
<b>2. Paradoxo hidrostático:</b>
</p>
<ul class="org-ul">
<li>Pressão <b>não depende</b> da forma do recipiente</li>
<li>Depende apenas de ρ, g, h</li>
</ul>

<p>
<b>Exemplo:</b> Três recipientes com formas diferentes, mesma altura de água (h = 2 m):
</p>
<ul class="org-ul">
<li>Pressão no fundo é a mesma nos três!</li>
<li>P = 1000 × 10 × 2 = 20.000 Pa</li>
</ul>
</div>
</div>

<div id="outline-container-orgd25f649" class="outline-4">
<h4 id="orgd25f649"><span class="section-number-4">3.2.3.</span> Princípio de Pascal</h4>
<div class="outline-text-4" id="text-3-2-3">
<p>
<b>Enunciado:</b> “A pressão aplicada em um ponto de um fluido em equilíbrio transmite-se integralmente a todos os pontos do fluido.”
</p>

<p>
<b>Em outras palavras:</b> Se você aumenta a pressão em um ponto do líquido, <b>todos os pontos</b> sofrem o mesmo aumento de pressão.
</p>

<pre class="example" id="org3547169">
ΔP₁ = ΔP₂ = ΔP₃ = ... = constante
</pre>
</div>
</div>

<div id="outline-container-orgad92f17" class="outline-4">
<h4 id="orgad92f17"><span class="section-number-4">3.2.4.</span> Prensa Hidráulica (Aplicação do Princípio de Pascal)</h4>
<div class="outline-text-4" id="text-3-2-4">
<p>
<b>Princípio:</b> Força pequena aplicada em êmbolo pequeno gera força grande em êmbolo grande.
</p>

<p>
<b>Sistema:</b>
</p>

<pre class="example" id="org4f61ced">
┌───┐         ┌─────────┐
│ F₁│         │   F₂    │
└─┬─┘         └────┬────┘
  │ A₁             │ A₂
──┴────────────────┴────
     Fluido (óleo)
</pre>

<p>
<b>Equação:</b>
</p>

<pre class="example" id="org84d9fc0">
F₁/A₁ = F₂/A₂

ou

F₂ = F₁ × (A₂/A₁)
</pre>

<p>
<b>Ganho mecânico:</b>
</p>

<pre class="example" id="orgb1af4a1">
GM = F₂/F₁ = A₂/A₁
</pre>

<p>
<b>Exemplo:</b> Êmbolo 1: A₁ = 10 cm², F₁ = 50 N Êmbolo 2: A₂ = 100 cm²
</p>

<p>
F₂ = F₁ × (A₂/A₁) = 50 × (100/10) = 50 × 10 = 500 N
</p>

<p>
<b>Ganho:</b> força multiplicada por 10!
</p>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Freios hidráulicos (carros)</li>
<li>Elevadores de postos</li>
<li>Máquinas hidráulicas</li>
<li>Cadeiras de dentista</li>
</ul>

<p>
<b>Importante:</b>
</p>
<ul class="org-ul">
<li>Ganha-se <b>força</b>, mas <b>não se ganha trabalho</b> (energia conservada)</li>
<li>Se êmbolo pequeno desce muito, êmbolo grande sobe pouco</li>
</ul>
</div>
</div>

<div id="outline-container-org4b331f6" class="outline-4">
<h4 id="org4b331f6"><span class="section-number-4">3.2.5.</span> Princípio de Arquimedes (Empuxo)</h4>
<div class="outline-text-4" id="text-3-2-5">
<p>
<b>Enunciado:</b> “Todo corpo mergulhado em um fluido recebe uma força vertical para cima, chamada empuxo, igual ao peso do fluido deslocado.”
</p>

<p>
<b>Empuxo (E):</b>
</p>

<pre class="example" id="orga72207b">
E = ρ_fluido × V_deslocado × g
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>E = empuxo (N)</li>
<li>ρ_fluido = densidade do fluido (kg/m³)</li>
<li>V_deslocado = volume de fluido deslocado (m³)</li>
<li>g = gravidade (m/s²)</li>
</ul>

<p>
<b>Simplificando:</b>
</p>

<pre class="example" id="orgc915b92">
E = m_fluido × g = P_fluido deslocado
</pre>

<p>
<b>“Empuxo = peso do líquido deslocado”</b>
</p>
</div>
</div>

<div id="outline-container-org86f6724" class="outline-4">
<h4 id="org86f6724"><span class="section-number-4">3.2.6.</span> Flutuação (Afunda, Flutua ou Fica em Equilíbrio?)</h4>
<div class="outline-text-4" id="text-3-2-6">
<p>
<b>Forças atuantes:</b>
</p>
<ul class="org-ul">
<li><b>Peso (P):</b> para baixo, P = m_corpo × g</li>
<li><b>Empuxo (E):</b> para cima, E = ρ_fluido × V_des × g</li>
</ul>

<p>
<b>3 Casos:</b>
</p>

<p>
<b>1. Corpo afunda (E &lt; P)</b>
</p>

<pre class="example" id="orgb854013">
ρ_corpo &gt; ρ_fluido
</pre>

<ul class="org-ul">
<li>Exemplo: pedra na água (ρ_pedra &gt; ρ_água)</li>
</ul>

<p>
<b>2. Corpo flutua (E = P, parcialmente imerso)</b>
</p>

<pre class="example" id="org760a929">
ρ_corpo &lt; ρ_fluido
</pre>

<ul class="org-ul">
<li>Exemplo: madeira na água, gelo na água</li>
</ul>

<p>
<b>3. Corpo em equilíbrio (E = P, totalmente imerso)</b>
</p>

<pre class="example" id="org0969f25">
ρ_corpo = ρ_fluido
</pre>

<ul class="org-ul">
<li>Exemplo: submarino em profundidade constante</li>
</ul>

<p>
<b>Por que o gelo flutua?</b>
</p>
<ul class="org-ul">
<li>ρ_gelo = 920 kg/m³</li>
<li>ρ_água = 1000 kg/m³</li>
<li>ρ_gelo &lt; ρ_água → flutua!</li>
<li>~92% do gelo fica submerso</li>
</ul>

<p>
<b>Por que navios de aço flutuam?</b>
</p>
<ul class="org-ul">
<li>ρ_aço &gt; ρ_água (aço afundaria)</li>
<li>Mas navio tem <b>volume oco</b> (ar dentro)</li>
<li>Densidade média do navio &lt; densidade da água</li>
<li>Empuxo &gt; Peso → flutua!</li>
</ul>
</div>
</div>

<div id="outline-container-orgd249059" class="outline-4">
<h4 id="orgd249059"><span class="section-number-4">3.2.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-2-7">
</div>
<div id="outline-container-orgba2087d" class="outline-5">
<h5 id="orgba2087d"><span class="section-number-5">3.2.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-2-7-1">
<p>
Prensa hidráulica com êmbolos de áreas 20 cm² e 100 cm². Aplicando 40 N no menor, qual a força no maior?
</p>

<p>
<b>Solução:</b> F₂ = F₁ × (A₂/A₁) = 40 × (100/20) = 40 × 5 = 200 N
</p>

<p>
<i>[Ver resposta 23 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org418487b" class="outline-5">
<h5 id="org418487b"><span class="section-number-5">3.2.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-2-7-2">
<p>
(UFMG) Um cubo de 8 cm de aresta e densidade 0,6 g/cm³ é colocado na água (ρ = 1 g/cm³). Ele flutua ou afunda?
</p>

<p>
<b>Solução:</b> ρ_cubo = 0,6 g/cm³ &lt; ρ_água = 1 g/cm³ ρ_cubo &lt; ρ_água → <b>flutua</b>
</p>

<p>
Fração submersa: 0,6/1 = 0,6 = 60%
</p>

<p>
<i>[Ver resposta 24 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orge8cb04d" class="outline-5">
<h5 id="orge8cb04d"><span class="section-number-5">3.2.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-2-7-3">
<p>
Um corpo de volume 0,01 m³ está totalmente imerso na água. Qual o empuxo? (ρ_água = 1000 kg/m³, g = 10 m/s²)
</p>

<p>
<b>Solução:</b> E = ρ × V × g = 1000 × 0,01 × 10 = 100 N
</p>

<p>
<i>[Ver resposta 25 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1f1fe7d" class="outline-5">
<h5 id="org1f1fe7d"><span class="section-number-5">3.2.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-2-7-4">
<p>
Uma pedra de 5 kg é mergulhada na água e sofre empuxo de 20 N. Qual a tensão no fio que a suspende?
</p>

<p>
<b>Solução:</b> P = m × g = 5 × 10 = 50 N
</p>

<p>
Equilíbrio: T + E = P T = P
</p>
<ul class="org-ul">
<li>E = 50</li>
<li>20 = 30 N</li>
</ul>

<p>
<i>[Ver resposta 26 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org927e485" class="outline-5">
<h5 id="org927e485"><span class="section-number-5">3.2.7.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-3-2-7-5">
<p>
Dois pontos A e B estão a 3 m e 8 m de profundidade em um lago. Qual a diferença de pressão? (ρ = 1000 kg/m³, g = 10 m/s²)
</p>

<p>
<b>Solução:</b> ΔP = ρgΔh = 1000 × 10 × (8-3) = 1000 × 10 × 5 = 50.000 Pa = 50 kPa
</p>

<p>
<i>[Ver resposta 27 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgddb25ac" class="outline-4">
<h4 id="orgddb25ac"><span class="section-number-4">3.2.8.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-3-2-8">
<p>
<b>Princípio de Pascal:</b>
</p>
<ul class="org-ul">
<li>Freios hidráulicos</li>
<li>Direção hidráulica</li>
<li>Prensas industriais</li>
<li>Macacos hidráulicos</li>
</ul>

<p>
<b>Princípio de Arquimedes:</b>
</p>
<ul class="org-ul">
<li>Navios e barcos</li>
<li>Submarinos (tanques de lastro)</li>
<li>Balões (ar quente menos denso)</li>
<li>Hidrometria (densímetros)</li>
</ul>

<p>
<b>Teorema de Stevin:</b>
</p>
<ul class="org-ul">
<li>Barragens</li>
<li>Caixas d'água</li>
<li>Sistemas de abastecimento</li>
<li>Vasos comunicantes (sifão)</li>
</ul>
</div>
</div>

<div id="outline-container-orgc965f0f" class="outline-4">
<h4 id="orgc965f0f"><span class="section-number-4">3.2.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-2-9">
<ol class="org-ol">
<li><b>Stevin:</b> P = ρgh (pressão não depende da forma)</li>
<li><b>Pascal:</b> pressão transmitida integralmente (prensa hidráulica)</li>
<li><b>Prensa:</b> F₂/F₁ = A₂/A₁ (multiplicador de força)</li>
<li><b>Empuxo:</b> E = ρ_fluido × V_deslocado × g</li>
<li><b>Flutuação:</b> compara ρ_corpo com ρ_fluido</li>
<li><b>Afunda:</b> ρ_corpo &gt; ρ_fluido</li>
<li><b>Flutua:</b> ρ_corpo &lt; ρ_fluido</li>
<li><b>Peso aparente:</b> P_aparente = P</li>
<li>E</li>
</ol>
</div>
</div>

<div id="outline-container-orgbf1c7b2" class="outline-4">
<h4 id="orgbf1c7b2"><span class="section-number-4">3.2.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-2-10">
<p>
<b>Teorema de Stevin:</b>
</p>
<ul class="org-ul">
<li>ΔP = ρgΔh</li>
<li>Mesma profundidade, mesma pressão</li>
<li>Pressão não depende da forma</li>
</ul>

<p>
<b>Princípio de Pascal:</b>
</p>
<ul class="org-ul">
<li>Pressão transmitida integralmente</li>
<li>Prensa hidráulica: F₂/F₁ = A₂/A₁</li>
</ul>

<p>
<b>Princípio de Arquimedes:</b>
</p>
<ul class="org-ul">
<li>Empuxo = peso do fluido deslocado</li>
<li>E = ρ_fluido × V × g</li>
<li>Flutuação: comparar densidades</li>
</ul>
</div>
</div>

<div id="outline-container-org35f50ea" class="outline-4">
<h4 id="org35f50ea"><span class="section-number-4">3.2.11.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-2-11">
<pre class="example" id="org56c5897">
Teorema de Stevin:
P = ρgh
ΔP = ρgΔh

Princípio de Pascal (Prensa Hidráulica):
P₁ = P₂
F₁/A₁ = F₂/A₂
F₂ = F₁ × (A₂/A₁)
Ganho mecânico: GM = A₂/A₁

Princípio de Arquimedes (Empuxo):
E = ρ_fluido × V_deslocado × g
E = m_fluido × g
E = P_fluido deslocado

Flutuação:
- Afunda: ρ_corpo &gt; ρ_fluido (E &lt; P)
- Flutua: ρ_corpo &lt; ρ_fluido (E ≥ P)
- Equilíbrio: ρ_corpo = ρ_fluido (E = P)

Peso Aparente:
P_aparente = P_real
- E

Dados úteis:
ρ_água = 1000 kg/m³ = 1 g/cm³
ρ_gelo = 920 kg/m³
g = 10 m/s²
</pre>
</div>
</div>

<div id="outline-container-org4ff8cf0" class="outline-4">
<h4 id="org4ff8cf0"><span class="section-number-4">3.2.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-3-2-12">
<pre class="example" id="org48a6b9b">
PRENSA HIDRÁULICA:
   F₁ ↓        F₂ ↑
   ┌─┐         ┌───┐
   │ │         │   │
   └┬┘         └─┬─┘
    │A₁          │A₂
────┴───────────┴────
      Fluido
   
F₂/F₁ = A₂/A₁

EMPUXO:
        E ↑
        │
    ┌───┴───┐
    │ Corpo │
    └───┬───┘
        │
        P ↓

E = ρ_fluido × V × g

FLUTUAÇÃO:

Afunda:         Flutua:
  ┌───┐           ≈≈≈
  │   │         ┌─┴─┐
  │ ● │         │ ● │
  └───┘         └───┘
ρ_corpo &gt; ρ_fluido   ρ_corpo &lt; ρ_fluido

VASOS COMUNICANTES:
   │    │
   │ ┌──┴──┐
   └─┤ líq │─┐
     └─────┘ │
        └────┘
  Mesmo nível!
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>conceitos fundamentais + aplicações)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org32443c8" class="outline-3">`;

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
