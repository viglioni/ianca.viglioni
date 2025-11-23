<script setup lang="ts">
import { ref } from "vue";

const code = "mat-16";
const title = "Matemática: Função Afim";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-1">
<ul class="org-ul">
<li>Matemática: Função Afim</li>
<li>Parte 1</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-orgbf2a483" class="outline-4">
<h4 id="orgbf2a483"><span class="section-number-4">4.1.1.</span> O que é Função?</h4>
<div class="outline-text-4" id="text-4-1-1">
<p>
<b>Função</b> é uma relação entre dois conjuntos (domínio e contradomínio) onde cada elemento do domínio está associado a um único elemento do contradomínio.
</p>

<p>
<b>Notação:</b> f: A → B (lê-se “f de A em B”)
</p>
<ul class="org-ul">
<li>f(x) = y (lê-se “f de x igual a y”)</li>
<li>x: variável independente (entrada)</li>
<li>y: variável dependente (saída)</li>
</ul>

<p>
<b>Exemplo prático:</b>
</p>
<ul class="org-ul">
<li>Preço de laranjas: f(x) = 5x</li>
<li>x = número de laranjas</li>
<li>f(x) = preço total</li>
<li>f(3) = 5(3) = 15 reais</li>
</ul>
</div>
</div>

<div id="outline-container-org2175a0c" class="outline-4">
<h4 id="org2175a0c"><span class="section-number-4">4.1.2.</span> Função Afim (ou Função do 1º Grau)</h4>
<div class="outline-text-4" id="text-4-1-2">
<p>
<b>Definição:</b> Função afim é toda função f: ℝ → ℝ da forma:
</p>

<pre class="example" id="orgae823d2">
f(x) = ax + b
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li><b>a</b> e <b>b</b> são números reais</li>
<li><b>a ≠ 0</b> (se a = 0, é função constante)</li>
<li><b>a</b>: coeficiente angular (taxa de variação)</li>
<li><b>b</b>: coeficiente linear (valor inicial, quando x = 0)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>f(x) = 2x + 3 (a = 2, b = 3)</li>
<li>f(x) = -x + 5 (a = -1, b = 5)</li>
<li>f(x) = 3x (a = 3, b = 0)</li>
<li>f(x) = -4 + 2x (a = 2, b = -4)</li>
</ul>
</div>
</div>

<div id="outline-container-org346daaa" class="outline-4">
<h4 id="org346daaa"><span class="section-number-4">4.1.3.</span> Coeficientes da Função Afim</h4>
<div class="outline-text-4" id="text-4-1-3">
</div>
<div id="outline-container-org9de0d53" class="outline-5">
<h5 id="org9de0d53"><span class="section-number-5">4.1.3.1.</span> Coeficiente Linear (b)</h5>
<div class="outline-text-5" id="text-4-1-3-1">
<p>
<b>Representa:</b>
</p>
<ul class="org-ul">
<li>Valor de f(x) quando x = 0</li>
<li>Ponto onde a reta corta o eixo y</li>
<li>Valor inicial</li>
</ul>

<p>
<b>Exemplo:</b> f(x) = 2x + 3 f(0) = 2(0) + 3 = 3 Ponto (0, 3) no eixo y
</p>
</div>
</div>

<div id="outline-container-org797cb5d" class="outline-5">
<h5 id="org797cb5d"><span class="section-number-5">4.1.3.2.</span> Coeficiente Angular (a)</h5>
<div class="outline-text-5" id="text-4-1-3-2">
<p>
<b>Representa:</b>
</p>
<ul class="org-ul">
<li>Taxa de variação da função</li>
<li>Inclinação da reta</li>
<li>Quanto y varia quando x aumenta 1 unidade</li>
</ul>

<p>
<b>Interpretação:</b>
</p>
<ul class="org-ul">
<li>a &gt; 0: função crescente</li>
<li>a &lt; 0: função decrescente</li>
<li>|a| maior: reta mais inclinada</li>
</ul>

