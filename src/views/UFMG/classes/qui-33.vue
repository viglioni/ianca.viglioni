<script setup lang="ts">
import { ref } from "vue";

const code = "qui-33";
const title = "Química: Ligações Químicas";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-2">
<ul class="org-ul">
<li>Química: Ligações Químicas</li>
<li>Parte 2 (Ligação Covalente)</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-orgc763e63" class="outline-4">
<h4 id="orgc763e63"><span class="section-number-4">3.2.1.</span> Revisão: Ligações Químicas</h4>
<div class="outline-text-4" id="text-3-2-1">
<p>
Na Aula 31, estudamos:
</p>
<ul class="org-ul">
<li><b>Ligação Iônica:</b> metal + não-metal, transferência de elétrons, íons</li>
</ul>

<p>
<b>Nesta aula:</b> Ligação Covalente (molecular)
</p>
</div>
</div>

<div id="outline-container-orgee853c4" class="outline-4">
<h4 id="orgee853c4"><span class="section-number-4">3.2.2.</span> Ligação Covalente</h4>
<div class="outline-text-4" id="text-3-2-2">
<p>
<b>Definição:</b> Ligação entre <b>não-metais</b> através do <b>compartilhamento de elétrons</b>.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Não-metal + Não-metal</li>
<li><b>Compartilham</b> elétrons (não transferem)</li>
<li>Formam <b>moléculas</b></li>
<li>Pequena diferença de eletronegatividade (ΔEN &lt; 1,7)</li>
</ul>

<p>
<b>Objetivo:</b> Ambos os átomos atingem configuração de gás nobre (regra do octeto ou dueto).
</p>
</div>
</div>

<div id="outline-container-orgb56d09f" class="outline-4">
<h4 id="orgb56d09f"><span class="section-number-4">3.2.3.</span> Formação da Ligação Covalente</h4>
<div class="outline-text-4" id="text-3-2-3">
</div>
<div id="outline-container-org4863703" class="outline-5">
<h5 id="org4863703"><span class="section-number-5">3.2.3.1.</span> Exemplo 1: Hidrogênio (H₂)</h5>
<div class="outline-text-5" id="text-3-2-3-1">
<p>
<b>H (Z = 1):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 1</li>
<li>Precisa de 1 elétron para completar (dueto: 2 elétrons)</li>
</ul>

<p>
<b>Ligação:</b>
</p>

<pre class="example" id="org66a164e">
H • + • H  →  H : H  ou  H─H
</pre>

<p>
Cada H compartilha 1 elétron → ambos ficam com 2 elétrons (estáveis)
</p>

<p>
<b>Fórmula molecular:</b> H₂
</p>

<p>
<b>Fórmula estrutural:</b> H─H (traço = par de elétrons compartilhado)
</p>
</div>
</div>

<div id="outline-container-org8341a98" class="outline-5">
<h5 id="org8341a98"><span class="section-number-5">3.2.3.2.</span> Exemplo 2: Cloro (Cl₂)</h5>
<div class="outline-text-5" id="text-3-2-3-2">
<p>
<b>Cl (Z = 17):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 8, 7</li>
<li>Precisa de 1 elétron para completar octeto (8)</li>
</ul>

<p>
<b>Representação de Lewis:</b>
</p>

<pre class="example" id="orge6d676e">
:Cl· + ·Cl:  →  :Cl:Cl:  ou  Cl─Cl
</pre>

<p>
Cada Cl compartilha 1 elétron → ambos com 8 elétrons na valência
</p>

<p>
<b>Fórmula molecular:</b> Cl₂
</p>
</div>
</div>

<div id="outline-container-org397ecc6" class="outline-5">
<h5 id="org397ecc6"><span class="section-number-5">3.2.3.3.</span> Exemplo 3: Água (H₂O)</h5>
<div class="outline-text-5" id="text-3-2-3-3">
<p>
<b>O (Z = 8):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 6</li>
<li>Precisa de 2 elétrons</li>
</ul>

<p>
<b>H:</b>
</p>
<ul class="org-ul">
<li>Precisa de 1 elétron (cada)</li>
</ul>

<p>
<b>Ligação:</b>
</p>

<pre class="example" id="org7d8a10e">
    ·O·
   H   H
   
Cada H compartilha 1 elétron com O
O compartilha 2 elétrons (1 com cada H)
</pre>

<p>
<b>Fórmula estrutural:</b>
</p>

<pre class="example" id="orgcfb93e7">
H─O─H
</pre>

<p>
O tem 8 elétrons (2 ligações + 4 não-ligantes) Cada H tem 2 elétrons
</p>
</div>
</div>

