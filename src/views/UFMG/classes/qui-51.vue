<script setup lang="ts">
import { ref } from "vue";

const code = "qui-51";
const title = "Química: Estequiometria";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-3">
<ul class="org-ul">
<li>Química: Estequiometria</li>
<li>Conceito de Mol e Massa Molar</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org39b9639" class="outline-4">
<h4 id="org39b9639"><span class="section-number-4">3.3.1.</span> O que é Estequiometria?</h4>
<div class="outline-text-4" id="text-3-3-1">
<p>
<b>Estequiometria:</b> estudo das <b>relações quantitativas</b> entre reagentes e produtos em reações químicas.
</p>

<p>
<b>Permite calcular:</b>
</p>
<ul class="org-ul">
<li>Quanto de reagente é necessário?</li>
<li>Quanto de produto será formado?</li>
<li>Qual reagente está em excesso?</li>
<li>Qual o rendimento da reação?</li>
</ul>

<p>
<b>Base:</b> Lei de Lavoisier (conservação das massas) + coeficientes das equações químicas
</p>
</div>
</div>

<div id="outline-container-orgaa25b0e" class="outline-4">
<h4 id="orgaa25b0e"><span class="section-number-4">3.3.2.</span> O Conceito de Mol</h4>
<div class="outline-text-4" id="text-3-3-2">
<p>
<b>Mol:</b> unidade de quantidade de matéria (SI)
</p>

<p>
<b>Definição:</b> <b>1 mol = 6,02 × 10²³ entidades</b> (átomos, moléculas, íons, etc.)
</p>

<p>
<b>Constante de Avogadro:</b>
</p>

<pre class="example" id="org940b675">
N_A = 6,02 × 10²³ /mol
</pre>

<p>
<b>Analogias:</b>
</p>
<ul class="org-ul">
<li>1 dúzia = 12 unidades</li>
<li>1 resma = 500 folhas</li>
<li><b>1 mol = 6,02 × 10²³ entidades</b></li>
</ul>

<p>
<b>Por que usar mol?</b>
</p>
<ul class="org-ul">
<li>Átomos são extremamente pequenos</li>
<li>Impossível contar individualmente</li>
<li>Mol permite trabalhar com quantidades macroscópicas</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>1 mol de átomos de carbono = 6,02 × 10²³ átomos de C</li>
<li>1 mol de moléculas de H₂O = 6,02 × 10²³ moléculas de H₂O</li>
<li>1 mol de íons Na⁺ = 6,02 × 10²³ íons Na⁺</li>
</ul>
</div>
</div>

<div id="outline-container-org068d8ad" class="outline-4">
<h4 id="org068d8ad"><span class="section-number-4">3.3.3.</span> Massa Atômica e Massa Molecular</h4>
<div class="outline-text-4" id="text-3-3-3">
<p>
<b>Massa Atômica (MA):</b>
</p>
<ul class="org-ul">
<li>Massa de 1 átomo do elemento</li>
<li>Unidade: <b>u</b> (unidade de massa atômica)</li>
<li>Encontrada na <b>tabela periódica</b></li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>H = 1 u</li>
<li>C = 12 u</li>
<li>O = 16 u</li>
<li>Na = 23 u</li>
<li>Cl = 35,5 u</li>
</ul>

<p>
<b>Massa Molecular (MM):</b>
</p>
<ul class="org-ul">
<li>Soma das massas atômicas dos átomos na molécula</li>
<li>Unidade: u</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>H₂O:</b> MM = 2×H + 1×O = 2×1 + 1×16 = 18 u
</p>

<p>
<b>CO₂:</b> MM = 1×C + 2×O = 1×12 + 2×16 = 44 u
</p>

<p>
<b>H₂SO₄:</b> MM = 2×1 + 1×32 + 4×16 = 2 + 32 + 64 = 98 u
</p>

<p>
<b>NaCl:</b> MM = 1×23 + 1×35,5 = 58,5 u
</p>
</div>
</div>

