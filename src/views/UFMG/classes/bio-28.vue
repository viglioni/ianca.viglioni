<script setup lang="ts">
import { ref } from "vue";

const code = "bio-28";
const title = "Biologia: Origem da Vida";
const subject = "biologia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-3">
<ul class="org-ul">
<li>Biologia: Origem da Vida</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org430ace1" class="outline-4">
<h4 id="org430ace1"><span class="section-number-4">6.3.1.</span> Introdução: Como a Vida Surgiu?</h4>
<div class="outline-text-4" id="text-6-3-1">
<p>
A <b>origem da vida</b> é uma das questões mais fascinantes da ciência. Como moléculas inanimadas deram origem a seres vivos?
</p>

<p>
<b>Perguntas fundamentais:</b>
</p>
<ul class="org-ul">
<li>Quando surgiu a vida na Terra?</li>
<li>Como surgiram os primeiros seres vivos?</li>
<li>Quais eram as condições da Terra primitiva?</li>
</ul>

<p>
<b>Estimativa:</b> A vida surgiu há aproximadamente <b>3,5 bilhões de anos</b>.
</p>
</div>
</div>

<div id="outline-container-org970782d" class="outline-4">
<h4 id="org970782d"><span class="section-number-4">6.3.2.</span> Teorias sobre a Origem da Vida</h4>
<div class="outline-text-4" id="text-6-3-2">
</div>
<div id="outline-container-org2844813" class="outline-5">
<h5 id="org2844813"><span class="section-number-5">6.3.2.1.</span> 1. Abiogênese (Geração Espontânea)</h5>
<div class="outline-text-5" id="text-6-3-2-1">
<ul class="org-ul">
<li>REFUTADA</li>
</ul>
<p>
<b>Conceito:</b> A vida poderia surgir espontaneamente da matéria bruta (não-viva).
</p>

<p>
<b>Exemplos históricos:</b>
</p>
<ul class="org-ul">
<li>Moscas surgindo de carne podre</li>
<li>Ratos nascendo de roupa suja + grãos</li>
<li>Sapos surgindo da lama</li>
</ul>

<p>
<b>Defensores:</b> Aristóteles, van Helmont
</p>

<p>
<b>Refutação:</b>
</p>

<p>
<b>Francesco Redi (1668):</b>
</p>
<ul class="org-ul">
<li><b>Experimento:</b> Carne em frascos abertos vs. fechados com gaze</li>
<li><b>Resultado:</b> Moscas só apareceram nos frascos abertos (ovos depositados)</li>
<li><b>Conclusão:</b> Moscas vêm de outras moscas, não da carne</li>
</ul>

<p>
<b>Needham vs. Spallanzani (século XVIII):</b>
</p>
<ul class="org-ul">
<li><b>Needham:</b> caldo aquecido + frasco fechado → microrganismos (abiogênese?)</li>
<li><b>Spallanzani:</b> caldo fervido + frasco selado → sem microrganismos</li>
<li><b>Crítica a Spallanzani:</b> ar (princípio vital) foi excluído</li>
</ul>

<p>
*Louis Pasteur (1860s)
</p>
<ul class="org-ul">
<li>EXPERIMENTO DEFINITIVO:*</li>
<li><b>Frasco pescoço de cisne:</b> permite entrada de ar, mas não de microrganismos</li>
<li>Caldo aquecido permanece estéril (até inclinar e tocar o “pescoço”)</li>
<li><b>Conclusão:</b> Microrganismos vêm de outros microrganismos (biogênese)</li>
</ul>

<p>
<b>Lei da Biogênese:</b> Todo ser vivo origina-se de outro ser vivo preexistente.
</p>
</div>
</div>

<div id="outline-container-orgea0f263" class="outline-5">
<h5 id="orgea0f263"><span class="section-number-5">6.3.2.2.</span> 2. Panspermia Cósmica</h5>
<div class="outline-text-5" id="text-6-3-2-2">
<p>
<b>Conceito:</b> A vida na Terra veio do espaço (meteoritos, cometas).
</p>

<p>
<b>Argumentos:</b>
</p>
<ul class="org-ul">
<li>Moléculas orgânicas encontradas em meteoritos</li>
<li>Micro-organismos extremófilos resistem a condições extremas</li>
</ul>

