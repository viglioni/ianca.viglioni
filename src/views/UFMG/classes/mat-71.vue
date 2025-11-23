<script setup lang="ts">
import { ref } from "vue";

const code = "mat-71";
const title = "Matemática: Revisão Final";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-2">
<ul class="org-ul">
<li>Matemática: Revisão Final</li>
<li>Geometria Plana e Trigonometria</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orge8e9dd1" class="outline-4">
<h4 id="orge8e9dd1"><span class="section-number-4">3.2.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-3-2-1">
<p>
Consolidar fórmulas de áreas, perímetros, Pitágoras e trigonometria básica.
</p>
</div>
</div>

<div id="outline-container-orge331a65" class="outline-4">
<h4 id="orge331a65"><span class="section-number-4">3.2.2.</span> PARTE 1: Geometria Plana</h4>
<div class="outline-text-4" id="text-3-2-2">
<ul class="org-ul">
<li>Áreas e Perímetros</li>
</ul>
<p>
<b>1. Triângulo</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org5e477f7">
A = (b × h) / 2

Onde:
b = base
h = altura
</pre>

<p>
<b>Perímetro:</b>
</p>

<pre class="example" id="org6c3c494">
P = a + b + c (soma dos lados)
</pre>

<p>
<b>Tipos de triângulo:</b>
</p>
<ul class="org-ul">
<li><b>Equilátero:</b> 3 lados iguais</li>
<li><b>Isósceles:</b> 2 lados iguais</li>
<li><b>Escaleno:</b> todos diferentes</li>
<li><b>Retângulo:</b> 1 ângulo de 90°</li>
</ul>

<p>
<b>2. Quadrado</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="orgae8bf6b">
A = L²

Onde L = lado
</pre>

<p>
<b>Perímetro:</b>
</p>

<pre class="example" id="orgb8af1ab">
P = 4L
</pre>

<p>
<b>Diagonal:</b>
</p>

<pre class="example" id="org5af4acb">
d = L√2
</pre>

<p>
<b>3. Retângulo</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="orge2a6b87">
A = b × h

Onde:
b = base
h = altura
</pre>

<p>
<b>Perímetro:</b>
</p>

<pre class="example" id="orgab65157">
P = 2(b + h)
</pre>

<p>
<b>Diagonal:</b>
</p>

<pre class="example" id="orgcb8abd6">
d = √(b² + h²)  (Pitágoras)
</pre>

<p>
<b>4. Paralelogramo</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org921201b">
A = b × h

Onde:
b = base
h = altura (perpendicular!)
</pre>

<p>
<b>5. Trapézio</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="orgc896c15">
A = [(B + b) × h] / 2

Onde:
B = base maior
b = base menor
h = altura
</pre>

<p>
<b>6. Losango</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org9de3860">
A = (D × d) / 2

Onde:
D = diagonal maior
d = diagonal menor
</pre>

<p>
<b>7. Círculo</b>
</p>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org81af3d5">
A = πr²

Onde r = raio
</pre>

<p>
<b>Perímetro (comprimento da circunferência):</b>
</p>

<pre class="example" id="orgf56510a">
C = 2πr
ou
C = πd  (onde d = diâmetro)
</pre>

<p>
<b>Comprimento de arco:</b>
</p>

<pre class="example" id="orgd0da15d">
ℓ = (α/360°) × 2πr

Onde α = ângulo em graus
</pre>

<p>
<b>Área de setor circular:</b>
</p>

<pre class="example" id="org3450ae7">
A_setor = (α/360°) × πr²
</pre>
</div>
</div>

<div id="outline-container-org6055fa6" class="outline-4">
<h4 id="org6055fa6"><span class="section-number-4">3.2.3.</span> PARTE 2: Teorema de Pitágoras</h4>
<div class="outline-text-4" id="text-3-2-3">
<p>
<b>Enunciado:</b> “Em um triângulo retângulo, o quadrado da hipotenusa é igual à soma dos quadrados dos catetos.”
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org00f152f">
a² = b² + c²

Onde:
a = hipotenusa (lado oposto ao ângulo reto)
b, c = catetos
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orge372173">
Catetos: 3 e 4
Hipotenusa: a² = 3² + 4² = 9 + 16 = 25
a = 5
</pre>

