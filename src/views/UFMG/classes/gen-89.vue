<script setup lang="ts">
import { ref } from "vue";

const code = "gen-89";
const title = "Sinais: *";
const subject = "sinais";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-1">
<ul class="org-ul">
<li>Flash Review Matemática</li>
<li>45min</li>
</ul>
</div>
<div id="outline-container-orga2df80f" class="outline-4">
<h4 id="orga2df80f"><span class="section-number-4">6.1.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-6-1-1">
<p>
Revisão ultra-rápida dos conceitos MAIS importantes de Matemática. Leia, relembre, confie!
</p>

<hr />
</div>
</div>

<div id="outline-container-orgcf09034" class="outline-4">
<h4 id="orgcf09034"><span class="section-number-4">6.1.2.</span> ⚡ TOP 10 FÓRMULAS DE MATEMÁTICA</h4>
<div class="outline-text-4" id="text-6-1-2">
<ol class="org-ol">
<li><b>Bhaskara</b></li>
</ol>

<pre class="example" id="orgb90eca7">
Δ = b² − 4ac
x = (−b ± √Δ) / 2a
</pre>

<ol class="org-ol">
<li value="2"><b>Vértice da Parábola</b></li>
</ol>

<pre class="example" id="orgdae0a68">
xᵥ = −b/2a
yᵥ = −Δ/4a
</pre>

<ol class="org-ol">
<li value="3"><b>Pitágoras</b></li>
</ol>

<pre class="example" id="org2d869f5">
a² = b² + c²
</pre>

<ol class="org-ol">
<li value="4">*Trigonometria</li>
<li>Tabela*</li>
</ol>

<pre class="example" id="orga51373f">
sen 30° = 1/2
sen 45° = √2/2
sen 60° = √3/2

cos 30° = √3/2
cos 45° = √2/2
cos 60° = 1/2
</pre>

<ol class="org-ol">
<li value="5"><b>Área do Triângulo</b></li>
</ol>

<pre class="example" id="org89a38fd">
A = (b × h) / 2
</pre>

<ol class="org-ol">
<li value="6"><b>Área do Círculo</b></li>
</ol>

<pre class="example" id="orgfb28169">
A = πr²
C = 2πr
</pre>

<ol class="org-ol">
<li value="7">*Logaritmo</li>
<li>Propriedades*</li>
</ol>

<pre class="example" id="org26ef93d">
logₐ (bc) = logₐ b + logₐ c
logₐ (b/c) = logₐ b − logₐ c
logₐ bⁿ = n · logₐ b
logₐ 1 = 0
logₐ a = 1
</pre>

<ol class="org-ol">
<li value="8"><b>Exponencial</b></li>
</ol>

<pre class="example" id="org1563328">
aˣ · aʸ = aˣ⁺ʸ
aˣ / aʸ = aˣ⁻ʸ
(aˣ)ʸ = aˣʸ
</pre>

<ol class="org-ol">
<li value="9"><b>Função Afim</b></li>
</ol>

<pre class="example" id="org3260c76">
f(x) = ax + b
Raiz: x = −b/a
</pre>

<ol class="org-ol">
<li value="10"><b>Conjuntos</b></li>
</ol>

<pre class="example" id="org53ee69c">
n(A ∪ B) = n(A) + n(B) − n(A ∩ B)
</pre>

<hr />
</div>
</div>

<div id="outline-container-org65919e6" class="outline-4">
<h4 id="org65919e6"><span class="section-number-4">6.1.3.</span> 🎯 LEMBRETE RÁPIDO</h4>
<div class="outline-text-4" id="text-6-1-3">
<p>
*Função Quadrática
</p>
<ul class="org-ul">
<li>Sinais:*</li>
</ul>

<pre class="example" id="org0276591">
a &gt; 0, Δ &gt; 0:
- Positiva: fora das raízes
- Negativa: entre as raízes
</pre>

<p>
<b>Ternas Pitagóricas:</b>
</p>

<pre class="example" id="org89c2155">
(3, 4, 5)
(5, 12, 13)
</pre>

<p>
<b>Relação Trigonométrica:</b>
</p>

<pre class="example" id="org5b7d249">
sen² α + cos² α = 1
tg α = sen α / cos α
</pre>

<hr />

<p>
<b>Você sabe isso! Confie!</b> ✅
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org683599e" class="outline-3">`;

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
