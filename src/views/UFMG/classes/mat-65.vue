<script setup lang="ts">
import { ref } from "vue";

const code = "mat-65";
const title = "Matemática: Revisão Final";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-2">
<ul class="org-ul">
<li>Matemática: Revisão Final</li>
<li>Função Afim e Quadrática</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org6af0213" class="outline-4">
<h4 id="org6af0213"><span class="section-number-4">2.2.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-2-2-1">
<p>
Consolidar completamente as funções de 1º e 2º grau, com foco em gráficos, raízes e aplicações.
</p>
</div>
</div>

<div id="outline-container-orgd25611f" class="outline-4">
<h4 id="orgd25611f"><span class="section-number-4">2.2.2.</span> PARTE 1: Função Afim (1º Grau)</h4>
<div class="outline-text-4" id="text-2-2-2">
<p>
<b>Definição:</b>
</p>

<pre class="example" id="org0db9ac6">
f(x) = ax + b, onde a ≠ 0
</pre>

<p>
<b>Parâmetros:</b>
</p>
<ul class="org-ul">
<li><b>a</b> = coeficiente angular (inclinação)</li>
<li><b>b</b> = coeficiente linear (onde corta o eixo y)</li>
</ul>

<p>
<b>Gráfico:</b> sempre uma RETA
</p>

<p>
<b>Análise do coeficiente a:</b>
</p>

<pre class="example" id="org6eb5d16">
a &gt; 0: função CRESCENTE (↗)
a &lt; 0: função DECRESCENTE (↘)
</pre>

<p>
<b>Raiz (zero da função):</b>
</p>

<pre class="example" id="orgfce501b">
f(x) = 0
ax + b = 0
x = −b/a
</pre>

<p>
<b>Coeficiente angular (taxa de variação):</b>
</p>

<pre class="example" id="org5934fa8">
a = Δy/Δx = (y₂ − y₁)/(x₂ − x₁)
</pre>

<p>
<b>Encontrar a lei f(x) = ax + b:</b>
</p>
<ul class="org-ul">
<li>Usar dois pontos</li>
<li>Montar sistema de equações</li>
<li>Resolver para a e b</li>
</ul>

<p>
<b>Exemplo completo:</b>
</p>

<p>
Determine f(x) sabendo que f(1) = 3 e f(4) = 12.
</p>

<pre class="example" id="org107dc7a">
f(x) = ax + b

f(1) = 3:  a(1) + b = 3  →  a + b = 3
f(4) = 12: a(4) + b = 12 →  4a + b = 12

Subtraindo:
4a + b − (a + b) = 12 − 3
3a = 9
a = 3

Substituindo: 3 + b = 3 → b = 0

Resposta: f(x) = 3x
</pre>

<p>
<b>Sinal da função afim:</b>
</p>

<p>
Para f(x) = ax + b, raiz em x = −b/a:
</p>

<pre class="example" id="org331563e">
Se a &gt; 0 (crescente):
  f(x) &gt; 0 para x &gt; −b/a
  f(x) &lt; 0 para x &lt; −b/a

Se a &lt; 0 (decrescente):
  f(x) &gt; 0 para x &lt; −b/a
  f(x) &lt; 0 para x &gt; −b/a
</pre>

<p>
*Aplicação
</p>
<ul class="org-ul">
<li>Questão Rápida:*</li>
</ul>

<p>
Uma empresa cobra taxa fixa de R$ 50 mais R$ 0,20 por minuto. Qual o custo de uma chamada de 40 minutos?
</p>

<pre class="example" id="org35d1deb">
f(x) = 0,20x + 50
f(40) = 0,20(40) + 50 = 8 + 50 = R$ 58
</pre>
</div>
</div>

<div id="outline-container-org9b789da" class="outline-4">
<h4 id="org9b789da"><span class="section-number-4">2.2.3.</span> PARTE 2: Função Quadrática (2º Grau)</h4>
<div class="outline-text-4" id="text-2-2-3">
<p>
<b>Definição:</b>
</p>

