<script setup lang="ts">
import { ref } from "vue";

const code = "fis-37";
const title = "Física: Forças Especiais";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-2">
<ul class="org-ul">
<li>Física: Forças Especiais</li>
<li>Peso, Normal e Atrito (Revisão e Aprofundamento)</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-orge816d79" class="outline-4">
<h4 id="orge816d79"><span class="section-number-4">5.2.1.</span> Revisão: Leis de Newton</h4>
<div class="outline-text-4" id="text-5-2-1">
<p>
Na Aula 22, estudamos as Leis de Newton e tipos básicos de forças.
</p>

<p>
<b>Nesta aula:</b> Aprofundamento em forças especiais e aplicações.
</p>
</div>
</div>

<div id="outline-container-orgceb6e12" class="outline-4">
<h4 id="orgceb6e12"><span class="section-number-4">5.2.2.</span> Força Peso (P)</h4>
<div class="outline-text-4" id="text-5-2-2">
<p>
<b>Definição:</b> Força gravitacional que a Terra exerce sobre um corpo.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgc69f6fc">
P = m · g
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>P: peso (N</li>
<li>newtons)</li>
<li>m: massa (kg)</li>
<li>g: aceleração da gravidade (m/s²)</li>
</ul>

<p>
<b>Na Terra:</b> g ≈ 10 m/s² (ou 9,8 m/s² para maior precisão)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Direção:</b> vertical</li>
<li><b>Sentido:</b> para baixo (centro da Terra)</li>
<li><b>Ponto de aplicação:</b> centro de gravidade do corpo</li>
</ul>

<p>
<b>Diferença Massa vs. Peso:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Massa (m)</th>
<th scope="col" class="org-left">Peso (P)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Quantidade de matéria</td>
<td class="org-left">Força gravitacional</td>
</tr>

<tr>
<td class="org-left">Escalar (kg)</td>
<td class="org-left">Vetor (N)</td>
</tr>

<tr>
<td class="org-left">NÃO varia</td>
<td class="org-left">VARIA com g</td>
</tr>

<tr>
<td class="org-left">Mesma em qualquer lugar</td>
<td class="org-left">Diferente em planetas</td>
</tr>
</tbody>
</table>

<p>
<b>Exemplos:</b>
</p>

<p>
Pessoa com 60 kg:
</p>
<ul class="org-ul">
<li><b>Terra:</b> P = 60 × 10 = 600 N</li>
<li><b>Lua:</b> g_Lua ≈ 1,6 m/s² → P = 60 × 1,6 = 96 N</li>
<li><b>Massa:</b> 60 kg (não muda!)</li>
</ul>
</div>
</div>

<div id="outline-container-org0ee738f" class="outline-4">
<h4 id="org0ee738f"><span class="section-number-4">5.2.3.</span> Força Normal (N)</h4>
<div class="outline-text-4" id="text-5-2-3">
<p>
<b>Definição:</b> Força de reação da superfície, perpendicular ao contato.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Direção:</b> perpendicular à superfície</li>
<li><b>Sentido:</b> “empurra” o corpo para fora da superfície</li>
<li><b>Intensidade:</b> varia conforme situação</li>
</ul>

<p>
<b>NÃO é sempre igual ao peso!</b>
</p>
</div>

<div id="outline-container-orged04b50" class="outline-5">
<h5 id="orged04b50"><span class="section-number-5">5.2.3.1.</span> Caso 1: Superfície Horizontal (equilíbrio vertical)</h5>
<div class="outline-text-5" id="text-5-2-3-1">
<pre class="example" id="org12b8291">
  ↑ N
  |
[corpo]
  |
  ↓ P
</pre>

<p>
<b>Equilíbrio vertical:</b> ΣF_y = 0 N
</p>
<ul class="org-ul">
<li>P = 0 <b>N = P = mg</b></li>
</ul>
</div>
</div>

<div id="outline-container-org9dfae43" class="outline-5">
<h5 id="org9dfae43"><span class="section-number-5">5.2.3.2.</span> Caso 2: Corpo em Aceleração Vertical</h5>
<div class="outline-text-5" id="text-5-2-3-2">
<p>
<b>a) Elevador subindo acelerado (a ↑):</b>
</p>

