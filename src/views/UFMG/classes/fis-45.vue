<script setup lang="ts">
import { ref } from "vue";

const code = "fis-45";
const title = "Física: Hidrostática";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-2">
<ul class="org-ul">
<li>Física: Hidrostática</li>
<li>Pressão em Sólidos e Fluidos</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgf367c02" class="outline-4">
<h4 id="orgf367c02"><span class="section-number-4">2.2.1.</span> Introdução à Hidrostática</h4>
<div class="outline-text-4" id="text-2-2-1">
<p>
<b>Hidrostática:</b> parte da Física que estuda os <b>fluidos em repouso</b> (líquidos e gases).
</p>

<p>
<b>Fluido:</b> substância que escoa, não mantém forma própria (líquidos e gases).
</p>

<p>
<b>Por que estudar?</b>
</p>
<ul class="org-ul">
<li>Barragens, submarinos, vasos comunicantes</li>
<li>Prensas hidráulicas, freios de carros</li>
<li>Pressão sanguínea, mergulho</li>
</ul>
</div>
</div>

<div id="outline-container-org28afd23" class="outline-4">
<h4 id="org28afd23"><span class="section-number-4">2.2.2.</span> Conceito de Pressão</h4>
<div class="outline-text-4" id="text-2-2-2">
<p>
<b>Pressão:</b> força por unidade de área
</p>

<pre class="example" id="orgebd835a">
P = F / A
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>P = pressão (Pa ou N/m²)</li>
<li>F = força perpendicular à superfície (N)</li>
<li>A = área (m²)</li>
</ul>

<p>
<b>Unidades:</b>
</p>
<ul class="org-ul">
<li><b>Pascal (Pa):</b> 1 Pa = 1 N/m² (unidade SI)</li>
<li><b>Atmosfera (atm):</b> 1 atm = 101.325 Pa ≈ 10⁵ Pa</li>
<li><b>mmHg:</b> 760 mmHg = 1 atm</li>
<li><b>Bar:</b> 1 bar = 10⁵ Pa</li>
</ul>

<p>
<b>Exemplo:</b> Uma força de 200 N atua sobre uma área de 0,5 m². P = F/A = 200/0,5 = 400 Pa
</p>
</div>
</div>

<div id="outline-container-org80f7efa" class="outline-4">
<h4 id="org80f7efa"><span class="section-number-4">2.2.3.</span> Pressão em Sólidos</h4>
<div class="outline-text-4" id="text-2-2-3">
<p>
<b>Quanto menor a área, maior a pressão!</b>
</p>

<p>
<b>Exemplos práticos:</b>
</p>
<ul class="org-ul">
<li><b>Faca:</b> corta porque área da lâmina é pequena → alta pressão</li>
<li><b>Prego:</b> área da ponta é muito pequena → penetra facilmente</li>
<li><b>Salto agulha:</b> concentra todo peso em área pequena → afunda no chão</li>
<li><b>Esqui:</b> distribui peso em área grande → não afunda na neve</li>
</ul>

<p>
<b>Exemplo:</b> Uma pessoa de 600 N usa sapatos com área total 300 cm². P = F/A = 600 / 0,03 m² = 20.000 Pa
</p>

<p>
Se usar salto agulha (área 2 cm²): P = 600 / 0,0002 = 3.000.000 Pa (150× maior!)
</p>
</div>
</div>

<div id="outline-container-orged8164d" class="outline-4">
<h4 id="orged8164d"><span class="section-number-4">2.2.4.</span> Pressão em Fluidos</h4>
<div class="outline-text-4" id="text-2-2-4">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Fluidos exercem pressão em <b>todas as direções</b></li>
<li>Pressão aumenta com a profundidade</li>
<li>Não depende da forma do recipiente</li>
</ul>
</div>
</div>

