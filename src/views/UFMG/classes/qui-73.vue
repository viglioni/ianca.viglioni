<script setup lang="ts">
import { ref } from "vue";

const code = "qui-73";
const title = "Química: Revisão Geral";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-4">
<ul class="org-ul">
<li>Química: Revisão Geral</li>
<li>Conceitos-Chave</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org56a853c" class="outline-4">
<h4 id="org56a853c"><span class="section-number-4">3.4.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-3-4-1">
<p>
Revisar rapidamente os principais conceitos de Química para a prova.
</p>
</div>
</div>

<div id="outline-container-orgf47404c" class="outline-4">
<h4 id="orgf47404c"><span class="section-number-4">3.4.2.</span> 1. Modelos Atômicos</h4>
<div class="outline-text-4" id="text-3-4-2">
<ul class="org-ul">
<li>Resumo Rápido</li>
</ul>
<pre class="example" id="org91ed3be">
Dalton (1808) → Bola de bilhar (maciça)
Thomson (1897) → Pudim de passas (descobriu elétron)
Rutherford (1911) → Planetário (descobriu núcleo)
Bohr (1913) → Níveis de energia (K, L, M, N...)
Atual → Orbitais (probabilidade)
</pre>
</div>
</div>

<div id="outline-container-org7b0fabb" class="outline-4">
<h4 id="org7b0fabb"><span class="section-number-4">3.4.3.</span> 2. Estrutura Atômica</h4>
<div class="outline-text-4" id="text-3-4-3">
<pre class="example" id="orgcbe19fe">
Próton (p⁺): carga +1, massa ~1 u
Nêutron (n⁰): carga 0, massa ~1 u
Elétron (e⁻): carga -1, massa ~1/1836 u

Notação: ᴬᴢX

Z = número atômico = prótons
A = número de massa = prótons + nêutrons
N = nêutrons = A
- Z

Isótopos: mesmo Z, A diferente
Isóbaros: mesmo A, Z diferente
Isótonos: mesmo N, Z e A diferentes
</pre>
</div>
</div>

<div id="outline-container-orga81e5e5" class="outline-4">
<h4 id="orga81e5e5"><span class="section-number-4">3.4.4.</span> 3. Tabela Periódica</h4>
<div class="outline-text-4" id="text-3-4-4">
<ul class="org-ul">
<li>Essencial</li>
</ul>
<p>
<b>Organização:</b>
</p>
<ul class="org-ul">
<li>7 períodos (linhas) = número de camadas</li>
<li>18 grupos (colunas) = propriedades semelhantes</li>
</ul>

<p>
<b>Famílias principais:</b>
</p>

<pre class="example" id="orgb890698">
Grupo 1: Metais Alcalinos (Li, Na, K...)
Grupo 2: Metais Alcalino-Terrosos (Be, Mg, Ca...)
Grupo 16: Calcogênios (O, S, Se...)
Grupo 17: Halogênios (F, Cl, Br, I...)
Grupo 18: Gases Nobres (He, Ne, Ar...)
</pre>

<p>
<b>Propriedades periódicas:</b>
</p>

<pre class="example" id="orgbcda8dc">
Raio atômico: ↑ na família, ← no período
Energia de ionização: ↓ na família, → no período
Eletronegatividade: ↓ na família, → no período

Mais eletronegativo: F (flúor)
Ordem: F &gt; O &gt; N &gt; Cl
</pre>
</div>
</div>

<div id="outline-container-org51667d8" class="outline-4">
<h4 id="org51667d8"><span class="section-number-4">3.4.5.</span> 4. Ligações Químicas</h4>
<div class="outline-text-4" id="text-3-4-5">
<p>
<b>Iônica:</b>
</p>
<ul class="org-ul">
<li>Metal + não-metal</li>
<li>Transferência de elétrons</li>
<li>Cátion + ânion</li>
<li>Exemplo: NaCl (Na⁺ + Cl⁻)</li>
</ul>

<p>
<b>Covalente:</b>
</p>
<ul class="org-ul">
<li>Não-metal + não-metal</li>
<li>Compartilhamento de elétrons</li>
<li>Exemplos: H₂, O₂, H₂O, CO₂</li>
</ul>

<p>
<b>Metálica:</b>
</p>
<ul class="org-ul">
<li>Metal + metal</li>
<li>“Mar de elétrons”</li>
<li>Exemplo: Fe, Cu, Al</li>
</ul>
</div>
</div>

<div id="outline-container-org4bbbff8" class="outline-4">
<h4 id="org4bbbff8"><span class="section-number-4">3.4.6.</span> 5. Estequiometria</h4>
<div class="outline-text-4" id="text-3-4-6">
<ul class="org-ul">
<li>Fórmulas-Chave</li>
</ul>
<pre class="example" id="org63e0d8e">
1 mol = 6,02 × 10²³ entidades (Nᴀ)

n = m/M  (mol)
m = n × M  (massa)
N = n × Nᴀ  (partículas)
V = n × 22,4 L  (CNTP)

Leis:
Lavoisier: m_reagentes = m_produtos
Proust: proporção constante
</pre>
</div>
</div>

<div id="outline-container-orgb72554a" class="outline-4">
<h4 id="orgb72554a"><span class="section-number-4">3.4.7.</span> 6. Funções Inorgânicas</h4>
<div class="outline-text-4" id="text-3-4-7">
<p>
<b>Ácidos:</b> liberam H⁺ em água
</p>
<ul class="org-ul">
<li>Exemplos: HCl, H₂SO₄, HNO₃</li>
</ul>

<p>
<b>Bases:</b> liberam OH⁻ em água
</p>
<ul class="org-ul">
<li>Exemplos: NaOH, Ca(OH)₂</li>
</ul>