<p>
<b>Exemplo:</b> f(x) = 2x + 3 Quando x aumenta 1, y aumenta 2
</p>
<ul class="org-ul">
<li>f(0) = 3</li>
<li>f(1) = 5 (aumentou 2)</li>
<li>f(2) = 7 (aumentou 2)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org4fc5a4e" class="outline-4">
<h4 id="org4fc5a4e"><span class="section-number-4">4.1.4.</span> Casos Especiais</h4>
<div class="outline-text-4" id="text-4-1-4">
</div>
<div id="outline-container-org52d48ae" class="outline-5">
<h5 id="org52d48ae"><span class="section-number-5">4.1.4.1.</span> Função Linear (b = 0)</h5>
<div class="outline-text-5" id="text-4-1-4-1">
<p>
f(x) = ax
</p>

<ul class="org-ul">
<li>Passa pela origem (0, 0)</li>
<li>Proporcionalidade direta</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>f(x) = 3x</li>
<li>f(x) = -2x</li>
</ul>
</div>
</div>

<div id="outline-container-org11590d8" class="outline-5">
<h5 id="org11590d8"><span class="section-number-5">4.1.4.2.</span> Função Constante (a = 0)</h5>
<div class="outline-text-5" id="text-4-1-4-2">
<p>
f(x) = b
</p>

<ul class="org-ul">
<li>Reta horizontal</li>
<li>Valor sempre igual a b</li>
<li><b>Tecnicamente não é função afim</b> (a deve ser ≠ 0)</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>f(x) = 5 (sempre vale 5)</li>
</ul>
</div>
</div>

<div id="outline-container-org3d2da58" class="outline-5">
<h5 id="org3d2da58"><span class="section-number-5">4.1.4.3.</span> Função Identidade (a = 1, b = 0)</h5>
<div class="outline-text-5" id="text-4-1-4-3">
<p>
f(x) = x
</p>

<ul class="org-ul">
<li>Bissetriz do 1º e 3º quadrantes</li>
<li>Ângulo de 45° com os eixos</li>
<li>f(x) = x para todo x</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgcdc0996" class="outline-4">
<h4 id="orgcdc0996"><span class="section-number-4">4.1.5.</span> Gráfico da Função Afim</h4>
<div class="outline-text-4" id="text-4-1-5">
<pre class="example" id="orgb7b3902">
GRÁFICO FUNÇÃO AFIM: f(x) = ax + b

Se a &gt; 0 (crescente):        Se a &lt; 0 (decrescente):

     y                            y
     │         ╱                  │╲
     │        ╱                   │ ╲
     │       ╱                    │  ╲
     │      ╱                     │   ╲
─────┼─────╱────── x         ─────┼────╲──── x
     │    ╱                        │     ╲
     │   ╱                         │      ╲
     │  ╱                          │       ╲

• Coeficiente angular a: inclinação
• Coeficiente linear b: interseção com eixo y
• Raiz (zero): ponto onde f(x) = 0
</pre>

<p>
<b>O gráfico é sempre uma RETA.</b>
</p>
</div>

<div id="outline-container-orge59d168" class="outline-5">
<h5 id="orge59d168"><span class="section-number-5">4.1.5.1.</span> Como Construir o Gráfico</h5>
<div class="outline-text-5" id="text-4-1-5-1">
<p>
<b>Método 1: Dois pontos</b>
</p>

<p>
Basta encontrar 2 pontos e traçar a reta.
</p>

<p>
<b>Pontos mais fáceis:</b> 1. <b>Quando x = 0:</b> f(0) = b → ponto (0, b) 2. <b>Quando f(x) = 0:</b> Zero da função → ponto (raiz, 0)
</p>

<p>
<b>Exemplo:</b> f(x) = 2x
</p>
<ul class="org-ul">
<li>4</li>
</ul>

<p>
<b>Ponto 1:</b> x = 0 f(0) = 2(0)
</p>
<ul class="org-ul">
<li>4 = -4 → (0, -4)</li>
</ul>

<p>
<b>Ponto 2:</b> f(x) = 0 0 = 2x
</p>
<ul class="org-ul">
<li>4 2x = 4 x = 2 → (2, 0)</li>
</ul>

<p>
Traçar reta pelos pontos (0, -4) e (2, 0).
</p>

<p>
<b>Método 2: Tabela de valores</b>
</p>

