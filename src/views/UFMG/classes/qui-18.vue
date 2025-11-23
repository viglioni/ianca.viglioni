<script setup lang="ts">
import { ref } from "vue";

const code = "qui-18";
const title = "Química: Tabela Periódica";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-3">
<ul class="org-ul">
<li>Química: Tabela Periódica</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org233d26c" class="outline-4">
<h4 id="org233d26c"><span class="section-number-4">4.3.1.</span> A Tabela Periódica Moderna</h4>
<div class="outline-text-4" id="text-4-3-1">
<p>
A <b>Tabela Periódica</b> é uma organização sistemática de todos os elementos químicos conhecidos, arranjados em ordem crescente de <b>número atômico (Z)</b>.
</p>

<p>
<b>História:</b>
</p>
<ul class="org-ul">
<li><b>Mendeleev (1869):</b> primeira tabela periódica (ordem de massa atômica)</li>
<li>Previu propriedades de elementos ainda não descobertos</li>
<li><b>Moseley (1913):</b> reorganizou por número atômico (Lei Periódica Moderna)</li>
</ul>

<p>
<b>Lei Periódica Moderna:</b> &gt; “As propriedades físicas e químicas dos elementos são funções periódicas de seus números atômicos.”
</p>
</div>
</div>

<div id="outline-container-org7fb5f06" class="outline-4">
<h4 id="org7fb5f06"><span class="section-number-4">4.3.2.</span> Estrutura da Tabela Periódica</h4>
<div class="outline-text-4" id="text-4-3-2">
</div>
<div id="outline-container-org7def32e" class="outline-5">
<h5 id="org7def32e"><span class="section-number-5">4.3.2.1.</span> Períodos (Linhas Horizontais)</h5>
<div class="outline-text-5" id="text-4-3-2-1">
<p>
São as <b>7 linhas horizontais</b> da tabela.
</p>

<p>
<b>Período indica:</b>
</p>
<ul class="org-ul">
<li>Número de camadas eletrônicas (níveis de energia)</li>
<li>Elementos do mesmo período têm o mesmo número de camadas</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li><b>Período 1:</b> H, He (1 camada: K)</li>
<li><b>Período 2:</b> Li, Be, B, C, N, O, F, Ne (2 camadas: K, L)</li>
<li><b>Período 3:</b> Na, Mg, Al, Si, P, S, Cl, Ar (3 camadas: K, L, M)</li>
</ul>
</div>
</div>

<div id="outline-container-org0bffb09" class="outline-5">
<h5 id="org0bffb09"><span class="section-number-5">4.3.2.2.</span> Famílias ou Grupos (Colunas Verticais)</h5>
<div class="outline-text-5" id="text-4-3-2-2">
<p>
São as <b>18 colunas verticais</b> da tabela.
</p>

<p>
<b>Família indica:</b>
</p>
<ul class="org-ul">
<li>Número de elétrons na camada de valência (última camada)</li>
<li>Elementos da mesma família têm propriedades químicas semelhantes</li>
</ul>

<p>
<b>Principais famílias:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-right" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Grupo</th>
<th scope="col" class="org-left">Nome</th>
<th scope="col" class="org-right">Elétrons Valência</th>
<th scope="col" class="org-left">Características</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">1 (IA)</td>
<td class="org-left">Metais Alcalinos</td>
<td class="org-right">1</td>
<td class="org-left">Muito reativos, moles, baixa densidade</td>
</tr>

<tr>
<td class="org-left">2 (IIA)</td>
<td class="org-left">Metais Alcalino-Terrosos</td>
<td class="org-right">2</td>
<td class="org-left">Reativos, mais duros que alcalinos</td>
</tr>

<tr>
<td class="org-left">13 (IIIA)</td>
<td class="org-left">Família do Boro</td>
<td class="org-right">3</td>
<td class="org-left">Propriedades variadas</td>
</tr>

<tr>
<td class="org-left">14 (IVA)</td>
<td class="org-left">Família do Carbono</td>
<td class="org-right">4</td>
<td class="org-left">Base da química orgânica</td>
</tr>

