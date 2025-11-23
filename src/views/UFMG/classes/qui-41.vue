<script setup lang="ts">
import { ref } from "vue";

const code = "qui-41";
const title = "Química: Propriedades das Substâncias Segundo Ligações";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-7-2">
<ul class="org-ul">
<li>Química: Propriedades das Substâncias Segundo Ligações</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-orgdc35327" class="outline-4">
<h4 id="orgdc35327"><span class="section-number-4">7.2.1.</span> Revisão: Ligações Químicas</h4>
<div class="outline-text-4" id="text-7-2-1">
<p>
Já estudamos os três tipos principais:
</p>
<ul class="org-ul">
<li><b>Aula 31:</b> Ligação Iônica (metal + não-metal, íons)</li>
<li><b>Aula 33:</b> Ligação Covalente (não-metal + não-metal, moléculas)</li>
<li><b>Aula 35:</b> Ligação Metálica (metais, mar de elétrons)</li>
</ul>

<p>
<b>Nesta aula:</b> Como o tipo de ligação determina as propriedades das substâncias.
</p>
</div>
</div>

<div id="outline-container-orgc4b108d" class="outline-4">
<h4 id="orgc4b108d"><span class="section-number-4">7.2.2.</span> Propriedades dos Compostos Iônicos</h4>
<div class="outline-text-4" id="text-7-2-2">
<p>
<b>Exemplos:</b> NaCl, CaO, MgCl₂, K₂SO₄
</p>
</div>

<div id="outline-container-org8d252f0" class="outline-5">
<h5 id="org8d252f0"><span class="section-number-5">7.2.2.1.</span> Características Físicas</h5>
<div class="outline-text-5" id="text-7-2-2-1">
<p>
<b>1. Estado Físico:</b>
</p>
<ul class="org-ul">
<li><b>Sólidos</b> à temperatura ambiente</li>
<li>Formam cristais (retículo cristalino ordenado)</li>
</ul>

<p>
<b>2. Pontos de Fusão e Ebulição:</b>
</p>
<ul class="org-ul">
<li><b>Muito altos</b></li>
<li>Fortes atrações eletrostáticas entre íons</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>NaCl: PF = 801°C</li>
<li>MgO: PF = 2852°C</li>
</ul>

<p>
<b>3. Dureza:</b>
</p>
<ul class="org-ul">
<li><b>Duros</b> (resistem a deformação)</li>
<li><b>Quebradiços</b> (fraturam ao invés de deformar)</li>
</ul>
</div>
</div>

<div id="outline-container-orgb50fbf8" class="outline-5">
<h5 id="orgb50fbf8"><span class="section-number-5">7.2.2.2.</span> Condutividade Elétrica</h5>
<div class="outline-text-5" id="text-7-2-2-2">
<p>
<b>Sólidos:</b> NÃO conduzem
</p>
<ul class="org-ul">
<li>Íons fixos no retículo, não se movem</li>
</ul>

<p>
<b>Fundidos (líquidos):</b> CONDUZEM
</p>
<ul class="org-ul">
<li>Íons livres para se mover</li>
</ul>

<p>
<b>Dissolvidos em água:</b> CONDUZEM
</p>
<ul class="org-ul">
<li>Íons dispersos na solução, móveis</li>
</ul>

<p>
<b>Resumo:</b>
</p>

<pre class="example" id="org5ee33ac">
Iônico sólido: NÃO conduz
Iônico fundido/dissolvido: CONDUZ
</pre>
</div>
</div>

<div id="outline-container-orgf1f4ed5" class="outline-5">
<h5 id="orgf1f4ed5"><span class="section-number-5">7.2.2.3.</span> Solubilidade</h5>
<div class="outline-text-5" id="text-7-2-2-3">
<p>
<b>Em água (polar):</b> Geralmente <b>solúveis</b>
</p>
<ul class="org-ul">
<li>“Semelhante dissolve semelhante”</li>
<li>Compostos iônicos são polares</li>
<li>Íons se dispersam na água</li>
</ul>

<p>
<b>Em solventes apolares:</b> <b>Insolúveis</b>
</p>
<ul class="org-ul">
<li>Gasolina, benzeno, etc.</li>
</ul>

<p>
<b>Regras de solubilidade (principais):</b>
</p>
<ul class="org-ul">
<li>Sais de Na⁺, K⁺, NH₄⁺: sempre solúveis</li>
<li>Nitratos (NO₃⁻): sempre solúveis</li>
<li>Cloretos, brometos, iodetos: geralmente solúveis (exceto Ag⁺, Pb²⁺)</li>
<li>Sulfatos: geralmente solúveis (exceto Ba²⁺, Pb²⁺)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgd5e1e73" class="outline-4">
<h4 id="orgd5e1e73"><span class="section-number-4">7.2.3.</span> Propriedades dos Compostos Covalentes (Moleculares)</h4>
<div class="outline-text-4" id="text-7-2-3">
<p>
<b>Exemplos:</b> H₂O, CO₂, CH₄, O₂, N₂
</p>
</div>

