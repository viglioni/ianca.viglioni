<script setup lang="ts">
import { ref } from "vue";

const code = "geo-24";
const title = "Geografia: Cartografia";
const subject = "geografia";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-4">
<ul class="org-ul">
<li>Geografia: Cartografia</li>
<li>Parte 2</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org6a94122" class="outline-4">
<h4 id="org6a94122"><span class="section-number-4">5.4.1.</span> Revisão: Cartografia Parte 1</h4>
<div class="outline-text-4" id="text-5-4-1">
<p>
Na Aula 19, estudamos:
</p>
<ul class="org-ul">
<li>Orientação (pontos cardeais, Rosa dos Ventos)</li>
<li>Coordenadas geográficas (latitude e longitude)</li>
<li>Fusos horários</li>
<li>Escala (numérica e gráfica)</li>
</ul>

<p>
<b>Nesta aula:</b> projeções cartográficas, tipos de mapas e representações.
</p>
</div>
</div>

<div id="outline-container-org5f03dca" class="outline-4">
<h4 id="org5f03dca"><span class="section-number-4">5.4.2.</span> Projeções Cartográficas</h4>
<div class="outline-text-4" id="text-5-4-2">
<p>
<b>Problema fundamental:</b> representar uma superfície esférica (Terra) em um plano (mapa) sempre causa <b>distorções</b>.
</p>

<p>
<b>Projeção Cartográfica:</b> técnica matemática para transferir a superfície curva da Terra para um plano.
</p>

<p>
<b>Distorções inevitáveis:</b>
</p>
<ul class="org-ul">
<li><b>Forma</b> (deformação dos contornos)</li>
<li><b>Área</b> (tamanho relativo)</li>
<li><b>Distância</b> (comprimentos)</li>
<li><b>Ângulo/direção</b></li>
</ul>

<p>
<b>Importante:</b> NENHUMA projeção é perfeita! Cada uma tem vantagens e distorções.
</p>
</div>
</div>

<div id="outline-container-orgbcee0c7" class="outline-4">
<h4 id="orgbcee0c7"><span class="section-number-4">5.4.3.</span> Tipos de Projeções</h4>
<div class="outline-text-4" id="text-5-4-3">
</div>
<div id="outline-container-org2fd9bad" class="outline-5">
<h5 id="org2fd9bad"><span class="section-number-5">5.4.3.1.</span> 1. Quanto à Superfície de Projeção</h5>
<div class="outline-text-5" id="text-5-4-3-1">
<p>
<b>a) Projeção Cilíndrica</b>
</p>
<ul class="org-ul">
<li>Terra projetada sobre um cilindro</li>
<li>Cilindro depois “desenrolado”</li>
<li><b>Distorções:</b> aumentam perto dos polos</li>
<li><b>Preserva:</b> direções (ângulos)</li>
<li><b>Uso:</b> navegação, mapas-múndi</li>
</ul>

<p>
<b>Exemplo:</b> Projeção de Mercator
</p>

<pre class="example" id="org71c17fe">
   Cilindro
      ║║
    ╱ ║║ ╲
   │ Terra│
    ╲ ║║ ╱
      ║║
      
Desenrolado: [────────────]
</pre>

<p>
<b>b) Projeção Cônica</b>
</p>
<ul class="org-ul">
<li>Terra projetada sobre um cone</li>
<li>Cone depois “desenrolado”</li>
<li><b>Distorções:</b> menores em latitudes médias</li>
<li><b>Preserva:</b> formas em regiões específicas</li>
<li><b>Uso:</b> mapas de continentes, países</li>
</ul>

<pre class="example" id="org7ad5e2f">
   /\\
  /  \\
 / Terra
/____  \\
</pre>

<p>
<b>c) Projeção Azimutal (ou Plana)</b>
</p>
<ul class="org-ul">
<li>Terra projetada sobre um plano tangente</li>
<li><b>Distorções:</b> aumentam do centro para as bordas</li>
<li><b>Preserva:</b> distâncias a partir do centro</li>
<li><b>Uso:</b> mapas polares, rotas aéreas</li>
</ul>