<tr>
<td class="org-left">15 (VA)</td>
<td class="org-left">Família do Nitrogênio</td>
<td class="org-right">5</td>
<td class="org-left">Não-metais importantes</td>
</tr>

<tr>
<td class="org-left">16 (VIA)</td>
<td class="org-left">Calcogênios</td>
<td class="org-right">6</td>
<td class="org-left">Oxigênio e enxofre são essenciais</td>
</tr>

<tr>
<td class="org-left">17 (VIIA)</td>
<td class="org-left">Halogênios</td>
<td class="org-right">7</td>
<td class="org-left">Muito reativos, formam sais</td>
</tr>

<tr>
<td class="org-left">18 (VIIIA)</td>
<td class="org-left">Gases Nobres</td>
<td class="org-right">8 (exceto He: 2)</td>
<td class="org-left">Inertes, estáveis</td>
</tr>
</tbody>
</table>

<p>
<b>Nomenclaturas:</b>
</p>
<ul class="org-ul">
<li><b>Antiga:</b> IA, IIA, IIIA&#x2026; VIIIA</li>
<li><b>Moderna (IUPAC):</b> 1, 2, 3&#x2026; 18</li>
</ul>
</div>
</div>

<div id="outline-container-org7526c91" class="outline-5">
<h5 id="org7526c91"><span class="section-number-5">4.3.2.3.</span> Elementos Representativos, Transição e Transição Interna</h5>
<div class="outline-text-5" id="text-4-3-2-3">
<p>
<b>Elementos Representativos:</b>
</p>
<ul class="org-ul">
<li>Grupos 1, 2, 13, 14, 15, 16, 17, 18</li>
<li>Famílias A (notação antiga)</li>
<li>Camadas de valência: s ou p</li>
</ul>

<p>
<b>Elementos de Transição:</b>
</p>
<ul class="org-ul">
<li>Grupos 3 a 12</li>
<li>Famílias B (notação antiga)</li>
<li>Camadas de valência: d (e também s)</li>
<li>Todos são metais</li>
</ul>

<p>
<b>Elementos de Transição Interna:</b>
</p>
<ul class="org-ul">
<li><b>Lantanídeos:</b> elementos 57-71</li>
<li><b>Actinídeos:</b> elementos 89-103</li>
<li>Camadas de valência: f (e também d e s)</li>
<li>Colocados separadamente na tabela</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org9ebd5db" class="outline-4">
<h4 id="org9ebd5db"><span class="section-number-4">4.3.3.</span> Classificação dos Elementos</h4>
<div class="outline-text-4" id="text-4-3-3">
</div>
<div id="outline-container-org142c951" class="outline-5">
<h5 id="org142c951"><span class="section-number-5">4.3.3.1.</span> Metais</h5>
<div class="outline-text-5" id="text-4-3-3-1">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Brilho metálico</li>
<li>Condutores de calor e eletricidade</li>
<li>Maleáveis e dúcteis</li>
<li>Sólidos (exceto Hg</li>
<li>mercúrio)</li>
<li>Tendência a perder elétrons (formar cátions)</li>
</ul>

<p>
<b>Localização:</b> maioria da tabela (lado esquerdo e centro)
</p>

<p>
<b>Exemplos:</b> Na, Fe, Cu, Au, Ag, Al, Zn
</p>
</div>
</div>

<div id="outline-container-orgd92ef9d" class="outline-5">
<h5 id="orgd92ef9d"><span class="section-number-5">4.3.3.2.</span> Não-Metais (Ametais)</h5>
<div class="outline-text-5" id="text-4-3-3-2">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Sem brilho metálico</li>
<li>Isolantes (maus condutores)</li>
<li>Quebradiços no estado sólido</li>
<li>Estados variados (sólidos, líquidos, gasosos)</li>
<li>Tendência a ganhar elétrons (formar ânions)</li>
</ul>

<p>
<b>Localização:</b> canto superior direito
</p>

<p>
<b>Exemplos:</b> C, N, O, P, S, Cl, Br (líquido)
</p>
</div>
</div>