<div id="outline-container-org7c86654" class="outline-4">
<h4 id="org7c86654"><span class="section-number-4">2.2.5.</span> Pressão Hidrostática (Pressão de uma Coluna de Líquido)</h4>
<div class="outline-text-4" id="text-2-2-5">
<p>
<b>Lei de Stevin:</b>
</p>

<pre class="example" id="orgd122666">
P = ρ × g × h
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>P = pressão hidrostática (Pa)</li>
<li>ρ (rho) = densidade do líquido (kg/m³)</li>
<li>g = aceleração da gravidade (≈10 m/s²)</li>
<li>h = profundidade (m)</li>
</ul>

<p>
<b>Importante:</b>
</p>
<ul class="org-ul">
<li>Pressão <b>não depende</b> da forma do recipiente</li>
<li>Pressão <b>depende</b> apenas de ρ, g, h</li>
<li>Mesma profundidade → mesma pressão</li>
</ul>

<p>
<b>Exemplo:</b> Pressão no fundo de uma piscina de 3 m de profundidade (água: ρ = 1000 kg/m³).
</p>

<p>
P = ρ × g × h P = 1000 × 10 × 3 P = 30.000 Pa = 30 kPa
</p>
</div>
</div>

<div id="outline-container-orgcbe2912" class="outline-4">
<h4 id="orgcbe2912"><span class="section-number-4">2.2.6.</span> Pressão Total (Pressão Absoluta)</h4>
<div class="outline-text-4" id="text-2-2-6">
<p>
<b>Pressão total = Pressão atmosférica + Pressão hidrostática</b>
</p>

<pre class="example" id="orgc33b4fd">
P_total = P_atm + ρ × g × h
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>P_atm = pressão atmosférica (≈ 10⁵ Pa ao nível do mar)</li>
</ul>

<p>
<b>Exemplo:</b> Pressão total a 3 m de profundidade na piscina: P_total = 100.000 + 30.000 = 130.000 Pa = 130 kPa
</p>
</div>
</div>

<div id="outline-container-org284e37d" class="outline-4">
<h4 id="org284e37d"><span class="section-number-4">2.2.7.</span> Densidade</h4>
<div class="outline-text-4" id="text-2-2-7">
<p>
<b>Densidade:</b> massa por unidade de volume
</p>

<pre class="example" id="org71254be">
ρ = m / V
</pre>

<p>
<b>Unidade SI:</b> kg/m³
</p>

<p>
<b>Densidades importantes:</b>
</p>

<pre class="example" id="org7801e09">
Água: ρ = 1000 kg/m³ = 1 g/cm³
Mercúrio: ρ = 13.600 kg/m³
Álcool: ρ = 800 kg/m³
Gelo: ρ = 920 kg/m³ (menos que água!)
Óleo: ρ = 900 kg/m³
Ar: ρ = 1,3 kg/m³
</pre>

<p>
<b>Exemplo:</b> Um bloco de 2 kg tem volume 0,001 m³ (1 litro). ρ = m/V = 2 / 0,001 = 2000 kg/m³
</p>
</div>
</div>

<div id="outline-container-orge11abdb" class="outline-4">
<h4 id="orge11abdb"><span class="section-number-4">2.2.8.</span> Pressão Atmosférica</h4>
<div class="outline-text-4" id="text-2-2-8">
<p>
<b>Pressão atmosférica:</b> pressão exercida pela coluna de ar da atmosfera.
</p>

<p>
<b>Ao nível do mar:</b>
</p>

<pre class="example" id="org2274174">
P_atm = 101.325 Pa ≈ 1 atm ≈ 10⁵ Pa
P_atm = 760 mmHg
</pre>

<p>
<b>Experiência de Torricelli:</b>
</p>
<ul class="org-ul">
<li>Tubo invertido com mercúrio</li>
<li>Coluna de Hg sobe 76 cm ao nível do mar</li>
<li>P_atm = ρ_Hg × g × h = 13.600 × 10 × 0,76 = 103.360 Pa ≈ 1 atm</li>
</ul>