<p>
<b>Problema:</b> NÃO explica a origem da vida, apenas seu transporte!
</p>

<p>
<b>Status:</b> Possível, mas não resolve a questão fundamental.
</p>
</div>
</div>

<div id="outline-container-orge22fac3" class="outline-5">
<h5 id="orge22fac3"><span class="section-number-5">6.3.2.3.</span> 3. Evolução Química (Hipótese mais aceita)</h5>
<div class="outline-text-5" id="text-6-3-2-3">
<p>
<b>Conceito:</b> A vida surgiu gradualmente por reações químicas na Terra primitiva.
</p>

<p>
<b>Defensores:</b> Oparin (URSS) e Haldane (Inglaterra), década de 1920.
</p>

<p>
<b>Etapas:</b> 1. Formação de moléculas orgânicas simples 2. Formação de moléculas complexas (proteínas, ácidos nucleicos) 3. Formação de coacervados (protocélulas) 4. Surgimento dos primeiros seres vivos
</p>
</div>
</div>
</div>

<div id="outline-container-org75d3d75" class="outline-4">
<h4 id="org75d3d75"><span class="section-number-4">6.3.3.</span> A Terra Primitiva (há 4 bilhões de anos)</h4>
<div class="outline-text-4" id="text-6-3-3">
<p>
<b>Condições:</b>
</p>

<ol class="org-ol">
<li><b>Atmosfera redutora (sem O₂):</b>
<ul class="org-ul">
<li>Composição: CH₄ (metano), NH₃ (amônia), H₂O (vapor), H₂ (hidrogênio)</li>
<li>SEM oxigênio livre (O₂)</li>
<li>SEM camada de ozônio (O₃)</li>
</ul></li>
<li><b>Intensa atividade vulcânica:</b>
<ul class="org-ul">
<li>Liberação de gases</li>
<li>Altas temperaturas</li>
</ul></li>
<li><b>Tempestades elétricas frequentes:</b>
<ul class="org-ul">
<li>Descargas elétricas constantes</li>
</ul></li>
<li><b>Radiação UV intensa:</b>
<ul class="org-ul">
<li>Sem proteção de ozônio</li>
</ul></li>
<li><b>Mares primitivos (sopa primordial):</b>
<ul class="org-ul">
<li>Água + moléculas orgânicas dissolvidas</li>
</ul></li>
</ol>
</div>
</div>

<div id="outline-container-org8e36618" class="outline-4">
<h4 id="org8e36618"><span class="section-number-4">6.3.4.</span> Experimento de Miller-Urey (1953)</h4>
<div class="outline-text-4" id="text-6-3-4">
<p>
<b>Objetivo:</b> Testar se moléculas orgânicas podem surgir das condições da Terra primitiva.
</p>

<p>
<b>Aparato:</b>
</p>
<ul class="org-ul">
<li>Frasco com água (oceano)</li>
<li>Mistura gasosa: CH₄, NH₃, H₂O, H₂ (atmosfera primitiva)</li>
<li>Descargas elétricas (simulando raios)</li>
<li>Aquecimento e condensação (ciclo de evaporação)</li>
</ul>

<p>
<b>Resultado:</b> Após 1 semana, formaram-se <b>aminoácidos</b> (blocos de proteínas) e outras moléculas orgânicas.
</p>

<p>
<b>Conclusão:</b> Moléculas orgânicas PODEM ser formadas abioticamente em condições da Terra primitiva.
</p>

<p>
<b>Importância:</b> Demonstrou experimentalmente a viabilidade da evolução química.
</p>

<p>
<b>Observação:</b> Descobertas recentes sugerem que a atmosfera primitiva tinha mais CO₂ e N₂, mas experimentos similares também produziram moléculas orgânicas.
</p>
</div>
</div>

<div id="outline-container-orgead031e" class="outline-4">
<h4 id="orgead031e"><span class="section-number-4">6.3.5.</span> Etapas da Evolução Química</h4>
<div class="outline-text-4" id="text-6-3-5">
</div>
<div id="outline-container-org5f535f3" class="outline-5">
<h5 id="org5f535f3"><span class="section-number-5">6.3.5.1.</span> 1. Formação de Monômeros</h5>
<div class="outline-text-5" id="text-6-3-5-1">
<p>
Moléculas simples → aminoácidos, nucleotídeos, açúcares, ácidos graxos
</p>

