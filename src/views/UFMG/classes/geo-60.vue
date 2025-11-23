<script setup lang="ts">
import { ref } from "vue";

const code = "geo-60";
const title = "Geografia: Climatologia";
const subject = "geografia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-4">
<ul class="org-ul">
<li>Geografia: Climatologia</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-orgd4b8402" class="outline-4">
<h4 id="orgd4b8402"><span class="section-number-4">5.4.1.</span> Introdução à Climatologia</h4>
<div class="outline-text-4" id="text-5-4-1">
<p>
<b>Climatologia:</b> ciência que estuda o <b>clima</b> e suas variações
</p>

<p>
<b>Diferença fundamental:</b>
</p>

<p>
<b>Tempo atmosférico:</b>
</p>
<ul class="org-ul">
<li>Condições atmosféricas momentâneas</li>
<li>Curto prazo (dias, horas)</li>
<li>Variável e instável</li>
<li>“Como está o tempo hoje?”</li>
</ul>

<p>
<b>Clima:</b>
</p>
<ul class="org-ul">
<li>Sucessão habitual dos tipos de tempo</li>
<li>Longo prazo (30+ anos)</li>
<li>Padrão médio</li>
<li>“Como é o clima da região?”</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>Tempo: “Hoje está frio em São Paulo (15°C)”</li>
<li>Clima: “São Paulo tem clima tropical de altitude”</li>
</ul>
</div>
</div>

<div id="outline-container-org73c1fed" class="outline-4">
<h4 id="org73c1fed"><span class="section-number-4">5.4.2.</span> Elementos Climáticos</h4>
<div class="outline-text-4" id="text-5-4-2">
<p>
<b>Elementos:</b> variáveis que caracterizam o clima
</p>

<p>
<b>1. Temperatura</b>
</p>

<p>
<b>Definição:</b> grau de calor da atmosfera
</p>

<p>
<b>Medição:</b> termômetro (°C ou °F)
</p>

<p>
<b>Variações:</b>
</p>
<ul class="org-ul">
<li><b>Diária:</b> mínima de manhã cedo, máxima à tarde</li>
<li><b>Anual:</b> inverno (mínima), verão (máxima)</li>
</ul>

<p>
<b>Amplitude térmica:</b>
</p>

<pre class="example" id="orgc79ca18">
Amplitude = Temperatura máxima
- Temperatura mínima
</pre>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li><b>Amplitude diária:</b> diferença entre máx e mín do dia</li>
<li><b>Amplitude anual:</b> diferença entre mês mais quente e mais frio</li>
</ul>

<p>
<b>2. Pressão Atmosférica</b>
</p>

<p>
<b>Definição:</b> peso (força) da coluna de ar sobre a superfície
</p>

<p>
<b>Medição:</b> barômetro (mbar ou hPa)
</p>

<p>
<b>Padrão:</b> 1013 hPa ao nível do mar
</p>

<p>
<b>Variações:</b>
</p>
<ul class="org-ul">
<li><b>Altitude:</b> ↑ altitude → ↓ pressão</li>
<li><b>Temperatura:</b> ↑ temperatura → ↓ pressão (ar sobe)</li>
</ul>

<p>
<b>Zonas de pressão:</b>
</p>
<ul class="org-ul">
<li><b>Alta pressão (anticiclone):</b> ar descendente, tempo estável, céu claro</li>
<li><b>Baixa pressão (ciclone):</b> ar ascendente, tempo instável, nuvens/chuvas</li>
</ul>

<p>
<b>3. Umidade</b>
</p>

<p>
<b>Definição:</b> quantidade de vapor de água no ar
</p>

<p>
<b>Medição:</b> higrômetro (%)
</p>

<p>
<b>Umidade relativa:</b>
</p>

<pre class="example" id="org685a400">
UR = (vapor presente / vapor máximo possível) × 100%
</pre>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Alta UR: ar próximo à saturação, sensação abafada</li>
<li>Baixa UR: ar seco, desconforto respiratório</li>
</ul>

<p>
<b>4. Precipitação</b>
</p>

<p>
<b>Definição:</b> queda de água da atmosfera (chuva, neve, granizo)
</p>

<p>
<b>Medição:</b> pluviômetro (mm)
</p>

<p>
<b>Tipos de chuva:</b>
</p>

<p>
<b>Chuva convectiva (ou de verão):</b>
</p>
<ul class="org-ul">
<li>Aquecimento do solo → ar quente sobe → condensação</li>
<li>Forte, rápida, localizada</li>
<li>Comum em tardes quentes</li>
</ul>

