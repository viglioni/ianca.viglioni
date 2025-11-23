<script setup lang="ts">
import { ref } from "vue";

const code = "qui-23";
const title = "Química: Propriedades Periódicas";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-3">
<ul class="org-ul">
<li>Química: Propriedades Periódicas</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org310a0c2" class="outline-4">
<h4 id="org310a0c2"><span class="section-number-4">5.3.1.</span> Revisão: Tabela Periódica</h4>
<div class="outline-text-4" id="text-5-3-1">
<p>
Na Aula 18, estudamos a organização da Tabela Periódica:
</p>
<ul class="org-ul">
<li>Períodos (linhas): indicam número de camadas</li>
<li>Famílias/Grupos (colunas): indicam elétrons de valência</li>
<li>Classificação: metais, não-metais, semimetais, gases nobres</li>
</ul>

<p>
<b>Nesta aula:</b> propriedades que variam periodicamente na tabela.
</p>
</div>
</div>

<div id="outline-container-org6a0e4e8" class="outline-4">
<h4 id="org6a0e4e8"><span class="section-number-4">5.3.2.</span> O que são Propriedades Periódicas?</h4>
<div class="outline-text-4" id="text-5-3-2">
<p>
<b>Propriedades Periódicas</b> são características dos elementos que variam de forma regular conforme a posição na Tabela Periódica.
</p>

<p>
<b>Variam conforme:</b>
</p>
<ul class="org-ul">
<li>Número atômico (Z)</li>
<li>Período (número de camadas)</li>
<li>Família (elétrons de valência)</li>
</ul>

<p>
<b>Principais propriedades periódicas:</b> 1. Raio Atômico 2. Energia de Ionização 3. Afinidade Eletrônica 4. Eletronegatividade 5. Eletropositividade (Caráter Metálico)
</p>
</div>
</div>

<div id="outline-container-orgb45d968" class="outline-4">
<h4 id="orgb45d968"><span class="section-number-4">5.3.3.</span> 1. Raio Atômico</h4>
<div class="outline-text-4" id="text-5-3-3">
<p>
<b>Definição:</b> medida do tamanho do átomo (distância do núcleo até a eletrosfera mais externa).
</p>

<p>
<b>Unidade:</b> picômetro (pm) ou ångström (Å)
</p>
<ul class="org-ul">
<li>1 Å = 10⁻¹⁰ m = 100 pm</li>
</ul>
</div>

<div id="outline-container-org49b2db6" class="outline-5">
<h5 id="org49b2db6"><span class="section-number-5">5.3.3.1.</span> Variação na Tabela Periódica</h5>
<div class="outline-text-5" id="text-5-3-3-1">
<p>
*Na mesma família (coluna)
</p>
<ul class="org-ul">
<li>de cima para baixo:*</li>
</ul>

<pre class="example" id="orgbc9b96b">
AUMENTA ↓
</pre>

<p>
<b>Por quê?</b>
</p>
<ul class="org-ul">
<li>Mais camadas eletrônicas</li>
<li>Elétrons mais distantes do núcleo</li>
</ul>

<p>
<b>Exemplo:</b> Família 1 (Alcalinos)
</p>
<ul class="org-ul">
<li>Li (2 camadas) &lt; Na (3 camadas) &lt; K (4 camadas) &lt; Rb &lt; Cs</li>
</ul>

<p>
*No mesmo período (linha)
</p>
<ul class="org-ul">
<li>da esquerda para direita:*</li>
</ul>

<pre class="example" id="org6f15246">
DIMINUI →
</pre>

<p>
<b>Por quê?</b>
</p>
<ul class="org-ul">
<li>Mesmo número de camadas</li>
<li>Mais prótons no núcleo → maior atração</li>
<li>Elétrons são puxados mais para perto</li>
</ul>

<p>
<b>Exemplo:</b> Período 3
</p>
<ul class="org-ul">
<li>Na &gt; Mg &gt; Al &gt; Si &gt; P &gt; S &gt; Cl &gt; Ar</li>
</ul>
</div>
</div>