<pre class="example" id="org9155822">
  ↑ N
  |
[corpo] ↑ a
  |
  ↓ P
</pre>

<p>
F_R = ma (para cima) N
</p>
<ul class="org-ul">
<li>P = ma <b>N = P + ma = m(g + a)</b></li>
</ul>

<p>
Normal <b>maior</b> que peso (sensação de “mais pesado”)
</p>

<p>
<b>b) Elevador descendo acelerado (a ↓):</b>
</p>

<p>
F_R = ma (para baixo) P
</p>
<ul class="org-ul">
<li>N = ma *N = P</li>
<li>ma = m(g</li>
<li>a)*</li>
</ul>

<p>
Normal <b>menor</b> que peso (sensação de “mais leve”)
</p>

<p>
<b>c) Queda livre (a = g ↓):</b>
</p>

<p>
N = m(g
</p>
<ul class="org-ul">
<li>g) = 0</li>
</ul>

<p>
<b>N = 0</b> (ausência de peso, “flutuação”)
</p>
</div>
</div>

<div id="outline-container-orgf0364a0" class="outline-5">
<h5 id="orgf0364a0"><span class="section-number-5">5.2.3.3.</span> Caso 3: Plano Inclinado</h5>
<div class="outline-text-5" id="text-5-2-3-3">
<pre class="example" id="org3742fb7">
        N ↑ (perp. ao plano)
       /|
      / |
   [corpo]
    / | \\
   /  |  \\ P_y (paralela)
  /   |   \\
 /    ↓    \\
/   P_x     \\ θ
──────────────
</pre>

<p>
<b>Decomposição do peso:</b>
</p>
<ul class="org-ul">
<li>P_x = P · sen(θ) = mg sen(θ) (paralelo ao plano)</li>
<li>P_y = P · cos(θ) = mg cos(θ) (perpendicular ao plano)</li>
</ul>

<p>
<b>Equilíbrio perpendicular:</b> <b>N = P_y = mg cos(θ)</b>
</p>
</div>
</div>

<div id="outline-container-org853597b" class="outline-5">
<h5 id="org853597b"><span class="section-number-5">5.2.3.4.</span> Caso 4: Corpo Pressionado Contra Parede</h5>
<div class="outline-text-5" id="text-5-2-3-4">
<pre class="example" id="orgf383d29">
Parede
  │ ← N
  │
  │ [corpo] → F (força aplicada)
  │
</pre>

<p>
<b>N = F</b> (força aplicada horizontalmente)
</p>
</div>
</div>
</div>

<div id="outline-container-org973f929" class="outline-4">
<h4 id="org973f929"><span class="section-number-4">5.2.4.</span> Força de Atrito (F_at)</h4>
<div class="outline-text-4" id="text-5-2-4">
<p>
<b>Definição:</b> Força que se opõe ao movimento relativo entre superfícies em contato.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Direção:</b> paralela às superfícies</li>
<li><b>Sentido:</b> oposto ao movimento (ou tendência)</li>
<li><b>Origem:</b> irregularidades microscópicas das superfícies</li>
</ul>
</div>

<div id="outline-container-orgae942bd" class="outline-5">
<h5 id="orgae942bd"><span class="section-number-5">5.2.4.1.</span> Atrito Estático (F_at,e)</h5>
<div class="outline-text-5" id="text-5-2-4-1">
<p>
<b>Quando:</b> corpo em repouso, tende a se mover mas ainda está parado.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Varia de 0 até máximo</li>
<li><b>F_at,e ≤ μ_e · N</b></li>
</ul>

<p>
<b>Força de atrito estático máximo:</b>
</p>

<pre class="example" id="org56fa791">
F_at,e(máx) = μ_e · N
</pre>

<p>
<b>μ_e:</b> coeficiente de atrito estático (adimensional)
</p>

<p>
<b>Exemplo:</b> Empurrando caixa com força crescente:
</p>
<ul class="org-ul">
<li>Força pequena: caixa não move (F_at = F_aplicada)</li>
<li>Aumenta força: atrito aumenta</li>
<li>Atinge F_at(máx): caixa está prestes a deslizar</li>
<li>Ultrapassa F_at(máx): caixa começa a deslizar</li>
</ul>
</div>
</div>

