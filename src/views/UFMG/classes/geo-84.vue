<script setup lang="ts">
import { ref } from "vue";

const code = "geo-84";
const title = "Geografia: Mapas Mentais e Conceitos Visuais";
const subject = "geografia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-4">
<ul class="org-ul">
<li>Geografia: Mapas Mentais e Conceitos Visuais</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org73a37e1" class="outline-4">
<h4 id="org73a37e1"><span class="section-number-4">5.4.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-5-4-1">
<p>
Criar mapas mentais visuais dos principais conceitos de Geografia para facilitar memorização.
</p>
</div>
</div>

<div id="outline-container-org09c6997" class="outline-4">
<h4 id="org09c6997"><span class="section-number-4">5.4.2.</span> MAPA MENTAL 1: Cartografia</h4>
<div class="outline-text-4" id="text-5-4-2">
<pre class="example" id="org802fda1">
                    CARTOGRAFIA
                        |
        ┌───────────────┼───────────────┐
        |               |               |
   ELEMENTOS      COORDENADAS        ESCALA
        |               |               |
    ┌───┴───┐      ┌────┴────┐     ┌───┴───┐
  Título  Legenda  LAT   LONG    Numérica Gráfica
  Orient. Rosa    0-90° 0-180°   1:100.000
                   N/S   L/O
                   
LATITUDE = Paralelos (horizontais)
Equador = 0°
Trópicos: 23,5°
Círculos polares: 66,5°

LONGITUDE = Meridianos (verticais)
Greenwich = 0°
Antimerídiamento = 180°

FUSOS HORÁRIOS:
360° ÷ 15° = 24 fusos
Leste: + horas
Oeste:
- horas
</pre>
</div>
</div>

<div id="outline-container-orgf85243c" class="outline-4">
<h4 id="orgf85243c"><span class="section-number-4">5.4.3.</span> MAPA MENTAL 2: Estrutura Geológica</h4>
<div class="outline-text-4" id="text-5-4-3">
<pre class="example" id="org543b80b">
                ESTRUTURA DA TERRA
                        |
        ┌───────────────┼───────────────┐
    CAMADAS         PLACAS           ROCHAS
        |           TECTÔNICAS            |
   ┌────┼────┐          |          ┌──────┼──────┐
Crosta Manto Núcleo  MOVIMENTOS  Magmát Sedim Metam
 (fina) (grosso) (Fe+Ni)  |      (magma)(fósseis)(transform)
                          |
                  ┌───────┼───────┐
              Divergente Convergente Transformante
              (afastam)   (colidem)  (deslizam)
                  ↓           ↓          ↓
               Dorsais    Montanhas   Falhas
               oceânicas  Terremotos  Terremotos

CONSEQUÊNCIAS:
- Vulcanismo
- Terremotos (sismo)
- Formação de montanhas
- Tsunamis

CICLO DAS ROCHAS:
Magmática → (intemperismo) → Sedimentar
     ↑                             ↓
     └──── (metamorfismo) ←────────┘
</pre>
</div>
</div>

<div id="outline-container-org6017b20" class="outline-4">
<h4 id="org6017b20"><span class="section-number-4">5.4.4.</span> MAPA MENTAL 3: Climatologia</h4>
<div class="outline-text-4" id="text-5-4-4">
<pre class="example" id="org0b52311">
                    CLIMA
                      |
        ┌─────────────┼─────────────┐
    ELEMENTOS              FATORES
        |                      |
    ┌───┴───┐          ┌───────┴────────┐
Temperatura Umidade   Latitude Altitude Maritimidade
Pressão     Chuva     |        |        |
Vento                 |        |        |
                      ↓        ↓        ↓
                   ↑ = ↓T    ↑ = ↓T  Menor
                                      amplitude

TIPOS DE CLIMA (Brasil):
┌──────────────────────────────────┐
│ EQUATORIAL: quente, úmido        │ Amazônia
│ TROPICAL: quente, chuva verão    │ Centro
│ SEMI-ÁRIDO: quente, seco         │ Sertão
│ TROPICAL ALTITUDE: ameno         │ Sudeste
│ SUBTROPICAL: 4 estações          │ Sul
└──────────────────────────────────┘

FENÔMENOS:
EL NIÑO                 LA NIÑA
(aquece Pacífico)      (resfria Pacífico)
    ↓                       ↓
Seca Amazônia          Chuva Amazônia
Chuva Sul              Seca Sul

