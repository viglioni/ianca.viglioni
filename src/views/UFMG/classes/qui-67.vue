<script setup lang="ts">
import { ref } from "vue";

const code = "qui-67";
const title = "Química: Revisão Final";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-4">
<ul class="org-ul">
<li>Química: Revisão Final</li>
<li>Modelos Atômicos e Tabela Periódica</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org31e2b9b" class="outline-4">
<h4 id="org31e2b9b"><span class="section-number-4">2.4.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-2-4-1">
<p>
Consolidar evolução dos modelos atômicos e organização da Tabela Periódica.
</p>
</div>
</div>

<div id="outline-container-org7092e51" class="outline-4">
<h4 id="org7092e51"><span class="section-number-4">2.4.2.</span> PARTE 1: Modelos Atômicos</h4>
<div class="outline-text-4" id="text-2-4-2">
<p>
*1. Dalton (1808)
</p>
<ul class="org-ul">
<li>“Bola de Bilhar”*</li>
</ul>

<p>
<b>Ideias principais:</b>
</p>
<ul class="org-ul">
<li>Átomos são esferas maciças, indivisíveis e indestrutíveis</li>
<li>Átomos do mesmo elemento são idênticos</li>
<li>Átomos de elementos diferentes têm massas diferentes</li>
<li>Reações químicas: rearranjo de átomos</li>
</ul>

<p>
<b>Limitação:</b> não explica fenômenos elétricos
</p>

<p>
*2. Thomson (1897)
</p>
<ul class="org-ul">
<li>“Pudim de Passas”*</li>
</ul>

<p>
<b>Descoberta:</b> elétron (partícula negativa)
</p>

<p>
<b>Modelo:</b>
</p>
<ul class="org-ul">
<li>Átomo é esfera positiva</li>
<li>Elétrons (negativos) incrustados na massa positiva</li>
<li>Átomo neutro (cargas equilibradas)</li>
</ul>

<p>
<b>Limitação:</b> não explica espalhamento de partículas alfa
</p>

<p>
*3. Rutherford (1911)
</p>
<ul class="org-ul">
<li>“Planetário”*</li>
</ul>

<p>
<b>Experimento:</b> bombardeio de folha de ouro com partículas alfa
</p>

<p>
<b>Descobertas:</b>
</p>
<ul class="org-ul">
<li>Núcleo pequeno, denso e positivo (prótons)</li>
<li>Maior parte do átomo é vazio</li>
<li>Elétrons giram ao redor do núcleo</li>
</ul>

<p>
<b>Modelo:</b>
</p>

<pre class="example" id="orged4018c">
e⁻ →  ●  ← e⁻  (eletrosfera)
      ⊕        (núcleo)
e⁻ →     ← e⁻
</pre>

<p>
<b>Limitação:</b> não explica estabilidade (elétron deveria perder energia e cair)
</p>

<p>
*4. Bohr (1913)
</p>
<ul class="org-ul">
<li>Níveis de Energia*</li>
</ul>

<p>
<b>Postulados:</b>
</p>
<ul class="org-ul">
<li>Elétrons em órbitas circulares definidas (níveis de energia)</li>
<li>Elétron não perde energia na órbita estacionária</li>
<li>Mudança de nível: absorve ou emite energia (fóton)</li>
</ul>

<p>
<b>Níveis de energia:</b> K, L, M, N, O, P, Q
</p>

<p>
<b>Capacidade máxima:</b>
</p>

<pre class="example" id="orgcaa1005">
K: 2 elétrons
L: 8 elétrons
M: 18 elétrons
N: 32 elétrons

Fórmula: 2n²
</pre>

<p>
<b>Saltos quânticos:</b>
</p>

<pre class="example" id="org72af89b">
Absorve energia: elétron sobe de nível
Emite energia: elétron desce de nível
</pre>

<p>
*5. Modelo Atual
</p>
<ul class="org-ul">
<li>Quântico/Orbital*</li>
</ul>

<p>
<b>Contribuições:</b>
</p>
<ul class="org-ul">
<li>Orbitais (regiões de probabilidade)</li>
<li>Números quânticos</li>
<li>Princípio da Incerteza de Heisenberg</li>
</ul>

<p>
<b>Subníveis:</b> s, p, d, f
</p>
</div>
</div>

<div id="outline-container-orgec1ce00" class="outline-4">
<h4 id="orgec1ce00"><span class="section-number-4">2.4.3.</span> PARTE 2: Estrutura Atômica</h4>
<div class="outline-text-4" id="text-2-4-3">
<p>
<b>Partículas fundamentais:</b>
</p>