<p>
<b>Fontes de energia:</b>
</p>
<ul class="org-ul">
<li>Descargas elétricas (raios)</li>
<li>Radiação UV</li>
<li>Calor vulcânico</li>
</ul>
</div>
</div>

<div id="outline-container-orgeb52565" class="outline-5">
<h5 id="orgeb52565"><span class="section-number-5">6.3.5.2.</span> 2. Formação de Polímeros</h5>
<div class="outline-text-5" id="text-6-3-5-2">
<p>
Monômeros → proteínas, ácidos nucleicos (RNA, DNA)
</p>

<p>
<b>Condições:</b>
</p>
<ul class="org-ul">
<li>Concentração em poças rasas (evaporação)</li>
<li>Superfícies minerais catalíticas (argilas)</li>
</ul>
</div>
</div>

<div id="outline-container-orgceebcd5" class="outline-5">
<h5 id="orgceebcd5"><span class="section-number-5">6.3.5.3.</span> 3. Formação de Agregados Moleculares</h5>
<div class="outline-text-5" id="text-6-3-5-3">
<p>
<b>Coacervados (Oparin):</b>
</p>
<ul class="org-ul">
<li>Aglomerados de moléculas orgânicas em meio aquoso</li>
<li>Separados do meio por uma “membrana”</li>
<li>Podem captar moléculas e crescer</li>
<li>NÃO são seres vivos (sem material genético, reprodução)</li>
</ul>

<p>
<b>Microesferas proteicas (Fox):</b>
</p>
<ul class="org-ul">
<li>Gotículas formadas por proteínas aquecidas</li>
<li>Semelhantes a células primitivas</li>
</ul>
</div>
</div>

<div id="outline-container-org5885418" class="outline-5">
<h5 id="org5885418"><span class="section-number-5">6.3.5.4.</span> 4. Surgimento do Material Genético</h5>
<div class="outline-text-5" id="text-6-3-5-4">
<p>
<b>Problema fundamental:</b> O que veio primeiro, DNA ou proteínas?
</p>
<ul class="org-ul">
<li>DNA precisa de proteínas (enzimas) para replicar</li>
<li>Proteínas precisam de DNA para serem sintetizadas</li>
</ul>

<p>
<b>Hipótese do Mundo de RNA:</b>
</p>
<ul class="org-ul">
<li><b>RNA</b> veio primeiro (antes de DNA e proteínas)</li>
<li>RNA pode:</li>
<li>Armazenar informação genética (como DNA)</li>
<li>Catalisar reações (como enzimas) → <b>ribozimas</b></li>
<li>Posteriormente, DNA (mais estável) assumiu armazenamento</li>
<li>Proteínas assumiram catálise</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orge58b1df" class="outline-4">
<h4 id="orge58b1df"><span class="section-number-4">6.3.6.</span> Primeiros Seres Vivos</h4>
<div class="outline-text-4" id="text-6-3-6">
<p>
<b>Características:</b> 1. <b>Procariontes:</b> sem núcleo 2. <b>Unicelulares:</b> uma única célula 3. <b>Anaeróbicos:</b> não usavam O₂ (ainda não havia) 4. <b>Heterotróficos:</b> consumiam moléculas orgânicas do ambiente
</p>

<p>
<b>Tipo provável:</b> semelhantes a bactérias primitivas
</p>

<p>
*Nutrição inicial
</p>
<ul class="org-ul">
<li>Heterotrofismo:*</li>
<li>Consumiam moléculas orgânicas da “sopa primordial”</li>
<li>Fermentação (anaeróbica)</li>
</ul>

<p>
*Surgimento da Fotossíntese
</p>
<ul class="org-ul">
<li>Autotrofismo:*</li>
<li>Cianobactérias (há ~3,5 bilhões de anos)</li>
<li>Produzem O₂ como subproduto</li>
<li><b>Grande Oxidação (há ~2,4 bi anos):</b> acúmulo de O₂ na atmosfera</li>
<li>Formação da camada de ozônio</li>
</ul>