<p>
<b>Ternas pitagóricas importantes:</b>
</p>

<pre class="example" id="orgcfcfdc8">
(3, 4, 5)
(5, 12, 13)
(8, 15, 17)
(7, 24, 25)

E seus múltiplos:
(6, 8, 10) = 2×(3,4,5)
(9, 12, 15) = 3×(3,4,5)
</pre>
</div>
</div>

<div id="outline-container-org90c488d" class="outline-4">
<h4 id="org90c488d"><span class="section-number-4">3.2.4.</span> PARTE 3: Trigonometria no Triângulo Retângulo</h4>
<div class="outline-text-4" id="text-3-2-4">
<p>
<b>Definições:</b>
</p>

<p>
Em um triângulo retângulo com ângulo α:
</p>

<pre class="example" id="org2617a08">
       |\\
       | \\
   CO  |  \\ H
       |   \\
       |____\\
         CA

H = hipotenusa
CO = cateto oposto a α
CA = cateto adjacente a α
</pre>

<p>
<b>Razões trigonométricas:</b>
</p>

<pre class="example" id="org9d6225a">
sen α = CO / H  (cateto oposto / hipotenusa)
cos α = CA / H  (cateto adjacente / hipotenusa)
tg α = CO / CA  (cateto oposto / cateto adjacente)
</pre>

<p>
<b>Relação fundamental:</b>
</p>

<pre class="example" id="org9a51934">
sen² α + cos² α = 1
</pre>

<p>
<b>Outras relações:</b>
</p>

<pre class="example" id="orgac76392">
tg α = sen α / cos α
</pre>
</div>
</div>

<div id="outline-container-org7fd2e57" class="outline-4">
<h4 id="org7fd2e57"><span class="section-number-4">3.2.5.</span> Valores Notáveis (30°, 45°, 60°)</h4>
<div class="outline-text-4" id="text-3-2-5">
<p>
<b>Tabela obrigatória:</b>
</p>

<pre class="example" id="org5119e3b">
┌─────┬─────┬────────┬────────┐
│  α  │ sen │  cos   │   tg   │
├─────┼─────┼────────┼────────┤
│ 30° │ 1/2 │ √3/2   │ √3/3   │
│ 45° │√2/2 │ √2/2   │   1    │
│ 60° │√3/2 │  1/2   │  √3    │
└─────┴─────┴────────┴────────┘
</pre>

<p>
<b>Dica para memorizar seno:</b>
</p>

<pre class="example" id="orgf8ea853">
sen 30° = 1/2  = √1/2
sen 45° = √2/2 = √2/2
sen 60° = √3/2 = √3/2

Numerador: 1, 2, 3 (√)
Denominador: sempre 2
</pre>

<p>
<b>Cosseno:</b> inverso do seno
</p>

<pre class="example" id="org4898489">
cos 30° = √3/2 = sen 60°
cos 45° = √2/2 = sen 45°
cos 60° = 1/2 = sen 30°
</pre>
</div>
</div>

<div id="outline-container-orgb425cfc" class="outline-4">
<h4 id="orgb425cfc"><span class="section-number-4">3.2.6.</span> Exemplos de Aplicação</h4>
<div class="outline-text-4" id="text-3-2-6">
<p>
<b>Exemplo 1:</b> Calcular a altura de um triângulo retângulo com hipotenusa 10 m e ângulo de 30°.
</p>

<pre class="example" id="org5e64c1e">
sen 30° = h / 10
1/2 = h / 10
h = 10 / 2 = 5 m
</pre>

<p>
<b>Exemplo 2:</b> Uma rampa tem 13 m de comprimento e 5 m de altura. Qual sua base?
</p>

<pre class="example" id="org119d652">
Pitágoras:
13² = 5² + b²
169 = 25 + b²
b² = 144
b = 12 m
</pre>

<p>
<b>Exemplo 3:</b> Calcular x no triângulo retângulo com catetos 6 e 8.
</p>

<pre class="example" id="orgaccc01c">
x² = 6² + 8²
x² = 36 + 64 = 100
x = 10
</pre>
</div>
</div>