<div id="outline-container-orge11e4e0" class="outline-5">
<h5 id="orge11e4e0"><span class="section-number-5">7.2.3.1.</span> Características Físicas</h5>
<div class="outline-text-5" id="text-7-2-3-1">
<p>
<b>1. Estado Físico:</b>
</p>
<ul class="org-ul">
<li>Maioria: <b>gases</b> ou <b>líquidos</b> à temp. ambiente</li>
<li>Alguns sólidos (gelo, açúcar, naftaleno)</li>
</ul>

<p>
<b>2. Pontos de Fusão e Ebulição:</b>
</p>
<ul class="org-ul">
<li><b>Baixos</b> (comparados a iônicos)</li>
<li>Forças intermoleculares fracas</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>H₂O: PE = 100°C</li>
<li>CO₂: sublima a -78°C</li>
</ul>

<p>
<b>Exceção:</b> Substâncias covalentes em rede (SiO₂, diamante)
</p>
<ul class="org-ul">
<li>PF/PE muito altos</li>
<li>Ligações covalentes formam rede tridimensional</li>
</ul>
</div>
</div>

<div id="outline-container-org2cdcf98" class="outline-5">
<h5 id="org2cdcf98"><span class="section-number-5">7.2.3.2.</span> Condutividade Elétrica</h5>
<div class="outline-text-5" id="text-7-2-3-2">
<p>
<b>Geralmente:</b> NÃO conduzem
</p>
<ul class="org-ul">
<li>Não têm íons ou elétrons livres</li>
</ul>

<p>
<b>Exceções:</b>
</p>
<ul class="org-ul">
<li><b>Grafite:</b> estrutura especial com elétrons livres</li>
<li><b>Ácidos em água:</b> formam íons (HCl → H⁺ + Cl⁻)</li>
</ul>
</div>
</div>

<div id="outline-container-orgcd1c6e3" class="outline-5">
<h5 id="orgcd1c6e3"><span class="section-number-5">7.2.3.3.</span> Solubilidade</h5>
<div class="outline-text-5" id="text-7-2-3-3">
<p>
Depende da <b>polaridade</b> da molécula:
</p>

<p>
<b>Moléculas polares:</b>
</p>
<ul class="org-ul">
<li>Solúveis em solventes polares (água)</li>
<li>Exemplos: H₂O, HCl, NH₃, álcoois</li>
</ul>

<p>
<b>Moléculas apolares:</b>
</p>
<ul class="org-ul">
<li>Solúveis em solventes apolares (gasolina, benzeno)</li>
<li>Exemplos: O₂, N₂, CH₄, CO₂, gorduras</li>
</ul>

<p>
<b>Regra de ouro:</b>
</p>

<pre class="example" id="org09fd905">
"Semelhante dissolve semelhante"
</pre>
</div>
</div>
</div>

<div id="outline-container-org8dc14d9" class="outline-4">
<h4 id="org8dc14d9"><span class="section-number-4">7.2.4.</span> Propriedades das Substâncias Metálicas</h4>
<div class="outline-text-4" id="text-7-2-4">
<p>
<b>Exemplos:</b> Fe, Cu, Au, Al, Na
</p>
</div>

<div id="outline-container-orgbfffd07" class="outline-5">
<h5 id="orgbfffd07"><span class="section-number-5">7.2.4.1.</span> Características</h5>
<div class="outline-text-5" id="text-7-2-4-1">
<p>
<b>1. Estado Físico:</b>
</p>
<ul class="org-ul">
<li><b>Sólidos</b> à temp. ambiente (exceto Hg</li>
<li>mercúrio)</li>
</ul>

<p>
<b>2. Pontos de Fusão:</b>
</p>
<ul class="org-ul">
<li><b>Variados</b> (baixos a muito altos)</li>
<li>W (tungstênio): 3422°C (alto)</li>
<li>Hg (mercúrio): -39°C (líquido)</li>
<li>Ga (gálio): 30°C (derrete na mão)</li>
</ul>

<p>
<b>3. Condutividade Elétrica e Térmica:</b>
</p>
<ul class="org-ul">
<li><b>Excelentes condutores</b> (sempre)</li>
<li>Elétrons livres transportam carga e calor</li>
</ul>

<p>
<b>Melhores condutores:</b>
</p>
<ul class="org-ul">
<li>Ag (prata) &gt; Cu (cobre) &gt; Au (ouro) &gt; Al (alumínio)</li>
</ul>