<p>
<b>Consequências do O₂:</b>
</p>
<ul class="org-ul">
<li>Extinção de muitos anaeróbicos</li>
<li>Surgimento da respiração aeróbica (mais eficiente)</li>
<li>Proteção contra radiação UV (ozônio)</li>
</ul>
</div>
</div>

<div id="outline-container-orgd6be991" class="outline-4">
<h4 id="orgd6be991"><span class="section-number-4">6.3.7.</span> Resumo das Teorias</h4>
<div class="outline-text-4" id="text-6-3-7">
<pre class="example" id="org0256c41">
┌────────────────┬─────────────────────────┬──────────┐
│    Teoria      │      Descrição          │  Status  │
├────────────────┼─────────────────────────┼──────────┤
│  Abiogênese    │ Geração espontânea      │ REFUTADA │
│                │ (matéria bruta→vida)    │          │
├────────────────┼─────────────────────────┼──────────┤
│  Biogênese     │ Vida vem de vida        │  ACEITA  │
│                │ (Pasteur)               │  (atual) │
├────────────────┼─────────────────────────┼──────────┤
│  Panspermia    │ Vida veio do espaço     │ Possível │
│                │                         │(não resolve)│
├────────────────┼─────────────────────────┼──────────┤
│Evolução Química│ Reações químicas        │MAIS ACEITA│
│(Oparin-Haldane)│ gradualmente→vida       │          │
└────────────────┴─────────────────────────┴──────────┘
</pre>
</div>
</div>

<div id="outline-container-org0acb92e" class="outline-4">
<h4 id="org0acb92e"><span class="section-number-4">6.3.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-6-3-8">
</div>
<div id="outline-container-orgdadf8e4" class="outline-5">
<h5 id="orgdadf8e4"><span class="section-number-5">6.3.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-6-3-8-1">
<p>
Explique por que o experimento de Pasteur com o frasco pescoço de cisne refutou definitivamente a abiogênese.
</p>

<p>
<b>Resposta:</b> O frasco permitia a entrada de ar (refutando a crítica de que faltava “princípio vital”), mas não de microrganismos (que ficavam presos nas curvas do pescoço). O caldo permaneceu estéril, provando que microrganismos não surgem espontaneamente, mas vêm de outros microrganismos já existentes.
</p>
</div>
</div>

<div id="outline-container-org409f17b" class="outline-5">
<h5 id="org409f17b"><span class="section-number-5">6.3.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-6-3-8-2">
<p>
Qual a importância do experimento de Miller-Urey para a teoria da evolução química?
</p>

<p>
<b>Resposta:</b> Demonstrou experimentalmente que moléculas orgânicas (aminoácidos) podem ser formadas abioticamente a partir de moléculas inorgânicas simples nas condições da Terra primitiva, validando a hipótese de Oparin-Haldane.
</p>
</div>
</div>

<div id="outline-container-orge81fb75" class="outline-5">
<h5 id="orge81fb75"><span class="section-number-5">6.3.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-6-3-8-3">
<p>
Por que os primeiros seres vivos eram necessariamente anaeróbicos?
</p>

<p>
<b>Resposta:</b> Porque a atmosfera primitiva não continha oxigênio livre (O₂). O oxigênio só passou a existir na atmosfera após o surgimento da fotossíntese pelas cianobactérias, há aproximadamente 3,5 bilhões de anos.
</p>
</div>
</div>

<div id="outline-container-org3c89beb" class="outline-5">
<h5 id="org3c89beb"><span class="section-number-5">6.3.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-6-3-8-4">
<p>
(UFMG) Qual a principal hipótese para explicar o que surgiu primeiro: DNA, RNA ou proteínas?
</p>

<p>
<b>Resposta:</b> <b>Hipótese do Mundo de RNA</b>: o RNA teria surgido primeiro, pois pode tanto armazenar informação genética (como DNA) quanto catalisar reações (como proteínas/enzimas), através de ribozimas.
</p>
</div>
</div>
</div>

