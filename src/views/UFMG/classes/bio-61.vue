<script setup lang="ts">
import { ref } from "vue";

const code = "bio-61";
const title = "Biologia: Níveis de Organização dos Seres Vivos";
const subject = "biologia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-5">
<ul class="org-ul">
<li>Biologia: Níveis de Organização dos Seres Vivos</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org48d7b56" class="outline-4">
<h4 id="org48d7b56"><span class="section-number-4">5.5.1.</span> Introdução</h4>
<div class="outline-text-4" id="text-5-5-1">
<p>
<b>Organização biológica:</b> hierarquia estrutural desde os átomos até a biosfera
</p>

<p>
<b>Importância:</b>
</p>
<ul class="org-ul">
<li>Compreender como a vida se organiza</li>
<li>Entender relações entre diferentes níveis</li>
<li>Base para todas as áreas da biologia</li>
</ul>

<p>
<b>Princípio fundamental:</b> cada nível possui <b>propriedades emergentes</b> (características que surgem apenas naquele nível)
</p>
</div>
</div>

<div id="outline-container-orgd79c828" class="outline-4">
<h4 id="orgd79c828"><span class="section-number-4">5.5.2.</span> Níveis de Organização</h4>
<div class="outline-text-4" id="text-5-5-2">
<p>
<b>Hierarquia (do menor ao maior):</b>
</p>

<ol class="org-ol">
<li>Átomos</li>
<li>Moléculas</li>
<li>Organelas</li>
<li>Células</li>
<li>Tecidos</li>
<li>Órgãos</li>
<li>Sistemas</li>
<li>Organismo</li>
<li>População</li>
<li>Comunidade</li>
<li>Ecossistema</li>
<li>Biosfera</li>
</ol>
</div>
</div>

<div id="outline-container-orgd66bee2" class="outline-4">
<h4 id="orgd66bee2"><span class="section-number-4">5.5.3.</span> Nível 1: Átomos</h4>
<div class="outline-text-4" id="text-5-5-3">
<p>
<b>Definição:</b> unidades básicas da matéria
</p>

<p>
<b>Elementos essenciais à vida:</b>
</p>
<ul class="org-ul">
<li><b>C (Carbono):</b> base das moléculas orgânicas</li>
<li><b>H (Hidrogênio):</b> água, compostos orgânicos</li>
<li><b>O (Oxigênio):</b> água, respiração, compostos orgânicos</li>
<li><b>N (Nitrogênio):</b> proteínas, ácidos nucleicos</li>
<li><b>P (Fósforo):</b> ATP, DNA, RNA</li>
<li><b>S (Enxofre):</b> algumas proteínas</li>
</ul>

<p>
<b>Exemplo:</b> átomo de carbono (C), oxigênio (O₂)
</p>
</div>
</div>

<div id="outline-container-org19ca1e8" class="outline-4">
<h4 id="org19ca1e8"><span class="section-number-4">5.5.4.</span> Nível 2: Moléculas</h4>
<div class="outline-text-4" id="text-5-5-4">
<p>
<b>Definição:</b> átomos ligados quimicamente
</p>

<p>
<b>Tipos:</b>
</p>

<p>
<b>Moléculas inorgânicas:</b>
</p>
<ul class="org-ul">
<li>Água (H₂O)</li>
<li>Sais minerais (NaCl, CaCO₃)</li>
<li>Gases (O₂, CO₂)</li>
</ul>

<p>
<b>Moléculas orgânicas (macromoléculas):</b>
</p>
<ul class="org-ul">
<li><b>Carboidratos:</b> glicose, amido, celulose</li>
<li><b>Lipídios:</b> triglicerídeos, fosfolipídios</li>
<li><b>Proteínas:</b> enzimas, anticorpos, colágeno</li>
<li><b>Ácidos nucleicos:</b> DNA, RNA</li>
</ul>

<p>
<b>Exemplo:</b> molécula de glicose (C₆H₁₂O₆), proteína hemoglobina
</p>
</div>
</div>