<p>
<b>Chuva orográfica (ou de relevo):</b>
</p>
<ul class="org-ul">
<li>Ar úmido encontra montanha → sobe → esfria → condensa</li>
<li>Lado do vento (barlavento): chuvoso</li>
<li>Lado oposto (sotavento): seco</li>
</ul>

<p>
<b>Chuva frontal:</b>
</p>
<ul class="org-ul">
<li>Encontro de massas de ar (fria e quente)</li>
<li>Duradoura, extensa</li>
<li>Comum em frentes frias</li>
</ul>

<p>
<b>5. Ventos</b>
</p>

<p>
<b>Definição:</b> deslocamento horizontal de ar
</p>

<p>
<b>Causa:</b> diferenças de pressão atmosférica
</p>

<p>
<b>Direção:</b> de alta para baixa pressão
</p>

<p>
<b>Medição:</b>
</p>
<ul class="org-ul">
<li>Direção: biruta, cata-vento</li>
<li>Velocidade: anemômetro (km/h, m/s)</li>
</ul>
</div>
</div>

<div id="outline-container-orgcc11c26" class="outline-4">
<h4 id="orgcc11c26"><span class="section-number-4">5.4.3.</span> Fatores Climáticos</h4>
<div class="outline-text-4" id="text-5-4-3">
<p>
<b>Fatores:</b> condições que influenciam/modificam os elementos climáticos
</p>

<p>
<b>1. Latitude</b>
</p>

<p>
<b>Influência:</b> determina ângulo de incidência dos raios solares
</p>

<p>
<b>Consequências:</b>
</p>
<ul class="org-ul">
<li><b>Baixas latitudes (Equador):</b> raios perpendiculares, mais calor</li>
<li><b>Altas latitudes (Polos):</b> raios inclinados, menos calor</li>
</ul>

<p>
<b>Zonas térmicas da Terra:</b>
</p>

<pre class="example" id="org4fe4a0f">
Polar (frio)          90°N
  ↑
Temperada            66,5°N (Círculo Polar Ártico)
  ↑
Tropical (quente)    23,5°N (Trópico de Câncer)
  ↑
Equatorial (muito quente) 0° (Equador)
  ↓
Tropical (quente)    23,5°S (Trópico de Capricórnio)
  ↓
Temperada            66,5°S (Círculo Polar Antártico)
  ↓
Polar (frio)          90°S
</pre>

<p>
<b>Regra geral:</b>
</p>
<ul class="org-ul">
<li>↑ latitude → ↓ temperatura</li>
<li>↓ latitude → ↑ temperatura</li>
</ul>

<p>
<b>2. Altitude</b>
</p>

<p>
<b>Influência:</b> altura em relação ao nível do mar
</p>

<p>
<b>Regra:</b>
</p>

<pre class="example" id="org1f6f152">
↑ altitude → ↓ temperatura
A cada 100-200m: -1°C
</pre>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>Nível do mar: 30°C</li>
<li>1000m de altitude: ~25°C</li>
</ul>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Ar rarefeito retém menos calor</li>
<li>Menor pressão atmosférica</li>
</ul>

<p>
<b>3. Maritimidade e Continentalidade</b>
</p>

<p>
<b>Maritimidade:</b> proximidade do oceano/mar
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Menor amplitude térmica</li>
<li>Clima mais úmido</li>
<li>Temperatura moderada (água aquece/esfria lentamente)</li>
</ul>

<p>
<b>Continentalidade:</b> distância do oceano
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Maior amplitude térmica</li>
<li>Clima mais seco</li>
<li>Extremos de temperatura (verão quente, inverno frio)</li>
</ul>

<p>
<b>Comparação:</b>
</p>

<pre class="example" id="orgff422e0">
┌──────────────┬─────────────┬──────────────┐
│ Característica│Maritimidade │Continentalidade│
├──────────────┼─────────────┼──────────────┤
│ Amplitude    │   Menor     │    Maior     │
│ Umidade      │   Alta      │    Baixa     │
│ Temperaturas │  Moderadas  │   Extremas   │
└──────────────┴─────────────┴──────────────┘
</pre>

<p>
<b>4. Massas de Ar</b>
</p>

<p>
<b>Definição:</b> grandes porções de ar com características uniformes (temperatura, umidade)
</p>

<p>
<b>Classificação:</b>
</p>

<p>
<b>Quanto à origem:</b>
</p>
<ul class="org-ul">
<li><b>Continental (c):</b> formadas sobre continentes (secas)</li>
<li><b>Marítima (m):</b> formadas sobre oceanos (úmidas)</li>
</ul>