<p>
Escolher valores de x e calcular f(x).
</p>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">x</td>
<td class="org-left">f(x) = 2x</td>
</tr>
</tbody>
</table>
<ul class="org-ul">
<li>4 |</li>
</ul>
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<tbody>
<tr>
<td class="org-right">0</td>
<td class="org-right">-4</td>
</tr>

<tr>
<td class="org-right">1</td>
<td class="org-right">-2</td>
</tr>

<tr>
<td class="org-right">2</td>
<td class="org-right">0</td>
</tr>

<tr>
<td class="org-right">3</td>
<td class="org-right">2</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>

<div id="outline-container-orgfdbe629" class="outline-4">
<h4 id="orgfdbe629"><span class="section-number-4">4.1.6.</span> Análise do Gráfico</h4>
<div class="outline-text-4" id="text-4-1-6">
</div>
<div id="outline-container-orgffc399e" class="outline-5">
<h5 id="orgffc399e"><span class="section-number-5">4.1.6.1.</span> Função Crescente (a &gt; 0)</h5>
<div class="outline-text-5" id="text-4-1-6-1">
<pre class="example" id="org46e91c1">
y ↑
  |     /
  |    /
  |   /
  |  /
  | /
  |/___________→ x
</pre>

<ul class="org-ul">
<li>Da esquerda para direita: sobe</li>
<li>Quanto maior x, maior f(x)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>f(x) = 2x + 1</li>
<li>f(x) = 0,5x</li>
<li>3</li>
</ul>
</div>
</div>

<div id="outline-container-orgf2b8fd9" class="outline-5">
<h5 id="orgf2b8fd9"><span class="section-number-5">4.1.6.2.</span> Função Decrescente (a &lt; 0)</h5>
<div class="outline-text-5" id="text-4-1-6-2">
<pre class="example" id="org319eb9a">
y ↑
  |\\
  | \\
  |  \\
  |   \\
  |    \\
  |_____\\______→ x
</pre>

<ul class="org-ul">
<li>Da esquerda para direita: desce</li>
<li>Quanto maior x, menor f(x)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>f(x) = -3x + 2</li>
<li>f(x) = -x + 4</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgc01a13b" class="outline-4">
<h4 id="orgc01a13b"><span class="section-number-4">4.1.7.</span> Zero ou Raiz da Função</h4>
<div class="outline-text-4" id="text-4-1-7">
<p>
<b>Zero da função:</b> Valor de x para o qual f(x) = 0.
</p>

<p>
<b>Como encontrar:</b> f(x) = 0 ax + b = 0 ax = -b <b>x = -b/a</b>
</p>

<p>
<b>Interpretação geométrica:</b>
</p>
<ul class="org-ul">
<li>Ponto onde a reta corta o eixo x</li>
<li>Coordenadas: (-b/a, 0)</li>
</ul>

<p>
<b>Exemplo 1:</b> f(x) = 2x
</p>
<ul class="org-ul">
<li>6 0 = 2x</li>
<li>6 2x = 6 x = 3</li>
</ul>

<p>
Raiz: x = 3 (ponto (3, 0))
</p>

<p>
<b>Exemplo 2:</b> f(x) = -x + 5 0 = -x + 5 x = 5
</p>

<p>
Raiz: x = 5 (ponto (5, 0))
</p>
</div>
</div>

<div id="outline-container-org0f948d8" class="outline-4">
<h4 id="org0f948d8"><span class="section-number-4">4.1.8.</span> Estudo do Sinal da Função</h4>
<div class="outline-text-4" id="text-4-1-8">
<p>
<b>Determinar para quais valores de x:</b>
</p>
<ul class="org-ul">
<li>f(x) &gt; 0 (função positiva)</li>
<li>f(x) = 0 (função nula)</li>
<li>f(x) &lt; 0 (função negativa)</li>
</ul>

<p>
<b>Método:</b> 1. Encontrar a raiz (x = -b/a) 2. Analisar o sinal de acordo com a
</p>
</div>

<div id="outline-container-orgc074976" class="outline-5">
<h5 id="orgc074976"><span class="section-number-5">4.1.8.1.</span> Função Crescente (a &gt; 0)</h5>
<div class="outline-text-5" id="text-4-1-8-1">
<pre class="example" id="orgc8b1f38">
      ++++++++++
