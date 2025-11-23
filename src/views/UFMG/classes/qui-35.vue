<script setup lang="ts">
import { ref } from "vue";

const code = "qui-35";
const title = "Química: Ligações Químicas";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-2">
<ul class="org-ul">
<li>Química: Ligações Químicas</li>
<li>Parte 3 (Ligação Metálica)</li>
<li>30min</li>
</ul>
</div>
<div id="outline-container-org1251acc" class="outline-4">
<h4 id="org1251acc"><span class="section-number-4">4.2.1.</span> Revisão: Ligações Químicas</h4>
<div class="outline-text-4" id="text-4-2-1">
<p>
Já estudamos:
</p>
<ul class="org-ul">
<li><b>Aula 31:</b> Ligação Iônica (metal + não-metal, transferência)</li>
<li><b>Aula 33:</b> Ligação Covalente (não-metal + não-metal, compartilhamento)</li>
</ul>

<p>
<b>Nesta aula:</b> Ligação Metálica
</p>
</div>
</div>

<div id="outline-container-orge4a9053" class="outline-4">
<h4 id="orge4a9053"><span class="section-number-4">4.2.2.</span> Ligação Metálica</h4>
<div class="outline-text-4" id="text-4-2-2">
<p>
<b>Definição:</b> Ligação entre <b>átomos de metais</b>, formando estruturas sólidas metálicas.
</p>

<p>
<b>Onde ocorre:</b>
</p>
<ul class="org-ul">
<li>Metais puros: Fe, Cu, Au, Ag, Al, Na, etc.</li>
<li>Ligas metálicas: bronze (Cu + Sn), aço (Fe + C), latão (Cu + Zn)</li>
</ul>
</div>
</div>

<div id="outline-container-org409d6de" class="outline-4">
<h4 id="org409d6de"><span class="section-number-4">4.2.3.</span> Modelo do “Mar de Elétrons”</h4>
<div class="outline-text-4" id="text-4-2-3">
<p>
<b>Teoria:</b>
</p>
<ul class="org-ul">
<li>Átomos metálicos perdem elétrons da camada de valência</li>
<li>Formam <b>cátions</b> (+) fixos em posições</li>
<li>Elétrons livres (“deslocalizados”) movem-se livremente</li>
<li><b>“Mar de elétrons”:</b> elétrons circulam entre os cátions</li>
</ul>

<p>
<b>Representação:</b>
</p>

<pre class="example" id="orga255f1d">
 ⁺   ⁺   ⁺   ⁺
e⁻ e⁻ e⁻ e⁻ e⁻
 ⁺   ⁺   ⁺   ⁺
e⁻ e⁻ e⁻ e⁻ e⁻
 ⁺   ⁺   ⁺   ⁺
</pre>

<p>
<b>Cátions (+):</b> núcleos dos átomos metálicos <b>e⁻:</b> elétrons livres, móveis
</p>

<p>
<b>Atração:</b>
</p>
<ul class="org-ul">
<li>Cátions (+) atraem elétrons (-)</li>
<li>Elétrons mantêm os cátions unidos</li>
<li><b>Ligação metálica:</b> atração entre cátions e mar de elétrons</li>
</ul>
</div>
</div>

<div id="outline-container-orgffdc9af" class="outline-4">
<h4 id="orgffdc9af"><span class="section-number-4">4.2.4.</span> Propriedades dos Metais</h4>
<div class="outline-text-4" id="text-4-2-4">
<p>
As propriedades dos metais são explicadas pelo modelo do mar de elétrons.
</p>
</div>

<div id="outline-container-orgb747c2b" class="outline-5">
<h5 id="orgb747c2b"><span class="section-number-5">4.2.4.1.</span> 1. Condutividade Elétrica</h5>
<div class="outline-text-5" id="text-4-2-4-1">
<p>
<b>Característica:</b> Metais <b>conduzem eletricidade</b> muito bem.
</p>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Elétrons livres movem-se facilmente</li>
<li>Ao aplicar diferença de potencial (voltagem), elétrons fluem</li>
<li><b>Corrente elétrica</b> = fluxo de elétrons</li>
</ul>

<p>
<b>Aplicações:</b> Fios elétricos (Cu, Al)
</p>

<p>
<b>Melhores condutores:</b> Ag (prata), Cu (cobre), Au (ouro)
</p>
</div>
</div>

