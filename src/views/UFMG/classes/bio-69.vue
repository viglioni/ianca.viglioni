<script setup lang="ts">
import { ref } from "vue";

const code = "bio-69";
const title = "Biologia: A Célula";
const subject = "biologia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-6">
<ul class="org-ul">
<li>Biologia: A Célula</li>
<li>Estruturas, Respiração, Fotossíntese</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-orgdbd8b48" class="outline-4">
<h4 id="orgdbd8b48"><span class="section-number-4">2.6.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-2-6-1">
<p>
Compreender estruturas celulares e principais processos metabólicos (respiração celular, fotossíntese, fermentação).
</p>
</div>
</div>

<div id="outline-container-orgd04a034" class="outline-4">
<h4 id="orgd04a034"><span class="section-number-4">2.6.2.</span> PARTE 1: Estruturas Celulares</h4>
<div class="outline-text-4" id="text-2-6-2">
<p>
<b>Célula:</b> unidade básica da vida
</p>

<p>
<b>Tipos celulares:</b>
</p>

<p>
<b>Procariótica:</b>
</p>
<ul class="org-ul">
<li>Sem núcleo definido</li>
<li>Sem organelas membranosas</li>
<li>Simples</li>
<li>Exemplo: bactérias</li>
</ul>

<p>
<b>Eucariótica:</b>
</p>
<ul class="org-ul">
<li>Núcleo definido</li>
<li>Organelas membranosas</li>
<li>Complexa</li>
<li>Exemplo: células animais, vegetais, fungos</li>
</ul>

<p>
<b>Principais organelas:</b>
</p>

<p>
<b>1. Núcleo:</b>
</p>
<ul class="org-ul">
<li>Contém DNA (material genético)</li>
<li>Controla atividades celulares</li>
<li>Envolvido por membrana nuclear (carioteca)</li>
</ul>

<p>
<b>2. Mitocôndria:</b>
</p>
<ul class="org-ul">
<li><b>“Usina de energia”</b></li>
<li>Respiração celular</li>
<li>Produz ATP (energia)</li>
<li>Presente em células animais e vegetais</li>
</ul>

<p>
<b>3. Cloroplasto (só células vegetais):</b>
</p>
<ul class="org-ul">
<li><b>Fotossíntese</b></li>
<li>Contém clorofila (verde)</li>
<li>Produz glicose a partir de luz</li>
</ul>

<p>
<b>4. Retículo Endoplasmático:</b>
</p>
<ul class="org-ul">
<li><b>RE rugoso:</b> síntese de proteínas (tem ribossomos)</li>
<li><b>RE liso:</b> síntese de lipídios</li>
</ul>

<p>
<b>5. Complexo de Golgi:</b>
</p>
<ul class="org-ul">
<li>Modifica e secreta proteínas</li>
<li>Forma vesículas</li>
</ul>

<p>
<b>6. Ribossomos:</b>
</p>
<ul class="org-ul">
<li>Síntese de proteínas</li>
<li>Podem estar livres ou no RE rugoso</li>
</ul>

<p>
<b>7. Lisossomos:</b>
</p>
<ul class="org-ul">
<li>Digestão intracelular</li>
<li>Contém enzimas digestivas</li>
</ul>

<p>
<b>8. Vacúolos:</b>
</p>
<ul class="org-ul">
<li>Armazenamento</li>
<li><b>Grande em células vegetais</b></li>
</ul>

<p>
<b>9. Parede celular (só células vegetais):</b>
</p>
<ul class="org-ul">
<li>Celulose</li>
<li>Proteção e sustentação</li>
</ul>
</div>
</div>

<div id="outline-container-orgcb4672b" class="outline-4">
<h4 id="orgcb4672b"><span class="section-number-4">2.6.3.</span> PARTE 2: Respiração Celular</h4>
<div class="outline-text-4" id="text-2-6-3">
<p>
<b>Definição:</b> processo de quebra da glicose para produzir ATP (energia)
</p>

<p>
<b>Equação geral:</b>
</p>

<pre class="example" id="org9c764f0">
C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + ATP
(glicose + oxigênio → gás carbônico + água + energia)
</pre>

<p>
<b>Local:</b> mitocôndria
</p>

<p>
<b>Etapas:</b>
</p>

<p>
<b>1. Glicólise (citoplasma):</b>
</p>
<ul class="org-ul">
<li>Glicose → 2 piruvatos</li>
<li>Produz: 2 ATP</li>
</ul>

<p>
<b>2. Ciclo de Krebs (matriz mitocondrial):</b>
</p>
<ul class="org-ul">
<li>Piruvato é oxidado</li>
<li>Libera CO₂</li>
<li>Produz: 2 ATP</li>
</ul>

<p>
<b>3. Cadeia respiratória (cristas mitocondriais):</b>
</p>
<ul class="org-ul">
<li>Maior produção de ATP</li>
<li>Produz: ~34 ATP</li>
</ul>

