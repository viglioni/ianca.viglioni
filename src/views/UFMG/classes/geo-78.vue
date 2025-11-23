<script setup lang="ts">
import { ref } from "vue";

const code = "geo-78";
const title = "Geografia: Revisão";
const subject = "geografia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-4">
<ul class="org-ul">
<li>Geografia: Revisão</li>
<li>Cartografia, Geologia e Climatologia</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org3b623bf" class="outline-4">
<h4 id="org3b623bf"><span class="section-number-4">4.4.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-4-4-1">
<p>
Consolidar os principais conceitos de Geografia para a prova.
</p>
</div>
</div>

<div id="outline-container-org96e24a1" class="outline-4">
<h4 id="org96e24a1"><span class="section-number-4">4.4.2.</span> PARTE 1: Cartografia (15min)</h4>
<div class="outline-text-4" id="text-4-4-2">
<p>
<b>Elementos do mapa:</b>
</p>

<pre class="example" id="org4f1aef6">
Título: indica o tema
Legenda: símbolos e significados
Escala: relação mapa/realidade
Orientação: Rosa dos ventos (N, S, L, O)
</pre>

<p>
<b>Escala:</b>
</p>

<pre class="example" id="org3e8ea60">
Numérica: 1:100.000
  1 cm no mapa = 100.000 cm na realidade = 1 km

Gráfica: régua graduada

Escala grande: mais detalhes (1:1.000)
Escala pequena: menos detalhes (1:1.000.000)
</pre>

<p>
<b>Coordenadas geográficas:</b>
</p>

<pre class="example" id="orge4b0cfe">
Latitude: 0° a 90° Norte ou Sul (Equador = 0°)
Longitude: 0° a 180° Leste ou Oeste (Greenwich = 0°)

Paralelos: linhas horizontais (latitude)
Meridianos: linhas verticais (longitude)
</pre>

<p>
<b>Projeções cartográficas:</b>
</p>

<pre class="example" id="org11e6e0e">
Cilíndrica: Mercator (distorce pólos)
Cônica: média latitude
Azimutal/Polar: centrada em um ponto
</pre>
</div>
</div>

<div id="outline-container-org36b817a" class="outline-4">
<h4 id="org36b817a"><span class="section-number-4">4.4.3.</span> PARTE 2: Estrutura Geológica (20min)</h4>
<div class="outline-text-4" id="text-4-4-3">
<p>
<b>Camadas da Terra:</b>
</p>

<pre class="example" id="org350ee08">
Crosta: fina, sólida (5-70 km)
Manto: espesso, magma viscoso
Núcleo externo: líquido (ferro, níquel)
Núcleo interno: sólido
</pre>

<p>
<b>Placas tectônicas:</b>
</p>

<pre class="example" id="org9d9a603">
Litosfera dividida em placas
Movimentam-se sobre o manto

Tipos de movimento:
- Divergente: placas se afastam (dorsal oceânica)
- Convergente: placas se chocam (montanhas, fossas)
- Transformante: placas deslizam (falhas, terremotos)
</pre>

<p>
<b>Consequências:</b>
</p>

<pre class="example" id="org4f6abe7">
Terremotos: vibração da crosta
Vulcanismo: magma atinge superfície
Formação de montanhas: choque de placas
Tsunamis: terremotos submarinos
</pre>

<p>
<b>Tipos de rocha:</b>
</p>

<pre class="example" id="orgf0ba5ab">
Magmáticas/Ígneas: resfriamento do magma
  Ex: granito, basalto

Sedimentares: acúmulo e compactação de sedimentos
  Ex: arenito, calcário
  Contêm fósseis

Metamórficas: transformação por pressão/temperatura
  Ex: mármore (de calcário), gnaisse (de granito)
</pre>

<p>
<b>Agentes externos (modelagem do relevo):</b>
</p>

<pre class="example" id="org9fe5c82">
Intemperismo: desagregação das rochas
Erosão: transporte de sedimentos
  - Pluvial (chuva)
  - Fluvial (rios)
  - Eólica (vento)
  - Marinha (ondas)
  - Glacial (gelo)
</pre>
</div>
</div>

<div id="outline-container-org0a9655d" class="outline-4">
<h4 id="org0a9655d"><span class="section-number-4">4.4.4.</span> PARTE 3: Climatologia (25min)</h4>
<div class="outline-text-4" id="text-4-4-4">
<p>
<b>Diferença: Tempo vs Clima</b>
</p>

<pre class="example" id="org47d6129">
Tempo: condição atmosférica momentânea
Clima: padrão atmosférico de longa duração
</pre>

<p>
<b>Elementos do clima:</b>
</p>