<p>
<b>Altitude:</b>
</p>
<ul class="org-ul">
<li>Quanto maior a altitude, menor a pressão atmosférica</li>
<li>No topo do Everest: P ≈ 0,3 atm</li>
</ul>
</div>
</div>

<div id="outline-container-orgde0cd2a" class="outline-4">
<h4 id="orgde0cd2a"><span class="section-number-4">2.2.9.</span> Teorema de Stevin</h4>
<div class="outline-text-4" id="text-2-2-9">
<p>
<b>“Pontos em um mesmo líquido, na mesma profundidade, têm a mesma pressão.”</b>
</p>

<p>
<b>Consequência: Vasos Comunicantes</b>
</p>
<ul class="org-ul">
<li>Líquidos em recipientes comunicantes ficam na mesma altura</li>
<li>Exemplo: sistema de esgoto, caixa d'água</li>
</ul>
</div>
</div>

<div id="outline-container-orgfb7913f" class="outline-4">
<h4 id="orgfb7913f"><span class="section-number-4">2.2.10.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-2-10">
</div>
<div id="outline-container-org2a2091a" class="outline-5">
<h5 id="org2a2091a"><span class="section-number-5">2.2.10.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-2-10-1">
<p>
Calcule a pressão exercida por uma força de 500 N sobre uma área de 2 m².
</p>

<p>
<b>Solução:</b> P = F/A = 500/2 = 250 Pa
</p>