<p>
<b>4. Brilho Metálico:</b>
</p>
<ul class="org-ul">
<li>Superfície reflete luz (elétrons livres)</li>
</ul>

<p>
<b>5. Maleabilidade e Ductilidade:</b>
</p>
<ul class="org-ul">
<li><b>Maleáveis:</b> podem ser martelados (lâminas)</li>
<li><b>Dúcteis:</b> podem ser esticados (fios)</li>
</ul>

<p>
<b>6. Densidade:</b>
</p>
<ul class="org-ul">
<li>Maioria são densos</li>
<li>Exceções: Li, Na, K (menos densos que água)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org912f919" class="outline-4">
<h4 id="org912f919"><span class="section-number-4">7.2.5.</span> Comparação das Propriedades</h4>
<div class="outline-text-4" id="text-7-2-5">
<pre class="example" id="org48c2dd7">
┌──────────────┬─────────┬──────────┬──────────┐
│  Propriedade │ IÔNICA  │COVALENTE │ METÁLICA │
├──────────────┼─────────┼──────────┼──────────┤
│Estado físico │ Sólidos │Gases/Líq.│ Sólidos  │
├──────────────┼─────────┼──────────┼──────────┤
│   PF / PE    │  Altos  │  Baixos  │ Variados │
├──────────────┼─────────┼──────────┼──────────┤
│Condutividade │Fund/Dis.│   Não    │   Sim    │
│  Elétrica    │         │          │ (sempre) │
├──────────────┼─────────┼──────────┼──────────┤
│ Solubilidade │  H₂O    │  Varia   │  Baixa   │
│              │(polar)  │(polar/ap)│          │
├──────────────┼─────────┼──────────┼──────────┤
│    Dureza    │Duros,   │  Varia   │  Varia   │
│              │quebradiç.│          │(maleáv.) │
├──────────────┼─────────┼──────────┼──────────┤
│   Exemplo    │  NaCl   │   H₂O    │    Fe    │
└──────────────┴─────────┴──────────┴──────────┘
</pre>
</div>
</div>

<div id="outline-container-org9f8d9a3" class="outline-4">
<h4 id="org9f8d9a3"><span class="section-number-4">7.2.6.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-7-2-6">
</div>
<div id="outline-container-org9dfa85c" class="outline-5">
<h5 id="org9dfa85c"><span class="section-number-5">7.2.6.1.</span> 1. Sal de Cozinha (NaCl)</h5>
<div class="outline-text-5" id="text-7-2-6-1">
<ul class="org-ul">
<li>Iônico</li>
<li>Sólido cristalino</li>
<li>Alto PF (801°C)</li>
<li>Solúvel em água</li>
<li>Solução conduz eletricidade (íons Na⁺ e Cl⁻)</li>
</ul>
</div>
</div>

<div id="outline-container-org6dc07db" class="outline-5">
<h5 id="org6dc07db"><span class="section-number-5">7.2.6.2.</span> 2. Água (H₂O)</h5>
<div class="outline-text-5" id="text-7-2-6-2">
<ul class="org-ul">
<li>Covalente Polar</li>
<li>Líquida à temp. ambiente</li>
<li>PE = 100°C (baixo)</li>
<li>Polar: dissolve iônicos e polares</li>
<li>Não conduz pura (mas conduz com íons dissolvidos)</li>
</ul>
</div>
</div>

<div id="outline-container-orgc5989c0" class="outline-5">
<h5 id="orgc5989c0"><span class="section-number-5">7.2.6.3.</span> 3. Cobre (Cu)</h5>
<div class="outline-text-5" id="text-7-2-6-3">
<ul class="org-ul">
<li>Metálico</li>
<li>Sólido à temp. ambiente</li>
<li>Excelente condutor elétrico (fios)</li>
<li>Maleável e dúctil</li>
<li>Brilho metálico</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org9992535" class="outline-4">
<h4 id="org9992535"><span class="section-number-4">7.2.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-7-2-7">
</div>
<div id="outline-container-org9b63907" class="outline-5">
<h5 id="org9b63907"><span class="section-number-5">7.2.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-7-2-7-1">
<p>
Por que o sal de cozinha (NaCl) não conduz eletricidade quando sólido, mas conduz quando dissolvido em água?
</p>

<p>
<b>Resposta:</b> <b>Sólido:</b> íons Na⁺ e Cl⁻ estão fixos no retículo cristalino, não podem se mover, logo NÃO conduzem.
</p>

<p>
<b>Dissolvido:</b> íons ficam livres na solução aquosa, podem se mover e transportar carga elétrica, logo CONDUZEM.
</p>
</div>
</div>

