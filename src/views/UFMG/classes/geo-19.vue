<script setup lang="ts">
import { ref } from "vue";

const code = "geo-19";
const title = "Geografia: Cartografia";
const subject = "geografia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-4">
<ul class="org-ul">
<li>Geografia: Cartografia</li>
<li>Parte 1</li>
<li>75min</li>
</ul>
</div>
<div id="outline-container-orgdfe5388" class="outline-4">
<h4 id="orgdfe5388"><span class="section-number-4">4.4.1.</span> O que é Cartografia?</h4>
<div class="outline-text-4" id="text-4-4-1">
<p>
<b>Cartografia</b> é a ciência e a arte de representar graficamente a superfície terrestre através de mapas, cartas e plantas.
</p>

<p>
<b>Função principal:</b>
</p>
<ul class="org-ul">
<li>Representar em 2D (papel/tela) um espaço 3D (Terra)</li>
<li>Facilitar a localização e orientação</li>
<li>Representar fenômenos geográficos</li>
</ul>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li>Navegação e orientação</li>
<li>Planejamento urbano e territorial</li>
<li>Estudos ambientais</li>
<li>Análise geopolítica</li>
<li>GPS e tecnologia</li>
</ul>
</div>
</div>

<div id="outline-container-org05375c3" class="outline-4">
<h4 id="org05375c3"><span class="section-number-4">4.4.2.</span> Evolução da Cartografia</h4>
<div class="outline-text-4" id="text-4-4-2">
<p>
<b>Cartografia Antiga:</b>
</p>
<ul class="org-ul">
<li>Mapas rudimentares (babilônios, egípcios)</li>
<li>Ptolomeu (século II): mapas com coordenadas</li>
<li>Idade Média: mapas religiosos (T-O)</li>
</ul>

<p>
<b>Era dos Descobrimentos (séc. XV-XVI):</b>
</p>
<ul class="org-ul">
<li>Grandes navegações exigiram mapas precisos</li>
<li>Portulanos (mapas náuticos)</li>
<li>Mercator: projeção cilíndrica (1569)</li>
</ul>

<p>
<b>Cartografia Moderna:</b>
</p>
<ul class="org-ul">
<li>Satélites (décadas 1960-70)</li>
<li>SIG</li>
<li>Sistemas de Informação Geográfica</li>
<li>GPS</li>
<li>Sistema de Posicionamento Global</li>
<li>Sensoriamento remoto</li>
<li>Cartografia digital</li>
</ul>
</div>
</div>

<div id="outline-container-org6926be6" class="outline-4">
<h4 id="org6926be6"><span class="section-number-4">4.4.3.</span> Orientação e Localização</h4>
<div class="outline-text-4" id="text-4-4-3">
</div>
<div id="outline-container-org016a4aa" class="outline-5">
<h5 id="org016a4aa"><span class="section-number-5">4.4.3.1.</span> Pontos Cardeais</h5>
<div class="outline-text-5" id="text-4-4-3-1">
<p>
Formas básicas de orientação:
</p>

<p>
<b>Principais:</b>
</p>
<ul class="org-ul">
<li><b>N (Norte):</b> direção do Polo Norte</li>
<li><b>S (Sul):</b> direção do Polo Sul</li>
<li><b>L ou E (Leste):</b> onde o Sol nasce</li>
<li><b>O ou W (Oeste):</b> onde o Sol se põe</li>
</ul>

<p>
<b>Colaterais:</b>
</p>
<ul class="org-ul">
<li><b>NE (Nordeste):</b> entre Norte e Leste</li>
<li><b>NO ou NW (Noroeste):</b> entre Norte e Oeste</li>
<li><b>SE (Sudeste):</b> entre Sul e Leste</li>
<li><b>SO ou SW (Sudoeste):</b> entre Sul e Oeste</li>
</ul>

