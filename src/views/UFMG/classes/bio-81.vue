<script setup lang="ts">
import { ref } from "vue";

const code = "bio-81";
const title = "Biologia: Genética";
const subject = "biologia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-1">
<ul class="org-ul">
<li>Biologia: Genética</li>
<li>Conceitos Fundamentais</li>
<li>45min</li>
</ul>
</div>
<div id="outline-container-org0c53c6e" class="outline-4">
<h4 id="org0c53c6e"><span class="section-number-4">5.1.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-5-1-1">
<p>
Compreender os conceitos básicos de genética: genes, cromossomos, DNA, Leis de Mendel.
</p>
</div>
</div>

<div id="outline-container-org51ca6fd" class="outline-4">
<h4 id="org51ca6fd"><span class="section-number-4">5.1.2.</span> PARTE 1: Conceitos Fundamentais</h4>
<div class="outline-text-4" id="text-5-1-2">
<p>
<b>DNA (Ácido Desoxirribonucleico):</b>
</p>

<pre class="example" id="org53aced2">
Molécula que armazena informação genética
Estrutura: dupla hélice
Composição:
- Açúcar (desoxirribose)
- Fosfato
- Bases nitrogenadas: A, T, C, G

Pareamento:
A ↔ T (adenina com timina)
C ↔ G (citosina com guanina)
</pre>

<p>
<b>Gene:</b>
</p>

<pre class="example" id="org58757eb">
Segmento de DNA que codifica uma característica
Unidade básica da hereditariedade
Localizado nos cromossomos
</pre>

<p>
<b>Cromossomos:</b>
</p>

<pre class="example" id="orgec6d334">
Estruturas que contêm DNA
Humanos: 46 cromossomos (23 pares)
- 22 pares autossômicos
- 1 par sexual (XX ou XY)
</pre>

<p>
<b>Genótipo vs Fenótipo:</b>
</p>

<pre class="example" id="orgd6c228a">
Genótipo: conjunto de genes (informação genética)
  Ex: AA, Aa, aa

Fenótipo: característica observável
  Ex: olhos castanhos, altura, tipo sanguíneo
</pre>
</div>
</div>

<div id="outline-container-orgf3395cb" class="outline-4">
<h4 id="orgf3395cb"><span class="section-number-4">5.1.3.</span> PARTE 2: Conceitos de Genética Mendeliana</h4>
<div class="outline-text-4" id="text-5-1-3">
<p>
<b>Alelos:</b>
</p>

<pre class="example" id="org66bb560">
Formas alternativas de um gene
Ex: gene para cor de olho
  - Alelo para castanho
  - Alelo para azul
</pre>

<p>
<b>Dominância e Recessividade:</b>
</p>

<pre class="example" id="org925a3ee">
Dominante (letra maiúscula): manifesta-se mesmo em dose única
  Ex: A = dominante

Recessivo (letra minúscula): manifesta-se apenas em dose dupla
  Ex: a = recessivo

AA = homozigoto dominante (fenótipo dominante)
Aa = heterozigoto (fenótipo dominante)
aa = homozigoto recessivo (fenótipo recessivo)
</pre>

<p>
<b>Homozigoto vs Heterozigoto:</b>
</p>

<pre class="example" id="org14819f9">
Homozigoto: alelos iguais (AA ou aa)
Heterozigoto: alelos diferentes (Aa)
</pre>
</div>
</div>

<div id="outline-container-org3810606" class="outline-4">
<h4 id="org3810606"><span class="section-number-4">5.1.4.</span> PARTE 3: Primeira Lei de Mendel (Lei da Segregação)</h4>
<div class="outline-text-4" id="text-5-1-4">
<p>
<b>Enunciado:</b> “Cada característica é determinada por um par de fatores que se separam na formação dos gametas.”
</p>

<p>
<b>Conceito:</b>
</p>

<pre class="example" id="org4b93524">
- Cada indivíduo tem 2 alelos para cada gene (um do pai, um da mãe)
- Na formação dos gametas, os alelos se separam
- Cada gameta recebe apenas 1 alelo
</pre>

<p>
<b>Cruzamento monoibridismo:</b>
</p>

<pre class="example" id="org37eec63">
P: AA × aa (pais)
Gametas: A   a
F₁: Aa (todos heterozigoto
- 100%)

F₁ × F₁: Aa × Aa
Gametas: A, a   A, a

Quadrado de Punnett:
        A    a
    A  AA   Aa
    a  Aa   aa

F₂: 1 AA : 2 Aa : 1 aa (proporção genotípica 1:2:1)
    3 dominantes : 1 recessivo (proporção fenotípica 3:1)
</pre>
</div>
</div>

<div id="outline-container-orged6a110" class="outline-4">
<h4 id="orged6a110"><span class="section-number-4">5.1.5.</span> PARTE 4: Segunda Lei de Mendel (Segregação Independente)</h4>
<div class="outline-text-4" id="text-5-1-5">
<p>
<b>Enunciado:</b> “Os fatores para duas ou mais características segregam-se independentemente durante a formação dos gametas.”
</p>

<p>
<b>Diibridismo:</b>
</p>

<pre class="example" id="orgb1cdfe2">
Exemplo: cor da semente (A = amarela, a = verde)
         textura (B = lisa, b = rugosa)

P: AABB × aabb
Gametas: AB    ab
F₁: AaBb (100% amarelas e lisas)

F₁ × F₁: AaBb × AaBb
Gametas: AB, Ab, aB, ab (cada parental)