─────────●─────────→ x
  -------  raiz
</pre>

<ul class="org-ul">
<li>x &lt; raiz: f(x) &lt; 0 (negativo)</li>
<li>x = raiz: f(x) = 0</li>
<li>x &gt; raiz: f(x) &gt; 0 (positivo)</li>
</ul>

<p>
<b>Exemplo:</b> f(x) = 2x
</p>
<ul class="org-ul">
<li>4 Raiz: x = 2</li>

<li>x &lt; 2: f(x) &lt; 0</li>
<li>x = 2: f(x) = 0</li>
<li>x &gt; 2: f(x) &gt; 0</li>
</ul>
</div>
</div>

<div id="outline-container-org99d131d" class="outline-5">
<h5 id="org99d131d"><span class="section-number-5">4.1.8.2.</span> Função Decrescente (a &lt; 0)</h5>
<div class="outline-text-5" id="text-4-1-8-2">
<pre class="example" id="org7427450">
  -------
─────────●─────────→ x
      ++++++++++
       raiz
</pre>

<ul class="org-ul">
<li>x &lt; raiz: f(x) &gt; 0 (positivo)</li>
<li>x = raiz: f(x) = 0</li>
<li>x &gt; raiz: f(x) &lt; 0 (negativo)</li>
</ul>

<p>
<b>Exemplo:</b> f(x) = -x + 3 Raiz: x = 3
</p>

<ul class="org-ul">
<li>x &lt; 3: f(x) &gt; 0</li>
<li>x = 3: f(x) = 0</li>
<li>x &gt; 3: f(x) &lt; 0</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgdc21cbe" class="outline-4">
<h4 id="orgdc21cbe"><span class="section-number-4">4.1.9.</span> Taxa de Variação</h4>
<div class="outline-text-4" id="text-4-1-9">
<p>
<b>Taxa de variação:</b> Quanto a função varia quando x varia.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgf09109d">
a = Δy / Δx = (y₂
- y₁) / (x₂
- x₁)
</pre>

<p>
<b>Interpretação:</b>
</p>
<ul class="org-ul">
<li>a = 2: a cada 1 unidade que x aumenta, y aumenta 2</li>
<li>a = -3: a cada 1 unidade que x aumenta, y diminui 3</li>
</ul>

<p>
<b>Exemplo:</b> Dois pontos: (1, 3) e (4, 9)
</p>

<p>
a = (9
</p>
<ul class="org-ul">
<li>3) / (4</li>
<li>1) = 6 / 3 = 2</li>
</ul>

<p>
Taxa de variação: 2 (função cresce 2 unidades de y para cada unidade de x)
</p>
</div>
</div>

<div id="outline-container-org23115b3" class="outline-4">
<h4 id="org23115b3"><span class="section-number-4">4.1.10.</span> Determinando a Função Afim</h4>
<div class="outline-text-4" id="text-4-1-10">
</div>
<div id="outline-container-orgfc9f314" class="outline-5">
<h5 id="orgfc9f314"><span class="section-number-5">4.1.10.1.</span> Caso 1: Dados a e b</h5>
<div class="outline-text-5" id="text-4-1-10-1">
<p>
<b>Direto:</b> f(x) = ax + b
</p>

<p>
<b>Exemplo:</b> a = 3, b = -2 f(x) = 3x
</p>
<ul class="org-ul">
<li>2</li>
</ul>
</div>
</div>

<div id="outline-container-org69c3b16" class="outline-5">
<h5 id="org69c3b16"><span class="section-number-5">4.1.10.2.</span> Caso 2: Dados dois pontos</h5>
<div class="outline-text-5" id="text-4-1-10-2">
<p>
<b>Método:</b> 1. Calcular a: a = (y₂
</p>
<ul class="org-ul">
<li>y₁) / (x₂</li>
<li>x₁) 2. Substituir um ponto em f(x) = ax + b para encontrar b</li>
</ul>

<p>
<b>Exemplo:</b> Pontos: (1, 5) e (3, 11)
</p>

<p>
<b>Passo 1:</b> Calcular a a = (11
</p>
<ul class="org-ul">
<li>5) / (3</li>
<li>1) = 6 / 2 = 3</li>
</ul>

