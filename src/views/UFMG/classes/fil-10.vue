<script setup lang="ts">
import { ref } from "vue";

const code = "fil-10";
const title = "Filosofia: Lógica";
const subject = "filosofia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-5">
<ul class="org-ul">
<li>Filosofia: Lógica</li>
<li>Argumento, Validade e Falácia</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org2ebe6c7" class="outline-4">
<h4 id="org2ebe6c7"><span class="section-number-4">2.5.1.</span> O que é Lógica?</h4>
<div class="outline-text-4" id="text-2-5-1">
<p>
<b>Lógica</b> é o ramo da Filosofia que estuda os princípios do raciocínio correto e da argumentação válida.
</p>

<p>
<b>Objetivo da lógica:</b>
</p>
<ul class="org-ul">
<li>Distinguir raciocínios válidos de raciocínios inválidos</li>
<li>Analisar a estrutura dos argumentos</li>
<li>Identificar erros de raciocínio (falácias)</li>
</ul>

<p>
<b>Importância:</b>
</p>
<ul class="org-ul">
<li>Fundamental para o pensamento crítico</li>
<li>Base da matemática, ciências e filosofia</li>
<li>Ajuda a evitar manipulações argumentativas</li>
<li>Essencial para debates e discussões racionais</li>
</ul>
</div>
</div>

<div id="outline-container-orgc5ec598" class="outline-4">
<h4 id="orgc5ec598"><span class="section-number-4">2.5.2.</span> O que é um Argumento?</h4>
<div class="outline-text-4" id="text-2-5-2">
<p>
<b>Argumento</b> é um conjunto de proposições (afirmações) em que algumas (premissas) servem de razão ou justificativa para outra (conclusão).
</p>

<p>
<b>Estrutura básica:</b>
</p>

<pre class="example" id="org140b50a">
Premissa 1
Premissa 2
...
Premissa n
─────────────
Conclusão
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgd0945f1">
Premissa 1: Todos os homens são mortais
Premissa 2: Sócrates é homem
─────────────────────────────────────
Conclusão: Logo, Sócrates é mortal
</pre>
</div>
</div>

<div id="outline-container-org0afdd9c" class="outline-4">
<h4 id="org0afdd9c"><span class="section-number-4">2.5.3.</span> Proposições</h4>
<div class="outline-text-4" id="text-2-5-3">
<p>
<b>Proposição</b> é uma afirmação que pode ser verdadeira ou falsa.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Expressa um conteúdo que pode ser julgado (verdadeiro ou falso)</li>
<li>Declarativa (afirmativa ou negativa)</li>
<li>Não é pergunta, ordem ou exclamação</li>
</ul>

<p>
<b>Exemplos de proposições:</b>
</p>
<ul class="org-ul">
<li>“O céu é azul” (verdadeiro)</li>
<li>“2 + 2 = 5” (falso)</li>
<li>“Brasília é a capital do Brasil” (verdadeiro)</li>
</ul>

<p>
<b>Não são proposições:</b>
</p>
<ul class="org-ul">
<li>“Que horas são?” (pergunta)</li>
<li>“Feche a porta!” (ordem)</li>
<li>“Que lindo!” (exclamação)</li>
<li>“x &gt; 5” (sentença aberta</li>
<li>depende do valor de x)</li>
</ul>
</div>
</div>

<div id="outline-container-orgccdfe85" class="outline-4">
<h4 id="orgccdfe85"><span class="section-number-4">2.5.4.</span> Premissas e Conclusão</h4>
<div class="outline-text-4" id="text-2-5-4">
</div>
<div id="outline-container-orgabc4ec6" class="outline-5">
<h5 id="orgabc4ec6"><span class="section-number-5">2.5.4.1.</span> Premissas</h5>
<div class="outline-text-5" id="text-2-5-4-1">
<ul class="org-ul">
<li>São as <b>razões</b> ou <b>evidências</b> apresentadas</li>
<li>Servem de <b>suporte</b> para a conclusão</li>
<li>Podem ser verdadeiras ou falsas</li>
</ul>
</div>
</div>

<div id="outline-container-org640d83f" class="outline-5">
<h5 id="org640d83f"><span class="section-number-5">2.5.4.2.</span> Conclusão</h5>
<div class="outline-text-5" id="text-2-5-4-2">
<ul class="org-ul">
<li>É a <b>afirmação</b> que se pretende estabelecer</li>
<li>Aquilo que se quer <b>provar</b> ou <b>demonstrar</b></li>
<li>Deve ser apoiada pelas premissas</li>
</ul>