EFEITO ESTUFA:
CO₂ + CH₄ → ↑ temperatura global
Natural + Intensificado (ação humana)
</pre>
</div>
</div>

<div id="outline-container-orgc000d5d" class="outline-4">
<h4 id="orgc000d5d"><span class="section-number-4">5.4.5.</span> MAPA MENTAL 4: Relevo e Erosão</h4>
<div class="outline-text-4" id="text-5-4-5">
<pre class="example" id="org4941572">
              MODELAGEM DO RELEVO
                      |
        ┌─────────────┴─────────────┐
    AGENTES                    FORMAS
    INTERNOS                   DE RELEVO
    (constroem)                    |
        |                   ┌──────┴──────┐
Tectonismo Vulcanismo   Montanhas Planaltos
                        Planícies  Depressões

AGENTES EXTERNOS (desgastam):
┌────────────────────────────────┐
│ INTEMPERISMO: desagregação     │
│ EROSÃO: transporte             │
│   - Pluvial (chuva)            │
│   - Fluvial (rios)             │
│   - Eólica (vento)             │
│   - Marinha (ondas)            │
│   - Glacial (gelo)             │
└────────────────────────────────┘

CICLO:
Intemperismo → Erosão → Transporte → Sedimentação
</pre>
</div>
</div>

<div id="outline-container-orgc262a4d" class="outline-4">
<h4 id="orgc262a4d"><span class="section-number-4">5.4.6.</span> MAPA MENTAL 5: Hidrografia</h4>
<div class="outline-text-4" id="text-5-4-6">
<pre class="example" id="orgb8201f4">
                  ÁGUA NA TERRA
                        |
        ┌───────────────┼───────────────┐
    OCEANOS           RIOS          ÁGUAS SUBTERRÂNEAS
    (97,5%)          (0,006%)           (0,6%)
        |                |                  |
    Salgada          Doce             Lençóis
    Correntes        Navegação        freáticos
    (quentes/frias)  Energia
                     Abastecimento

BACIAS HIDROGRÁFICAS (Brasil):
- Amazônica (maior do mundo)
- Platina (Paraná, Paraguai, Uruguai)
- São Francisco

CICLO DA ÁGUA:
Evaporação → Condensação → Precipitação → Infiltração/Escoamento
</pre>
</div>
</div>

<div id="outline-container-org1447c8c" class="outline-4">
<h4 id="org1447c8c"><span class="section-number-4">5.4.7.</span> DIAGRAMA: Latitude e Temperatura</h4>
<div class="outline-text-4" id="text-5-4-7">
<pre class="example" id="org18def01">
LATITUDE vs TEMPERATURA

  90°N ──────── Pólo Norte
   |            (FRIO)
   |              ↑
  66,5°N ─── Círculo Polar Ártico
   |
  23,5°N ─── Trópico de Câncer
   |
   0° ────── EQUADOR (QUENTE)
   |
  23,5°S ─── Trópico de Capricórnio
   |
  66,5°S ─── Círculo Polar Antártico
   |              ↓
  90°S ──────── Pólo Sul
               (FRIO)

Quanto MAIOR a latitude → MENOR a temperatura
</pre>
</div>
</div>

<div id="outline-container-org00faa7d" class="outline-4">
<h4 id="org00faa7d"><span class="section-number-4">5.4.8.</span> ESQUEMA: Altitude e Temperatura</h4>
<div class="outline-text-4" id="text-5-4-8">
<pre class="example" id="org02e308e">
ALTITUDE vs TEMPERATURA

4000m ─────── -14°C ─── Neve permanente
3000m ─────── -8°C  ─── Muito frio
2000m ─────── -2°C  ─── Frio
1000m ─────── 4°C   ─── Ameno
  0m  ─────── 10°C  ─── Temperatura base

Regra: ↑ 1000m → ↓ 6°C (aproximadamente)
</pre>
</div>
</div>

<div id="outline-container-org6a71536" class="outline-4">
<h4 id="org6a71536"><span class="section-number-4">5.4.9.</span> TABELA VISUAL: Climas do Mundo</h4>
<div class="outline-text-4" id="text-5-4-9">
<pre class="example" id="orgf76d6c3">
┌─────────────┬───────────┬──────────┬────────────┐
│   CLIMA     │TEMPERATURA│  CHUVA   │   REGIÃO   │
├─────────────┼───────────┼──────────┼────────────┤
│ Equatorial  │ Quente    │ Abundante│ Linha Eq.  │
│ Tropical    │ Quente    │ Verão    │ Trópicos   │
│ Desértico   │ Extremos  │ Escassa  │ 30° N/S    │
│ Temperado   │ 4 estações│ Regular  │ Média lat. │
│ Frio        │ Frio/Gelo │ Baixa    │ Alta lat.  │
│ Polar       │ Muito frio│ Neve     │ Pólos      │
│ Mediterrâneo│ Ameno     │ Inverno  │ Mediterrâ. │
└─────────────┴───────────┴──────────┴────────────┘
</pre>
</div>
</div>

