<script setup lang="ts">
import { ref } from "vue";

const code = "qui-31";
const title = "Química: Ligações Químicas";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-2">
<ul class="org-ul">
<li>Química: Ligações Químicas</li>
<li>Parte 1 (Ligação Iônica)</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-org9eef5ec" class="outline-4">
<h4 id="org9eef5ec"><span class="section-number-4">2.2.1.</span> Introdução: Por que Átomos se Ligam?</h4>
<div class="outline-text-4" id="text-2-2-1">
<p>
A maioria dos átomos na natureza <b>não existe isolada</b>, mas <b>ligada</b> a outros átomos.
</p>

<p>
<b>Por quê?</b>
</p>
<ul class="org-ul">
<li>Átomos isolados geralmente são <b>instáveis</b></li>
<li>Ligações químicas levam à <b>estabilidade</b></li>
</ul>

<p>
<b>Regra do Octeto (ou Teoria do Octeto):</b> &gt; Átomos tendem a ganhar, perder ou compartilhar elétrons para adquirir <b>8 elétrons na camada de valência</b> (configuração de gás nobre).
</p>

<p>
<b>Exceções:</b>
</p>
<ul class="org-ul">
<li><b>Hélio (He):</b> estável com 2 elétrons (camada K completa)</li>
<li><b>Hidrogênio (H):</b> estável com 2 elétrons (dueto)</li>
<li>Alguns elementos do 3º período podem expandir octeto</li>
</ul>

<p>
<b>Gases Nobres:</b>
</p>
<ul class="org-ul">
<li>Já têm 8 elétrons na valência (He tem 2)</li>
<li>São <b>estáveis</b> e <b>inertes</b> (não fazem ligações facilmente)</li>
<li>Exemplos: He (2), Ne (2,8), Ar (2,8,8)</li>
</ul>
</div>
</div>

<div id="outline-container-orgff5c83e" class="outline-4">
<h4 id="orgff5c83e"><span class="section-number-4">2.2.2.</span> Tipos de Ligações Químicas</h4>
<div class="outline-text-4" id="text-2-2-2">
<p>
<b>Principais tipos:</b> 1. <b>Ligação Iônica</b> (ou eletrovalente) 2. <b>Ligação Covalente</b> (ou molecular) 3. <b>Ligação Metálica</b>
</p>

<p>
<b>Classificação depende:</b>
</p>
<ul class="org-ul">
<li>Tipo de átomo envolvido (metal, não-metal, semimetal)</li>
<li>Diferença de eletronegatividade</li>
</ul>
</div>
</div>

<div id="outline-container-org4eed269" class="outline-4">
<h4 id="org4eed269"><span class="section-number-4">2.2.3.</span> Ligação Iônica</h4>
<div class="outline-text-4" id="text-2-2-3">
<p>
<b>Definição:</b> Ligação entre <b>metal e não-metal</b> através da <b>transferência de elétrons</b>.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Metal <b>perde</b> elétrons → forma <b>cátion</b> (+)</li>
<li>Não-metal <b>ganha</b> elétrons → forma <b>ânion</b> (-)</li>
<li>Atração eletrostática entre íons de cargas opostas</li>
</ul>

<p>
<b>Condições:</b>
</p>
<ul class="org-ul">
<li>Grande diferença de eletronegatividade (ΔEN ≥ 1,7)</li>
<li>Metal (baixa EN) + Não-metal (alta EN)</li>
</ul>
</div>

<div id="outline-container-org1077a79" class="outline-5">
<h5 id="org1077a79"><span class="section-number-5">2.2.3.1.</span> Formação da Ligação Iônica</h5>
<div class="outline-text-5" id="text-2-2-3-1">
<p>
<b>Exemplo 1: Cloreto de Sódio (NaCl)</b>
</p>

<p>
<b>Sódio (Na, Z = 11):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 8, 1</li>
<li>1 elétron na valência</li>
<li>Tende a <b>perder 1 e⁻</b> → Na⁺ (2, 8)</li>
<li>estável</li>
</ul>

<p>
<b>Cloro (Cl, Z = 17):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 8, 7</li>
<li>7 elétrons na valência</li>
<li>Tende a <b>ganhar 1 e⁻</b> → Cl⁻ (2, 8, 8)</li>
<li>estável</li>
</ul>

<p>
<b>Ligação:</b>
</p>

<pre class="example" id="org10b6dd6">
Na → Na⁺ + e⁻  (perde)
Cl + e⁻ → Cl⁻  (ganha)

Na⁺ + Cl⁻ → NaCl
</pre>

<p>
<b>Resultado:</b> Cristal iônico de NaCl (sal de cozinha)
</p>

<p>
<b>Exemplo 2: Óxido de Magnésio (MgO)</b>
</p>

<p>
<b>Magnésio (Mg, Z = 12):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 8, 2</li>
<li>Perde 2 e⁻ → Mg²⁺ (2, 8)</li>
</ul>