<div id="outline-container-orgd54a5c4" class="outline-5">
<h5 id="orgd54a5c4"><span class="section-number-5">4.3.3.3.</span> Semimetais (Metaloides)</h5>
<div class="outline-text-5" id="text-4-3-3-3">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Propriedades intermediárias</li>
<li>Semicondutores</li>
<li>Importantes para eletrônica</li>
</ul>

<p>
<b>Localização:</b> “escada” entre metais e não-metais
</p>

<p>
<b>Exemplos:</b> B, Si, Ge, As, Sb, Te, (Po)
</p>
</div>
</div>

<div id="outline-container-org74b9292" class="outline-5">
<h5 id="org74b9292"><span class="section-number-5">4.3.3.4.</span> Gases Nobres</h5>
<div class="outline-text-5" id="text-4-3-3-4">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Inertes (muito estáveis)</li>
<li>Não formam ligações facilmente</li>
<li>Camada de valência completa</li>
<li>Todos são gases</li>
</ul>

<p>
<b>Exemplos:</b> He, Ne, Ar, Kr, Xe, Rn
</p>
</div>
</div>
</div>

<div id="outline-container-org231ce95" class="outline-4">
<h4 id="org231ce95"><span class="section-number-4">4.3.4.</span> Distribuição Eletrônica e Posição na Tabela</h4>
<div class="outline-text-4" id="text-4-3-4">
<p>
A distribuição eletrônica determina a posição do elemento:
</p>

<p>
<b>Regras:</b> 1. <b>Último nível ocupado</b> → Período (número de camadas) 2. <b>Elétrons na camada de valência</b> → Família
</p>

<p>
<b>Subnível mais energético:</b>
</p>
<ul class="org-ul">
<li><b>s ou p:</b> elemento representativo (família A)</li>
<li><b>d:</b> elemento de transição (família B)</li>
<li><b>f:</b> transição interna</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Sódio (Na, Z = 11):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 1s² 2s² 2p⁶ 3s¹</li>
<li>Camadas: K=2, L=8, M=1 → <b>3 camadas</b> → Período 3</li>
<li>Valência: 1 elétron → <b>Grupo 1</b> (IA)</li>
<li>Metais Alcalinos</li>
</ul>

<p>
<b>Cloro (Cl, Z = 17):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 1s² 2s² 2p⁶ 3s² 3p⁵</li>
<li>Camadas: K=2, L=8, M=7 → <b>3 camadas</b> → Período 3</li>
<li>Valência: 7 elétrons → <b>Grupo 17</b> (VIIA)</li>
<li>Halogênios</li>
</ul>

<p>
<b>Ferro (Fe, Z = 26):</b>
</p>
<ul class="org-ul">
<li>Distribuição: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶</li>
<li>Camadas: 4 → Período 4</li>
<li>Subnível mais energético: 3d → <b>Elemento de transição</b></li>
</ul>
</div>
</div>

<div id="outline-container-orgf12a59f" class="outline-4">
<h4 id="orgf12a59f"><span class="section-number-4">4.3.5.</span> Propriedades Periódicas e Aperiódicas</h4>
<div class="outline-text-4" id="text-4-3-5">
<p>
<b>Propriedades Periódicas:</b> variam periodicamente com o número atômico
</p>

<p>
<b>Propriedades Aperiódicas:</b> não seguem periodicidade (ex: massa atômica)
</p>

<p>
<i>Estudaremos as propriedades periódicas detalhadamente na próxima aula (Aula 23).</i>
</p>
</div>
</div>

<div id="outline-container-org9d5f58b" class="outline-4">
<h4 id="org9d5f58b"><span class="section-number-4">4.3.6.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-3-6">
</div>
<div id="outline-container-orgdb8d656" class="outline-5">
<h5 id="orgdb8d656"><span class="section-number-5">4.3.6.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-3-6-1">
<p>
Um elemento químico tem número atômico 19. Determine: a) Sua distribuição eletrônica b) Seu período c) Sua família d) Sua classificação (metal, não-metal, etc.)
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li>Z = 19 → 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹</li>

<li>4 camadas (K, L, M, N) → <b>Período 4</b></li>

<li>1 elétron na valência → <b>Grupo 1 (IA)</b></li>
<li>Metais Alcalinos</li>