<div id="outline-container-orgd369dbb" class="outline-5">
<h5 id="orgd369dbb"><span class="section-number-5">3.2.3.4.</span> Exemplo 4: Amônia (NH₃)</h5>
<div class="outline-text-5" id="text-3-2-3-4">
<p>
<b>N (Z = 7):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 5</li>
<li>Precisa de 3 elétrons</li>
</ul>

<p>
<b>H:</b> precisa de 1 (cada um)
</p>

<p>
<b>Fórmula estrutural:</b>
</p>

<pre class="example" id="org139d417">
  H
  │
H─N─H
</pre>

<p>
N faz 3 ligações (compartilha 6 elétrons) + 2 não-ligantes = 8 total
</p>
</div>
</div>

<div id="outline-container-org5003ab8" class="outline-5">
<h5 id="org5003ab8"><span class="section-number-5">3.2.3.5.</span> Exemplo 5: Metano (CH₄)</h5>
<div class="outline-text-5" id="text-3-2-3-5">
<p>
<b>C (Z = 6):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 2, 4</li>
<li>Precisa de 4 elétrons</li>
</ul>

<p>
<b>Fórmula estrutural:</b>
</p>

<pre class="example" id="org7fa9038">
  H
  │
H─C─H
  │
  H
</pre>

<p>
C faz 4 ligações → 8 elétrons (octeto completo)
</p>
</div>
</div>
</div>

<div id="outline-container-org0919c05" class="outline-4">
<h4 id="org0919c05"><span class="section-number-4">3.2.4.</span> Tipos de Ligações Covalentes</h4>
<div class="outline-text-4" id="text-3-2-4">
</div>
<div id="outline-container-org735cdcb" class="outline-5">
<h5 id="org735cdcb"><span class="section-number-5">3.2.4.1.</span> 1. Ligação Simples</h5>
<div class="outline-text-5" id="text-3-2-4-1">
<p>
Um par de elétrons compartilhado.
</p>

<p>
<b>Representação:</b> A─B
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>H─H</li>
<li>Cl─Cl</li>
<li>H─O─H</li>
</ul>
</div>
</div>

<div id="outline-container-org13ac107" class="outline-5">
<h5 id="org13ac107"><span class="section-number-5">3.2.4.2.</span> 2. Ligação Dupla</h5>
<div class="outline-text-5" id="text-3-2-4-2">
<p>
Dois pares de elétrons compartilhados.
</p>

<p>
<b>Representação:</b> A═B
</p>

<p>
<b>Exemplo: Oxigênio (O₂)</b>
</p>

<p>
<b>O:</b> 2, 6 (precisa de 2 elétrons)
</p>

<pre class="example" id="org4c2d187">
:O::O:  ou  O═O
</pre>

<p>
Cada O compartilha 2 elétrons (4 no total) → ligação dupla
</p>
</div>
</div>

<div id="outline-container-org78e8692" class="outline-5">
<h5 id="org78e8692"><span class="section-number-5">3.2.4.3.</span> 3. Ligação Tripla</h5>
<div class="outline-text-5" id="text-3-2-4-3">
<p>
Três pares de elétrons compartilhados.
</p>

<p>
<b>Representação:</b> A≡B
</p>

<p>
<b>Exemplo: Nitrogênio (N₂)</b>
</p>

<p>
<b>N:</b> 2, 5 (precisa de 3 elétrons)
</p>

<pre class="example" id="orgd95f3ee">
:N:::N:  ou  N≡N
</pre>

<p>
Cada N compartilha 3 elétrons (6 no total) → ligação tripla
</p>

<p>
<b>Outro exemplo: Gás carbônico (CO₂)</b>
</p>

<pre class="example" id="orgc584a72">
O═C═O
</pre>

<p>
C faz duas ligações duplas (4 pares = 8 elétrons)
</p>
</div>
</div>
</div>

<div id="outline-container-orgb5ae384" class="outline-4">
<h4 id="orgb5ae384"><span class="section-number-4">3.2.5.</span> Polaridade das Ligações Covalentes</h4>
<div class="outline-text-4" id="text-3-2-5">
</div>
<div id="outline-container-org2d60590" class="outline-5">
<h5 id="org2d60590"><span class="section-number-5">3.2.5.1.</span> Ligação Covalente Apolar</h5>
<div class="outline-text-5" id="text-3-2-5-1">
<p>
<b>Condição:</b> ΔEN = 0 (átomos iguais ou eletronegatividades iguais)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Elétrons compartilhados <b>igualmente</b></li>
<li>Sem polo positivo/negativo</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>H₂, O₂, N₂, Cl₂ (moléculas diatômicas iguais)</li>
<li>CH₄ (simetria molecular)</li>
</ul>
</div>
</div>

