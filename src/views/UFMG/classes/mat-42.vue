<script setup lang="ts">
import { ref } from "vue";

const code = "mat-42";
const title = "Matemática: Relação entre Funções Exponencial e Logarítmica";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-8-1">
<ul class="org-ul">
<li>Matemática: Relação entre Funções Exponencial e Logarítmica</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-orgf6e38b5" class="outline-4">
<h4 id="orgf6e38b5"><span class="section-number-4">8.1.1.</span> Funções Inversas</h4>
<div class="outline-text-4" id="text-8-1-1">
<p>
<b>Definição:</b> Duas funções f e g são inversas se:
</p>

<pre class="example" id="org90f5d24">
f(g(x)) = x  e  g(f(x)) = x
</pre>

<p>
<b>Notação:</b> g = f⁻¹ (função inversa de f)
</p>

<p>
<b>Graficamente:</b> Gráficos são simétricos em relação à reta y = x
</p>
</div>
</div>

<div id="outline-container-org3269ba7" class="outline-4">
<h4 id="org3269ba7"><span class="section-number-4">8.1.2.</span> Função Exponencial e Logarítmica: Inversas</h4>
<div class="outline-text-4" id="text-8-1-2">
<p>
<b>Função exponencial:</b> f(x) = a^x <b>Função logarítmica:</b> g(x) = log_a x
</p>

<p>
<b>São funções inversas!</b>
</p>
</div>

<div id="outline-container-orgcddd3ae" class="outline-5">
<h5 id="orgcddd3ae"><span class="section-number-5">8.1.2.1.</span> Verificação</h5>
<div class="outline-text-5" id="text-8-1-2-1">
<p>
<b>1. f(g(x)) = x:</b>
</p>

<pre class="example" id="org6e40034">
f(g(x)) = f(log_a x)
        = a^(log_a x)
        = x  ✓
</pre>

<p>
<b>2. g(f(x)) = x:</b>
</p>

<pre class="example" id="orgae56120">
g(f(x)) = g(a^x)
        = log_a (a^x)
        = x  ✓
</pre>
</div>
</div>
</div>

<div id="outline-container-org4823f62" class="outline-4">
<h4 id="org4823f62"><span class="section-number-4">8.1.3.</span> Propriedades Fundamentais</h4>
<div class="outline-text-4" id="text-8-1-3">
<p>
<b>Decorrentes da relação inversa:</b>
</p>

<p>
<b>1. Composição:</b>
</p>

<pre class="example" id="org141aefd">
a^(log_a x) = x  (x &gt; 0)
log_a (a^x) = x  (x ∈ ℝ)
</pre>

<p>
<b>2. Domínio e Imagem:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Função</th>
<th scope="col" class="org-left">Domínio</th>
<th scope="col" class="org-left">Imagem</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">f(x) = a^x</td>
<td class="org-left">ℝ</td>
<td class="org-left">ℝ₊* (0, +∞)</td>
</tr>

<tr>
<td class="org-left">g(x) = log_a x</td>
<td class="org-left">ℝ₊* (0, +∞)</td>
<td class="org-left">ℝ</td>
</tr>
</tbody>
</table>

<p>
<b>Observe:</b> Domínio de uma é imagem da outra!
</p>

<p>
<b>3. Interceptos:</b>
</p>

<p>
<b>Exponencial:</b>
</p>
<ul class="org-ul">
<li>Intercepto y: (0, 1)</li>
<li>sempre!</li>
<li>Não intercepta eixo x (assíntota)</li>
</ul>

<p>
<b>Logarítmica:</b>
</p>
<ul class="org-ul">
<li>Intercepto x: (1, 0)</li>
<li>sempre!</li>
<li>Não intercepta eixo y (assíntota)</li>
</ul>
</div>
</div>

<div id="outline-container-orgbc1fcf8" class="outline-4">
<h4 id="orgbc1fcf8"><span class="section-number-4">8.1.4.</span> Gráficos: Simetria</h4>
<div class="outline-text-4" id="text-8-1-4">
<p>
<b>Propriedade:</b> Gráficos de f(x) = a^x e g(x) = log_a x são <b>simétricos</b> em relação à <b>reta y = x</b>.
</p>
</div>