<div id="outline-container-org364b193" class="outline-4">
<h4 id="org364b193"><span class="section-number-4">6.3.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-6-3-9">
<ol class="org-ol">
<li><b>Abiogênese:</b> REFUTADA por Pasteur</li>
<li><b>Biogênese:</b> vida vem de vida (princípio atual)</li>
<li><b>Pasteur:</b> frasco pescoço de cisne (definitivo)</li>
<li><b>Miller-Urey:</b> simulou Terra primitiva, produziu aminoácidos</li>
<li><b>Atmosfera primitiva:</b> SEM O₂ (redutora)</li>
<li><b>Primeiros seres:</b> procariontes, unicelulares, anaeróbicos, heterotróficos</li>
<li><b>Mundo de RNA:</b> RNA veio antes de DNA e proteínas</li>
<li><b>Cianobactérias:</b> primeiras fotossintetizantes, produziram O₂</li>
</ol>
</div>
</div>

<div id="outline-container-org5dbe37e" class="outline-4">
<h4 id="org5dbe37e"><span class="section-number-4">6.3.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-6-3-10">
<p>
<b>Teorias Históricas:</b>
</p>
<ul class="org-ul">
<li><b>Abiogênese:</b> geração espontânea (REFUTADA)</li>
<li><b>Biogênese:</b> vida de vida (ACEITA)</li>
<li><b>Panspermia:</b> vida do espaço (não explica origem)</li>
<li><b>Evolução Química:</b> Oparin-Haldane (MAIS ACEITA)</li>
</ul>

<p>
<b>Experimentos:</b>
</p>
<ul class="org-ul">
<li><b>Redi:</b> carne com gaze (moscas)</li>
<li><b>Pasteur:</b> pescoço de cisne (definitivo)</li>
<li><b>Miller-Urey:</b> Terra primitiva → aminoácidos</li>
</ul>

<p>
<b>Terra Primitiva:</b>
</p>
<ul class="org-ul">
<li>Atmosfera: CH₄, NH₃, H₂O, H₂ (SEM O₂!)</li>
<li>Energia: raios, UV, vulcões</li>
<li>Oceanos: “sopa primordial”</li>
</ul>

<p>
<b>Primeiros Seres:</b>
</p>
<ul class="org-ul">
<li>Procariontes</li>
<li>Unicelulares</li>
<li>Anaeróbicos</li>
<li>Heterotróficos</li>
</ul>

<p>
<b>Sequência:</b> Moléculas simples → polímeros → coacervados → material genético (RNA) → células primitivas → fotossíntese → O₂ → vida atual
</p>
</div>
</div>

<div id="outline-container-org9573f4f" class="outline-4">
<h4 id="org9573f4f"><span class="section-number-4">6.3.11.</span> Linha do Tempo</h4>
<div class="outline-text-4" id="text-6-3-11">
<pre class="example" id="orgabc1720">
4,6 bi anos: Formação da Terra
4 bi anos: Terra primitiva (atmosfera redutora)
3,5-3,8 bi anos: Primeiros seres vivos (fósseis)
3,5 bi anos: Cianobactérias (fotossíntese)
2,4 bi anos: Grande Oxidação (O₂ na atmosfera)
2 bi anos: Primeiros eucariontes
600 mi anos: Seres multicelulares
HOJE: Biodiversidade atual
</pre>
</div>
</div>

<div id="outline-container-org53bf8c0" class="outline-4">
<h4 id="org53bf8c0"><span class="section-number-4">6.3.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-6-3-12">
<pre class="example" id="org86c4759">
ORIGEM DA VIDA
- EVOLUÇÃO QUÍMICA

Terra Primitiva (sem O₂)
        ↓
Energia (raios, UV, calor)
        ↓
Moléculas Orgânicas Simples
(aminoácidos, nucleotídeos)
        ↓
Polímeros
(proteínas, RNA, DNA)
        ↓
Coacervados/Protocélulas
(agregados moleculares)
        ↓
Primeiros Seres Vivos
(procariontes, anaeróbicos, heterotróficos)
        ↓
Fotossíntese (cianobactérias)
        ↓
O₂ na atmosfera
        ↓
Vida aeróbica + Ozônio
        ↓
Evolução da Biodiversidade

EXPERIMENTO DE PASTEUR:
    ╱╲
   │  │  ← pescoço de cisne
   │  │
   ╲  ╱
    │ │ ← caldo estéril
    └─┘
(ar entra, microrganismos não)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>conceito fundamental de Biologia)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org309a6a9" class="outline-3">`;

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
