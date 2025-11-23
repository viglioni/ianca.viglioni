<script setup lang="ts">
import { ref } from "vue";

const code = "fis-8";
const title = "Física: Cinemática";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-3">
<ul class="org-ul">
<li>Física: Cinemática</li>
<li>MRU (Movimento Retilíneo Uniforme)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orge3e7527" class="outline-4">
<h4 id="orge3e7527"><span class="section-number-4">2.3.1.</span> O que é Cinemática?</h4>
<div class="outline-text-4" id="text-2-3-1">
<p>
<b>Cinemática</b> é o ramo da Física que estuda o movimento dos corpos sem se preocupar com as causas (forças). Foca em descrever <b>como</b> os corpos se movem.
</p>

<p>
<b>Grandezas cinemáticas:</b>
</p>
<ul class="org-ul">
<li>Posição</li>
<li>Deslocamento</li>
<li>Velocidade</li>
<li>Aceleração</li>
<li>Tempo</li>
</ul>
</div>
</div>

<div id="outline-container-orgd9d7f4d" class="outline-4">
<h4 id="orgd9d7f4d"><span class="section-number-4">2.3.2.</span> Conceitos Fundamentais</h4>
<div class="outline-text-4" id="text-2-3-2">
</div>
<div id="outline-container-org3cdebe1" class="outline-5">
<h5 id="org3cdebe1"><span class="section-number-5">2.3.2.1.</span> Referencial</h5>
<div class="outline-text-5" id="text-2-3-2-1">
<p>
<b>Definição:</b> Sistema de coordenadas em relação ao qual descrevemos o movimento.
</p>

<p>
<b>Importância:</b> O movimento é relativo
</p>
<ul class="org-ul">
<li>depende do referencial escolhido.</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>Você sentado em um trem em movimento:</li>
<li>Em relação ao trem: está parado</li>
<li>Em relação à Terra: está em movimento</li>
</ul>
</div>
</div>

<div id="outline-container-org0bd0e33" class="outline-5">
<h5 id="org0bd0e33"><span class="section-number-5">2.3.2.2.</span> Trajetória</h5>
<div class="outline-text-5" id="text-2-3-2-2">
<p>
<b>Definição:</b> Linha que une todas as posições ocupadas pelo corpo durante o movimento.
</p>

<p>
<b>Tipos:</b>
</p>
<ul class="org-ul">
<li>Retilínea (linha reta)</li>
<li>Curvilínea (curva)</li>
<li>Circular</li>
</ul>

<p>
<b>Depende do referencial:</b> A trajetória pode mudar conforme o referencial.
</p>
</div>
</div>

<div id="outline-container-org9447d71" class="outline-5">
<h5 id="org9447d71"><span class="section-number-5">2.3.2.3.</span> Posição (S)</h5>
<div class="outline-text-5" id="text-2-3-2-3">
<p>
<b>Definição:</b> Localização do corpo em relação ao referencial.
</p>

<p>
<b>Unidade SI:</b> metro (m)
</p>

<p>
<b>Notação:</b>
</p>
<ul class="org-ul">
<li>S = posição em instante genérico</li>
<li>S₀ = posição inicial (em t = 0)</li>
<li>S_f = posição final</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org7ab28e5">
Origem (0)     10m      20m      30m
    |-----------|---------|---------|
              S₀=10m            S=25m
</pre>
</div>
</div>

<div id="outline-container-orge479642" class="outline-5">
<h5 id="orge479642"><span class="section-number-5">2.3.2.4.</span> Deslocamento (ΔS)</h5>
<div class="outline-text-5" id="text-2-3-2-4">
<p>
<b>Definição:</b> Variação de posição entre dois instantes.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org7a3a3de">
ΔS = S_f
- S₀
</pre>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Pode ser positivo (movimento no sentido positivo)</li>
<li>Pode ser negativo (movimento no sentido negativo)</li>
<li>Pode ser zero (voltou à posição inicial)</li>
</ul>

<p>
<b>Diferença entre deslocamento e distância percorrida:</b>
</p>
<ul class="org-ul">
<li><b>Deslocamento:</b> variação de posição (vetorial)</li>
<li><b>Distância percorrida:</b> total percorrido (escalar)</li>
</ul>