<div id="outline-container-org2442bb4" class="outline-4">
<h4 id="org2442bb4"><span class="section-number-4">5.5.5.</span> Nível 3: Organelas</h4>
<div class="outline-text-4" id="text-5-5-5">
<p>
<b>Definição:</b> estruturas especializadas dentro das células
</p>

<p>
<b>Principais organelas:</b>
</p>

<p>
<b>Núcleo:</b>
</p>
<ul class="org-ul">
<li>Contém DNA</li>
<li>Controla atividades celulares</li>
</ul>

<p>
<b>Mitocôndrias:</b>
</p>
<ul class="org-ul">
<li>Respiração celular</li>
<li>Produção de ATP (energia)</li>
</ul>

<p>
<b>Ribossomos:</b>
</p>
<ul class="org-ul">
<li>Síntese de proteínas</li>
</ul>

<p>
<b>Retículo Endoplasmático (RE):</b>
</p>
<ul class="org-ul">
<li>RE rugoso: síntese e transporte de proteínas</li>
<li>RE liso: síntese de lipídios</li>
</ul>

<p>
<b>Complexo de Golgi:</b>
</p>
<ul class="org-ul">
<li>Modificação e secreção de proteínas</li>
</ul>

<p>
<b>Lisossomos:</b>
</p>
<ul class="org-ul">
<li>Digestão intracelular</li>
</ul>

<p>
<b>Cloroplastos (só em células vegetais):</b>
</p>
<ul class="org-ul">
<li>Fotossíntese</li>
</ul>

<p>
<b>Vacúolos (principalmente vegetais):</b>
</p>
<ul class="org-ul">
<li>Armazenamento</li>
</ul>

<p>
<b>Exemplo:</b> mitocôndria, cloroplasto, núcleo
</p>

<p>
<b>Propriedade emergente:</b> capacidade de realizar funções específicas (fotossíntese, respiração)
</p>
</div>
</div>

<div id="outline-container-org5fa4674" class="outline-4">
<h4 id="org5fa4674"><span class="section-number-4">5.5.6.</span> Nível 4: Célula</h4>
<div class="outline-text-4" id="text-5-5-6">
<p>
<b>Definição:</b> <b>unidade básica da vida</b>
</p>

<p>
<b>“Toda célula vem de outra célula”</b> (Virchow)
</p>

<p>
<b>Tipos:</b>
</p>

<p>
<b>Célula procariótica:</b>
</p>
<ul class="org-ul">
<li>Sem núcleo definido (DNA disperso)</li>
<li>Sem organelas membranosas</li>
<li>Simples</li>
<li>Exemplo: bactérias, cianobactérias</li>
</ul>

<p>
<b>Célula eucariótica:</b>
</p>
<ul class="org-ul">
<li>Núcleo definido (DNA no núcleo)</li>
<li>Organelas membranosas</li>
<li>Complexa</li>
<li>Exemplos: células animais, vegetais, fungos, protozoários</li>
</ul>

<p>
<b>Tipos de organismos:</b>
</p>
<ul class="org-ul">
<li><b>Unicelulares:</b> 1 célula (bactérias, protozoários, algumas algas)</li>
<li><b>Multicelulares:</b> muitas células (animais, plantas, fungos)</li>
</ul>

<p>
<b>Exemplo:</b> neurônio, hemácia, célula vegetal
</p>

<p>
<b>Propriedade emergente:</b> <b>vida</b> (metabolismo, reprodução, resposta a estímulos)
</p>
</div>
</div>

<div id="outline-container-orgc30cc38" class="outline-4">
<h4 id="orgc30cc38"><span class="section-number-4">5.5.7.</span> Nível 5: Tecido</h4>
<div class="outline-text-4" id="text-5-5-7">
<p>
<b>Definição:</b> conjunto de células <b>semelhantes</b> que realizam função <b>específica</b>
</p>

<p>
<b>Só existe em organismos multicelulares!</b>
</p>

<p>
<b>Tecidos animais principais:</b>
</p>

<p>
<b>1. Tecido Epitelial:</b>
</p>
<ul class="org-ul">
<li>Revestimento e proteção</li>
<li>Glândulas (secreção)</li>
<li>Exemplos: pele, mucosas</li>
</ul>

