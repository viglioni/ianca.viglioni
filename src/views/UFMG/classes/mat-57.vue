<script setup lang="ts">
import { ref } from "vue";

const code = "mat-57";
const title = "Matemática: Unidades de Medida e Conversões";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-1">
<ul class="org-ul">
<li>Matemática: Unidades de Medida e Conversões</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgdacbbc2" class="outline-4">
<h4 id="orgdacbbc2"><span class="section-number-4">5.1.1.</span> Sistema Internacional de Unidades (SI)</h4>
<div class="outline-text-4" id="text-5-1-1">
<p>
<b>SI:</b> sistema padrão de medidas usado mundialmente (exceto EUA)
</p>

<p>
<b>Grandezas fundamentais:</b>
</p>

<pre class="example" id="org36b5c64">
┌──────────────┬─────────┬─────────┐
│  Grandeza    │ Unidade │ Símbolo │
├──────────────┼─────────┼─────────┤
│ Comprimento  │  metro  │    m    │
│ Massa        │quilograma│   kg    │
│ Tempo        │ segundo │    s    │
│ Temperatura  │ kelvin  │    K    │
│ Corrente     │ ampere  │    A    │
│ Intensidade  │ candela │   cd    │
│ Quantidade   │   mol   │   mol   │
└──────────────┴─────────┴─────────┘
</pre>
</div>
</div>

<div id="outline-container-org4282425" class="outline-4">
<h4 id="org4282425"><span class="section-number-4">5.1.2.</span> Prefixos do SI</h4>
<div class="outline-text-4" id="text-5-1-2">
<p>
<b>Múltiplos e submúltiplos:</b>
</p>

<pre class="example" id="org0058a40">
┌────────┬────────┬───────────┐
│Prefixo │Símbolo │   Valor   │
├────────┼────────┼───────────┤
│  kilo  │   k    │   10³     │
│  hecto │   h    │   10²     │
│  deca  │   da   │   10¹     │
├────────┼────────┼───────────┤
│  BASE  │   -    │   10⁰     │
├────────┼────────┼───────────┤
│  deci  │   d    │   10⁻¹    │
│  centi │   c    │   10⁻²    │
│  mili  │   m    │   10⁻³    │
└────────┴────────┴───────────┘
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>1 km = 1000 m (quilo = mil)</li>
<li>1 m = 100 cm (centi = centésimo)</li>
<li>1 m = 1000 mm (mili = milésimo)</li>
</ul>
</div>
</div>

<div id="outline-container-org9de59e0" class="outline-4">
<h4 id="org9de59e0"><span class="section-number-4">5.1.3.</span> Comprimento</h4>
<div class="outline-text-4" id="text-5-1-3">
<p>
<b>Unidade SI:</b> metro (m)
</p>

<p>
<b>Conversões:</b>
</p>

<pre class="example" id="org118e34d">
km → hm → dam → m → dm → cm → mm
×10  ×10  ×10   ×10  ×10  ×10
</pre>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>1 km = 1000 m</b>
</p>
<ul class="org-ul">
<li>Para converter: km → m (×1000)</li>
<li>2,5 km = 2500 m</li>
</ul>

<p>
<b>1 m = 100 cm</b>
</p>
<ul class="org-ul">
<li>Para converter: m → cm (×100)</li>
<li>1,5 m = 150 cm</li>
</ul>

<p>
<b>1 m = 1000 mm</b>
</p>
<ul class="org-ul">
<li>Para converter: m → mm (×1000)</li>
<li>0,5 m = 500 mm</li>
</ul>

<p>
<b>1 cm = 10 mm</b>
</p>
<ul class="org-ul">
<li>Para converter: cm → mm (×10)</li>
<li>2,3 cm = 23 mm</li>
</ul>

<p>
<b>Regra prática:</b>
</p>
<ul class="org-ul">
<li>Cada “casa” = ×10 (para direita) ou ÷10 (para esquerda)</li>
<li>km → m: 3 casas → ×10³ = ×1000</li>
<li>m → mm: 3 casas → ×10³ = ×1000</li>
</ul>
</div>
</div>

<div id="outline-container-org81ee8bb" class="outline-4">
<h4 id="org81ee8bb"><span class="section-number-4">5.1.4.</span> Área</h4>
<div class="outline-text-4" id="text-5-1-4">
<p>
<b>Unidade SI:</b> metro quadrado (m²)
</p>

<p>
<b>Conversões:</b>
</p>

<pre class="example" id="orgf62470c">
km² → hm² → dam² → m² → dm² → cm² → mm²
×100  ×100  ×100   ×100  ×100  ×100
</pre>

