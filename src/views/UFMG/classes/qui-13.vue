<script setup lang="ts">
import { ref } from "vue";

const code = "qui-13";
const title = "Química: Estrutura Atômica e Radioatividade";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-3">
<ul class="org-ul">
<li>Química: Estrutura Atômica e Radioatividade</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org3c96c89" class="outline-4">
<h4 id="org3c96c89"><span class="section-number-4">3.3.1.</span> Estrutura do Átomo</h4>
<div class="outline-text-4" id="text-3-3-1">
<p>
<b>Átomo</b> é a menor partícula que caracteriza um elemento químico. É formado por três partículas fundamentais:
</p>
</div>

<div id="outline-container-orgb6afe60" class="outline-5">
<h5 id="orgb6afe60"><span class="section-number-5">3.3.1.1.</span> Partículas Subatômicas</h5>
<div class="outline-text-5" id="text-3-3-1-1">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Partícula</th>
<th scope="col" class="org-left">Símbolo</th>
<th scope="col" class="org-right">Carga</th>
<th scope="col" class="org-right">Massa (u)</th>
<th scope="col" class="org-left">Localização</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left"><b>Próton</b></td>
<td class="org-left">p⁺</td>
<td class="org-right">+1</td>
<td class="org-right">1</td>
<td class="org-left">Núcleo</td>
</tr>

<tr>
<td class="org-left"><b>Nêutron</b></td>
<td class="org-left">n⁰</td>
<td class="org-right">0</td>
<td class="org-right">1</td>
<td class="org-left">Núcleo</td>
</tr>

<tr>
<td class="org-left"><b>Elétron</b></td>
<td class="org-left">e⁻</td>
<td class="org-right">-1</td>
<td class="org-right">~0 (1/1836)</td>
<td class="org-left">Eletrosfera</td>
</tr>
</tbody>
</table>

<p>
<b>Observações:</b>
</p>
<ul class="org-ul">
<li>Prótons e nêutrons têm massa semelhante</li>
<li>Elétrons têm massa desprezível comparada aos prótons/nêutrons</li>
<li>Átomo neutro: número de prótons = número de elétrons</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgfea9d32" class="outline-4">
<h4 id="orgfea9d32"><span class="section-number-4">3.3.2.</span> Representação do Átomo</h4>
<div class="outline-text-4" id="text-3-3-2">
<p>
<b>Número Atômico (Z):</b>
</p>
<ul class="org-ul">
<li>Número de prótons no núcleo</li>
<li>Identifica o elemento químico</li>
<li>Em átomo neutro: Z = número de prótons = número de elétrons</li>
</ul>

<p>
<b>Número de Massa (A):</b>
</p>
<ul class="org-ul">
<li>Soma de prótons e nêutrons no núcleo</li>
<li>A = Z + N (onde N = número de nêutrons)</li>
</ul>

<p>
<b>Notação:</b>
</p>

<pre class="example" id="orgd7acda7">
  A
 X
  Z

Onde:
X = símbolo do elemento
A = número de massa
Z = número atômico
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org2e5c300">
  23
 Na    →  Sódio
  11

Z = 11 (11 prótons e 11 elétrons)
A = 23
N = A
- Z = 23
- 11 = 12 nêutrons
</pre>
</div>
</div>

<div id="outline-container-org33acee0" class="outline-4">
<h4 id="org33acee0"><span class="section-number-4">3.3.3.</span> Íons</h4>
<div class="outline-text-4" id="text-3-3-3">
<p>
<b>Íon</b> é um átomo ou grupo de átomos que perdeu ou ganhou elétrons, adquirindo carga elétrica.
</p>
</div>

<div id="outline-container-org85df0f4" class="outline-5">
<h5 id="org85df0f4"><span class="section-number-5">3.3.3.1.</span> Cátion (íon positivo)</h5>
<div class="outline-text-5" id="text-3-3-3-1">
<ul class="org-ul">
<li>Átomo que <b>perdeu</b> elétrons</li>
<li>Carga positiva</li>
<li>Geralmente metais</li>
</ul>

<p>
<b>Exemplo:</b> Na → Na⁺ + e⁻
</p>

<ul class="org-ul">
<li>Na: 11 prótons, 11 elétrons (neutro)</li>
<li>Na⁺: 11 prótons, 10 elétrons (cátion)</li>
</ul>
</div>
</div>

<div id="outline-container-org605f3e1" class="outline-5">
<h5 id="org605f3e1"><span class="section-number-5">3.3.3.2.</span> Ânion (íon negativo)</h5>
<div class="outline-text-5" id="text-3-3-3-2">
<ul class="org-ul">
<li>Átomo que <b>ganhou</b> elétrons</li>
<li>Carga negativa</li>
<li>Geralmente ametais</li>
</ul>