<p>
<b>Exemplo:</b> Uma pessoa sai da posição 10 m, vai até 30 m e volta para 15 m.
</p>
<ul class="org-ul">
<li>Distância percorrida: 20 m + 15 m = 35 m</li>
<li>Deslocamento: 15 m</li>
<li>10 m = 5 m</li>
</ul>
</div>
</div>

<div id="outline-container-org3b4164f" class="outline-5">
<h5 id="org3b4164f"><span class="section-number-5">2.3.2.5.</span> Velocidade</h5>
<div class="outline-text-5" id="text-2-3-2-5">
<p>
<b>Definição:</b> Grandeza que indica a rapidez e o sentido do movimento.
</p>

<p>
<b>Unidade SI:</b> m/s (metro por segundo)
</p>

<p>
<b>Outras unidades:</b> km/h, cm/s
</p>

<p>
<b>Conversão importante:</b>
</p>
<ul class="org-ul">
<li>1 m/s = 3,6 km/h</li>
<li>1 km/h = 1/3,6 m/s ≈ 0,278 m/s</li>
</ul>

<p>
<b>Para converter:</b>
</p>
<ul class="org-ul">
<li>km/h → m/s: dividir por 3,6</li>
<li>m/s → km/h: multiplicar por 3,6</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org4b251b8" class="outline-4">
<h4 id="org4b251b8"><span class="section-number-4">2.3.3.</span> Movimento Retilíneo Uniforme (MRU)</h4>
<div class="outline-text-4" id="text-2-3-3">
</div>
<div id="outline-container-org1b36cc1" class="outline-5">
<h5 id="org1b36cc1"><span class="section-number-5">2.3.3.1.</span> Definição</h5>
<div class="outline-text-5" id="text-2-3-3-1">
<p>
<b>MRU</b> é o movimento em que:
</p>
<ul class="org-ul">
<li>Trajetória é uma <b>reta</b></li>
<li>Velocidade é <b>constante</b> (não muda)</li>
<li>Não há aceleração (a = 0)</li>
</ul>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Percorre distâncias iguais em intervalos de tempo iguais</li>
<li>Velocidade instantânea = velocidade média</li>
</ul>
</div>
</div>

<div id="outline-container-org4175f35" class="outline-5">
<h5 id="org4175f35"><span class="section-number-5">2.3.3.2.</span> Velocidade no MRU</h5>
<div class="outline-text-5" id="text-2-3-3-2">
<p>
Como a velocidade é constante:
</p>

<p>
<b>v = constante</b>
</p>

<p>
<b>Fórmula da velocidade:</b>
</p>

<pre class="example" id="org5259365">
v = ΔS / Δt

Onde:
- v = velocidade (m/s ou km/h)
- ΔS = deslocamento (m ou km)
- Δt = intervalo de tempo (s ou h)
</pre>

<p>
<b>Desenvolvendo:</b>
</p>

<pre class="example" id="org523ff33">
v = (S
- S₀) / (t
- t₀)

Se t₀ = 0:
v = (S
- S₀) / t
</pre>
</div>
</div>

<div id="outline-container-org3004cdd" class="outline-5">
<h5 id="org3004cdd"><span class="section-number-5">2.3.3.3.</span> Função Horária da Posição no MRU</h5>
<div class="outline-text-5" id="text-2-3-3-3">
<p>
<b>Equação fundamental do MRU:</b>
</p>

<pre class="example" id="org7001be9">
S = S₀ + vt

Onde:
- S = posição final (m)
- S₀ = posição inicial (m)
- v = velocidade (m/s)
- t = tempo (s)
</pre>

<p>
<b>Esta é uma função do 1º grau:</b> S(t) = S₀ + vt
</p>

<p>
<b>Significado dos termos:</b>
</p>
<ul class="org-ul">
<li><b>S₀:</b> posição quando t = 0 (coeficiente linear)</li>
<li><b>v:</b> velocidade (coeficiente angular</li>
<li>inclinação da reta)</li>
</ul>
</div>
</div>

<div id="outline-container-org347885f" class="outline-5">
<h5 id="org347885f"><span class="section-number-5">2.3.3.4.</span> Gráficos do MRU</h5>
</div>
</div>
<div id="outline-container-org29791cc" class="outline-4">
<h4 id="org29791cc"><span class="section-number-4">2.3.4.</span> 1. Gráfico S × t (Posição × Tempo)</h4>
<div class="outline-text-4" id="text-2-3-4">
<p>
<b>Característica:</b> Reta (função do 1º grau)
</p>