<div id="outline-container-org68824ae" class="outline-5">
<h5 id="org68824ae"><span class="section-number-5">5.3.3.2.</span> Resumo Visual</h5>
<div class="outline-text-5" id="text-5-3-3-2">
<ul class="org-ul">
<li>Raio Atômico</li>
</ul>
<pre class="example" id="org82b2a8a">
Tabela Periódica:

DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │ │
AUMENTA│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIOR raio: canto inferior esquerdo (Fr, Cs)
MENOR raio: canto superior direito (He, F, Ne)
</pre>
</div>
</div>

<div id="outline-container-orgf65d505" class="outline-5">
<h5 id="orgf65d505"><span class="section-number-5">5.3.3.3.</span> Raio Iônico</h5>
<div class="outline-text-5" id="text-5-3-3-3">
<p>
<b>Cátion (íon positivo):</b> perdeu elétrons
</p>
<ul class="org-ul">
<li><b>Menor</b> que o átomo neutro</li>
<li>Menos repulsão eletrônica</li>
</ul>

<p>
<b>Exemplo:</b> Na (raio maior) → Na⁺ (raio menor)
</p>

<p>
<b>Ânion (íon negativo):</b> ganhou elétrons
</p>
<ul class="org-ul">
<li><b>Maior</b> que o átomo neutro</li>
<li>Mais repulsão eletrônica</li>
</ul>

<p>
<b>Exemplo:</b> Cl (raio menor) → Cl⁻ (raio maior)
</p>

<p>
<b>Regra geral:</b>
</p>

<pre class="example" id="orge5076fa">
Cátion &lt; Átomo neutro &lt; Ânion
</pre>
</div>
</div>
</div>

<div id="outline-container-org4f17fcb" class="outline-4">
<h4 id="org4f17fcb"><span class="section-number-4">5.3.4.</span> 2. Energia de Ionização (EI ou PI)</h4>
<div class="outline-text-4" id="text-5-3-4">
<p>
<b>Definição:</b> energia necessária para <b>remover</b> um elétron de um átomo gasoso no estado fundamental.
</p>

<pre class="example" id="orgb230011">
X(g) + energia → X⁺(g) + e⁻
</pre>

<p>
<b>Unidade:</b> eV (elétron-volt) ou kJ/mol
</p>

<p>
<b>Ionizações sucessivas:</b>
</p>
<ul class="org-ul">
<li><b>1ª EI:</b> remover o 1º elétron</li>
<li><b>2ª EI:</b> remover o 2º elétron (SEMPRE maior que a 1ª)</li>
<li><b>3ª EI:</b> remover o 3º elétron</li>
</ul>

<p>
<b>Cada ionização sucessiva requer MAIS energia.</b>
</p>
</div>

<div id="outline-container-org7d4a6fb" class="outline-5">
<h5 id="org7d4a6fb"><span class="section-number-5">5.3.4.1.</span> Variação na Tabela Periódica</h5>
<div class="outline-text-5" id="text-5-3-4-1">
<p>
*Na mesma família (coluna)
</p>
<ul class="org-ul">
<li>de cima para baixo:*</li>
</ul>

<pre class="example" id="orgfc4ff27">
DIMINUI ↓
</pre>

<p>
<b>Por quê?</b>
</p>
<ul class="org-ul">
<li>Raio maior → elétrons mais distantes</li>
<li>Mais fácil remover (menos atração nuclear)</li>
</ul>

<p>
*No mesmo período (linha)
</p>
<ul class="org-ul">
<li>da esquerda para direita:*</li>
</ul>

<pre class="example" id="org654cef2">
AUMENTA →
</pre>

<p>
<b>Por quê?</b>
</p>
<ul class="org-ul">
<li>Raio menor → elétrons mais próximos do núcleo</li>
<li>Mais difícil remover (maior atração nuclear)</li>
</ul>
</div>
</div>

<div id="outline-container-org1f3562a" class="outline-5">
<h5 id="org1f3562a"><span class="section-number-5">5.3.4.2.</span> Resumo Visual</h5>
<div class="outline-text-5" id="text-5-3-4-2">
<ul class="org-ul">
<li>Energia de Ionização</li>
</ul>
<pre class="example" id="orgbfa7d63">
Tabela Periódica:

AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │ │
DIMINUI│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIOR EI: canto superior direito (He, Ne, F)
MENOR EI: canto inferior esquerdo (Fr, Cs)
</pre>

<p>
<b>Exceções importantes:</b>
</p>
<ul class="org-ul">
<li><b>Gases nobres:</b> EI muito alta (estáveis)</li>
<li><b>Metais alcalinos:</b> EI muito baixa (perdem elétron facilmente)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org58168e7" class="outline-4">
<h4 id="org58168e7"><span class="section-number-4">5.3.5.</span> 3. Afinidade Eletrônica (AE)</h4>
<div class="outline-text-4" id="text-5-3-5">
<p>
<b>Definição:</b> energia <b>liberada</b> quando um átomo gasoso <b>ganha</b> um elétron.
</p>

<pre class="example" id="org410154c">
X(g) + e⁻ → X⁻(g) + energia
</pre>

<p>
<b>Unidade:</b> eV ou kJ/mol
</p>

<p>
<b>Valores:</b>
</p>
<ul class="org-ul">
<li>Geralmente negativos (processo exotérmico</li>
<li>libera energia)</li>
<li>Quanto mais negativo, maior a afinidade (mais favorável)</li>
</ul>
</div>

<div id="outline-container-org6ab4ed3" class="outline-5">
<h5 id="org6ab4ed3"><span class="section-number-5">5.3.5.1.</span> Variação na Tabela Periódica</h5>
<div class="outline-text-5" id="text-5-3-5-1">
<p>
<b>Segue padrão semelhante à Energia de Ionização:</b>
</p>

<p>
<b>Na família:</b> DIMINUI de cima para baixo ↓ <b>No período:</b> AUMENTA da esquerda para direita →
</p>

<p>
<b>Maior AE (mais negativa):</b> Halogênios (Grupo 17)
</p>
<ul class="org-ul">
<li>Cl, F, Br (ganham elétron facilmente)</li>
</ul>

<p>
<b>Menor AE:</b> Metais alcalinos e gases nobres
</p>
<ul class="org-ul">
<li>Gases nobres: estáveis, não querem elétrons</li>
</ul>
</div>
</div>

<div id="outline-container-org39781fb" class="outline-5">
<h5 id="org39781fb"><span class="section-number-5">5.3.5.2.</span> Resumo Visual</h5>
<div class="outline-text-5" id="text-5-3-5-2">
<ul class="org-ul">
<li>Afinidade Eletrônica</li>
</ul>
<pre class="example" id="orgda927e7">
AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │ Hal│X│← gases nobres (AE≈0)
DIMINUI│ │ │ógn.│ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIOR AE: Halogênios (Cl, F, Br)
MENOR AE: Gases nobres, metais alcalinos
</pre>
</div>
</div>
</div>

<div id="outline-container-orgf46432e" class="outline-4">
<h4 id="orgf46432e"><span class="section-number-4">5.3.6.</span> 4. Eletronegatividade (EN)</h4>
<div class="outline-text-4" id="text-5-3-6">
<p>
<b>Definição:</b> tendência de um átomo em <b>atrair elétrons</b> em uma ligação química.
</p>

<p>
<b>Escala de Pauling:</b>
</p>
<ul class="org-ul">
<li><b>F (flúor):</b> 4,0 (mais eletronegativo)</li>
<li><b>Fr (frâncio):</b> 0,7 (menos eletronegativo)</li>
<li><b>Gases nobres:</b> não têm valor (não fazem ligações)</li>
</ul>
</div>

<div id="outline-container-orgf5574c8" class="outline-5">
<h5 id="orgf5574c8"><span class="section-number-5">5.3.6.1.</span> Variação na Tabela Periódica</h5>
<div class="outline-text-5" id="text-5-3-6-1">
<p>
<b>Na família:</b> DIMINUI de cima para baixo ↓ <b>No período:</b> AUMENTA da esquerda para direita →
</p>

<p>
<b>Padrão similar à Energia de Ionização e Afinidade Eletrônica.</b>
</p>
</div>
</div>

