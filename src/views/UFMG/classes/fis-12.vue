<script setup lang="ts">
import { ref } from "vue";

const code = "fis-12";
const title = "Física: Cinemática";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-2">
<ul class="org-ul">
<li>Física: Cinemática</li>
<li>MRUV e Queda Livre</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org784dc1b" class="outline-4">
<h4 id="org784dc1b"><span class="section-number-4">3.2.1.</span> Recordando: MRU vs MRUV</h4>
<div class="outline-text-4" id="text-3-2-1">
<p>
<b>MRU (Movimento Retilíneo Uniforme):</b>
</p>
<ul class="org-ul">
<li>Velocidade <b>constante</b></li>
<li>Aceleração = 0</li>
<li>Equação: s = s₀ + vt</li>
</ul>

<p>
<b>MRUV (Movimento Retilíneo Uniformemente Variado):</b>
</p>
<ul class="org-ul">
<li>Velocidade <b>variável</b></li>
<li>Aceleração <b>constante</b> (≠ 0)</li>
<li>Movimento em linha reta com aceleração uniforme</li>
</ul>
</div>
</div>

<div id="outline-container-orgbc49779" class="outline-4">
<h4 id="orgbc49779"><span class="section-number-4">3.2.2.</span> O que é Aceleração?</h4>
<div class="outline-text-4" id="text-3-2-2">
<p>
<b>Aceleração</b> é a taxa de variação da velocidade em relação ao tempo.
</p>

<p>
<b>Definição:</b>
</p>

<pre class="example" id="orgc4cb1c1">
a = Δv / Δt = (v
- v₀) / t
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>a = aceleração</li>
<li>v = velocidade final</li>
<li>v₀ = velocidade inicial</li>
<li>Δv = variação da velocidade</li>
<li>t = intervalo de tempo</li>
</ul>

<p>
<b>Unidade no SI:</b> m/s² (metros por segundo ao quadrado)
</p>

<p>
<b>Interpretação:</b>
</p>
<ul class="org-ul">
<li>a = 2 m/s² significa que a velocidade aumenta 2 m/s a cada segundo</li>
<li>a = -3 m/s² significa que a velocidade diminui 3 m/s a cada segundo (desaceleração)</li>
</ul>

<p>
<b>Exemplo:</b> Um carro parte do repouso e atinge 20 m/s em 5 segundos. Qual sua aceleração?
</p>

<p>
a = (v
</p>
<ul class="org-ul">
<li>v₀) / t = (20</li>
<li>0) / 5 = 4 m/s²</li>
</ul>
</div>
</div>

<div id="outline-container-org887bf8f" class="outline-4">
<h4 id="org887bf8f"><span class="section-number-4">3.2.3.</span> Tipos de Movimento Acelerado</h4>
<div class="outline-text-4" id="text-3-2-3">
</div>
<div id="outline-container-org33bc596" class="outline-5">
<h5 id="org33bc596"><span class="section-number-5">3.2.3.1.</span> Aceleração Positiva (a &gt; 0)</h5>
<div class="outline-text-5" id="text-3-2-3-1">
<ul class="org-ul">
<li>Movimento <b>acelerado</b></li>
<li>Velocidade aumenta</li>
<li>v e a têm o mesmo sinal</li>
</ul>

<p>
<b>Exemplo:</b> Carro acelerando para frente
</p>
</div>
</div>

<div id="outline-container-org19d12e5" class="outline-5">
<h5 id="org19d12e5"><span class="section-number-5">3.2.3.2.</span> Aceleração Negativa (a &lt; 0)</h5>
<div class="outline-text-5" id="text-3-2-3-2">
<ul class="org-ul">
<li>Movimento <b>retardado</b> ou <b>desacelerado</b></li>
<li>Velocidade diminui em módulo</li>
<li>v e a têm sinais opostos</li>
</ul>

<p>
<b>Exemplo:</b> Carro freando
</p>

