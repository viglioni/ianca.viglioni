<script setup lang="ts">
import { ref } from "vue";

const code = "mat-75";
const title = "Matemática: Revisão Geral";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-1">
<ul class="org-ul">
<li>Matemática: Revisão Geral</li>
<li>Todos os Tópicos</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-org982a8c7" class="outline-4">
<h4 id="org982a8c7"><span class="section-number-4">4.1.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-4-1-1">
<p>
Revisão abrangente de TODOS os tópicos de Matemática vistos, com foco em resolver dúvidas e fixar pontos críticos.
</p>
</div>
</div>

<div id="outline-container-org4e4d209" class="outline-4">
<h4 id="org4e4d209"><span class="section-number-4">4.1.2.</span> BLOCO 1: Conjuntos e Fundamentos (15min)</h4>
<div class="outline-text-4" id="text-4-1-2">
<p>
<b>Relações essenciais:</b>
</p>

<pre class="example" id="orgae3afa8">
∈ (pertence): 3 ∈ {1, 2, 3}
⊂ (contido): {1, 2} ⊂ {1, 2, 3}
∪ (união): {1, 2} ∪ {2, 3} = {1, 2, 3}
∩ (interseção): {1, 2} ∩ {2, 3} = {2}

n(A ∪ B) = n(A) + n(B) − n(A ∩ B)
</pre>

<p>
<b>MMC e MDC:</b>
</p>

<pre class="example" id="org6ca3a1a">
MMC: menor múltiplo comum (eventos que se repetem)
MDC: maior divisor comum (dividir em partes iguais)

MMC × MDC = produto dos números
</pre>

<p>
<b>Questão rápida:</b>
</p>

<pre class="example" id="org8c48450">
Dois ônibus passam juntos às 6h. Um passa a cada 12 min, outro a cada 18 min.
Quando passarão juntos novamente?

MMC(12, 18) = 36 minutos
Resposta: 6h36min
</pre>
</div>
</div>

<div id="outline-container-orgdbb66a3" class="outline-4">
<h4 id="orgdbb66a3"><span class="section-number-4">4.1.3.</span> BLOCO 2: Funções (30min)</h4>
<div class="outline-text-4" id="text-4-1-3">
<p>
<b>Função Afim: f(x) = ax + b</b>
</p>

<pre class="example" id="org08969a6">
a &gt; 0: crescente
a &lt; 0: decrescente
Raiz: x = −b/a
</pre>

<p>
<b>Função Quadrática: f(x) = ax² + bx + c</b>
</p>

<pre class="example" id="org1e12571">
Δ = b² − 4ac
x = (−b ± √Δ) / 2a

Vértice:
xᵥ = −b/2a
yᵥ = −Δ/4a

Concavidade:
a &gt; 0: ∪ (mínimo no vértice)
a &lt; 0: ∩ (máximo no vértice)

Sinal (a &gt; 0, Δ &gt; 0):
f(x) &gt; 0: fora das raízes
f(x) &lt; 0: entre as raízes
</pre>

<p>
<b>Função Exponencial: f(x) = aˣ</b>
</p>

<pre class="example" id="org69b48f0">
a &gt; 1: crescente
0 &lt; a &lt; 1: decrescente

Propriedades:
aˣ · aʸ = aˣ⁺ʸ
aˣ / aʸ = aˣ⁻ʸ
(aˣ)ʸ = aˣʸ
</pre>

<p>
<b>Função Logarítmica: f(x) = logₐ x</b>
</p>

<pre class="example" id="org5f16f0d">
logₐ b = x ⟺ aˣ = b

Casos especiais:
logₐ 1 = 0
logₐ a = 1
logₐ aˣ = x

Propriedades:
logₐ (bc) = logₐ b + logₐ c
logₐ (b/c) = logₐ b − logₐ c
logₐ bⁿ = n · logₐ b

Mudança de base:
logₐ b = log b / log a
</pre>

<p>
<b>Exercício integrador:</b>
</p>