<p>
<b>2. Tecido Conjuntivo:</b>
</p>
<ul class="org-ul">
<li>Sustentação, preenchimento, transporte</li>
<li>Tipos: ósseo, cartilaginoso, adiposo, sanguíneo</li>
<li>Exemplos: ossos, sangue, tendões</li>
</ul>

<p>
<b>3. Tecido Muscular:</b>
</p>
<ul class="org-ul">
<li>Movimento e contração</li>
<li>Tipos: estriado esquelético, estriado cardíaco, liso</li>
<li>Exemplos: músculos dos braços, coração</li>
</ul>

<p>
<b>4. Tecido Nervoso:</b>
</p>
<ul class="org-ul">
<li>Transmissão de impulsos nervosos</li>
<li>Células: neurônios</li>
<li>Exemplos: cérebro, nervos</li>
</ul>

<p>
<b>Tecidos vegetais principais:</b>
</p>

<p>
<b>Meristemas:</b> crescimento (células indiferenciadas) <b>Parênquima:</b> fotossíntese, reserva <b>Xilema:</b> condução de seiva bruta (água e sais) <b>Floema:</b> condução de seiva elaborada (açúcares) <b>Epiderme:</b> revestimento e proteção
</p>

<p>
<b>Exemplo:</b> tecido muscular cardíaco, tecido nervoso
</p>

<p>
<b>Propriedade emergente:</b> função especializada (contração muscular, condução nervosa)
</p>
</div>
</div>

<div id="outline-container-org032c941" class="outline-4">
<h4 id="org032c941"><span class="section-number-4">5.5.8.</span> Nível 6: Órgão</h4>
<div class="outline-text-4" id="text-5-5-8">
<p>
<b>Definição:</b> conjunto de <b>tecidos</b> que trabalham juntos para realizar função(ões) específica(s)
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Composto por vários tecidos</li>
<li>Forma e função definidas</li>
<li>Parte de um sistema</li>
</ul>

<p>
<b>Exemplos animais:</b>
</p>
<ul class="org-ul">
<li><b>Coração:</b> tecido muscular + nervoso + epitelial + conjuntivo</li>
<li><b>Estômago:</b> epitelial + muscular + conjuntivo + nervoso</li>
<li><b>Pulmão:</b> epitelial + conjuntivo + muscular</li>
<li><b>Olho, rim, fígado, cérebro</b></li>
</ul>

<p>
<b>Exemplos vegetais:</b>
</p>
<ul class="org-ul">
<li><b>Folha:</b> fotossíntese</li>
<li><b>Raiz:</b> absorção, fixação</li>
<li><b>Caule:</b> sustentação, transporte</li>
<li><b>Flor:</b> reprodução</li>
</ul>

<p>
<b>Exemplo:</b> coração (bombeia sangue), pulmão (trocas gasosas)
</p>

<p>
<b>Propriedade emergente:</b> função complexa e integrada
</p>
</div>
</div>

<div id="outline-container-org015a428" class="outline-4">
<h4 id="org015a428"><span class="section-number-4">5.5.9.</span> Nível 7: Sistema (ou Sistema de Órgãos)</h4>
<div class="outline-text-4" id="text-5-5-9">
<p>
<b>Definição:</b> conjunto de <b>órgãos</b> que trabalham de forma integrada para realizar função(ões) vitais
</p>

<p>
<b>Principais sistemas do corpo humano:</b>
</p>

<p>
<b>1. Sistema Circulatório:</b>
</p>
<ul class="org-ul">
<li>Órgãos: coração, vasos sanguíneos</li>
<li>Função: transporte de sangue, nutrientes, O₂, CO₂</li>
</ul>

<p>
<b>2. Sistema Respiratório:</b>
</p>
<ul class="org-ul">
<li>Órgãos: pulmões, traqueia, brônquios</li>
<li>Função: trocas gasosas (O₂ e CO₂)</li>
</ul>

<p>
<b>3. Sistema Digestório:</b>
</p>
<ul class="org-ul">
<li>Órgãos: boca, esôfago, estômago, intestinos</li>
<li>Função: digestão e absorção de nutrientes</li>
</ul>

