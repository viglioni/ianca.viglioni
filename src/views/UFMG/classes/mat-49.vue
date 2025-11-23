<script setup lang="ts">
import { ref } from "vue";

const code = "mat-49";
const title = "Matemática: Geometria Plana";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-1">
<ul class="org-ul">
<li>Matemática: Geometria Plana</li>
<li>Triângulos, Círculos e Teorema de Pitágoras</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-org887bd1c" class="outline-4">
<h4 id="org887bd1c"><span class="section-number-4">3.1.1.</span> Triângulos</h4>
<div class="outline-text-4" id="text-3-1-1">
<ul class="org-ul">
<li>Definição e Classificação</li>
</ul>
<pre class="example" id="orgf6bc73b">
TIPOS DE TRIÂNGULOS

QUANTO AOS LADOS:

Equilátero              Isósceles              Escaleno
(3 lados iguais)        (2 lados iguais)       (lados diferentes)

     /\\                      /\\                     /\\
    /  \\                    /  \\                   /  \\
   /____\\                  /____\\                 /____\\
  ℓ  ℓ   ℓ                ℓ  b   ℓ              a   b   c

• 3 ângulos 60°         • 2 ângulos iguais     • 3 ângulos diferentes


QUANTO AOS ÂNGULOS:

Acutângulo              Retângulo              Obtusângulo
(3 ângulos agudos)      (1 ângulo reto)        (1 ângulo obtuso)

     /\\                      |\\                     /\\
    /  \\                     | \\                   /  \\___
   /____\\                    |__\\                 /      \\
  &lt;90° &lt;90° &lt;90°            90°                   &gt;90°

• Todos &lt; 90°           • Um = 90°             • Um &gt; 90°
</pre>

<p>
<b>Triângulo:</b> polígono de 3 lados e 3 ângulos
</p>

<p>
<b>Propriedade fundamental:</b>
</p>

<pre class="example" id="orgc891f97">
Soma dos ângulos internos = 180°
α + β + γ = 180°
</pre>

<p>
<b>Classificação quanto aos lados:</b>
</p>

<p>
<b>1. Equilátero</b>
</p>
<ul class="org-ul">
<li>3 lados <b>iguais</b></li>
<li>3 ângulos iguais (60° cada)</li>
</ul>

<p>
<b>2. Isósceles</b>
</p>
<ul class="org-ul">
<li>2 lados <b>iguais</b></li>
<li>2 ângulos iguais (base)</li>
</ul>

<p>
<b>3. Escaleno</b>
</p>
<ul class="org-ul">
<li>3 lados <b>diferentes</b></li>
<li>3 ângulos diferentes</li>
</ul>

<p>
<b>Classificação quanto aos ângulos:</b>
</p>

<p>
<b>1. Acutângulo</b>
</p>
<ul class="org-ul">
<li>3 ângulos <b>agudos</b> (&lt; 90°)</li>
</ul>

<p>
<b>2. Retângulo</b>
</p>
<ul class="org-ul">
<li>1 ângulo <b>reto</b> (= 90°)</li>
</ul>

<p>
<b>3. Obtusângulo</b>
</p>
<ul class="org-ul">
<li>1 ângulo <b>obtuso</b> (&gt; 90°)</li>
</ul>
</div>
</div>

<div id="outline-container-orgf4d9e35" class="outline-4">
<h4 id="orgf4d9e35"><span class="section-number-4">3.1.2.</span> Elementos do Triângulo</h4>
<div class="outline-text-4" id="text-3-1-2">
<p>
<b>Altura (h):</b>
</p>
<ul class="org-ul">
<li>Segmento perpendicular do vértice à base</li>
<li>Todo triângulo tem <b>3 alturas</b></li>
</ul>

<p>
<b>Mediana:</b>
</p>
<ul class="org-ul">
<li>Segmento do vértice ao ponto médio do lado oposto</li>
</ul>

<p>
<b>Bissetriz:</b>
</p>
<ul class="org-ul">
<li>Divide o ângulo ao meio</li>
</ul>