<div id="outline-container-org3f3c9bc" class="outline-5">
<h5 id="org3f3c9bc"><span class="section-number-5">5.2.4.2.</span> Atrito Cinético (F_at,c)</h5>
<div class="outline-text-5" id="text-5-2-4-2">
<p>
<b>Quando:</b> corpo em movimento.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org8615e46">
F_at,c = μ_c · N
</pre>

<p>
<b>μ_c:</b> coeficiente de atrito cinético
</p>

<p>
<b>Observações:</b>
</p>
<ul class="org-ul">
<li>Valor constante (não varia)</li>
<li>Geralmente μ_c &lt; μ_e (mais fácil manter movimento que iniciar)</li>
</ul>
</div>
</div>

<div id="outline-container-org1451125" class="outline-5">
<h5 id="org1451125"><span class="section-number-5">5.2.4.3.</span> Fatores que Influenciam o Atrito</h5>
<div class="outline-text-5" id="text-5-2-4-3">
<p>
<b>Depende de:</b>
</p>
<ul class="org-ul">
<li><b>Natureza das superfícies:</b> μ (coeficiente)</li>
<li><b>Força normal:</b> N</li>
</ul>

<p>
<b>NÃO depende de:</b>
</p>
<ul class="org-ul">
<li>Área de contato</li>
<li>Velocidade (atrito cinético)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org2a745b7" class="outline-4">
<h4 id="org2a745b7"><span class="section-number-4">5.2.5.</span> Aplicações</h4>
<div class="outline-text-4" id="text-5-2-5">
</div>
<div id="outline-container-org84bb45f" class="outline-5">
<h5 id="org84bb45f"><span class="section-number-5">5.2.5.1.</span> Problema 1</h5>
<div class="outline-text-5" id="text-5-2-5-1">
<p>
Um bloco de 10 kg está sobre uma superfície horizontal. μ_e = 0,4 e μ_c = 0,3. Qual a força mínima para: a) Tirar o bloco do repouso? b) Mantê-lo em movimento? (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
N = P = mg = 10 × 10 = 100 N
</p>

<ol class="org-ol">
<li><b>Força para tirar do repouso:</b> F ≥ F_at,e(máx) = μ_e · N = 0,4 × 100 = 40 N</li>
</ol>

<p>
<b>F ≥ 40 N</b>
</p>

<ol class="org-ol">
<li value="2"><b>Manter em movimento:</b> F = F_at,c = μ_c · N = 0,3 × 100 = 30 N</li>
</ol>

<p>
<b>F = 30 N</b>
</p>
</div>
</div>

<div id="outline-container-orgb819f00" class="outline-5">
<h5 id="orgb819f00"><span class="section-number-5">5.2.5.2.</span> Problema 2</h5>
<div class="outline-text-5" id="text-5-2-5-2">
<p>
Bloco de 5 kg em plano inclinado de 30°. Determine a normal e a componente paralela do peso. (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
P = 5 × 10 = 50 N
</p>

<p>
<b>Normal:</b> N = mg cos(30°) = 50 × (√3/2) ≈ 50 × 0,87 ≈ 43,5 N
</p>

<p>
<b>Componente paralela:</b> P_x = mg sen(30°) = 50 × 0,5 = 25 N
</p>
</div>
</div>
</div>

<div id="outline-container-orgd2351e6" class="outline-4">
<h4 id="orgd2351e6"><span class="section-number-4">5.2.6.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-2-6">
</div>
<div id="outline-container-orgff02903" class="outline-5">
<h5 id="orgff02903"><span class="section-number-5">5.2.6.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-2-6-1">
<p>
Qual o peso de um corpo de massa 8 kg na Terra (g = 10 m/s²)?
</p>

<p>
<b>Solução:</b> P = mg = 8 × 10 = 80 N
</p>

<p>
<i>[Ver resposta 29 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgd3b2598" class="outline-5">
<h5 id="orgd3b2598"><span class="section-number-5">5.2.6.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-2-6-2">
<p>
Uma pessoa de 70 kg está em um elevador que sobe com aceleração de 2 m/s². Qual a normal? (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
Elevador subindo acelerado: N = m(g + a) = 70(10 + 2) = 70 × 12 = 840 N
</p>

<p>
<i>[Ver resposta 30 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org9d0b9e3" class="outline-5">
<h5 id="org9d0b9e3"><span class="section-number-5">5.2.6.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-2-6-3">
<p>
(UFMG) Um bloco está em repouso sobre uma mesa. A força normal é: a) Sempre igual ao peso b) Par ação-reação do peso c) Força de reação da mesa
</p>

<p>
<i>[Ver resposta 31 no final do documento]</i>
</p>

<p>
<b>Importante:</b> Normal NÃO é par ação-reação do peso!
</p>
<ul class="org-ul">
<li>Peso: Terra atrai bloco</li>
<li>Reação do peso: Bloco atrai Terra</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgbe0ec4d" class="outline-4">
<h4 id="orgbe0ec4d"><span class="section-number-4">5.2.7.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-2-7">
<ol class="org-ol">
<li><b>Peso:</b> sempre P = mg (para baixo)</li>
<li><b>Normal:</b> perpendicular à superfície</li>
<li><b>N = P:</b> só em superfície horizontal sem aceleração vertical</li>
<li><b>Plano inclinado:</b> N = mg cos(θ)</li>
<li><b>Atrito estático:</b> F_at ≤ μ_e N (varia)</li>
<li><b>Atrito cinético:</b> F_at = μ_c N (constante)</li>
<li><b>μ_e &gt; μ_c:</b> iniciar movimento é mais difícil</li>
<li><b>Atrito:</b> sempre oposto ao movimento</li>
</ol>
</div>
</div>

<div id="outline-container-org2622005" class="outline-4">
<h4 id="org2622005"><span class="section-number-4">5.2.8.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-2-8">
<p>
<b>Peso:</b>
</p>
<ul class="org-ul">
<li>P = mg</li>
<li>Vertical, para baixo</li>
<li>Varia com g</li>
</ul>

<p>
<b>Normal:</b>
</p>
<ul class="org-ul">
<li>Perpendicular à superfície</li>
<li>Varia conforme situação</li>
<li>Horizontal: N = P</li>
<li>Inclinado: N = mg cos(θ)</li>
</ul>

<p>
<b>Atrito:</b>
</p>
<ul class="org-ul">
<li>Opõe movimento</li>
<li>Estático: F_at ≤ μ_e N</li>
<li>Cinético: F_at = μ_c N</li>
<li>μ_e &gt; μ_c</li>
</ul>
</div>
</div>

<div id="outline-container-orgca51de4" class="outline-4">
<h4 id="orgca51de4"><span class="section-number-4">5.2.9.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-5-2-9">
<pre class="example" id="orgbfc4a31">
Peso:
P = m · g

Normal (casos):
Horizontal: N = P = mg
Elevador (↑a): N = m(g + a)
Elevador (↓a): N = m(g
- a)
Plano inclinado: N = mg cos(θ)

Atrito:
Estático (máx): F_at,e = μ_e · N
Cinético: F_at,c = μ_c · N

Plano Inclinado:
P_paralela = mg sen(θ)
P_perpendicular = mg cos(θ)
</pre>
</div>
</div>

<div id="outline-container-org497db39" class="outline-4">
<h4 id="org497db39"><span class="section-number-4">5.2.10.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-2-10">
<pre class="example" id="org9abf2db">
PESO:
    [corpo]
       |
       ↓ P = mg
       
NORMAL:

Horizontal:    Inclinado (θ):
  ↑ N             N ↑
  |              /|
[corpo]      [corpo]
  |            /
  ↓ P         / P
           θ
           
ATRITO:

Estático:           Cinético:
[corpo] → F_apl   [corpo] → v
←F_at (varia)     ←F_at (constante)

F_at ≤ μ_e·N      F_at = μ_c·N
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 30 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>forças são essenciais!)</li>
</ul>
</div>
</div>
</div>
</div>

<div id="outline-container-orgb125073" class="outline-2">`;

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
