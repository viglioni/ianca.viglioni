<script setup lang="ts">
import { ref } from "vue";

const code = "fis-54";
const title = "Física: Princípio de Arquimedes Aprofundado e Teorema de Torricelli";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-2">
<ul class="org-ul">
<li>Física: Princípio de Arquimedes Aprofundado e Teorema de Torricelli</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgac4da88" class="outline-4">
<h4 id="orgac4da88"><span class="section-number-4">4.2.1.</span> Revisão: Princípio de Arquimedes</h4>
<div class="outline-text-4" id="text-4-2-1">
<p>
<b>Enunciado:</b> “Todo corpo mergulhado em um fluido recebe uma força vertical para cima (empuxo) igual ao peso do fluido deslocado.”
</p>

<pre class="example" id="org73a8b77">
E = ρ_fluido × V_deslocado × g
</pre>
</div>
</div>

<div id="outline-container-org2a067ac" class="outline-4">
<h4 id="org2a067ac"><span class="section-number-4">4.2.2.</span> Casos de Flutuação</h4>
<div class="outline-text-4" id="text-4-2-2">
<ul class="org-ul">
<li>Aprofundamento</li>
</ul>
<p>
<b>Forças atuantes:</b>
</p>
<ul class="org-ul">
<li><b>Peso (P):</b> P = m_corpo × g = ρ_corpo × V_corpo × g</li>
<li><b>Empuxo (E):</b> E = ρ_fluido × V_deslocado × g</li>
</ul>

<p>
<b>1. Corpo totalmente imerso:</b>
</p>

<p>
<b>a) Afunda (acelera para baixo):</b>
</p>

<pre class="example" id="org57c4387">
P &gt; E
ρ_corpo &gt; ρ_fluido
</pre>

<p>
<b>b) Sobe (acelera para cima):</b>
</p>

<pre class="example" id="orgd6cf6d4">
P &lt; E
ρ_corpo &lt; ρ_fluido
</pre>

<p>
<b>c) Equilíbrio (fica parado):</b>
</p>

<pre class="example" id="orgbba10ae">
P = E
ρ_corpo = ρ_fluido
</pre>

<p>
<b>2. Corpo parcialmente imerso (flutuando):</b>
</p>

<pre class="example" id="org83a8f2d">
P = E
ρ_corpo &lt; ρ_fluido
</pre>

<p>
<b>Fração submersa:</b>
</p>

<pre class="example" id="orga06a1e7">
f = V_submerso / V_total = ρ_corpo / ρ_fluido
</pre>

<p>
<b>Exemplo:</b> Gelo (ρ = 920 kg/m³) na água (ρ = 1000 kg/m³): f = 920/1000 = 0,92 = 92% submerso
</p>
</div>
</div>

<div id="outline-container-org59455bd" class="outline-4">
<h4 id="org59455bd"><span class="section-number-4">4.2.3.</span> Peso Aparente</h4>
<div class="outline-text-4" id="text-4-2-3">
<p>
<b>Peso aparente:</b> força que o corpo parece ter quando imerso
</p>

<pre class="example" id="orgb315a82">
P_aparente = P_real
- E
</pre>

<p>
<b>Consequências:</b>
</p>
<ul class="org-ul">
<li>Objetos “pesam menos” dentro d'água</li>
<li>Quanto maior o empuxo, menor o peso aparente</li>
<li>Se E = P, peso aparente = 0 (flutuação)</li>
<li>Se E &gt; P, peso aparente é negativo (tende a subir)</li>
</ul>

<p>
<b>Exemplo:</b> Pedra de 100 N no ar sofre empuxo de 30 N na água. P_aparente = 100
</p>
<ul class="org-ul">
<li>30 = 70 N</li>
</ul>

<p>
“Pesa” apenas 70 N dentro d'água!
</p>
</div>
</div>

<div id="outline-container-orgfa457f5" class="outline-4">
<h4 id="orgfa457f5"><span class="section-number-4">4.2.4.</span> Densidade e Flutuação</h4>
<div class="outline-text-4" id="text-4-2-4">
<p>
<b>Densidade relativa:</b>
</p>

<pre class="example" id="org0d1e50e">
d = ρ_substância / ρ_água
</pre>