<div id="outline-container-org2651c4d" class="outline-5">
<h5 id="org2651c4d"><span class="section-number-5">4.2.4.2.</span> 2. Condutividade Térmica</h5>
<div class="outline-text-5" id="text-4-2-4-2">
<p>
<b>Característica:</b> Metais conduzem <b>calor</b> eficientemente.
</p>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Elétrons livres transportam energia térmica rapidamente</li>
<li>Vibração dos cátions também contribui</li>
</ul>

<p>
<b>Aplicações:</b> Panelas (Al, Fe), dissipadores de calor (Cu)
</p>
</div>
</div>

<div id="outline-container-org56359ae" class="outline-5">
<h5 id="org56359ae"><span class="section-number-5">4.2.4.3.</span> 3. Maleabilidade</h5>
<div class="outline-text-5" id="text-4-2-4-3">
<p>
<b>Característica:</b> Metais podem ser <b>martelados</b> em lâminas finas sem quebrar.
</p>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Cátions podem deslizar uns sobre os outros</li>
<li>Mar de elétrons “se ajusta” à nova posição</li>
<li>Ligação não é rompida</li>
</ul>

<p>
<b>Exemplos:</b> Folhas de alumínio, ouro batido
</p>
</div>
</div>

<div id="outline-container-org1ce9ccc" class="outline-5">
<h5 id="org1ce9ccc"><span class="section-number-5">4.2.4.4.</span> 4. Ductilidade</h5>
<div class="outline-text-5" id="text-4-2-4-4">
<p>
<b>Característica:</b> Metais podem ser <b>esticados</b> em fios.
</p>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Mesma razão da maleabilidade</li>
<li>Cátions deslizam, elétrons mantêm ligação</li>
</ul>

<p>
<b>Exemplos:</b> Fios de cobre, arame
</p>
</div>
</div>

<div id="outline-container-orga61357c" class="outline-5">
<h5 id="orga61357c"><span class="section-number-5">4.2.4.5.</span> 5. Brilho Metálico</h5>
<div class="outline-text-5" id="text-4-2-4-5">
<p>
<b>Característica:</b> Metais têm <b>superfície brilhante</b> quando polidos.
</p>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Elétrons livres absorvem e re-emitem luz (reflexão)</li>
<li>Aparecem “brilhantes”</li>
</ul>

<p>
<b>Aplicações:</b> Espelhos (Ag), joias (Au, Ag)
</p>
</div>
</div>

<div id="outline-container-org138d7df" class="outline-5">
<h5 id="org138d7df"><span class="section-number-5">4.2.4.6.</span> 6. Estado Físico e Pontos de Fusão/Ebulição</h5>
<div class="outline-text-5" id="text-4-2-4-6">
<p>
<b>Característica:</b>
</p>
<ul class="org-ul">
<li>Maioria são <b>sólidos</b> à temperatura ambiente (exceto Hg</li>
<li>mercúrio)</li>
<li>Pontos de fusão/ebulição <b>variados</b> (geralmente médios a altos)</li>
</ul>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Ligações metálicas são fortes (mas menos que iônicas)</li>
<li>Dependem do número de elétrons de valência e tamanho do átomo</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li><b>Altos PF:</b> W (tungstênio)</li>
<li>3422°C</li>
<li><b>Baixos PF:</b> Hg (mercúrio)</li>
<li>líquido (-39°C), Ga (gálio)</li>
<li>30°C</li>
</ul>
</div>
</div>

<div id="outline-container-org29adcda" class="outline-5">
<h5 id="org29adcda"><span class="section-number-5">4.2.4.7.</span> 7. Densidade</h5>
<div class="outline-text-5" id="text-4-2-4-7">
<p>
<b>Característica:</b> Muitos metais são <b>densos</b>.
</p>

<p>
<b>Explicação:</b>
</p>
<ul class="org-ul">
<li>Átomos empacotados compactamente no retículo cristalino</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li><b>Mais densos:</b> Os (ósmio), Ir (irídio), Pt (platina), Au (ouro)</li>
<li><b>Menos densos:</b> Li (lítio), Na (sódio), K (potássio)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org833f6dd" class="outline-4">
<h4 id="org833f6dd"><span class="section-number-4">4.2.5.</span> Ligas Metálicas</h4>
<div class="outline-text-4" id="text-4-2-5">
<p>
<b>Liga metálica:</b> mistura de dois ou mais metais (ou metal + não-metal).
</p>