<div id="outline-container-org86edb4d" class="outline-5">
<h5 id="org86edb4d"><span class="section-number-5">5.3.6.2.</span> Resumo Visual</h5>
<div class="outline-text-5" id="text-5-3-6-2">
<ul class="org-ul">
<li>Eletronegatividade</li>
</ul>
<pre class="example" id="orge547baf">
AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │F│← 4,0 (máximo)
DIMINUI│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
Fr ────┴─┴─┴────┴─┘
0,7

MAIS eletronegativo: F &gt; O &gt; N &gt; Cl
MENOS eletronegativo: Fr, Cs (metais alcalinos)
</pre>

<p>
<b>Sequência decorar:</b>
</p>

<pre class="example" id="org8fc88ea">
F &gt; O &gt; N &gt; Cl &gt; Br &gt; I &gt; S &gt; C &gt; H
4,0  3,5  3,0  3,0
</pre>

<p>
<b>Aplicação:</b>
</p>
<ul class="org-ul">
<li><b>Diferença de EN:</b> determina tipo de ligação</li>
<li>ΔEN = 0: ligação covalente apolar</li>
<li>0 &lt; ΔEN &lt; 1,7: ligação covalente polar</li>
<li>ΔEN ≥ 1,7: ligação iônica</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgfc75fd1" class="outline-4">
<h4 id="orgfc75fd1"><span class="section-number-4">5.3.7.</span> 5. Eletropositividade ou Caráter Metálico</h4>
<div class="outline-text-4" id="text-5-3-7">
<p>
<b>Definição:</b> tendência de um átomo em <b>perder elétrons</b> (formar cátions).
</p>

<p>
<b>Também chamado:</b>
</p>
<ul class="org-ul">
<li>Caráter metálico</li>
<li>Reatividade metálica</li>
</ul>
</div>

<div id="outline-container-org701ed04" class="outline-5">
<h5 id="org701ed04"><span class="section-number-5">5.3.7.1.</span> Variação na Tabela Periódica</h5>
<div class="outline-text-5" id="text-5-3-7-1">
<p>
<b>OPOSTO da Eletronegatividade:</b>
</p>

<p>
<b>Na família:</b> AUMENTA de cima para baixo ↓ <b>No período:</b> DIMINUI da esquerda para direita ←
</p>
</div>
</div>

<div id="outline-container-org979fb3d" class="outline-5">
<h5 id="org979fb3d"><span class="section-number-5">5.3.7.2.</span> Resumo Visual</h5>
<div class="outline-text-5" id="text-5-3-7-2">
<ul class="org-ul">
<li>Eletropositividade</li>
</ul>
<pre class="example" id="orge025ce2">
DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │Fr Cs    │ │
AUMENTA│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIS eletropositivo: Fr, Cs (metais alcalinos)
MENOS eletropositivo: F, O, N (não-metais)
</pre>

<p>
<b>Relação:</b>
</p>
<ul class="org-ul">
<li><b>Metais:</b> alta eletropositividade (perdem elétrons)</li>
<li><b>Não-metais:</b> alta eletronegatividade (ganham elétrons)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org58b4527" class="outline-4">
<h4 id="org58b4527"><span class="section-number-4">5.3.8.</span> Comparação das Propriedades Periódicas</h4>
<div class="outline-text-4" id="text-5-3-8">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Propriedade</th>
<th scope="col" class="org-left">Mesmo Período (→)</th>
<th scope="col" class="org-left">Mesma Família (↓)</th>
<th scope="col" class="org-left">Máximo</th>
<th scope="col" class="org-left">Mínimo</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left"><b>Raio Atômico</b></td>
<td class="org-left">Diminui</td>
<td class="org-left">Aumenta</td>
<td class="org-left">Fr, Cs</td>
<td class="org-left">He, F</td>
</tr>

<tr>
<td class="org-left"><b>Energia de Ionização</b></td>
<td class="org-left">Aumenta</td>
<td class="org-left">Diminui</td>
<td class="org-left">He, Ne</td>
<td class="org-left">Fr, Cs</td>
</tr>