<div id="outline-container-orgaef5d61" class="outline-5">
<h5 id="orgaef5d61"><span class="section-number-5">8.1.4.1.</span> Exemplo: a = 2</h5>
<div class="outline-text-5" id="text-8-1-4-1">
<p>
<b>f(x) = 2^x:</b>
</p>
<ul class="org-ul">
<li>Passa por (0, 1), (1, 2), (2, 4)</li>
<li>Crescente</li>
<li>Assíntota: y = 0 (eixo x)</li>
</ul>

<p>
<b>g(x) = log₂ x:</b>
</p>
<ul class="org-ul">
<li>Passa por (1, 0), (2, 1), (4, 2)</li>
<li>Crescente</li>
<li>Assíntota: x = 0 (eixo y)</li>
</ul>

<p>
<b>Gráfico:</b>
</p>

<pre class="example" id="orgbf93e93">
  |    y=x (diagonal)
4 |   /    •2^x
2 | •/   •
1 |•/──•─────
  |/ •log₂x
  |•____________
    1  2  4
</pre>

<p>
<b>Simetria:</b> Pontos (a, b) em f correspondem a (b, a) em g.
</p>
</div>
</div>
</div>

<div id="outline-container-org42db8b7" class="outline-4">
<h4 id="org42db8b7"><span class="section-number-4">8.1.5.</span> Equações Envolvendo Ambas</h4>
<div class="outline-text-4" id="text-8-1-5">
</div>
<div id="outline-container-org3df829d" class="outline-5">
<h5 id="org3df829d"><span class="section-number-5">8.1.5.1.</span> Tipo 1: a^x = k → Usar log</h5>
<div class="outline-text-5" id="text-8-1-5-1">
<p>
<b>Exemplo:</b> 2^x = 5
</p>

<p>
*Método 1
</p>
<ul class="org-ul">
<li>Logaritmo decimal:*</li>
</ul>

<pre class="example" id="orgab15425">
log(2^x) = log 5
x log 2 = log 5
x = (log 5)/(log 2)
x ≈ 0,699/0,301 ≈ 2,32
</pre>

<p>
*Método 2
</p>
<ul class="org-ul">
<li>Logaritmo na base adequada:*</li>
</ul>

<pre class="example" id="orgabece40">
log₂(2^x) = log₂ 5
x = log₂ 5
</pre>
</div>
</div>

<div id="outline-container-org31df059" class="outline-5">
<h5 id="org31df059"><span class="section-number-5">8.1.5.2.</span> Tipo 2: log_a x = k → Usar exponencial</h5>
<div class="outline-text-5" id="text-8-1-5-2">
<p>
<b>Exemplo:</b> log₃ x = 4
</p>

<pre class="example" id="org02cf8c7">
3⁴ = x
x = 81
</pre>
</div>
</div>

<div id="outline-container-orga8e1d83" class="outline-5">
<h5 id="orga8e1d83"><span class="section-number-5">8.1.5.3.</span> Tipo 3: Mistas</h5>
<div class="outline-text-5" id="text-8-1-5-3">
<p>
<b>Exemplo:</b> 2^x = log₂ 16
</p>

<p>
<b>Resolver log₂ 16 primeiro:</b> log₂ 16 = log₂ (2⁴) = 4
</p>

<p>
<b>Então:</b> 2^x = 4 = 2² x = 2
</p>
</div>
</div>
</div>

<div id="outline-container-org91e51a4" class="outline-4">
<h4 id="org91e51a4"><span class="section-number-4">8.1.6.</span> Mudança de Base: Aplicações</h4>
<div class="outline-text-4" id="text-8-1-6">
<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org09308cf">
log_a b = (log_c b)/(log_c a)
</pre>

<p>
<b>Uso prático:</b> Calcular logaritmos em bases diferentes de 10 ou e.
</p>