<p>
<b>Exemplo:</b> Cl + e⁻ → Cl⁻
</p>

<ul class="org-ul">
<li>Cl: 17 prótons, 17 elétrons (neutro)</li>
<li>Cl⁻: 17 prótons, 18 elétrons (ânion)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orge979267" class="outline-4">
<h4 id="orge979267"><span class="section-number-4">3.3.4.</span> Isótopos, Isóbaros e Isótonos</h4>
<div class="outline-text-4" id="text-3-3-4">
</div>
<div id="outline-container-org3ef5d4a" class="outline-5">
<h5 id="org3ef5d4a"><span class="section-number-5">3.3.4.1.</span> Isótopos</h5>
<div class="outline-text-5" id="text-3-3-4-1">
<p>
<b>Mesmo elemento (mesmo Z), diferentes massas (diferente A)</b>
</p>
<ul class="org-ul">
<li>Mesmo número de prótons</li>
<li>Diferente número de nêutrons</li>
</ul>

<p>
<b>Exemplo:</b> Isótopos do Carbono
</p>
<ul class="org-ul">
<li>¹²C₆: 6 prótons, 6 nêutrons</li>
<li>¹³C₆: 6 prótons, 7 nêutrons</li>
<li>¹⁴C₆: 6 prótons, 8 nêutrons</li>
</ul>

<p>
<b>Aplicação:</b> Carbono-14 (¹⁴C) é usado para datação de fósseis
</p>
</div>
</div>

<div id="outline-container-orgd612dfa" class="outline-5">
<h5 id="orgd612dfa"><span class="section-number-5">3.3.4.2.</span> Isóbaros</h5>
<div class="outline-text-5" id="text-3-3-4-2">
<p>
<b>Elementos diferentes (diferente Z), mesma massa (mesmo A)</b>
</p>
<ul class="org-ul">
<li>Diferente número de prótons</li>
<li>Mesma massa total</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>⁴⁰K₁₉: 19 prótons, 21 nêutrons</li>
<li>⁴⁰Ca₂₀: 20 prótons, 20 nêutrons</li>
</ul>
</div>
</div>

<div id="outline-container-orgaa80cab" class="outline-5">
<h5 id="orgaa80cab"><span class="section-number-5">3.3.4.3.</span> Isótonos</h5>
<div class="outline-text-5" id="text-3-3-4-3">
<p>
<b>Elementos diferentes (diferente Z), mesmo número de nêutrons</b>
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>¹⁴C₆: 6 prótons, 8 nêutrons</li>
<li>¹⁵N₇: 7 prótons, 8 nêutrons</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgd4e963d" class="outline-4">
<h4 id="orgd4e963d"><span class="section-number-4">3.3.5.</span> Resumo</h4>
<div class="outline-text-4" id="text-3-3-5">
<ul class="org-ul">
<li>ISO</li>
</ul>
<pre class="example" id="orgad49753">
┌─────────────┬────────┬────────┬──────────┐
│             │   Z    │   A    │    N     │
├─────────────┼────────┼────────┼──────────┤
│ Isótopos    │ Igual  │ Diferente│ Diferente│
│ Isóbaros    │Diferente│ Igual  │ Diferente│
│ Isótonos    │Diferente│Diferente│  Igual   │
└─────────────┴────────┴────────┴──────────┘
</pre>
</div>
</div>

<div id="outline-container-org5030749" class="outline-4">
<h4 id="org5030749"><span class="section-number-4">3.3.6.</span> Massa Atômica e Massa Molecular</h4>
<div class="outline-text-4" id="text-3-3-6">
</div>
<div id="outline-container-org1cc2ed5" class="outline-5">
<h5 id="org1cc2ed5"><span class="section-number-5">3.3.6.1.</span> Massa Atômica (MA)</h5>
<div class="outline-text-5" id="text-3-3-6-1">
<ul class="org-ul">
<li>Massa de um átomo medida em unidades de massa atômica (u)</li>
<li>1 u = 1/12 da massa do átomo de ¹²C</li>
</ul>

<p>
<b>Para isótopos:</b> Média ponderada das massas dos isótopos naturais
</p>

<p>
<b>Exemplo:</b> Cloro natural
</p>
<ul class="org-ul">
<li>³⁵Cl (75%) → massa = 35 u</li>
<li>³⁷Cl (25%) → massa = 37 u</li>
</ul>