<tr>
<td class="org-left"><b>Afinidade Eletrônica</b></td>
<td class="org-left">Aumenta</td>
<td class="org-left">Diminui</td>
<td class="org-left">Cl, F</td>
<td class="org-left">Gases nobres</td>
</tr>

<tr>
<td class="org-left"><b>Eletronegatividade</b></td>
<td class="org-left">Aumenta</td>
<td class="org-left">Diminui</td>
<td class="org-left">F (4,0)</td>
<td class="org-left">Fr (0,7)</td>
</tr>

<tr>
<td class="org-left"><b>Eletropositividade</b></td>
<td class="org-left">Diminui</td>
<td class="org-left">Aumenta</td>
<td class="org-left">Fr, Cs</td>
<td class="org-left">F, O</td>
</tr>
</tbody>
</table>
</div>
</div>

<div id="outline-container-org3572933" class="outline-4">
<h4 id="org3572933"><span class="section-number-4">5.3.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-3-9">
</div>
<div id="outline-container-orgc176751" class="outline-5">
<h5 id="orgc176751"><span class="section-number-5">5.3.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-3-9-1">
<p>
Compare o raio atômico: a) Na e K b) Na e Cl
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li>Na (Período 3) e K (Período 4)</li>
<li>mesma família (Grupo 1) Na família, raio aumenta para baixo. <b>K &gt; Na</b></li>

<li>Na e Cl</li>
<li>mesmo período (Período 3) No período, raio diminui para a direita. <b>Na &gt; Cl</b></li>
</ol>