<p>
<b>Exemplo:</b> Calcular log₅ 20
</p>

<pre class="example" id="org68ec2ca">
log₅ 20 = (log 20)/(log 5)
        ≈ 1,301/0,699
        ≈ 1,86
</pre>

<p>
<b>Ou usando ln:</b>
</p>

<pre class="example" id="org73cbf7e">
log₅ 20 = (ln 20)/(ln 5)
        ≈ 2,996/1,609
        ≈ 1,86
</pre>
</div>
</div>

<div id="outline-container-org6bf176a" class="outline-4">
<h4 id="org6bf176a"><span class="section-number-4">8.1.7.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-8-1-7">
</div>
<div id="outline-container-org0a5ea78" class="outline-5">
<h5 id="org0a5ea78"><span class="section-number-5">8.1.7.1.</span> Problema 1: Crescimento Exponencial</h5>
<div class="outline-text-5" id="text-8-1-7-1">
<p>
Uma população de 1000 bactérias dobra a cada hora. Quando atinge 10.000?
</p>

<p>
<b>Modelo:</b> P(t) = 1000 · 2^t
</p>

<p>
<b>Resolver:</b> 1000 · 2^t = 10000 2^t = 10 t = log₂ 10 t = (log 10)/(log 2) = 1/0,301 ≈ 3,32 horas
</p>