<p>
<b>4. Sistema Nervoso:</b>
</p>
<ul class="org-ul">
<li>Órgãos: cérebro, medula espinhal, nervos</li>
<li>Função: coordenação, controle, sensações</li>
</ul>

<p>
<b>5. Sistema Endócrino:</b>
</p>
<ul class="org-ul">
<li>Órgãos: glândulas (hipófise, tireoide, pâncreas)</li>
<li>Função: produção de hormônios, regulação</li>
</ul>

<p>
<b>6. Sistema Excretor (Urinário):</b>
</p>
<ul class="org-ul">
<li>Órgãos: rins, bexiga, ureteres</li>
<li>Função: filtração do sangue, eliminação de excretas</li>
</ul>

<p>
<b>7. Sistema Reprodutor:</b>
</p>
<ul class="org-ul">
<li>Órgãos: testículos/ovários, útero</li>
<li>Função: reprodução</li>
</ul>

<p>
<b>8. Sistema Muscular:</b>
</p>
<ul class="org-ul">
<li>Órgãos: músculos esqueléticos</li>
<li>Função: movimento, locomoção</li>
</ul>

<p>
<b>9. Sistema Esquelético:</b>
</p>
<ul class="org-ul">
<li>Órgãos: ossos, articulações</li>
<li>Função: sustentação, proteção, movimento</li>
</ul>

<p>
<b>10. Sistema Tegumentar:</b>
</p>
<ul class="org-ul">
<li>Órgãos: pele, pelos, unhas</li>
<li>Função: proteção, termorregulação</li>
</ul>

<p>
<b>Exemplo:</b> sistema digestório (digestão completa de alimentos)
</p>

<p>
<b>Propriedade emergente:</b> função vital complexa
</p>
</div>
</div>

<div id="outline-container-org81fc83a" class="outline-4">
<h4 id="org81fc83a"><span class="section-number-4">5.5.10.</span> Nível 8: Organismo</h4>
<div class="outline-text-4" id="text-5-5-10">
<p>
<b>Definição:</b> ser vivo completo e funcional
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Todos os sistemas integrados</li>
<li>Capaz de viver de forma independente</li>
<li>Realiza todas as funções vitais</li>
</ul>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li><b>Unicelulares:</b> 1 célula = 1 organismo (bactérias, protozoários)</li>
<li><b>Multicelulares:</b> muitas células formam 1 organismo (humanos, árvores)</li>
</ul>

<p>
<b>Exemplo:</b> ser humano, cachorro, pé de feijão, bactéria
</p>

<p>
<b>Propriedade emergente:</b> individualidade, autonomia
</p>
</div>
</div>

<div id="outline-container-org05d343b" class="outline-4">
<h4 id="org05d343b"><span class="section-number-4">5.5.11.</span> Nível 9: População</h4>
<div class="outline-text-4" id="text-5-5-11">
<p>
<b>Definição:</b> conjunto de organismos da <b>mesma espécie</b> vivendo na <b>mesma área</b> ao <b>mesmo tempo</b>
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Mesma espécie (podem se reproduzir entre si)</li>
<li>Mesma área geográfica</li>
<li>Mesmo período de tempo</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>População de onças-pintadas no Pantanal</li>
<li>População de humanos em Belo Horizonte</li>
<li>População de bactérias em uma cultura</li>
</ul>

<p>
<b>Propriedades emergentes:</b>
</p>
<ul class="org-ul">
<li><b>Densidade populacional:</b> indivíduos/área</li>
<li><b>Taxa de natalidade e mortalidade</b></li>
<li><b>Crescimento populacional</b></li>
<li><b>Estrutura etária</b> (pirâmide etária)</li>
</ul>

<p>
<b>Exemplo:</b> todos os pinheiros de uma floresta
</p>
</div>
</div>