F₂: proporção fenotípica 9:3:3:1
  9 amarelas lisas (A_B_)
  3 amarelas rugosas (A_bb)
  3 verdes lisas (aaB_)
  1 verde rugosa (aabb)
</pre>
</div>
</div>

<div id="outline-container-org4ed1107" class="outline-4">
<h4 id="org4ed1107"><span class="section-number-4">5.1.6.</span> PARTE 5: Genética de Grupos Sanguíneos</h4>
<div class="outline-text-4" id="text-5-1-6">
<p>
<b>Sistema ABO:</b>
</p>

<pre class="example" id="orgad2577e">
Alelos: Iᴬ, Iᴮ, i

Iᴬ e Iᴮ = codominantes
i = recessivo

Genótipos e fenótipos:
IᴬIᴬ ou Iᴬi → Tipo A
IᴮIᴮ ou Iᴮi → Tipo B
IᴬIᴮ → Tipo AB (codominância!)
ii → Tipo O
</pre>

<p>
<b>Fator Rh:</b>
</p>

<pre class="example" id="org14236ab">
R = dominante (Rh+)
r = recessivo (Rh-)

RR ou Rr → Rh positivo
rr → Rh negativo
</pre>

<p>
<b>Doação de sangue:</b>
</p>

<pre class="example" id="org47b6eb0">
O- : doador universal
AB+: receptor universal

Tipo O: doa para todos, recebe só de O
Tipo AB: recebe de todos, doa só para AB
</pre>
</div>
</div>

<div id="outline-container-org09fc131" class="outline-4">
<h4 id="org09fc131"><span class="section-number-4">5.1.7.</span> PARTE 6: Herança Sexual</h4>
<div class="outline-text-4" id="text-5-1-7">
<p>
<b>Cromossomos sexuais:</b>
</p>

<pre class="example" id="orgfd4ebbf">
Mulher: XX (homogamética)
Homem: XY (heterogamético)

Determinação do sexo:
Mulher produz: X, X
Homem produz: X, Y

Probabilidade: 50% menino, 50% menina
</pre>

<p>
<b>Herança ligada ao sexo (cromossomo X):</b>
</p>

<pre class="example" id="org2bfe3f7">
Exemplo: daltonismo (d = recessivo no cromossomo X)

Mulher:
XᴰXᴰ: normal
XᴰXᵈ: normal (portadora)
XᵈXᵈ: daltônica

Homem:
XᴰY: normal
XᵈY: daltônico

Homens são mais afetados (só precisam de 1 alelo)
</pre>
</div>
</div>

<div id="outline-container-orgade6918" class="outline-4">
<h4 id="orgade6918"><span class="section-number-4">5.1.8.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-5-1-8">
</div>
<div id="outline-container-orgd4c2670" class="outline-5">
<h5 id="orgd4c2670"><span class="section-number-5">5.1.8.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-5-1-8-1">
<p>
Qual a diferença entre genótipo e fenótipo?
</p>

<p>
<i>[Ver resposta 35 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orga96e709" class="outline-5">
<h5 id="orga96e709"><span class="section-number-5">5.1.8.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-5-1-8-2">
<p>
No cruzamento Aa × Aa, quais as proporções esperadas em F₁?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org2913696">
Genotípica: 1 AA : 2 Aa : 1 aa (1:2:1)
Fenotípica: 3 dominantes : 1 recessivo (3:1)
</pre>
</div>
</div>

<div id="outline-container-org167e520" class="outline-5">
<h5 id="org167e520"><span class="section-number-5">5.1.8.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-5-1-8-3">
<p>
Qual o genótipo de uma pessoa com sangue tipo B que pode ter filhos tipo O?
</p>

<p>
<i>[Ver resposta 36 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgecdf49f" class="outline-5">
<h5 id="orgecdf49f"><span class="section-number-5">5.1.8.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-5-1-8-4">
<p>
Por que doenças ligadas ao X são mais comuns em homens?
</p>

<p>
<i>[Ver resposta 37 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org424a508" class="outline-5">
<h5 id="org424a508"><span class="section-number-5">5.1.8.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-5-1-8-5">
<p>
Quais são as bases nitrogenadas do DNA e como se pareiam?
</p>

<p>
<i>[Ver resposta 38 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgb382dce" class="outline-4">
<h4 id="orgb382dce"><span class="section-number-4">5.1.9.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-1-9">
<pre class="example" id="org706e493">
DNA → Genes → Cromossomos

PRIMEIRA LEI DE MENDEL:
Aa × Aa → 3:1

SEGUNDA LEI DE MENDEL:
AaBb × AaBb → 9:3:3:1

GRUPOS SANGUÍNEOS:
A: IᴬIᴬ ou Iᴬi
B: IᴮIᴮ ou Iᴮi
AB: IᴬIᴮ (codominância)
O: ii

SEXO:
XX = mulher
XY = homem
</pre>
</div>
</div>

<div id="outline-container-org8e004e0" class="outline-4">
<h4 id="org8e004e0"><span class="section-number-4">5.1.10.</span> Conceitos-Chave</h4>
<div class="outline-text-4" id="text-5-1-10">
<pre class="example" id="orgb8b9167">
- DNA, gene, cromossomo
- Genótipo vs fenótipo
- Dominante vs recessivo
- Homozigoto vs heterozigoto
- Leis de Mendel (3:1 e 9:3:3:1)
- Sistema ABO e Rh
- Herança ligada ao sexo
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 45 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgc7defeb" class="outline-3">`;

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