<p>
<i>[Ver resposta 46 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3e7d060" class="outline-5">
<h5 id="org3e7d060"><span class="section-number-5">8.1.7.2.</span> Problema 2: Decaimento Radioativo</h5>
<div class="outline-text-5" id="text-8-1-7-2">
<p>
Substância com meia-vida de 5 anos. Tempo para restar 10% da massa inicial?
</p>

<p>
<b>Modelo:</b> M(t) = M₀ · (1/2)^(t/5)
</p>

<p>
<b>Resolver:</b> (1/2)^(t/5) = 0,1
</p>

<p>
<b>Aplicar log:</b> log[(1/2)^(t/5)] = log 0,1 (t/5) log(1/2) = log 0,1 (t/5) × (-0,301) = -1 t/5 = 1/0,301 ≈ 3,32 t ≈ 16,6 anos
</p>
</div>
</div>

<div id="outline-container-org89964d3" class="outline-5">
<h5 id="org89964d3"><span class="section-number-5">8.1.7.3.</span> Problema 3: Juros Compostos</h5>
<div class="outline-text-5" id="text-8-1-7-3">
<p>
Capital de R$ 2000 a 8% ao ano. Quando duplica?
</p>

<p>
<b>Modelo:</b> M = 2000(1,08)^t
</p>

<p>
<b>Resolver:</b> 2000(1,08)^t = 4000 1,08^t = 2 t = log₁.₀₈ 2 t = (log 2)/(log 1,08) t ≈ 0,301/0,0334 ≈ 9 anos
</p>
</div>
</div>
</div>

<div id="outline-container-org9f404b7" class="outline-4">
<h4 id="org9f404b7"><span class="section-number-4">8.1.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-8-1-8">
</div>
<div id="outline-container-orgff0a710" class="outline-5">
<h5 id="orgff0a710"><span class="section-number-5">8.1.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-8-1-8-1">
<p>
Resolva: 3^x = 20
</p>

<p>
<b>Solução:</b> x = log₃ 20 = (log 20)/(log 3) ≈ 1,301/0,477 ≈ 2,73
</p>

<p>
<i>[Ver resposta 47 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgaa00071" class="outline-5">
<h5 id="orgaa00071"><span class="section-number-5">8.1.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-8-1-8-2">
<p>
Se log₂ x = 5, qual o valor de x?
</p>

<p>
<b>Solução:</b> 2⁵ = x x = 32
</p>

<p>
<i>[Ver resposta 48 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org4c234b5" class="outline-5">
<h5 id="org4c234b5"><span class="section-number-5">8.1.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-8-1-8-3">
<p>
Simplifique: 5^(log₅ 7)
</p>

<p>
<b>Solução:</b> Propriedade: a^(log_a b) = b
</p>

<p>
5^(log₅ 7) = 7
</p>

<p>
<i>[Ver resposta 49 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org04feb51" class="outline-5">
<h5 id="org04feb51"><span class="section-number-5">8.1.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-8-1-8-4">
<p>
Calcule: log₂ (2^(3x)) quando x = 2
</p>

<p>
<b>Solução:</b> log₂ (2^(3x)) = 3x = 3 × 2 = 6
</p>

<p>
<i>[Ver resposta 50 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgb8c9a6b" class="outline-4">
<h4 id="orgb8c9a6b"><span class="section-number-4">8.1.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-8-1-9">
<ol class="org-ol">
<li><b>a^(log_a b) = b</b> (propriedade inversa)</li>
<li><b>log_a (a^x) = x</b> (propriedade inversa)</li>
<li><b>Simetria:</b> gráficos refletem em y = x</li>
<li><b>Equação a^x = k:</b> aplicar log</li>
<li><b>Equação log x = k:</b> passar para exponencial</li>
<li><b>Mudança de base:</b> log_a b = (log b)/(log a)</li>
<li><b>Domínio exp:</b> ℝ; <b>Imagem exp:</b> (0, +∞)</li>
<li><b>Domínio log:</b> (0, +∞); <b>Imagem log:</b> ℝ</li>
</ol>
</div>
</div>

<div id="outline-container-org0e52350" class="outline-4">
<h4 id="org0e52350"><span class="section-number-4">8.1.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-8-1-10">
<p>
<b>Funções Inversas:</b>
</p>
<ul class="org-ul">
<li>f(x) = a^x ⟺ f⁻¹(x) = log_a x</li>
<li>Composição = identidade</li>
<li>Gráficos simétricos (y = x)</li>
</ul>

<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>a^(log_a x) = x</li>
<li>log_a (a^x) = x</li>
</ul>

<p>
<b>Domínio/Imagem:</b>
</p>
<ul class="org-ul">
<li>Exp: D = ℝ, Im = (0,+∞)</li>
<li>Log: D = (0,+∞), Im = ℝ</li>
</ul>

<p>
<b>Pontos Especiais:</b>
</p>
<ul class="org-ul">
<li>Exp: (0, 1)</li>
<li>Log: (1, 0)</li>
</ul>
</div>
</div>

<div id="outline-container-org885c6fc" class="outline-4">
<h4 id="org885c6fc"><span class="section-number-4">8.1.11.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-8-1-11">
<pre class="example" id="orgb54e6a5">
Relação Inversa:
f(x) = a^x  ⟺  f⁻¹(x) = log_a x

Composição:
a^(log_a x) = x  (x &gt; 0)
log_a (a^x) = x  (x ∈ ℝ)

Resolver a^x = k:
x = log_a k = (log k)/(log a)

Resolver log_a x = k:
x = a^k

Mudança de Base:
log_a b = (log b)/(log a)
</pre>
</div>
</div>

<div id="outline-container-org16c36d5" class="outline-4">
<h4 id="org16c36d5"><span class="section-number-4">8.1.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-8-1-12">
<pre class="example" id="orgbb2217e">
SIMETRIA:

    f(x)=a^x    y=x    g(x)=log_a x
         \\       /       /
          \\     /       /
           \\   /       /
         (0,1)/__(1,0)
             /
            /
           /

Pontos correspondentes:
Exp: (0,1), (1,a), (2,a²)
Log: (1,0), (a,1), (a²,2)

RELAÇÃO:
         Exponencial
              ↓
         y = a^x
              ↓
         Aplica log_a
              ↓
         x = log_a y
              ↓
         Logarítmica

PROPRIEDADES INVERSAS:
a^(log_a x) = x
log_a (a^x) = x
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>relação fundamental!)</li>
</ul>

<hr />
</div>
</div>
</div>
</div>

<div id="outline-container-orgc3edf75" class="outline-2">`;

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