<li>Grupo 1, lado esquerdo → <b>Metal alcalino</b></li>
</ol>

<p>
<i>É o elemento Potássio (K)</i>
</p>

<p>
<i>[Ver resposta 72 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orge880afa" class="outline-5">
<h5 id="orge880afa"><span class="section-number-5">4.3.6.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-3-6-2">
<p>
Qual família tem 7 elétrons na camada de valência? Quais suas principais características?
</p>

<p>
<b>Solução:</b>
</p>

<p>
7 elétrons na valência → *Grupo 17 (VIIA)
</p>
<ul class="org-ul">
<li>Halogênios*</li>
</ul>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Muito reativos</li>
<li>Formam sais com metais</li>
<li>Ganham 1 elétron facilmente (formam ânions -1)</li>
<li>Elementos: F, Cl, Br, I, At</li>
</ul>

<p>
<i>[Ver resposta 73 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf2c010c" class="outline-5">
<h5 id="orgf2c010c"><span class="section-number-5">4.3.6.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-3-6-3">
<p>
(UFMG) Um elemento X está no 3º período e tem 5 elétrons na camada de valência. Determine: a) Sua distribuição eletrônica b) Sua família c) Seu número atômico
</p>

<p>
<b>Solução:</b>
</p>

<p>
3º período: 3 camadas (K, L, M) 5 elétrons na valência: M tem 5 elétrons
</p>

<p>
Distribuição: K = 2 L = 8 M = 5
</p>

<ol class="org-ol">
<li>1s² 2s² 2p⁶ 3s² 3p³</li>

<li>5 elétrons → <b>Grupo 15 (VA)</b></li>
<li>Família do Nitrogênio</li>

<li>Z = 2 + 8 + 5 = <b>15</b> (Fósforo</li>
<li>P)</li>
</ol>

<p>
<i>[Ver resposta 74 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org21ae0ec" class="outline-5">
<h5 id="org21ae0ec"><span class="section-number-5">4.3.6.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-3-6-4">
<p>
Classifique os elementos em metal, não-metal, semimetal ou gás nobre: a) Grupo 1 b) Grupo 18 c) Silício (Si) d) Oxigênio (O)
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li>Grupo 1 (IA) → <b>Metais alcalinos</b> (metal)</li>

<li>Grupo 18 (VIIIA) → <b>Gases nobres</b></li>

<li>Si: localizado na “escada” → <b>Semimetal</b></li>

<li>O: canto superior direito → <b>Não-metal</b> (ametal)</li>
</ol>

