<script setup lang="ts">
import { ref } from "vue";

const code = "qui-46";
const title = "Química: Reações Químicas";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-3">
<ul class="org-ul">
<li>Química: Reações Químicas</li>
<li>Evidências, Equações e Balanceamento</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org40140e0" class="outline-4">
<h4 id="org40140e0"><span class="section-number-4">2.3.1.</span> O que é uma Reação Química?</h4>
<div class="outline-text-4" id="text-2-3-1">
<p>
<b>Reação química:</b> processo onde substâncias iniciais (<b>reagentes</b>) se transformam em novas substâncias (<b>produtos</b>).
</p>

<p>
<b>Representação:</b>
</p>

<pre class="example" id="org451faad">
Reagentes → Produtos
</pre>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Rearranjo de átomos:</b> átomos não são criados ou destruídos (Lei de Lavoisier)</li>
<li><b>Quebra e formação de ligações</b></li>
<li><b>Mudança nas propriedades</b> das substâncias</li>
<li><b>Energia envolvida</b> (absorção ou liberação)</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orge7cb0f2">
2 H₂ + O₂ → 2 H₂O
hidrogênio + oxigênio → água
</pre>
</div>
</div>

<div id="outline-container-org1aaebdb" class="outline-4">
<h4 id="org1aaebdb"><span class="section-number-4">2.3.2.</span> Evidências de uma Reação Química</h4>
<div class="outline-text-4" id="text-2-3-2">
<p>
<b>Como saber se ocorreu uma reação?</b>
</p>

<p>
<b>1. Mudança de cor</b>
</p>
<ul class="org-ul">
<li>Exemplo: ferro enferruja (cinza → marrom-avermelhado)</li>
<li>Exemplo: frutas oxidam e escurecem</li>
</ul>

<p>
<b>2. Liberação de gás (efervescência)</b>
</p>
<ul class="org-ul">
<li>Exemplo: bicarbonato de sódio + vinagre → CO₂</li>
<li>Exemplo: comprimido efervescente</li>
</ul>

<p>
<b>3. Formação de precipitado (sólido)</b>
</p>
<ul class="org-ul">
<li>Quando dois líquidos incolores formam sólido colorido</li>
<li>Exemplo: AgNO₃ + NaCl → AgCl (precipitado branco)</li>
</ul>

<p>
<b>4. Variação de temperatura</b>
</p>
<ul class="org-ul">
<li><b>Exotérmica:</b> libera calor (queima de combustíveis)</li>
<li><b>Endotérmica:</b> absorve calor (gelo químico)</li>
</ul>

<p>
<b>5. Liberação de luz</b>
</p>
<ul class="org-ul">
<li>Exemplo: combustão, fogos de artifício</li>
<li>Exemplo: vaga-lumes (bioluminescência)</li>
</ul>

<p>
<b>6. Mudança de odor</b>
</p>
<ul class="org-ul">
<li>Exemplo: decomposição de alimentos</li>
</ul>
</div>
</div>

<div id="outline-container-orgfdc2d6c" class="outline-4">
<h4 id="orgfdc2d6c"><span class="section-number-4">2.3.3.</span> Equação Química</h4>
<div class="outline-text-4" id="text-2-3-3">
<p>
<b>Equação química:</b> representação simbólica de uma reação.
</p>

<p>
<b>Componentes:</b>
</p>

<pre class="example" id="org256e0eb">
Reagentes → Produtos

Coeficientes + Fórmulas + Estados físicos
</pre>

<p>
<b>Estados físicos:</b>
</p>
<ul class="org-ul">
<li><b>(s)</b> = sólido (solid)</li>
<li><b>(l)</b> = líquido (liquid)</li>
<li><b>(g)</b> = gás (gas)</li>
<li><b>(aq)</b> = aquoso (aqueous, dissolvido em água)</li>
</ul>

<p>
<b>Exemplo completo:</b>
</p>

<pre class="example" id="orgab14479">
2 H₂(g) + O₂(g) → 2 H₂O(l)
</pre>
</div>
</div>

<div id="outline-container-org21ccc52" class="outline-4">
<h4 id="org21ccc52"><span class="section-number-4">2.3.4.</span> Lei de Lavoisier (Conservação das Massas)</h4>
<div class="outline-text-4" id="text-2-3-4">
<p>
<b>“Na natureza, nada se cria, nada se perde, tudo se transforma.”</b>
</p>

<p>
<b>Consequência:</b>
</p>
<ul class="org-ul">
<li><b>Número de átomos de cada elemento</b> nos reagentes = número nos produtos</li>
<li><b>Massa total dos reagentes</b> = massa total dos produtos</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org276edce">
C + O₂ → CO₂
12g + 32g → 44g
</pre>
</div>
</div>