<p>
<b>Observação importante:</b>
</p>
<ul class="org-ul">
<li>Aceleração negativa ≠ sempre desaceleração</li>
<li>O que importa é a relação entre os sinais de v e a:</li>
<li><b>Mesmos sinais:</b> acelerado</li>
<li><b>Sinais opostos:</b> retardado</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org0254805" class="outline-4">
<h4 id="org0254805"><span class="section-number-4">3.2.4.</span> Equações do MRUV</h4>
<div class="outline-text-4" id="text-3-2-4">
<p>
No MRUV, temos 4 equações principais (chamadas de “equações horárias”):
</p>
</div>
</div>

<div id="outline-container-orgb3b4668" class="outline-4">
<h4 id="orgb3b4668"><span class="section-number-4">3.2.5.</span> 1. Função Horária da Velocidade</h4>
<div class="outline-text-4" id="text-3-2-5">
<p>
<b>v = v₀ + at</b>
</p>

<p>
Onde:
</p>
<ul class="org-ul">
<li>v = velocidade no instante t</li>
<li>v₀ = velocidade inicial</li>
<li>a = aceleração</li>
<li>t = tempo</li>
</ul>

<p>
<b>Uso:</b> Encontrar a velocidade em qualquer instante.
</p>

<p>
<b>Exemplo:</b> Um móvel parte com v₀ = 10 m/s e acelera a 2 m/s². Qual a velocidade em t = 5s?
</p>

<p>
v = 10 + 2(5) = 10 + 10 = 20 m/s
</p>
</div>
</div>

<div id="outline-container-org8a3237e" class="outline-4">
<h4 id="org8a3237e"><span class="section-number-4">3.2.6.</span> 2. Função Horária da Posição (Equação de Torricelli com tempo)</h4>
<div class="outline-text-4" id="text-3-2-6">
<p>
<b>s = s₀ + v₀t + (1/2)at²</b>
</p>

<p>
Onde:
</p>
<ul class="org-ul">
<li>s = posição no instante t</li>
<li>s₀ = posição inicial</li>
<li>v₀ = velocidade inicial</li>
<li>a = aceleração</li>
<li>t = tempo</li>
</ul>

<p>
<b>Uso:</b> Encontrar a posição em qualquer instante.
</p>

<p>
<b>Exemplo:</b> Um móvel parte de s₀ = 0 com v₀ = 5 m/s e a = 2 m/s². Qual a posição em t = 4s?
</p>

<p>
s = 0 + 5(4) + (1/2)(2)(4²) s = 0 + 20 + (1)(16) s = 36 m
</p>
</div>
</div>

<div id="outline-container-org9b054e6" class="outline-4">
<h4 id="org9b054e6"><span class="section-number-4">3.2.7.</span> 3. Equação de Torricelli (sem tempo)</h4>
<div class="outline-text-4" id="text-3-2-7">
<p>
<b>v² = v₀² + 2aΔs</b>
</p>

<p>
Onde:
</p>
<ul class="org-ul">
<li>v = velocidade final</li>
<li>v₀ = velocidade inicial</li>
<li>a = aceleração</li>
<li>Δs = deslocamento (s</li>
<li>s₀)</li>
</ul>

<p>
<b>Uso:</b> Relacionar velocidade e deslocamento <b>sem usar o tempo</b>.
</p>

<p>
<b>Exemplo:</b> Um carro a 10 m/s acelera a 2 m/s² por 50 m. Qual a velocidade final?
</p>

<p>
v² = 10² + 2(2)(50) v² = 100 + 200 v² = 300 v = √300 ≈ 17,3 m/s
</p>
</div>
</div>

<div id="outline-container-org3c01bdf" class="outline-4">
<h4 id="org3c01bdf"><span class="section-number-4">3.2.8.</span> 4. Velocidade Média</h4>
<div class="outline-text-4" id="text-3-2-8">
<p>
<b>v_m = (v₀ + v) / 2</b>
</p>

<p>
<b>Válida apenas para MRUV</b> (movimento uniformemente variado)
</p>

<p>
<b>Exemplo:</b> Um móvel parte com 10 m/s e chega a 30 m/s. Qual a velocidade média?
</p>

