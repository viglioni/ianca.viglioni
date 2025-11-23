<script setup lang="ts">
import { ref } from "vue";

const code = "ger-4-3";
const title = "Física: Grandezas Vetoriais, Escalares e Vetores";
const subject = "geral";
const themes: string[] = [];
const dates = ["2025-12-14"];
const lessonContent = `<div class="outline-text-3" id="text-1-3">
<ul class="org-ul">
<li>Física: Grandezas Vetoriais, Escalares e Vetores</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org4e8d93e" class="outline-4">
<h4 id="org4e8d93e"><span class="section-number-4">1.3.1.</span> O que são Grandezas Físicas?</h4>
<div class="outline-text-4" id="text-1-3-1">
<p>
<b>Grandezas físicas</b> são propriedades que podem ser medidas e quantificadas. Elas são classificadas em dois tipos principais: escalares e vetoriais.
</p>
</div>
</div>

<div id="outline-container-org6e279ca" class="outline-4">
<h4 id="org6e279ca"><span class="section-number-4">1.3.2.</span> Grandezas Escalares</h4>
<div class="outline-text-4" id="text-1-3-2">
<p>
<b>Definição:</b> Grandezas que ficam completamente determinadas por um <b>valor numérico</b> (módulo) e uma <b>unidade de medida</b>.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Precisam apenas de um número e uma unidade</li>
<li>Não possuem direção ou sentido</li>
<li>Podem ser somadas algebricamente (soma comum)</li>
</ul>

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
<th scope="col" class="org-left">Grandeza</th>
<th scope="col" class="org-left">Exemplo</th>
<th scope="col" class="org-left">Unidade (SI)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Tempo</td>
<td class="org-left">5 segundos</td>
<td class="org-left">s</td>
</tr>

<tr>
<td class="org-left">Massa</td>
<td class="org-left">10 quilogramas</td>
<td class="org-left">kg</td>
</tr>

<tr>
<td class="org-left">Temperatura</td>
<td class="org-left">25 graus Celsius</td>
<td class="org-left">°C</td>
</tr>

<tr>
<td class="org-left">Energia</td>
<td class="org-left">100 joules</td>
<td class="org-left">J</td>
</tr>

<tr>
<td class="org-left">Volume</td>
<td class="org-left">2 litros</td>
<td class="org-left">L ou m³</td>
</tr>

<tr>
<td class="org-left">Densidade</td>
<td class="org-left">1000 kg/m³</td>
<td class="org-left">kg/m³</td>
</tr>

<tr>
<td class="org-left">Pressão</td>
<td class="org-left">101325 Pa</td>
<td class="org-left">Pa</td>
</tr>

<tr>
<td class="org-left">Trabalho</td>
<td class="org-left">50 J</td>
<td class="org-left">J</td>
</tr>

<tr>
<td class="org-left">Potência</td>
<td class="org-left">100 W</td>
<td class="org-left">W</td>
</tr>

<tr>
<td class="org-left">Carga elétrica</td>
<td class="org-left">5 C</td>
<td class="org-left">C</td>
</tr>
</tbody>
</table>

<p>
<b>Operações com escalares:</b>
</p>
<ul class="org-ul">
<li>Soma: 5 kg + 3 kg = 8 kg</li>
<li>Subtração: 10 m</li>
<li>4 m = 6 m</li>
<li>Multiplicação: 2 × 5 s = 10 s</li>
</ul>
</div>
</div>

<div id="outline-container-orgb30a60f" class="outline-4">
<h4 id="orgb30a60f"><span class="section-number-4">1.3.3.</span> Grandezas Vetoriais</h4>
<div class="outline-text-4" id="text-1-3-3">
<p>
<b>Definição:</b> Grandezas que necessitam de <b>módulo</b> (intensidade), <b>direção</b> e <b>sentido</b> para serem completamente determinadas.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Precisam de valor numérico, direção e sentido</li>
<li>São representadas por vetores (setas)</li>
<li>Não podem ser somadas algebricamente (usam regras vetoriais)</li>
</ul>

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
<th scope="col" class="org-left">Grandeza</th>
<th scope="col" class="org-left">Exemplo</th>
<th scope="col" class="org-left">Unidade (SI)</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Deslocamento</td>
<td class="org-left">10 m para leste</td>
<td class="org-left">m</td>
</tr>

<tr>
<td class="org-left">Velocidade</td>
<td class="org-left">20 m/s para norte</td>
<td class="org-left">m/s</td>
</tr>

<tr>
<td class="org-left">Aceleração</td>
<td class="org-left">5 m/s² para cima</td>
<td class="org-left">m/s²</td>
</tr>

<tr>
<td class="org-left">Força</td>
<td class="org-left">50 N para baixo</td>
<td class="org-left">N</td>
</tr>

<tr>
<td class="org-left">Quantidade de movimento</td>
<td class="org-left">100 kg·m/s horizontal</td>
<td class="org-left">kg·m/s</td>
</tr>

<tr>
<td class="org-left">Impulso</td>
<td class="org-left">10 N·s vertical</td>
<td class="org-left">N·s</td>
</tr>

<tr>
<td class="org-left">Campo elétrico</td>
<td class="org-left">500 N/C para direita</td>
<td class="org-left">N/C</td>
</tr>

<tr>
<td class="org-left">Campo magnético</td>
<td class="org-left">0,5 T perpendicular</td>
<td class="org-left">T</td>
</tr>
</tbody>
</table>

<p>
<b>Exemplo prático:</b>
</p>
<ul class="org-ul">
<li><b>Escalar:</b> “Andei 5 km” (distância)</li>
<li><b>Vetorial:</b> “Andei 5 km para o norte” (deslocamento)</li>
</ul>
</div>
</div>

<div id="outline-container-org0168b2b" class="outline-4">
<h4 id="org0168b2b"><span class="section-number-4">1.3.4.</span> Elementos de um Vetor</h4>
<div class="outline-text-4" id="text-1-3-4">
<p>
Um vetor é representado graficamente por uma <b>seta</b> e possui três características fundamentais:
</p>
</div>

<div id="outline-container-org14e0aec" class="outline-5">
<h5 id="org14e0aec"><span class="section-number-5">1.3.4.1.</span> 1. Módulo (ou Intensidade)</h5>
<div class="outline-text-5" id="text-1-3-4-1">
<ul class="org-ul">
<li>É o “tamanho” do vetor</li>
<li>Representa o valor numérico da grandeza</li>
<li>Corresponde ao comprimento da seta</li>
<li>Notação: |v⃗| ou v</li>
</ul>
</div>
</div>

<div id="outline-container-orge0013b4" class="outline-5">
<h5 id="orge0013b4"><span class="section-number-5">1.3.4.2.</span> 2. Direção</h5>
<div class="outline-text-5" id="text-1-3-4-2">
<ul class="org-ul">
<li>É a reta sobre a qual o vetor está orientado</li>
<li>Exemplos: horizontal, vertical, diagonal, inclinada 30° com a horizontal</li>
</ul>
</div>
</div>

<div id="outline-container-org629cb54" class="outline-5">
<h5 id="org629cb54"><span class="section-number-5">1.3.4.3.</span> 3. Sentido</h5>
<div class="outline-text-5" id="text-1-3-4-3">
<ul class="org-ul">
<li>É a orientação do vetor ao longo da direção</li>
<li>Indicado pela ponta da seta</li>
<li>Exemplos: para cima/baixo, esquerda/direita, norte/sul/leste/oeste</li>
</ul>

<p>
<b>Representação gráfica:</b>
</p>

<pre class="example" id="orgf108d63">
      ↑
      |  Módulo (tamanho da seta)
      |
      •  Origem (ponto de aplicação)
     
Direção: vertical
Sentido: para cima
</pre>
</div>
</div>
</div>

<div id="outline-container-org4b57917" class="outline-4">
<h4 id="org4b57917"><span class="section-number-4">1.3.5.</span> Notação de Vetores</h4>
<div class="outline-text-4" id="text-1-3-5">
<p>
<b>Forma algébrica:</b>
</p>
<ul class="org-ul">
<li>v⃗ (vetor v com seta em cima)</li>
<li><b>v</b> (vetor v em negrito)</li>
<li>|v⃗| = módulo do vetor v</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>F⃗ = força (vetor)</li>
<li>|F⃗| = 10 N (módulo da força)</li>
</ul>
</div>
</div>

<div id="outline-container-orga298d0f" class="outline-4">
<h4 id="orga298d0f"><span class="section-number-4">1.3.6.</span> Sistemas de Coordenadas</h4>
<div class="outline-text-4" id="text-1-3-6">
</div>
<div id="outline-container-org4e5f83a" class="outline-5">
<h5 id="org4e5f83a"><span class="section-number-5">1.3.6.1.</span> Sistema Cartesiano (2D)</h5>
<div class="outline-text-5" id="text-1-3-6-1">
<ul class="org-ul">
<li>Eixo x (horizontal): direita (+), esquerda (-)</li>
<li>Eixo y (vertical): cima (+), baixo (-)</li>
</ul>
</div>
</div>

<div id="outline-container-org231e919" class="outline-5">
<h5 id="org231e919"><span class="section-number-5">1.3.6.2.</span> Pontos Cardeais</h5>
<div class="outline-text-5" id="text-1-3-6-2">
<ul class="org-ul">
<li>Norte (N): +y</li>
<li>Sul (S): -y</li>
<li>Leste (L ou E): +x</li>
<li>Oeste (O ou W): -x</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orge101b89" class="outline-4">
<h4 id="orge101b89"><span class="section-number-4">1.3.7.</span> Componentes de um Vetor</h4>
<div class="outline-text-4" id="text-1-3-7">
<p>
Todo vetor pode ser decomposto em <b>componentes</b> ao longo dos eixos coordenados.
</p>

<p>
<b>Para um vetor v⃗ no plano xy:</b>
</p>

<ul class="org-ul">
<li><b>Componente x:</b> vₓ = |v⃗| · cos θ</li>
<li><b>Componente y:</b> vᵧ = |v⃗| · sen θ</li>
</ul>

<p>
Onde θ é o ângulo que o vetor faz com o eixo x.
</p>

<p>
<b>Módulo a partir das componentes:</b> |v⃗| = √(vₓ² + vᵧ²)
</p>

<p>
<b>Ângulo a partir das componentes:</b> tan θ = vᵧ / vₓ
</p>

<p>
<b>Exemplo:</b> Um vetor de módulo 10 m faz 30° com a horizontal.
</p>

<ul class="org-ul">
<li>vₓ = 10 · cos 30° = 10 · 0,866 = 8,66 m</li>
<li>vᵧ = 10 · sen 30° = 10 · 0,5 = 5 m</li>
</ul>

<p>
<b>Verificação:</b> |v⃗| = √(8,66² + 5²) = √(75 + 25) = √100 = 10 m ✓
</p>
</div>
</div>

<div id="outline-container-org5f636a2" class="outline-4">
<h4 id="org5f636a2"><span class="section-number-4">1.3.8.</span> Operações com Vetores</h4>
<div class="outline-text-4" id="text-1-3-8">
</div>
<div id="outline-container-orga2480db" class="outline-5">
<h5 id="orga2480db"><span class="section-number-5">1.3.8.1.</span> 1. Adição de Vetores</h5>
<div class="outline-text-5" id="text-1-3-8-1">
<p>
<b>Regra do Paralelogramo:</b>
</p>
<ul class="org-ul">
<li>Coloca-se os vetores com a mesma origem</li>
<li>Completa-se um paralelogramo</li>
<li>A diagonal representa a soma (resultante)</li>
</ul>

<p>
<b>Regra do Polígono (método ponta-cabeça):</b>
</p>
<ul class="org-ul">
<li>Coloca-se a origem do segundo vetor na extremidade do primeiro</li>
<li>O vetor resultante vai da origem do primeiro à extremidade do último</li>
<li>Mais prático para vários vetores</li>
</ul>

<p>
<b>Método das componentes:</b> 1. Decompor cada vetor em componentes x e y 2. Somar as componentes x: Rₓ = v₁ₓ + v₂ₓ 3. Somar as componentes y: Rᵧ = v₁ᵧ + v₂ᵧ 4. Calcular o módulo: |R⃗| = √(Rₓ² + Rᵧ²)
</p>

<p>
<b>Exemplo:</b> v₁⃗ = (3, 4) e v₂⃗ = (1, 2)
</p>

<p>
R⃗ = v₁⃗ + v₂⃗ = (3+1, 4+2) = (4, 6)
</p>

<p>
​|R⃗| = √(4² + 6²) = √(16 + 36) = √52 ≈ 7,2
</p>
</div>
</div>

<div id="outline-container-orga808aea" class="outline-5">
<h5 id="orga808aea"><span class="section-number-5">1.3.8.2.</span> 2. Subtração de Vetores</h5>
<div class="outline-text-5" id="text-1-3-8-2">
<p>
*v₁⃗
</p>
<ul class="org-ul">
<li>v₂⃗ = v₁⃗ + (-v₂⃗)*</li>
</ul>

<p>
O vetor -v₂⃗ tem mesmo módulo e direção que v₂⃗, mas sentido oposto.
</p>

<p>
<b>Método das componentes:</b>
</p>
<ul class="org-ul">
<li>Rₓ = v₁ₓ</li>
<li>v₂ₓ</li>
<li>Rᵧ = v₁ᵧ</li>
<li>v₂ᵧ</li>
</ul>

<p>
<b>Exemplo:</b> v₁⃗ = (5, 3) e v₂⃗ = (2, 1)
</p>

<p>
R⃗ = v₁⃗
</p>
<ul class="org-ul">
<li>v₂⃗ = (5-2, 3-1) = (3, 2)</li>
</ul>
</div>
</div>

<div id="outline-container-org8acc742" class="outline-5">
<h5 id="org8acc742"><span class="section-number-5">1.3.8.3.</span> 3. Multiplicação por Escalar</h5>
<div class="outline-text-5" id="text-1-3-8-3">
<p>
Multiplicar um vetor por um número k:
</p>

<ul class="org-ul">
<li>Se k &gt; 0: mesma direção e sentido, módulo multiplicado por k</li>
<li>Se k &lt; 0: mesma direção, sentido oposto, módulo multiplicado por |k|</li>
<li>Se k = 0: vetor nulo</li>
</ul>

<p>
<b>Exemplo:</b> v⃗ = (2, 3)
</p>

<p>
2v⃗ = (4, 6) → módulo dobrado, mesma direção e sentido -v⃗ = (-2, -3) → mesmo módulo, sentido oposto
</p>
</div>
</div>
</div>

<div id="outline-container-org4996850" class="outline-4">
<h4 id="org4996850"><span class="section-number-4">1.3.9.</span> Casos Especiais de Adição Vetorial</h4>
<div class="outline-text-4" id="text-1-3-9">
</div>
<div id="outline-container-orgee0be11" class="outline-5">
<h5 id="orgee0be11"><span class="section-number-5">1.3.9.1.</span> Vetores na Mesma Direção e Mesmo Sentido</h5>
<div class="outline-text-5" id="text-1-3-9-1">
<p>
​|R⃗| = |v₁⃗| + |v₂⃗|
</p>

<p>
<b>Exemplo:</b> 5 N + 3 N = 8 N (na mesma direção)
</p>
</div>
</div>

<div id="outline-container-org6a324f2" class="outline-5">
<h5 id="org6a324f2"><span class="section-number-5">1.3.9.2.</span> Vetores na Mesma Direção e Sentidos Opostos</h5>
<div class="outline-text-5" id="text-1-3-9-2">
<p>
​|R⃗| = ||v₁⃗|
</p>
<ul class="org-ul">
<li>|v₂⃗||</li>
</ul>

<p>
<b>Exemplo:</b> 5 N
</p>
<ul class="org-ul">
<li>3 N = 2 N (direção do maior)</li>
</ul>
</div>
</div>

<div id="outline-container-orge71fbc3" class="outline-5">
<h5 id="orge71fbc3"><span class="section-number-5">1.3.9.3.</span> Vetores Perpendiculares (90°)</h5>
<div class="outline-text-5" id="text-1-3-9-3">
<p>
​|R⃗| = √(|v₁⃗|² + |v₂⃗|²) (Teorema de Pitágoras)
</p>

<p>
<b>Exemplo:</b> v₁⃗ = 3 m (horizontal) v₂⃗ = 4 m (vertical) |R⃗| = √(3² + 4²) = √(9 + 16) = √25 = 5 m
</p>

<p>
<b>Ângulo:</b> tan θ = 4/3 → θ = arctan(4/3) ≈ 53,1°
</p>
</div>
</div>

<div id="outline-container-org1c6e24f" class="outline-5">
<h5 id="org1c6e24f"><span class="section-number-5">1.3.9.4.</span> Vetores com Ângulo θ entre Eles</h5>
<div class="outline-text-5" id="text-1-3-9-4">
<p>
​|R⃗| = √(|v₁⃗|² + |v₂⃗|² + 2|v₁⃗||v₂⃗|cos θ)
</p>

<p>
<b>Lei dos Cossenos</b>
</p>
</div>
</div>
</div>

<div id="outline-container-org1cea05f" class="outline-4">
<h4 id="org1cea05f"><span class="section-number-4">1.3.10.</span> Unidades de Medida no SI</h4>
<div class="outline-text-4" id="text-1-3-10">
<p>
<b>Sistema Internacional de Unidades (SI):</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Grandeza</th>
<th scope="col" class="org-left">Unidade</th>
<th scope="col" class="org-left">Símbolo</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Comprimento</td>
<td class="org-left">metro</td>
<td class="org-left">m</td>
</tr>

<tr>
<td class="org-left">Massa</td>
<td class="org-left">quilograma</td>
<td class="org-left">kg</td>
</tr>

<tr>
<td class="org-left">Tempo</td>
<td class="org-left">segundo</td>
<td class="org-left">s</td>
</tr>

<tr>
<td class="org-left">Velocidade</td>
<td class="org-left">metro por segundo</td>
<td class="org-left">m/s</td>
</tr>

<tr>
<td class="org-left">Aceleração</td>
<td class="org-left">metro por segundo ao quadrado</td>
<td class="org-left">m/s²</td>
</tr>

<tr>
<td class="org-left">Força</td>
<td class="org-left">newton</td>
<td class="org-left">N (kg·m/s²)</td>
</tr>

<tr>
<td class="org-left">Energia</td>
<td class="org-left">joule</td>
<td class="org-left">J (N·m)</td>
</tr>

<tr>
<td class="org-left">Potência</td>
<td class="org-left">watt</td>
<td class="org-left">W (J/s)</td>
</tr>
</tbody>
</table>

<p>
<b>Conversões comuns:</b>
</p>
<ul class="org-ul">
<li>1 km = 1000 m</li>
<li>1 h = 3600 s</li>
<li>1 km/h = 1/3,6 m/s ≈ 0,278 m/s</li>
<li>1 m/s = 3,6 km/h</li>
</ul>
</div>
</div>

<div id="outline-container-org9806c92" class="outline-4">
<h4 id="org9806c92"><span class="section-number-4">1.3.11.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-1-3-11">
</div>
<div id="outline-container-org61f78c7" class="outline-5">
<h5 id="org61f78c7"><span class="section-number-5">1.3.11.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-1-3-11-1">
<p>
Classifique as grandezas em escalares ou vetoriais: a) Temperatura b) Velocidade c) Massa d) Força e) Energia
</p>

<p>
<b>Resposta:</b> a) Escalar b) Vetorial c) Escalar d) Vetorial e) Escalar
</p>
</div>
</div>

<div id="outline-container-org6b910e0" class="outline-5">
<h5 id="org6b910e0"><span class="section-number-5">1.3.11.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-1-3-11-2">
<p>
Um vetor tem módulo 20 m e faz ângulo de 60° com a horizontal. Determine suas componentes.
</p>

<p>
<b>Solução:</b>
</p>
<ul class="org-ul">
<li>vₓ = 20 · cos 60° = 20 · 0,5 = 10 m</li>
<li>vᵧ = 20 · sen 60° = 20 · 0,866 = 17,32 m</li>
</ul>

<p>
<i>[Ver resposta 13 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org5b6abb2" class="outline-5">
<h5 id="org5b6abb2"><span class="section-number-5">1.3.11.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-1-3-11-3">
<p>
Dois vetores perpendiculares têm módulos 6 m e 8 m. Determine o módulo da resultante.
</p>

<p>
<b>Solução:</b> Como são perpendiculares, usamos Pitágoras: |R⃗| = √(6² + 8²) = √(36 + 64) = √100 = 10 m
</p>

<p>
<i>[Ver resposta 14 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orga50cb7d" class="outline-5">
<h5 id="orga50cb7d"><span class="section-number-5">1.3.11.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-1-3-11-4">
<p>
Um carro percorre 30 km para o norte e depois 40 km para o leste. Qual o módulo do deslocamento resultante?
</p>

<p>
<b>Solução:</b> Vetores perpendiculares: |R⃗| = √(30² + 40²) = √(900 + 1600) = √2500 = 50 km
</p>

<p>
<b>Ângulo com o norte:</b> tan θ = 40/30 = 4/3 θ = arctan(4/3) ≈ 53,1° para o leste
</p>

<p>
<i>[Ver resposta 15 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org714bf1b" class="outline-5">
<h5 id="org714bf1b"><span class="section-number-5">1.3.11.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-1-3-11-5">
<p>
Dados v₁⃗ = (4, 3) e v₂⃗ = (1, -2), calcule: a) v₁⃗ + v₂⃗ b) v₁⃗
</p>
<ul class="org-ul">
<li>v₂⃗ c) |v₁⃗|</li>
</ul>

<p>
<b>Solução:</b> a) v₁⃗ + v₂⃗ = (4+1, 3-2) = (5, 1)
</p>

<ol class="org-ol">
<li value="2">v₁⃗</li>
<li>v₂⃗ = (4-1, 3-(-2)) = (3, 5)</li>

<li>|v₁⃗| = √(4² + 3²) = √(16 + 9) = √25 = 5</li>
</ol>
</div>
</div>

<div id="outline-container-orga09208e" class="outline-5">
<h5 id="orga09208e"><span class="section-number-5">1.3.11.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-1-3-11-6">
<p>
Converta 72 km/h para m/s.
</p>

<p>
<b>Solução:</b> 72 km/h = 72 ÷ 3,6 = 20 m/s
</p>

<p>
Ou: 72 km/h = 72.000 m / 3600 s = 20 m/s
</p>

<p>
<i>[Ver resposta 16 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org2981db8" class="outline-4">
<h4 id="org2981db8"><span class="section-number-4">1.3.12.</span> Valores Notáveis de Seno e Cosseno</h4>
<div class="outline-text-4" id="text-1-3-12">
<p>
Memorize para facilitar os cálculos:
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Ângulo</th>
<th scope="col" class="org-left">sen θ</th>
<th scope="col" class="org-left">cos θ</th>
<th scope="col" class="org-left">tan θ</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">0°</td>
<td class="org-left">0</td>
<td class="org-left">1</td>
<td class="org-left">0</td>
</tr>

<tr>
<td class="org-left">30°</td>
<td class="org-left">1/2 = 0,5</td>
<td class="org-left">√3/2 ≈ 0,866</td>
<td class="org-left">√3/3 ≈ 0,577</td>
</tr>

<tr>
<td class="org-left">45°</td>
<td class="org-left">√2/2 ≈ 0,707</td>
<td class="org-left">√2/2 ≈ 0,707</td>
<td class="org-left">1</td>
</tr>

<tr>
<td class="org-left">60°</td>
<td class="org-left">√3/2 ≈ 0,866</td>
<td class="org-left">1/2 = 0,5</td>
<td class="org-left">√3 ≈ 1,732</td>
</tr>

<tr>
<td class="org-left">90°</td>
<td class="org-left">1</td>
<td class="org-left">0</td>
<td class="org-left">∞</td>
</tr>
</tbody>
</table>
</div>
</div>

<div id="outline-container-orgaa7af3b" class="outline-4">
<h4 id="orgaa7af3b"><span class="section-number-4">1.3.13.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-1-3-13">
<ol class="org-ol">
<li><b>Identificação:</b> Pergunte-se “precisa de direção?”. Se sim, é vetorial</li>
<li><b>Decomposição:</b> Use sempre sen e cos corretamente (cos para x, sen para y)</li>
<li><b>Perpendiculares:</b> Lembre-se de Pitágoras</li>
<li><b>Conversões:</b> km/h → m/s: divida por 3,6; m/s → km/h: multiplique por 3,6</li>
<li><b>Desenhe:</b> Sempre que possível, faça um esboço dos vetores</li>
<li><b>Ângulos notáveis:</b> Memorize sen 30°, cos 30°, sen 60°, cos 60°, sen 45°, cos 45°</li>
</ol>
</div>
</div>

<div id="outline-container-orge6b9bc8" class="outline-4">
<h4 id="orge6b9bc8"><span class="section-number-4">1.3.14.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-1-3-14">
<p>
<b>Escalares vs Vetoriais:</b>
</p>
<ul class="org-ul">
<li><b>Escalar:</b> só precisa de número + unidade (massa, tempo, temperatura)</li>
<li><b>Vetorial:</b> precisa de módulo, direção e sentido (força, velocidade, deslocamento)</li>
</ul>

<p>
<b>Componentes:</b>
</p>
<ul class="org-ul">
<li>vₓ = |v⃗| · cos θ</li>
<li>vᵧ = |v⃗| · sen θ</li>
<li>|v⃗| = √(vₓ² + vᵧ²)</li>
</ul>

<p>
<b>Casos especiais:</b>
</p>
<ul class="org-ul">
<li>Mesmo sentido: soma simples</li>
<li>Sentidos opostos: subtração (sinal do maior)</li>
<li>Perpendiculares: Pitágoras</li>
</ul>
</div>
</div>

<div id="outline-container-orga3697fa" class="outline-4">
<h4 id="orga3697fa"><span class="section-number-4">1.3.15.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-1-3-15">
<pre class="example" id="org1e5a0c5">
Componentes de um vetor:
vₓ = |v⃗| · cos θ
vᵧ = |v⃗| · sen θ

Módulo a partir das componentes:
|v⃗| = √(vₓ² + vᵧ²)

Ângulo:
tan θ = vᵧ / vₓ

Adição vetorial (componentes):
R⃗ = v₁⃗ + v₂⃗
Rₓ = v₁ₓ + v₂ₓ
Rᵧ = v₁ᵧ + v₂ᵧ

Vetores perpendiculares:
|R⃗| = √(|v₁⃗|² + |v₂⃗|²)

Lei dos Cossenos (ângulo θ entre vetores):
|R⃗| = √(|v₁⃗|² + |v₂⃗|² + 2|v₁⃗||v₂⃗|cos θ)

Conversões:
1 km/h = 1/3,6 m/s
1 m/s = 3,6 km/h
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>base para toda a cinemática e dinâmica)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org49fbc24" class="outline-3">`;

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