<p>
<b>Subcolaterais:</b>
</p>
<ul class="org-ul">
<li>NNE, ENE, ESE, SSE, SSO, OSO, ONO, NNO</li>
</ul>
</div>
</div>

<div id="outline-container-org57ef27a" class="outline-5">
<h5 id="org57ef27a"><span class="section-number-5">4.4.3.2.</span> Rosa dos Ventos</h5>
<div class="outline-text-5" id="text-4-4-3-2">
<p>
Figura que representa os pontos cardeais, colaterais e subcolaterais.
</p>

<pre class="example" id="org7fb7dee">
      N
     NNO NNE
  NO       NE
 ONO   •   ENE
O            E
 OSO   •   ESE
  SO       SE
     SSO SSE
      S
</pre>
</div>
</div>

<div id="outline-container-orgc227c5b" class="outline-5">
<h5 id="orgc227c5b"><span class="section-number-5">4.4.3.3.</span> Métodos de Orientação</h5>
<div class="outline-text-5" id="text-4-4-3-3">
<p>
<b>1. Pelo Sol:</b>
</p>
<ul class="org-ul">
<li>Sol nasce no Leste (L/E)</li>
<li>Sol se põe no Oeste (O/W)</li>
<li>Ao meio-dia (Hemisfério Sul): Sol ao Norte</li>
</ul>

<p>
<b>2. Pela Lua:</b>
</p>
<ul class="org-ul">
<li>Crescente (C): lado iluminado indica Oeste</li>
<li>Minguante (D invertido): lado iluminado indica Leste</li>
</ul>

<p>
<b>3. Pelo Cruzeiro do Sul (Hemisfério Sul):</b>
</p>
<ul class="org-ul">
<li>Prolongar 4,5 vezes o eixo maior</li>
<li>Traçar perpendicular ao horizonte</li>
<li>Ponto indica Sul</li>
</ul>

<p>
<b>4. Pela Bússola:</b>
</p>
<ul class="org-ul">
<li>Agulha magnética aponta para Norte magnético</li>
<li>Declinação magnética: diferença entre Norte geográfico e magnético</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org26f235f" class="outline-4">
<h4 id="org26f235f"><span class="section-number-4">4.4.4.</span> Coordenadas Geográficas</h4>
<div class="outline-text-4" id="text-4-4-4">
<p>
Sistema de localização absoluta baseado em linhas imaginárias.
</p>
</div>

<div id="outline-container-org5eaf24c" class="outline-5">
<h5 id="org5eaf24c"><span class="section-number-5">4.4.4.1.</span> Latitude</h5>
<div class="outline-text-5" id="text-4-4-4-1">
<p>
<b>Definição:</b> distância angular de um ponto em relação à Linha do Equador.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Varia de 0° a 90°</li>
<li><b>0°:</b> Linha do Equador</li>
<li><b>90° N:</b> Polo Norte</li>
<li><b>90° S:</b> Polo Sul</li>
<li>Paralelos: linhas paralelas ao Equador</li>
</ul>

<p>
<b>Paralelos Principais:</b>
</p>
<ul class="org-ul">
<li>Equador: 0°</li>
<li>Trópico de Câncer: 23°27' N</li>
<li>Trópico de Capricórnio: 23°27' S</li>
<li>Círculo Polar Ártico: 66°33' N</li>
<li>Círculo Polar Antártico: 66°33' S</li>
</ul>

<p>
<b>Hemisférios:</b>
</p>
<ul class="org-ul">
<li>Norte ou Setentrional (acima do Equador)</li>
<li>Sul ou Meridional (abaixo do Equador)</li>
</ul>
</div>
</div>