<div id="outline-container-org05ce265" class="outline-4">
<h4 id="org05ce265"><span class="section-number-4">5.5.12.</span> Nível 10: Comunidade (ou Biocenose)</h4>
<div class="outline-text-4" id="text-5-5-12">
<p>
<b>Definição:</b> conjunto de <b>populações</b> de diferentes <b>espécies</b> vivendo e interagindo na <b>mesma área</b>
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Várias espécies</li>
<li>Interações ecológicas (predação, competição, mutualismo, etc.)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Comunidade da Mata Atlântica: árvores + macacos + aves + insetos + fungos + bactérias</li>
<li>Comunidade de um lago: peixes + algas + plantas aquáticas + bactérias</li>
</ul>

<p>
<b>Propriedades emergentes:</b>
</p>
<ul class="org-ul">
<li><b>Diversidade de espécies</b> (biodiversidade)</li>
<li><b>Relações ecológicas</b> (predação, parasitismo, mutualismo)</li>
<li><b>Cadeia alimentar</b></li>
<li><b>Nicho ecológico</b></li>
</ul>

<p>
<b>Exemplo:</b> todos os seres vivos de um recife de coral
</p>
</div>
</div>

<div id="outline-container-org10aaa19" class="outline-4">
<h4 id="org10aaa19"><span class="section-number-4">5.5.13.</span> Nível 11: Ecossistema</h4>
<div class="outline-text-4" id="text-5-5-13">
<p>
<b>Definição:</b> conjunto da <b>comunidade</b> (seres vivos) + <b>fatores abióticos</b> (ambiente físico)
</p>

<p>
<b>Componentes:</b>
</p>

<p>
<b>Bióticos (vivos):</b>
</p>
<ul class="org-ul">
<li>Todos os seres vivos (comunidade)</li>
<li>Produtores, consumidores, decompositores</li>
</ul>

<p>
<b>Abióticos (não vivos):</b>
</p>
<ul class="org-ul">
<li>Água, ar, solo, luz, temperatura, nutrientes</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Ecossistema amazônico</li>
<li>Ecossistema marinho</li>
<li>Ecossistema de uma lagoa</li>
</ul>

<p>
<b>Propriedades emergentes:</b>
</p>
<ul class="org-ul">
<li><b>Fluxo de energia</b> (sol → produtores → consumidores)</li>
<li><b>Ciclos biogeoquímicos</b> (água, carbono, nitrogênio)</li>
<li><b>Produtividade primária</b></li>
<li><b>Sucessão ecológica</b></li>
</ul>

<p>
<b>Exemplo:</b> floresta amazônica (plantas + animais + microorganismos + solo + clima)
</p>
</div>
</div>

<div id="outline-container-orgf5b33b7" class="outline-4">
<h4 id="orgf5b33b7"><span class="section-number-4">5.5.14.</span> Nível 12: Biosfera</h4>
<div class="outline-text-4" id="text-5-5-14">
<p>
<b>Definição:</b> conjunto de <b>todos os ecossistemas da Terra</b>
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Maior nível de organização</li>
<li>Inclui toda a vida na Terra</li>
<li>Atmosfera + hidrosfera + litosfera (partes habitadas)</li>
</ul>

<p>
<b>Limites:</b>
</p>
<ul class="org-ul">
<li>~10 km de altitude (atmosfera)</li>
<li>Profundidade oceânica (~11 km)</li>
<li>Alguns metros no solo</li>
</ul>

<p>
<b>Propriedade emergente:</b>
</p>
<ul class="org-ul">
<li><b>Sistema global integrado</b></li>
<li><b>Regulação do clima global</b></li>
<li><b>Ciclos globais de elementos</b></li>
</ul>

<p>
<b>Exemplo:</b> toda a vida na Terra
</p>
</div>
</div>

<div id="outline-container-org62e1345" class="outline-4">
<h4 id="org62e1345"><span class="section-number-4">5.5.15.</span> Resumo dos Níveis Ecológicos</h4>
<div class="outline-text-4" id="text-5-5-15">
<p>
<b>Níveis de organização ecológica (importantes para provas!):</b>
</p>

<pre class="example" id="org749520b">
Organismo → População → Comunidade → Ecossistema → Biosfera

Organismo: 1 indivíduo
População: mesma espécie, mesma área
Comunidade: várias espécies, mesma área
Ecossistema: comunidade + ambiente
Biosfera: todos os ecossistemas da Terra
</pre>
</div>
</div>