<p>
<b>Indicadores de premissas:</b>
</p>
<ul class="org-ul">
<li>porque, pois, uma vez que, dado que, visto que, já que</li>
</ul>

<p>
<b>Indicadores de conclusão:</b>
</p>
<ul class="org-ul">
<li>logo, portanto, então, assim, consequentemente, por isso</li>
</ul>

<p>
<b>Exemplo:</b> “*Visto que* todos os mamíferos são animais de sangue quente <b>e</b> as baleias são mamíferos, <b>logo</b> as baleias são animais de sangue quente.”
</p>

<ul class="org-ul">
<li>Premissa 1: Todos os mamíferos são animais de sangue quente</li>
<li>Premissa 2: As baleias são mamíferos</li>
<li>Conclusão: As baleias são animais de sangue quente</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org2df411e" class="outline-4">
<h4 id="org2df411e"><span class="section-number-4">2.5.5.</span> Validade de um Argumento</h4>
<div class="outline-text-4" id="text-2-5-5">
<p>
<b>Argumento válido:</b> É aquele em que, <b>se</b> as premissas forem verdadeiras, a conclusão <b>necessariamente</b> será verdadeira.
</p>

<p>
<b>Importante:</b>
</p>
<ul class="org-ul">
<li>Validade é sobre a <b>estrutura</b> do argumento, não sobre a verdade das premissas</li>
<li>Um argumento pode ser válido mesmo com premissas falsas</li>
<li>O que importa é: <b>SE</b> as premissas fossem verdadeiras, a conclusão seria verdadeira?</li>
</ul>
</div>

<div id="outline-container-org961176a" class="outline-5">
<h5 id="org961176a"><span class="section-number-5">2.5.5.1.</span> Exemplo de Argumento Válido</h5>
<div class="outline-text-5" id="text-2-5-5-1">
<pre class="example" id="orgb395ae0">
Premissa 1: Todos os cães são mamíferos
Premissa 2: Rex é um cão
───────────────────────────────────
Conclusão: Rex é mamífero
</pre>

<p>
<b>Válido:</b> Se as premissas são verdadeiras, a conclusão necessariamente é verdadeira.
</p>
</div>
</div>

<div id="outline-container-org9167907" class="outline-5">
<h5 id="org9167907"><span class="section-number-5">2.5.5.2.</span> Exemplo de Argumento Inválido</h5>
<div class="outline-text-5" id="text-2-5-5-2">
<pre class="example" id="orga511a76">
Premissa 1: Todos os cães são mamíferos
Premissa 2: Rex é mamífero
───────────────────────────────────
Conclusão: Rex é cão
</pre>

<p>
<b>Inválido:</b> Mesmo que as premissas sejam verdadeiras, a conclusão pode ser falsa (Rex pode ser um gato, por exemplo).
</p>
</div>
</div>
</div>

<div id="outline-container-orgdc5c707" class="outline-4">
<h4 id="orgdc5c707"><span class="section-number-4">2.5.6.</span> Verdade vs Validade</h4>
<div class="outline-text-4" id="text-2-5-6">
<p>
<b>Diferença crucial:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Conceito</th>
<th scope="col" class="org-left">Aplica-se a</th>
<th scope="col" class="org-left">Significado</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left"><b>Verdade</b></td>
<td class="org-left">Proposições</td>
<td class="org-left">Uma afirmação corresponde à realidade</td>
</tr>

<tr>
<td class="org-left"><b>Validade</b></td>
<td class="org-left">Argumentos</td>
<td class="org-left">A conclusão decorre logicamente das premissas</td>
</tr>
</tbody>
</table>

<p>
<b>Possibilidades:</b>
</p>

<ol class="org-ol">
<li><b>Argumento válido com premissas e conclusão verdadeiras</b> ✓ (ideal</li>
<li>argumento sólido)</li>
<li><b>Argumento válido com premissas falsas e conclusão verdadeira</b> (válido, mas não confiável)</li>
<li><b>Argumento válido com premissas falsas e conclusão falsa</b> (válido, mas não confiável)</li>
<li><b>Argumento inválido</b> (independente da verdade das proposições)</li>
</ol>

<p>
<b>Exemplo de argumento válido mas com premissa falsa:</b>
</p>