<p>
<b>Quanto à temperatura:</b>
</p>
<ul class="org-ul">
<li><b>Equatorial (E):</b> quentes</li>
<li><b>Tropical (T):</b> quentes</li>
<li><b>Polar (P):</b> frias</li>
<li><b>Ártica/Antártica (A):</b> muito frias</li>
</ul>

<p>
<b>Exemplos no Brasil:</b>
</p>
<ul class="org-ul">
<li><b>mEc (massa Equatorial continental):</b> quente e úmida, Amazônia</li>
<li><b>mTa (massa Tropical atlântica):</b> quente e úmida, litoral</li>
<li><b>mPa (massa Polar atlântica):</b> fria e úmida, frentes frias</li>
</ul>

<p>
<b>5. Correntes Marítimas</b>
</p>

<p>
<b>Definição:</b> deslocamentos de água nos oceanos
</p>

<p>
<b>Tipos:</b>
</p>

<p>
<b>Correntes quentes:</b>
</p>
<ul class="org-ul">
<li>Fluem do Equador aos polos</li>
<li>Aumentam temperatura e umidade</li>
<li>Ex: Corrente do Brasil</li>
</ul>

<p>
<b>Correntes frias:</b>
</p>
<ul class="org-ul">
<li>Fluem dos polos ao Equador</li>
<li>Diminuem temperatura e umidade</li>
<li>Ex: Corrente de Humboldt (Peru), Benguela (África)</li>
</ul>

<p>
<b>6. Vegetação</b>
</p>

<p>
<b>Influência:</b>
</p>
<ul class="org-ul">
<li>Maior evapotranspiração → maior umidade</li>
<li>Reduz amplitude térmica</li>
<li>Florestas retêm mais umidade que áreas desmatadas</li>
</ul>

<p>
<b>7. Relevo</b>
</p>

<p>
<b>Influência:</b>
</p>
<ul class="org-ul">
<li><b>Altitude:</b> ↑ altitude → ↓ temperatura</li>
<li><b>Chuvas orográficas:</b> montanhas forçam ar a subir</li>
<li><b>Barreira:</b> impede passagem de massas de ar</li>
</ul>
</div>
</div>

<div id="outline-container-orgc22e231" class="outline-4">
<h4 id="orgc22e231"><span class="section-number-4">5.4.4.</span> Tipos Climáticos</h4>
<div class="outline-text-4" id="text-5-4-4">
<p>
<b>Principais climas do mundo:</b>
</p>

<p>
<b>1. Clima Equatorial</b>
</p>

<p>
<b>Localização:</b> próximo ao Equador (0°)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Temperatura: alta o ano todo (24-27°C)</li>
<li>Amplitude térmica: muito baixa (&lt;3°C)</li>
<li>Precipitação: abundante (&gt;2000 mm/ano)</li>
<li>Chuvas: bem distribuídas o ano todo</li>
</ul>

<p>
<b>Vegetação:</b> Floresta Equatorial (Amazônia, Congo)
</p>

<p>
<b>2. Clima Tropical</b>
</p>

<p>
<b>Localização:</b> entre Trópicos e Equador
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Temperatura: alta (20-28°C)</li>
<li>Amplitude térmica: baixa</li>
<li>Precipitação: 1000-2000 mm/ano</li>
<li><b>Duas estações:</b> verão chuvoso, inverno seco</li>
</ul>

<p>
<b>Vegetação:</b> Savanas, Cerrado
</p>

<p>
<b>3. Clima Subtropical</b>
</p>

<p>
<b>Localização:</b> entre Trópicos e Círculos Polares
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Temperatura: moderada (10-20°C)</li>
<li>Amplitude térmica: média a alta</li>
<li>Precipitação: bem distribuída (1000-2000 mm)</li>
<li><b>Quatro estações bem definidas</b></li>
</ul>

<p>
<b>Vegetação:</b> Florestas temperadas, campos
</p>

<p>
<b>4. Clima Temperado</b>
</p>

<p>
<b>Localização:</b> latitudes médias (40-60°)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Temperatura: verões quentes, invernos frios</li>
<li>Amplitude térmica: alta</li>
<li>Precipitação: variável</li>
<li><b>Quatro estações distintas</b></li>
</ul>

<p>
<b>5. Clima Desértico (Árido)</b>
</p>

<p>
<b>Localização:</b> faixas tropicais, continentes
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Temperatura: altas durante o dia, baixas à noite</li>
<li>Amplitude térmica: muito alta (diária)</li>
<li>Precipitação: &lt;250 mm/ano</li>
<li>Ar muito seco</li>
</ul>

<p>
<b>Vegetação:</b> Xerófitas (cactos), vegetação esparsa
</p>

<p>
<b>Exemplos:</b> Saara, Atacama, desertos australianos
</p>