<pre class="example" id="org1a9d7b3">
┌──────────┬────────┬────────┬─────────┐
│ Partícula│ Símbolo│ Carga  │ Massa   │
├──────────┼────────┼────────┼─────────┤
│ Próton   │   p⁺   │  +1    │ ~1 u    │
│ Nêutron  │   n⁰   │   0    │ ~1 u    │
│ Elétron  │   e⁻   │  -1    │ ~1/1836u│
└──────────┴────────┴────────┴─────────┘
</pre>

<p>
<b>Notação:</b>
</p>

<pre class="example" id="orgedcdfd8">
  A
 ᴢX

A = número de massa = p + n
Z = número atômico = p = e⁻ (átomo neutro)
</pre>

<p>
<b>Relações:</b>
</p>

<pre class="example" id="orga7c5814">
Z = número de prótons
A = Z + N (N = número de nêutrons)
N = A
- Z
</pre>

<p>
<b>Íons:</b>
</p>

<pre class="example" id="org434cac1">
Cátion: perde elétrons (carga +)
Ânion: ganha elétrons (carga -)

Exemplo: Na⁺ (perdeu 1 e⁻), Cl⁻ (ganhou 1 e⁻)
</pre>

<p>
<b>Isótopos, Isóbaros, Isótonos:</b>
</p>

<pre class="example" id="org8115691">
Isótopos: mesmo Z, A diferente
  Exemplo: ¹²C e ¹⁴C

Isóbaros: mesmo A, Z diferente
  Exemplo: ⁴⁰K e ⁴⁰Ca

Isótonos: mesmo N, Z e A diferentes
  Exemplo: ¹⁴C e ¹⁵N (ambos com 7 nêutrons)
</pre>
</div>
</div>

<div id="outline-container-orgf63a48c" class="outline-4">
<h4 id="orgf63a48c"><span class="section-number-4">2.4.4.</span> PARTE 3: Tabela Periódica</h4>
<div class="outline-text-4" id="text-2-4-4">
<p>
<b>Organização:</b>
</p>

<p>
<b>Lei Periódica:</b> “As propriedades dos elementos são funções periódicas de seus números atômicos.”
</p>

<p>
<b>Períodos (linhas horizontais):</b> 7 períodos
</p>
<ul class="org-ul">
<li>Indicam número de camadas eletrônicas</li>
</ul>

<p>
<b>Famílias/Grupos (colunas verticais):</b> 18 grupos
</p>
<ul class="org-ul">
<li>Elementos com propriedades químicas semelhantes</li>
<li>Mesma quantidade de elétrons na camada de valência</li>
</ul>

<p>
<b>Principais famílias:</b>
</p>

<pre class="example" id="org0aba330">
Grupo 1: Metais Alcalinos (Li, Na, K, Rb, Cs, Fr)
Grupo 2: Metais Alcalino-Terrosos (Be, Mg, Ca, Sr, Ba, Ra)
Grupo 13: Família do Boro
Grupo 14: Família do Carbono
Grupo 15: Família do Nitrogênio
Grupo 16: Calcogênios (O, S, Se, Te, Po)
Grupo 17: Halogênios (F, Cl, Br, I, At)
Grupo 18: Gases Nobres (He, Ne, Ar, Kr, Xe, Rn)
</pre>

<p>
<b>Classificação:</b>
</p>

<p>
<b>Metais:</b>
</p>
<ul class="org-ul">
<li>Maioria dos elementos</li>
<li>Brilhantes, condutores, maleáveis</li>
<li>Lado esquerdo e centro da tabela</li>
</ul>

<p>
<b>Não-metais (ametais):</b>
</p>
<ul class="org-ul">
<li>Lado direito superior</li>
<li>C, N, O, P, S, Se, F, Cl, Br, I</li>
</ul>

<p>
<b>Semimetais (metaloides):</b>
</p>
<ul class="org-ul">
<li>Propriedades intermediárias</li>
<li>B, Si, Ge, As, Sb, Te, Po, At</li>
</ul>

<p>
<b>Gases nobres:</b>
</p>
<ul class="org-ul">
<li>Grupo 18</li>
<li>Inertes (estáveis)</li>
<li>Camada de valência completa</li>
</ul>

<p>
<b>Hidrogênio (H):</b>
</p>
<ul class="org-ul">
<li>Elemento especial</li>
<li>Não se encaixa perfeitamente em nenhuma família</li>
</ul>
</div>
</div>

<div id="outline-container-org2da4444" class="outline-4">
<h4 id="org2da4444"><span class="section-number-4">2.4.5.</span> Propriedades Periódicas</h4>
<div class="outline-text-4" id="text-2-4-5">
<p>
<b>1. Raio Atômico:</b>
</p>

<pre class="example" id="org4688fab">
↑ Na família (grupo): raio aumenta (mais camadas)
→ No período: raio diminui (mais prótons, maior atração)
</pre>