<div id="outline-container-orgb373d75" class="outline-5">
<h5 id="orgb373d75"><span class="section-number-5">3.2.5.2.</span> Ligação Covalente Polar</h5>
<div class="outline-text-5" id="text-3-2-5-2">
<p>
<b>Condição:</b> 0 &lt; ΔEN &lt; 1,7 (átomos diferentes)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Elétrons compartilhados <b>desigualmente</b></li>
<li>Átomo mais eletronegativo “puxa” mais os elétrons</li>
<li>Forma <b>polos:</b> δ⁺ (parcialmente positivo) e δ⁻ (parcialmente negativo)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li><b>HCl:</b> Cl mais eletronegativo → H^{(δ+)─Cl}(δ-)</li>
<li><b>H₂O:</b> O mais eletronegativo → H^{(δ+)─O}(δ-)─H^(δ+)</li>
</ul>

<p>
<b>Dipolo elétrico:</b> representado por seta → apontando para polo negativo
</p>

<pre class="example" id="orgb5620b4">
H → Cl
  ↑
 dipolo
</pre>
</div>
</div>
</div>

<div id="outline-container-org3ddb8bf" class="outline-4">
<h4 id="org3ddb8bf"><span class="section-number-4">3.2.6.</span> Geometria Molecular (Introdução)</h4>
<div class="outline-text-4" id="text-3-2-6">
<p>
A <b>forma tridimensional</b> da molécula influencia propriedades.
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Linear:</b> CO₂ (O═C═O)
</p>
<ul class="org-ul">
<li>180°</li>
</ul>

<p>
<b>Angular:</b> H₂O
</p>

<pre class="example" id="org72a5594">
H
 \\
  O  (104,5°)
 /
H
</pre>

<p>
<b>Trigonal plana:</b> BF₃
</p>
<ul class="org-ul">
<li>120°</li>
</ul>

<p>
<b>Tetraédrica:</b> CH₄
</p>

<pre class="example" id="org263a923">
  H
  │
H─C─H  (109,5°)
  │
  H
</pre>

<p>
<b>Piramidal:</b> NH₃
</p>

<p>
(Aprofundaremos geometria em aulas futuras)
</p>
</div>
</div>

<div id="outline-container-org84e5959" class="outline-4">
<h4 id="org84e5959"><span class="section-number-4">3.2.7.</span> Propriedades dos Compostos Covalentes (Moleculares)</h4>
<div class="outline-text-4" id="text-3-2-7">
<p>
<b>1. Estado físico:</b>
</p>
<ul class="org-ul">
<li><b>Gases</b> ou <b>líquidos</b> à temperatura ambiente (maioria)</li>
<li>Alguns sólidos (açúcar, gelo)</li>
</ul>

<p>
<b>2. Ponto de fusão e ebulição:</b>
</p>
<ul class="org-ul">
<li><b>Baixos</b> (forças intermoleculares fracas)</li>
<li>Exceção: macromoléculas (diamante, quartzo)</li>
</ul>

<p>
<b>3. Condutividade elétrica:</b>
</p>
<ul class="org-ul">
<li><b>NÃO conduzem</b> (não têm íons livres)</li>
<li>Exceção: grafite (estrutura especial)</li>
</ul>

<p>
<b>4. Solubilidade:</b>
</p>
<ul class="org-ul">
<li>Polares: solúveis em solventes polares (água)</li>
<li>Apolares: solúveis em solventes apolares (gasolina)</li>
<li>“Semelhante dissolve semelhante”</li>
</ul>
</div>
</div>

<div id="outline-container-orgbe74bad" class="outline-4">
<h4 id="orgbe74bad"><span class="section-number-4">3.2.8.</span> Comparação: Ligação Iônica vs. Covalente</h4>
<div class="outline-text-4" id="text-3-2-8">
<pre class="example" id="org82a77d1">
┌──────────────┬──────────────┬──────────────┐
│              │    IÔNICA    │  COVALENTE   │
├──────────────┼──────────────┼──────────────┤
│ Átomos       │Metal+Não-met.│Não-metal+Não │
│ Processo     │ Transferência│Compartilhamento│
│ Formam       │    Íons      │  Moléculas   │
│ Estado físico│   Sólidos    │ Gases/Líquidos│
│ PF/PE        │    Altos     │    Baixos    │
│ Condutividade│Fund/Dissol.  │  Não conduz  │
│ Exemplo      │    NaCl      │     H₂O      │
└──────────────┴──────────────┴──────────────┘
</pre>
</div>
</div>

<div id="outline-container-orgda1dc24" class="outline-4">
<h4 id="orgda1dc24"><span class="section-number-4">3.2.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-2-9">
</div>
<div id="outline-container-orgc42809b" class="outline-5">
<h5 id="orgc42809b"><span class="section-number-5">3.2.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-2-9-1">
<p>
Represente a fórmula estrutural do F₂ (Z do F = 9).
</p>

<p>
<b>Solução:</b>
</p>

<p>
F: 2, 7 (precisa de 1 elétron)
</p>