<pre class="example" id="orgace36e8">
S ↑
  |      /
  |    /    ← v &gt; 0 (movimento progressivo)
  |  /
  |/___________→ t
 S₀

S ↑
  |\\
  |  \\      ← v &lt; 0 (movimento retrógrado)
  |    \\
  |______\\_____→ t
        S₀
</pre>

<p>
<b>Interpretações:</b>
</p>
<ul class="org-ul">
<li><b>Inclinação (coeficiente angular):</b> valor da velocidade</li>
<li>Reta mais inclinada = maior velocidade</li>
<li>Inclinação positiva = v &gt; 0</li>
<li>Inclinação negativa = v &lt; 0</li>

<li><b>Coeficiente linear:</b> posição inicial (S₀)</li>

<li><p>
<b>Velocidade a partir do gráfico:</b>
</p>

<pre class="example" id="org4edc525">
  v = ΔS / Δt = (S₂
- S₁) / (t₂
- t₁)
</pre></li>
</ul>
</div>
</div>

<div id="outline-container-orgf0a627b" class="outline-4">
<h4 id="orgf0a627b"><span class="section-number-4">2.3.5.</span> 2. Gráfico v × t (Velocidade × Tempo)</h4>
<div class="outline-text-4" id="text-2-3-5">
<p>
<b>Característica:</b> Reta horizontal (velocidade constante)
</p>

<pre class="example" id="org849e6c6">
v ↑
  |________
  |        |______→ t
  0
  
Velocidade constante = MRU
</pre>

<p>
<b>Área sob o gráfico:</b> A área entre a reta e o eixo do tempo representa o <b>deslocamento</b>.
</p>

<pre class="example" id="org6dc0fa3">
Área = base × altura = t × v = ΔS
</pre>
</div>
</div>

<div id="outline-container-org4d4a53a" class="outline-4">
<h4 id="org4d4a53a"><span class="section-number-4">2.3.6.</span> Movimento Progressivo e Retrógrado</h4>
<div class="outline-text-4" id="text-2-3-6">
</div>
<div id="outline-container-org6e03f81" class="outline-5">
<h5 id="org6e03f81"><span class="section-number-5">2.3.6.1.</span> Movimento Progressivo</h5>
<div class="outline-text-5" id="text-2-3-6-1">
<ul class="org-ul">
<li><b>v &gt; 0</b> (velocidade positiva)</li>
<li>Corpo se afasta da origem</li>
<li>Posição aumenta com o tempo</li>
</ul>
</div>
</div>

<div id="outline-container-org4472830" class="outline-5">
<h5 id="org4472830"><span class="section-number-5">2.3.6.2.</span> Movimento Retrógrado</h5>
<div class="outline-text-5" id="text-2-3-6-2">
<ul class="org-ul">
<li><b>v &lt; 0</b> (velocidade negativa)</li>
<li>Corpo se aproxima da origem</li>
<li>Posição diminui com o tempo</li>
</ul>

<p>
<b>Observação:</b> O sinal da velocidade indica o sentido, não se o corpo está “rápido” ou “lento”.
</p>
</div>
</div>
</div>

<div id="outline-container-org8687d6c" class="outline-4">
<h4 id="org8687d6c"><span class="section-number-4">2.3.7.</span> Encontro de Móveis</h4>
<div class="outline-text-4" id="text-2-3-7">
<p>
Dois móveis se encontram quando ocupam a mesma posição no mesmo instante.
</p>

<p>
<b>Condição de encontro:</b>
</p>

<pre class="example" id="orgdd9ab93">
S₁ = S₂
</pre>

<p>
<b>Método:</b> 1. Escrever a função horária de cada móvel 2. Igualar as posições 3. Resolver a equação para encontrar t 4. Substituir t em uma das equações para encontrar S
</p>

<p>
<b>Exemplo:</b> Móvel A: S_A = 10 + 5t Móvel B: S_B = 50 + 2t
</p>

<p>
Encontro:
</p>

<pre class="example" id="org04a4200">
10 + 5t = 50 + 2t
5t
- 2t = 50
- 10
3t = 40
t = 40/3 ≈ 13,3 s

Posição do encontro:
S = 10 + 5(40/3) = 10 + 200/3 ≈ 76,7 m
</pre>
</div>
</div>