<p>
<b>Oxigênio (O, Z = 8):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 6</li>
<li>Ganha 2 e⁻ → O²⁻ (2, 8)</li>
</ul>

<p>
<b>Ligação:</b>
</p>

<pre class="example" id="org649a668">
Mg → Mg²⁺ + 2e⁻
O + 2e⁻ → O²⁻

Mg²⁺ + O²⁻ → MgO
</pre>

<p>
<b>Exemplo 3: Cloreto de Cálcio (CaCl₂)</b>
</p>

<p>
<b>Cálcio (Ca, Z = 20):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 8, 8, 2</li>
<li>Perde 2 e⁻ → Ca²⁺</li>
</ul>

<p>
<b>Cloro (Cl, Z = 17):</b>
</p>
<ul class="org-ul">
<li>Ganha 1 e⁻ → Cl⁻</li>
</ul>

<p>
<b>Problema:</b> Ca perde 2 e⁻, mas cada Cl ganha apenas 1 e⁻!
</p>

<p>
<b>Solução:</b> <b>2 átomos de Cl</b> para 1 átomo de Ca
</p>

<pre class="example" id="org941bfb2">
Ca → Ca²⁺ + 2e⁻
2Cl + 2e⁻ → 2Cl⁻

Ca²⁺ + 2Cl⁻ → CaCl₂
</pre>

<p>
<b>Fórmula:</b> CaCl₂ (1 Ca para 2 Cl)
</p>
</div>
</div>
</div>

<div id="outline-container-org8c04d32" class="outline-4">
<h4 id="org8c04d32"><span class="section-number-4">2.2.4.</span> Propriedades dos Compostos Iônicos</h4>
<div class="outline-text-4" id="text-2-2-4">
<p>
<b>1. Estado físico:</b>
</p>
<ul class="org-ul">
<li><b>Sólidos</b> à temperatura ambiente</li>
<li>Cristais iônicos (arranjo ordenado de íons)</li>
</ul>

<p>
<b>2. Ponto de fusão e ebulição:</b>
</p>
<ul class="org-ul">
<li><b>Altos</b> (fortes atrações eletrostáticas)</li>
<li>Exemplo: NaCl funde a 801°C</li>
</ul>

<p>
<b>3. Condutividade elétrica:</b>
</p>
<ul class="org-ul">
<li><b>Sólidos:</b> NÃO conduzem (íons fixos no retículo)</li>
<li><b>Fundidos ou dissolvidos:</b> CONDUZEM (íons livres)</li>
</ul>

<p>
<b>4. Solubilidade:</b>
</p>
<ul class="org-ul">
<li>Geralmente <b>solúveis em água</b> (solvente polar)</li>
<li>Insolúveis em solventes apolares (gasolina, etc.)</li>
</ul>

<p>
<b>5. Dureza:</b>
</p>
<ul class="org-ul">
<li>Duros, mas <b>quebradiços</b> (fraturam facilmente)</li>
</ul>
</div>
</div>

<div id="outline-container-org617e0a7" class="outline-4">
<h4 id="org617e0a7"><span class="section-number-4">2.2.5.</span> Fórmula de Compostos Iônicos</h4>
<div class="outline-text-4" id="text-2-2-5">
<p>
<b>Regra:</b> Número total de cargas positivas = número total de cargas negativas
</p>

<p>
<b>Método prático (troca de valências):</b>
</p>

<p>
Cátion A^(m+) + Ânion B^(n-) → A_n B_m
</p>

<p>
<b>Exemplos:</b>
</p>

<ol class="org-ol">
<li><b>Al³⁺ + O²⁻</b>
<ul class="org-ul">
<li>Troca: Al₂O₃</li>
<li>Óxido de alumínio</li>
</ul></li>
<li><b>Fe³⁺ + S²⁻</b>
<ul class="org-ul">
<li>Troca: Fe₂S₃</li>
<li>Sulfeto de ferro III</li>
</ul></li>
<li><b>Na⁺ + SO₄²⁻</b>
<ul class="org-ul">
<li>Troca: Na₂SO₄</li>
<li>Sulfato de sódio</li>
</ul></li>
</ol>

<p>
<b>Simplificação:</b> Se houver divisor comum, simplifique.
</p>

<p>
Exemplo: Ca²⁺ + O²⁻ → Ca₂O₂ → <b>CaO</b> (simplificado)
</p>
</div>
</div>

<div id="outline-container-org05658e4" class="outline-4">
<h4 id="org05658e4"><span class="section-number-4">2.2.6.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-2-6">
</div>
<div id="outline-container-orge72bfc2" class="outline-5">
<h5 id="orge72bfc2"><span class="section-number-5">2.2.6.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-2-6-1">
<p>
O que acontece com os átomos de sódio (Na) e cloro (Cl) ao formarem NaCl?
</p>