<p>
MA(Cl) = (35 × 75 + 37 × 25) / 100 MA(Cl) = (2625 + 925) / 100 MA(Cl) = 35,5 u
</p>
</div>
</div>

<div id="outline-container-org2601bcd" class="outline-5">
<h5 id="org2601bcd"><span class="section-number-5">3.3.6.2.</span> Massa Molecular (MM)</h5>
<div class="outline-text-5" id="text-3-3-6-2">
<p>
Soma das massas atômicas dos átomos que formam a molécula.
</p>

<p>
<b>Exemplo:</b> H₂O
</p>
<ul class="org-ul">
<li>H: 1 u (2 átomos)</li>
<li>O: 16 u (1 átomo)</li>
</ul>

<p>
MM(H₂O) = 2(1) + 1(16) = 18 u
</p>
</div>
</div>
</div>

<div id="outline-container-orgaa42a19" class="outline-4">
<h4 id="orgaa42a19"><span class="section-number-4">3.3.7.</span> Distribuição Eletrônica</h4>
<div class="outline-text-4" id="text-3-3-7">
<p>
Os elétrons estão distribuídos em <b>camadas</b> ou <b>níveis de energia</b> ao redor do núcleo.
</p>
</div>

<div id="outline-container-orga0623be" class="outline-5">
<h5 id="orga0623be"><span class="section-number-5">3.3.7.1.</span> Camadas Eletrônicas</h5>
<div class="outline-text-5" id="text-3-3-7-1">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-left" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-right">Camada</th>
<th scope="col" class="org-left">Nome</th>
<th scope="col" class="org-right">Nº máximo de elétrons</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-right">1</td>
<td class="org-left">K</td>
<td class="org-right">2</td>
</tr>

<tr>
<td class="org-right">2</td>
<td class="org-left">L</td>
<td class="org-right">8</td>
</tr>

<tr>
<td class="org-right">3</td>
<td class="org-left">M</td>
<td class="org-right">18</td>
</tr>

<tr>
<td class="org-right">4</td>
<td class="org-left">N</td>
<td class="org-right">32</td>
</tr>

<tr>
<td class="org-right">5</td>
<td class="org-left">O</td>
<td class="org-right">32</td>
</tr>

<tr>
<td class="org-right">6</td>
<td class="org-left">P</td>
<td class="org-right">18</td>
</tr>

<tr>
<td class="org-right">7</td>
<td class="org-left">Q</td>
<td class="org-right">8</td>
</tr>
</tbody>
</table>

<p>
<b>Fórmula geral:</b> Máximo = 2n² (onde n = número da camada)
</p>
</div>
</div>

<div id="outline-container-org12cb8b6" class="outline-5">
<h5 id="org12cb8b6"><span class="section-number-5">3.3.7.2.</span> Distribuição por Camadas (Diagrama de Pauling)</h5>
<div class="outline-text-5" id="text-3-3-7-2">
<p>
<b>Ordem de preenchimento (Diagrama de Linus Pauling):</b>
</p>

<pre class="example" id="orgbb9ffec">
1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s²...
</pre>

<p>
<b>Regra prática:</b> 1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s&#x2026;
</p>

<p>
<b>Capacidade dos subníveis:</b>
</p>
<ul class="org-ul">
<li>s: até 2 elétrons</li>
<li>p: até 6 elétrons</li>
<li>d: até 10 elétrons</li>
<li>f: até 14 elétrons</li>
</ul>
</div>
</div>

<div id="outline-container-org83c3233" class="outline-5">
<h5 id="org83c3233"><span class="section-number-5">3.3.7.3.</span> Exemplos de Distribuição</h5>
<div class="outline-text-5" id="text-3-3-7-3">
<p>
<b>Exemplo 1: Sódio (Na, Z = 11)</b>
</p>

<p>
11 elétrons para distribuir:
</p>
<ul class="org-ul">
<li>1s²: 2 elétrons (restam 9)</li>
<li>2s²: 2 elétrons (restam 7)</li>
<li>2p⁶: 6 elétrons (restam 1)</li>
<li>3s¹: 1 elétron</li>
</ul>

<p>
<b>Configuração:</b> 1s² 2s² 2p⁶ 3s¹
</p>

<p>
<b>Por camadas:</b> K=2, L=8, M=1
</p>

<p>
<b>Exemplo 2: Cloro (Cl, Z = 17)</b>
</p>

<p>
17 elétrons:
</p>
<ul class="org-ul">
<li>1s² 2s² 2p⁶ 3s² 3p⁵</li>
</ul>

<p>
<b>Por camadas:</b> K=2, L=8, M=7
</p>