<p>
<b>Sais:</b> cátion + ânion
</p>
<ul class="org-ul">
<li>Exemplos: NaCl, K₂SO₄</li>
</ul>

<p>
<b>Óxidos:</b> elemento + oxigênio
</p>
<ul class="org-ul">
<li>Exemplos: CO₂, H₂O, Fe₂O₃</li>
</ul>
</div>
</div>

<div id="outline-container-orgfb61073" class="outline-4">
<h4 id="orgfb61073"><span class="section-number-4">3.4.8.</span> 7. Separação de Misturas</h4>
<div class="outline-text-4" id="text-3-4-8">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<pre class="example" id="org42b60dd">
Filtração: sólido + líquido
Destilação simples: líquido + sólido dissolvido
Destilação fracionada: líquidos miscíveis
Decantação: líquidos imiscíveis ou sólido + líquido
Centrifugação: acelera decantação
</pre>
</div>
</div>

<div id="outline-container-orgced284f" class="outline-4">
<h4 id="orgced284f"><span class="section-number-4">3.4.9.</span> 8. pH e pOH (Conceito Básico)</h4>
<div class="outline-text-4" id="text-3-4-9">
<pre class="example" id="org9ebbabf">
pH &lt; 7: ácido
pH = 7: neutro
pH &gt; 7: básico

pH + pOH = 14
</pre>
</div>
</div>

<div id="outline-container-org05b426e" class="outline-4">
<h4 id="org05b426e"><span class="section-number-4">3.4.10.</span> 9. Reações Químicas</h4>
<div class="outline-text-4" id="text-3-4-10">
<ul class="org-ul">
<li>Tipos</li>
</ul>
<p>
<b>Síntese:</b>
</p>

<pre class="example" id="orgfe73cc3">
A + B → AB
</pre>

<p>
<b>Decomposição:</b>
</p>

<pre class="example" id="org1543d67">
AB → A + B
</pre>

<p>
<b>Simples troca:</b>
</p>

<pre class="example" id="org3b31582">
AB + C → AC + B
</pre>

<p>
<b>Dupla troca:</b>
</p>

<pre class="example" id="org6b13064">
AB + CD → AD + CB
</pre>
</div>
</div>

<div id="outline-container-orge994e80" class="outline-4">
<h4 id="orge994e80"><span class="section-number-4">3.4.11.</span> 10. Dados Importantes</h4>
<div class="outline-text-4" id="text-3-4-11">
<ul class="org-ul">
<li>Memorizar</li>
</ul>
<p>
<b>Massas molares comuns:</b>
</p>

<pre class="example" id="org74daec2">
H = 1 g/mol
C = 12 g/mol
N = 14 g/mol
O = 16 g/mol
Na = 23 g/mol
Cl = 35,5 g/mol
Ca = 40 g/mol

H₂O = 18 g/mol
CO₂ = 44 g/mol
NaCl = 58,5 g/mol
</pre>

<p>
<b>Constantes:</b>
</p>

<pre class="example" id="org8f13e00">
Nᴀ = 6,02 × 10²³ /mol
V_molar (CNTP) = 22,4 L/mol
</pre>
</div>
</div>

<div id="outline-container-orgcc01f79" class="outline-4">
<h4 id="orgcc01f79"><span class="section-number-4">3.4.12.</span> Questões Rápidas</h4>
<div class="outline-text-4" id="text-3-4-12">
</div>
<div id="outline-container-orgafdeffc" class="outline-5">
<h5 id="orgafdeffc"><span class="section-number-5">3.4.12.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-3-4-12-1">
<p>
Quantos nêutrons tem ³⁵₁₇Cl?
</p>

<p>
<i>[Ver resposta 11 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org9c82ab4" class="outline-5">
<h5 id="org9c82ab4"><span class="section-number-5">3.4.12.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-3-4-12-2">
<p>
Qual elemento é mais eletronegativo: N ou O?
</p>

<p>
<i>[Ver resposta 12 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org84061a9" class="outline-5">
<h5 id="org84061a9"><span class="section-number-5">3.4.12.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-3-4-12-3">
<p>
NaCl é ligação iônica ou covalente?
</p>

<p>
<i>[Ver resposta 13 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org9509867" class="outline-5">
<h5 id="org9509867"><span class="section-number-5">3.4.12.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-3-4-12-4">
<p>
Quantos mols há em 90 g de H₂O? (M = 18 g/mol)
</p>

<p>
<i>[Ver resposta 14 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgc573387" class="outline-5">
<h5 id="orgc573387"><span class="section-number-5">3.4.12.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-3-4-12-5">
<p>
pH = 3 é ácido, neutro ou básico?
</p>

<p>
<i>[Ver resposta 15 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgdc0c3b6" class="outline-4">
<h4 id="orgdc0c3b6"><span class="section-number-4">3.4.13.</span> Resumo Ultra-Rápido</h4>
<div class="outline-text-4" id="text-3-4-13">
<pre class="example" id="org991a8ba">
ESTRUTURA:
Z = prótons
A = prótons + nêutrons
N = A
- Z

TABELA:
Famílias importantes: Alcalinos, Halogênios, Gases Nobres
F = mais eletronegativo

LIGAÇÕES:
Iônica: metal + não-metal
Covalente: não-metal + não-metal
Metálica: metal + metal

ESTEQUIOMETRIA:
n = m/M
1 mol = 6,02×10²³
V_molar = 22,4 L

FUNÇÕES:
Ácido: H⁺
Base: OH⁻
Sal: cátion + ânion
Óxido: elemento + O

pH:
&lt; 7: ácido
= 7: neutro
&gt; 7: básico
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Fácil-Médio (revisão rápida) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgddd66f2" class="outline-3">`;

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