<div id="outline-container-org32ce7d4" class="outline-5">
<h5 id="org32ce7d4"><span class="section-number-5">7.2.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-7-2-7-2">
<p>
Explique por que metais são bons condutores de eletricidade.
</p>

<p>
<b>Resposta:</b> Metais têm <b>elétrons livres</b> (mar de elétrons) que se movem facilmente. Ao aplicar diferença de potencial, os elétrons fluem, criando corrente elétrica.
</p>
</div>
</div>

<div id="outline-container-orgc7c96fd" class="outline-5">
<h5 id="orgc7c96fd"><span class="section-number-5">7.2.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-7-2-7-3">
<p>
Uma substância é sólida à temperatura ambiente, tem alto ponto de fusão, é solúvel em água e sua solução conduz eletricidade. Que tipo de ligação tem?
</p>

<p>
<b>Resposta:</b> <b>Ligação iônica</b>. As características (sólido, alto PF, solúvel em água, solução condutora) são típicas de compostos iônicos.
</p>
</div>
</div>

<div id="outline-container-orgd3978cf" class="outline-5">
<h5 id="orgd3978cf"><span class="section-number-5">7.2.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-7-2-7-4">
<p>
(UFMG) Compare NaCl e H₂O quanto à condutividade elétrica.
</p>

<p>
<b>Resposta:</b>
</p>
<ul class="org-ul">
<li><b>NaCl sólido:</b> não conduz (íons fixos)</li>
<li><b>NaCl fundido/dissolvido:</b> conduz (íons livres)</li>
<li><b>H₂O pura:</b> não conduz (covalente, sem íons)</li>
<li><b>H₂O com sais dissolvidos:</b> conduz (íons do sal)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgdc70423" class="outline-4">
<h4 id="orgdc70423"><span class="section-number-4">7.2.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-7-2-8">
<ol class="org-ol">
<li><b>Iônico:</b> sólidos, altos PF/PE, conduzem fundidos/dissolvidos</li>
<li><b>Covalente:</b> gases/líquidos, baixos PF/PE, não conduzem</li>
<li><b>Metálico:</b> sólidos, conduzem sempre, maleáveis</li>
<li><b>Solubilidade:</b> “semelhante dissolve semelhante”</li>
<li><b>Condutividade:</b> precisa de partículas carregadas móveis</li>
<li><b>Iônicos:</b> solúveis em água (polar)</li>
<li><b>Covalentes apolares:</b> solúveis em apolares</li>
<li><b>Metais:</b> sempre conduzem (elétrons livres)</li>
</ol>
</div>
</div>

<div id="outline-container-org58737f1" class="outline-4">
<h4 id="org58737f1"><span class="section-number-4">7.2.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-7-2-9">
<p>
<b>Iônica:</b>
</p>
<ul class="org-ul">
<li>Sólidos cristalinos</li>
<li>Altos PF/PE</li>
<li>Conduzem fundidos/dissolvidos</li>
<li>Solúveis em água</li>
</ul>

<p>
<b>Covalente:</b>
</p>
<ul class="org-ul">
<li>Gases/líquidos (maioria)</li>
<li>Baixos PF/PE</li>
<li>Não conduzem (geralmente)</li>
<li>Solubilidade varia</li>
</ul>

<p>
<b>Metálica:</b>
</p>
<ul class="org-ul">
<li>Sólidos (exceto Hg)</li>
<li>Conduzem sempre</li>
<li>Maleáveis, dúcteis</li>
<li>Brilho metálico</li>
</ul>
</div>
</div>

<div id="outline-container-orgd91b095" class="outline-4">
<h4 id="orgd91b095"><span class="section-number-4">7.2.10.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-7-2-10">
<pre class="example" id="org0a99f5e">
PROPRIEDADES × LIGAÇÕES:

IÔNICA (NaCl):
├─ Sólido cristalino
├─ Alto PF (801°C)
├─ Conduz fundido/dissolvido
└─ Solúvel H₂O

COVALENTE (H₂O):
├─ Líquido/Gás
├─ Baixo PE (100°C)
├─ Não conduz puro
└─ Polar: dissolve polar

METÁLICA (Cu):
├─ Sólido
├─ Conduz sempre
├─ Maleável, dúctil
└─ Brilho

TABELA:
           Iônico  Cov.  Met.
Estado     Sól.    G/L   Sól.
PF/PE      Alto    Baixo Var.
Conduz     F/D     Não   Sim
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 30 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (importante
</p>
<ul class="org-ul">
<li>relaciona estrutura e propriedades!)</li>
</ul>
</div>
</div>
</div>
</div>

<div id="outline-container-orgb50da14" class="outline-2">`;

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