<pre class="example" id="org7141394">
┌─────┐
│Plano│
└──┬──┘
 Terra
</pre>
</div>
</div>

<div id="outline-container-org6d4b7b3" class="outline-5">
<h5 id="org6d4b7b3"><span class="section-number-5">5.4.3.2.</span> 2. Quanto às Propriedades Preservadas</h5>
<div class="outline-text-5" id="text-5-4-3-2">
<p>
<b>a) Projeção Conforme</b>
</p>
<ul class="org-ul">
<li>Preserva <b>ângulos e formas</b> locais</li>
<li><b>Distorce áreas</b> (especialmente em altas latitudes)</li>
<li><b>Exemplo:</b> Mercator</li>
</ul>

<p>
<b>b) Projeção Equivalente</b>
</p>
<ul class="org-ul">
<li>Preserva <b>áreas</b> (proporções corretas)</li>
<li><b>Distorce formas</b></li>
<li><b>Exemplo:</b> Peters, Mollweide</li>
</ul>

<p>
<b>c) Projeção Equidistante</b>
</p>
<ul class="org-ul">
<li>Preserva <b>distâncias</b> a partir de um ponto</li>
<li><b>Distorce áreas e formas</b></li>
<li><b>Exemplo:</b> Azimutal equidistante</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org7509a00" class="outline-4">
<h4 id="org7509a00"><span class="section-number-4">5.4.4.</span> Principais Projeções</h4>
<div class="outline-text-4" id="text-5-4-4">
</div>
<div id="outline-container-org27bd3eb" class="outline-5">
<h5 id="org27bd3eb"><span class="section-number-5">5.4.4.1.</span> Projeção de Mercator (1569)</h5>
<div class="outline-text-5" id="text-5-4-4-1">
<p>
<b>Tipo:</b> Cilíndrica conforme
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Paralelos e meridianos formam ângulos retos</li>
<li><b>Preserva:</b> formas e ângulos (navegação)</li>
<li><b>Distorce:</b> áreas (altas latitudes muito exageradas)</li>
</ul>

<p>
<b>Distorções:</b>
</p>
<ul class="org-ul">
<li>Groenlândia parece maior que a África (na realidade, África é 14× maior)</li>
<li>Polos aparecem infinitamente grandes (não representados)</li>
</ul>

<p>
<b>Uso:</b>
</p>
<ul class="org-ul">
<li>Navegação marítima (mantém rumos constantes)</li>
<li>Mapas-múndi tradicionais</li>
</ul>

<p>
<b>Crítica:</b>
</p>
<ul class="org-ul">
<li><b>Eurocentrismo:</b> Europa no centro, exagerada</li>
<li>Distorce percepção geopolítica</li>
</ul>
</div>
</div>

<div id="outline-container-orge8e69fb" class="outline-5">
<h5 id="orge8e69fb"><span class="section-number-5">5.4.4.2.</span> Projeção de Peters (1973)</h5>
<div class="outline-text-5" id="text-5-4-4-2">
<p>
<b>Tipo:</b> Cilíndrica equivalente
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Preserva:</b> áreas (proporções corretas)</li>
<li><b>Distorce:</b> formas (continentes “esticados” verticalmente)</li>
</ul>

<p>
<b>Objetivo:</b>
</p>
<ul class="org-ul">
<li>Crítica à Mercator</li>
<li>Valorizar países tropicais e do Sul (tamanhos reais)</li>
</ul>

<p>
<b>Uso:</b>
</p>
<ul class="org-ul">
<li>Mapas temáticos</li>
<li>Representação mais justa das áreas</li>
</ul>