<p>
v_m = (10 + 30) / 2 = 20 m/s
</p>
</div>
</div>

<div id="outline-container-org4374222" class="outline-4">
<h4 id="org4374222"><span class="section-number-4">3.2.9.</span> Resumo das Equações do MRUV</h4>
<div class="outline-text-4" id="text-3-2-9">
<pre class="example" id="org7d875eb">
1. v = v₀ + at

2. s = s₀ + v₀t + (1/2)at²

3. v² = v₀² + 2aΔs

4. v_m = (v₀ + v) / 2
</pre>
</div>
</div>

<div id="outline-container-orgd0f0043" class="outline-4">
<h4 id="orgd0f0043"><span class="section-number-4">3.2.10.</span> Como Escolher a Equação Certa?</h4>
<div class="outline-text-4" id="text-3-2-10">
<p>
<b>Analise o que você tem e o que quer descobrir:</b>
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Tem</th>
<th scope="col" class="org-left">Quer</th>
<th scope="col" class="org-left">Use</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">v₀, a, t</td>
<td class="org-left">v</td>
<td class="org-left">v = v₀ + at</td>
</tr>

<tr>
<td class="org-left">v₀, a, t</td>
<td class="org-left">s</td>
<td class="org-left">s = s₀ + v₀t + (1/2)at²</td>
</tr>

<tr>
<td class="org-left">v₀, a, Δs</td>
<td class="org-left">v</td>
<td class="org-left">v² = v₀² + 2aΔs</td>
</tr>

<tr>
<td class="org-left">v₀, v</td>
<td class="org-left">v_m</td>
<td class="org-left">v_m = (v₀ + v) / 2</td>
</tr>

<tr>
<td class="org-left">v₀, v, a</td>
<td class="org-left">t</td>
<td class="org-left">v = v₀ + at</td>
</tr>

<tr>
<td class="org-left">v₀, v, a</td>
<td class="org-left">Δs</td>
<td class="org-left">v² = v₀² + 2aΔs</td>
</tr>
</tbody>
</table>

<p>
<b>Dica:</b> Se o problema <b>não menciona tempo</b>, use Torricelli (v² = v₀² + 2aΔs)!
</p>
</div>
</div>

<div id="outline-container-orgcedc0ef" class="outline-4">
<h4 id="orgcedc0ef"><span class="section-number-4">3.2.11.</span> Gráficos do MRUV</h4>
<div class="outline-text-4" id="text-3-2-11">
<pre class="example" id="org128030c">
GRÁFICOS DO MOVIMENTO RETILÍNEO UNIFORMEMENTE VARIADO (MRUV)

1. Velocidade × Tempo          2. Posição × Tempo

   v                              S
   │    ╱                          │      ╱╲
   │   ╱                           │     ╱  ╲
   │  ╱ (reta)                     │    ╱    ╲ (parábola)
   │ ╱                             │   ╱      ╲
   └─────────── t                  └──────────── t

3. Aceleração × Tempo

   a
   │  ┌─────────┐
   │  │(constante)
   │  │         │
   └──┴─────────┴─── t

Características:
• v × t: Reta (inclinação = aceleração a)
• S × t: Parábola
• a × t: Horizontal (aceleração constante)
• Área sob v × t = deslocamento
• Área sob a × t = variação de velocidade
</pre>
</div>

<div id="outline-container-orgf924a5e" class="outline-5">
<h5 id="orgf924a5e"><span class="section-number-5">3.2.11.1.</span> Gráfico v × t (Velocidade × Tempo)</h5>
<div class="outline-text-5" id="text-3-2-11-1">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Reta inclinada</li>
<li>Inclinação = aceleração</li>
<li>Área sob a curva = deslocamento</li>
</ul>

<pre class="example" id="orgcaf5592">
v ↑
  |     /
  |    /  (a &gt; 0, movimento acelerado)
  |   /
  |  /
  | /
  |/___________→ t
</pre>