<p>
<b>Total: ~38 ATP por molécula de glicose</b>
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Aeróbia:</b> precisa de O₂</li>
<li><b>Eficiente:</b> muito ATP produzido</li>
<li>Ocorre em todos os seres eucarióticos</li>
</ul>
</div>
</div>

<div id="outline-container-org3c5e1e7" class="outline-4">
<h4 id="org3c5e1e7"><span class="section-number-4">2.6.4.</span> PARTE 3: Fotossíntese</h4>
<div class="outline-text-4" id="text-2-6-4">
<p>
<b>Definição:</b> processo de produção de glicose usando luz solar
</p>

<p>
<b>Equação geral:</b>
</p>

<pre class="example" id="org7f156e2">
6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂
(gás carbônico + água + luz → glicose + oxigênio)
</pre>

<p>
<b>Local:</b> cloroplasto (células vegetais)
</p>

<p>
<b>Etapas:</b>
</p>

<p>
<b>1. Fase clara (tilacoides):</b>
</p>
<ul class="org-ul">
<li>Depende de luz</li>
<li>Quebra H₂O (fotólise)</li>
<li>Libera O₂</li>
<li>Produz ATP e NADPH</li>
</ul>

<p>
<b>2. Fase escura / Ciclo de Calvin (estroma):</b>
</p>
<ul class="org-ul">
<li>Não depende diretamente de luz</li>
<li>Fixa CO₂</li>
<li>Produz glicose</li>
</ul>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Ocorre em plantas, algas, cianobactérias</li>
<li>Responsável por O₂ atmosférico</li>
<li>Base das cadeias alimentares</li>
</ul>

<p>
<b>Importância:</b>
</p>
<ul class="org-ul">
<li>Produz alimento (glicose)</li>
<li>Libera O₂</li>
<li>Remove CO₂ da atmosfera</li>
</ul>
</div>
</div>

<div id="outline-container-org70ae60e" class="outline-4">
<h4 id="org70ae60e"><span class="section-number-4">2.6.5.</span> PARTE 4: Fermentação</h4>
<div class="outline-text-4" id="text-2-6-5">
<p>
<b>Definição:</b> processo anaeróbio (sem O₂) de produção de energia
</p>

<p>
<b>Tipos:</b>
</p>

<p>
<b>1. Fermentação Alcoólica:</b>
</p>

<pre class="example" id="org6128b2f">
C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂ + 2 ATP
(glicose → etanol + gás carbônico + energia)
</pre>

<p>
<b>Realizadores:</b> leveduras (Saccharomyces)
</p>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Produção de bebidas (vinho, cerveja)</li>
<li>Pão (CO₂ faz crescer)</li>
</ul>

<p>
<b>2. Fermentação Lática:</b>
</p>

<pre class="example" id="org2a9411f">
C₆H₁₂O₆ → 2 C₃H₆O₃ + 2 ATP
(glicose → ácido lático + energia)
</pre>

<p>
<b>Realizadores:</b>
</p>
<ul class="org-ul">
<li>Lactobacilos</li>
<li>Músculos humanos (em exercício intenso)</li>
</ul>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Produção de iogurte, queijo</li>
<li>Conservação de alimentos</li>
</ul>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Anaeróbia:</b> sem O₂</li>
<li><b>Pouco eficiente:</b> apenas 2 ATP</li>
<li>Produtos finais variados (etanol ou ácido lático)</li>
</ul>
</div>
</div>

<div id="outline-container-org8ca54f2" class="outline-4">
<h4 id="org8ca54f2"><span class="section-number-4">2.6.6.</span> PARTE 5: Quimiossíntese</h4>
<div class="outline-text-4" id="text-2-6-6">
<p>
<b>Definição:</b> produção de matéria orgânica a partir de substâncias inorgânicas (sem luz)
</p>

<p>
<b>Realizadores:</b> algumas bactérias
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgf51906c">
Nitrosomonas: oxida NH₃ → produz energia
Nitrobacter: oxida NO₂⁻ → produz energia
</pre>

<p>
<b>Importância:</b>
</p>
<ul class="org-ul">
<li>Ciclo do nitrogênio</li>
<li>Produtores em ambientes sem luz (fontes hidrotermais)</li>
</ul>
</div>
</div>

<div id="outline-container-orgdf5bcec" class="outline-4">
<h4 id="orgdf5bcec"><span class="section-number-4">2.6.7.</span> Comparação dos Processos</h4>
<div class="outline-text-4" id="text-2-6-7">
<pre class="example" id="org6dc5ccb">
┌──────────────┬────────────┬──────────┬─────────┐
│   Processo   │  Local     │    O₂    │   ATP   │
├──────────────┼────────────┼──────────┼─────────┤
│ Respiração   │Mitocôndria │ Precisa  │  ~38    │
│ Fotossíntese │Cloroplasto │ Libera   │   ATP*  │
│ Fermentação  │Citoplasma  │ Não usa  │    2    │
│Quimiossíntese│    -       │ Variável │ Variável│
└──────────────┴────────────┴──────────┴─────────┘