<p>
<b>6. Clima Polar</b>
</p>

<p>
<b>Localização:</b> regiões polares (&gt;66,5° lat)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Temperatura: muito baixas (&lt;0°C)</li>
<li>Amplitude térmica: moderada</li>
<li>Precipitação: baixa (neve)</li>
<li>Verão muito curto</li>
</ul>

<p>
<b>Vegetação:</b> Tundra ou ausente (gelo permanente)
</p>
</div>
</div>

<div id="outline-container-orgba62920" class="outline-4">
<h4 id="orgba62920"><span class="section-number-4">5.4.5.</span> Climas do Brasil</h4>
<div class="outline-text-4" id="text-5-4-5">
<p>
<b>Brasil:</b> clima predominantemente <b>quente</b> (baixa latitude)
</p>

<p>
<b>Principais tipos:</b>
</p>

<p>
<b>1. Equatorial:</b>
</p>
<ul class="org-ul">
<li>Região Norte (Amazônia)</li>
<li>Quente e úmido o ano todo</li>
<li>Chuvas abundantes</li>
</ul>

<p>
<b>2. Tropical:</b>
</p>
<ul class="org-ul">
<li>Centro-Oeste, parte do Nordeste e Sudeste</li>
<li>Verão chuvoso, inverno seco</li>
<li>Temperatura alta</li>
</ul>

<p>
<b>3. Tropical Semiárido:</b>
</p>
<ul class="org-ul">
<li>Sertão nordestino</li>
<li>Quente e seco</li>
<li>Chuvas escassas e irregulares</li>
</ul>

<p>
<b>4. Tropical de Altitude:</b>
</p>
<ul class="org-ul">
<li>Regiões elevadas do Sudeste</li>
<li>Temperaturas mais amenas (altitude)</li>
<li>Verão chuvoso, inverno seco</li>
</ul>

<p>
<b>5. Subtropical:</b>
</p>
<ul class="org-ul">
<li>Sul do Brasil</li>
<li>Quatro estações</li>
<li>Chuvas bem distribuídas</li>
<li>Geadas no inverno</li>
</ul>
</div>
</div>

<div id="outline-container-orgb2c6e4d" class="outline-4">
<h4 id="orgb2c6e4d"><span class="section-number-4">5.4.6.</span> Mudanças Climáticas</h4>
<div class="outline-text-4" id="text-5-4-6">
<p>
<b>Aquecimento global:</b>
</p>
<ul class="org-ul">
<li>Aumento da temperatura média da Terra</li>
<li>Causas: emissão de gases estufa (CO₂, CH₄)</li>
<li>Consequências: derretimento de geleiras, elevação do nível do mar, eventos extremos</li>
</ul>

<p>
<b>Efeito estufa:</b>
</p>
<ul class="org-ul">
<li>Natural: retém calor, torna Terra habitável</li>
<li>Intensificado: atividades humanas aumentam gases estufa</li>
</ul>
</div>
</div>

<div id="outline-container-org0e09000" class="outline-4">
<h4 id="org0e09000"><span class="section-number-4">5.4.7.</span> Exercícios de Fixação</h4>
<div class="outline-text-4" id="text-5-4-7">
</div>
<div id="outline-container-orgadcb8e8" class="outline-5">
<h5 id="orgadcb8e8"><span class="section-number-5">5.4.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-4-7-1">
<p>
Qual a diferença entre tempo atmosférico e clima?
</p>

