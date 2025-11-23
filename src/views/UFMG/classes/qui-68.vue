<script setup lang="ts">
import { ref } from "vue";

const code = "qui-68";
const title = "Química: Revisão Final";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-5">
<ul class="org-ul">
<li>Química: Revisão Final</li>
<li>Estequiometria Completa</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org26b04fa" class="outline-4">
<h4 id="org26b04fa"><span class="section-number-4">2.5.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-2-5-1">
<p>
Consolidar mol, massa molar, leis ponderais e cálculos estequiométricos.
</p>
</div>
</div>

<div id="outline-container-org3a435b5" class="outline-4">
<h4 id="org3a435b5"><span class="section-number-4">2.5.2.</span> PARTE 1: Conceito de Mol</h4>
<div class="outline-text-4" id="text-2-5-2">
<p>
<b>Mol:</b> unidade de quantidade de matéria
</p>

<p>
<b>Constante de Avogadro:</b>
</p>

<pre class="example" id="org18c4f49">
1 mol = 6,02 × 10²³ entidades
N_A = 6,02 × 10²³ /mol
</pre>

<p>
<b>Massa Molar (M):</b>
</p>

<pre class="example" id="orgd55f7be">
Massa de 1 mol da substância
Unidade: g/mol
Valor numérico = massa molecular
</pre>

<p>
<b>Exemplos:</b>
</p>

<pre class="example" id="org12bb1a6">
H₂O: M = 18 g/mol
CO₂: M = 44 g/mol
NaCl: M = 58,5 g/mol
</pre>

<p>
<b>Relações fundamentais:</b>
</p>

<pre class="example" id="org13840bf">
n = m/M  (mol a partir da massa)
m = n × M  (massa a partir de mol)
N = n × N_A  (número de partículas)
</pre>

<p>
<b>Volume molar (CNTP):</b>
</p>

<pre class="example" id="org4bce5e6">
V_m = 22,4 L/mol
V = n × 22,4 L
</pre>
</div>
</div>

<div id="outline-container-org293a621" class="outline-4">
<h4 id="org293a621"><span class="section-number-4">2.5.3.</span> PARTE 2: Leis Ponderais</h4>
<div class="outline-text-4" id="text-2-5-3">
<p>
<b>1. Lei de Lavoisier (Conservação das Massas):</b>
</p>

<pre class="example" id="org4ceb7cf">
Σ m_reagentes = Σ m_produtos
</pre>

<p>
“Nada se cria, nada se perde, tudo se transforma”
</p>

<p>
<b>2. Lei de Proust (Proporções Constantes):</b>
</p>

<pre class="example" id="org24bb508">
Mesma substância, mesma proporção em massa
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgf79b672">
H₂O sempre: H:O = 1:8
2g H + 16g O → 18g H₂O
4g H + 32g O → 36g H₂O
</pre>

<p>
<b>3. Lei de Dalton (Proporções Múltiplas):</b>
</p>

<pre class="example" id="org60314e1">
Compostos diferentes, proporções inteiras
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgfe09cad">
CO:  12g C + 16g O
CO₂: 12g C + 32g O
Razão de O: 16:32 = 1:2 (inteiros!)
</pre>
</div>
</div>

<div id="outline-container-orgd17390e" class="outline-4">
<h4 id="orgd17390e"><span class="section-number-4">2.5.4.</span> PARTE 3: Cálculos Estequiométricos</h4>
<div class="outline-text-4" id="text-2-5-4">
<p>
<b>Método geral:</b>
</p>

<p>
<b>1. Escrever a equação balanceada</b> <b>2. Identificar dados e pergunta</b> <b>3. Calcular massas molares necessárias</b> <b>4. Usar proporção estequiométrica</b> <b>5. Resolver por regra de três</b>
</p>

<p>
<b>Exemplo completo:</b>
</p>

<p>
<b>Reação:</b> 2 H₂ + O₂ → 2 H₂O
</p>

<p>
Quantos gramas de H₂O são produzidos a partir de 8 g de H₂?
</p>