<pre class="example" id="org27cccb6">
v ↑
  |\\
  | \\   (a &lt; 0, movimento retardado)
  |  \\
  |   \\
  |    \\
  |_____\\______→ t
</pre>

<p>
<b>Inclinação = aceleração:</b>
</p>
<ul class="org-ul">
<li>Reta crescente → a &gt; 0</li>
<li>Reta decrescente → a &lt; 0</li>
<li>Quanto mais inclinada, maior o módulo de a</li>
</ul>

<p>
<b>Área sob a curva = deslocamento:</b> Δs = área do trapézio (ou triângulo + retângulo)
</p>
</div>
</div>

<div id="outline-container-org175b10e" class="outline-5">
<h5 id="org175b10e"><span class="section-number-5">3.2.11.2.</span> Gráfico s × t (Posição × Tempo)</h5>
<div class="outline-text-5" id="text-3-2-11-2">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Parábola (função do 2° grau)</li>
<li>Concavidade determina o sinal de a</li>
</ul>

<pre class="example" id="orge7ac536">
s ↑
  |      /
  |     /
  |    /     (a &gt; 0, concavidade para cima)
  |   /
  |  /
  |_/___________→ t
</pre>

<pre class="example" id="org32ee666">
s ↑
  |\\
  | \\____
  |      \\___   (a &lt; 0, concavidade para baixo)
  |          \\
  |           \\
  |____________→ t
</pre>

<p>
<b>Concavidade:</b>
</p>
<ul class="org-ul">
<li>Para cima (∪) → a &gt; 0</li>
<li>Para baixo (∩) → a &lt; 0</li>
</ul>
</div>
</div>

<div id="outline-container-orge4b9e1c" class="outline-5">
<h5 id="orge4b9e1c"><span class="section-number-5">3.2.11.3.</span> Gráfico a × t (Aceleração × Tempo)</h5>
<div class="outline-text-5" id="text-3-2-11-3">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Reta horizontal (aceleração constante)</li>
<li>Área sob a curva = variação da velocidade</li>
</ul>

<pre class="example" id="org13afa9e">
a ↑
  |____________
  |            (a constante e positiva)
  |
  |____________→ t
</pre>
</div>
</div>
</div>

<div id="outline-container-org0956796" class="outline-4">
<h4 id="org0956796"><span class="section-number-4">3.2.12.</span> Queda Livre</h4>
<div class="outline-text-4" id="text-3-2-12">
<p>
<b>Definição:</b> Movimento vertical de um corpo abandonado no vácuo (ou desprezando resistência do ar), sob ação exclusiva da gravidade.
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Movimento uniformemente variado (MRUV)</li>
<li>Aceleração = g (aceleração da gravidade)</li>
<li>g ≈ 10 m/s² (aproximação)</li>
<li>g = 9,8 m/s² (valor mais preciso)</li>
</ul>

<p>
<b>Orientação:</b>
</p>
<ul class="org-ul">
<li><b>Para baixo (↓):</b> consideramos positivo → g = +10 m/s²</li>
<li><b>Para cima (↑):</b> consideramos negativo → g = -10 m/s²</li>
</ul>
</div>
</div>

<div id="outline-container-orgc31f5f4" class="outline-4">
<h4 id="orgc31f5f4"><span class="section-number-4">3.2.13.</span> Equações da Queda Livre</h4>
<div class="outline-text-4" id="text-3-2-13">
<p>
Mesmas equações do MRUV, substituindo <b>a por g</b>:
</p>

<pre class="example" id="org2e37085">
1. v = v₀ + gt

2. h = h₀ + v₀t + (1/2)gt²

3. v² = v₀² + 2gΔh

4. v_m = (v₀ + v) / 2
</pre>

<p>
<b>Convenção usual:</b>
</p>
<ul class="org-ul">
<li>Eixo y positivo para <b>cima</b></li>
<li>g = -10 m/s² (gravidade aponta para baixo)</li>
<li>Altura h ao invés de posição s</li>
</ul>
</div>
</div>

