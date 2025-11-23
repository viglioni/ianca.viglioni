<script setup lang="ts">
import { ref } from "vue";

const code = "mat-44";
const title = "Matemática: Geometria Plana";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-1">
<ul class="org-ul">
<li>Matemática: Geometria Plana</li>
<li>Áreas de Figuras (Parte 1)</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-orgfd48a60" class="outline-4">
<h4 id="orgfd48a60"><span class="section-number-4">2.1.1.</span> Introdução à Geometria Plana</h4>
<div class="outline-text-4" id="text-2-1-1">
<p>
<b>Geometria Plana:</b> estuda figuras bidimensionais (2D)
</p>
<ul class="org-ul">
<li>polígonos, círculos, etc.</li>
</ul>

<p>
<b>Conceitos fundamentais:</b>
</p>
<ul class="org-ul">
<li><b>Ponto:</b> posição no espaço (sem dimensão)</li>
<li><b>Reta:</b> conjunto infinito de pontos alinhados</li>
<li><b>Plano:</b> superfície plana infinita</li>
<li><b>Ângulo:</b> abertura entre duas semirretas</li>
<li><b>Polígono:</b> figura fechada formada por segmentos de reta</li>
</ul>
</div>
</div>

<div id="outline-container-org6bdaef7" class="outline-4">
<h4 id="org6bdaef7"><span class="section-number-4">2.1.2.</span> Unidades de Área</h4>
<div class="outline-text-4" id="text-2-1-2">
<p>
<b>Unidade SI:</b> metro quadrado (m²)
</p>

<p>
<b>Conversões:</b>
</p>

<pre class="example" id="org084706d">
1 m² = 100 dm² = 10.000 cm² = 1.000.000 mm²
1 km² = 1.000.000 m²
1 hectare (ha) = 10.000 m²
</pre>
</div>
</div>

<div id="outline-container-orgf196060" class="outline-4">
<h4 id="orgf196060"><span class="section-number-4">2.1.3.</span> Retângulo</h4>
<div class="outline-text-4" id="text-2-1-3">
<p>
<b>Definição:</b> quadrilátero com 4 ângulos retos (90°)
</p>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Base (b):</b> comprimento</li>
<li><b>Altura (h):</b> largura</li>
</ul>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org2e96628">
A = b × h
</pre>

<p>
<b>Perímetro:</b>
</p>

<pre class="example" id="orgc6e7936">
P = 2(b + h)
</pre>

<p>
<b>Exemplo:</b> Retângulo com b = 8 cm e h = 5 cm
</p>
<ul class="org-ul">
<li>A = 8 × 5 = 40 cm²</li>
<li>P = 2(8 + 5) = 26 cm</li>
</ul>
</div>
</div>

<div id="outline-container-org603cd29" class="outline-4">
<h4 id="org603cd29"><span class="section-number-4">2.1.4.</span> Quadrado</h4>
<div class="outline-text-4" id="text-2-1-4">
<p>
<b>Definição:</b> retângulo com todos os lados iguais
</p>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Lado (l)</b></li>
</ul>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org4611710">
A = l²
</pre>

<p>
<b>Perímetro:</b>
</p>

<pre class="example" id="orgb833536">
P = 4l
</pre>

<p>
<b>Diagonal:</b>
</p>

<pre class="example" id="orgfe30f86">
d = l√2
</pre>

<p>
<b>Exemplo:</b> Quadrado com l = 6 cm
</p>
<ul class="org-ul">
<li>A = 6² = 36 cm²</li>
<li>P = 4 × 6 = 24 cm</li>
<li>d = 6√2 ≈ 8,49 cm</li>
</ul>
</div>
</div>

<div id="outline-container-org37cbd9a" class="outline-4">
<h4 id="org37cbd9a"><span class="section-number-4">2.1.5.</span> Paralelogramo</h4>
<div class="outline-text-4" id="text-2-1-5">
<p>
<b>Definição:</b> quadrilátero com lados opostos paralelos
</p>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Base (b)</b></li>
<li><b>Altura (h):</b> distância perpendicular entre as bases</li>
</ul>

<p>
<b>Área:</b>
</p>

<pre class="example" id="orgec7d148">
A = b × h
</pre>

<p>
<b>Importante:</b> A altura é perpendicular à base, não é o lado inclinado!
</p>