<div id="outline-container-orga83e5d8" class="outline-4">
<h4 id="orga83e5d8"><span class="section-number-4">3.3.4.</span> Massa Molar (M)</h4>
<div class="outline-text-4" id="text-3-3-4">
<p>
<b>Massa Molar:</b> massa de 1 mol de substância
</p>

<p>
<b>Unidade: g/mol</b>
</p>

<p>
<b>Relação:</b>
</p>

<pre class="example" id="org25cdfee">
Massa molar (g/mol) = Massa molecular (u)
</pre>

<p>
<b>Apenas muda a unidade!</b>
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>H₂O: MM = 18 u → M = 18 g/mol</li>
<li><b>1 mol de H₂O = 18 g</b></li>
<li>CO₂: MM = 44 u → M = 44 g/mol</li>
<li><b>1 mol de CO₂ = 44 g</b></li>
<li>NaCl: MM = 58,5 u → M = 58,5 g/mol</li>
<li><b>1 mol de NaCl = 58,5 g</b></li>
</ul>
</div>
</div>

<div id="outline-container-org187c894" class="outline-4">
<h4 id="org187c894"><span class="section-number-4">3.3.5.</span> Relação entre Massa, Mol e Número de Partículas</h4>
<div class="outline-text-4" id="text-3-3-5">
<p>
<b>Três grandezas relacionadas:</b>
</p>

<p>
<b>1. Massa (m):</b> em gramas (g) <b>2. Quantidade de matéria (n):</b> em mols (mol) <b>3. Número de partículas (N):</b> unidades
</p>

<p>
<b>Fórmulas:</b>
</p>

<pre class="example" id="orgba47895">
n = m / M
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>n = número de mols (mol)</li>
<li>m = massa (g)</li>
<li>M = massa molar (g/mol)</li>
</ul>

<pre class="example" id="org84430e5">
N = n × N_A
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>N = número de partículas</li>
<li>n = número de mols</li>
<li>N_A = 6,02 × 10²³</li>
</ul>

<p>
<b>Combinando:</b>
</p>

<pre class="example" id="org7e0f0ba">
N = (m/M) × N_A
</pre>
</div>
</div>

<div id="outline-container-orgf5375f2" class="outline-4">
<h4 id="orgf5375f2"><span class="section-number-4">3.3.6.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-3-6">
<ul class="org-ul">
<li>Cálculos com Mol</li>
</ul>
</div>
<div id="outline-container-orgb1a6f1c" class="outline-5">
<h5 id="orgb1a6f1c"><span class="section-number-5">3.3.6.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-3-6-1">
<p>
Quantos mols há em 36 g de água (H₂O)?
</p>

<p>
<b>Dados:</b>
</p>
<ul class="org-ul">
<li>m = 36 g</li>
<li>M(H₂O) = 18 g/mol</li>
</ul>

<p>
<b>Solução:</b> n = m/M = 36/18 = 2 mol
</p>