<div id="outline-container-orgfefebc4" class="outline-4">
<h4 id="orgfefebc4"><span class="section-number-4">5.5.16.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-5-16">
</div>
<div id="outline-container-org4f15a5c" class="outline-5">
<h5 id="org4f15a5c"><span class="section-number-5">5.5.16.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-5-16-1">
<p>
Qual a diferença entre célula procariótica e eucariótica?
</p>

<p>
<i>[Ver resposta 81 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb1b25d0" class="outline-5">
<h5 id="orgb1b25d0"><span class="section-number-5">5.5.16.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-5-16-2">
<p>
Qual é a unidade básica da vida?
</p>

<p>
<i>[Ver resposta 82 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgfee3f4d" class="outline-5">
<h5 id="orgfee3f4d"><span class="section-number-5">5.5.16.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-5-16-3">
<p>
(UFMG) Todos os peixes de um lago formam: a) Uma comunidade b) Uma população c) Um ecossistema d) Um organismo
</p>

<p>
<i>[Ver resposta 83 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orga1344be" class="outline-5">
<h5 id="orga1344be"><span class="section-number-5">5.5.16.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-5-16-4">
<p>
Defina ecossistema.
</p>

<p>
<i>[Ver resposta 84 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org16420ad" class="outline-5">
<h5 id="org16420ad"><span class="section-number-5">5.5.16.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-5-16-5">
<p>
Qual a diferença entre população e comunidade?
</p>

<p>
<i>[Ver resposta 85 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1893b08" class="outline-5">
<h5 id="org1893b08"><span class="section-number-5">5.5.16.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-5-5-16-6">
<p>
O que são propriedades emergentes?
</p>

<p>
<i>[Ver resposta 86 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgeb1884c" class="outline-5">
<h5 id="orgeb1884c"><span class="section-number-5">5.5.16.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-5-5-16-7">
<p>
Coloque em ordem crescente de organização: tecido, célula, organismo, órgão, organela.
</p>

<p>
<i>[Ver resposta 87 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgc211d7f" class="outline-4">
<h4 id="orgc211d7f"><span class="section-number-4">5.5.17.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-5-17">
<ol class="org-ol">
<li><b>Célula:</b> unidade básica da vida</li>
<li><b>Unicelular:</b> 1 célula; <b>Multicelular:</b> muitas células</li>
<li><b>Tecido:</b> células semelhantes, função específica</li>
<li><b>Órgão:</b> vários tecidos</li>
<li><b>Sistema:</b> vários órgãos</li>
<li><b>População:</b> mesma espécie, mesma área</li>
<li><b>Comunidade:</b> várias espécies, mesma área</li>
<li><b>Ecossistema:</b> comunidade + ambiente</li>
<li><b>Ordem:</b> átomo → molécula → organela → célula → tecido → órgão → sistema → organismo → população → comunidade → ecossistema → biosfera</li>
<li><b>Propriedade emergente:</b> surge em cada nível</li>
</ol>
</div>
</div>

<div id="outline-container-org9722cfc" class="outline-4">
<h4 id="org9722cfc"><span class="section-number-4">5.5.18.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-5-18">
<p>
<b>Hierarquia básica:</b>
</p>
<ul class="org-ul">
<li>Átomos → Moléculas → Organelas → Célula</li>
<li>Célula → Tecido → Órgão → Sistema → Organismo</li>
<li>Organismo → População → Comunidade → Ecossistema → Biosfera</li>
</ul>

<p>
<b>Diferenças importantes:</b>
</p>
<ul class="org-ul">
<li><b>Célula:</b> unidade básica da vida</li>
<li><b>Tecido:</b> só em multicelulares</li>
<li><b>População:</b> mesma espécie</li>
<li><b>Comunidade:</b> várias espécies</li>
<li><b>Ecossistema:</b> seres vivos + ambiente</li>
</ul>

<p>
<b>Propriedades emergentes:</b>
</p>
<ul class="org-ul">
<li>Cada nível tem características próprias</li>
<li>Não existem nos níveis inferiores</li>
</ul>
</div>
</div>

<div id="outline-container-orgbe08fba" class="outline-4">
<h4 id="orgbe08fba"><span class="section-number-4">5.5.19.</span> Tabela Resumo</h4>
<div class="outline-text-4" id="text-5-5-19">
<pre class="example" id="org3fe38b0">
┌───────────┬──────────────────────────────────────┐
│   Nível   │           Descrição                  │
├───────────┼──────────────────────────────────────┤
│ Átomo     │ Unidade básica da matéria (C, H, O)  │
│ Molécula  │ Átomos ligados (H₂O, glicose, DNA)   │
│ Organela  │ Estruturas celulares (núcleo, mitoc.)│
│ Célula    │ **Unidade básica da vida**           │
│ Tecido    │ Células semelhantes (muscular, ner.) │
│ Órgão     │ Tecidos juntos (coração, pulmão)     │
│ Sistema   │ Órgãos integrados (digestório, circ.)│
│ Organismo │ Ser vivo completo (humano, árvore)   │
│ População │ Mesma espécie, mesma área            │
│Comunidade │ Várias espécies, mesma área          │
│Ecossistema│ Comunidade + ambiente (Amazônia)     │
│ Biosfera  │ Todos ecossistemas da Terra          │
└───────────┴──────────────────────────────────────┘
</pre>
</div>
</div>

<div id="outline-container-org916a963" class="outline-4">
<h4 id="org916a963"><span class="section-number-4">5.5.20.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-5-20">
<pre class="example" id="org50515fd">
NÍVEIS DE ORGANIZAÇÃO:

Átomo (C, H, O, N)
  ↓
Molécula (H₂O, glicose, DNA)
  ↓
Organela (mitocôndria, núcleo)
  ↓
CÉLULA ← **Unidade da vida**
  ↓
Tecido (muscular, nervoso)
  ↓
Órgão (coração, pulmão)
  ↓
Sistema (circulatório, digestório)
  ↓
ORGANISMO (ser vivo completo)
  ↓
População (mesma espécie) 🐟🐟🐟
  ↓
Comunidade (várias espécies) 🐟🌿🦐🦀
  ↓
Ecossistema (comunidade + água/solo/luz) 🌍
  ↓
Biosfera (toda a vida na Terra) 🌎

NÍVEIS ECOLÓGICOS:

1 🐟           = Organismo
🐟🐟🐟         = População (mesma espécie)
🐟🌿🦐        = Comunidade (várias espécies)
🐟🌿🦐 + 💧☀️  = Ecossistema (+ ambiente)
🌎            = Biosfera (toda a Terra)

TIPOS DE CÉLULAS:

Procariótica:        Eucariótica:
  ╔═══════╗            ╔══════════╗
  ║ DNA   ║            ║ ┌──────┐ ║
  ║ disperso║          ║ │Núcleo│ ║
  ║       ║            ║ │ DNA  │ ║
  ╚═══════╝            ║ └──────┘ ║
                       ║ organelas║
  Bactérias            ╚══════════╝
                       Animais, plantas
</pre>
</div>
</div>

<div id="outline-container-orgc00483d" class="outline-4">
<h4 id="orgc00483d"><span class="section-number-4">5.5.21.</span> Principais Sistemas do Corpo Humano</h4>
<div class="outline-text-4" id="text-5-5-21">
<pre class="example" id="orgeaa72c1">
Sistema          Função Principal
───────────────────────────────────
Circulatório  →  Transporte (sangue)
Respiratório  →  Trocas gasosas (O₂/CO₂)
Digestório    →  Digestão/absorção
Nervoso       →  Coordenação/controle
Endócrino     →  Hormônios/regulação
Excretor      →  Filtração/eliminação
Reprodutor    →  Reprodução
Muscular      →  Movimento
Esquelético   →  Sustentação/proteção
Tegumentar    →  Proteção (pele)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Fácil-Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>conceitos fundamentais!)</li>
</ul>

<hr />
</div>
</div>
</div>
</div>

<div id="outline-container-org0d29ffb" class="outline-2">`;

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