<div id="outline-container-org354a085" class="outline-4">
<h4 id="org354a085"><span class="section-number-4">2.3.5.</span> Balanceamento de Equações Químicas</h4>
<div class="outline-text-4" id="text-2-3-5">
<p>
<b>Balancear:</b> ajustar os <b>coeficientes</b> para igualar o número de átomos de cada elemento nos dois lados.
</p>

<p>
<b>Regras:</b> 1. <b>Nunca mude os índices</b> das fórmulas (H₂O sempre será H₂O!) 2. <b>Ajuste apenas os coeficientes</b> (números antes das fórmulas) 3. <b>Use números inteiros</b> menores possíveis 4. <b>Comece pelo elemento mais complexo</b> 5. <b>Deixe H e O por último</b> (geralmente)
</p>

<p>
<b>Método prático:</b>
</p>

<p>
<b>Passo 1:</b> Escreva a equação não balanceada <b>Passo 2:</b> Conte os átomos de cada elemento <b>Passo 3:</b> Ajuste os coeficientes <b>Passo 4:</b> Verifique
</p>
</div>
</div>

<div id="outline-container-org1a5d02e" class="outline-4">
<h4 id="org1a5d02e"><span class="section-number-4">2.3.6.</span> Exemplos de Balanceamento</h4>
<div class="outline-text-4" id="text-2-3-6">
</div>
<div id="outline-container-orgaa5d3de" class="outline-5">
<h5 id="orgaa5d3de"><span class="section-number-5">2.3.6.1.</span> Exemplo 1: Combustão do metano</h5>
<div class="outline-text-5" id="text-2-3-6-1">
<pre class="example" id="org8b8dc06">
CH₄ + O₂ → CO₂ + H₂O  (não balanceada)
</pre>

<p>
<b>Contando átomos:</b>
</p>
<ul class="org-ul">
<li>Reagentes: C=1, H=4, O=2</li>
<li>Produtos: C=1, H=2, O=3</li>
</ul>

<p>
<b>Balanceando H:</b>
</p>

<pre class="example" id="orgdb58a21">
CH₄ + O₂ → CO₂ + 2 H₂O
</pre>

<p>
Agora: H=4 nos dois lados
</p>

<p>
<b>Balanceando O:</b> Produtos têm: 2 (do CO₂) + 2 (das 2 H₂O) = 4 oxigênios Reagentes precisam de 4 O → 2 O₂
</p>

<p>
<b>Equação balanceada:</b>
</p>

<pre class="example" id="org48a6bca">
CH₄ + 2 O₂ → CO₂ + 2 H₂O
</pre>

<p>
<b>Verificação:</b>
</p>
<ul class="org-ul">
<li>C: 1 = 1 ✓</li>
<li>H: 4 = 4 ✓</li>
<li>O: 4 = 4 ✓</li>
</ul>
</div>
</div>

<div id="outline-container-org7282bc8" class="outline-5">
<h5 id="org7282bc8"><span class="section-number-5">2.3.6.2.</span> Exemplo 2: Formação da água</h5>
<div class="outline-text-5" id="text-2-3-6-2">
<pre class="example" id="org5b018e4">
H₂ + O₂ → H₂O  (não balanceada)
</pre>

<p>
<b>Balanceando:</b>
</p>

<pre class="example" id="org6b42142">
2 H₂ + O₂ → 2 H₂O
</pre>

<p>
<b>Verificação:</b>
</p>
<ul class="org-ul">
<li>H: 4 = 4 ✓</li>
<li>O: 2 = 2 ✓</li>
</ul>
</div>
</div>

<div id="outline-container-org2aec2d2" class="outline-5">
<h5 id="org2aec2d2"><span class="section-number-5">2.3.6.3.</span> Exemplo 3: Fotossíntese</h5>
<div class="outline-text-5" id="text-2-3-6-3">
<pre class="example" id="orgfb334c4">
CO₂ + H₂O → C₆H₁₂O₆ + O₂  (não balanceada)
</pre>

<p>
<b>Balanceando carbono:</b>
</p>

<pre class="example" id="org7f9bc76">
6 CO₂ + H₂O → C₆H₁₂O₆ + O₂
</pre>

<p>
<b>Balanceando hidrogênio:</b>
</p>

<pre class="example" id="orged0ff9b">
6 CO₂ + 6 H₂O → C₆H₁₂O₆ + O₂
</pre>

<p>
<b>Balanceando oxigênio:</b> Reagentes: 6×2 + 6×1 = 18 O Produtos: 6 (na glicose) + ? (no O₂) 18 = 6 + ? ? = 12 → 6 O₂
</p>

<p>
<b>Equação balanceada:</b>
</p>

<pre class="example" id="orgb95f157">
6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂
</pre>
</div>
</div>
</div>