<div id="outline-container-orgf868fe4" class="outline-4">
<h4 id="orgf868fe4"><span class="section-number-4">2.3.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-3-8">
</div>
<div id="outline-container-orgc82a2db" class="outline-5">
<h5 id="orgc82a2db"><span class="section-number-5">2.3.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-3-8-1">
<p>
Um carro percorre 180 km em 2 horas. Qual sua velocidade média?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgddd78e5">
v = ΔS / Δt
v = 180 km / 2 h
v = 90 km/h
</pre>

<p>
<b>Em m/s:</b>
</p>

<pre class="example" id="orgccbda7f">
v = 90 / 3,6 = 25 m/s
</pre>
</div>
</div>

<div id="outline-container-orgf3e7288" class="outline-5">
<h5 id="orgf3e7288"><span class="section-number-5">2.3.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-3-8-2">
<p>
Um móvel parte da posição 20 m com velocidade constante de 5 m/s. Determine: a) A função horária da posição b) A posição em t = 10 s c) O instante em que passa pela posição 70 m
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li><b>Função horária:</b></li>
</ol>

<pre class="example" id="orgc9e75e3">
S = S₀ + vt
S = 20 + 5t
</pre>

<ol class="org-ol">
<li value="2"><b>Posição em t = 10 s:</b></li>
</ol>

<pre class="example" id="org44c77b8">
S = 20 + 5(10)
S = 20 + 50
S = 70 m
</pre>

<ol class="org-ol">
<li value="3"><b>Instante em que S = 70 m:</b></li>
</ol>

<pre class="example" id="org9f3142c">
70 = 20 + 5t
50 = 5t
t = 10 s
</pre>
</div>
</div>

<div id="outline-container-orgd22808a" class="outline-5">
<h5 id="orgd22808a"><span class="section-number-5">2.3.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-3-8-3">
<p>
Dois carros partem simultaneamente de posições diferentes. O carro A parte da posição 0 com velocidade 20 m/s. O carro B parte da posição 100 m com velocidade 15 m/s, ambos no mesmo sentido. Quando e onde o carro A alcança o carro B?
</p>

<p>
<b>Solução:</b>
</p>

<p>
Funções horárias:
</p>

<pre class="example" id="orgb86703f">
Carro A: S_A = 0 + 20t = 20t
Carro B: S_B = 100 + 15t
</pre>

<p>
Encontro (S_A = S_B):
</p>

<pre class="example" id="org25f4ea1">
20t = 100 + 15t
20t
- 15t = 100
5t = 100
t = 20 s
</pre>

<p>
Posição do encontro:
</p>

<pre class="example" id="orge3ff480">
S = 20(20) = 400 m
</pre>

<p>
<i>[Ver resposta 33 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org9a8600b" class="outline-5">
<h5 id="org9a8600b"><span class="section-number-5">2.3.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-3-8-4">
<p>
Um trem de 200 m de comprimento atravessa uma ponte de 300 m com velocidade constante de 20 m/s. Quanto tempo leva para atravessar completamente a ponte?
</p>

<p>
<b>Solução:</b>
</p>

<p>
Para atravessar completamente, o trem deve percorrer:
</p>

<pre class="example" id="org1eb7c23">
Distância = comprimento da ponte + comprimento do trem
ΔS = 300 + 200 = 500 m
</pre>

<p>
Tempo:
</p>

<pre class="example" id="orgf943b44">
v = ΔS / Δt
20 = 500 / Δt
Δt = 500 / 20
Δt = 25 s
</pre>

<p>
<i>[Ver resposta 34 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgd28f89c" class="outline-5">
<h5 id="orgd28f89c"><span class="section-number-5">2.3.8.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-3-8-5">
<p>
Converta 108 km/h para m/s.
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org62f60ef">
v = 108 / 3,6 = 30 m/s
</pre>
</div>
</div>

<div id="outline-container-org32ede92" class="outline-5">
<h5 id="org32ede92"><span class="section-number-5">2.3.8.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-2-3-8-6">
<p>
Um gráfico S × t mostra uma reta que passa pelos pontos (0, 10) e (5, 35). Determine: a) A posição inicial b) A velocidade c) A função horária
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li><b>Posição inicial:</b> S₀ = 10 m (quando t = 0)</li>

<li><b>Velocidade:</b></li>
</ol>