<p>
<b>Base (b):</b>
</p>
<ul class="org-ul">
<li>Lado de referência (geralmente o horizontal)</li>
</ul>
</div>
</div>

<div id="outline-container-orgc81d877" class="outline-4">
<h4 id="orgc81d877"><span class="section-number-4">3.1.3.</span> Área do Triângulo</h4>
<div class="outline-text-4" id="text-3-1-3">
<p>
<b>Fórmula geral:</b>
</p>

<pre class="example" id="org339bb9f">
A = (base × altura) / 2
A = (b × h) / 2
</pre>

<p>
<b>“Base vezes altura dividido por dois”</b>
</p>

<p>
<b>Exemplo:</b> Triângulo com b = 10 cm e h = 6 cm A = (10 × 6) / 2 = 30 cm²
</p>
</div>
</div>

<div id="outline-container-org60a0fd7" class="outline-4">
<h4 id="org60a0fd7"><span class="section-number-4">3.1.4.</span> Triângulo Retângulo</h4>
<div class="outline-text-4" id="text-3-1-4">
<pre class="example" id="orgc2aaac0">
TEOREMA DE PITÁGORAS

Triângulo Retângulo:

          c (hipotenusa)
        ╱│
      ╱  │
    ╱    │ b (cateto)
  ╱      │
╱________│
     a
(cateto)

FÓRMULA: a² + b² = c²

Onde:
• c = hipotenusa (lado maior, oposto ao ângulo reto)
• a, b = catetos (lados menores)


TERNAS PITAGÓRICAS CLÁSSICAS:

(3, 4, 5):      3² + 4² = 5²  →  9 + 16 = 25 ✓
(5, 12, 13):    5² + 12² = 13²  →  25 + 144 = 169 ✓
(8, 15, 17):    8² + 15² = 17²  →  64 + 225 = 289 ✓
(7, 24, 25):    7² + 24² = 25²  →  49 + 576 = 625 ✓

Múltiplos também funcionam:
(6, 8, 10) = 2×(3, 4, 5)
(9, 12, 15) = 3×(3, 4, 5)
</pre>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Hipotenusa (a):</b> lado oposto ao ângulo reto (maior lado)</li>
<li><b>Catetos (b e c):</b> lados que formam o ângulo reto</li>
</ul>

<pre class="example" id="org6109ddb">
   |\\
   | \\
c  |  \\ a (hipotenusa)
   |   \\
   |____\\
      b
</pre>

<p>
<b>Teorema de Pitágoras:</b>
</p>

<pre class="example" id="orgfe38f36">
a² = b² + c²
</pre>

<p>
<b>“O quadrado da hipotenusa é igual à soma dos quadrados dos catetos”</b>
</p>

<p>
<b>Exemplo:</b> Catetos: b = 3, c = 4 a² = 3² + 4² = 9 + 16 = 25 a = 5
</p>

<p>
<b>Ternas pitagóricas famosas:</b>
</p>
<ul class="org-ul">
<li>3, 4, 5</li>
<li>5, 12, 13</li>
<li>8, 15, 17</li>
<li>6, 8, 10 (múltiplo de 3, 4, 5)</li>
</ul>
</div>
</div>

<div id="outline-container-orgc92a248" class="outline-4">
<h4 id="orgc92a248"><span class="section-number-4">3.1.5.</span> Triângulo Equilátero</h4>
<div class="outline-text-4" id="text-3-1-5">
<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>Todos os lados iguais (l)</li>
<li>Todos os ângulos = 60°</li>
</ul>

<p>
<b>Altura:</b>
</p>

<pre class="example" id="org1d0c8c7">
h = (l√3) / 2
</pre>

<p>
<b>Área:</b>
</p>

<pre class="example" id="org6b54c99">
A = (l²√3) / 4
</pre>

<p>
<b>Exemplo:</b> Triângulo equilátero com l = 6 cm h = (6√3) / 2 = 3√3 cm A = (36√3) / 4 = 9√3 cm²
</p>
</div>
</div>