<pre class="example" id="orge42f366">
:F: + :F:  →  :F:F:  ou  F─F
</pre>

<p>
<i>[Ver resposta 18 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org5e6d069" class="outline-5">
<h5 id="org5e6d069"><span class="section-number-5">3.2.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-2-9-2">
<p>
Quantas ligações o carbono faz na molécula CO₂?
</p>

<p>
<b>Solução:</b>
</p>

<p>
C: 2, 4 (precisa de 4 elétrons = 4 ligações)
</p>

<p>
Estrutura: O═C═O
</p>

<p>
C faz <b>2 ligações duplas</b> (total: 4 ligações)
</p>

<p>
<i>[Ver resposta 19 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org86da578" class="outline-5">
<h5 id="org86da578"><span class="section-number-5">3.2.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-2-9-3">
<p>
A ligação H─Cl é polar ou apolar? Por quê?
</p>

<p>
<b>Solução:</b>
</p>

<p>
H e Cl são átomos <b>diferentes</b> Cl é <b>mais eletronegativo</b> que H ΔEN &gt; 0
</p>

<p>
<i>[Ver resposta 20 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org37cd0bd" class="outline-5">
<h5 id="org37cd0bd"><span class="section-number-5">3.2.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-2-9-4">
<p>
(UFMG) Qual o tipo de ligação em cada substância: a) NaCl b) H₂ c) CaO
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li><b>NaCl:</b> Na (metal) + Cl (não-metal) → <b>Iônica</b></li>

<li><b>H₂:</b> H + H (não-metais iguais) → <b>Covalente apolar</b></li>

<li><b>CaO:</b> Ca (metal) + O (não-metal) → <b>Iônica</b></li>
</ol>
</div>
</div>
</div>

<div id="outline-container-org5c5441f" class="outline-4">
<h4 id="org5c5441f"><span class="section-number-4">3.2.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-2-10">
<ol class="org-ol">
<li><b>Ligação covalente:</b> não-metal + não-metal</li>
<li><b>Compartilhamento</b> de elétrons (não transferência)</li>
<li><b>Ligação simples:</b> 1 par (─)</li>
<li><b>Ligação dupla:</b> 2 pares (═)</li>
<li><b>Ligação tripla:</b> 3 pares (≡)</li>
<li><b>Apolar:</b> ΔEN = 0 (átomos iguais ou simétricos)</li>
<li><b>Polar:</b> 0 &lt; ΔEN &lt; 1,7 (átomos diferentes)</li>
<li><b>Propriedades:</b> baixos PF/PE, não conduzem</li>
</ol>
</div>
</div>

<div id="outline-container-orgf2a680e" class="outline-4">
<h4 id="orgf2a680e"><span class="section-number-4">3.2.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-2-11">
<p>
<b>Ligação Covalente:</b>
</p>
<ul class="org-ul">
<li>Não-metal + Não-metal</li>
<li>Compartilhamento de elétrons</li>
<li>Formam moléculas</li>
</ul>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li>Simples: ─ (1 par)</li>
<li>Dupla: ═ (2 pares)</li>
<li>Tripla: ≡ (3 pares)</li>
</ul>

<p>
<b>Polaridade:</b>
</p>
<ul class="org-ul">
<li>Apolar: ΔEN = 0</li>
<li>Polar: 0 &lt; ΔEN &lt; 1,7</li>
</ul>

<p>
<b>Propriedades (molecular):</b>
</p>
<ul class="org-ul">
<li>Baixos PF/PE</li>
<li>Gases ou líquidos</li>
<li>Não conduzem eletricidade</li>
</ul>
</div>
</div>

<div id="outline-container-org0364648" class="outline-4">
<h4 id="org0364648"><span class="section-number-4">3.2.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-3-2-12">
<pre class="example" id="org2742195">
LIGAÇÃO COVALENTE:

Não-metal  +  Não-metal
     ↓            ↓
 Compartilham elétrons
          ↓
      Moléculas

Exemplos:
H · + · H  →  H:H  →  H─H  (H₂)

:Cl· + ·Cl: → :Cl:Cl: → Cl─Cl (Cl₂)

·Ö· + H + H → H:Ö:H → H─O─H (H₂O)
              

Tipos de Ligação:
Simples:  A─B   (1 par)
Dupla:    A═B   (2 pares)
Tripla:   A≡B   (3 pares)

Polaridade:
Apolar:  H─H  (ΔEN = 0)
         Cl─Cl

Polar:   H^δ+─Cl^δ-  (ΔEN &gt; 0)
         H^δ+─O^δ-─H^δ+
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 30 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>ligação covalente é fundamental!)</li>
</ul>
</div>
</div>
</div>
</div>

<div id="outline-container-org53a2106" class="outline-2">`;

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
