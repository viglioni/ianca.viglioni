<script setup lang="ts">
import { ref } from "vue";

const code = "mat-64";
const title = "Matemática: Revisão Final";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-1">
<ul class="org-ul">
<li>Matemática: Revisão Final</li>
<li>Conjuntos, MMC/MDC, Razão e Proporção</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orge5c85bd" class="outline-4">
<h4 id="orge5c85bd"><span class="section-number-4">2.1.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-2-1-1">
<p>
Consolidar os conceitos fundamentais estudados na Semana 1, essenciais para toda a Matemática.
</p>
</div>
</div>

<div id="outline-container-org408da2c" class="outline-4">
<h4 id="org408da2c"><span class="section-number-4">2.1.2.</span> 1. Teoria dos Conjuntos</h4>
<div class="outline-text-4" id="text-2-1-2">
<ul class="org-ul">
<li>Revisão Rápida</li>
</ul>
<p>
<b>Conjunto:</b> coleção de elementos bem definidos
</p>

<p>
<b>Notações:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3, 4} → conjunto por extensão</li>
<li>B = {x ∈ ℕ | x &lt; 5} → conjunto por compreensão</li>
</ul>

<p>
<b>Conjuntos especiais:</b>
</p>

<pre class="example" id="org75b231f">
∅ ou {} = conjunto vazio
ℕ = {0, 1, 2, 3, ...} = naturais
ℤ = {..., -2, -1, 0, 1, 2, ...} = inteiros
ℚ = {a/b | a,b ∈ ℤ, b ≠ 0} = racionais
ℝ = todos os números reais
</pre>

<p>
<b>Relações:</b>
</p>
<ul class="org-ul">
<li>∈ (pertence): 3 ∈ {1, 2, 3}</li>
<li>⊂ (contido): {1, 2} ⊂ {1, 2, 3}</li>
<li>∪ (união): {1, 2} ∪ {2, 3} = {1, 2, 3}</li>
<li>∩ (interseção): {1, 2} ∩ {2, 3} = {2}</li>
<li>− (diferença): {1, 2, 3} − {2} = {1, 3}</li>
</ul>

<p>
<b>Número de elementos:</b>
</p>

<pre class="example" id="orgcc77589">
n(A ∪ B) = n(A) + n(B) − n(A ∩ B)
</pre>

<p>
<b>Exercício rápido:</b> Em uma turma, 30 alunos gostam de Matemática, 25 de Física, 10 de ambas. Quantos alunos há na turma?
</p>

<pre class="example" id="org1740b25">
n(M ∪ F) = n(M) + n(F) − n(M ∩ F)
n(M ∪ F) = 30 + 25 − 10 = 45 alunos
</pre>
</div>
</div>

<div id="outline-container-orgc7364fa" class="outline-4">
<h4 id="orgc7364fa"><span class="section-number-4">2.1.3.</span> 2. MMC e MDC</h4>
<div class="outline-text-4" id="text-2-1-3">
<ul class="org-ul">
<li>Revisão Rápida</li>
</ul>
<p>
<b>MDC (Máximo Divisor Comum):</b>
</p>
<ul class="org-ul">
<li>Maior número que divide todos</li>
<li>Método: fatoração ou divisões sucessivas</li>
<li><b>Números primos entre si:</b> MDC = 1</li>
</ul>

<p>
<b>Exemplo:</b> MDC(12, 18)
</p>

<pre class="example" id="org47cd8b4">
12 = 2² × 3
18 = 2 × 3²
MDC = 2 × 3 = 6
</pre>

<p>
<b>MMC (Mínimo Múltiplo Comum):</b>
</p>
<ul class="org-ul">
<li>Menor múltiplo comum a todos</li>
<li>Método: fatoração simultânea</li>
</ul>

<p>
<b>Exemplo:</b> MMC(12, 18)
</p>

<pre class="example" id="orgf1544d1">
12, 18 | 2
 6,  9 | 2
 3,  9 | 3
 1,  3 | 3
 1,  1

MMC = 2 × 2 × 3 × 3 = 36
</pre>

<p>
<b>Relação importante:</b>
</p>

<pre class="example" id="org26e451d">
MMC(a,b) × MDC(a,b) = a × b
</pre>

<p>
<b>Aplicações:</b>
</p>
<ul class="org-ul">
<li><b>MDC:</b> dividir em partes iguais (máximas)</li>
<li><b>MMC:</b> eventos que se repetem (próximo encontro)</li>
</ul>

<p>
<b>Exercício rápido:</b> Dois ônibus passam no mesmo ponto: um a cada 12 minutos, outro a cada 18 minutos. Se passaram juntos às 8h, quando passarão juntos novamente?
</p>

<pre class="example" id="org68099e1">
MMC(12, 18) = 36 minutos
8h + 36min = 8h36min
</pre>
</div>
</div>