<p>
<b>Comparação Mercator vs Peters:</b>
</p>
<ul class="org-ul">
<li><b>Mercator:</b> Europa e América do Norte exageradas</li>
<li><b>Peters:</b> África e América do Sul em tamanho real</li>
</ul>
</div>
</div>

<div id="outline-container-orgcf32f3e" class="outline-5">
<h5 id="orgcf32f3e"><span class="section-number-5">5.4.4.3.</span> Projeção de Robinson</h5>
<div class="outline-text-5" id="text-5-4-4-3">
<p>
<b>Tipo:</b> Pseudo-cilíndrica
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li><b>Compromisso:</b> minimiza todas as distorções</li>
<li>Não preserva perfeitamente nada, mas equilibra</li>
<li>Meridianos curvos (não retilíneos)</li>
</ul>

<p>
<b>Uso:</b>
</p>
<ul class="org-ul">
<li>Mapas-múndi gerais</li>
<li>Adotada por National Geographic, ONU</li>
</ul>
</div>
</div>

<div id="outline-container-org027efde" class="outline-5">
<h5 id="org027efde"><span class="section-number-5">5.4.4.4.</span> Projeção Azimutal Polar</h5>
<div class="outline-text-5" id="text-5-4-4-4">
<p>
<b>Tipo:</b> Plana/Azimutal
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Centro: Polo Norte ou Polo Sul</li>
<li>Meridianos: raios do centro</li>
<li>Paralelos: círculos concêntricos</li>
</ul>

<p>
<b>Uso:</b>
</p>
<ul class="org-ul">
<li>Mapas polares</li>
<li>Geopolítica do Ártico</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org2f6d859" class="outline-4">
<h4 id="org2f6d859"><span class="section-number-4">5.4.5.</span> Tipos de Representações Cartográficas</h4>
<div class="outline-text-4" id="text-5-4-5">
</div>
<div id="outline-container-org6d180e2" class="outline-5">
<h5 id="org6d180e2"><span class="section-number-5">5.4.5.1.</span> Mapa</h5>
<div class="outline-text-5" id="text-5-4-5-1">
<p>
Representação plana da superfície terrestre em escala pequena (grande área).
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Mapa-múndi</li>
<li>Mapa do Brasil</li>
<li>Mapa político da América do Sul</li>
</ul>
</div>
</div>

<div id="outline-container-orgcd6ff3c" class="outline-5">
<h5 id="orgcd6ff3c"><span class="section-number-5">5.4.5.2.</span> Carta</h5>
<div class="outline-text-5" id="text-5-4-5-2">
<p>
Representação em escala média.
</p>

<p>
<b>Uso:</b> finalidades técnicas, científicas, navegação.
</p>

<p>
<b>Exemplo:</b> cartas náuticas, topográficas
</p>
</div>
</div>

<div id="outline-container-org5cfb9bd" class="outline-5">
<h5 id="org5cfb9bd"><span class="section-number-5">5.4.5.3.</span> Planta</h5>
<div class="outline-text-5" id="text-5-4-5-3">
<p>
Representação em escala grande (pequena área, muitos detalhes).
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Planta de cidade</li>
<li>Planta de bairro</li>
<li>Planta arquitetônica</li>
</ul>

<p>
<b>Resumo:</b>
</p>

<pre class="example" id="org376381b">
MAPA: escala pequena (1:1.000.000)
- país, continente
CARTA: escala média (1:100.000)
- região
PLANTA: escala grande (1:10.000)
- cidade, bairro
</pre>
</div>
</div>
</div>

<div id="outline-container-org0acb36b" class="outline-4">
<h4 id="org0acb36b"><span class="section-number-4">5.4.6.</span> Elementos de um Mapa</h4>
<div class="outline-text-4" id="text-5-4-6">
<p>
Todo mapa deve conter:
</p>