<pre class="example" id="orgbc8e2a1">
v = ΔS / Δt = (35
- 10) / (5
- 0)
v = 25 / 5
v = 5 m/s
</pre>

<ol class="org-ol">
<li value="3"><b>Função horária:</b></li>
</ol>

<pre class="example" id="org5ac99a5">
S = S₀ + vt
S = 10 + 5t
</pre>
</div>
</div>
</div>

<div id="outline-container-orge1c6d56" class="outline-4">
<h4 id="orge1c6d56"><span class="section-number-4">2.3.9.</span> Aplicações Práticas do MRU</h4>
<div class="outline-text-4" id="text-2-3-9">
<p>
<b>1. Esteiras rolantes:</b> movimento uniforme <b>2. Trens e metrôs:</b> aproximação de MRU em trechos retos <b>3. Objetos em órbita:</b> movimento aproximadamente uniforme <b>4. Luz no vácuo:</b> MRU perfeito (c = 3 × 10⁸ m/s)
</p>
</div>
</div>

<div id="outline-container-orgb3f7312" class="outline-4">
<h4 id="orgb3f7312"><span class="section-number-4">2.3.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-3-10">
<ol class="org-ol">
<li><b>Conversão:</b> Sempre verifique as unidades! km/h ↔ m/s (÷ ou × 3,6)</li>
<li><b>Sinais:</b> Velocidade negativa = movimento retrógrado</li>
<li><b>Gráfico S×t:</b> Inclinação = velocidade</li>
<li><b>Gráfico v×t:</b> Área = deslocamento</li>
<li><b>Encontro:</b> Igualar as posições (S₁ = S₂)</li>
<li><b>Distância vs Deslocamento:</b> Cuidado com a diferença</li>
<li><b>Função horária:</b> S = S₀ + vt (sempre!)</li>
</ol>
</div>
</div>

<div id="outline-container-org1600c76" class="outline-4">
<h4 id="org1600c76"><span class="section-number-4">2.3.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-3-11">
<p>
<b>MRU:</b>
</p>
<ul class="org-ul">
<li>Movimento retilíneo</li>
<li>Velocidade constante</li>
<li>Aceleração = 0</li>
<li>Distâncias iguais em tempos iguais</li>
</ul>

<p>
<b>Fórmulas:</b>
</p>
<ul class="org-ul">
<li>v = ΔS / Δt</li>
<li>S = S₀ + vt</li>
</ul>

<p>
<b>Gráficos:</b>
</p>
<ul class="org-ul">
<li><b>S × t:</b> reta inclinada</li>
<li><b>v × t:</b> reta horizontal</li>
</ul>

<p>
<b>Sinais:</b>
</p>
<ul class="org-ul">
<li>v &gt; 0: progressivo (afasta da origem)</li>
<li>v &lt; 0: retrógrado (aproxima da origem)</li>
</ul>
</div>
</div>

<div id="outline-container-org33d1dd9" class="outline-4">
<h4 id="org33d1dd9"><span class="section-number-4">2.3.12.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-3-12">
<pre class="example" id="org6455725">
Velocidade (constante no MRU):
v = ΔS / Δt = (S
- S₀) / t

Função Horária da Posição:
S = S₀ + vt

Conversão de unidades:
1 m/s = 3,6 km/h
km/h → m/s: dividir por 3,6
m/s → km/h: multiplicar por 3,6

Encontro de móveis:
S₁ = S₂
(igualar as funções horárias)

Deslocamento:
ΔS = S_final
- S_inicial

Área no gráfico v×t:
Área = deslocamento = v × t
</pre>
</div>
</div>

<div id="outline-container-orgfcdded5" class="outline-4">
<h4 id="orgfcdded5"><span class="section-number-4">2.3.13.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-2-3-13">
<pre class="example" id="org3d5b0d9">
MRU
- Características:
┌─────────────────────────────────┐
│ Trajetória: RETA                │
│ Velocidade: CONSTANTE           │
│ Aceleração: ZERO                │
│ Equação: S = S₀ + vt           │
└─────────────────────────────────┘

Gráfico S×t        Gráfico v×t
    S ↑                v ↑
      |  /               |____
      | /                |    
      |/___→ t           |____→ t
     S₀                  0
   (reta)            (horizontal)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para toda cinemática)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgea23c4e" class="outline-3">`;

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