<p>
<b>Se d &lt; 1:</b> flutua na água <b>Se d = 1:</b> equilíbrio na água <b>Se d &gt; 1:</b> afunda na água
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Madeira: d ≈ 0,6 → flutua</li>
<li>Gelo: d = 0,92 → flutua</li>
<li>Ferro: d ≈ 7,8 → afunda</li>
<li>Chumbo: d ≈ 11,3 → afunda</li>
<li>Óleo: d ≈ 0,9 → flutua sobre água</li>
</ul>
</div>
</div>

<div id="outline-container-orga7de30d" class="outline-4">
<h4 id="orga7de30d"><span class="section-number-4">4.2.5.</span> Aplicações do Princípio de Arquimedes</h4>
<div class="outline-text-4" id="text-4-2-5">
<p>
<b>1. Submarinos:</b>
</p>
<ul class="org-ul">
<li><b>Tanques de lastro:</b> enchem com água para afundar, esvaziam para subir</li>
<li>Subir: expulsam água → diminui massa → diminui peso → E &gt; P</li>
<li>Afundar: enchem com água → aumenta massa → aumenta peso → P &gt; E</li>
</ul>

<p>
<b>2. Balões e dirigíveis:</b>
</p>
<ul class="org-ul">
<li>Usam gases menos densos que o ar (hélio, ar quente)</li>
<li>ρ_gás &lt; ρ_ar → empuxo levanta o balão</li>
</ul>

<p>
<b>3. Densímetro:</b>
</p>
<ul class="org-ul">
<li>Mede densidade de líquidos</li>
<li>Quanto mais denso o líquido, menos o densímetro afunda</li>
</ul>

<p>
<b>4. Icebergs:</b>
</p>
<ul class="org-ul">
<li>92% submersos, apenas 8% visíveis</li>
<li>Perigo para navegação!</li>
</ul>
</div>
</div>

<div id="outline-container-org521235f" class="outline-4">
<h4 id="org521235f"><span class="section-number-4">4.2.6.</span> Teorema de Torricelli (Escoamento de Fluidos)</h4>
<div class="outline-text-4" id="text-4-2-6">
<p>
<b>Enunciado:</b> “A velocidade de saída de um fluido por um orifício em um recipiente é a mesma que um corpo teria se caísse livremente da altura da superfície do líquido até o orifício.”
</p>

<pre class="example" id="org5930d05">
v = √(2gh)
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>v = velocidade de saída (m/s)</li>
<li>g = gravidade (m/s²)</li>
<li>h = altura da coluna de líquido acima do orifício (m)</li>
</ul>

<p>
<b>Observações:</b>
</p>
<ul class="org-ul">
<li>Fórmula idêntica à queda livre!</li>
<li>v não depende da densidade do líquido</li>
<li>v aumenta com h (quanto maior a altura, maior a velocidade)</li>
</ul>

<p>
<b>Exemplo:</b> Orifício a 5 m abaixo da superfície: v = √(2 × 10 × 5) = √100 = 10 m/s
</p>
</div>
</div>

<div id="outline-container-orgdc50ec1" class="outline-4">
<h4 id="orgdc50ec1"><span class="section-number-4">4.2.7.</span> Vazão (Taxa de Escoamento)</h4>
<div class="outline-text-4" id="text-4-2-7">
<p>
<b>Vazão (Q):</b> volume de fluido que atravessa uma seção por unidade de tempo
</p>

<pre class="example" id="org971ec05">
Q = A × v
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>Q = vazão (m³/s ou L/s)</li>
<li>A = área do orifício (m²)</li>
<li>v = velocidade de saída (m/s)</li>
</ul>

<p>
<b>Combinando com Torricelli:</b>
</p>

<pre class="example" id="orga839f9a">
Q = A × √(2gh)
</pre>

<p>
<b>Exemplo:</b> Orifício circular de raio 2 cm (área = πr² = 3,14 × 0,02² = 0,001256 m²) a 5 m de profundidade: v = √(2 × 10 × 5) = 10 m/s Q = 0,001256 × 10 = 0,01256 m³/s = 12,56 L/s
</p>
</div>
</div>

<div id="outline-container-org5a32863" class="outline-4">
<h4 id="org5a32863"><span class="section-number-4">4.2.8.</span> Equação da Continuidade</h4>
<div class="outline-text-4" id="text-4-2-8">
<p>
<b>Para fluido incompressível (líquido):</b>
</p>