<p>
<i>[Ver resposta 75 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org1253ada" class="outline-4">
<h4 id="org1253ada"><span class="section-number-4">4.3.7.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-3-7">
<ol class="org-ol">
<li><b>Período = número de camadas</b> (níveis de energia)</li>
<li><b>Família = elétrons na valência</b> (última camada)</li>
<li><b>Grupos principais:</b> 1 (alcalinos), 2 (alcalino-terrosos), 17 (halogênios), 18 (gases nobres)</li>
<li><b>Metais:</b> maioria (esquerda/centro); <b>não-metais:</b> canto superior direito</li>
<li><b>Semimetais:</b> “escada” entre metais e não-metais</li>
<li><b>Transição:</b> grupos 3-12 (todos metais, subnível d)</li>
<li><b>Gases nobres:</b> extremamente estáveis (valência completa)</li>
<li><b>Distribuição eletrônica</b> determina tudo: período e família</li>
</ol>
</div>
</div>

<div id="outline-container-orgac33aaa" class="outline-4">
<h4 id="orgac33aaa"><span class="section-number-4">4.3.8.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-3-8">
<p>
<b>Organização:</b>
</p>
<ul class="org-ul">
<li><b>Horizontal (Períodos):</b> 7 linhas = número de camadas</li>
<li><b>Vertical (Grupos/Famílias):</b> 18 colunas = elétrons de valência</li>
</ul>

<p>
<b>Famílias importantes:</b>
</p>
<ul class="org-ul">
<li>Grupo 1: Metais Alcalinos (1 e⁻ valência)</li>
<li>Grupo 2: Alcalino-Terrosos (2 e⁻)</li>
<li>Grupo 17: Halogênios (7 e⁻)</li>
<li>Grupo 18: Gases Nobres (8 e⁻, exceto He)</li>
</ul>

<p>
<b>Classificação:</b>
</p>
<ul class="org-ul">
<li>Metais: esquerda/centro (perdem e⁻)</li>
<li>Não-metais: direita superior (ganham e⁻)</li>
<li>Semimetais: “escada” (semicondutores)</li>
<li>Gases nobres: grupo 18 (inertes)</li>
</ul>

<p>
<b>Lei Periódica:</b> Propriedades variam periodicamente com número atômico (Z)
</p>
</div>
</div>

<div id="outline-container-orgab63236" class="outline-4">
<h4 id="orgab63236"><span class="section-number-4">4.3.9.</span> Fórmulas e Conceitos Essenciais</h4>
<div class="outline-text-4" id="text-4-3-9">
<pre class="example" id="orge2ee676">
Número Atômico (Z):
Determina a posição na tabela

Distribuição Eletrônica → Posição:
Último nível → Período
Elétrons valência → Família

Valência por Grupo:
Grupo 1: 1 elétron
Grupo 2: 2 elétrons
Grupo 13: 3 elétrons
Grupo 14: 4 elétrons
Grupo 15: 5 elétrons
Grupo 16: 6 elétrons
Grupo 17: 7 elétrons
Grupo 18: 8 elétrons (He: 2)

Subnível mais energético:
s ou p → Representativo (A)
d → Transição (B)
f → Transição interna
</pre>
</div>
</div>

<div id="outline-container-org5fcbe22" class="outline-4">
<h4 id="org5fcbe22"><span class="section-number-4">4.3.10.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-3-10">
<pre class="example" id="org89046ac">
Estrutura da Tabela Periódica:

PERÍODOS (1-7)
↓
1  IA ──────────────────────── VIIIA
2  IIA                          gases
3  Metais  Transição  Não-met. nobres
4  alcal.  (B)        Semimet.
5          3-12       IIIA-VIIA
6  
7  Lantanídeos (f)
   Actinídeos (f)

Classificação:
┌──────────┬─────────────────────┐
│ Posição  │  Classificação      │
├──────────┼─────────────────────┤
│ Esquerda │ Metais              │
│ Centro   │ Transição (metais)  │
│ "Escada" │ Semimetais          │
│ Direita  │ Não-metais          │
│ Grupo 18 │ Gases Nobres        │
└──────────┴─────────────────────┘

Principais Famílias:
Grupo 1:  Metais Alcalinos (1e⁻)
Grupo 2:  Alcalino-Terrosos (2e⁻)
Grupo 17: Halogênios (7e⁻) [reativos]
Grupo 18: Gases Nobres (8e⁻) [inertes]
</pre>
</div>
</div>

<div id="outline-container-org1392b90" class="outline-4">
<h4 id="org1392b90"><span class="section-number-4">4.3.11.</span> Tabela de Referência</h4>
<div class="outline-text-4" id="text-4-3-11">
<ul class="org-ul">
<li>Famílias</li>
</ul>
<pre class="example" id="orgfd14d49">
┌───────┬──────────────────┬──────┬──────────────┐
│ Grupo │ Nome             │ Val. │ Exemplos     │
├───────┼──────────────────┼──────┼──────────────┤
│  1    │ Alcalinos        │  1   │ Li,Na,K,Rb,Cs│
│  2    │ Alcalino-Terrosos│  2   │ Be,Mg,Ca,Sr,Ba│
│  13   │ Boro             │  3   │ B,Al,Ga,In   │
│  14   │ Carbono          │  4   │ C,Si,Ge,Sn,Pb│
│  15   │ Nitrogênio       │  5   │ N,P,As,Sb,Bi │
│  16   │ Calcogênios      │  6   │ O,S,Se,Te,Po │
│  17   │ Halogênios       │  7   │ F,Cl,Br,I,At │
│  18   │ Gases Nobres     │ 8(2) │ He,Ne,Ar,Kr  │
└───────┴──────────────────┴──────┴──────────────┘
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Fundamental <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base de toda química)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org57319b4" class="outline-3">`;

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