<p>
<b>Exemplo:</b> Paralelogramo com b = 10 cm e h = 4 cm
</p>
<ul class="org-ul">
<li>A = 10 × 4 = 40 cm²</li>
</ul>
</div>
</div>

<div id="outline-container-orgfea40ec" class="outline-4">
<h4 id="orgfea40ec"><span class="section-number-4">2.1.6.</span> Trapézio</h4>
<div class="outline-text-4" id="text-2-1-6">
<p>
<b>Definição:</b> quadrilátero com um par de lados paralelos (bases)
</p>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Base maior (B)</b></li>
<li><b>Base menor (b)</b></li>
<li><b>Altura (h):</b> distância perpendicular entre as bases</li>
</ul>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org6f04391">
A = ((B + b) × h) / 2
</pre>

<p>
<b>“Média das bases vezes a altura”</b>
</p>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li><b>Trapézio retângulo:</b> dois ângulos retos</li>
<li><b>Trapézio isósceles:</b> lados não paralelos iguais</li>
<li><b>Trapézio escaleno:</b> lados desiguais</li>
</ul>

<p>
<b>Exemplo:</b> Trapézio com B = 12 cm, b = 8 cm, h = 5 cm
</p>
<ul class="org-ul">
<li>A = ((12 + 8) × 5) / 2 = (20 × 5) / 2 = 50 cm²</li>
</ul>
</div>
</div>

<div id="outline-container-org56b4e29" class="outline-4">
<h4 id="org56b4e29"><span class="section-number-4">2.1.7.</span> Losango</h4>
<div class="outline-text-4" id="text-2-1-7">
<p>
<b>Definição:</b> quadrilátero com todos os lados iguais (diagonais perpendiculares)
</p>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Diagonal maior (D)</b></li>
<li><b>Diagonal menor (d)</b></li>
</ul>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org60f5be8">
A = (D × d) / 2
</pre>

<p>
<b>“Produto das diagonais dividido por 2”</b>
</p>

<p>
<b>Exemplo:</b> Losango com D = 10 cm e d = 6 cm
</p>
<ul class="org-ul">
<li>A = (10 × 6) / 2 = 30 cm²</li>
</ul>
</div>
</div>

<div id="outline-container-org876386a" class="outline-4">
<h4 id="org876386a"><span class="section-number-4">2.1.8.</span> Resumo das Fórmulas de Quadriláteros</h4>
<div class="outline-text-4" id="text-2-1-8">
<pre class="example" id="orgab43e8b">
┌──────────────┬──────────────────┬─────────────┐
│   Figura     │      Área        │  Perímetro  │
├──────────────┼──────────────────┼─────────────┤
│ Retângulo    │    A = b × h     │  P = 2(b+h) │
│ Quadrado     │    A = l²        │  P = 4l     │
│ Paralelogramo│    A = b × h     │  P = 2(b+l) │
│ Trapézio     │ A = (B+b)×h / 2  │  P = B+b+l₁+l₂│
│ Losango      │ A = (D×d) / 2    │  P = 4l     │
└──────────────┴──────────────────┴─────────────┘
</pre>
</div>
</div>

<div id="outline-container-org56ac8a2" class="outline-4">
<h4 id="org56ac8a2"><span class="section-number-4">2.1.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-1-9">
</div>
<div id="outline-container-org04029ca" class="outline-5">
<h5 id="org04029ca"><span class="section-number-5">2.1.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-1-9-1">
<p>
Um retângulo tem perímetro 30 cm e base 9 cm. Qual sua área?
</p>

<p>
<b>Solução:</b> P = 2(b + h) 30 = 2(9 + h) 30 = 18 + 2h 2h = 12 h = 6 cm
</p>

<p>
A = b × h = 9 × 6 = 54 cm²
</p>