<div id="outline-container-org76a5bfe" class="outline-5">
<h5 id="org76a5bfe"><span class="section-number-5">4.4.4.2.</span> Longitude</h5>
<div class="outline-text-5" id="text-4-4-4-2">
<p>
<b>Definição:</b> distância angular de um ponto em relação ao Meridiano de Greenwich.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Varia de 0° a 180°</li>
<li><b>0°:</b> Meridiano de Greenwich (Londres)</li>
<li><b>180°:</b> Linha Internacional da Data (Pacífico)</li>
<li><b>0° a 180° W (Oeste):</b> a oeste de Greenwich</li>
<li><b>0° a 180° E (Leste):</b> a leste de Greenwich</li>
<li>Meridianos: linhas que vão de polo a polo</li>
</ul>

<p>
<b>Hemisférios:</b>
</p>
<ul class="org-ul">
<li>Ocidental (a oeste de Greenwich)</li>
<li>Oriental (a leste de Greenwich)</li>
</ul>
</div>
</div>

<div id="outline-container-orga9766f9" class="outline-5">
<h5 id="orga9766f9"><span class="section-number-5">4.4.4.3.</span> Coordenadas Geográficas</h5>
<div class="outline-text-5" id="text-4-4-4-3">
<p>
Combinação de latitude e longitude para localização precisa.
</p>

<p>
<b>Formato:</b>
</p>
<ul class="org-ul">
<li>Latitude: graus, minutos, segundos (N ou S)</li>
<li>Longitude: graus, minutos, segundos (E ou W)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Belo Horizonte: 19°55'15” S, 43°56'16” W</li>
<li>São Paulo: 23°33' S, 46°38' W</li>
<li>Paris: 48°51' N, 2°21' E</li>
</ul>

<p>
<b>Conversão:</b>
</p>
<ul class="org-ul">
<li>1° (grau) = 60' (minutos)</li>
<li>1' (minuto) = 60” (segundos)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org33cd78d" class="outline-4">
<h4 id="org33cd78d"><span class="section-number-4">4.4.5.</span> Fusos Horários</h4>
<div class="outline-text-4" id="text-4-4-5">
<p>
A Terra gira 360° em 24 horas → 15° por hora.
</p>

<p>
<b>Fuso Horário:</b> divisão da Terra em 24 faixas de 15° de longitude.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Referência: Meridiano de Greenwich (0°)</li>
<li>A cada 15° de longitude = 1 hora de diferença</li>
<li><b>Leste:</b> horário adiantado (adiciona horas)</li>
<li><b>Oeste:</b> horário atrasado (subtrai horas)</li>
</ul>

<p>
<b>Linha Internacional da Data (180°):</b>
</p>
<ul class="org-ul">
<li>Divisor de datas</li>
<li>Atravessando de Oeste para Leste: avança 1 dia</li>
<li>Atravessando de Leste para Oeste: retrocede 1 dia</li>
</ul>

<p>
<b>Brasil:</b>
</p>
<ul class="org-ul">
<li>4 fusos horários (reduzidos para 4 em 2008, depois 3 em 2013)</li>
<li>Atualmente: 3 fusos (após mudanças)</li>
<li>Brasília: GMT -3 (UTC -3)</li>
</ul>
</div>
</div>

<div id="outline-container-org6bb2b7f" class="outline-4">
<h4 id="org6bb2b7f"><span class="section-number-4">4.4.6.</span> Escala</h4>
<div class="outline-text-4" id="text-4-4-6">
<p>
<b>Escala</b> é a relação entre a distância no mapa e a distância real na superfície.
</p>

<p>
<b>Tipos:</b>
</p>
</div>

<div id="outline-container-orgf3de52b" class="outline-5">
<h5 id="orgf3de52b"><span class="section-number-5">4.4.6.1.</span> Escala Numérica</h5>
<div class="outline-text-5" id="text-4-4-6-1">
<p>
Expressa por uma fração ou razão.
</p>

<p>
<b>Formato:</b>
</p>

<pre class="example" id="org18bbe1a">
1:100.000  ou  1/100.000
</pre>