<div id="outline-container-orgbb2e696" class="outline-4">
<h4 id="orgbb2e696"><span class="section-number-4">5.4.10.</span> ESQUEMA: Placas Tectônicas</h4>
<div class="outline-text-4" id="text-5-4-10">
<ul class="org-ul">
<li>Movimentos</li>
</ul>
<pre class="example" id="org03054f7">
DIVERGENTE (afastamento):
Placa ←─────────────→ Placa
         (magma sobe)
Resultado: Dorsais oceânicas, novo fundo oceânico

CONVERGENTE (colisão):
Placa ──→←── Placa
    (choque)
Resultado: Montanhas, fossas oceânicas, terremotos

TRANSFORMANTE (deslizamento):
Placa ↑
      ─────
Placa ↓
Resultado: Falhas geológicas, terremotos
</pre>
</div>
</div>

<div id="outline-container-org6291a84" class="outline-4">
<h4 id="org6291a84"><span class="section-number-4">5.4.11.</span> MAPA MENTAL 6: Brasil</h4>
<div class="outline-text-4" id="text-5-4-11">
<ul class="org-ul">
<li>Regionalização</li>
</ul>
<pre class="example" id="org0ffb01e">
              REGIÕES DO BRASIL
                     |
    ┌────────────────┼────────────────┐
  NORTE           NORDESTE         CENTRO-OESTE
    |                 |                 |
Amazônia         Semi-árido         Planalto Central
Floresta         Seca/chuva irreg   Cerrado
Bacia Amaz       Caatinga           Pantanal
                 Zona da Mata
                 
        SUDESTE              SUL
           |                  |
     Mais populous.      4 estações
     Industrializado     Subtropical
     Serra do Mar        Pampas (RS)
     Mata Atlântica      Araucárias
</pre>
</div>
</div>

<div id="outline-container-orgde538b4" class="outline-4">
<h4 id="orgde538b4"><span class="section-number-4">5.4.12.</span> FLUXOGRAMA: Problemas Ambientais</h4>
<div class="outline-text-4" id="text-5-4-12">
<pre class="example" id="orgea7c1bb">
AÇÃO HUMANA
     ↓
┌────┴────┬────────┬─────────┬──────────┐
DESMATAMENTO  POLUIÇÃO  QUEIMADAS  URBANIZAÇÃO
     ↓          ↓          ↓           ↓
Perda      Ar/água/solo  CO₂    Ilhas de calor
biodiversid  contaminados Desequ  Impermeabilização
Erosão                    ecológ  Enchentes
     ↓          ↓          ↓           ↓
        MUDANÇAS CLIMÁTICAS
        AQUECIMENTO GLOBAL
              ↓
    Derretimento geleiras
    Elevação nível do mar
    Eventos climáticos extremos
</pre>
</div>
</div>

<div id="outline-container-org7b9692a" class="outline-4">
<h4 id="org7b9692a"><span class="section-number-4">5.4.13.</span> Dicas para Usar Mapas Mentais</h4>
<div class="outline-text-4" id="text-5-4-13">
<p>
<b>Como criar:</b>
</p>

<pre class="example" id="org68b2c8c">
1. Palavra central no meio
2. Ramificações principais (temas)
3. Sub-ramificações (detalhes)
4. Use cores diferentes
5. Adicione símbolos/desenhos
6. Mantenha conciso
</pre>

<p>
<b>Como revisar:</b>
</p>

<pre class="example" id="org0ffa08d">
1. Leia o mapa completo
2. Cubra partes e tente lembrar
3. Refaça de memória
4. Compare com original
5. Repita até fixar
</pre>

<p>
<b>Benefícios:</b>
</p>

<pre class="example" id="org7922556">
✓ Organização visual
✓ Conexões claras
✓ Memorização facilitada
✓ Revisão rápida
✓ Visão geral do tema
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Fácil-Médio (visual) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org83f7aca" class="outline-3">`;

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