<p>
<b>Objetivo:</b> Melhorar propriedades (dureza, resistência à corrosão, etc.)
</p>

<p>
<b>Exemplos:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Liga</th>
<th scope="col" class="org-left">Composição</th>
<th scope="col" class="org-left">Uso</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left"><b>Aço</b></td>
<td class="org-left">Fe + C (carbono)</td>
<td class="org-left">Construção, ferramentas</td>
</tr>

<tr>
<td class="org-left"><b>Bronze</b></td>
<td class="org-left">Cu + Sn (estanho)</td>
<td class="org-left">Esculturas, moedas antigas</td>
</tr>

<tr>
<td class="org-left"><b>Latão</b></td>
<td class="org-left">Cu + Zn (zinco)</td>
<td class="org-left">Instrumentos musicais</td>
</tr>

<tr>
<td class="org-left"><b>Ouro 18k</b></td>
<td class="org-left">Au (75%) + Cu/Ag (25%)</td>
<td class="org-left">Joias (ouro puro é mole)</td>
</tr>

<tr>
<td class="org-left"><b>Aço inox</b></td>
<td class="org-left">Fe + Cr + Ni</td>
<td class="org-left">Talheres, equipamentos</td>
</tr>
</tbody>
</table>

<p>
<b>Vantagens das ligas:</b>
</p>
<ul class="org-ul">
<li><b>Mais duras</b> que metais puros</li>
<li>Resistência à <b>corrosão</b></li>
<li>Podem ser <b>mais baratas</b></li>
<li>Propriedades <b>ajustáveis</b></li>
</ul>
</div>
</div>

<div id="outline-container-org568eaf5" class="outline-4">
<h4 id="org568eaf5"><span class="section-number-4">4.2.6.</span> Resumo: Três Tipos de Ligação</h4>
<div class="outline-text-4" id="text-4-2-6">
<pre class="example" id="orge9f3c3a">
┌──────────┬─────────┬──────────┬──────────┐
│          │ IÔNICA  │COVALENTE │ METÁLICA │
├──────────┼─────────┼──────────┼──────────┤
│  Átomos  │Metal+   │Não-metal │  Metais  │
│          │Não-metal│+Não-metal│          │
├──────────┼─────────┼──────────┼──────────┤
│ Processo │Transfer.│Compartil.│Mar de e⁻ │
├──────────┼─────────┼──────────┼──────────┤
│  Formam  │  Íons   │Moléculas │  Rede    │
│          │cristais │          │ cristalina│
├──────────┼─────────┼──────────┼──────────┤
│   PF/PE  │  Altos  │  Baixos  │ Variados │
├──────────┼─────────┼──────────┼──────────┤
│Condutiv. │Fund/Dis.│   Não    │   Sim    │
│ Elétrica │         │          │ (sempre) │
├──────────┼─────────┼──────────┼──────────┤
│ Exemplo  │  NaCl   │   H₂O    │   Fe     │
└──────────┴─────────┴──────────┴──────────┘
</pre>
</div>
</div>

<div id="outline-container-org2eafeea" class="outline-4">
<h4 id="org2eafeea"><span class="section-number-4">4.2.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-2-7">
</div>
<div id="outline-container-orgb48ca8f" class="outline-5">
<h5 id="orgb48ca8f"><span class="section-number-5">4.2.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-2-7-1">
<p>
Por que metais conduzem eletricidade, mas compostos iônicos sólidos não?
</p>

<p>
<b>Resposta:</b> <b>Metais:</b> têm elétrons livres que se movem facilmente, transportando carga.
</p>

<p>
<b>Iônicos sólidos:</b> íons estão <b>fixos</b> no retículo cristalino, não podem se mover. Só conduzem quando fundidos ou dissolvidos (íons ficam livres).
</p>
</div>
</div>

<div id="outline-container-orgf299c71" class="outline-5">
<h5 id="orgf299c71"><span class="section-number-5">4.2.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-2-7-2">
<p>
Explique por que o ouro usado em joias é geralmente uma liga (ouro 18k) e não ouro puro.
</p>

<p>
<b>Resposta:</b> Ouro puro (24k) é muito <b>mole e maleável</b>, deformando facilmente. A liga com cobre ou prata (18k = 75% Au + 25% outros) torna o material <b>mais duro e resistente</b>, adequado para joias.
</p>
</div>
</div>