<pre class="example" id="org47d2001">
f(x) = ax² + bx + c, onde a ≠ 0
</pre>

<p>
<b>Gráfico:</b> sempre uma PARÁBOLA
</p>

<p>
<b>Concavidade:</b>
</p>

<pre class="example" id="orgc7e5519">
a &gt; 0: parábola abre para CIMA (∪)
a &lt; 0: parábola abre para BAIXO (∩)
</pre>

<p>
<b>Discriminante (Delta):</b>
</p>

<pre class="example" id="org2800c05">
Δ = b² − 4ac
</pre>

<p>
<b>Raízes (fórmula de Bhaskara):</b>
</p>

<pre class="example" id="org899143b">
x = (−b ± √Δ) / 2a
</pre>

<p>
<b>Análise do discriminante:</b>
</p>

<pre class="example" id="org654d7ad">
Δ &gt; 0: duas raízes reais distintas (parábola corta x em 2 pontos)
Δ = 0: uma raiz real (parábola tangencia x)
Δ &lt; 0: nenhuma raiz real (parábola não toca x)
</pre>

<p>
<b>Vértice da parábola:</b>
</p>

<pre class="example" id="orgce083c1">
xᵥ = −b / 2a
yᵥ = −Δ / 4a  ou  yᵥ = f(xᵥ)
</pre>

<p>
<b>Ponto de máximo ou mínimo:</b>
</p>
<ul class="org-ul">
<li>Se a &gt; 0: vértice é ponto de <b>mínimo</b></li>
<li>Se a &lt; 0: vértice é ponto de <b>máximo</b></li>
</ul>

<p>
<b>Conjunto imagem:</b>
</p>

<pre class="example" id="org402bcb1">
a &gt; 0: Im = [yᵥ, +∞)  (y ≥ yᵥ)
a &lt; 0: Im = (−∞, yᵥ]  (y ≤ yᵥ)
</pre>

<p>
<b>Eixo de simetria:</b>
</p>

<pre class="example" id="orgcb2cd78">
x = xᵥ = −b/2a
</pre>

<p>
<b>Soma e produto das raízes:</b>
</p>

<pre class="example" id="orgdae0fc9">
x₁ + x₂ = −b/a
x₁ · x₂ = c/a
</pre>

<p>
<b>Forma fatorada (quando tem raízes):</b>
</p>

<pre class="example" id="org7212f40">
f(x) = a(x − x₁)(x − x₂)
</pre>
</div>
</div>

<div id="outline-container-org2a83b93" class="outline-4">
<h4 id="org2a83b93"><span class="section-number-4">2.2.4.</span> Exemplo Completo</h4>
<div class="outline-text-4" id="text-2-2-4">
<ul class="org-ul">
<li>Função Quadrática</li>
</ul>
<p>
<b>Dada f(x) = x² − 6x + 5:</b>
</p>

<p>
<b>a) Raízes:</b>
</p>

<pre class="example" id="orgead5f5e">
Δ = b² − 4ac = (−6)² − 4(1)(5) = 36 − 20 = 16

x = [6 ± 4] / 2

x₁ = 10/2 = 5
x₂ = 2/2 = 1

Raízes: 1 e 5
</pre>

<p>
<b>Verificação por fatoração:</b>
</p>

<pre class="example" id="org1abdf43">
x² − 6x + 5 = (x − 1)(x − 5) ✓
</pre>

<p>
<b>b) Vértice:</b>
</p>

<pre class="example" id="org58200a7">
xᵥ = −b/2a = 6/2 = 3

yᵥ = f(3) = 3² − 6(3) + 5 = 9 − 18 + 5 = −4

Vértice: V(3, −4)
</pre>

<p>
<b>c) Gráfico:</b>
</p>

<pre class="example" id="org31d1090">
  y
  │
  5│●             ●
  │  \\         /
  0├───●─────●─────→ x
  │   1     5
  │      ●
 -4│     (3,-4)
  │    vértice