<p>
<b>Passo 1:</b> Equação balanceada ✓
</p>

<p>
<b>Passo 2:</b> Dados:
</p>
<ul class="org-ul">
<li>m(H₂) = 8 g</li>
<li>m(H₂O) = ?</li>
</ul>

<p>
<b>Passo 3:</b> Massas molares:
</p>
<ul class="org-ul">
<li>M(H₂) = 2 g/mol</li>
<li>M(H₂O) = 18 g/mol</li>
</ul>

<p>
<b>Passo 4:</b> Proporção estequiométrica:
</p>

<pre class="example" id="org2ce3bcb">
2 H₂ : 2 H₂O
2 mol : 2 mol
</pre>

<p>
Em massa:
</p>

<pre class="example" id="org0ec81ff">
2 × 2g : 2 × 18g
4g : 36g
</pre>

<p>
<b>Passo 5:</b> Regra de três:
</p>

<pre class="example" id="org33f0c1c">
4 g H₂  ──  36 g H₂O
8 g H₂  ──  x

x = (8 × 36)/4 = 72 g
</pre>

<p>
<i>[Ver resposta 5 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org098e4da" class="outline-4">
<h4 id="org098e4da"><span class="section-number-4">2.5.5.</span> PARTE 4: Tipos de Cálculos</h4>
<div class="outline-text-4" id="text-2-5-5">
<p>
<b>1. Massa → Massa</b>
</p>

<p>
<b>Exemplo:</b> N₂ + 3 H₂ → 2 NH₃
</p>

<p>
Quantos gramas de NH₃ são produzidos a partir de 28 g de N₂?
</p>

<pre class="example" id="orgd1307f3">
M(N₂) = 28 g/mol
M(NH₃) = 17 g/mol

Proporção:
1 mol N₂ : 2 mol NH₃
28 g N₂ : 34 g NH₃

28 g N₂ ── 34 g NH₃
28 g N₂ ── x

x = 34 g NH₃
</pre>

<p>
<b>2. Massa → Volume (CNTP)</b>
</p>

<p>
<b>Exemplo:</b> CaCO₃ → CaO + CO₂
</p>

<p>
Qual o volume de CO₂ produzido a partir de 100 g de CaCO₃? (CNTP)
</p>

<pre class="example" id="org4901361">
M(CaCO₃) = 100 g/mol

n(CaCO₃) = 100/100 = 1 mol

Proporção: 1 mol CaCO₃ → 1 mol CO₂

n(CO₂) = 1 mol
V = 1 × 22,4 = 22,4 L
</pre>

<p>
<b>3. Volume → Volume (CNTP)</b>
</p>

<p>
<b>Exemplo:</b> N₂ + 3 H₂ → 2 NH₃
</p>

<p>
Qual o volume de NH₃ produzido a partir de 60 L de H₂? (CNTP)
</p>

<pre class="example" id="orgcdf0836">
Proporção:
3 H₂ : 2 NH₃
3 volumes : 2 volumes

3 L H₂ ── 2 L NH₃
60 L H₂ ── x

x = (60 × 2)/3 = 40 L NH₃
</pre>

<p>
<b>4. Pureza</b>
</p>

<p>
Quando o reagente não é 100% puro:
</p>

<p>
<b>Exemplo:</b> 200 g de calcário com 90% de CaCO₃. Qual a massa pura?
</p>

<pre class="example" id="orga6ad75b">
m_pura = m_total × pureza%
m_pura = 200 × 0,90 = 180 g de CaCO₃
</pre>

<p>
<b>5. Rendimento</b>
</p>

<p>
Quando a reação não é completa:
</p>

<pre class="example" id="org9b9e2e2">
Rendimento = (massa obtida / massa teórica) × 100%
</pre>

<p>
<b>Exemplo:</b> Teoria prevê 50 g, obteve-se 40 g.
</p>

<pre class="example" id="orgc5eecdb">
Rendimento = (40/50) × 100% = 80%
</pre>
</div>
</div>

<div id="outline-container-org625c06d" class="outline-4">
<h4 id="org625c06d"><span class="section-number-4">2.5.6.</span> Questões de Fixação Rápida</h4>
<div class="outline-text-4" id="text-2-5-6">
</div>
<div id="outline-container-org71513a7" class="outline-5">
<h5 id="org71513a7"><span class="section-number-5">2.5.6.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-2-5-6-1">
<p>
Quantos mols há em 44 g de CO₂? (M = 44 g/mol)
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org49b2a6f">
n = m/M = 44/44 = 1 mol
</pre>
</div>
</div>

<div id="outline-container-org4665f6d" class="outline-5">
<h5 id="org4665f6d"><span class="section-number-5">2.5.6.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-2-5-6-2">
<p>
Qual a massa de 2 mols de H₂O? (M = 18 g/mol)
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org4f578f9">
m = n × M = 2 × 18 = 36 g
</pre>
</div>
</div>

<div id="outline-container-org8f0c0f7" class="outline-5">
<h5 id="org8f0c0f7"><span class="section-number-5">2.5.6.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-2-5-6-3">
<p>
Quantas moléculas há em 0,5 mol de qualquer substância?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgfd89529">
N = n × N_A = 0,5 × 6,02×10²³ = 3,01×10²³ moléculas
</pre>
</div>
</div>

<div id="outline-container-orgd2f982c" class="outline-5">
<h5 id="orgd2f982c"><span class="section-number-5">2.5.6.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-2-5-6-4">
<p>
Qual o volume de 3 mols de gás nas CNTP?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orga2b48b3">
V = n × 22,4 = 3 × 22,4 = 67,2 L
</pre>
</div>
</div>

<div id="outline-container-org105992a" class="outline-5">
<h5 id="org105992a"><span class="section-number-5">2.5.6.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-2-5-6-5">
<p>
Na reação 2 H₂ + O₂ → 2 H₂O, se 10 g de H₂O são obtidos a partir de 100 g de reagentes, verifique Lavoisier.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org2aa92ae">
Lavoisier: m_reagentes = m_produtos
Mas só formou 10g? Não! Falta informação.
Se 10g de H₂O formados, então:
m(reagentes restantes) = 100
- 10 = 90g
Massa total conservada ✓
</pre>
</div>
</div>
</div>

<div id="outline-container-orgc06dca3" class="outline-4">
<h4 id="orgc06dca3"><span class="section-number-4">2.5.7.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-5-7">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<pre class="example" id="org8a76c70">
MOL:
1 mol = 6,02 × 10²³ entidades
N_A = 6,02 × 10²³ /mol

RELAÇÕES:
n = m/M
m = n × M
N = n × N_A
V = n × 22,4 L (CNTP)

LEIS PONDERAIS:
Lavoisier: m_reagentes = m_produtos
Proust: proporção constante
Dalton: proporções inteiras

MASSAS MOLARES COMUNS:
H₂ = 2 g/mol
O₂ = 32 g/mol
H₂O = 18 g/mol
CO₂ = 44 g/mol
NaCl = 58,5 g/mol
C = 12 g/mol
O = 16 g/mol
N = 14 g/mol

VOLUME MOLAR:
CNTP: V_m = 22,4 L/mol

PUREZA:
m_pura = m_total × pureza%

RENDIMENTO:
R = (m_obtida / m_teórica) × 100%
</pre>
</div>
</div>

<div id="outline-container-orgb3fbaf3" class="outline-4">
<h4 id="orgb3fbaf3"><span class="section-number-4">2.5.8.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-2-5-8">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei calcular número de mols (n = m/M)</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular massa a partir de mols</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular número de partículas</li>
<li class="off"><code>[&#xa0;]</code> Sei as três leis ponderais</li>
<li class="off"><code>[&#xa0;]</code> Sei balancear equações químicas</li>
<li class="off"><code>[&#xa0;]</code> Sei fazer cálculos massa → massa</li>
<li class="off"><code>[&#xa0;]</code> Sei fazer cálculos com volume (CNTP)</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular pureza</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular rendimento</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orge2d1eac" class="outline-3">`;

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