<div id="outline-container-orgeff30c1" class="outline-4">
<h4 id="orgeff30c1"><span class="section-number-4">3.2.14.</span> Casos Especiais de Queda Livre</h4>
<div class="outline-text-4" id="text-3-2-14">
</div>
<div id="outline-container-org6844b01" class="outline-5">
<h5 id="org6844b01"><span class="section-number-5">3.2.14.1.</span> 1. Objeto Abandonado (v₀ = 0)</h5>
<div class="outline-text-5" id="text-3-2-14-1">
<p>
<b>Exemplo:</b> Soltar uma pedra do alto de um prédio
</p>

<ul class="org-ul">
<li>v₀ = 0</li>
<li>g = 10 m/s² (para baixo)</li>
</ul>

<p>
<b>Equações simplificadas:</b>
</p>
<ul class="org-ul">
<li>v = gt</li>
<li>h = (1/2)gt²</li>
<li>v² = 2gh</li>
</ul>

<p>
<b>Exemplo:</b> Uma pedra é solta de uma altura de 20 m. Com que velocidade atinge o solo? (g = 10 m/s²)
</p>

<p>
v² = v₀² + 2gΔh v² = 0 + 2(10)(20) v² = 400 v = 20 m/s
</p>

<p>
<b>Tempo de queda:</b> h = (1/2)gt² 20 = (1/2)(10)t² 20 = 5t² t² = 4 t = 2 s
</p>
</div>
</div>

<div id="outline-container-org6e16055" class="outline-5">
<h5 id="org6e16055"><span class="section-number-5">3.2.14.2.</span> 2. Lançamento Vertical para Baixo (v₀ &gt; 0)</h5>
<div class="outline-text-5" id="text-3-2-14-2">
<p>
<b>Exemplo:</b> Arremessar uma bola para baixo
</p>

<ul class="org-ul">
<li>v₀ &gt; 0 (velocidade inicial para baixo)</li>
<li>g = 10 m/s² (mesma direção)</li>
<li>Movimento acelerado</li>
</ul>
</div>
</div>

<div id="outline-container-org87669d1" class="outline-5">
<h5 id="org87669d1"><span class="section-number-5">3.2.14.3.</span> 3. Lançamento Vertical para Cima (v₀ &gt; 0)</h5>
<div class="outline-text-5" id="text-3-2-14-3">
<p>
<b>Exemplo:</b> Arremessar uma bola para cima
</p>

<p>
<b>Convenção:</b>
</p>
<ul class="org-ul">
<li>Eixo positivo: para cima</li>
<li>v₀ &gt; 0 (para cima)</li>
<li>g = -10 m/s² (para baixo)</li>
</ul>

<p>
<b>Fases do movimento:</b>
</p>

<p>
<b>Subida:</b>
</p>
<ul class="org-ul">
<li>v diminui (movimento retardado)</li>
<li>v e g têm sinais opostos</li>
<li>No ponto mais alto: v = 0</li>
</ul>

<p>
<b>Descida:</b>
</p>
<ul class="org-ul">
<li>v aumenta em módulo (movimento acelerado)</li>
<li>v e g têm mesmo sinal</li>
<li>Velocidade ao retornar = velocidade inicial (em módulo)</li>
</ul>

<p>
<b>Altura máxima:</b> No ponto mais alto, v = 0
</p>

<p>
v² = v₀² + 2g(-h_max) 0 = v₀²
</p>
<ul class="org-ul">
<li>2gh_max h_max = v₀² / (2g)</li>
</ul>

<p>
<b>Tempo de subida:</b> v = v₀ + gt 0 = v₀
</p>
<ul class="org-ul">
<li>gt_subida t_subida = v₀ / g</li>
</ul>

<p>
<b>Tempo total (subida + descida):</b> t_total = 2 × t_subida = 2v₀ / g
</p>

