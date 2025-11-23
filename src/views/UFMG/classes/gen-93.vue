<script setup lang="ts">
import { ref } from "vue";

const code = "gen-93";
const title = "Geral: Aula 93";
const subject = "geral";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-6-5">
<ul class="org-ul">
<li>Flash Review Biologia e Português</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-orge75a3a8" class="outline-4">
<h4 id="orge75a3a8"><span class="section-number-4">6.5.1.</span> Objetivo</h4>
<div class="outline-text-4" id="text-6-5-1">
<p>
Última revisão de Biologia e Português. Você está pronto!
</p>

<hr />
</div>
</div>

<div id="outline-container-orge91579e" class="outline-4">
<h4 id="orge91579e"><span class="section-number-4">6.5.2.</span> ⚡ BIOLOGIA</h4>
<div class="outline-text-4" id="text-6-5-2">
<ul class="org-ul">
<li>GENÉTICA</li>
</ul>
<p>
<b>Leis de Mendel:</b>
</p>

<pre class="example" id="orga8c5da4">
1ª Lei: Aa × Aa → 3:1
2ª Lei: AaBb × AaBb → 9:3:3:1
</pre>

<p>
<b>DNA:</b>
</p>

<pre class="example" id="org28a3bdd">
A-T (adenina-timina)
C-G (citosina-guanina)
</pre>

<p>
<b>Genótipo vs Fenótipo:</b>
</p>

<pre class="example" id="orgd05e802">
Genótipo: genes (AA, Aa, aa)
Fenótipo: característica observável
</pre>

<p>
<b>Grupos Sanguíneos:</b>
</p>

<pre class="example" id="org54c156d">
A: IᴬIᴬ ou Iᴬi
B: IᴮIᴮ ou Iᴮi
AB: IᴬIᴮ
O: ii
</pre>

<p>
<b>Célula:</b>
</p>

<pre class="example" id="org80bf96c">
Mitocôndria: respiração (ATP)
Cloroplasto: fotossíntese (só plantas)
</pre>

<p>
<b>Processos:</b>
</p>

<pre class="example" id="orge876ef5">
Respiração: Glicose + O₂ → CO₂ + H₂O + ATP
Fotossíntese: CO₂ + H₂O + luz → Glicose + O₂
</pre>

<hr />
</div>
</div>

<div id="outline-container-org0289095" class="outline-4">
<h4 id="org0289095"><span class="section-number-4">6.5.3.</span> ⚡ PORTUGUÊS</h4>
<div class="outline-text-4" id="text-6-5-3">
<ul class="org-ul">
<li>INTERPRETAÇÃO</li>
</ul>
<p>
<b>Estratégias:</b>
</p>

<pre class="example" id="org2462633">
1. Ler enunciado ANTES do texto
2. Identificar tema central
3. Basear-se APENAS no texto
4. Eliminar alternativas absurdas
</pre>

<p>
<b>Armadilhas:</b>
</p>

<pre class="example" id="org97de93c">
✗ Extrapolação (ir além do texto)
✗ Redução (detalhe como ideia principal)
✗ Distorção (mudar sentido)
</pre>

<p>
<b>Concordância:</b>
</p>

<pre class="example" id="org292e7dc">
Sujeito simples: verbo concorda
"O aluno estuda"

Sujeito composto (antes): verbo plural
"Maria e João estudam"
</pre>

<p>
<b>Crase:</b>
</p>

<pre class="example" id="orgbed65db">
a + a = à
Macete: trocar por "ao"
</pre>

<hr />

<p>
<b>Você está afiado! Confiança!</b> ✅
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org082b995" class="outline-3">`;

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