<div id="outline-container-org7df6825" class="outline-4">
<h4 id="org7df6825"><span class="section-number-4">2.3.7.</span> Tipos de Reações Químicas</h4>
<div class="outline-text-4" id="text-2-3-7">
<p>
<b>1. Síntese (Adição)</b>
</p>

<pre class="example" id="org307c6ed">
A + B → AB
</pre>

<p>
Exemplo: 2 H₂ + O₂ → 2 H₂O
</p>

<p>
<b>2. Decomposição (Análise)</b>
</p>

<pre class="example" id="orga9fcf00">
AB → A + B
</pre>

<p>
Exemplo: 2 H₂O → 2 H₂ + O₂ (eletrólise)
</p>

<p>
<b>3. Simples Troca (Deslocamento)</b>
</p>

<pre class="example" id="org32853b8">
A + BC → AC + B
</pre>

<p>
Exemplo: Zn + 2 HCl → ZnCl₂ + H₂
</p>

<p>
<b>4. Dupla Troca</b>
</p>

<pre class="example" id="org9edaeb8">
AB + CD → AD + CB
</pre>

<p>
Exemplo: NaCl + AgNO₃ → NaNO₃ + AgCl
</p>

<p>
<b>5. Combustão</b>
</p>

<pre class="example" id="org5c5e2cb">
Combustível + O₂ → CO₂ + H₂O + energia
</pre>

<p>
Exemplo: CH₄ + 2 O₂ → CO₂ + 2 H₂O
</p>
</div>
</div>

<div id="outline-container-orgb8a6f4a" class="outline-4">
<h4 id="orgb8a6f4a"><span class="section-number-4">2.3.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-3-8">
</div>
<div id="outline-container-orgd1cbe4d" class="outline-5">
<h5 id="orgd1cbe4d"><span class="section-number-5">2.3.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-3-8-1">
<p>
Balanceie: Fe + O₂ → Fe₂O₃
</p>

<p>
<b>Solução:</b> Fe: 2 nos produtos, precisa de 2 nos reagentes O: 3 nos produtos, mas O₂ vem em pares
</p>

<p>
Múltiplo comum: 6 oxigênios
</p>

<pre class="example" id="org410977e">
4 Fe + 3 O₂ → 2 Fe₂O₃
</pre>

<p>
<b>Verificação:</b>
</p>
<ul class="org-ul">
<li>Fe: 4 = 4 ✓</li>
<li>O: 6 = 6 ✓</li>
</ul>