<p>
<b>Importante:</b> Cada “casa” = ×100 (não ×10!)
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>1 m² = 10.000 cm²</b>
</p>
<ul class="org-ul">
<li>m² → cm²: 2 casas → ×100² = ×10.000</li>
<li>2 m² = 20.000 cm²</li>
</ul>

<p>
<b>1 km² = 1.000.000 m²</b>
</p>
<ul class="org-ul">
<li>km² → m²: 3 casas → ×100³ = ×1.000.000</li>
</ul>

<p>
<b>1 hectare (ha) = 10.000 m²</b>
</p>
<ul class="org-ul">
<li>Usado para terrenos, fazendas</li>
<li>1 ha = 100 m × 100 m</li>
</ul>

<p>
<b>1 m² = 1.000.000 mm²</b>
</p>
<ul class="org-ul">
<li>m² → mm²: 3 casas → ×100³ = ×1.000.000</li>
</ul>
</div>
</div>

<div id="outline-container-org7bdedb6" class="outline-4">
<h4 id="org7bdedb6"><span class="section-number-4">5.1.5.</span> Volume</h4>
<div class="outline-text-4" id="text-5-1-5">
<p>
<b>Unidade SI:</b> metro cúbico (m³)
</p>

<p>
<b>Conversões:</b>
</p>

<pre class="example" id="orgf8802ee">
km³ → hm³ → dam³ → m³ → dm³ → cm³ → mm³
×1000 ×1000 ×1000  ×1000 ×1000 ×1000
</pre>

<p>
<b>Importante:</b> Cada “casa” = ×1000 (não ×10!)
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>1 m³ = 1000 dm³</b>
</p>
<ul class="org-ul">
<li>m³ → dm³: 1 casa → ×1000</li>
</ul>

<p>
<b>1 m³ = 1.000.000 cm³</b>
</p>
<ul class="org-ul">
<li>m³ → cm³: 2 casas → ×1000² = ×1.000.000</li>
</ul>

<p>
<b>Relação com litro:</b>
</p>

<pre class="example" id="org1b933c2">
1 m³ = 1000 L (litros)
1 dm³ = 1 L
1 cm³ = 1 mL (mililitro)
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>2 m³ = 2000 L</li>
<li>500 cm³ = 500 mL = 0,5 L</li>
</ul>
</div>
</div>

<div id="outline-container-orgc9a278e" class="outline-4">
<h4 id="orgc9a278e"><span class="section-number-4">5.1.6.</span> Massa</h4>
<div class="outline-text-4" id="text-5-1-6">
<p>
<b>Unidade SI:</b> quilograma (kg)
</p>

<p>
<b>Conversões:</b>
</p>

<pre class="example" id="orge16c4d5">
kg → hg → dag → g → dg → cg → mg
×10  ×10  ×10  ×10  ×10  ×10
</pre>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>1 kg = 1000 g</b>
</p>
<ul class="org-ul">
<li>kg → g: 3 casas → ×10³ = ×1000</li>
<li>2,5 kg = 2500 g</li>
</ul>

<p>
<b>1 g = 1000 mg</b>
</p>
<ul class="org-ul">
<li>g → mg: 3 casas → ×10³ = ×1000</li>
<li>0,5 g = 500 mg</li>
</ul>

<p>
<b>Tonelada:</b>
</p>

<pre class="example" id="org78e4a8a">
1 t = 1000 kg
</pre>

<p>
<b>Atenção:</b> Massa ≠ Peso
</p>
<ul class="org-ul">
<li>Massa: quantidade de matéria (kg)</li>
<li>Peso: força da gravidade (N, newtons)</li>
</ul>
</div>
</div>

<div id="outline-container-orgbd34fb8" class="outline-4">
<h4 id="orgbd34fb8"><span class="section-number-4">5.1.7.</span> Tempo</h4>
<div class="outline-text-4" id="text-5-1-7">
<p>
<b>Unidade SI:</b> segundo (s)
</p>

<p>
<b>Conversões:</b>
</p>

<pre class="example" id="orgc08f44b">
1 min = 60 s
1 h = 60 min = 3600 s
1 dia = 24 h = 1440 min = 86.400 s
</pre>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>2,5 h em minutos:</b> 2,5 h = 2,5 × 60 = 150 min
</p>

<p>
<b>90 min em horas:</b> 90 min = 90 ÷ 60 = 1,5 h
</p>

<p>
<b>2 h 30 min em segundos:</b> 2 h 30 min = (2 × 3600) + (30 × 60) = 7200 + 1800 = 9000 s
</p>
</div>
</div>