<p>
<b>Exemplo 3: Cálcio (Ca, Z = 20)</b>
</p>

<p>
20 elétrons:
</p>
<ul class="org-ul">
<li>1s² 2s² 2p⁶ 3s² 3p⁶ 4s²</li>
</ul>

<p>
<b>Por camadas:</b> K=2, L=8, M=8, N=2
</p>
</div>
</div>
</div>

<div id="outline-container-org7993796" class="outline-4">
<h4 id="org7993796"><span class="section-number-4">3.3.8.</span> Camada de Valência</h4>
<div class="outline-text-4" id="text-3-3-8">
<p>
<b>Camada de valência</b> é a camada mais externa (última camada com elétrons).
</p>

<ul class="org-ul">
<li>Determina as propriedades químicas</li>
<li>Responsável pelas ligações químicas</li>
<li>Elétrons da última camada = elétrons de valência</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Na (K=2, L=8, M=1): 1 elétron de valência</li>
<li>Cl (K=2, L=8, M=7): 7 elétrons de valência</li>
<li>He (K=2): 2 elétrons de valência (camada completa)</li>
</ul>
</div>
</div>

<div id="outline-container-org7a23a9e" class="outline-4">
<h4 id="org7a23a9e"><span class="section-number-4">3.3.9.</span> Radioatividade</h4>
<div class="outline-text-4" id="text-3-3-9">
<p>
<b>Radioatividade</b> é a emissão espontânea de partículas e/ou energia por núcleos atômicos instáveis.
</p>
</div>

<div id="outline-container-orgbf6ac4d" class="outline-5">
<h5 id="orgbf6ac4d"><span class="section-number-5">3.3.9.1.</span> Descoberta</h5>
<div class="outline-text-5" id="text-3-3-9-1">
<ul class="org-ul">
<li><b>Henri Becquerel (1896):</b> Descobriu a radioatividade do urânio</li>
<li><b>Marie e Pierre Curie:</b> Isolaram rádio e polônio</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgaeb18b6" class="outline-4">
<h4 id="orgaeb18b6"><span class="section-number-4">3.3.10.</span> Tipos de Emissões Radioativas</h4>
<div class="outline-text-4" id="text-3-3-10">
</div>
<div id="outline-container-org5cab06f" class="outline-5">
<h5 id="org5cab06f"><span class="section-number-5">3.3.10.1.</span> 1. Partículas Alfa (α)</h5>
<div class="outline-text-5" id="text-3-3-10-1">
<p>
<b>Constituição:</b> Núcleo de hélio (²He₄)
</p>
<ul class="org-ul">
<li>2 prótons + 2 nêutrons</li>
<li>Carga: +2</li>
<li>Massa: 4 u</li>
</ul>

<p>
<b>Poder de penetração:</b> Baixo (barrada por folha de papel)
</p>

<p>
<b>Equação:</b>
</p>

<pre class="example" id="orgd5353a1">
 A         A-4           4
X    →    Y      +      He
 Z         Z-2           2
</pre>

<p>
<b>Exemplo:</b> ²³⁸U₉₂ → ²³⁴Th₉₀ + ⁴He₂
</p>

<ul class="org-ul">
<li>Perde 2 prótons (Z diminui 2)</li>
<li>Perde 2 nêutrons (A diminui 4)</li>
</ul>
</div>
</div>

<div id="outline-container-org2b6fe6c" class="outline-5">
<h5 id="org2b6fe6c"><span class="section-number-5">3.3.10.2.</span> 2. Partículas Beta (β)</h5>
<div class="outline-text-5" id="text-3-3-10-2">
<p>
<b>Constituição:</b> Elétron de alta energia (⁰e₋₁) ou pósitron (⁰e₊₁)
</p>

<p>
<b>Beta negativo (β⁻):</b>
</p>
<ul class="org-ul">
<li>Nêutron se transforma em próton + elétron</li>
<li>n⁰ → p⁺ + e⁻</li>
<li>Carga: -1</li>
<li>Massa: ~0</li>
</ul>

<p>
<b>Poder de penetração:</b> Médio (barrada por placa de alumínio)
</p>

<p>
<b>Equação:</b>
</p>

<pre class="example" id="org2fa390e">
 A         A          0
X    →    Y    +     e
 Z         Z+1       -1
</pre>

<p>
<b>Exemplo:</b> ¹⁴C₆ → ¹⁴N₇ + ⁰e₋₁
</p>

<ul class="org-ul">
<li>Ganha 1 próton (Z aumenta 1)</li>
<li>Perde 1 nêutron</li>
<li>A permanece igual</li>
</ul>