<p>
<b>Resposta:</b>
</p>
<ul class="org-ul">
<li><b>Na (2,8,1):</b> perde 1 elétron → Na⁺ (2,8)</li>
<li>cátion</li>
<li><b>Cl (2,8,7):</b> ganha 1 elétron → Cl⁻ (2,8,8)</li>
<li>ânion</li>
<li>Formam ligação iônica por atração eletrostática entre Na⁺ e Cl⁻</li>
</ul>
</div>
</div>

<div id="outline-container-org5355f12" class="outline-5">
<h5 id="org5355f12"><span class="section-number-5">2.2.6.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-2-6-2">
<p>
Determine a fórmula do composto formado entre alumínio (Al³⁺) e oxigênio (O²⁻).
</p>

<p>
<b>Solução:</b> Troca de valências: Al³⁺ → índice 2 O²⁻ → índice 3
</p>

<p>
<b>Fórmula:</b> Al₂O₃
</p>

<p>
<i>[Ver resposta 8 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3150919" class="outline-5">
<h5 id="org3150919"><span class="section-number-5">2.2.6.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-2-6-3">
<p>
Por que o sal de cozinha (NaCl) conduz eletricidade quando dissolvido em água, mas não no estado sólido?
</p>

<p>
<b>Resposta:</b>
</p>
<ul class="org-ul">
<li><b>Sólido:</b> íons estão fixos no retículo cristalino, não podem se mover, NÃO conduzem</li>
<li><b>Dissolvido:</b> íons ficam livres na solução, podem se mover e transportar carga, CONDUZEM eletricidade</li>
</ul>
</div>
</div>

<div id="outline-container-orgd51ead6" class="outline-5">
<h5 id="orgd51ead6"><span class="section-number-5">2.2.6.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-2-6-4">
<p>
(UFMG) Qual o tipo de ligação entre magnésio (Mg) e cloro (Cl)?
</p>

<p>
<b>Resposta:</b> <b>Ligação iônica</b>.
</p>
<ul class="org-ul">
<li>Mg é metal (perde elétrons)</li>
<li>Cl é não-metal (ganha elétrons)</li>
<li>Grande diferença de eletronegatividade</li>
<li>Fórmula: MgCl₂</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orga672216" class="outline-4">
<h4 id="orga672216"><span class="section-number-4">2.2.7.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-2-7">
<ol class="org-ol">
<li><b>Ligação iônica:</b> metal + não-metal</li>
<li><b>Transferência</b> de elétrons (não compartilhamento)</li>
<li><b>Metal perde</b> → cátion (+)</li>
<li><b>Não-metal ganha</b> → ânion (-)</li>
<li><b>Propriedades:</b> sólidos, altos PF/PE, conduzem fundidos/dissolvidos</li>
<li><b>Fórmula:</b> total de cargas + = total de cargas -</li>
<li><b>Regra do octeto:</b> 8 elétrons na valência (estável)</li>
<li><b>Gases nobres:</b> já estáveis (8 e⁻)</li>
</ol>
</div>
</div>

<div id="outline-container-org992b435" class="outline-4">
<h4 id="org992b435"><span class="section-number-4">2.2.8.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-2-8">
<p>
<b>Ligação Iônica:</b>
</p>
<ul class="org-ul">
<li>Metal + Não-metal</li>
<li>Transferência de elétrons</li>
<li>Formação de íons</li>
<li>Atração eletrostática</li>
</ul>

<p>
<b>Íons:</b>
</p>
<ul class="org-ul">
<li><b>Cátion:</b> íon positivo (perdeu e⁻)</li>
<li><b>Ânion:</b> íon negativo (ganhou e⁻)</li>
</ul>

<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>Sólidos cristalinos</li>
<li>Altos PF e PE</li>
<li>Conduzem fundidos/dissolvidos</li>
<li>Solúveis em água</li>
</ul>

<p>
<b>Fórmula:</b>
</p>
<ul class="org-ul">
<li>Troca de valências</li>
<li>Cargas balanceadas</li>
</ul>
</div>
</div>

<div id="outline-container-orgca0ad23" class="outline-4">
<h4 id="orgca0ad23"><span class="section-number-4">2.2.9.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-2-2-9">
<pre class="example" id="orgdcf3844">
LIGAÇÃO IÔNICA:

Metal (baixa EN)  +  Não-metal (alta EN)
        ↓                    ↓
    Perde e⁻            Ganha e⁻
        ↓                    ↓
     Cátion⁺              Ânion⁻
        ↓                    ↓
        └────────┬───────────┘
          Atração eletrostática
                 ↓
          Composto Iônico

Exemplo:
Na (2,8,1) → Na⁺ (2,8) + e⁻
Cl (2,8,7) + e⁻ → Cl⁻ (2,8,8)

Na⁺ + Cl⁻ → NaCl

Propriedades:
├─ Sólidos (cristais)
├─ Altos PF/PE
├─ Conduzem fundidos/dissolvidos
└─ Solúveis em H₂O
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 30 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>ligações são fundamentais!)</li>
</ul>
</div>
</div>
</div>
</div>

<div id="outline-container-org3ce167d" class="outline-2">`;

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