<p>
“A vazão é constante em todas as seções do tubo”
</p>

<pre class="example" id="orgc9e84d5">
A₁ × v₁ = A₂ × v₂ = Q
</pre>

<p>
<b>Consequência:</b>
</p>
<ul class="org-ul">
<li>Tubo estreito → velocidade alta</li>
<li>Tubo largo → velocidade baixa</li>
</ul>

<p>
<b>Exemplo:</b> Mangueira com A₁ = 4 cm², v₁ = 2 m/s Bico com A₂ = 1 cm²
</p>

<p>
A₁v₁ = A₂v₂ 4 × 2 = 1 × v₂ v₂ = 8 m/s
</p>

<p>
Velocidade quadruplica!
</p>
</div>
</div>

<div id="outline-container-org4033934" class="outline-4">
<h4 id="org4033934"><span class="section-number-4">4.2.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-2-9">
</div>
<div id="outline-container-org6a3e56d" class="outline-5">
<h5 id="org6a3e56d"><span class="section-number-5">4.2.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-2-9-1">
<p>
Um bloco de 2 kg e volume 0,002 m³ é mergulhado totalmente na água. Ele afunda ou sobe? (ρ_água = 1000 kg/m³, g = 10 m/s²)
</p>

<p>
<b>Solução:</b> P = m × g = 2 × 10 = 20 N E = ρ × V × g = 1000 × 0,002 × 10 = 20 N
</p>

<p>
E = P → <b>equilíbrio</b> (fica parado no lugar onde for solto)
</p>

<p>
ρ_corpo = m/V = 2/0,002 = 1000 kg/m³ = ρ_água
</p>