<p>
<i>[Ver resposta 1 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org75855f0" class="outline-5">
<h5 id="org75855f0"><span class="section-number-5">2.1.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-1-9-2">
<p>
Um terreno quadrado tem área de 400 m². Qual o comprimento de sua cerca (perímetro)?
</p>

<p>
<b>Solução:</b> A = l² 400 = l² l = 20 m
</p>

<p>
P = 4l = 4 × 20 = 80 m
</p>

<p>
<i>[Ver resposta 2 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org8533d8f" class="outline-5">
<h5 id="org8533d8f"><span class="section-number-5">2.1.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-1-9-3">
<p>
Um trapézio tem bases 15 cm e 9 cm, e altura 8 cm. Calcule sua área.
</p>

<p>
<b>Solução:</b> A = ((B + b) × h) / 2 A = ((15 + 9) × 8) / 2 A = (24 × 8) / 2 A = 192 / 2 A = 96 cm²
</p>

<p>
<i>[Ver resposta 3 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1b53295" class="outline-5">
<h5 id="org1b53295"><span class="section-number-5">2.1.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-1-9-4">
<p>
(UFMG) Um losango tem diagonais de 12 cm e 16 cm. Qual sua área?
</p>

<p>
<b>Solução:</b> A = (D × d) / 2 A = (16 × 12) / 2 A = 192 / 2 A = 96 cm²
</p>

<p>
<i>[Ver resposta 4 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgefbf8d9" class="outline-5">
<h5 id="orgefbf8d9"><span class="section-number-5">2.1.9.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-1-9-5">
<p>
Um paralelogramo tem base 10 cm e área 60 cm². Qual sua altura?
</p>

<p>
<b>Solução:</b> A = b × h 60 = 10 × h h = 6 cm
</p>

<p>
<i>[Ver resposta 5 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org2bdbddd" class="outline-4">
<h4 id="org2bdbddd"><span class="section-number-4">2.1.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-1-10">
<ol class="org-ol">
<li><b>Retângulo:</b> base × altura</li>
<li><b>Quadrado:</b> lado²</li>
<li><b>Paralelogramo:</b> base × altura (altura perpendicular!)</li>
<li><b>Trapézio:</b> média das bases × altura</li>
<li><b>Losango:</b> (diagonal maior × diagonal menor) / 2</li>
<li><b>Sempre verificar unidades</b></li>
<li><b>Desenhar a figura ajuda</b></li>
<li><b>Altura ≠ lado inclinado</b> (no paralelogramo/trapézio)</li>
</ol>
</div>
</div>

<div id="outline-container-orgb49be73" class="outline-4">
<h4 id="orgb49be73"><span class="section-number-4">2.1.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-1-11">
<p>
<b>Quadriláteros:</b>
</p>
<ul class="org-ul">
<li><b>4 lados</b>, soma dos ângulos internos = 360°</li>
</ul>

<p>
<b>Áreas:</b>
</p>
<ul class="org-ul">
<li>Retângulo/Paralelogramo: base × altura</li>
<li>Quadrado: lado²</li>
<li>Trapézio: média das bases × altura</li>
<li>Losango: produto das diagonais / 2</li>
</ul>

<p>
<b>Altura:</b>
</p>
<ul class="org-ul">
<li>Sempre perpendicular à base</li>
<li>Não confundir com lado inclinado</li>
</ul>
</div>
</div>

<div id="outline-container-org8bdfb7a" class="outline-4">
<h4 id="org8bdfb7a"><span class="section-number-4">2.1.12.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-1-12">
<pre class="example" id="orgf446667">
Retângulo:
A = b × h
P = 2(b + h)

Quadrado:
A = l²
P = 4l
Diagonal: d = l√2

Paralelogramo:
A = b × h  (h perpendicular!)

Trapézio:
A = ((B + b) × h) / 2
onde B = base maior, b = base menor

Losango:
A = (D × d) / 2
onde D = diagonal maior, d = diagonal menor

Conversões:
1 m² = 10.000 cm²
1 km² = 1.000.000 m²
1 ha = 10.000 m²
</pre>
</div>
</div>

<div id="outline-container-org79b0371" class="outline-4">
<h4 id="org79b0371"><span class="section-number-4">2.1.13.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-2-1-13">
<pre class="example" id="org9903912">
QUADRILÁTEROS:

Retângulo:        Quadrado:
┌────────┐        ┌────┐
│   h    │        │ l  │
│        │        │    │
└────────┘        └────┘
    b                 l

Paralelogramo:    Trapézio:
  /‾‾‾‾‾‾\\             b
 /    h   \\        ┌─────┐
/          \\       │  h  │
────────────       └─────────┘
     b                 B

Losango:
     D
    /|\\
   / | \\
  /  |d \\
 /   |   \\
/    |    \\
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>geometria sempre cai!)</li>
</ul>

<hr />

<p>
<i>Continua na próxima aula com Triângulos e Círculos&#x2026;</i>
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org62d9a92" class="outline-3">`;

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