<pre class="example" id="org4083ac4">
Premissa 1: Todos os peixes voam (FALSO)
Premissa 2: O tubarão é um peixe (VERDADEIRO)
────────────────────────────────────────────
Conclusão: O tubarão voa (FALSO)
</pre>

<p>
<b>Válido:</b> SE a premissa 1 fosse verdadeira, a conclusão seria verdadeira. A estrutura é correta.
</p>
</div>
</div>

<div id="outline-container-org88104de" class="outline-4">
<h4 id="org88104de"><span class="section-number-4">2.5.7.</span> Argumento Sólido (Sound)</h4>
<div class="outline-text-4" id="text-2-5-7">
<p>
<b>Argumento sólido</b> = argumento <b>válido</b> + premissas <b>verdadeiras</b>
</p>

<p>
É o argumento ideal:
</p>
<ul class="org-ul">
<li>Estrutura correta (válido)</li>
<li>Premissas verdadeiras</li>
<li>Conclusão necessariamente verdadeira</li>
</ul>
</div>
</div>

<div id="outline-container-org1fdf1f1" class="outline-4">
<h4 id="org1fdf1f1"><span class="section-number-4">2.5.8.</span> Tipos de Argumentos</h4>
<div class="outline-text-4" id="text-2-5-8">
</div>
<div id="outline-container-org74f986f" class="outline-5">
<h5 id="org74f986f"><span class="section-number-5">2.5.8.1.</span> 1. Argumento Dedutivo</h5>
<div class="outline-text-5" id="text-2-5-8-1">
<p>
<b>Definição:</b> A conclusão está <b>contida</b> nas premissas; a conclusão não traz informação nova.
</p>

<p>
<b>Característica:</b> Se válido e premissas verdadeiras, conclusão é <b>necessariamente</b> verdadeira.
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org8a61cbc">
Todos os A são B
x é A
────────────
x é B
</pre>

<p>
<b>Exemplo concreto:</b>
</p>

<pre class="example" id="org2ed6445">
Todos os metais conduzem eletricidade
O cobre é metal
───────────────────────────────────
O cobre conduz eletricidade
</pre>
</div>
</div>

<div id="outline-container-orgd9c2619" class="outline-5">
<h5 id="orgd9c2619"><span class="section-number-5">2.5.8.2.</span> 2. Argumento Indutivo</h5>
<div class="outline-text-5" id="text-2-5-8-2">
<p>
<b>Definição:</b> A conclusão <b>generaliza</b> a partir de casos particulares; traz informação nova.
</p>

<p>
<b>Característica:</b> Mesmo com premissas verdadeiras, conclusão é apenas <b>provável</b>.
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org63d2e15">
Cisne 1 é branco
Cisne 2 é branco
Cisne 3 é branco
(observei 1000 cisnes brancos)
──────────────────────────────
Todos os cisnes são brancos (?)
</pre>

<p>
<b>Problema:</b> Pode ser refutado por um contraexemplo (cisnes negros existem na Austrália).
</p>
</div>
</div>

<div id="outline-container-org2682fd9" class="outline-5">
<h5 id="org2682fd9"><span class="section-number-5">2.5.8.3.</span> 3. Argumento por Analogia</h5>
<div class="outline-text-5" id="text-2-5-8-3">
<p>
<b>Definição:</b> Conclui que algo é verdadeiro com base em semelhanças com outra situação.
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgce225c8">
A Terra tem água e vida
Marte tem (ou teve) água
───────────────────────────
Marte pode ter (ou ter tido) vida
</pre>
</div>
</div>
</div>

<div id="outline-container-org000937e" class="outline-4">
<h4 id="org000937e"><span class="section-number-4">2.5.9.</span> Falácias</h4>
<div class="outline-text-4" id="text-2-5-9">
<p>
<b>Falácia</b> é um erro de raciocínio que torna um argumento inválido, mesmo que pareça convincente.
</p>

<p>
<b>Tipos principais:</b>
</p>
</div>

<div id="outline-container-org7b64262" class="outline-5">
<h5 id="org7b64262"><span class="section-number-5">2.5.9.1.</span> 1. Falácia do Apelo à Autoridade (Ad Verecundiam)</h5>
<div class="outline-text-5" id="text-2-5-9-1">
<p>
<b>Erro:</b> Aceitar algo como verdadeiro apenas porque uma autoridade disse, sem analisar os argumentos.
</p>

<p>
<b>Exemplo:</b> “O ator famoso X disse que este produto emagrece, então deve ser verdade.”
</p>

<p>
<b>Por que é falácia:</b> Atores não são especialistas em nutrição.
</p>