<p>
<b>Simetria:</b>
</p>
<ul class="org-ul">
<li>Tempo de subida = tempo de descida</li>
<li>Velocidade ao retornar = velocidade inicial (em módulo, mas sentido oposto)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgfce6a88" class="outline-4">
<h4 id="orgfce6a88"><span class="section-number-4">3.2.15.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-3-2-15">
</div>
<div id="outline-container-org99767e1" class="outline-5">
<h5 id="org99767e1"><span class="section-number-5">3.2.15.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-3-2-15-1">
<p>
Um carro parte do repouso com aceleração constante de 2 m/s². Calcule: a) A velocidade após 10 s b) A distância percorrida em 10 s
</p>

<p>
<b>Solução:</b> Dados: v₀ = 0, a = 2 m/s², t = 10 s
</p>

<ol class="org-ol">
<li>v = v₀ + at v = 0 + 2(10) v = 20 m/s</li>

<li>s = s₀ + v₀t + (1/2)at² s = 0 + 0 + (1/2)(2)(10²) s = 0 + 0 + 100 s = 100 m</li>
</ol>
</div>
</div>

<div id="outline-container-orgc848352" class="outline-5">
<h5 id="orgc848352"><span class="section-number-5">3.2.15.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-3-2-15-2">
<p>
Um móvel tem velocidade inicial de 20 m/s e desacelera a -4 m/s². Quanto tempo leva para parar?
</p>

<p>
<b>Solução:</b> Dados: v₀ = 20 m/s, a = -4 m/s², v = 0 (parar)
</p>

<p>
v = v₀ + at 0 = 20 + (-4)t 4t = 20 t = 5 s
</p>
</div>
</div>

<div id="outline-container-org21fcd83" class="outline-5">
<h5 id="org21fcd83"><span class="section-number-5">3.2.15.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-3-2-15-3">
<p>
Um carro a 15 m/s freia com desaceleração de 3 m/s². Qual a distância percorrida até parar?
</p>

<p>
<b>Solução:</b> Dados: v₀ = 15 m/s, v = 0, a = -3 m/s²
</p>

<p>
<b>Não temos t, use Torricelli!</b>
</p>

<p>
v² = v₀² + 2aΔs 0 = 15² + 2(-3)Δs 0 = 225
</p>
<ul class="org-ul">
<li>6Δs 6Δs = 225 Δs = 37,5 m</li>
</ul>
</div>
</div>

<div id="outline-container-org8caf8d9" class="outline-5">
<h5 id="org8caf8d9"><span class="section-number-5">3.2.15.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-3-2-15-4">
<p>
Uma pedra é solta do alto de um edifício de 45 m. Calcule: a) O tempo de queda b) A velocidade ao atingir o solo (Use g = 10 m/s²)
</p>

<p>
<b>Solução:</b> Dados: h = 45 m, v₀ = 0, g = 10 m/s²
</p>

<ol class="org-ol">
<li>h = (1/2)gt² 45 = (1/2)(10)t² 45 = 5t² t² = 9 t = 3 s</li>

<li>v = gt (pois v₀ = 0) v = 10(3) v = 30 m/s</li>
</ol>

<p>
<b>Ou usando Torricelli:</b> v² = 0 + 2(10)(45) v² = 900 v = 30 m/s
</p>
</div>
</div>

<div id="outline-container-orge2c16e5" class="outline-5">
<h5 id="orge2c16e5"><span class="section-number-5">3.2.15.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-3-2-15-5">
<p>
Uma bola é lançada verticalmente para cima com v₀ = 30 m/s. Calcule: a) Altura máxima b) Tempo para atingir altura máxima c) Tempo total no ar (Use g = 10 m/s²)
</p>

<p>
<b>Solução:</b> Dados: v₀ = 30 m/s, g = -10 m/s² (para cima)
</p>

<ol class="org-ol">
<li>Na altura máxima, v = 0 v² = v₀² + 2g(-h_max) 0 = 30² + 2(-10)h_max 0 = 900</li>
<li>20h_max 20h_max = 900 h_max = 45 m</li>

<li>v = v₀ + gt 0 = 30 + (-10)t 10t = 30 t = 3 s</li>

<li>t_total = 2 × t_subida = 2 × 3 = 6 s</li>
</ol>
</div>
</div>