<p>
<b>Beta positivo (β⁺):</b>
</p>
<ul class="org-ul">
<li>Próton se transforma em nêutron + pósitron</li>
<li>Menos comum</li>
</ul>
</div>
</div>

<div id="outline-container-org6bf96c8" class="outline-5">
<h5 id="org6bf96c8"><span class="section-number-5">3.3.10.3.</span> 3. Raios Gama (γ)</h5>
<div class="outline-text-5" id="text-3-3-10-3">
<p>
<b>Constituição:</b> Radiação eletromagnética de alta energia
</p>

<ul class="org-ul">
<li>Sem massa</li>
<li>Sem carga</li>
<li>Acompanha emissões α ou β</li>
</ul>

<p>
<b>Poder de penetração:</b> Alto (atravessa a maioria dos materiais; barrada por chumbo grosso)
</p>

<p>
<b>Equação:</b>
</p>

<pre class="example" id="orgfa64a76">
 A         A
X*   →    X    +   γ
 Z         Z
</pre>

<p>
(* indica núcleo excitado)
</p>

<ul class="org-ul">
<li>Z e A não mudam</li>
<li>Apenas libera energia</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org5bafbd8" class="outline-4">
<h4 id="org5bafbd8"><span class="section-number-4">3.3.11.</span> Resumo das Emissões</h4>
<div class="outline-text-4" id="text-3-3-11">
<pre class="example" id="orgee942b2">
┌──────────┬─────────┬──────┬───────────────┬──────────────┐
│ Emissão  │ Símbolo │Carga │    Massa      │  Penetração  │
├──────────┼─────────┼──────┼───────────────┼──────────────┤
│ Alfa     │ ⁴He₂ (α)│  +2  │      4 u      │    Baixa     │
│ Beta (-)│ ⁰e₋₁ (β⁻)│  -1  │     ~0        │    Média     │
│ Gama     │    γ    │   0  │      0        │    Alta      │
└──────────┴─────────┴──────┴───────────────┴──────────────┘
</pre>
</div>
</div>

<div id="outline-container-orgfbc775a" class="outline-4">
<h4 id="orgfbc775a"><span class="section-number-4">3.3.12.</span> Leis da Radioatividade</h4>
<div class="outline-text-4" id="text-3-3-12">
</div>
<div id="outline-container-org95897f0" class="outline-5">
<h5 id="org95897f0"><span class="section-number-5">3.3.12.1.</span> Lei de Soddy (1ª Lei)</h5>
<div class="outline-text-5" id="text-3-3-12-1">
<p>
<b>Emissão alfa:</b> Z diminui 2, A diminui 4
</p>
</div>
</div>

<div id="outline-container-org7a28f58" class="outline-5">
<h5 id="org7a28f58"><span class="section-number-5">3.3.12.2.</span> Lei de Soddy-Fajans-Russell (2ª Lei)</h5>
<div class="outline-text-5" id="text-3-3-12-2">
<p>
<b>Emissão beta:</b> Z aumenta 1, A permanece igual
</p>
</div>
</div>
</div>

<div id="outline-container-org111953e" class="outline-4">
<h4 id="org111953e"><span class="section-number-4">3.3.13.</span> Meia-Vida (t₁/₂)</h4>
<div class="outline-text-4" id="text-3-3-13">
<p>
<b>Definição:</b> Tempo necessário para que metade dos átomos de uma amostra radioativa se desintegre.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org524e07f">
N = N₀ × (1/2)ⁿ

ou

N = N₀ × (1/2)^(t/t₁/₂)
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>N = quantidade final</li>
<li>N₀ = quantidade inicial</li>
<li>n = número de meias-vidas</li>
<li>t = tempo decorrido</li>
<li>t₁/₂ = meia-vida</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<p>
Uma amostra de 80 g de um isótopo radioativo com meia-vida de 10 anos. Quanto resta após 30 anos?
</p>

<p>
t/t₁/₂ = 30/10 = 3 meias-vidas
</p>

<p>
N = 80 × (1/2)³ N = 80 × 1/8 N = 10 g
</p>

<p>
<b>Evolução:</b>
</p>
<ul class="org-ul">
<li>0 anos: 80 g</li>
<li>10 anos (1 meia-vida): 40 g</li>
<li>20 anos (2 meias-vidas): 20 g</li>
<li>30 anos (3 meias-vidas): 10 g</li>
</ul>
</div>
</div>