<p>
<b>Passo 2:</b> Encontrar b (usando ponto (1, 5)) 5 = 3(1) + b 5 = 3 + b b = 2
</p>

<p>
<b>Função:</b> f(x) = 3x + 2
</p>

<p>
<b>Verificação com o outro ponto (3, 11):</b> f(3) = 3(3) + 2 = 9 + 2 = 11 ✓
</p>
</div>
</div>

<div id="outline-container-orgf9bf949" class="outline-5">
<h5 id="orgf9bf949"><span class="section-number-5">4.1.10.3.</span> Caso 3: Dados raiz e um ponto</h5>
<div class="outline-text-5" id="text-4-1-10-3">
<p>
<b>Método:</b> 1. Raiz → f(raiz) = 0 → ponto (raiz, 0) 2. Usar dois pontos (raiz e ponto dado)
</p>

<p>
<b>Exemplo:</b> Raiz: x = 2, ponto: (0, -4)
</p>

<p>
<b>Passo 1:</b> a = (-4
</p>
<ul class="org-ul">
<li>0) / (0</li>
<li>2) = -4 / -2 = 2</li>
</ul>

<p>
<b>Passo 2:</b> Usando (0, -4) -4 = 2(0) + b b = -4
</p>

<p>
<b>Função:</b> f(x) = 2x
</p>
<ul class="org-ul">
<li>4</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org313d4a7" class="outline-4">
<h4 id="org313d4a7"><span class="section-number-4">4.1.11.</span> Interseção de Retas</h4>
<div class="outline-text-4" id="text-4-1-11">
<p>
<b>Ponto de interseção:</b> Onde duas funções têm o mesmo valor.
</p>

<p>
<b>Método:</b> Igualar as funções
</p>

<p>
f(x) = g(x)
</p>

<p>
<b>Exemplo:</b> f(x) = 2x + 1 g(x) = -x + 4
</p>

<p>
2x + 1 = -x + 4 3x = 3 x = 1
</p>

<p>
f(1) = 2(1) + 1 = 3
</p>

<p>
<b>Ponto de interseção:</b> (1, 3)
</p>
</div>
</div>

<div id="outline-container-orgc13c060" class="outline-4">
<h4 id="orgc13c060"><span class="section-number-4">4.1.12.</span> Inequações do 1º Grau</h4>
<div class="outline-text-4" id="text-4-1-12">
<p>
<b>Resolver inequações usando o estudo do sinal.</b>
</p>

<p>
<b>Exemplo 1:</b> 2x
</p>
<ul class="org-ul">
<li>4 &gt; 0</li>
</ul>

<p>
Raiz: 2x
</p>
<ul class="org-ul">
<li>4 = 0 → x = 2 a = 2 &gt; 0 (crescente)</li>
</ul>

<p>
Estudo do sinal:
</p>
<ul class="org-ul">
<li>x &lt; 2: negativo</li>
<li>x &gt; 2: positivo</li>
</ul>

<p>
<b>Solução:</b> x &gt; 2 ou (2, +∞)
</p>

<p>
<b>Exemplo 2:</b> -x + 3 ≥ 0
</p>

<p>
Raiz: x = 3 a = -1 &lt; 0 (decrescente)
</p>

<p>
Estudo do sinal:
</p>
<ul class="org-ul">
<li>x &lt; 3: positivo</li>
<li>x &gt; 3: negativo</li>
</ul>

<p>
<b>Solução:</b> x ≤ 3 ou (-∞, 3]
</p>
</div>
</div>

<div id="outline-container-org22f7dda" class="outline-4">
<h4 id="org22f7dda"><span class="section-number-4">4.1.13.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-4-1-13">
</div>
<div id="outline-container-org6eac92f" class="outline-5">
<h5 id="org6eac92f"><span class="section-number-5">4.1.13.1.</span> Exemplo 1: Conversão de Temperatura</h5>
<div class="outline-text-5" id="text-4-1-13-1">
<p>
Celsius para Fahrenheit: F = 1,8C + 32
</p>

<ul class="org-ul">
<li>C = 0°: F = 32°F</li>
<li>C = 100°: F = 212°F</li>
</ul>