<div id="outline-container-org151beca" class="outline-5">
<h5 id="org151beca"><span class="section-number-5">3.2.15.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-3-2-15-6">
<p>
Dois móveis partem do mesmo ponto. O primeiro tem velocidade constante de 20 m/s. O segundo parte do repouso com aceleração de 4 m/s². Quando o segundo alcança o primeiro?
</p>

<p>
<b>Solução:</b> <b>Móvel 1 (MRU):</b> s₁ = 20t <b>Móvel 2 (MRUV):</b> s₂ = 0 + 0 + (1/2)(4)t² = 2t²
</p>

<p>
<b>Quando se encontram:</b> s₁ = s₂ 20t = 2t² 2t²
</p>
<ul class="org-ul">
<li>20t = 0 2t(t</li>
<li>10) = 0</li>
</ul>

<p>
t = 0 (início) ou t = 10 s
</p>

<p>
<i>[Ver resposta 53 no final do documento]</i>
</p>

<p>
<b>Posição do encontro:</b> s = 20(10) = 200 m
</p>
</div>
</div>

<div id="outline-container-org6d3c6f8" class="outline-5">
<h5 id="org6d3c6f8"><span class="section-number-5">3.2.15.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-3-2-15-7">
<p>
Um trem viaja a 72 km/h quando o maquinista vê um obstáculo. Ele freia com desaceleração de 2 m/s². A que distância mínima do obstáculo ele deve iniciar a frenagem para não colidir?
</p>

<p>
<b>Solução:</b> Primeiro, converter: 72 km/h = 72/3,6 = 20 m/s
</p>

<p>
Dados: v₀ = 20 m/s, v = 0, a = -2 m/s²
</p>

<p>
v² = v₀² + 2aΔs 0 = 20² + 2(-2)Δs 0 = 400
</p>
<ul class="org-ul">
<li>4Δs 4Δs = 400 Δs = 100 m</li>
</ul>