<div id="outline-container-org417c21b" class="outline-4">
<h4 id="org417c21b"><span class="section-number-4">3.1.6.</span> Círculo e Circunferência</h4>
<div class="outline-text-4" id="text-3-1-6">
<pre class="example" id="org3b71cdc">
    CÍRCULO E CIRCUNFERÊNCIA
- ELEMENTOS
    
                  Diâmetro (d = 2r)
                 ←─────────→
              ╭─────────────╮
            ╱        │        ╲
          ╱          │          ╲  ← Circunferência
         │           ●───────────│    (linha)
         │         Centro        │
         │     (raio r) →        │
          ╲                     ╱
            ╲                 ╱
              ╰─────────────╯
         └──────────────────────┘
              Círculo (área)
    
    Elementos:
    • Centro: ponto fixo
    • Raio (r): distância do centro até a borda
    • Diâmetro (d): d = 2r
    • Circunferência (C): perímetro = 2πr = πd
    • Área (A): A = πr²
    
    Relações:
    • d = 2r
    • C = 2πr = πd
    • A = πr² = π(d/2)²
</pre>

<p>
<b>Circunferência:</b> linha curva fechada (borda) <b>Círculo:</b> região interna (área)
</p>

<p>
<b>Elementos:</b>
</p>

<p>
<b>Centro (O):</b> ponto central
</p>

<p>
<b>Raio (r):</b> distância do centro a qualquer ponto da circunferência
</p>

<p>
<b>Diâmetro (d):</b> maior distância entre dois pontos
</p>

<pre class="example" id="orge1a13b4">
d = 2r
</pre>

<p>
<b>Corda:</b> segmento que une dois pontos da circunferência
</p>

<p>
<b>Arco:</b> parte da circunferência
</p>

<p>
<b>Setor circular:</b> “fatia” do círculo
</p>
</div>
</div>

<div id="outline-container-org313cf4b" class="outline-4">
<h4 id="org313cf4b"><span class="section-number-4">3.1.7.</span> Comprimento da Circunferência</h4>
<div class="outline-text-4" id="text-3-1-7">
<pre class="example" id="orgc3dcb19">
C = 2πr
ou
C = πd
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>π (pi) ≈ 3,14 ou 3,1416</li>
<li>r = raio</li>
<li>d = diâmetro</li>
</ul>

<p>
<b>Exemplo:</b> Circunferência com r = 5 cm C = 2 × 3,14 × 5 = 31,4 cm
</p>
</div>
</div>

<div id="outline-container-org8925a0c" class="outline-4">
<h4 id="org8925a0c"><span class="section-number-4">3.1.8.</span> Área do Círculo</h4>
<div class="outline-text-4" id="text-3-1-8">
<pre class="example" id="orgee97559">
A = πr²
</pre>

<p>
<b>Exemplo:</b> Círculo com r = 4 cm A = 3,14 × 4² = 3,14 × 16 = 50,24 cm²
</p>
</div>
</div>

<div id="outline-container-org8f9ac87" class="outline-4">
<h4 id="org8f9ac87"><span class="section-number-4">3.1.9.</span> Setor Circular</h4>
<div class="outline-text-4" id="text-3-1-9">
<p>
<b>Setor:</b> “fatia” do círculo
</p>

<p>
<b>Área do setor:</b>
</p>

<pre class="example" id="org7638963">
A_setor = (θ/360°) × πr²
</pre>

<p>
<b>Onde θ é o ângulo central em graus</b>
</p>

<p>
<b>Exemplo:</b> Setor de 90° (1/4 do círculo) com r = 6 A_setor = (90/360) × π × 36 = (1/4) × 36π = 9π cm²
</p>
</div>
</div>

<div id="outline-container-orgf5f54d5" class="outline-4">
<h4 id="orgf5f54d5"><span class="section-number-4">3.1.10.</span> Perímetro e Área</h4>
<div class="outline-text-4" id="text-3-1-10">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<p>
<b>Triângulos:</b>
</p>