- Concavidade: para cima (a = 1 &gt; 0)
- Raízes: x = 1 e x = 5
- Vértice: V(3, −4)
- ponto de mínimo
</pre>

<p>
<b>d) Imagem:</b>
</p>

<pre class="example" id="org80a2419">
Im = [−4, +∞)  ou  {y ∈ ℝ | y ≥ −4}
</pre>

<p>
<b>e) Sinal:</b>
</p>

<pre class="example" id="orgfe85b6b">
f(x) &gt; 0: x &lt; 1 ou x &gt; 5
f(x) = 0: x = 1 ou x = 5
f(x) &lt; 0: 1 &lt; x &lt; 5
</pre>
</div>
</div>

<div id="outline-container-org4b2b270" class="outline-4">
<h4 id="org4b2b270"><span class="section-number-4">2.2.5.</span> Sinal da Função Quadrática</h4>
<div class="outline-text-4" id="text-2-2-5">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<p>
<b>Caso 1: Δ &gt; 0 (duas raízes: x₁ e x₂, com x₁ &lt; x₂)</b>
</p>

<pre class="example" id="org0cd78bf">
Se a &gt; 0 (∪):
  f(x) &gt; 0: x &lt; x₁ ou x &gt; x₂ (fora das raízes)
  f(x) &lt; 0: x₁ &lt; x &lt; x₂ (entre as raízes)

Se a &lt; 0 (∩):
  f(x) &gt; 0: x₁ &lt; x &lt; x₂ (entre as raízes)
  f(x) &lt; 0: x &lt; x₁ ou x &gt; x₂ (fora das raízes)
</pre>

<p>
<b>Caso 2: Δ = 0 (uma raiz: x₀)</b>
</p>

<pre class="example" id="orgdb44549">
Se a &gt; 0: f(x) ≥ 0 para todo x (toca x apenas em x₀)
Se a &lt; 0: f(x) ≤ 0 para todo x (toca x apenas em x₀)
</pre>

<p>
<b>Caso 3: Δ &lt; 0 (sem raízes reais)</b>
</p>

<pre class="example" id="org0772f43">
Se a &gt; 0: f(x) &gt; 0 para todo x (sempre positiva)
Se a &lt; 0: f(x) &lt; 0 para todo x (sempre negativa)
</pre>
</div>
</div>

<div id="outline-container-orgd6854ec" class="outline-4">
<h4 id="orgd6854ec"><span class="section-number-4">2.2.6.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-2-2-6">
</div>
<div id="outline-container-org81dc22e" class="outline-5">
<h5 id="org81dc22e"><span class="section-number-5">2.2.6.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-2-2-6-1">
<p>
Determine a raiz de f(x) = 2x − 8.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org69dc06e">
2x − 8 = 0
x = 4
</pre>
</div>
</div>

<div id="outline-container-orga160ff7" class="outline-5">
<h5 id="orga160ff7"><span class="section-number-5">2.2.6.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-2-2-6-2">
<p>
Uma função afim passa por (0, 5) e (2, 9). Determine f(x).
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org295401d">
b = 5 (ponto (0, 5))
a = (9−5)/(2−0) = 4/2 = 2
f(x) = 2x + 5
</pre>
</div>
</div>

<div id="outline-container-org7a862a8" class="outline-5">
<h5 id="org7a862a8"><span class="section-number-5">2.2.6.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-2-2-6-3">
<p>
Resolva x² − 5x + 6 = 0.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org64638f9">
Δ = 25 − 24 = 1
x = (5 ± 1)/2
x₁ = 3, x₂ = 2
</pre>
</div>
</div>

<div id="outline-container-org0fad32c" class="outline-5">
<h5 id="org0fad32c"><span class="section-number-5">2.2.6.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-2-2-6-4">
<p>
Determine o vértice de f(x) = −x² + 4x − 3.
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org6eb6871">
xᵥ = −4/(2×(−1)) = 4/2 = 2
yᵥ = −(2)² + 4(2) − 3 = −4 + 8 − 3 = 1
V(2, 1)
- ponto de máximo
</pre>
</div>
</div>