<div id="outline-container-orgacc28a4" class="outline-4">
<h4 id="orgacc28a4"><span class="section-number-4">5.1.8.</span> Velocidade</h4>
<div class="outline-text-4" id="text-5-1-8">
<p>
<b>Unidade SI:</b> metro por segundo (m/s)
</p>

<p>
<b>Conversão km/h ↔ m/s:</b>
</p>

<pre class="example" id="org6e8d1fe">
km/h → m/s: dividir por 3,6
m/s → km/h: multiplicar por 3,6
</pre>

<p>
<b>Por quê?</b>
</p>
<ul class="org-ul">
<li>1 km = 1000 m</li>
<li>1 h = 3600 s</li>
<li>1 km/h = 1000 m / 3600 s = 1/3,6 m/s</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>72 km/h em m/s:</b> 72 km/h = 72 ÷ 3,6 = 20 m/s
</p>

<p>
<b>10 m/s em km/h:</b> 10 m/s = 10 × 3,6 = 36 km/h
</p>

<p>
<b>108 km/h em m/s:</b> 108 km/h = 108 ÷ 3,6 = 30 m/s
</p>
</div>
</div>

<div id="outline-container-orge8008de" class="outline-4">
<h4 id="orge8008de"><span class="section-number-4">5.1.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-1-9">
</div>
<div id="outline-container-org5103e9a" class="outline-5">
<h5 id="org5103e9a"><span class="section-number-5">5.1.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-1-9-1">
<p>
Converta 3,5 km em metros.
</p>

<p>
<b>Solução:</b> km → m: ×1000 3,5 km = 3,5 × 1000 = 3500 m
</p>