<p>
<i>[Ver resposta 89 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org6252123" class="outline-5">
<h5 id="org6252123"><span class="section-number-5">5.3.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-3-9-2">
<p>
Ordene em ordem crescente de energia de ionização: F, Cl, Br
</p>

<p>
<b>Solução:</b>
</p>

<p>
Mesma família (Grupo 17
</p>
<ul class="org-ul">
<li>Halogênios) Na família, EI diminui para baixo.</li>
</ul>

<p>
F (Período 2) &gt; Cl (Período 3) &gt; Br (Período 4)
</p>

<p>
<i>[Ver resposta 90 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org5ae11ec" class="outline-5">
<h5 id="org5ae11ec"><span class="section-number-5">5.3.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-3-9-3">
<p>
Qual elemento é mais eletronegativo: C, N, O ou F?
</p>

<p>
<b>Solução:</b>
</p>

<p>
Todos no Período 2. No período, EN aumenta para a direita.
</p>

<p>
<b>F &gt; O &gt; N &gt; C</b>
</p>

<p>
<i>[Ver resposta 91 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgdab3cbd" class="outline-5">
<h5 id="orgdab3cbd"><span class="section-number-5">5.3.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-3-9-4">
<p>
(UFMG) Compare o tamanho: Na, Na⁺, Cl, Cl⁻
</p>

<p>
<b>Solução:</b>
</p>

<p>
Na → Na⁺ (perdeu elétron): cátion é menor Cl → Cl⁻ (ganhou elétron): ânion é maior
</p>

<p>
Na e Cl estão no mesmo período (3): Na &gt; Cl
</p>

<p>
Ordem: <b>Na⁺ &lt; Na &lt; Cl &lt; Cl⁻</b>
</p>

<p>
<i>[Ver resposta 92 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb139c67" class="outline-5">
<h5 id="orgb139c67"><span class="section-number-5">5.3.9.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-3-9-5">
<p>
Explique por que a 2ª energia de ionização é sempre maior que a 1ª.
</p>

<p>
<b>Solução:</b>
</p>

<p>
Após remover o 1º elétron:
</p>
<ul class="org-ul">
<li>Átomo vira cátion (+)</li>
<li>Menos elétrons → menos repulsão</li>
<li>Raio diminui</li>
<li>Elétrons mais atraídos pelo núcleo</li>
</ul>

<p>
<b>Resultado:</b> 2ª ionização requer MAIS energia (elétron está mais fortemente ligado).
</p>

<p>
<i>[Ver resposta 93 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgaf59ba1" class="outline-4">
<h4 id="orgaf59ba1"><span class="section-number-4">5.3.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-3-10">
<ol class="org-ol">
<li><b>Raio atômico:</b> ↓ na família, ← no período (oposto das demais)</li>
<li><b>EI, AE, EN:</b> mesmo padrão (↑ direita, ↓ baixo)</li>
<li><b>Eletropositividade:</b> oposto de eletronegatividade</li>
<li><b>F:</b> mais eletronegativo (4,0)</li>
<li><b>Cátion &lt; átomo neutro &lt; ânion</b> (tamanho)</li>
<li><b>2ª EI &gt; 1ª EI</b> (sempre!)</li>
<li><b>Halogênios:</b> alta afinidade eletrônica</li>
<li><b>Gases nobres:</b> alta EI, baixa AE (estáveis)</li>
</ol>
</div>
</div>

<div id="outline-container-org5501e4e" class="outline-4">
<h4 id="org5501e4e"><span class="section-number-4">5.3.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-3-11">
<p>
<b>Padrões Gerais:</b>
</p>

<p>
<b>Grupo (↓):</b>
</p>
<ul class="org-ul">
<li>Raio: AUMENTA</li>
<li>EI, AE, EN: DIMINUI</li>
<li>Eletropositividade: AUMENTA</li>
</ul>

<p>
<b>Período (→):</b>
</p>
<ul class="org-ul">
<li>Raio: DIMINUI</li>
<li>EI, AE, EN: AUMENTA</li>
<li>Eletropositividade: DIMINUI</li>
</ul>

<p>
<b>Extremos:</b>
</p>
<ul class="org-ul">
<li><b>F:</b> maior EN (4,0), menor raio (entre os reativos)</li>
<li><b>Fr/Cs:</b> maior raio, menor EN, maior eletropositividade</li>
<li><b>He:</b> menor raio absoluto, maior EI</li>
<li><b>Halogênios:</b> maior AE</li>
</ul>
</div>
</div>

<div id="outline-container-org1118962" class="outline-4">
<h4 id="org1118962"><span class="section-number-4">5.3.12.</span> Resumo Visual Completo</h4>
<div class="outline-text-4" id="text-5-3-12">
<pre class="example" id="org21af1c0">
TABELA PERIÓDICA
- TENDÊNCIAS

         RAIO ATÔMICO
         DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │ │
AUMENTA│ │ │    │ │
     ↓ │ │ │    │ │
       └─┴─┴────┴─┘

     EI, AE, EN
      AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │F│ MAX
DIMINUI│ │ │    │ │
     ↓ │ │ │    │ │
       └─┴─┴────┴─┘
Fr/Cs MIN

 ELETROPOSITIVIDADE
    DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │Fr Cs    │ │ MAX
AUMENTA│ │ │    │ │
     ↓ │ │ │    │F│ MIN
       └─┴─┴────┴─┘
</pre>
</div>
</div>

<div id="outline-container-org2d6eaae" class="outline-4">
<h4 id="org2d6eaae"><span class="section-number-4">5.3.13.</span> Tabela Resumo</h4>
<div class="outline-text-4" id="text-5-3-13">
<pre class="example" id="org94954de">
┌───────────────────┬───────────┬───────────┬────────┐
│    Propriedade    │  Período  │  Família  │  Max   │
│                   │    (→)    │    (↓)    │        │
├───────────────────┼───────────┼───────────┼────────┤
│ Raio Atômico      │  Diminui  │  Aumenta  │ Fr, Cs │
│ Energia Ionização │  Aumenta  │  Diminui  │  He    │
│ Afinidade Eletr.  │  Aumenta  │  Diminui  │  Cl, F │
│ Eletronegatividade│  Aumenta  │  Diminui  │  F(4,0)│
│ Eletropositividade│  Diminui  │  Aumenta  │ Fr, Cs │
└───────────────────┴───────────┴───────────┴────────┘

Tamanho de Íons:
Cátion⁺ &lt; Átomo neutro &lt; Ânion⁻

Eletronegatividade (decorar):
F &gt; O &gt; N &gt; Cl &gt; Br &gt; I &gt; S &gt; C &gt; H
4,0  3,5  3,0  3,0
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>muito cobrado!)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgccd7013" class="outline-3">`;

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