<pre class="example" id="org982e8f2">
Temperatura: calor da atmosfera
Umidade: vapor d'água no ar
Pressão atmosférica: peso do ar
Precipitação: chuva, neve, granizo
Ventos: movimento do ar
</pre>

<p>
<b>Fatores do clima:</b>
</p>

<pre class="example" id="org512e675">
Latitude:
  - Baixa latitude (Equador): mais quente
  - Alta latitude (pólos): mais frio
  - Influencia temperatura

Altitude:
  - Maior altitude → menor temperatura
  - ↑ 1000m → ↓ 6°C

Continentalidade/Maritimidade:
  - Litoral: menor amplitude térmica (água regula)
  - Interior: maior amplitude térmica

Massas de ar:
  - Grandes porções de ar com características uniformes
  - Quentes, frias, úmidas, secas

Correntes marítimas:
  - Quentes: aquecem clima costeiro
  - Frias: resfriam clima costeiro

Vegetação:
  - Aumenta umidade
  - Atenua temperatura
</pre>

<p>
<b>Tipos de clima (Brasil e mundo):</b>
</p>

<pre class="example" id="orgf08f8be">
BRASIL:
Equatorial: quente e úmido o ano todo (Amazônia)
Tropical: quente, chuvas no verão (Brasil Central)
Semi-árido: quente e seco (Sertão nordestino)
Tropical de altitude: ameno (planaltos do Sudeste)
Subtropical: 4 estações definidas (Sul)

MUNDO:
Equatorial: quente e úmido
Tropical: quente, estação seca
Desértico: muito seco
Temperado: 4 estações
Frio/Polar: muito frio
Mediterrâneo: verões secos, invernos chuvosos
</pre>

<p>
<b>Fenômenos climáticos:</b>
</p>

<pre class="example" id="orgc13e848">
El Niño: aquecimento do Pacífico
  - Seca na Amazônia
  - Chuvas no Sul

La Niña: resfriamento do Pacífico
  - Mais chuvas na Amazônia
  - Seca no Sul

Efeito estufa: aquecimento global
  - CO₂, CH₄ retêm calor
  - Natural + intensificado por ação humana

Inversão térmica:
  - Ar frio embaixo, quente em cima
  - Dificulta dispersão de poluentes
</pre>
</div>
</div>

<div id="outline-container-orgc1c248e" class="outline-4">
<h4 id="orgc1c248e"><span class="section-number-4">4.4.5.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-4-4-5">
</div>
<div id="outline-container-orgf5cbfe0" class="outline-5">
<h5 id="orgf5cbfe0"><span class="section-number-5">4.4.5.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-4-4-5-1">
<p>
Em uma escala 1:50.000, 2 cm no mapa representam quantos metros na realidade?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgc3f665d">
2 cm × 50.000 = 100.000 cm = 1.000 m = 1 km
</pre>
</div>
</div>

<div id="outline-container-orge6167a4" class="outline-5">
<h5 id="orge6167a4"><span class="section-number-5">4.4.5.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-4-4-5-2">
<p>
Qual tipo de rocha pode conter fósseis?
</p>

<p>
<i>[Ver resposta 21 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgbea2cd2" class="outline-5">
<h5 id="orgbea2cd2"><span class="section-number-5">4.4.5.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-4-4-5-3">
<p>
Por que lugares de maior altitude são mais frios?
</p>

<p>
<i>[Ver resposta 22 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org4bef420" class="outline-5">
<h5 id="org4bef420"><span class="section-number-5">4.4.5.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-4-4-5-4">
<p>
Qual a diferença entre tempo e clima?
</p>

<p>
<i>[Ver resposta 23 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3a203fb" class="outline-5">
<h5 id="org3a203fb"><span class="section-number-5">4.4.5.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-4-4-5-5">
<p>
O que é El Niño?
</p>

<p>
<i>[Ver resposta 24 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgeed8d0e" class="outline-4">
<h4 id="orgeed8d0e"><span class="section-number-4">4.4.6.</span> Conceitos-Chave</h4>
<div class="outline-text-4" id="text-4-4-6">
<pre class="example" id="org2125e15">
CARTOGRAFIA:
- Escala, latitude, longitude
- Paralelos e meridianos
- Projeções

GEOLOGIA:
- Placas tectônicas
- Tipos de rocha (ígnea, sedimentar, metamórfica)
- Agentes externos (erosão)

CLIMATOLOGIA:
- Elementos: temperatura, umidade, pressão, chuva
- Fatores: latitude, altitude, maritimidade
- Tipos de clima
- El Niño, La Niña, efeito estufa
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org4e97c6b" class="outline-3">`;

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