<p>
<i>[Ver resposta 55 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org366ef15" class="outline-5">
<h5 id="org366ef15"><span class="section-number-5">5.1.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-1-9-2">
<p>
Converta 250 cm em metros.
</p>

<p>
<b>Solução:</b> cm → m: ÷100 250 cm = 250 ÷ 100 = 2,5 m
</p>

<p>
<i>[Ver resposta 56 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org0abdf53" class="outline-5">
<h5 id="org0abdf53"><span class="section-number-5">5.1.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-1-9-3">
<p>
Quantos cm² há em 2 m²?
</p>

<p>
<b>Solução:</b> m² → cm²: ×10.000 (2 casas) 2 m² = 2 × 10.000 = 20.000 cm²
</p>

<p>
<i>[Ver resposta 57 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgcb343d5" class="outline-5">
<h5 id="orgcb343d5"><span class="section-number-5">5.1.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-1-9-4">
<p>
Converta 5000 mL em litros.
</p>

<p>
<b>Solução:</b> 1 mL = 0,001 L 5000 mL = 5000 × 0,001 = 5 L
</p>

<p>
Ou: 1000 mL = 1 L 5000 mL = 5000 ÷ 1000 = 5 L
</p>

<p>
<i>[Ver resposta 58 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org5fa5109" class="outline-5">
<h5 id="org5fa5109"><span class="section-number-5">5.1.9.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-1-9-5">
<p>
Converta 2,5 t (toneladas) em kg.
</p>

<p>
<b>Solução:</b> 1 t = 1000 kg 2,5 t = 2,5 × 1000 = 2500 kg
</p>

<p>
<i>[Ver resposta 59 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org2969509" class="outline-5">
<h5 id="org2969509"><span class="section-number-5">5.1.9.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-5-1-9-6">
<p>
Converta 90 km/h em m/s.
</p>

<p>
<b>Solução:</b> km/h → m/s: ÷3,6 90 km/h = 90 ÷ 3,6 = 25 m/s
</p>

<p>
<i>[Ver resposta 60 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orge0b5bad" class="outline-5">
<h5 id="orge0b5bad"><span class="section-number-5">5.1.9.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-5-1-9-7">
<p>
Um terreno tem área de 2 hectares. Quantos m²?
</p>

<p>
<b>Solução:</b> 1 ha = 10.000 m² 2 ha = 2 × 10.000 = 20.000 m²
</p>

<p>
<i>[Ver resposta 61 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7d1c8cf" class="outline-5">
<h5 id="org7d1c8cf"><span class="section-number-5">5.1.9.8.</span> Exercício 8</h5>
<div class="outline-text-5" id="text-5-1-9-8">
<p>
Converta 2 h 15 min em minutos.
</p>

<p>
<b>Solução:</b> 2 h = 2 × 60 = 120 min Total: 120 + 15 = 135 min
</p>

<p>
<i>[Ver resposta 62 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org53e9ece" class="outline-4">
<h4 id="org53e9ece"><span class="section-number-4">5.1.10.</span> Outras Unidades Importantes</h4>
<div class="outline-text-4" id="text-5-1-10">
<p>
<b>Temperatura:</b>
</p>

<pre class="example" id="org7a9a7ee">
Celsius (°C) ↔ Kelvin (K):
K = °C + 273
°C = K
- 273
</pre>

<p>
<b>Pressão:</b>
</p>

<pre class="example" id="org6ab6241">
1 atm = 101.325 Pa
1 atm = 760 mmHg
1 bar = 10⁵ Pa
</pre>

<p>
<b>Energia:</b>
</p>

<pre class="example" id="org1c218b1">
1 cal = 4,18 J (joule)
1 kcal = 1000 cal
1 kWh = 3,6 × 10⁶ J
</pre>
</div>
</div>

<div id="outline-container-orgb2eeaf6" class="outline-4">
<h4 id="orgb2eeaf6"><span class="section-number-4">5.1.11.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-1-11">
<ol class="org-ol">
<li><b>Comprimento:</b> cada casa = ×10 ou ÷10</li>
<li><b>Área:</b> cada casa = ×100 ou ÷100</li>
<li><b>Volume:</b> cada casa = ×1000 ou ÷1000</li>
<li><b>1 L = 1 dm³ = 1000 cm³ = 1000 mL</b></li>
<li><b>1 m³ = 1000 L</b></li>
<li><b>km/h → m/s: ÷3,6</b></li>
<li><b>m/s → km/h: ×3,6</b></li>
<li><b>1 ha = 10.000 m²</b></li>
<li><b>1 t = 1000 kg</b></li>
<li><b>Sempre verificar unidades no problema</b></li>
</ol>
</div>
</div>

<div id="outline-container-org6117d6c" class="outline-4">
<h4 id="org6117d6c"><span class="section-number-4">5.1.12.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-1-12">
<p>
<b>Prefixos:</b>
</p>
<ul class="org-ul">
<li>kilo (k) = 1000</li>
<li>centi (c) = 0,01 (centésimo)</li>
<li>mili (m) = 0,001 (milésimo)</li>
</ul>

<p>
<b>Conversões importantes:</b>
</p>
<ul class="org-ul">
<li>1 km = 1000 m</li>
<li>1 m = 100 cm = 1000 mm</li>
<li>1 m² = 10.000 cm²</li>
<li>1 m³ = 1000 L</li>
<li>1 L = 1000 mL</li>
<li>1 kg = 1000 g</li>
<li>1 h = 3600 s</li>
</ul>

<p>
<b>Velocidade:</b>
</p>
<ul class="org-ul">
<li>km/h ÷ 3,6 = m/s</li>
<li>m/s × 3,6 = km/h</li>
</ul>
</div>
</div>

<div id="outline-container-orgfc5dd05" class="outline-4">
<h4 id="orgfc5dd05"><span class="section-number-4">5.1.13.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-5-1-13">
<pre class="example" id="org3e09cd1">
COMPRIMENTO (cada casa ×10):
km
- hm
- dam
- m
- dm
- cm
- mm

ÁREA (cada casa ×100):
km²
- hm²
- dam²
- m²
- dm²
- cm²
- mm²

VOLUME (cada casa ×1000):
km³
- hm³
- dam³
- m³
- dm³
- cm³
- mm³

MASSA (cada casa ×10):
kg
- hg
- dag
- g
- dg
- cg
- mg

VOLUME/CAPACIDADE:
1 m³ = 1000 L
1 dm³ = 1 L
1 cm³ = 1 mL

VELOCIDADE:
km/h → m/s: ÷3,6
m/s → km/h: ×3,6

TEMPO:
1 h = 60 min = 3600 s
1 dia = 24 h

ÁREA (especiais):
1 hectare (ha) = 10.000 m²

MASSA:
1 tonelada (t) = 1000 kg
</pre>
</div>
</div>

<div id="outline-container-org8f7def7" class="outline-4">
<h4 id="org8f7def7"><span class="section-number-4">5.1.14.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-1-14">
<pre class="example" id="orgff8e955">
ESCALA DE COMPRIMENTO:
km → hm → dam → m → dm → cm → mm
←÷10  ÷10  ÷10  ÷10  ÷10  ÷10←
→×10  ×10  ×10  ×10  ×10  ×10→

VOLUME E CAPACIDADE:
   1 m³
    │
  1000 L
    │
 1000 dm³

   1 L
    │
 1000 mL
    │
 1000 cm³

VELOCIDADE:
  km/h  ←─×3,6──  m/s
  km/h  ──÷3,6─→  m/s

EXEMPLOS:
72 km/h = 20 m/s
90 km/h = 25 m/s
108 km/h = 30 m/s
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>conversões aparecem em todas as matérias!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org1f86916" class="outline-3">`;

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