<div id="outline-container-orgeef885e" class="outline-4">
<h4 id="orgeef885e"><span class="section-number-4">3.3.14.</span> Aplicações da Radioatividade</h4>
<div class="outline-text-4" id="text-3-3-14">
</div>
<div id="outline-container-org365050b" class="outline-5">
<h5 id="org365050b"><span class="section-number-5">3.3.14.1.</span> Medicina</h5>
<div class="outline-text-5" id="text-3-3-14-1">
<ul class="org-ul">
<li><b>Radioterapia:</b> Tratamento de câncer</li>
<li><b>Radiografia:</b> Diagnóstico por imagem</li>
<li><b>Medicina nuclear:</b> Traçadores radioativos (iodo-131 para tireoide)</li>
</ul>
</div>
</div>

<div id="outline-container-orgfae55e2" class="outline-5">
<h5 id="orgfae55e2"><span class="section-number-5">3.3.14.2.</span> Indústria</h5>
<div class="outline-text-5" id="text-3-3-14-2">
<ul class="org-ul">
<li><b>Esterilização:</b> Alimentos e equipamentos médicos</li>
<li><b>Medição de espessura:</b> Controle de qualidade</li>
</ul>
</div>
</div>

<div id="outline-container-org37cacad" class="outline-5">
<h5 id="org37cacad"><span class="section-number-5">3.3.14.3.</span> Datação</h5>
<div class="outline-text-5" id="text-3-3-14-3">
<ul class="org-ul">
<li><b>Carbono-14:</b> Datação de fósseis (até 50.000 anos)</li>
<li><b>Urânio-238:</b> Datação de rochas (milhões/bilhões de anos)</li>
</ul>
</div>
</div>

<div id="outline-container-org6161e6c" class="outline-5">
<h5 id="org6161e6c"><span class="section-number-5">3.3.14.4.</span> Energia</h5>
<div class="outline-text-5" id="text-3-3-14-4">
<ul class="org-ul">
<li><b>Usinas nucleares:</b> Geração de energia elétrica</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org2ff3136" class="outline-4">
<h4 id="org2ff3136"><span class="section-number-4">3.3.15.</span> Fissão e Fusão Nuclear</h4>
<div class="outline-text-4" id="text-3-3-15">
</div>
<div id="outline-container-org28528b7" class="outline-5">
<h5 id="org28528b7"><span class="section-number-5">3.3.15.1.</span> Fissão Nuclear</h5>
<div class="outline-text-5" id="text-3-3-15-1">
<p>
<b>Divisão de um núcleo pesado em núcleos menores, com liberação de energia</b>
</p>

<ul class="org-ul">
<li>Usado em usinas nucleares e bombas atômicas</li>
<li>Exemplo: ²³⁵U + nêutron → fragmentos + nêutrons + energia</li>
</ul>

<p>
<b>Reação em cadeia:</b> Nêutrons liberados causam novas fissões
</p>
</div>
</div>

<div id="outline-container-org8172861" class="outline-5">
<h5 id="org8172861"><span class="section-number-5">3.3.15.2.</span> Fusão Nuclear</h5>
<div class="outline-text-5" id="text-3-3-15-2">
<p>
<b>União de núcleos leves formando núcleo mais pesado, com liberação de energia</b>
</p>

<ul class="org-ul">
<li>Ocorre no Sol e estrelas</li>
<li>Fonte de energia das estrelas</li>
<li>Exemplo: ²H + ³H → ⁴He + nêutron + energia</li>
</ul>

<p>
<b>Energia liberada é maior que na fissão!</b>
</p>
</div>
</div>
</div>

<div id="outline-container-orgea40485" class="outline-4">
<h4 id="orgea40485"><span class="section-number-4">3.3.16.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-3-16">
</div>
<div id="outline-container-orgb555891" class="outline-5">
<h5 id="orgb555891"><span class="section-number-5">3.3.16.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-3-16-1">
<p>
Um átomo possui 17 prótons, 18 nêutrons e 17 elétrons. Determine: a) Número atômico (Z) b) Número de massa (A) c) Representação
</p>

<p>
<b>Solução:</b> a) Z = número de prótons = 17 b) A = Z + N = 17 + 18 = 35 c) ³⁵Cl₁₇ (Cloro-35)
</p>
</div>
</div>

<div id="outline-container-org7c73d28" class="outline-5">
<h5 id="org7c73d28"><span class="section-number-5">3.3.16.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-3-16-2">
<p>
O íon Ca²⁺ possui 20 prótons. Quantos elétrons possui?
</p>

<p>
<b>Solução:</b> Cátion +2 = perdeu 2 elétrons
</p>

<p>
Átomo neutro: 20 prótons, 20 elétrons Ca²⁺: 20 prótons, 18 elétrons
</p>