<p>
<b>Significado:</b>
</p>
<ul class="org-ul">
<li>1 cm no mapa = 100.000 cm na realidade</li>
<li>1 cm no mapa = 1.000 m = 1 km</li>
</ul>

<p>
<b>Interpretação:</b>
</p>
<ul class="org-ul">
<li><b>Denominador grande</b> (ex: 1:1.000.000) → Escala pequena → Área grande, poucos detalhes</li>
<li><b>Denominador pequeno</b> (ex: 1:10.000) → Escala grande → Área pequena, muitos detalhes</li>
</ul>
</div>
</div>

<div id="outline-container-org4ee0585" class="outline-5">
<h5 id="org4ee0585"><span class="section-number-5">4.4.6.2.</span> Escala Gráfica</h5>
<div class="outline-text-5" id="text-4-4-6-2">
<p>
Representação visual com uma barra graduada.
</p>

<pre class="example" id="orgee31cac">
|----|----|----|----|
0    1    2    3    4 km
</pre>
</div>
</div>
</div>

<div id="outline-container-org8b4e8af" class="outline-4">
<h4 id="org8b4e8af"><span class="section-number-4">4.4.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-4-7">
</div>
<div id="outline-container-orga2eb3f2" class="outline-5">
<h5 id="orga2eb3f2"><span class="section-number-5">4.4.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-4-7-1">
<p>
Uma cidade está localizada a 30° de latitude Sul e 45° de longitude Oeste. Em quais hemisférios ela está?
</p>

<p>
<b>Solução:</b>
</p>

<p>
Latitude Sul → <b>Hemisfério Sul (Meridional)</b> Longitude Oeste → <b>Hemisfério Ocidental (Oeste)</b>
</p>