<p>
<i>[Ver resposta 6 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgfac8df8" class="outline-5">
<h5 id="orgfac8df8"><span class="section-number-5">2.2.10.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-2-10-2">
<p>
Qual a pressão hidrostática a 5 m de profundidade na água? (ρ = 1000 kg/m³, g = 10 m/s²)
</p>

<p>
<b>Solução:</b> P = ρ × g × h P = 1000 × 10 × 5 P = 50.000 Pa = 50 kPa
</p>

<p>
<i>[Ver resposta 7 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1fa4d30" class="outline-5">
<h5 id="org1fa4d30"><span class="section-number-5">2.2.10.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-2-10-3">
<p>
(UFMG) A pressão total a 10 m de profundidade em um lago é aproximadamente: (Dados: P_atm = 10⁵ Pa, ρ_água = 1000 kg/m³, g = 10 m/s²)
</p>

<p>
<b>Solução:</b> P_hidrostática = ρ × g × h = 1000 × 10 × 10 = 100.000 Pa P_total = P_atm + P_hidrostática = 100.000 + 100.000 = 200.000 Pa = 2 × 10⁵ Pa
</p>

<p>
<i>[Ver resposta 8 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orge730d64" class="outline-5">
<h5 id="orge730d64"><span class="section-number-5">2.2.10.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-2-10-4">
<p>
Um cubo de 8 kg e aresta 0,2 m está apoiado sobre uma mesa. Qual a pressão sobre a mesa?
</p>

<p>
<b>Solução:</b> F = P = m × g = 8 × 10 = 80 N A = lado² = (0,2)² = 0,04 m² P = F/A = 80/0,04 = 2000 Pa
</p>

<p>
<i>[Ver resposta 9 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgdf90c2e" class="outline-5">
<h5 id="orgdf90c2e"><span class="section-number-5">2.2.10.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-2-10-5">
<p>
Mergulhadores não devem subir rapidamente. Por quê?
</p>

<p>
<b>Solução:</b> Na profundidade, a pressão é alta. O nitrogênio do ar se dissolve no sangue. Ao subir rapidamente, a pressão diminui bruscamente e o nitrogênio forma bolhas no sangue (doença de descompressão ou embolia).
</p>

<p>
<i>[Ver resposta 10 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org110780a" class="outline-4">
<h4 id="org110780a"><span class="section-number-4">2.2.11.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-2-2-11">
<p>
<b>1. Barragens:</b>
</p>
<ul class="org-ul">
<li>Mais espessas na base (maior pressão)</li>
<li>P aumenta com h</li>
</ul>

<p>
<b>2. Mergulho:</b>
</p>
<ul class="org-ul">
<li>A cada 10 m, pressão aumenta ≈1 atm</li>
<li>Submarinos precisam ser muito resistentes</li>
</ul>

<p>
<b>3. Caixa d'água:</b>
</p>
<ul class="org-ul">
<li>Instalada no alto para gerar pressão</li>
<li>Quanto mais alta, maior a pressão nas torneiras</li>
</ul>

<p>
<b>4. Vasos comunicantes:</b>
</p>
<ul class="org-ul">
<li>Esgoto, níveis de água</li>
<li>Princípio da mangueira de nível</li>
</ul>
</div>
</div>

<div id="outline-container-orgd40603b" class="outline-4">
<h4 id="orgd40603b"><span class="section-number-4">2.2.12.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-2-12">
<ol class="org-ol">
<li><b>Pressão em sólidos:</b> P = F/A</li>
<li><b>Pressão hidrostática:</b> P = ρgh</li>
<li><b>Pressão total:</b> P_total = P_atm + ρgh</li>
<li><b>Mesma profundidade → mesma pressão</b></li>
<li><b>Pressão não depende da forma do recipiente</b></li>
<li><b>Densidade da água:</b> 1000 kg/m³</li>
<li><b>P_atm ≈ 10⁵ Pa ≈ 1 atm</b></li>
<li><b>Unidades:</b> sempre converter para SI</li>
</ol>
</div>
</div>

<div id="outline-container-orga240d0a" class="outline-4">
<h4 id="orga240d0a"><span class="section-number-4">2.2.13.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-2-13">
<p>
<b>Pressão:</b>
</p>
<ul class="org-ul">
<li>Força por área: P = F/A</li>
<li>Unidade SI: Pascal (Pa)</li>
</ul>

<p>
<b>Pressão Hidrostática:</b>
</p>
<ul class="org-ul">
<li>P = ρgh (não depende da forma)</li>
<li>Aumenta com profundidade</li>
</ul>

<p>
<b>Densidade:</b>
</p>
<ul class="org-ul">
<li>ρ = m/V</li>
<li>Água: 1000 kg/m³</li>
</ul>

<p>
<b>Teorema de Stevin:</b>
</p>
<ul class="org-ul">
<li>Mesma profundidade, mesma pressão</li>
<li>Vasos comunicantes: líquidos na mesma altura</li>
</ul>
</div>
</div>

<div id="outline-container-orgf74007b" class="outline-4">
<h4 id="orgf74007b"><span class="section-number-4">2.2.14.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-2-14">
<pre class="example" id="org9afa669">
Pressão:
P = F / A

Pressão Hidrostática (Lei de Stevin):
P = ρ × g × h

Pressão Total:
P_total = P_atm + ρ × g × h

Densidade:
ρ = m / V

Conversões:
1 atm = 101.325 Pa ≈ 10⁵ Pa
1 atm = 760 mmHg
1 bar = 10⁵ Pa

Densidades:
ρ_água = 1000 kg/m³
ρ_Hg = 13.600 kg/m³
g = 10 m/s² (Terra)
</pre>
</div>
</div>

<div id="outline-container-orge128f22" class="outline-4">
<h4 id="orge128f22"><span class="section-number-4">2.2.15.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-2-2-15">
<pre class="example" id="org78429b5">
PRESSÃO EM SÓLIDOS:
  F ↓
 ┌───┐
 │   │  P = F/A
 └───┘
  A

PRESSÃO EM FLUIDOS:
    ← → Pressão em
  ↑     todas direções
  ↓

PRESSÃO HIDROSTÁTICA:
       P_atm
  ┌─────────┐
  │  água   │
  │    h    │  P = ρgh
  │         │
  └─────────┘
  P_total = P_atm + ρgh

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
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>conceitos fundamentais)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org54bb7ed" class="outline-3">`;

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