<p>
<i>[Ver resposta 55 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org75e1ed2" class="outline-5">
<h5 id="org75e1ed2"><span class="section-number-5">3.3.16.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-3-16-3">
<p>
Faça a distribuição eletrônica do Oxigênio (O, Z = 8).
</p>

<p>
<b>Solução:</b> 8 elétrons: 1s² 2s² 2p⁴
</p>

<p>
<b>Por camadas:</b> K=2, L=6
</p>

<p>
<b>Elétrons de valência:</b> 6 (camada L)
</p>
</div>
</div>

<div id="outline-container-org15c1d96" class="outline-5">
<h5 id="org15c1d96"><span class="section-number-5">3.3.16.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-3-16-4">
<p>
Identifique o tipo de relação entre: a) ¹²C₆ e ¹⁴C₆ b) ⁴⁰K₁₉ e ⁴⁰Ca₂₀ c) ¹⁴C₆ e ¹⁵N₇
</p>

<p>
<b>Solução:</b> a) Mesmo Z (6), diferente A → <b>Isótopos</b> b) Diferente Z, mesmo A (40) → <b>Isóbaros</b> c) Z=6 (8n), Z=7 (8n) → mesmo N=8 → <b>Isótonos</b>
</p>
</div>
</div>

<div id="outline-container-org8222af9" class="outline-5">
<h5 id="org8222af9"><span class="section-number-5">3.3.16.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-3-3-16-5">
<p>
Complete a equação: ²³⁸U₉₂ → ? + ⁴He₂
</p>

<p>
<b>Solução:</b> Emissão alfa (perde 2p e 2n):
</p>

<p>
Z: 92
</p>
<ul class="org-ul">
<li>2 = 90 A: 238</li>
<li>4 = 234</li>
</ul>

<p>
<i>[Ver resposta 56 no final do documento]</i>
</p>

<p>
Equação completa: ²³⁸U₉₂ → ²³⁴Th₉₀ + ⁴He₂
</p>
</div>
</div>

<div id="outline-container-orgbe9eb44" class="outline-5">
<h5 id="orgbe9eb44"><span class="section-number-5">3.3.16.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-3-3-16-6">
<p>
Complete: ¹⁴C₆ → ? + ⁰e₋₁
</p>

<p>
<b>Solução:</b> Emissão beta (ganha 1p):
</p>

<p>
Z: 6 + 1 = 7 A: 14 (permanece)
</p>

<p>
<i>[Ver resposta 57 no final do documento]</i>
</p>

<p>
Equação: ¹⁴C₆ → ¹⁴N₇ + ⁰e₋₁
</p>
</div>
</div>

<div id="outline-container-orgebf68fb" class="outline-5">
<h5 id="orgebf68fb"><span class="section-number-5">3.3.16.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-3-3-16-7">
<p>
Uma amostra de 100 g de um elemento radioativo tem meia-vida de 5 anos. Qual a massa após 15 anos?
</p>

<p>
<b>Solução:</b> n = t/t₁/₂ = 15/5 = 3 meias-vidas
</p>

<p>
N = 100 × (1/2)³ N = 100 × 1/8 N = 12,5 g
</p>