*ATP usado internamente
</pre>
</div>
</div>

<div id="outline-container-orgc9b2c86" class="outline-4">
<h4 id="orgc9b2c86"><span class="section-number-4">2.6.8.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-2-6-8">
</div>
<div id="outline-container-org13746d0" class="outline-5">
<h5 id="org13746d0"><span class="section-number-5">2.6.8.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-2-6-8-1">
<p>
Qual organela realiza respiração celular?
</p>

<p>
<i>[Ver resposta 6 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org2943047" class="outline-5">
<h5 id="org2943047"><span class="section-number-5">2.6.8.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-2-6-8-2">
<p>
Qual organela realiza fotossíntese?
</p>

<p>
<i>[Ver resposta 7 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf9aa7a8" class="outline-5">
<h5 id="orgf9aa7a8"><span class="section-number-5">2.6.8.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-2-6-8-3">
<p>
Qual a equação geral da fotossíntese?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org4573382">
6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂
</pre>
</div>
</div>

<div id="outline-container-org2565333" class="outline-5">
<h5 id="org2565333"><span class="section-number-5">2.6.8.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-2-6-8-4">
<p>
Qual processo produz mais ATP: respiração ou fermentação?
</p>

<p>
<i>[Ver resposta 8 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org61c8b20" class="outline-5">
<h5 id="org61c8b20"><span class="section-number-5">2.6.8.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-2-6-8-5">
<p>
O que é fermentação lática? Dê um exemplo.
</p>

<p>
<i>[Ver resposta 9 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org5234de3" class="outline-5">
<h5 id="org5234de3"><span class="section-number-5">2.6.8.6.</span> Questão 6</h5>
<div class="outline-text-5" id="text-2-6-8-6">
<p>
Qual a diferença entre célula procariótica e eucariótica?
</p>

<p>
<i>[Ver resposta 10 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org79532c9" class="outline-4">
<h4 id="org79532c9"><span class="section-number-4">2.6.9.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-2-6-9">
<pre class="example" id="org38ef1de">
CÉLULA VEGETAL:
┌─────────────────────┐
│  Parede celular     │
│ ┌─────────────────┐ │
│ │ Cloroplasto ● ● │ │
│ │                 │ │
│ │   ┌───────┐     │ │
│ │   │Núcleo │     │ │
│ │   └───────┘     │ │
│ │  Mitocôndria ○  │ │
│ │  Vacúolo grande │ │
│ └─────────────────┘ │
└─────────────────────┘

PROCESSOS:

Fotossíntese (cloroplasto):
CO₂ + H₂O + luz → Glicose + O₂

Respiração (mitocôndria):
Glicose + O₂ → CO₂ + H₂O + ATP

Fermentação (citoplasma):
Glicose → Etanol/Lático + CO₂ + 2 ATP
</pre>
</div>
</div>

<div id="outline-container-orgc46c02f" class="outline-4">
<h4 id="orgc46c02f"><span class="section-number-4">2.6.10.</span> Fórmulas e Equações Essenciais</h4>
<div class="outline-text-4" id="text-2-6-10">
<pre class="example" id="org664abda">
FOTOSSÍNTESE:
6 CO₂ + 6 H₂O + luz → C₆H₁₂O₆ + 6 O₂

RESPIRAÇÃO CELULAR:
C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + ~38 ATP

FERMENTAÇÃO ALCOÓLICA:
C₆H₁₂O₆ → 2 C₂H₅OH + 2 CO₂ + 2 ATP

FERMENTAÇÃO LÁTICA:
C₆H₁₂O₆ → 2 C₃H₆O₃ + 2 ATP
</pre>
</div>
</div>

<div id="outline-container-orgfa567fd" class="outline-4">
<h4 id="orgfa567fd"><span class="section-number-4">2.6.11.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-2-6-11">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei diferenciar célula procariótica e eucariótica</li>
<li class="off"><code>[&#xa0;]</code> Conheço as principais organelas e suas funções</li>
<li class="off"><code>[&#xa0;]</code> Sei a equação da respiração celular</li>
<li class="off"><code>[&#xa0;]</code> Sei a equação da fotossíntese</li>
<li class="off"><code>[&#xa0;]</code> Sei onde ocorre cada processo</li>
<li class="off"><code>[&#xa0;]</code> Sei diferenciar fermentação alcoólica e lática</li>
<li class="off"><code>[&#xa0;]</code> Sei que respiração produz mais ATP que fermentação</li>
<li class="off"><code>[&#xa0;]</code> Sei que mitocôndria é a “usina de energia”</li>
<li class="off"><code>[&#xa0;]</code> Sei que cloroplasto faz fotossíntese</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgcb58d4f" class="outline-3">`;

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