<p>
<i>[Ver resposta 76 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org59494e7" class="outline-5">
<h5 id="org59494e7"><span class="section-number-5">5.4.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-4-7-2">
<p>
Por que regiões de grande altitude têm temperaturas mais baixas?
</p>

<p>
<i>[Ver resposta 77 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7f9c44c" class="outline-5">
<h5 id="org7f9c44c"><span class="section-number-5">5.4.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-4-7-3">
<p>
Qual a diferença entre maritimidade e continentalidade?
</p>

<p>
<i>[Ver resposta 78 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgd65531b" class="outline-5">
<h5 id="orgd65531b"><span class="section-number-5">5.4.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-4-7-4">
<p>
Quais são os três tipos de chuva?
</p>

<p>
<i>[Ver resposta 79 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org0b35012" class="outline-5">
<h5 id="org0b35012"><span class="section-number-5">5.4.7.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-4-7-5">
<p>
(UFMG) Por que o litoral tem clima mais ameno que o interior?
</p>

<p>
<i>[Ver resposta 80 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org6d37133" class="outline-4">
<h4 id="org6d37133"><span class="section-number-4">5.4.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-4-8">
<ol class="org-ol">
<li><b>Tempo ≠ Clima:</b> tempo é momentâneo, clima é padrão</li>
<li><b>Elementos:</b> temperatura, pressão, umidade, precipitação, vento</li>
<li><b>Fatores:</b> latitude, altitude, maritimidade, massas de ar, correntes</li>
<li><b>Altitude:</b> ↑ altitude → ↓ temperatura</li>
<li><b>Latitude:</b> ↑ latitude → ↓ temperatura</li>
<li><b>Maritimidade:</b> menor amplitude térmica</li>
<li><b>3 tipos de chuva:</b> convectiva, orográfica, frontal</li>
<li><b>Brasil:</b> predominantemente tropical/quente</li>
</ol>
</div>
</div>

<div id="outline-container-orgaa47c3f" class="outline-4">
<h4 id="orgaa47c3f"><span class="section-number-4">5.4.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-4-9">
<p>
<b>Elementos Climáticos:</b>
</p>
<ul class="org-ul">
<li>Temperatura, pressão, umidade, precipitação, vento</li>
</ul>

<p>
<b>Fatores Climáticos:</b>
</p>
<ul class="org-ul">
<li>Latitude, altitude, maritimidade/continentalidade</li>
<li>Massas de ar, correntes marítimas, relevo, vegetação</li>
</ul>

<p>
<b>Tipos de Chuva:</b>
</p>
<ul class="org-ul">
<li>Convectiva: aquecimento</li>
<li>Orográfica: montanha</li>
<li>Frontal: massas de ar</li>
</ul>

<p>
<b>Climas:</b>
</p>
<ul class="org-ul">
<li>Equatorial: quente e úmido sempre</li>
<li>Tropical: 2 estações (chuvoso/seco)</li>
<li>Desértico: seco (&lt;250mm)</li>
<li>Polar: muito frio</li>
</ul>
</div>
</div>

<div id="outline-container-orgb1d103f" class="outline-4">
<h4 id="orgb1d103f"><span class="section-number-4">5.4.10.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-4-10">
<pre class="example" id="orgc2ed281">
ELEMENTOS vs FATORES:

ELEMENTOS (o que medir):
🌡️ Temperatura
📊 Pressão
💧 Umidade
🌧️ Precipitação
💨 Vento

FATORES (o que influencia):
🌍 Latitude
⛰️ Altitude
🌊 Maritimidade
☁️ Massas de ar
🌊 Correntes marítimas

TIPOS DE CHUVA:

Convectiva:        Orográfica:        Frontal:
    ☁️                 ☁️              ☁️ ☁️
    ↑              ↗️  ↑              ← →
  [solo]         [/montanha]      [massa][massa]
  quente                          fria  quente

ZONAS TÉRMICAS:
90°N ─── Polar ❄️
66,5°N ─ Temperada 🍂
23,5°N ─ Tropical ☀️
0° ───── Equatorial 🔥
23,5°S ─ Tropical ☀️
66,5°S ─ Temperada 🍂
90°S ─── Polar ❄️

CLIMAS DO BRASIL:
Norte: Equatorial 🌳
Nordeste interior: Semiárido 🌵
Centro-Oeste: Tropical 🌾
Sudeste: Tropical/Altitude ☀️⛰️
Sul: Subtropical 🍃
</pre>
</div>
</div>

<div id="outline-container-org5ab36ef" class="outline-4">
<h4 id="org5ab36ef"><span class="section-number-4">5.4.11.</span> Tabela Resumo dos Climas</h4>
<div class="outline-text-4" id="text-5-4-11">
<pre class="example" id="orgaa25c27">
┌───────────┬──────────┬───────────┬─────────────┐
│   Clima   │   Temp   │   Chuva   │  Vegetação  │
├───────────┼──────────┼───────────┼─────────────┤
│Equatorial │Sempre alta│Abundante │Floresta densa│
│           │ (&gt;24°C)  │ano todo   │             │
│           │          │           │             │
│Tropical   │  Alta    │2 estações │Savana/Cerrado│
│           │ (20-28°C)│verão chuvoso│           │
│           │          │           │             │
│Desértico  │Extremos  │&lt;250mm/ano │Xerófitas    │
│           │dia/noite │           │             │
│           │          │           │             │
│Subtropical│Moderada  │Bem distrib│Floresta/Campo│
│           │4 estações│           │             │
│           │          │           │             │
│Polar      │Muito fria│Baixa(neve)│Tundra/Gelo  │
│           │  (&lt;0°C)  │           │             │
└───────────┴──────────┴───────────┴─────────────┘
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>tema recorrente!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgfe7c2d3" class="outline-3">`;

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