<pre class="example" id="org9fa2da1">
Resolva o sistema:
{f(x) = x² − 4
{g(x) = 2x − 4

x² − 4 = 2x − 4
x² − 2x = 0
x(x − 2) = 0
x = 0 ou x = 2

Pontos: (0, −4) e (2, 0)
</pre>
</div>
</div>

<div id="outline-container-orgba106e5" class="outline-4">
<h4 id="orgba106e5"><span class="section-number-4">4.1.4.</span> BLOCO 3: Geometria (25min)</h4>
<div class="outline-text-4" id="text-4-1-4">
<p>
<b>Áreas (revisão rápida):</b>
</p>

<pre class="example" id="org2965464">
Triângulo: (b × h)/2
Quadrado: L²
Retângulo: b × h
Trapézio: [(B + b) × h]/2
Círculo: πr²
</pre>

<p>
<b>Perímetros:</b>
</p>

<pre class="example" id="orgdb44a6e">
Quadrado: 4L
Retângulo: 2(b + h)
Círculo: 2πr
</pre>

<p>
<b>Pitágoras:</b>
</p>

<pre class="example" id="org053ef94">
a² = b² + c²

Ternas: (3,4,5), (5,12,13), (8,15,17)
</pre>

<p>
<b>Exemplo prático:</b>
</p>

<pre class="example" id="org9fe8d2e">
Uma escada de 5 m está a 3 m da parede. Qual a altura alcançada?

5² = 3² + h²
25 = 9 + h²
h² = 16
h = 4 m
</pre>
</div>
</div>

<div id="outline-container-org1307628" class="outline-4">
<h4 id="org1307628"><span class="section-number-4">4.1.5.</span> BLOCO 4: Trigonometria (20min)</h4>
<div class="outline-text-4" id="text-4-1-5">
<p>
<b>Tabela obrigatória:</b>
</p>

<pre class="example" id="orga248c6f">
       30°    45°    60°
sen:   1/2    √2/2   √3/2
cos:   √3/2   √2/2   1/2
tg:    √3/3   1      √3
</pre>

<p>
<b>Relações:</b>
</p>

<pre class="example" id="orgc5221b2">
sen² α + cos² α = 1
tg α = sen α / cos α

sen α = CO / H
cos α = CA / H
tg α = CO / CA
</pre>

<p>
<b>Exercício:</b>
</p>

<pre class="example" id="org14425c8">
Em um triângulo retângulo, hipotenusa = 10 m, ângulo = 30°.
Calcule o cateto oposto.

sen 30° = CO / 10
1/2 = CO / 10
CO = 5 m
</pre>
</div>
</div>

<div id="outline-container-org1675b1f" class="outline-4">
<h4 id="org1675b1f"><span class="section-number-4">4.1.6.</span> BLOCO 5: Razão, Proporção e Porcentagem (15min)</h4>
<div class="outline-text-4" id="text-4-1-6">
<p>
<b>Razão:</b>
</p>

<pre class="example" id="org90127a6">
a/b (a está para b)
</pre>

<p>
<b>Proporção:</b>
</p>

<pre class="example" id="org0dbc0a1">
a/b = c/d → ad = bc
</pre>

<p>
<b>Regra de três:</b>
</p>

<pre class="example" id="org0ca82f9">
Direta: grandezas na mesma direção
Inversa: grandezas em direções opostas
</pre>

<p>
<b>Porcentagem:</b>
</p>

<pre class="example" id="org3c69c61">
x% de y = (x/100) × y

Aumento de x%: multiplicar por (1 + x/100)
Desconto de x%: multiplicar por (1 − x/100)
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org2d7699d">
Preço: R$ 200
Aumento de 15%: 200 × 1,15 = R$ 230
Desconto de 20%: 200 × 0,80 = R$ 160
</pre>
</div>
</div>

<div id="outline-container-org87a58a4" class="outline-4">
<h4 id="org87a58a4"><span class="section-number-4">4.1.7.</span> BLOCO 6: Estatística Básica (15min)</h4>
<div class="outline-text-4" id="text-4-1-7">
<p>
<b>Média aritmética:</b>
</p>

<pre class="example" id="orgc5000c7">
MA = (x₁ + x₂ + ... + xₙ) / n
</pre>

<p>
<b>Mediana:</b>
</p>
<ul class="org-ul">
<li>Ordenar os dados</li>
<li>Valor central (ou média dos dois centrais)</li>
</ul>

<p>
<b>Moda:</b>
</p>
<ul class="org-ul">
<li>Valor que mais aparece</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org7fc347a">
Dados: 5, 7, 7, 8, 10

Média: (5+7+7+8+10)/5 = 37/5 = 7,4
Mediana: 7 (valor central)
Moda: 7 (aparece 2 vezes)
</pre>
</div>
</div>

<div id="outline-container-orgeb7031b" class="outline-4">
<h4 id="orgeb7031b"><span class="section-number-4">4.1.8.</span> BLOCO 7: Problemas Mistos</h4>
<div class="outline-text-4" id="text-4-1-8">
<ul class="org-ul">
<li>Treino Final</li>
</ul>
</div>
<div id="outline-container-orgacdc0e7" class="outline-5">
<h5 id="orgacdc0e7"><span class="section-number-5">4.1.8.1.</span> Problema 1</h5>
<div class="outline-text-5" id="text-4-1-8-1">
<p>
Um terreno retangular tem 15 m de comprimento e 8 m de largura. Calcule: a) Área b) Perímetro c) Diagonal
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orga3f0053">
a) A = 15 × 8 = 120 m²
b) P = 2(15 + 8) = 2(23) = 46 m
c) d² = 15² + 8² = 225 + 64 = 289 → d = 17 m
</pre>
</div>
</div>