<ol class="org-ol">
<li><b>Título:</b> assunto representado</li>
<li><b>Legenda:</b> significado dos símbolos</li>
<li><b>Escala:</b> relação mapa/realidade</li>
<li><b>Orientação:</b> Rosa dos Ventos ou seta Norte</li>
<li><b>Fonte:</b> origem dos dados</li>
<li><b>Coordenadas:</b> latitude/longitude (opcional)</li>
</ol>
</div>
</div>

<div id="outline-container-org809e660" class="outline-4">
<h4 id="org809e660"><span class="section-number-4">5.4.7.</span> Tipos de Mapas Temáticos</h4>
<div class="outline-text-4" id="text-5-4-7">
</div>
<div id="outline-container-orgdd76c1d" class="outline-5">
<h5 id="orgdd76c1d"><span class="section-number-5">5.4.7.1.</span> Mapa Físico</h5>
<div class="outline-text-5" id="text-5-4-7-1">
<p>
Representa relevo, hidrografia, vegetação.
</p>

<p>
<b>Cores convencionais:</b>
</p>
<ul class="org-ul">
<li><b>Verde:</b> planícies, baixas altitudes</li>
<li><b>Amarelo/laranja:</b> planaltos</li>
<li><b>Marrom/vermelho:</b> montanhas</li>
<li><b>Azul:</b> água (oceanos, rios, lagos)</li>
<li><b>Branco:</b> neve, gelo</li>
</ul>
</div>
</div>

<div id="outline-container-org7eebcca" class="outline-5">
<h5 id="org7eebcca"><span class="section-number-5">5.4.7.2.</span> Mapa Político</h5>
<div class="outline-text-5" id="text-5-4-7-2">
<p>
Representa divisões administrativas (países, estados, municípios).
</p>

<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li>Fronteiras</li>
<li>Capitais</li>
<li>Cidades principais</li>
</ul>
</div>
</div>

<div id="outline-container-org319ba03" class="outline-5">
<h5 id="org319ba03"><span class="section-number-5">5.4.7.3.</span> Mapa Econômico</h5>
<div class="outline-text-5" id="text-5-4-7-3">
<p>
Representa atividades econômicas, recursos, produção.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Agricultura (cultivos)</li>
<li>Indústria (localização)</li>
<li>Recursos minerais</li>
</ul>
</div>
</div>

<div id="outline-container-org6140fdf" class="outline-5">
<h5 id="org6140fdf"><span class="section-number-5">5.4.7.4.</span> Mapa Demográfico</h5>
<div class="outline-text-5" id="text-5-4-7-4">
<p>
Representa população.
</p>

<p>
<b>Temas:</b>
</p>
<ul class="org-ul">
<li>Densidade demográfica</li>
<li>Distribuição populacional</li>
<li>Migrações</li>
</ul>
</div>
</div>

<div id="outline-container-org308e1f9" class="outline-5">
<h5 id="org308e1f9"><span class="section-number-5">5.4.7.5.</span> Mapa Climático</h5>
<div class="outline-text-5" id="text-5-4-7-5">
<p>
Representa climas, temperaturas, chuvas.
</p>
</div>
</div>
</div>

<div id="outline-container-org00ac3e4" class="outline-4">
<h4 id="org00ac3e4"><span class="section-number-4">5.4.8.</span> Curvas de Nível</h4>
<div class="outline-text-4" id="text-5-4-8">
<p>
<b>Definição:</b> linhas que unem pontos de mesma altitude.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Equidistância vertical constante (ex: 10 m, 50 m)</li>
<li><b>Curvas próximas:</b> relevo íngreme (montanha)</li>
<li><b>Curvas afastadas:</b> relevo suave (planície)</li>
<li>Nunca se cruzam</li>
</ul>

<p>
<b>Uso:</b> mapas topográficos, engenharia
</p>

<pre class="example" id="org6f6e64b">
Vista de cima:      Vista de perfil:
   ___                  /\\
  /   \\                /  \\
 /     \\              /    \\
|       |            /______\\
 \\     /            
  \\___/              