<p>
<i>[Ver resposta 11 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7543f58" class="outline-5">
<h5 id="org7543f58"><span class="section-number-5">2.3.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-3-8-2">
<p>
Balanceie: Al + HCl → AlCl₃ + H₂
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org1a92640">
2 Al + 6 HCl → 2 AlCl₃ + 3 H₂
</pre>

<p>
<b>Verificação:</b>
</p>
<ul class="org-ul">
<li>Al: 2 = 2 ✓</li>
<li>H: 6 = 6 ✓</li>
<li>Cl: 6 = 6 ✓</li>
</ul>

<p>
<i>[Ver resposta 12 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org52ed706" class="outline-5">
<h5 id="org52ed706"><span class="section-number-5">2.3.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-3-8-3">
<p>
(UFMG) Qual evidência indica que houve reação química quando se mistura bicarbonato de sódio com vinagre?
</p>

<p>
<b>Solução:</b> Ocorre efervescência (liberação de gás CO₂), que é uma evidência de reação química.
</p>

<p>
<i>[Ver resposta 13 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org0f160c1" class="outline-5">
<h5 id="org0f160c1"><span class="section-number-5">2.3.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-3-8-4">
<p>
Balanceie: C₃H₈ + O₂ → CO₂ + H₂O
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orga59a502">
C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O
</pre>

<p>
<b>Passo a passo:</b>
</p>
<ul class="org-ul">
<li>C: 3 → 3 CO₂</li>
<li>H: 8 → 4 H₂O</li>
<li>O: (3×2) + (4×1) = 10 → 5 O₂</li>
</ul>

<p>
<i>[Ver resposta 14 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org237b856" class="outline-5">
<h5 id="org237b856"><span class="section-number-5">2.3.8.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-3-8-5">
<p>
Classifique: 2 HgO → 2 Hg + O₂
</p>

<p>
<b>Solução:</b> Uma substância composta (HgO) se decompõe em duas substâncias simples (Hg e O₂).
</p>

<p>
<i>[Ver resposta 15 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org77d31be" class="outline-4">
<h4 id="org77d31be"><span class="section-number-4">2.3.9.</span> Reações no Cotidiano</h4>
<div class="outline-text-4" id="text-2-3-9">
<p>
<b>1. Respiração celular:</b>
</p>

<pre class="example" id="org7df156b">
C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + energia
</pre>

<p>
<b>2. Fotossíntese:</b>
</p>

<pre class="example" id="orge98c494">
6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂
(luz solar)
</pre>

<p>
<b>3. Combustão de gasolina:</b>
</p>

<pre class="example" id="org445b223">
2 C₈H₁₈ + 25 O₂ → 16 CO₂ + 18 H₂O
</pre>

<p>
<b>4. Ferrugem:</b>
</p>

<pre class="example" id="org31851b9">
4 Fe + 3 O₂ → 2 Fe₂O₃
</pre>

<p>
<b>5. Digestão:</b> Quebra de proteínas, carboidratos, lipídios
</p>
</div>
</div>

<div id="outline-container-org50c90a9" class="outline-4">
<h4 id="org50c90a9"><span class="section-number-4">2.3.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-3-10">
<ol class="org-ol">
<li><b>Balanceamento:</b> ajustar apenas coeficientes, nunca índices</li>
<li><b>Lei de Lavoisier:</b> massa se conserva</li>
<li><b>Evidências:</b> cor, gás, precipitado, temperatura, luz</li>
<li><b>Ordem de balanceamento:</b> elementos complexos primeiro, H e O por último</li>
<li><b>Verificação:</b> sempre contar átomos ao final</li>
<li><b>Estados físicos:</b> (s), (l), (g), (aq)</li>
<li><b>Coeficientes:</b> usar menores inteiros possíveis</li>
</ol>
</div>
</div>

<div id="outline-container-org25547f7" class="outline-4">
<h4 id="org25547f7"><span class="section-number-4">2.3.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-3-11">
<p>
<b>Reação Química:</b>
</p>
<ul class="org-ul">
<li>Transformação de substâncias</li>
<li>Rearranjo de átomos</li>
<li>Conservação da massa (Lavoisier)</li>
</ul>

<p>
<b>Evidências:</b>
</p>
<ul class="org-ul">
<li>Mudança de cor, odor</li>
<li>Gás, precipitado</li>
<li>Variação de temperatura, luz</li>
</ul>

<p>
<b>Balanceamento:</b>
</p>
<ul class="org-ul">
<li>Igualar número de átomos</li>
<li>Ajustar coeficientes (não índices)</li>
<li>Usar menores inteiros</li>
</ul>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li>Síntese: A + B → AB</li>
<li>Decomposição: AB → A + B</li>
<li>Simples troca: A + BC → AC + B</li>
<li>Dupla troca: AB + CD → AD + CB</li>
<li>Combustão: combustível + O₂ → CO₂ + H₂O</li>
</ul>
</div>
</div>

<div id="outline-container-orge9a87bd" class="outline-4">
<h4 id="orge9a87bd"><span class="section-number-4">2.3.12.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-3-12">
<pre class="example" id="org2f6ef4d">
Lei de Lavoisier (Conservação das Massas):
m_reagentes = m_produtos

Equação Química:
Reagentes → Produtos
(coeficientes) Fórmulas (estados físicos)

Tipos de Reações:
Síntese:        A + B → AB
Decomposição:   AB → A + B
Simples troca:  A + BC → AC + B
Dupla troca:    AB + CD → AD + CB
Combustão:      CₓHᵧ + O₂ → CO₂ + H₂O

Estados Físicos:
(s) = sólido
(l) = líquido
(g) = gás
(aq) = aquoso
</pre>
</div>
</div>

<div id="outline-container-orgfdfc708" class="outline-4">
<h4 id="orgfdfc708"><span class="section-number-4">2.3.13.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-2-3-13">
<pre class="example" id="orgf3c1479">
REAÇÃO QUÍMICA:

Reagentes  →  Produtos
   A + B   →    AB

EVIDÊNCIAS:
🎨 Mudança de cor
💨 Liberação de gás
⬇️ Formação de precipitado
🌡️ Variação de temperatura
💡 Liberação de luz

BALANCEAMENTO:

   CH₄  +  O₂  →  CO₂  +  H₂O
    ↓      ↓      ↓       ↓
   1 CH₄ + 2 O₂ → 1 CO₂ + 2 H₂O
   
   C: 1 = 1 ✓
   H: 4 = 4 ✓
   O: 4 = 4 ✓

TIPOS:
Síntese:    ⚫ + ⚫ → ⚫⚫
Decomposição: ⚫⚫ → ⚫ + ⚫
Simples troca: ⚫ + ⚫⚪ → ⚫⚪ + ⚫
Dupla troca: ⚫⚪ + ⚫🔴 → ⚫🔴 + ⚫⚪
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para estequiometria)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org4675c6d" class="outline-3">`;

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