<p>
<b>Pergunta:</b> Qual temperatura tem o mesmo valor em °C e °F?
</p>

<p>
C = F C = 1,8C + 32 C
</p>
<ul class="org-ul">
<li>1,8C = 32 -0,8C = 32 C = -40°C</li>
</ul>

<p>
<i>[Ver resposta 62 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1648f31" class="outline-5">
<h5 id="org1648f31"><span class="section-number-5">4.1.13.2.</span> Exemplo 2: Custo de Táxi</h5>
<div class="outline-text-5" id="text-4-1-13-2">
<p>
Bandeirada: R$ 5,00 Por km: R$ 3,00/km
</p>

<p>
<b>Função:</b> C(x) = 3x + 5
</p>

<p>
onde x = distância em km
</p>

<p>
<b>Pergunta:</b> Quanto custa uma corrida de 12 km? C(12) = 3(12) + 5 = 36 + 5 = R$ 41,00
</p>
</div>
</div>

<div id="outline-container-org1c99141" class="outline-5">
<h5 id="org1c99141"><span class="section-number-5">4.1.13.3.</span> Exemplo 3: Plano de Celular</h5>
<div class="outline-text-5" id="text-4-1-13-3">
<p>
Plano A: R$ 50 fixo + R$ 0,50/min Plano B: R$ 30 fixo + R$ 1,00/min
</p>

<p>
A(x) = 50 + 0,5x B(x) = 30 + 1,0x
</p>

<p>
<b>Pergunta:</b> A partir de quantos minutos o Plano A é mais vantajoso?
</p>

<p>
A(x) &lt; B(x) 50 + 0,5x &lt; 30 + 1,0x 50
</p>
<ul class="org-ul">
<li>30 &lt; 1,0x</li>
<li>0,5x 20 &lt; 0,5x x &gt; 40</li>
</ul>

<p>
<i>[Ver resposta 63 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org3dad648" class="outline-4">
<h4 id="org3dad648"><span class="section-number-4">4.1.14.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-1-14">
</div>
<div id="outline-container-org9db4c5e" class="outline-5">
<h5 id="org9db4c5e"><span class="section-number-5">4.1.14.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-1-14-1">
<p>
Determine a função afim f(x) = ax + b sabendo que f(2) = 5 e f(4) = 11.
</p>

<p>
<b>Solução:</b> Pontos: (2, 5) e (4, 11)
</p>

<p>
a = (11
</p>
<ul class="org-ul">
<li>5) / (4</li>
<li>2) = 6 / 2 = 3</li>
</ul>

<p>
5 = 3(2) + b 5 = 6 + b b = -1
</p>

<p>
<i>[Ver resposta 64 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org749f8f3" class="outline-5">
<h5 id="org749f8f3"><span class="section-number-5">4.1.14.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-1-14-2">
<p>
Encontre o zero da função f(x) = -2x + 8.
</p>

<p>
<b>Solução:</b> 0 = -2x + 8 2x = 8 x = 4
</p>

<p>
<i>[Ver resposta 65 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org6e3fddf" class="outline-5">
<h5 id="org6e3fddf"><span class="section-number-5">4.1.14.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-1-14-3">
<p>
Estude o sinal de f(x) = 3x
</p>
<ul class="org-ul">
<li>9.</li>
</ul>

<p>
<b>Solução:</b> Raiz: 3x
</p>
<ul class="org-ul">
<li>9 = 0 → x = 3 a = 3 &gt; 0 (crescente)</li>

<li>x &lt; 3: f(x) &lt; 0 (negativo)</li>
<li>x = 3: f(x) = 0</li>
<li>x &gt; 3: f(x) &gt; 0 (positivo)</li>
</ul>
</div>
</div>

<div id="outline-container-org6476409" class="outline-5">
<h5 id="org6476409"><span class="section-number-5">4.1.14.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-1-14-4">
<p>
Determine o ponto de interseção das retas f(x) = 2x
</p>
<ul class="org-ul">
<li>1 e g(x) = -x + 5.</li>
</ul>

<p>
<b>Solução:</b> 2x
</p>
<ul class="org-ul">
<li>1 = -x + 5 3x = 6 x = 2</li>
</ul>

<p>
y = 2(2)
</p>
<ul class="org-ul">
<li>1 = 3</li>
</ul>

<p>
<i>[Ver resposta 66 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org846717c" class="outline-5">
<h5 id="org846717c"><span class="section-number-5">4.1.14.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-4-1-14-5">
<p>
Resolva a inequação: 4x
</p>
<ul class="org-ul">
<li>8 ≤ 0</li>
</ul>

<p>
<b>Solução:</b> Raiz: 4x = 8 → x = 2 a = 4 &gt; 0 (crescente)
</p>

<p>
f(x) ≤ 0 → região negativa ou zero
</p>

<p>
<i>[Ver resposta 67 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org38e8c1f" class="outline-4">
<h4 id="org38e8c1f"><span class="section-number-4">4.1.15.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-1-15">
<ol class="org-ol">
<li><b>Gráfico é sempre reta</b> (função do 1º grau)</li>
<li><b>a &gt; 0:</b> crescente; <b>a &lt; 0:</b> decrescente</li>
<li><b>Raiz:</b> x = -b/a (onde corta eixo x)</li>
<li><b>b:</b> onde corta eixo y (quando x = 0)</li>
<li><b>Dois pontos determinam uma reta</b> (e a função)</li>
<li><b>Estudo do sinal:</b> use a raiz + crescente/decrescente</li>
<li><b>Inequação:</b> estudo do sinal da função</li>
<li><b>Interseção:</b> igualar as funções</li>
</ol>
</div>
</div>

<div id="outline-container-org8358171" class="outline-4">
<h4 id="org8358171"><span class="section-number-4">4.1.16.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-1-16">
<p>
<b>Função Afim:</b>
</p>
<ul class="org-ul">
<li>f(x) = ax + b (a ≠ 0)</li>
<li>Gráfico: reta</li>
<li>a: coeficiente angular (taxa de variação)</li>
<li>b: coeficiente linear (intercepto em y)</li>
</ul>

<p>
<b>Comportamento:</b>
</p>
<ul class="org-ul">
<li>a &gt; 0: crescente</li>
<li>a &lt; 0: decrescente</li>
<li>|a| maior: mais inclinada</li>
</ul>

<p>
<b>Zero/Raiz:</b>
</p>
<ul class="org-ul">
<li>x = -b/a</li>
<li>Ponto (−b/a, 0)</li>
</ul>

<p>
<b>Estudo do sinal:</b>
</p>
<ul class="org-ul">
<li>Crescente: − 0 +</li>
<li>Decrescente: + 0 −</li>
</ul>
</div>
</div>

<div id="outline-container-org3e07b1b" class="outline-4">
<h4 id="org3e07b1b"><span class="section-number-4">4.1.17.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-1-17">
<pre class="example" id="org4835d2c">
Função Afim:
f(x) = ax + b (a ≠ 0)

Coeficiente angular:
a = Δy/Δx = (y₂
- y₁)/(x₂
- x₁)

Zero da função:
f(x) = 0
x = -b/a

Casos especiais:
Função linear: f(x) = ax (b = 0)
Função identidade: f(x) = x (a = 1, b = 0)
Função constante: f(x) = b (a = 0)

Ponto de interseção:
f(x) = g(x)
</pre>
</div>
</div>

<div id="outline-container-orgd80495f" class="outline-4">
<h4 id="orgd80495f"><span class="section-number-4">4.1.18.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-1-18">
<pre class="example" id="orgff54140">
┌─────────────┬──────────────┬──────────────┐
│  Sinal de a │   Gráfico    │ Comportamento│
├─────────────┼──────────────┼──────────────┤
│   a &gt; 0     │      /       │  Crescente   │
│   a &lt; 0     │      \\       │  Decrescente │
└─────────────┴──────────────┴──────────────┘

┌──────────────┬─────────────────────────────┐
│  Coeficiente │        Significado          │
├──────────────┼─────────────────────────────┤
│      a       │ Taxa de variação/Inclinação │
│      b       │ Valor inicial (x=0)         │
│    -b/a      │ Raiz/Zero da função         │
└──────────────┴─────────────────────────────┘
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para todas as funções)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org8457463" class="outline-3">`;

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