<p>
<i>[Ver resposta 43 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org6c8b3fc" class="outline-5">
<h5 id="org6c8b3fc"><span class="section-number-5">4.2.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-2-9-2">
<p>
Um cubo de madeira (ρ = 600 kg/m³) flutua na água. Qual fração fica submersa?
</p>

<p>
<b>Solução:</b> f = ρ_madeira / ρ_água = 600/1000 = 0,6 = 60%
</p>

<p>
<i>[Ver resposta 44 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgffbff52" class="outline-5">
<h5 id="orgffbff52"><span class="section-number-5">4.2.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-2-9-3">
<p>
Uma pedra de 50 N no ar “pesa” 40 N dentro d'água. Qual o empuxo?
</p>

<p>
<b>Solução:</b> P_aparente = P_real
</p>
<ul class="org-ul">
<li>E 40 = 50</li>
<li>E E = 10 N</li>
</ul>

<p>
<i>[Ver resposta 45 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb836b5d" class="outline-5">
<h5 id="orgb836b5d"><span class="section-number-5">4.2.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-2-9-4">
<p>
(UFMG) Um tanque tem um orifício a 3,2 m abaixo da superfície da água. Qual a velocidade de saída?
</p>

<p>
<b>Solução:</b> v = √(2gh) = √(2 × 10 × 3,2) = √64 = 8 m/s
</p>

<p>
<i>[Ver resposta 46 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org6c4610a" class="outline-5">
<h5 id="org6c4610a"><span class="section-number-5">4.2.9.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-4-2-9-5">
<p>
Um iceberg tem volume total de 1000 m³. Qual o volume emerso? (ρ_gelo = 920 kg/m³, ρ_água do mar = 1025 kg/m³)
</p>

<p>
<b>Solução:</b> f_submerso = ρ_gelo / ρ_água = 920/1025 ≈ 0,898 = 89,8%
</p>

<p>
V_submerso = 0,898 × 1000 = 898 m³ V_emerso = 1000
</p>
<ul class="org-ul">
<li>898 = 102 m³</li>
</ul>

<p>
<i>[Ver resposta 47 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org075f960" class="outline-5">
<h5 id="org075f960"><span class="section-number-5">4.2.9.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-4-2-9-6">
<p>
Um objeto de 8 kg tem volume 0,01 m³. Qual seu peso aparente na água?
</p>

<p>
<b>Solução:</b> P = m × g = 8 × 10 = 80 N E = ρ × V × g = 1000 × 0,01 × 10 = 100 N
</p>

<p>
P_aparente = P
</p>
<ul class="org-ul">
<li>E = 80</li>
<li>100 = -20 N</li>
</ul>

<p>
Negativo! Objeto sobe (tende a flutuar).
</p>

<p>
<i>[Ver resposta 48 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org8cccb14" class="outline-4">
<h4 id="org8cccb14"><span class="section-number-4">4.2.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-2-10">
<ol class="org-ol">
<li><b>Empuxo:</b> E = ρ_fluido × V_deslocado × g</li>
<li><b>Flutuação:</b> comparar ρ_corpo com ρ_fluido</li>
<li><b>Afunda:</b> ρ_corpo &gt; ρ_fluido</li>
<li><b>Flutua:</b> ρ_corpo &lt; ρ_fluido</li>
<li><b>Fração submersa:</b> f = ρ_corpo / ρ_fluido</li>
<li><b>Peso aparente:</b> P_ap = P</li>
<li>E</li>
<li><b>Torricelli:</b> v = √(2gh)</li>
<li><b>Vazão:</b> Q = A × v</li>
<li><b>Continuidade:</b> A₁v₁ = A₂v₂</li>
</ol>
</div>
</div>

<div id="outline-container-orgbf57bef" class="outline-4">
<h4 id="orgbf57bef"><span class="section-number-4">4.2.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-2-11">
<p>
<b>Arquimedes:</b>
</p>
<ul class="org-ul">
<li>Empuxo = peso do fluido deslocado</li>
<li>E = ρ_fluido × V × g</li>
<li>Flutuação: comparar densidades</li>
</ul>

<p>
<b>Peso Aparente:</b>
</p>
<ul class="org-ul">
<li>P_aparente = P_real</li>
<li>E</li>
<li>Objetos “pesam menos” na água</li>
</ul>

<p>
<b>Torricelli:</b>
</p>
<ul class="org-ul">
<li>v = √(2gh)</li>
<li>Velocidade de saída independe de ρ</li>
<li>Depende apenas de h</li>
</ul>

<p>
<b>Vazão:</b>
</p>
<ul class="org-ul">
<li>Q = A × v</li>
<li>A₁v₁ = A₂v₂ (continuidade)</li>
</ul>
</div>
</div>

<div id="outline-container-org3323011" class="outline-4">
<h4 id="org3323011"><span class="section-number-4">4.2.12.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-2-12">
<pre class="example" id="org39ee59c">
Princípio de Arquimedes:
E = ρ_fluido × V_deslocado × g

Flutuação:
ρ_corpo &gt; ρ_fluido → afunda
ρ_corpo &lt; ρ_fluido → flutua
ρ_corpo = ρ_fluido → equilíbrio

Fração submersa (corpo flutuando):
f = V_submerso / V_total = ρ_corpo / ρ_fluido

Peso Aparente:
P_aparente = P_real
- E

Teorema de Torricelli:
v = √(2gh)

Vazão:
Q = A × v
Q = A × √(2gh)

Equação da Continuidade:
A₁ × v₁ = A₂ × v₂

Dados úteis:
ρ_água = 1000 kg/m³
ρ_gelo = 920 kg/m³
ρ_água do mar ≈ 1025 kg/m³
g = 10 m/s²
</pre>
</div>
</div>

<div id="outline-container-org9700136" class="outline-4">
<h4 id="org9700136"><span class="section-number-4">4.2.13.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-2-13">
<pre class="example" id="org9e19ca7">
FLUTUAÇÃO:

Afunda:          Flutua:         Equilíbrio:
  ┌───┐           ≈≈≈              ≈≈≈
  │   │         ┌─┴─┐            ┌─┴─┐
  │ ● │         │ ● │            │ ● │
  └───┘         └───┘            └───┘
   P&gt;E           P=E              P=E
ρ_c &gt; ρ_f     ρ_c &lt; ρ_f        ρ_c = ρ_f

PESO APARENTE:
  Ar:        Água:
   ↓ P        ↓ P
  ┌─┐        ┌─┐ ↑ E
  │●│        │●│
  └─┘        └─┘ ↓ P_ap=P-E

TORRICELLI:
  ═════════  h
      ●───→ v = √(2gh)
      
CONTINUIDADE:
  ████  →  ██  →  ████
  largo    estreito  largo
  v baixa  v alta    v baixa
  
  A₁v₁ = A₂v₂ = constante
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>conceitos fundamentais de hidrostática)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org19686b3" class="outline-3">`;

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