<p>
<i>[Ver resposta 28 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgc93581e" class="outline-5">
<h5 id="orgc93581e"><span class="section-number-5">3.3.6.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-3-6-2">
<p>
Qual a massa de 0,5 mol de NaCl?
</p>

<p>
<b>Dados:</b>
</p>
<ul class="org-ul">
<li>n = 0,5 mol</li>
<li>M(NaCl) = 58,5 g/mol</li>
</ul>

<p>
<b>Solução:</b> m = n × M = 0,5 × 58,5 = 29,25 g
</p>

<p>
<i>[Ver resposta 29 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org4ba8bee" class="outline-5">
<h5 id="org4ba8bee"><span class="section-number-5">3.3.6.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-3-6-3">
<p>
Quantas moléculas há em 2 mols de CO₂?
</p>

<p>
<b>Dados:</b>
</p>
<ul class="org-ul">
<li>n = 2 mol</li>
<li>N_A = 6,02 × 10²³</li>
</ul>

<p>
<b>Solução:</b> N = n × N_A = 2 × 6,02 × 10²³ = 1,204 × 10²⁴ moléculas
</p>

<p>
<i>[Ver resposta 30 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org81782c4" class="outline-5">
<h5 id="org81782c4"><span class="section-number-5">3.3.6.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-3-6-4">
<p>
Quantos mols de átomos de carbono há em 24 g de C?
</p>

<p>
<b>Dados:</b>
</p>
<ul class="org-ul">
<li>m = 24 g</li>
<li>M(C) = 12 g/mol</li>
</ul>

<p>
<b>Solução:</b> n = m/M = 24/12 = 2 mol
</p>

<p>
<i>[Ver resposta 31 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3617247" class="outline-5">
<h5 id="org3617247"><span class="section-number-5">3.3.6.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-3-3-6-5">
<p>
(UFMG) Quantos átomos há em 4 g de hélio (He = 4 g/mol)?
</p>

<p>
<b>Solução:</b> n = m/M = 4/4 = 1 mol N = n × N_A = 1 × 6,02 × 10²³ = 6,02 × 10²³ átomos
</p>

<p>
<i>[Ver resposta 32 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgef8707d" class="outline-4">
<h4 id="orgef8707d"><span class="section-number-4">3.3.7.</span> Volume Molar de Gases (CNTP)</h4>
<div class="outline-text-4" id="text-3-3-7">
<p>
<b>CNTP:</b> Condições Normais de Temperatura e Pressão
</p>
<ul class="org-ul">
<li>Temperatura: 0°C = 273 K</li>
<li>Pressão: 1 atm = 101.325 Pa</li>
</ul>

<p>
<b>Lei de Avogadro:</b> “Volumes iguais de gases diferentes, nas mesmas condições de temperatura e pressão, contêm o mesmo número de moléculas.”
</p>

<p>
<b>Volume molar nas CNTP:</b>
</p>

<pre class="example" id="org735987a">
V_m = 22,4 L/mol
</pre>

<p>
<b>1 mol de qualquer gás ocupa 22,4 L nas CNTP</b>
</p>

<p>
<b>Relação:</b>
</p>

<pre class="example" id="org4746737">
V = n × V_m
V = n × 22,4
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>V = volume (L)</li>
<li>n = número de mols</li>
<li>V_m = 22,4 L/mol (CNTP)</li>
</ul>

<p>
<b>Exemplo:</b> 2 mols de O₂ nas CNTP ocupam: V = n × 22,4 = 2 × 22,4 = 44,8 L
</p>
</div>
</div>

<div id="outline-container-org07408be" class="outline-4">
<h4 id="org07408be"><span class="section-number-4">3.3.8.</span> Exercícios com Volume Molar</h4>
<div class="outline-text-4" id="text-3-3-8">
</div>
<div id="outline-container-org22c3226" class="outline-5">
<h5 id="org22c3226"><span class="section-number-5">3.3.8.1.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-3-3-8-1">
<p>
Qual o volume de 3 mols de N₂ nas CNTP?
</p>

<p>
<b>Solução:</b> V = n × 22,4 = 3 × 22,4 = 67,2 L
</p>

<p>
<i>[Ver resposta 33 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgd3d8edf" class="outline-5">
<h5 id="orgd3d8edf"><span class="section-number-5">3.3.8.2.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-3-3-8-2">
<p>
Quantos mols de gás há em 11,2 L nas CNTP?
</p>

<p>
<b>Solução:</b> n = V/22,4 = 11,2/22,4 = 0,5 mol
</p>

<p>
<i>[Ver resposta 34 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf1fc69d" class="outline-5">
<h5 id="orgf1fc69d"><span class="section-number-5">3.3.8.3.</span> Exercício 8</h5>
<div class="outline-text-5" id="text-3-3-8-3">
<p>
Qual a massa de 44,8 L de CO₂ nas CNTP? (M = 44 g/mol)
</p>

<p>
<b>Solução:</b> n = V/22,4 = 44,8/22,4 = 2 mol m = n × M = 2 × 44 = 88 g
</p>

<p>
<i>[Ver resposta 35 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org696adfc" class="outline-4">
<h4 id="org696adfc"><span class="section-number-4">3.3.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-3-9">
<ol class="org-ol">
<li><b>1 mol = 6,02 × 10²³ entidades</b> (Constante de Avogadro)</li>
<li><b>Massa molar (g/mol)</b> = valor numérico da massa molecular</li>
<li><b>n = m/M</b> (relação fundamental)</li>
<li><b>N = n × N_A</b> (número de partículas)</li>
<li><b>Volume molar (CNTP) = 22,4 L/mol</b></li>
<li><b>Sempre identificar: o que é dado? O que é pedido?</b></li>
<li><b>Calcular massa molar antes</b> de resolver problemas</li>
<li><b>CNTP:</b> 0°C e 1 atm</li>
</ol>
</div>
</div>

<div id="outline-container-org1a4e872" class="outline-4">
<h4 id="org1a4e872"><span class="section-number-4">3.3.10.</span> Principais Massas Molares para Memorizar</h4>
<div class="outline-text-4" id="text-3-3-10">
<pre class="example" id="org37861c0">
Elementos:
H = 1 g/mol
C = 12 g/mol
N = 14 g/mol
O = 16 g/mol
Na = 23 g/mol
S = 32 g/mol
Cl = 35,5 g/mol
Ca = 40 g/mol

Substâncias comuns:
H₂O = 18 g/mol
O₂ = 32 g/mol
CO₂ = 44 g/mol
H₂SO₄ = 98 g/mol
NaCl = 58,5 g/mol
</pre>
</div>
</div>

<div id="outline-container-org15b1f96" class="outline-4">
<h4 id="org15b1f96"><span class="section-number-4">3.3.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-3-11">
<p>
<b>Mol:</b>
</p>
<ul class="org-ul">
<li>Unidade de quantidade de matéria</li>
<li>1 mol = 6,02 × 10²³ entidades</li>
</ul>

<p>
<b>Massa Molar:</b>
</p>
<ul class="org-ul">
<li>Massa de 1 mol</li>
<li>Unidade: g/mol</li>
<li>Valor numérico = massa molecular</li>
</ul>

<p>
<b>Relações:</b>
</p>
<ul class="org-ul">
<li>n = m/M (massa ↔ mol)</li>
<li>N = n × N_A (mol ↔ partículas)</li>
<li>V = n × 22,4 (mol ↔ volume, CNTP)</li>
</ul>
</div>
</div>

<div id="outline-container-org65031a7" class="outline-4">
<h4 id="org65031a7"><span class="section-number-4">3.3.12.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-3-12">
<pre class="example" id="orgad55770">
Constante de Avogadro:
N_A = 6,02 × 10²³ /mol

Quantidade de matéria:
n = m / M

Número de partículas:
N = n × N_A

Volume de gás (CNTP):
V = n × 22,4 L

Volume molar (CNTP):
V_m = 22,4 L/mol

Massa a partir de mols:
m = n × M

Mols a partir de volume (CNTP):
n = V / 22,4

Cálculo de massa molar:
M = Σ (massa atômica × quantidade de átomos)

Exemplo:
H₂SO₄: M = 2×1 + 1×32 + 4×16 = 98 g/mol
</pre>
</div>
</div>

<div id="outline-container-orgf5b321e" class="outline-4">
<h4 id="orgf5b321e"><span class="section-number-4">3.3.13.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-3-3-13">
<pre class="example" id="org5e9b973">
TRIÂNGULO DAS GRANDEZAS:

         m (massa, g)
        /  \\
       /    \\
      /  M   \\
     /_______ \\
    n          N
  (mol)    (partículas)
  
  n = m/M
  N = n × N_A
  
CONVERSÕES:

Massa ←─────→ Mol ←─────→ Partículas
  m     n=m/M   n    N=n×N_A    N
(gramas)      (mol)            (unidades)
  
  ↓ (gases, CNTP)
  
Volume
  V = n × 22,4 L

MOL:
📦 1 mol = 6,02×10²³ entidades
📦 1 mol = Massa molar (g)
📦 1 mol gás = 22,4 L (CNTP)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para toda estequiometria!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org0bc8839" class="outline-3">`;

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