<p>
<i>[Ver resposta 58 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf849709" class="outline-5">
<h5 id="orgf849709"><span class="section-number-5">3.3.16.8.</span> Exercício 8</h5>
<div class="outline-text-5" id="text-3-3-16-8">
<p>
Calcule a massa atômica do cloro, sabendo que na natureza há 75% de ³⁵Cl e 25% de ³⁷Cl.
</p>

<p>
<b>Solução:</b> MA = (35 × 75 + 37 × 25) / 100 MA = (2625 + 925) / 100 MA = 3550 / 100 MA = 35,5 u
</p>

<p>
<i>[Ver resposta 59 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org71e71ee" class="outline-4">
<h4 id="org71e71ee"><span class="section-number-4">3.3.17.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-3-17">
<ol class="org-ol">
<li><b>Número atômico (Z)</b> define o elemento</li>
<li>não muda em íons</li>
<li><b>Íons:</b> Cátion perde e⁻, ânion ganha e⁻</li>
<li><b>Isótopos:</b> Mesmo elemento, massas diferentes (Ex: C-12, C-14)</li>
<li><b>Distribuição eletrônica:</b> Siga a ordem de Pauling</li>
<li><b>Alfa:</b> perde 2p e 2n (Z-2, A-4)</li>
<li><b>Beta:</b> ganha 1p (Z+1, A igual)</li>
<li><b>Gama:</b> só energia (Z e A não mudam)</li>
<li><b>Meia-vida:</b> N = N₀ × (1/2)ⁿ</li>
<li><b>Conversões:</b> 1 u ≈ 1,66 × 10⁻²⁴ g</li>
</ol>
</div>
</div>

<div id="outline-container-org53ad6f1" class="outline-4">
<h4 id="org53ad6f1"><span class="section-number-4">3.3.18.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-3-18">
<p>
<b>Estrutura atômica:</b>
</p>
<ul class="org-ul">
<li>Prótons: +1, no núcleo</li>
<li>Nêutrons: 0, no núcleo</li>
<li>Elétrons: -1, na eletrosfera</li>
<li>Z = prótons = elétrons (átomo neutro)</li>
<li>A = prótons + nêutrons</li>
</ul>

<p>
<b>Íons:</b>
</p>
<ul class="org-ul">
<li>Cátion: perdeu e⁻ (carga +)</li>
<li>Ânion: ganhou e⁻ (carga -)</li>
</ul>

<p>
<b>ISO:</b>
</p>
<ul class="org-ul">
<li>Isótopos: mesmo Z</li>
<li>Isóbaros: mesmo A</li>
<li>Isótonos: mesmo N</li>
</ul>

<p>
<b>Radioatividade:</b>
</p>
<ul class="org-ul">
<li>α: ⁴He₂ (perde 2p, 2n)</li>
<li>β⁻: ⁰e₋₁ (ganha 1p)</li>
<li>γ: energia (sem mudança)</li>
</ul>
</div>
</div>

<div id="outline-container-orgef7a2c3" class="outline-4">
<h4 id="orgef7a2c3"><span class="section-number-4">3.3.19.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-3-19">
<pre class="example" id="orga9b35cd">
Estrutura Atômica:

A = Z + N

N = A
- Z

Z = prótons = elétrons (átomo neutro)

Distribuição eletrônica:
Máximo por camada = 2n²

Radioatividade:

Emissão alfa:
  A         A-4           4
 X    →    Y      +      He
  Z         Z-2           2

Emissão beta:
  A         A          0
 X    →    Y    +     e
  Z         Z+1       -1

Meia-vida:
N = N₀ × (1/2)ⁿ

ou

N = N₀ × (1/2)^(t/t₁/₂)

Massa atômica (isótopos):
MA = Σ(massa × abundância) / 100
</pre>
</div>
</div>

<div id="outline-container-org1292876" class="outline-4">
<h4 id="org1292876"><span class="section-number-4">3.3.20.</span> Tabela Resumo</h4>
<div class="outline-text-4" id="text-3-3-20">
<ul class="org-ul">
<li>Partículas</li>
</ul>
<pre class="example" id="org602b45a">
┌────────────┬────────┬────────┬──────────────┐
│ Partícula  │ Carga  │  Massa │ Localização  │
├────────────┼────────┼────────┼──────────────┤
│ Próton     │   +1   │   1 u  │   Núcleo     │
│ Nêutron    │    0   │   1 u  │   Núcleo     │
│ Elétron    │   -1   │  ~0    │ Eletrosfera  │
└────────────┴────────┴────────┴──────────────┘

┌────────────┬────────┬────────┬──────────────┐
│  Emissão   │ Carga  │  Massa │  Penetração  │
├────────────┼────────┼────────┼──────────────┤
│ Alfa (α)   │   +2   │   4 u  │    Baixa     │
│ Beta (β⁻)  │   -1   │   ~0   │    Média     │
│ Gama (γ)   │    0   │    0   │    Alta      │
└────────────┴────────┴────────┴──────────────┘
</pre>
</div>
</div>

<div id="outline-container-org4843b5c" class="outline-4">
<h4 id="org4843b5c"><span class="section-number-4">3.3.21.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-3-3-21">
<p>
<b>Medicina:</b>
</p>
<ul class="org-ul">
<li>Iodo-131: Tratamento de tireoide</li>
<li>Cobalto-60: Radioterapia</li>
<li>Tecnécio-99m: Diagnóstico por imagem</li>
</ul>

<p>
<b>Datação:</b>
</p>
<ul class="org-ul">
<li>C-14: Fósseis (meia-vida 5.730 anos)</li>
<li>U-238: Rochas (meia-vida 4,5 bilhões de anos)</li>
</ul>

<p>
<b>Energia:</b>
</p>
<ul class="org-ul">
<li>Fissão de U-235: Usinas nucleares</li>
<li>Fusão: Energia do Sol</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para tabela periódica e ligações químicas)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org0b1c398" class="outline-3">`;

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