<p>
<b>2. Energia de Ionização:</b>
</p>
<ul class="org-ul">
<li>Energia para remover 1 elétron</li>
</ul>

<pre class="example" id="orgb8ccf18">
↑ Na família: diminui (elétrons mais afastados)
→ No período: aumenta (maior atração nuclear)
</pre>

<p>
<b>3. Eletronegatividade:</b>
</p>
<ul class="org-ul">
<li>Capacidade de atrair elétrons em ligação</li>
</ul>

<pre class="example" id="org65f1e9e">
↑ Na família: diminui
→ No período: aumenta

Mais eletronegativo: F (flúor)
Menos eletronegativo: Fr (frâncio)

Ordem: F &gt; O &gt; N &gt; Cl
</pre>

<p>
<b>4. Eletroafinidade:</b>
</p>
<ul class="org-ul">
<li>Energia liberada ao receber 1 elétron</li>
<li>Segue tendência similar à eletronegatividade</li>
</ul>
</div>
</div>

<div id="outline-container-orge42a81c" class="outline-4">
<h4 id="orge42a81c"><span class="section-number-4">2.4.6.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-2-4-6">
</div>
<div id="outline-container-org15d93e2" class="outline-5">
<h5 id="org15d93e2"><span class="section-number-5">2.4.6.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-2-4-6-1">
<p>
Qual modelo atômico descobriu o núcleo?
</p>

<p>
<i>[Ver resposta 2 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org33462f3" class="outline-5">
<h5 id="org33462f3"><span class="section-number-5">2.4.6.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-2-4-6-2">
<p>
Um elemento tem Z = 17 e A = 35. Quantos nêutrons possui?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgbb28e83">
N = A
- Z = 35
- 17 = 18 nêutrons
</pre>
</div>
</div>

<div id="outline-container-org8a954fc" class="outline-5">
<h5 id="org8a954fc"><span class="section-number-5">2.4.6.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-2-4-6-3">
<p>
Quantos elétrons cabem na camada M?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org5787bc3">
n = 3
2n² = 2(3)² = 18 elétrons
</pre>
</div>
</div>

<div id="outline-container-org701b795" class="outline-5">
<h5 id="org701b795"><span class="section-number-5">2.4.6.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-2-4-6-4">
<p>
¹²C e ¹⁴C são:
</p>

<p>
<i>[Ver resposta 3 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgd2653aa" class="outline-5">
<h5 id="orgd2653aa"><span class="section-number-5">2.4.6.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-2-4-6-5">
<p>
Qual elemento é mais eletronegativo: O ou S?
</p>

<p>
<i>[Ver resposta 4 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org6ee28f9" class="outline-4">
<h4 id="org6ee28f9"><span class="section-number-4">2.4.7.</span> Resumo de Modelos</h4>
<div class="outline-text-4" id="text-2-4-7">
<pre class="example" id="orgecb3eda">
Dalton → Esfera maciça
Thomson → Pudim de passas
Rutherford → Núcleo + eletrosfera
Bohr → Níveis de energia
Atual → Orbitais (probabilidade)
</pre>
</div>
</div>

<div id="outline-container-org62c6a92" class="outline-4">
<h4 id="org62c6a92"><span class="section-number-4">2.4.8.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-4-8">
<pre class="example" id="orgc7b611e">
ESTRUTURA ATÔMICA:
Z = número de prótons
A = Z + N
N = A
- Z

Capacidade de camada:
Máximo = 2n²

TABELA PERIÓDICA:
Períodos: 7 (linhas)
Grupos: 18 (colunas)

PROPRIEDADES PERIÓDICAS:
Raio atômico: ↑ família, ← período
Energia ionização: ↓ família, → período
Eletronegatividade: ↓ família, → período

Mais eletronegativo: F
Ordem: F &gt; O &gt; N &gt; Cl
</pre>
</div>
</div>

<div id="outline-container-org3c6a47a" class="outline-4">
<h4 id="org3c6a47a"><span class="section-number-4">2.4.9.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-2-4-9">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei os principais modelos atômicos em ordem</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular número de nêutrons (N = A</li>
<li>Z)</li>
<li class="off"><code>[&#xa0;]</code> Sei diferenciar isótopos, isóbaros, isótonos</li>
<li class="off"><code>[&#xa0;]</code> Sei a organização da Tabela Periódica</li>
<li class="off"><code>[&#xa0;]</code> Conheço as principais famílias</li>
<li class="off"><code>[&#xa0;]</code> Sei classificar metais, não-metais, semimetais</li>
<li class="off"><code>[&#xa0;]</code> Sei as tendências das propriedades periódicas</li>
<li class="off"><code>[&#xa0;]</code> Sei que F é o mais eletronegativo</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (fundamental!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org7b0a4ce" class="outline-3">`;

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