Curvas de nível    Montanha
</pre>
</div>
</div>

<div id="outline-container-org0fb2f7a" class="outline-4">
<h4 id="org0fb2f7a"><span class="section-number-4">5.4.9.</span> Sensoriamento Remoto e Tecnologias</h4>
<div class="outline-text-4" id="text-5-4-9">
<p>
<b>Sensoriamento Remoto:</b> obtenção de informações sobre a superfície terrestre sem contato direto.
</p>

<p>
<b>Tecnologias:</b>
</p>

<ol class="org-ol">
<li><b>Satélites:</b>
<ul class="org-ul">
<li>Imagens de alta resolução</li>
<li>Monitoramento ambiental</li>
<li>Clima e meteorologia</li>
</ul></li>
<li><b>GPS (Global Positioning System):</b>
<ul class="org-ul">
<li>Localização precisa por satélites</li>
<li>Navegação</li>
<li>Mapeamento</li>
</ul></li>
<li><b>SIG (Sistema de Informação Geográfica):</b>
<ul class="org-ul">
<li>Software para análise espacial</li>
<li>Cruzamento de dados geográficos</li>
<li>Planejamento urbano e ambiental</li>
</ul></li>
<li><b>Drones:</b>
<ul class="org-ul">
<li>Mapeamento de pequenas áreas</li>
<li>Alta precisão</li>
</ul></li>
</ol>
</div>
</div>

<div id="outline-container-org3c4ace2" class="outline-4">
<h4 id="org3c4ace2"><span class="section-number-4">5.4.10.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-4-10">
</div>
<div id="outline-container-org2b9d082" class="outline-5">
<h5 id="org2b9d082"><span class="section-number-5">5.4.10.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-4-10-1">
<p>
Qual projeção é mais adequada para navegação marítima? Por quê?
</p>

<p>
<b>Resposta:</b> <b>Projeção de Mercator</b>. Porque preserva ângulos e formas, permitindo traçar rotas de rumo constante (loxodrômicas). Apesar de distorcer áreas, mantém as direções corretas, essencial para navegação.
</p>
</div>
</div>

<div id="outline-container-org4305288" class="outline-5">
<h5 id="org4305288"><span class="section-number-5">5.4.10.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-4-10-2">
<p>
Compare as projeções de Mercator e Peters quanto à representação da África.
</p>

<p>
<b>Resposta:</b>
</p>
<ul class="org-ul">
<li><b>Mercator:</b> África aparece menor que a Groenlândia (distorção de área)</li>
<li><b>Peters:</b> África em tamanho real, muito maior que Groenlândia (preserva área)</li>
</ul>

<p>
A África tem 30 milhões km², Groenlândia 2 milhões km². Peters mostra proporção correta.
</p>
</div>
</div>

<div id="outline-container-orgeae7210" class="outline-5">
<h5 id="orgeae7210"><span class="section-number-5">5.4.10.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-4-10-3">
<p>
Em um mapa, curvas de nível estão muito próximas. O que isso indica?
</p>

<p>
<b>Resposta:</b> Relevo <b>íngreme</b> (montanhoso). Curvas próximas significam que a altitude varia muito em pequena distância horizontal, caracterizando terreno inclinado.
</p>
</div>
</div>

<div id="outline-container-orgd88c375" class="outline-5">
<h5 id="orgd88c375"><span class="section-number-5">5.4.10.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-4-10-4">
<p>
(UFMG) Qual tipo de representação tem maior escala: mapa, carta ou planta?
</p>

<p>
<b>Resposta:</b> <b>Planta</b> (escala grande, ex: 1:10.000).
</p>

<p>
Lembre-se: escala grande = denominador pequeno = área pequena = mais detalhes.
</p>
</div>
</div>
</div>

