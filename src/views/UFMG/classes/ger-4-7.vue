<script setup lang="ts">
import { ref } from "vue";

const code = "ger-4-7";
const title = "Química: Propriedades das Substâncias";
const subject = "geral";
const themes = [];
const dates = ["2025-12-14"];
const lessonContent = `<div class="outline-text-3" id="text-1-4">
<ul class="org-ul">
<li>Química: Propriedades das Substâncias</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org05a48b4" class="outline-4">
<h4 id="org05a48b4"><span class="section-number-4">1.4.1.</span> O que são Propriedades das Substâncias?</h4>
<div class="outline-text-4" id="text-1-4-1">
<p>
As <b>propriedades das substâncias</b> são características que permitem identificar, diferenciar e classificar diferentes materiais. Dividem-se em:
</p>

<ul class="org-ul">
<li><b>Propriedades físicas:</b> podem ser observadas sem alterar a composição da substância</li>
<li><b>Propriedades químicas:</b> relacionadas ao comportamento da substância em reações químicas</li>
</ul>
</div>
</div>

<div id="outline-container-org9f797df" class="outline-4">
<h4 id="org9f797df"><span class="section-number-4">1.4.2.</span> Propriedades Físicas Gerais</h4>
<div class="outline-text-4" id="text-1-4-2">
<p>
São propriedades comuns a toda matéria, independente da substância:
</p>
</div>

<div id="outline-container-org5982d83" class="outline-5">
<h5 id="org5982d83"><span class="section-number-5">1.4.2.1.</span> Massa</h5>
<div class="outline-text-5" id="text-1-4-2-1">
<ul class="org-ul">
<li>Quantidade de matéria de um corpo</li>
<li>Unidade SI: quilograma (kg)</li>
<li>Não varia com a localização</li>
</ul>
</div>
</div>

<div id="outline-container-org218af07" class="outline-5">
<h5 id="org218af07"><span class="section-number-5">1.4.2.2.</span> Volume</h5>
<div class="outline-text-5" id="text-1-4-2-2">
<ul class="org-ul">
<li>Espaço ocupado por um corpo</li>
<li>Unidade SI: metro cúbico (m³)</li>
<li>Também: litro (L), mililitro (mL)</li>
<li>1 L = 1000 mL = 1 dm³ = 0,001 m³</li>
</ul>
</div>
</div>

<div id="outline-container-orgf4872d8" class="outline-5">
<h5 id="orgf4872d8"><span class="section-number-5">1.4.2.3.</span> Inércia</h5>
<div class="outline-text-5" id="text-1-4-2-3">
<ul class="org-ul">
<li>Tendência de um corpo manter seu estado de movimento ou repouso</li>
<li>Relacionada à massa (quanto maior a massa, maior a inércia)</li>
</ul>
</div>
</div>

<div id="outline-container-orgd41b307" class="outline-5">
<h5 id="orgd41b307"><span class="section-number-5">1.4.2.4.</span> Impenetrabilidade</h5>
<div class="outline-text-5" id="text-1-4-2-4">
<ul class="org-ul">
<li>Dois corpos não podem ocupar o mesmo lugar no espaço ao mesmo tempo</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org594fc4c" class="outline-4">
<h4 id="org594fc4c"><span class="section-number-4">1.4.3.</span> Propriedades Físicas Específicas</h4>
<div class="outline-text-4" id="text-1-4-3">
<p>
São características particulares de cada substância, usadas para identificação:
</p>
</div>
</div>

<div id="outline-container-orgfc50ccd" class="outline-4">
<h4 id="orgfc50ccd"><span class="section-number-4">1.4.4.</span> 1. Densidade (d ou ρ)</h4>
<div class="outline-text-4" id="text-1-4-4">
<p>
<b>Definição:</b> Relação entre a massa e o volume de uma substância.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org95371c9">
d = m / V
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>d = densidade</li>
<li>m = massa</li>
<li>V = volume</li>
</ul>

<p>
<b>Unidades comuns:</b>
</p>
<ul class="org-ul">
<li>g/cm³</li>
<li>kg/m³</li>
<li>g/mL</li>
</ul>

<p>
<b>Conversão:</b> 1 g/cm³ = 1 g/mL = 1000 kg/m³
</p>

<p>
<b>Exemplos de densidades (a 20°C):</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Substância</th>
<th scope="col" class="org-left">Densidade (g/cm³)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Ouro</td>
<td class="org-left">19,3</td>
</tr>

<tr>
<td class="org-left">Chumbo</td>
<td class="org-left">11,3</td>
</tr>

<tr>
<td class="org-left">Ferro</td>
<td class="org-left">7,87</td>
</tr>

<tr>
<td class="org-left">Alumínio</td>
<td class="org-left">2,70</td>
</tr>

<tr>
<td class="org-left">Água</td>
<td class="org-left">1,00</td>
</tr>

<tr>
<td class="org-left">Gelo</td>
<td class="org-left">0,92</td>
</tr>

<tr>
<td class="org-left">Etanol</td>
<td class="org-left">0,79</td>
</tr>

<tr>
<td class="org-left">Gasolina</td>
<td class="org-left">0,70</td>
</tr>

<tr>
<td class="org-left">Ar</td>
<td class="org-left">0,0013</td>
</tr>
</tbody>
</table>

<p>
<b>Observações importantes:</b>
</p>
<ul class="org-ul">
<li>A densidade da água é 1 g/cm³ (referência)</li>
<li>Substâncias com d &lt; 1 g/cm³ flutuam na água</li>
<li>Substâncias com d &gt; 1 g/cm³ afundam na água</li>
<li>O gelo flutua porque d(gelo) &lt; d(água)</li>
</ul>
</div>

<div id="outline-container-org4614148" class="outline-5">
<h5 id="org4614148"><span class="section-number-5">1.4.4.1.</span> Exemplo 1</h5>
<div class="outline-text-5" id="text-1-4-4-1">
<p>
Um bloco de ferro tem massa 78,7 g e volume 10 cm³. Qual sua densidade?
</p>

<p>
<b>Solução:</b> d = m / V = 78,7 g / 10 cm³ = 7,87 g/cm³
</p>
</div>
</div>

<div id="outline-container-org1078c5b" class="outline-5">
<h5 id="org1078c5b"><span class="section-number-5">1.4.4.2.</span> Exemplo 2</h5>
<div class="outline-text-5" id="text-1-4-4-2">
<p>
Qual a massa de 500 mL de etanol? (d = 0,79 g/mL)
</p>

<p>
<b>Solução:</b> d = m / V 0,79 = m / 500 m = 0,79 × 500 = 395 g
</p>
</div>
</div>

<div id="outline-container-org7af7bf9" class="outline-5">
<h5 id="org7af7bf9"><span class="section-number-5">1.4.4.3.</span> Exemplo 3</h5>
<div class="outline-text-5" id="text-1-4-4-3">
<p>
Um cubo de gelo (d = 0,92 g/cm³) flutua ou afunda na água?
</p>

<p>
<i>[Ver resposta 17 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgec36ce8" class="outline-4">
<h4 id="orgec36ce8"><span class="section-number-4">1.4.5.</span> 2. Temperatura de Fusão (TF ou PF)</h4>
<div class="outline-text-4" id="text-1-4-5">
<p>
<b>Definição:</b> Temperatura na qual uma substância pura passa do estado sólido para o líquido (ou vice-versa).
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Específica para cada substância pura</li>
<li>Permanece constante durante toda a fusão</li>
<li>À pressão de 1 atm (nível do mar)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Substância</th>
<th scope="col" class="org-right">TF (°C) a 1 atm</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Tungstênio</td>
<td class="org-right">3422</td>
</tr>

<tr>
<td class="org-left">Ferro</td>
<td class="org-right">1535</td>
</tr>

<tr>
<td class="org-left">Ouro</td>
<td class="org-right">1064</td>
</tr>

<tr>
<td class="org-left">Alumínio</td>
<td class="org-right">660</td>
</tr>

<tr>
<td class="org-left">Chumbo</td>
<td class="org-right">327</td>
</tr>

<tr>
<td class="org-left">Água</td>
<td class="org-right">0</td>
</tr>

<tr>
<td class="org-left">Mercúrio</td>
<td class="org-right">-39</td>
</tr>

<tr>
<td class="org-left">Etanol</td>
<td class="org-right">-114</td>
</tr>
</tbody>
</table>

<p>
<b>Curva de aquecimento:</b>
</p>

<pre class="example" id="org6212df2">
Temperatura
   ↑
   |     Líquido
   |----------------
TF |     Fusão (platô)
   |----------------
   |     Sólido
   |________________→ Tempo
</pre>

<p>
<b>Observações:</b>
</p>
<ul class="org-ul">
<li>Durante a fusão, T permanece constante</li>
<li>Substâncias puras têm TF definida</li>
<li>Misturas fundem em faixa de temperatura</li>
</ul>
</div>
</div>

<div id="outline-container-orgb1d071e" class="outline-4">
<h4 id="orgb1d071e"><span class="section-number-4">1.4.6.</span> 3. Temperatura de Ebulição (TE ou PE)</h4>
<div class="outline-text-4" id="text-1-4-6">
<p>
<b>Definição:</b> Temperatura na qual uma substância passa do estado líquido para o gasoso com formação de bolhas em todo o líquido.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Específica para cada substância pura</li>
<li>Permanece constante durante toda a ebulição</li>
<li>Varia com a pressão (menor pressão → menor TE)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Substância</th>
<th scope="col" class="org-right">TE (°C) a 1 atm</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Água</td>
<td class="org-right">100</td>
</tr>

<tr>
<td class="org-left">Etanol</td>
<td class="org-right">78</td>
</tr>

<tr>
<td class="org-left">Acetona</td>
<td class="org-right">56</td>
</tr>

<tr>
<td class="org-left">Éter</td>
<td class="org-right">35</td>
</tr>

<tr>
<td class="org-left">Mercúrio</td>
<td class="org-right">357</td>
</tr>

<tr>
<td class="org-left">Ferro</td>
<td class="org-right">2750</td>
</tr>

<tr>
<td class="org-left">Ouro</td>
<td class="org-right">2856</td>
</tr>

<tr>
<td class="org-left">Oxigênio</td>
<td class="org-right">-183</td>
</tr>

<tr>
<td class="org-left">Nitrogênio</td>
<td class="org-right">-196</td>
</tr>
</tbody>
</table>

<p>
<b>Influência da altitude:</b>
</p>
<ul class="org-ul">
<li>Quanto maior a altitude, menor a pressão atmosférica</li>
<li>Menor pressão → menor temperatura de ebulição</li>
<li>No nível do mar: água ferve a 100°C</li>
<li>A 3000 m de altitude: água ferve a ~90°C</li>
</ul>

<p>
<b>Evaporação vs Ebulição:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Evaporação</th>
<th scope="col" class="org-left">Ebulição</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Ocorre na superfície</td>
<td class="org-left">Ocorre em todo o líquido</td>
</tr>

<tr>
<td class="org-left">Qualquer temperatura</td>
<td class="org-left">Temperatura específica</td>
</tr>

<tr>
<td class="org-left">Processo lento</td>
<td class="org-left">Processo rápido</td>
</tr>

<tr>
<td class="org-left">Sem bolhas</td>
<td class="org-left">Com bolhas</td>
</tr>
</tbody>
</table>
</div>
</div>

<div id="outline-container-org55e2176" class="outline-4">
<h4 id="org55e2176"><span class="section-number-4">1.4.7.</span> 4. Solubilidade</h4>
<div class="outline-text-4" id="text-1-4-7">
<p>
<b>Definição:</b> Capacidade de uma substância (soluto) se dissolver em outra (solvente) a uma dada temperatura.
</p>

<p>
<b>Unidades comuns:</b>
</p>
<ul class="org-ul">
<li>g soluto / 100 g solvente</li>
<li>g/L</li>
<li>mol/L</li>
</ul>

<p>
<b>Coeficiente de solubilidade (Cs):</b> Quantidade máxima de soluto que dissolve em 100 g de solvente a determinada temperatura.
</p>

<p>
<b>Classificação das soluções:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Tipo</th>
<th scope="col" class="org-left">Característica</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left"><b>Insaturada</b></td>
<td class="org-left">Quantidade de soluto &lt; Cs (pode dissolver mais)</td>
</tr>

<tr>
<td class="org-left"><b>Saturada</b></td>
<td class="org-left">Quantidade de soluto = Cs (equilíbrio)</td>
</tr>

<tr>
<td class="org-left"><b>Supersaturada</b></td>
<td class="org-left">Quantidade de soluto &gt; Cs (instável)</td>
</tr>
</tbody>
</table>

<p>
<b>Exemplos de solubilidade em água (20°C):</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Substância</th>
<th scope="col" class="org-right">Solubilidade (g/100g H₂O)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">NaCl (sal)</td>
<td class="org-right">36</td>
</tr>

<tr>
<td class="org-left">Açúcar</td>
<td class="org-right">200</td>
</tr>

<tr>
<td class="org-left">KNO₃</td>
<td class="org-right">32</td>
</tr>

<tr>
<td class="org-left">CaCO₃</td>
<td class="org-right">0,0013 (pouco solúvel)</td>
</tr>
</tbody>
</table>

<p>
<b>Fatores que afetam a solubilidade:</b>
</p>
</div>

<div id="outline-container-orgaf3afa8" class="outline-5">
<h5 id="orgaf3afa8"><span class="section-number-5">1.4.7.1.</span> Temperatura</h5>
<div class="outline-text-5" id="text-1-4-7-1">
<ul class="org-ul">
<li><b>Sólidos em líquidos:</b> geralmente aumenta com a temperatura</li>
<li><b>Gases em líquidos:</b> diminui com a temperatura</li>
</ul>
</div>
</div>

<div id="outline-container-orgdf98c6c" class="outline-5">
<h5 id="orgdf98c6c"><span class="section-number-5">1.4.7.2.</span> Natureza do soluto e solvente</h5>
<div class="outline-text-5" id="text-1-4-7-2">
<ul class="org-ul">
<li><b>“Semelhante dissolve semelhante”</b></li>
<li>Polar dissolve polar</li>
<li>Apolar dissolve apolar</li>
<li>Exemplos:
<ul class="org-ul">
<li>Água (polar) dissolve sal (polar) ✓</li>
<li>Água (polar) NÃO dissolve óleo (apolar) ✗</li>
<li>Gasolina (apolar) dissolve óleo (apolar) ✓</li>
</ul></li>
</ul>
</div>
</div>

<div id="outline-container-org6542e14" class="outline-5">
<h5 id="org6542e14"><span class="section-number-5">1.4.7.3.</span> Pressão (para gases)</h5>
<div class="outline-text-5" id="text-1-4-7-3">
<ul class="org-ul">
<li>Aumenta a pressão → aumenta a solubilidade de gases</li>
<li>Lei de Henry</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org20d5ef8" class="outline-4">
<h4 id="org20d5ef8"><span class="section-number-4">1.4.8.</span> Outras Propriedades Físicas Importantes</h4>
<div class="outline-text-4" id="text-1-4-8">
</div>
<div id="outline-container-org2ce4a3c" class="outline-5">
<h5 id="org2ce4a3c"><span class="section-number-5">1.4.8.1.</span> Ponto de Congelamento</h5>
<div class="outline-text-5" id="text-1-4-8-1">
<ul class="org-ul">
<li>Temperatura na qual líquido passa a sólido</li>
<li>Para substâncias puras: PF = PC (ponto de fusão = ponto de congelamento)</li>
</ul>
</div>
</div>

<div id="outline-container-org5565c16" class="outline-5">
<h5 id="org5565c16"><span class="section-number-5">1.4.8.2.</span> Viscosidade</h5>
<div class="outline-text-5" id="text-1-4-8-2">
<ul class="org-ul">
<li>Resistência ao escoamento</li>
<li>Mel &gt; água &gt; álcool</li>
</ul>
</div>
</div>

<div id="outline-container-org58b80c6" class="outline-5">
<h5 id="org58b80c6"><span class="section-number-5">1.4.8.3.</span> Dureza</h5>
<div class="outline-text-5" id="text-1-4-8-3">
<ul class="org-ul">
<li>Resistência ao risco</li>
<li>Escala de Mohs (1 a 10)</li>
<li>Diamante: 10 (mais duro)</li>
<li>Talco: 1 (menos duro)</li>
</ul>
</div>
</div>

<div id="outline-container-org867f1d0" class="outline-5">
<h5 id="org867f1d0"><span class="section-number-5">1.4.8.4.</span> Maleabilidade</h5>
<div class="outline-text-5" id="text-1-4-8-4">
<ul class="org-ul">
<li>Capacidade de ser transformado em lâminas</li>
<li>Ouro é muito maleável</li>
</ul>
</div>
</div>

<div id="outline-container-orgdc3bd3d" class="outline-5">
<h5 id="orgdc3bd3d"><span class="section-number-5">1.4.8.5.</span> Ductilidade</h5>
<div class="outline-text-5" id="text-1-4-8-5">
<ul class="org-ul">
<li>Capacidade de ser transformado em fios</li>
<li>Cobre é muito dúctil</li>
</ul>
</div>
</div>

<div id="outline-container-orgead05c7" class="outline-5">
<h5 id="orgead05c7"><span class="section-number-5">1.4.8.6.</span> Cor e Brilho</h5>
<div class="outline-text-5" id="text-1-4-8-6">
<ul class="org-ul">
<li>Características visuais</li>
<li>Podem ajudar na identificação</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgec639db" class="outline-4">
<h4 id="orgec639db"><span class="section-number-4">1.4.9.</span> Substância Pura vs Mistura</h4>
<div class="outline-text-4" id="text-1-4-9">
<p>
<b>Substância Pura:</b>
</p>
<ul class="org-ul">
<li>Composição fixa e definida</li>
<li>Propriedades físicas constantes</li>
<li>TF e TE constantes durante as mudanças de estado</li>
<li>Exemplos: H₂O, NaCl, Fe, O₂</li>
</ul>

<p>
<b>Mistura:</b>
</p>
<ul class="org-ul">
<li>Composição variável</li>
<li>Propriedades dependem da proporção</li>
<li>TF e TE variam durante as mudanças de estado</li>
<li>Exemplos: ar, água do mar, sangue, gasolina</li>
</ul>

<p>
<b>Gráficos de mudança de estado:</b>
</p>

<pre class="example" id="org0230fbc">
Substância Pura:           Mistura:
T ↑                        T ↑
  |    Vapor                 |      Vapor
  |____                      |  ____/
  | Eb                       | /Ebulição
  |____                      |/
  | Líquido                  |   Líquido
  |____                      |____
  | Fu                       | ___/
  |____                      |/Fusão
  | Sólido                   | Sólido
  |_____→ tempo              |_____→ tempo
  
 Platôs constantes       Faixas de temperatura
</pre>
</div>
</div>

<div id="outline-container-orge4c03f3" class="outline-4">
<h4 id="orge4c03f3"><span class="section-number-4">1.4.10.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-1-4-10">
</div>
<div id="outline-container-org4f96385" class="outline-5">
<h5 id="org4f96385"><span class="section-number-5">1.4.10.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-1-4-10-1">
<p>
Um objeto de 200 g ocupa volume de 25 cm³. Calcule sua densidade e identifique o material (consulte a tabela).
</p>

<p>
<b>Solução:</b> d = m / V = 200 g / 25 cm³ = 8 g/cm³
</p>

<p>
Consultando a tabela: densidade próxima ao ferro (7,87 g/cm³). <i>[Ver resposta 18 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org67ed3db" class="outline-5">
<h5 id="org67ed3db"><span class="section-number-5">1.4.10.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-1-4-10-2">
<p>
Quantos gramas de sal (NaCl) podem ser dissolvidos em 500 g de água a 20°C? (Cs = 36 g/100g H₂O)
</p>

<p>
<b>Solução:</b> Se 100 g H₂O dissolvem 36 g NaCl 500 g H₂O dissolvem x g NaCl
</p>

<p>
x = (500 × 36) / 100 = 180 g
</p>

<p>
<i>[Ver resposta 19 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb5bbe2b" class="outline-5">
<h5 id="orgb5bbe2b"><span class="section-number-5">1.4.10.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-1-4-10-3">
<p>
Qual a massa de 2 L de gasolina? (d = 0,70 g/mL)
</p>

<p>
<b>Solução:</b> 2 L = 2000 mL
</p>

<p>
d = m / V 0,70 = m / 2000 m = 0,70 × 2000 = 1400 g = 1,4 kg
</p>

<p>
<i>[Ver resposta 20 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb19200d" class="outline-5">
<h5 id="orgb19200d"><span class="section-number-5">1.4.10.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-1-4-10-4">
<p>
Por que o gelo flutua na água?
</p>

<p>
<i>[Ver resposta 21 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org65ae1a6" class="outline-5">
<h5 id="org65ae1a6"><span class="section-number-5">1.4.10.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-1-4-10-5">
<p>
Em uma cidade a 1500 m de altitude, a água ferve antes ou depois de 100°C?
</p>

<p>
<i>[Ver resposta 22 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org05ba6fd" class="outline-4">
<h4 id="org05ba6fd"><span class="section-number-4">1.4.11.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-1-4-11">
<ol class="org-ol">
<li><b>Densidade:</b> Memorize que água = 1 g/cm³ (referência)</li>
<li><b>Flutuação:</b> d &lt; d(água) = flutua; d &gt; d(água) = afunda</li>
<li><b>Conversões:</b> 1 g/cm³ = 1 g/mL; 1 L = 1000 mL</li>
<li><b>TF e TE:</b> Substâncias puras têm valores constantes; misturas têm faixas</li>
<li><b>Solubilidade:</b> Geralmente aumenta com temperatura (sólidos); diminui com temperatura (gases)</li>
<li><b>Semelhante dissolve semelhante:</b> polar + polar; apolar + apolar</li>
<li><b>Altitude:</b> Maior altitude → menor TE da água</li>
</ol>
</div>
</div>

<div id="outline-container-orgc531730" class="outline-4">
<h4 id="orgc531730"><span class="section-number-4">1.4.12.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-1-4-12">
<p>
<b>Densidade:</b>
</p>
<ul class="org-ul">
<li>d = m / V</li>
<li>Água = 1 g/cm³</li>
<li>d &lt; 1 → flutua</li>
<li>d &gt; 1 → afunda</li>
</ul>

<p>
<b>Temperaturas de mudança de estado:</b>
</p>
<ul class="org-ul">
<li><b>TF (fusão):</b> sólido ↔ líquido</li>
<li><b>TE (ebulição):</b> líquido → vapor</li>
<li>Substância pura: T constante</li>
<li>Mistura: faixa de T</li>
</ul>

<p>
<b>Solubilidade:</b>
</p>
<ul class="org-ul">
<li>Sólidos: ↑ T → ↑ solubilidade</li>
<li>Gases: ↑ T → ↓ solubilidade</li>
<li>Polar dissolve polar</li>
<li>Apolar dissolve apolar</li>
</ul>
</div>
</div>

<div id="outline-container-orga69f7df" class="outline-4">
<h4 id="orga69f7df"><span class="section-number-4">1.4.13.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-1-4-13">
<pre class="example" id="org2540516">
Densidade:
d = m / V

Conversões:
1 g/cm³ = 1 g/mL = 1000 kg/m³
1 L = 1000 mL = 1 dm³

Solubilidade:
Cs = massa do soluto / massa do solvente × 100
(geralmente em g soluto / 100 g solvente)

Água:
- d = 1 g/cm³ (líquida a 4°C)
- TF = 0°C (a 1 atm)
- TE = 100°C (a 1 atm)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>cai frequentemente em questões contextualizadas)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgd9342e1" class="outline-3">`;

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