<p>
<i>[Ver resposta 54 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org4c1574b" class="outline-4">
<h4 id="org4c1574b"><span class="section-number-4">3.2.16.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-3-2-16">
<ol class="org-ol">
<li><b>Identifique o tipo de movimento:</b> MRU (v constante) ou MRUV (a constante)?</li>
<li><b>Liste os dados:</b> v₀, v, a, t, Δs</li>
<li>o que você tem? O que quer?</li>
<li><b>Sem tempo no problema?</b> Use Torricelli: v² = v₀² + 2aΔs</li>
<li><b>Queda livre:</b> Use g = 10 m/s² (ou 9,8 se especificado)</li>
<li><b>Atenção aos sinais:</b>
<ul class="org-ul">
<li>Defina um referencial (positivo para cima ou para baixo)</li>
<li>Mantenha consistência</li>
</ul></li>
<li><b>Conversão:</b> km/h → m/s: divida por 3,6</li>
<li><b>Gráficos:</b>
<ul class="org-ul">
<li>v×t: inclinação = a, área = Δs</li>
<li>s×t: concavidade indica sinal de a</li>
</ul></li>
<li><b>Lançamento vertical:</b> No ponto mais alto, v = 0</li>
</ol>
</div>
</div>

<div id="outline-container-org6e8b3b8" class="outline-4">
<h4 id="org6e8b3b8"><span class="section-number-4">3.2.17.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-3-2-17">
<p>
<b>MRUV:</b>
</p>
<ul class="org-ul">
<li>Aceleração constante (≠ 0)</li>
<li>Velocidade varia uniformemente</li>
<li>4 equações principais</li>
</ul>

<p>
<b>Queda Livre:</b>
</p>
<ul class="org-ul">
<li>MRUV com a = g</li>
<li>g ≈ 10 m/s²</li>
<li>Abandonado: v₀ = 0</li>
<li>Lançado para cima: no topo v = 0</li>
</ul>

<p>
<b>Sinais:</b>
</p>
<ul class="org-ul">
<li>Movimento acelerado: v e a mesmo sinal</li>
<li>Movimento retardado: v e a sinais opostos</li>
</ul>

<p>
<b>Gráficos:</b>
</p>
<ul class="org-ul">
<li>v×t: reta (inclinação = a)</li>
<li>s×t: parábola (concavidade mostra sinal de a)</li>
<li>a×t: reta horizontal</li>
</ul>
</div>
</div>

<div id="outline-container-org73daf2a" class="outline-4">
<h4 id="org73daf2a"><span class="section-number-4">3.2.18.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-2-18">
<pre class="example" id="org22456da">
Equações do MRUV:

v = v₀ + at

s = s₀ + v₀t + (1/2)at²

v² = v₀² + 2aΔs  (Torricelli
- sem tempo)

v_m = (v₀ + v) / 2  (válida só para MRUV)

Queda Livre (substitua a por g):

v = v₀ + gt

h = h₀ + v₀t + (1/2)gt²

v² = v₀² + 2gΔh

Altura máxima (lançamento vertical):
h_max = v₀² / (2g)

Tempo de subida:
t_subida = v₀ / g

Tempo total:
t_total = 2v₀ / g

Conversão:
km/h → m/s: dividir por 3,6
m/s → km/h: multiplicar por 3,6
</pre>
</div>
</div>

<div id="outline-container-org20c4c3d" class="outline-4">
<h4 id="org20c4c3d"><span class="section-number-4">3.2.19.</span> Tabela Resumo</h4>
<div class="outline-text-4" id="text-3-2-19">
<pre class="example" id="orgabc0ce1">
┌──────────────────┬─────────────────────────────┐
│   Grandeza       │        MRUV                 │
├──────────────────┼─────────────────────────────┤
│ Velocidade       │ Variável (uniformemente)    │
│ Aceleração       │ Constante (≠ 0)             │
│ Gráfico v×t      │ Reta inclinada              │
│ Gráfico s×t      │ Parábola                    │
│ Gráfico a×t      │ Reta horizontal             │
└──────────────────┴─────────────────────────────┘

┌──────────────────────┬────────────────────────┐
│   Situação           │     Equação Ideal      │
├──────────────────────┼────────────────────────┤
│ Tem t, quer v        │ v = v₀ + at            │
│ Tem t, quer s        │ s = s₀ + v₀t + ½at²   │
│ NÃO tem t            │ v² = v₀² + 2aΔs        │
│ Quer v_média         │ v_m = (v₀ + v) / 2     │
└──────────────────────┴────────────────────────┘
</pre>
</div>
</div>

<div id="outline-container-orgfd121bc" class="outline-4">
<h4 id="orgfd121bc"><span class="section-number-4">3.2.20.</span> Erros Comuns a Evitar</h4>
<div class="outline-text-4" id="text-3-2-20">
<ol class="org-ol">
<li><b>Confundir MRU com MRUV</b>
<ul class="org-ul">
<li>MRU: s = s₀ + vt (sem termo at²)</li>
<li>MRUV: s = s₀ + v₀t + (1/2)at²</li>
</ul></li>
<li><b>Esquecer o (1/2) na equação do espaço</b>
<ul class="org-ul">
<li>Correto: s = s₀ + v₀t + *(1/2)*at²</li>
<li>Errado: s = s₀ + v₀t + at²</li>
</ul></li>
<li><b>Usar v_m = (v₀+v)/2 no MRU</b>
<ul class="org-ul">
<li>Só vale para MRUV!</li>
<li>No MRU, v_m = v (constante)</li>
</ul></li>
<li><b>Sinais inconsistentes</b>
<ul class="org-ul">
<li>Defina um referencial e mantenha!</li>
<li>Para cima: g = -10 m/s²</li>
<li>Para baixo: g = +10 m/s²</li>
</ul></li>
<li><b>Não converter km/h para m/s</b>
<ul class="org-ul">
<li>Sempre converta para SI!</li>
<li>72 km/h = 20 m/s</li>
</ul></li>
</ol>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>cai muito em vestibulares)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgc413905" class="outline-3">`;

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