<pre class="example" id="orgee9c8c3">
┌──────────────┬────────────────┬─────────────┐
│   Tipo       │     Área       │  Perímetro  │
├──────────────┼────────────────┼─────────────┤
│ Qualquer     │   (b×h)/2      │  a + b + c  │
│ Equilátero   │  (l²√3)/4      │     3l      │
│ Retângulo    │   (b×c)/2      │  a + b + c  │
└──────────────┴────────────────┴─────────────┘
</pre>

<p>
<b>Círculo:</b>
</p>

<pre class="example" id="org91c2015">
Área: A = πr²
Comprimento: C = 2πr = πd
</pre>
</div>
</div>

<div id="outline-container-org0f74d20" class="outline-4">
<h4 id="org0f74d20"><span class="section-number-4">3.1.11.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-1-11">
</div>
<div id="outline-container-org7481d8a" class="outline-5">
<h5 id="org7481d8a"><span class="section-number-5">3.1.11.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-1-11-1">
<p>
Um triângulo tem ângulos de 50° e 60°. Qual o terceiro ângulo?
</p>

<p>
<b>Solução:</b> α + β + γ = 180° 50° + 60° + γ = 180° γ = 70°
</p>

<p>
<i>[Ver resposta 16 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgca2f2e3" class="outline-5">
<h5 id="orgca2f2e3"><span class="section-number-5">3.1.11.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-1-11-2">
<p>
Triângulo retângulo com catetos 6 cm e 8 cm. Calcule a hipotenusa.
</p>

<p>
<b>Solução:</b> a² = b² + c² a² = 6² + 8² a² = 36 + 64 = 100 a = 10 cm
</p>

<p>
<i>[Ver resposta 17 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org489912a" class="outline-5">
<h5 id="org489912a"><span class="section-number-5">3.1.11.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-1-11-3">
<p>
(UFMG) Um círculo tem diâmetro 10 cm. Qual sua área? (Use π = 3,14)
</p>

<p>
<b>Solução:</b> d = 10 → r = 5 A = πr² = 3,14 × 5² = 3,14 × 25 = 78,5 cm²
</p>

<p>
<i>[Ver resposta 18 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgc2ea0ac" class="outline-5">
<h5 id="orgc2ea0ac"><span class="section-number-5">3.1.11.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-1-11-4">
<p>
Triângulo com base 12 cm e altura 5 cm. Calcule a área.
</p>

<p>
<b>Solução:</b> A = (b × h) / 2 = (12 × 5) / 2 = 30 cm²
</p>

<p>
<i>[Ver resposta 19 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org512b6f9" class="outline-5">
<h5 id="org512b6f9"><span class="section-number-5">3.1.11.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-3-1-11-5">
<p>
Uma roda tem raio 0,5 m. Quantos metros ela percorre em uma volta completa?
</p>

<p>
<b>Solução:</b> C = 2πr = 2 × 3,14 × 0,5 = 3,14 m
</p>

<p>
<i>[Ver resposta 20 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgc7a79c6" class="outline-5">
<h5 id="orgc7a79c6"><span class="section-number-5">3.1.11.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-3-1-11-6">
<p>
Triângulo equilátero com lado 4 cm. Calcule a área.
</p>

<p>
<b>Solução:</b> A = (l²√3) / 4 = (16√3) / 4 = 4√3 cm² A ≈ 4 × 1,73 = 6,92 cm²
</p>

<p>
<i>[Ver resposta 21 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7115e27" class="outline-5">
<h5 id="org7115e27"><span class="section-number-5">3.1.11.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-3-1-11-7">
<p>
Uma escada de 5 m está apoiada a 3 m do chão. Qual a distância da base da escada até a parede?
</p>

<p>
<b>Solução:</b> Triângulo retângulo: hipotenusa = 5, um cateto = 3 5² = 3² + c² 25 = 9 + c² c² = 16 c = 4 m
</p>

<p>
<i>[Ver resposta 22 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org47dac11" class="outline-4">
<h4 id="org47dac11"><span class="section-number-4">3.1.12.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-3-1-12">
<p>
<b>1. Construção civil:</b>
</p>
<ul class="org-ul">
<li>Esquadro (triângulo 3-4-5) para garantir ângulos retos</li>
<li>Telhados (cálculo de vigas)</li>
</ul>

<p>
<b>2. Navegação:</b>
</p>
<ul class="org-ul">
<li>Triangulação para determinar posições</li>
</ul>

<p>
<b>3. Engenharia:</b>
</p>
<ul class="org-ul">
<li>Estruturas triangulares (estáveis)</li>
<li>Rodas (círculos)</li>
</ul>
</div>
</div>

<div id="outline-container-org21cde9a" class="outline-4">
<h4 id="org21cde9a"><span class="section-number-4">3.1.13.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-1-13">
<ol class="org-ol">
<li><b>Soma dos ângulos do triângulo:</b> sempre 180°</li>
<li><b>Área do triângulo:</b> (base × altura) / 2</li>
<li><b>Pitágoras:</b> a² = b² + c² (só triângulo retângulo!)</li>
<li><b>Ternas pitagóricas:</b> 3-4-5, 5-12-13, 8-15-17</li>
<li><b>Círculo:</b> área = πr², comprimento = 2πr</li>
<li><b>π ≈ 3,14</b> ou deixe em função de π</li>
<li><b>Equilátero:</b> altura = (l√3)/2, área = (l²√3)/4</li>
<li><b>Diâmetro = 2 × raio</b></li>
</ol>
</div>
</div>

<div id="outline-container-org35d840b" class="outline-4">
<h4 id="org35d840b"><span class="section-number-4">3.1.14.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-1-14">
<p>
<b>Triângulo:</b>
</p>
<ul class="org-ul">
<li>3 lados, soma ângulos = 180°</li>
<li>Área = (b×h)/2</li>
</ul>

<p>
<b>Triângulo Retângulo:</b>
</p>
<ul class="org-ul">
<li>Pitágoras: a² = b² + c²</li>
<li>Hipotenusa = maior lado</li>
</ul>

<p>
<b>Triângulo Equilátero:</b>
</p>
<ul class="org-ul">
<li>3 lados iguais, 3 ângulos de 60°</li>
<li>Área = (l²√3)/4</li>
</ul>

<p>
<b>Círculo:</b>
</p>
<ul class="org-ul">
<li>Área = πr²</li>
<li>Comprimento = 2πr</li>
<li>d = 2r</li>
</ul>
</div>
</div>

<div id="outline-container-orgd7b1f78" class="outline-4">
<h4 id="orgd7b1f78"><span class="section-number-4">3.1.15.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-1-15">
<pre class="example" id="org042999b">
TRIÂNGULOS:

Soma ângulos internos:
α + β + γ = 180°

Área (geral):
A = (b × h) / 2

Teorema de Pitágoras (retângulo):
a² = b² + c²

Triângulo Equilátero:
Altura: h = (l√3) / 2
Área: A = (l²√3) / 4

CÍRCULO:

Área:
A = πr²

Comprimento (perímetro):
C = 2πr = πd

Relação raio-diâmetro:
d = 2r

Setor circular:
A_setor = (θ/360°) × πr²

Valores de π:
π ≈ 3,14 ou 3,1416
</pre>
</div>
</div>

<div id="outline-container-org175b408" class="outline-4">
<h4 id="org175b408"><span class="section-number-4">3.1.16.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-3-1-16">
<pre class="example" id="orge2beedd">
TRIÂNGULOS:

Equilátero:    Isósceles:    Escaleno:
   /\\              /\\            /\\
  /  \\            /  \\          /  \\
 /____\\          /____\\        /____\\
 l    l          a    a       a  b  c
(todos iguais)  (2 iguais)   (todos diferentes)

TRIÂNGULO RETÂNGULO:
       |\\
       | \\
    c  |  \\ a (hipotenusa)
       |   \\
       |____\\
          b
   a² = b² + c²

CÍRCULO:
      ___
    /     \\
   |   r   |  A = πr²
    \\     /   C = 2πr
      ‾‾‾

ÁREA DO TRIÂNGULO:
    /|\\
   / | \\
  /  |h \\
 /   |   \\
/____|____\\
     b
A = (b×h)/2
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>sempre cai!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org0a75b98" class="outline-3">`;

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