<p>
<b>Quando NÃO é falácia:</b> Citar um especialista relevante com argumento (“Segundo o oncologista Dr. Y, fumar aumenta risco de câncer porque&#x2026;”)
</p>
</div>
</div>

<div id="outline-container-org9b634db" class="outline-5">
<h5 id="org9b634db"><span class="section-number-5">2.5.9.2.</span> 2. Falácia Ad Hominem (Ataque à Pessoa)</h5>
<div class="outline-text-5" id="text-2-5-9-2">
<p>
<b>Erro:</b> Atacar a pessoa em vez de refutar o argumento.
</p>

<p>
<b>Exemplo:</b> “Você não pode falar sobre honestidade porque já foi preso.”
</p>

<p>
<b>Por que é falácia:</b> A validade do argumento independe de quem o apresenta.
</p>
</div>
</div>

<div id="outline-container-org8e74b88" class="outline-5">
<h5 id="org8e74b88"><span class="section-number-5">2.5.9.3.</span> 3. Falácia do Apelo à Emoção (Ad Misericordiam, Ad Populum)</h5>
<div class="outline-text-5" id="text-2-5-9-3">
<p>
<b>Erro:</b> Usar emoções (piedade, medo, popularidade) em vez de razões lógicas.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li><b>Ad Misericordiam (piedade):</b> “Professor, não me reprove, minha mãe vai ficar muito triste!”</li>
<li><b>Ad Populum (popularidade):</b> “Todo mundo usa drogas, logo não é errado.”</li>
<li><b>Apelo ao medo:</b> “Se você não votar em mim, o país vai acabar!”</li>
</ul>
</div>
</div>

<div id="outline-container-org06bbb12" class="outline-5">
<h5 id="org06bbb12"><span class="section-number-5">2.5.9.4.</span> 4. Petição de Princípio (Raciocínio Circular)</h5>
<div class="outline-text-5" id="text-2-5-9-4">
<p>
<b>Erro:</b> A conclusão já está pressuposta nas premissas.
</p>

<p>
<b>Exemplo:</b> “Deus existe porque está escrito na Bíblia, e a Bíblia é verdadeira porque é a palavra de Deus.”
</p>

<p>
<b>Por que é falácia:</b> Usa a conclusão (Deus existe) para justificar a premissa (Bíblia é verdadeira).
</p>
</div>
</div>

<div id="outline-container-org2b2e607" class="outline-5">
<h5 id="org2b2e607"><span class="section-number-5">2.5.9.5.</span> 5. Falsa Causa (Post Hoc Ergo Propter Hoc)</h5>
<div class="outline-text-5" id="text-2-5-9-5">
<p>
<b>Erro:</b> Assumir que porque B veio depois de A, então A causou B.
</p>

<p>
<b>Exemplo:</b> “Usei este amuleto e passei na prova, logo o amuleto me deu sorte.”
</p>

<p>
<b>Por que é falácia:</b> Correlação não implica causalidade.
</p>
</div>
</div>

<div id="outline-container-orgd3f1703" class="outline-5">
<h5 id="orgd3f1703"><span class="section-number-5">2.5.9.6.</span> 6. Falso Dilema (Falsa Dicotomia)</h5>
<div class="outline-text-5" id="text-2-5-9-6">
<p>
<b>Erro:</b> Apresentar apenas duas opções quando existem mais.
</p>

<p>
<b>Exemplo:</b> “Ou você está comigo ou contra mim.”
</p>

<p>
<b>Por que é falácia:</b> Pode-se ser neutro, ou ter posição intermediária.
</p>
</div>
</div>

<div id="outline-container-org67cf4e4" class="outline-5">
<h5 id="org67cf4e4"><span class="section-number-5">2.5.9.7.</span> 7. Generalização Apressada</h5>
<div class="outline-text-5" id="text-2-5-9-7">
<p>
<b>Erro:</b> Concluir algo geral a partir de poucos casos.
</p>

<p>
<b>Exemplo:</b> “Conheci dois franceses arrogantes, logo todos os franceses são arrogantes.”
</p>

<p>
<b>Por que é falácia:</b> Amostra muito pequena para generalizar.
</p>
</div>
</div>

<div id="outline-container-org8a541cf" class="outline-5">
<h5 id="org8a541cf"><span class="section-number-5">2.5.9.8.</span> 8. Espantalho (Straw Man)</h5>
<div class="outline-text-5" id="text-2-5-9-8">
<p>
<b>Erro:</b> Distorcer o argumento do oponente para atacar uma versão mais fraca.
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A: “Devemos ter controle de armas mais rigoroso.”</li>
<li>B: “Você quer desarmar toda a população e deixar todos indefesos!”</li>
</ul>

<p>
<b>Por que é falácia:</b> B distorceu o argumento de A.
</p>
</div>
</div>

<div id="outline-container-org6d16d84" class="outline-5">
<h5 id="org6d16d84"><span class="section-number-5">2.5.9.9.</span> 9. Derrapagem (Slippery Slope)</h5>
<div class="outline-text-5" id="text-2-5-9-9">
<p>
<b>Erro:</b> Afirmar que uma ação levará inevitavelmente a consequências extremas.
</p>

<p>
<b>Exemplo:</b> “Se legalizarmos a maconha, em breve terão cocaína e heroína em todas as esquinas!”
</p>

<p>
<b>Por que é falácia:</b> Não há necessariamente essa cadeia inevitável.
</p>
</div>
</div>
</div>

<div id="outline-container-org84ffa77" class="outline-4">
<h4 id="org84ffa77"><span class="section-number-4">2.5.10.</span> Princípios Lógicos Fundamentais</h4>
<div class="outline-text-4" id="text-2-5-10">
</div>
<div id="outline-container-org3867af6" class="outline-5">
<h5 id="org3867af6"><span class="section-number-5">2.5.10.1.</span> 1. Princípio da Identidade</h5>
<div class="outline-text-5" id="text-2-5-10-1">
<p>
<b>A é A</b>
</p>

<p>
Uma coisa é igual a si mesma.
</p>
</div>
</div>

<div id="outline-container-orgb9520c3" class="outline-5">
<h5 id="orgb9520c3"><span class="section-number-5">2.5.10.2.</span> 2. Princípio da Não-Contradição</h5>
<div class="outline-text-5" id="text-2-5-10-2">
<p>
<b>A não pode ser A e não-A ao mesmo tempo e no mesmo sentido</b>
</p>

<p>
Uma proposição não pode ser verdadeira e falsa simultaneamente.
</p>

<p>
<b>Exemplo:</b> “Está chovendo” e “Não está chovendo” não podem ser ambas verdadeiras ao mesmo tempo no mesmo lugar.
</p>
</div>
</div>

<div id="outline-container-org3ca1777" class="outline-5">
<h5 id="org3ca1777"><span class="section-number-5">2.5.10.3.</span> 3. Princípio do Terceiro Excluído</h5>
<div class="outline-text-5" id="text-2-5-10-3">
<p>
<b>Ou A ou não-A (não há terceira opção)</b>
</p>

<p>
Uma proposição é verdadeira ou falsa, não há meio termo.
</p>
</div>
</div>
</div>

<div id="outline-container-org0bb1cb3" class="outline-4">
<h4 id="org0bb1cb3"><span class="section-number-4">2.5.11.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-5-11">
</div>
<div id="outline-container-orgd018eb6" class="outline-5">
<h5 id="orgd018eb6"><span class="section-number-5">2.5.11.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-5-11-1">
<p>
Identifique as premissas e a conclusão: “Todos os mamíferos têm coração. As baleias são mamíferos. Portanto, as baleias têm coração.”
</p>

<p>
<b>Resposta:</b>
</p>
<ul class="org-ul">
<li>Premissa 1: Todos os mamíferos têm coração</li>
<li>Premissa 2: As baleias são mamíferos</li>
<li>Conclusão: As baleias têm coração</li>
</ul>
</div>
</div>

<div id="outline-container-orgf1e9203" class="outline-5">
<h5 id="orgf1e9203"><span class="section-number-5">2.5.11.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-5-11-2">
<p>
O argumento abaixo é válido ou inválido? “Todos os gatos são felinos. Todos os felinos são carnívoros. Logo, todos os gatos são carnívoros.”
</p>

<p>
<i>[Ver resposta 41 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1e867ef" class="outline-5">
<h5 id="org1e867ef"><span class="section-number-5">2.5.11.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-5-11-3">
<p>
Identifique a falácia: “Você não pode criticar o governo porque não é político.”
</p>

<p>
<i>[Ver resposta 42 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orge0c1068" class="outline-5">
<h5 id="orge0c1068"><span class="section-number-5">2.5.11.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-5-11-4">
<p>
Identifique a falácia: “Ou você apoia este projeto ou é contra o progresso da cidade.”
</p>

<p>
<i>[Ver resposta 43 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org2c7fe6a" class="outline-5">
<h5 id="org2c7fe6a"><span class="section-number-5">2.5.11.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-5-11-5">
<p>
Este argumento é válido? “Alguns políticos são corruptos. João é político. Logo, João é corrupto.”
</p>

<p>
<i>[Ver resposta 44 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org65be540" class="outline-4">
<h4 id="org65be540"><span class="section-number-4">2.5.12.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-5-12">
<ol class="org-ol">
<li><b>Validade ≠ Verdade:</b> Validade é estrutura; verdade é correspondência com a realidade</li>
<li><b>Identifique indicadores:</b> “logo”, “portanto” → conclusão; “porque”, “pois” → premissa</li>
<li><b>Falácias comuns:</b> Ad Hominem, Apelo à Autoridade, Falso Dilema</li>
<li><b>Argumento válido:</b> SE premissas verdadeiras → conclusão necessariamente verdadeira</li>
<li><b>Argumento sólido:</b> Válido + premissas verdadeiras</li>
<li><b>Atenção a “todos”, “alguns”, “nenhum”:</b> mudam completamente a validade</li>
</ol>
</div>
</div>

<div id="outline-container-orgb27ecfc" class="outline-4">
<h4 id="orgb27ecfc"><span class="section-number-4">2.5.13.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-5-13">
<p>
<b>Argumento:</b>
</p>
<ul class="org-ul">
<li>Premissas (razões) + Conclusão (o que se quer provar)</li>
</ul>

<p>
<b>Validade:</b>
</p>
<ul class="org-ul">
<li>Estrutura correta</li>
<li>SE premissas verdadeiras → conclusão necessariamente verdadeira</li>
<li>Não depende da verdade das premissas</li>
</ul>

<p>
<b>Argumento Sólido:</b>
</p>
<ul class="org-ul">
<li>Válido + Premissas verdadeiras</li>
</ul>

<p>
<b>Falácias principais:</b>
</p>
<ul class="org-ul">
<li><b>Ad Hominem:</b> ataca a pessoa</li>
<li><b>Apelo à Autoridade:</b> autoridade sem expertise</li>
<li><b>Apelo à Emoção:</b> manipula emoções</li>
<li><b>Falso Dilema:</b> só duas opções (quando há mais)</li>
<li><b>Petição de Princípio:</b> circular</li>
<li><b>Falsa Causa:</b> confunde correlação com causalidade</li>
<li><b>Espantalho:</b> distorce argumento alheio</li>
</ul>
</div>
</div>

<div id="outline-container-org5c15e9d" class="outline-4">
<h4 id="org5c15e9d"><span class="section-number-4">2.5.14.</span> Tabela Resumo</h4>
<div class="outline-text-4" id="text-2-5-14">
<pre class="example" id="org510e6fa">
┌──────────────────┬───────────────────────────┐
│    Conceito      │        Definição          │
├──────────────────┼───────────────────────────┤
│ Proposição       │ Afirmação V ou F          │
│ Premissa         │ Razão/suporte             │
│ Conclusão        │ O que se quer provar      │
│ Validade         │ Estrutura correta         │
│ Verdade          │ Corresponde à realidade   │
│ Argumento Sólido │ Válido + premissas V      │
│ Falácia          │ Erro de raciocínio        │
└──────────────────┴───────────────────────────┘
</pre>
</div>
</div>

<div id="outline-container-org85a9576" class="outline-4">
<h4 id="org85a9576"><span class="section-number-4">2.5.15.</span> Estrutura Básica de Análise</h4>
<div class="outline-text-4" id="text-2-5-15">
<p>
<b>Para analisar um argumento:</b>
</p>

<ol class="org-ol">
<li><b>Identificar:</b> Quais são as premissas? Qual é a conclusão?</li>
<li><b>Avaliar a validade:</b> A conclusão decorre logicamente das premissas?</li>
<li><b>Avaliar a verdade:</b> As premissas são verdadeiras?</li>
<li><b>Identificar falácias:</b> Há erros de raciocínio?</li>
<li><b>Conclusão:</b> O argumento é sólido (válido + premissas verdadeiras)?</li>
</ol>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (importante
</p>
<ul class="org-ul">
<li>pensamento crítico é essencial)</li>
</ul>

<hr />
</div>
</div>
</div>
</div>

<div id="outline-container-org4590a6b" class="outline-2">`;

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