<div id="outline-container-org236b7ef" class="outline-5">
<h5 id="org236b7ef"><span class="section-number-5">4.1.8.2.</span> Problema 2</h5>
<div class="outline-text-5" id="text-4-1-8-2">
<p>
Resolva: log₂ (x + 3) = 4
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org7a32bc6">
x + 3 = 2⁴
x + 3 = 16
x = 13

Verificação: x + 3 = 16 &gt; 0 ✓
</pre>
</div>
</div>

<div id="outline-container-org10ca518" class="outline-5">
<h5 id="org10ca518"><span class="section-number-5">4.1.8.3.</span> Problema 3</h5>
<div class="outline-text-5" id="text-4-1-8-3">
<p>
Uma população de bactérias dobra a cada hora. Começando com 100, quantas haverá em 5 horas?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org5482283">
P(t) = 100 × 2ᵗ
P(5) = 100 × 2⁵ = 100 × 32 = 3200 bactérias
</pre>
</div>
</div>

<div id="outline-container-org0d36cb4" class="outline-5">
<h5 id="org0d36cb4"><span class="section-number-5">4.1.8.4.</span> Problema 4</h5>
<div class="outline-text-5" id="text-4-1-8-4">
<p>
Determine o vértice de f(x) = x² − 6x + 5.
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org987fe24">
xᵥ = −(−6)/(2×1) = 6/2 = 3
yᵥ = 3² − 6(3) + 5 = 9 − 18 + 5 = −4

Vértice: V(3, −4)
</pre>
</div>
</div>

<div id="outline-container-org4a4235b" class="outline-5">
<h5 id="org4a4235b"><span class="section-number-5">4.1.8.5.</span> Problema 5</h5>
<div class="outline-text-5" id="text-4-1-8-5">
<p>
15% dos alunos faltaram. Se 34 compareceram, quantos são no total?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org5a1b3a5">
15% faltaram → 85% compareceram

85% de x = 34
0,85x = 34
x = 34/0,85 = 40 alunos
</pre>
</div>
</div>
</div>

<div id="outline-container-org2a5959a" class="outline-4">
<h4 id="org2a5959a"><span class="section-number-4">4.1.9.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-1-9">
<ul class="org-ul">
<li>RESUMO GERAL</li>
</ul>
<pre class="example" id="orgf90cc4e">
CONJUNTOS:
n(A ∪ B) = n(A) + n(B) − n(A ∩ B)

FUNÇÕES:
Afim: f(x) = ax + b, raiz = −b/a
Quadrática: Δ = b² − 4ac, x = (−b±√Δ)/2a, xᵥ=−b/2a
Exponencial: aˣ·aʸ = aˣ⁺ʸ
Logarítmica: logₐ b = x ⟺ aˣ = b

GEOMETRIA:
Triângulo: A = bh/2
Círculo: A = πr², C = 2πr
Pitágoras: a² = b² + c²

TRIGONOMETRIA:
sen α = CO/H, cos α = CA/H, tg α = CO/CA
sen²α + cos²α = 1

       30°    45°    60°
sen:   1/2    √2/2   √3/2
cos:   √3/2   √2/2   1/2

ESTATÍSTICA:
Média = soma / quantidade
</pre>
</div>
</div>

<div id="outline-container-orgdd99fb4" class="outline-4">
<h4 id="orgdd99fb4"><span class="section-number-4">4.1.10.</span> Checklist Final</h4>
<div class="outline-text-4" id="text-4-1-10">
<ul class="org-ul">
<li>Matemática</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver problemas de conjuntos</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular MMC e MDC</li>
<li class="off"><code>[&#xa0;]</code> Sei trabalhar com funções afim e quadrática</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver equações exponenciais e logarítmicas</li>
<li class="off"><code>[&#xa0;]</code> Sei todas as propriedades de logaritmos</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular áreas e perímetros</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar Pitágoras</li>
<li class="off"><code>[&#xa0;]</code> Memorizei a tabela trigonométrica (30°, 45°, 60°)</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver regra de três</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular porcentagens</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular média, mediana, moda</li>
</ul>
</div>
</div>

<div id="outline-container-orgecf0aac" class="outline-4">
<h4 id="orgecf0aac"><span class="section-number-4">4.1.11.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-1-11">
<ol class="org-ol">
<li><b>Leia com atenção</b></li>
<li>identifique o que é pedido</li>
<li><b>Escreva os dados</b></li>
<li>organize informações</li>
<li><b>Escolha a fórmula certa</b></li>
<li>revise mentalmente</li>
<li><b>Calcule com calma</b></li>
<li>erros bobos custam pontos</li>
<li><b>Verifique o resultado</b></li>
<li>faz sentido?</li>
<li><b>Geometria:</b> sempre faça um esboço</li>
<li><b>Logaritmo:</b> sempre verifique condições de existência</li>
<li><b>MRUV vs MRU:</b> identifique se há aceleração</li>
</ol>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio-Alto (revisão abrangente) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (TODO o conteúdo!)
</p>
</div>
</div>
</div>

<div id="outline-container-org6bb3132" class="outline-3">`;

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