<div id="outline-container-orgf3a2d9f" class="outline-5">
<h5 id="orgf3a2d9f"><span class="section-number-5">4.2.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-2-7-3">
<p>
Qual o tipo de ligação presente em: a) Fe (ferro) b) H₂O (água) c) KCl (cloreto de potássio)
</p>

<p>
<b>Respostas:</b>
</p>

<ol class="org-ol">
<li><b>Metálica</b> (Fe é metal)</li>

<li><b>Covalente</b> (H e O são não-metais)</li>

<li><b>Iônica</b> (K é metal, Cl é não-metal)</li>
</ol>
</div>
</div>

<div id="outline-container-org4041248" class="outline-5">
<h5 id="org4041248"><span class="section-number-5">4.2.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-2-7-4">
<p>
(UFMG) Por que o cobre é usado em fios elétricos?
</p>

<p>
<b>Resposta:</b> Cobre tem excelente <b>condutividade elétrica</b> (elétrons livres), é <b>maleável</b> e <b>ductil</b> (pode ser esticado em fios), e tem custo relativamente baixo comparado à prata (melhor condutor).
</p>
</div>
</div>
</div>

<div id="outline-container-org80ef95e" class="outline-4">
<h4 id="org80ef95e"><span class="section-number-4">4.2.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-2-8">
<ol class="org-ol">
<li><b>Ligação metálica:</b> entre metais</li>
<li><b>Mar de elétrons:</b> elétrons livres, móveis</li>
<li><b>Conduzem eletricidade:</b> sempre (elétrons livres)</li>
<li><b>Maleáveis e dúcteis:</b> cátions deslizam</li>
<li><b>Brilho metálico:</b> elétrons refletem luz</li>
<li><b>Ligas:</b> mistura de metais (melhoram propriedades)</li>
<li><b>Comparar ligações:</b> iônica, covalente, metálica</li>
<li><b>Hg:</b> único metal líquido (temperatura ambiente)</li>
</ol>
</div>
</div>

<div id="outline-container-org79485b8" class="outline-4">
<h4 id="org79485b8"><span class="section-number-4">4.2.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-2-9">
<p>
<b>Ligação Metálica:</b>
</p>
<ul class="org-ul">
<li>Entre metais</li>
<li>Mar de elétrons livres</li>
<li>Cátions fixos + elétrons móveis</li>
</ul>

<p>
<b>Propriedades dos Metais:</b>
</p>
<ul class="org-ul">
<li>Condutividade elétrica (elétrons livres)</li>
<li>Condutividade térmica</li>
<li>Maleabilidade (martelar)</li>
<li>Ductilidade (esticar)</li>
<li>Brilho metálico</li>
<li>Sólidos (maioria)</li>
</ul>

<p>
<b>Ligas Metálicas:</b>
</p>
<ul class="org-ul">
<li>Mistura de metais</li>
<li>Melhoram propriedades</li>
<li>Exemplos: aço, bronze, latão</li>
</ul>
</div>
</div>

<div id="outline-container-orgf118d43" class="outline-4">
<h4 id="orgf118d43"><span class="section-number-4">4.2.10.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-2-10">
<pre class="example" id="orge5fa5e4">
LIGAÇÃO METÁLICA:

Metal  +  Metal  →  Retículo Metálico
  ↓        ↓
Perdem valência
  ↓
Cátions ⁺ + Mar de elétrons e⁻

Modelo:
   ⁺   ⁺   ⁺   ⁺
  e⁻ e⁻ e⁻ e⁻ e⁻  ← elétrons livres
   ⁺   ⁺   ⁺   ⁺
  e⁻ e⁻ e⁻ e⁻ e⁻
   ⁺   ⁺   ⁺   ⁺

Propriedades:
├─ Conduzem eletricidade (e⁻ livres)
├─ Conduzem calor
├─ Maleáveis (cátions deslizam)
├─ Dúcteis (esticam)
├─ Brilho (reflexão luz)
└─ Sólidos (maioria)

COMPARAÇÃO LIGAÇÕES:

IÔNICA:     Metal → Não-metal
            Transferência
            
COVALENTE:  Não-metal → Não-metal
            Compartilhamento
            
METÁLICA:   Metal → Metal
            Mar de elétrons
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 30 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (importante
</p>
<ul class="org-ul">
<li>completa o estudo de ligações!)</li>
</ul>
</div>
</div>
</div>
</div>

<div id="outline-container-orga31f15e" class="outline-2">`;

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