<div id="outline-container-org43dcaaf" class="outline-4">
<h4 id="org43dcaaf"><span class="section-number-4">3.2.7.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-3-2-7">
</div>
<div id="outline-container-org6ef517d" class="outline-5">
<h5 id="org6ef517d"><span class="section-number-5">3.2.7.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-3-2-7-1">
<p>
Qual a área de um triângulo de base 8 m e altura 5 m?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org6a33d4d">
A = (8 × 5) / 2 = 40 / 2 = 20 m²
</pre>
</div>
</div>

<div id="outline-container-org4709505" class="outline-5">
<h5 id="org4709505"><span class="section-number-5">3.2.7.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-3-2-7-2">
<p>
Qual a área de um círculo de raio 3 m? (use π ≈ 3)
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org2cce707">
A = πr² = 3 × 3² = 3 × 9 = 27 m²
</pre>
</div>
</div>

<div id="outline-container-org061877a" class="outline-5">
<h5 id="org061877a"><span class="section-number-5">3.2.7.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-3-2-7-3">
<p>
Calcule a hipotenusa de um triângulo com catetos 5 e 12.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org6f3f439">
a² = 5² + 12² = 25 + 144 = 169
a = 13
</pre>
</div>
</div>

<div id="outline-container-org1c24b18" class="outline-5">
<h5 id="org1c24b18"><span class="section-number-5">3.2.7.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-3-2-7-4">
<p>
Calcule sen 30° + cos 60°.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org6f9ab55">
sen 30° = 1/2
cos 60° = 1/2
Soma = 1/2 + 1/2 = 1
</pre>
</div>
</div>

<div id="outline-container-org0a5f550" class="outline-5">
<h5 id="org0a5f550"><span class="section-number-5">3.2.7.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-3-2-7-5">
<p>
Em um triângulo retângulo, a hipotenusa é 20 m e um ângulo é 60°. Qual o cateto oposto?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgd72083f">
sen 60° = CO / 20
√3/2 = CO / 20
CO = 20√3/2 = 10√3 m
</pre>
</div>
</div>
</div>

<div id="outline-container-orgfdaa3c1" class="outline-4">
<h4 id="orgfdaa3c1"><span class="section-number-4">3.2.8.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-2-8">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<pre class="example" id="orgac6a2f1">
ÁREAS:
Triângulo: A = (b×h)/2
Quadrado: A = L²
Retângulo: A = b×h
Paralelogramo: A = b×h
Trapézio: A = [(B+b)×h]/2
Losango: A = (D×d)/2
Círculo: A = πr²

PERÍMETROS:
Quadrado: P = 4L
Retângulo: P = 2(b+h)
Círculo: C = 2πr = πd

PITÁGORAS:
a² = b² + c²
(a = hipotenusa, b e c = catetos)

TRIGONOMETRIA:
sen α = CO / H
cos α = CA / H
tg α = CO / CA

Relação fundamental:
sen² α + cos² α = 1
tg α = sen α / cos α

VALORES NOTÁVEIS:
       30°    45°    60°
sen:   1/2    √2/2   √3/2
cos:   √3/2   √2/2   1/2
tg:    √3/3   1      √3

TERNAS PITAGÓRICAS:
(3, 4, 5)
(5, 12, 13)
(8, 15, 17)
</pre>
</div>
</div>

<div id="outline-container-org1dfb4cd" class="outline-4">
<h4 id="org1dfb4cd"><span class="section-number-4">3.2.9.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-3-2-9">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei as fórmulas de áreas de todas as figuras</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular perímetros</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar Pitágoras</li>
<li class="off"><code>[&#xa0;]</code> Sei as ternas pitagóricas mais comuns</li>
<li class="off"><code>[&#xa0;]</code> Sei as definições de seno, cosseno e tangente</li>
<li class="off"><code>[&#xa0;]</code> Memorizei a tabela de valores notáveis (30°, 45°, 60°)</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar trigonometria em problemas práticos</li>
<li class="off"><code>[&#xa0;]</code> Sei a relação fundamental: sen² + cos² = 1</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgc2f033d" class="outline-3">`;

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