<div id="outline-container-org4a87bfe" class="outline-5">
<h5 id="org4a87bfe"><span class="section-number-5">2.2.6.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-2-2-6-5">
<p>
Para quais valores de x a função f(x) = x² − 4 é negativa?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org2814572">
x² − 4 &lt; 0
Raízes: x = ±2
a &gt; 0 → negativa entre as raízes
−2 &lt; x &lt; 2
</pre>
</div>
</div>
</div>

<div id="outline-container-orgdb29452" class="outline-4">
<h4 id="orgdb29452"><span class="section-number-4">2.2.7.</span> Problemas Aplicados</h4>
<div class="outline-text-4" id="text-2-2-7">
</div>
<div id="outline-container-org0d10e6b" class="outline-5">
<h5 id="org0d10e6b"><span class="section-number-5">2.2.7.1.</span> Problema 1 (Afim)</h5>
<div class="outline-text-5" id="text-2-2-7-1">
<p>
Um táxi cobra R$ 5 de bandeirada mais R$ 3 por km. Quanto custa uma corrida de 12 km?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgfd0be05">
f(x) = 3x + 5
f(12) = 3(12) + 5 = 36 + 5 = R$ 41
</pre>
</div>
</div>

<div id="outline-container-orgb98b46d" class="outline-5">
<h5 id="orgb98b46d"><span class="section-number-5">2.2.7.2.</span> Problema 2 (Quadrática)</h5>
<div class="outline-text-5" id="text-2-2-7-2">
<p>
Um projétil é lançado com altura h(t) = −5t² + 20t (metros). Qual a altura máxima?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgb46281d">
a = −5 &lt; 0 → tem máximo no vértice
tᵥ = −20/(2×(−5)) = 20/10 = 2 segundos
h_máx = −5(2)² + 20(2) = −20 + 40 = 20 metros
</pre>
</div>
</div>
</div>

<div id="outline-container-org331257a" class="outline-4">
<h4 id="org331257a"><span class="section-number-4">2.2.8.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-2-8">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<pre class="example" id="org569405f">
FUNÇÃO AFIM:
f(x) = ax + b
Raiz: x = −b/a
Coef. angular: a = Δy/Δx

FUNÇÃO QUADRÁTICA:
f(x) = ax² + bx + c

Discriminante:
Δ = b² − 4ac

Raízes (Bhaskara):
x = (−b ± √Δ) / 2a

Vértice:
xᵥ = −b/2a
yᵥ = −Δ/4a

Soma e produto:
x₁ + x₂ = −b/a
x₁ · x₂ = c/a

Imagem:
a &gt; 0: Im = [yᵥ, +∞)
a &lt; 0: Im = (−∞, yᵥ]
</pre>
</div>
</div>

<div id="outline-container-orgecf6132" class="outline-4">
<h4 id="orgecf6132"><span class="section-number-4">2.2.9.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-2-2-9">
<p>
<b>Função Afim:</b>
</p>
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei determinar f(x) dados dois pontos</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular a raiz</li>
<li class="off"><code>[&#xa0;]</code> Sei identificar se é crescente ou decrescente</li>
<li class="off"><code>[&#xa0;]</code> Sei esboçar o gráfico</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver problemas aplicados</li>
</ul>

<p>
<b>Função Quadrática:</b>
</p>
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei calcular delta e aplicar Bhaskara</li>
<li class="off"><code>[&#xa0;]</code> Sei determinar o vértice</li>
<li class="off"><code>[&#xa0;]</code> Sei identificar concavidade</li>
<li class="off"><code>[&#xa0;]</code> Sei esboçar o gráfico completo</li>
<li class="off"><code>[&#xa0;]</code> Sei determinar o sinal da função</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular imagem</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver problemas de máximo/mínimo</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgee2054a" class="outline-3">`;

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