<div id="outline-container-orgc0f498c" class="outline-4">
<h4 id="orgc0f498c"><span class="section-number-4">5.4.11.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-4-11">
<ol class="org-ol">
<li><b>Projeção cilíndrica:</b> distorce polos (Mercator, Peters)</li>
<li><b>Mercator:</b> preserva formas, distorce áreas</li>
<li><b>Peters:</b> preserva áreas, distorce formas</li>
<li><b>Curvas próximas:</b> relevo íngreme</li>
<li><b>Escala grande:</b> planta (mais detalhes)</li>
<li><b>Escala pequena:</b> mapa (menos detalhes)</li>
<li><b>Mapa temático:</b> representa um tema específico</li>
<li><b>SIG, GPS, satélites:</b> tecnologias modernas</li>
</ol>
</div>
</div>

<div id="outline-container-orgf232061" class="outline-4">
<h4 id="orgf232061"><span class="section-number-4">5.4.12.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-4-12">
<p>
<b>Projeções:</b>
</p>
<ul class="org-ul">
<li><b>Mercator:</b> conforme (ângulos), navegação, distorce áreas</li>
<li><b>Peters:</b> equivalente (áreas), crítica ao eurocentrismo</li>
<li><b>Robinson:</b> compromisso, equilíbrio</li>
</ul>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li>Cilíndrica: distorce polos</li>
<li>Cônica: latitudes médias</li>
<li>Azimutal: centrada em ponto</li>
</ul>

<p>
<b>Representações:</b>
</p>
<ul class="org-ul">
<li>Mapa: escala pequena (país, continente)</li>
<li>Carta: escala média (região)</li>
<li>Planta: escala grande (cidade, bairro)</li>
</ul>

<p>
<b>Curvas de Nível:</b>
</p>
<ul class="org-ul">
<li>Próximas: íngreme</li>
<li>Afastadas: suave</li>
</ul>
</div>
</div>

<div id="outline-container-org23c391a" class="outline-4">
<h4 id="org23c391a"><span class="section-number-4">5.4.13.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-4-13">
<pre class="example" id="orgc78f325">
PROJEÇÕES:

Cilíndrica (Mercator):
 ║Terra║
 ║ ↓   ║
[────────] Polos distorcidos

Peters (Equivalente):
[────────] Áreas corretas
    ↕      Formas esticadas

Cônica:
   /\\
  /Te\\ 
 /__rra_\\ Latitudes médias

Azimutal:
   ┌─┐
 ┌─┴─┴─┐  Centro = polo
 └─────┘

CURVAS DE NÍVEL:

Íngreme:  Suave:
 ___        ___
 ___
 ___        ___
 ___
           ___
</pre>
</div>
</div>

<div id="outline-container-orgb0844e9" class="outline-4">
<h4 id="orgb0844e9"><span class="section-number-4">5.4.14.</span> Tabela Comparativa</h4>
<div class="outline-text-4" id="text-5-4-14">
<pre class="example" id="org89c070f">
┌──────────┬───────────┬──────────┬──────────┐
│ Projeção │   Tipo    │ Preserva │ Distorce │
├──────────┼───────────┼──────────┼──────────┤
│ Mercator │ Cilíndrica│ Ângulos  │  Áreas   │
│ Peters   │ Cilíndrica│  Áreas   │  Formas  │
│ Robinson │Pseudo-cil.│Equilíbrio│  Pouco   │
│ Azimutal │   Plana   │Distâncias│  Bordas  │
└──────────┴───────────┴──────────┴──────────┘

Escala:
┌────────┬──────────────┬──────────┬─────────┐
│  Tipo  │    Escala    │   Área   │Detalhes │
├────────┼──────────────┼──────────┼─────────┤
│  MAPA  │Pequena(1:1M) │  Grande  │  Poucos │
│ CARTA  │Média(1:100k) │  Média   │  Médios │
│ PLANTA │Grande(1:10k) │ Pequena  │  Muitos │
└────────┴──────────────┴──────────┴─────────┘
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>interpretação de mapas)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org5e4e55d" class="outline-3">`;

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