<p>
<i>[Ver resposta 76 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orga5ceeb1" class="outline-5">
<h5 id="orga5ceeb1"><span class="section-number-5">4.4.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-4-7-2">
<p>
Calcule a diferença de horário entre duas cidades:
</p>
<ul class="org-ul">
<li>Cidade A: 15° W</li>
<li>Cidade B: 60° W</li>
</ul>

<p>
<b>Solução:</b>
</p>

<p>
Diferença de longitude: 60°
</p>
<ul class="org-ul">
<li>15° = 45°</li>
</ul>

<p>
Diferença de tempo: 45° ÷ 15°/h = 3 horas
</p>

<p>
Cidade B está mais a Oeste → horário atrasado
</p>

<p>
<i>[Ver resposta 77 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgad065ea" class="outline-5">
<h5 id="orgad065ea"><span class="section-number-5">4.4.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-4-7-3">
<p>
Em um mapa de escala 1:500.000, a distância entre duas cidades é de 8 cm. Qual a distância real?
</p>

<p>
<b>Solução:</b>
</p>

<p>
Escala: 1 cm no mapa = 500.000 cm real
</p>

<p>
Distância real: 8 × 500.000 = 4.000.000 cm
</p>

<p>
Convertendo: 4.000.000 cm = 40.000 m = 40 km
</p>

<p>
<i>[Ver resposta 78 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7babcdc" class="outline-5">
<h5 id="org7babcdc"><span class="section-number-5">4.4.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-4-7-4">
<p>
Uma cidade está a 120° Leste de Greenwich. Quando em Greenwich são 12h, que horas são na cidade?
</p>

<p>
<b>Solução:</b>
</p>

<p>
120° Leste → horário adiantado
</p>

<p>
Diferença: 120° ÷ 15° = 8 horas
</p>

<p>
Horário na cidade: 12h + 8h = 20h
</p>

<p>
<i>[Ver resposta 79 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org01abd8b" class="outline-4">
<h4 id="org01abd8b"><span class="section-number-4">4.4.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-4-8">
<ol class="org-ol">
<li><b>Latitude:</b> 0° (Equador) a 90° (Polos), N ou S</li>
<li><b>Longitude:</b> 0° (Greenwich) a 180°, E ou W</li>
<li><b>Leste = adiantado</b> (soma horas); <b>Oeste = atrasado</b> (subtrai)</li>
<li><b>Fuso horário:</b> 15° = 1 hora</li>
<li><b>Escala grande:</b> denominador pequeno, mais detalhes</li>
<li><b>Escala pequena:</b> denominador grande, menos detalhes</li>
<li><b>Paralelos principais:</b> Equador (0°), Trópicos (23°27'), Círculos Polares (66°33')</li>
<li><b>Conversão escala:</b> 1 cm × escala = distância real (em cm)</li>
</ol>
</div>
</div>

<div id="outline-container-orgeae8517" class="outline-4">
<h4 id="orgeae8517"><span class="section-number-4">4.4.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-4-9">
<p>
<b>Orientação:</b>
</p>
<ul class="org-ul">
<li>Cardeais: N, S, L/E, O/W</li>
<li>Colaterais: NE, NO, SE, SO</li>
<li>Sol: nasce L, põe O</li>
</ul>

<p>
<b>Coordenadas:</b>
</p>
<ul class="org-ul">
<li>Latitude: paralelos (horizontal), 0°-90° N/S</li>
<li>Longitude: meridianos (vertical), 0°-180° E/W</li>
<li>Equador: 0° latitude</li>
<li>Greenwich: 0° longitude</li>
</ul>

<p>
<b>Fusos:</b>
</p>
<ul class="org-ul">
<li>15° = 1 hora</li>
<li>Leste: + horas</li>
<li>Oeste:</li>
<li>horas</li>
<li>180°: Linha da Data</li>
</ul>

<p>
<b>Escala:</b>
</p>
<ul class="org-ul">
<li>Numérica: 1:X</li>
<li>Grande escala = pequeno denominador = mais detalhes</li>
<li>Pequena escala = grande denominador = menos detalhes</li>
</ul>
</div>
</div>

<div id="outline-container-org428c7ea" class="outline-4">
<h4 id="org428c7ea"><span class="section-number-4">4.4.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-4-10">
<pre class="example" id="orgcc1b271">
Fuso Horário:
Diferença de horas = Δlongitude ÷ 15°

Leste de Greenwich: + horas
Oeste de Greenwich:
- horas

Distância Real (escala):
D_real = D_mapa × escala

Exemplo: escala 1:100.000
D_real (cm) = D_mapa (cm) × 100.000

Conversões:
1° = 60'
1' = 60"
100.000 cm = 1.000 m = 1 km
</pre>
</div>
</div>

<div id="outline-container-orgc52c381" class="outline-4">
<h4 id="orgc52c381"><span class="section-number-4">4.4.11.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-4-11">
<pre class="example" id="org2cd8eea">
Coordenadas Geográficas:

        90°N (Polo Norte)
           |
    Círculo Polar Ártico 66°33'N
           |
    Trópico de Câncer 23°27'N
           |
0° ←─── EQUADOR ────→ 0°
           |
    Trópico de Capricórnio 23°27'S
           |
    Círculo Polar Antártico 66°33'S
           |
        90°S (Polo Sul)

    180°W ← Greenwich → 180°E
             (0°)

Escala:
┌────────────────┬──────────┬──────────┐
│ Tipo           │ Área     │ Detalhes │
├────────────────┼──────────┼──────────┤
│ Grande         │ Pequena  │  Muitos  │
│ (ex: 1:10.000) │          │          │
├────────────────┼──────────┼──────────┤
│ Pequena        │ Grande   │  Poucos  │
│ (ex: 1:1.000.000)│        │          │
└────────────────┴──────────┴──────────┘

Fusos Horários:
360° ÷ 24h = 15°/hora

OESTE ← Greenwich → LESTE
 (-h)      (0°)      (+h)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 75 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>base da Geografia)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgf1bf4db" class="outline-3">`;

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