<div id="outline-container-org5f6ef73" class="outline-4">
<h4 id="org5f6ef73"><span class="section-number-4">2.1.4.</span> 3. Razão e Proporção</h4>
<div class="outline-text-4" id="text-2-1-4">
<ul class="org-ul">
<li>Revisão Rápida</li>
</ul>
<p>
<b>Razão:</b>
</p>

<pre class="example" id="orgd5ac27b">
a/b (lê-se "a está para b")
</pre>

<p>
<b>Proporção:</b>
</p>

<pre class="example" id="org99928da">
a/b = c/d
</pre>

<p>
<b>Propriedade fundamental:</b>
</p>

<pre class="example" id="orgb32f79b">
a × d = b × c (produto dos extremos = produto dos meios)
</pre>

<p>
<b>Grandezas diretamente proporcionais:</b>
</p>
<ul class="org-ul">
<li>Uma aumenta → outra aumenta na mesma razão</li>
<li>Regra de três simples direta</li>
</ul>

<p>
<b>Exemplo:</b> 5 kg custam R$ 20. Quanto custam 8 kg?
</p>

<pre class="example" id="org234b2f2">
5 kg ─── R$ 20
8 kg ─── x

5/8 = 20/x
5x = 160
x = 32
</pre>

<p>
<b>Grandezas inversamente proporcionais:</b>
</p>
<ul class="org-ul">
<li>Uma aumenta → outra diminui</li>
<li>Regra de três simples inversa</li>
</ul>

<p>
<b>Exemplo:</b> 4 trabalhadores fazem um serviço em 6 dias. E 6 trabalhadores?
</p>

<pre class="example" id="org194287e">
Mais trabalhadores → menos dias (inversa)

4 trab ─── 6 dias
6 trab ─── x

Inverter uma razão:
6/4 = 6/x
6x = 24
x = 4 dias
</pre>

<p>
<b>Divisão proporcional:</b>
</p>

<p>
<b>Diretamente proporcional a a, b, c:</b>
</p>

<pre class="example" id="org0abc81f">
x/a = y/b = z/c = k
x = ka, y = kb, z = kc
</pre>

<p>
<b>Exemplo:</b> Dividir 120 em partes proporcionais a 2, 3, 5.
</p>

<pre class="example" id="orgc87cfd4">
x/2 = y/3 = z/5 = k
x + y + z = 120
2k + 3k + 5k = 120
10k = 120
k = 12

x = 2×12 = 24
y = 3×12 = 36
z = 5×12 = 60
</pre>
</div>
</div>

<div id="outline-container-org1d662c6" class="outline-4">
<h4 id="org1d662c6"><span class="section-number-4">2.1.5.</span> Questões de Fixação Rápida</h4>
<div class="outline-text-4" id="text-2-1-5">
</div>
<div id="outline-container-orgc733187" class="outline-5">
<h5 id="orgc733187"><span class="section-number-5">2.1.5.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-2-1-5-1">
<p>
Se A = {1, 2, 3}, B = {2, 3, 4}, calcule n(A ∪ B).
</p>

<p>
<i>[Ver resposta 1 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7171e20" class="outline-5">
<h5 id="org7171e20"><span class="section-number-5">2.1.5.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-2-1-5-2">
<p>
Calcule MDC(24, 36) e MMC(24, 36).
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org1985329">
24 = 2³ × 3
36 = 2² × 3²
MDC = 2² × 3 = 12
MMC = 2³ × 3² = 72
</pre>
</div>
</div>

<div id="outline-container-org9ef6a2d" class="outline-5">
<h5 id="org9ef6a2d"><span class="section-number-5">2.1.5.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-2-1-5-3">
<p>
Uma torneira enche um tanque em 6 horas. Outra em 4 horas. Juntas, em quanto tempo enchem?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgde0f50b">
Em 1h: primeira enche 1/6, segunda enche 1/4
Juntas: 1/6 + 1/4 = 2/12 + 3/12 = 5/12 por hora
Tempo total: 12/5 = 2,4 horas = 2h24min
</pre>
</div>
</div>
</div>

<div id="outline-container-orgf1bc007" class="outline-4">
<h4 id="orgf1bc007"><span class="section-number-4">2.1.6.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-1-6">
<pre class="example" id="orgcac60fa">
CONJUNTOS:
n(A ∪ B) = n(A) + n(B) − n(A ∩ B)

MMC e MDC:
MMC(a,b) × MDC(a,b) = a × b

PROPORÇÃO:
a/b = c/d → ad = bc

REGRA DE TRÊS:
Direta: grandezas na mesma direção
Inversa: grandezas em direções opostas

DIVISÃO PROPORCIONAL:
x/a = y/b = z/c = (x+y+z)/(a+b+c)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Fácil-Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (base de tudo!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org9514b3f" class="outline-3">`;

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
