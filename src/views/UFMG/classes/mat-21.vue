<script setup lang="ts">
import { ref } from "vue";

const code = "mat-21";
const title = "Matemática: Função Afim";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-1">
<ul class="org-ul">
<li>Matemática: Função Afim</li>
<li>Parte 2</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-org3f5f220" class="outline-4">
<h4 id="org3f5f220"><span class="section-number-4">5.1.1.</span> Revisão: Função Afim</h4>
<div class="outline-text-4" id="text-5-1-1">
<p>
Na Aula 16, estudamos os conceitos básicos da função afim:
</p>
<ul class="org-ul">
<li>f(x) = ax + b (a ≠ 0)</li>
<li>Coeficientes a (angular) e b (linear)</li>
<li>Gráfico: reta</li>
<li>Zero, crescimento/decrescimento, estudo do sinal</li>
</ul>

<p>
<b>Nesta aula, aprofundaremos:</b>
</p>
<ul class="org-ul">
<li>Posição relativa entre retas</li>
<li>Sistemas de equações via funções</li>
<li>Aplicações e problemas contextualizados</li>
<li>Função modular</li>
<li>Inequações mais complexas</li>
</ul>
</div>
</div>

<div id="outline-container-org5dcdb94" class="outline-4">
<h4 id="org5dcdb94"><span class="section-number-4">5.1.2.</span> Posição Relativa entre Duas Retas</h4>
<div class="outline-text-4" id="text-5-1-2">
<p>
Dadas duas funções afins f(x) = a₁x + b₁ e g(x) = a₂x + b₂:
</p>
</div>

<div id="outline-container-org5242aca" class="outline-5">
<h5 id="org5242aca"><span class="section-number-5">5.1.2.1.</span> 1. Retas Concorrentes</h5>
<div class="outline-text-5" id="text-5-1-2-1">
<p>
Retas que se cruzam em um único ponto.
</p>

<p>
<b>Condição:</b>
</p>

<pre class="example" id="org9882ed1">
a₁ ≠ a₂  (coeficientes angulares diferentes)
</pre>

<p>
<b>Ponto de interseção:</b> Resolver f(x) = g(x)
</p>

<p>
<b>Exemplo:</b> f(x) = 2x + 1 g(x) = -x + 4
</p>

<p>
2x + 1 = -x + 4 3x = 3 x = 1 → y = 3
</p>

<p>
Ponto de interseção: (1, 3)
</p>
</div>
</div>

<div id="outline-container-org939d57c" class="outline-5">
<h5 id="org939d57c"><span class="section-number-5">5.1.2.2.</span> 2. Retas Paralelas</h5>
<div class="outline-text-5" id="text-5-1-2-2">
<p>
Retas que não se cruzam (mesma inclinação, posições diferentes).
</p>

<p>
<b>Condição:</b>
</p>

<pre class="example" id="org3d4fce4">
a₁ = a₂  e  b₁ ≠ b₂
</pre>

<p>
<b>Exemplo:</b> f(x) = 3x + 2 g(x) = 3x
</p>
<ul class="org-ul">
<li>5</li>
</ul>

<p>
Ambas têm a = 3, mas b diferentes → paralelas
</p>
</div>
</div>

<div id="outline-container-orgcf4caa4" class="outline-5">
<h5 id="orgcf4caa4"><span class="section-number-5">5.1.2.3.</span> 3. Retas Coincidentes</h5>
<div class="outline-text-5" id="text-5-1-2-3">
<p>
Mesma reta (todos os pontos em comum).
</p>

<p>
<b>Condição:</b>
</p>

<pre class="example" id="org2d41e66">
a₁ = a₂  e  b₁ = b₂
</pre>

<p>
<b>Exemplo:</b> f(x) = 2x + 3 g(x) = 2x + 3
</p>

<p>
São a mesma função → retas coincidentes
</p>
</div>
</div>

<div id="outline-container-org2fb2c09" class="outline-5">
<h5 id="org2fb2c09"><span class="section-number-5">5.1.2.4.</span> 4. Retas Perpendiculares</h5>
<div class="outline-text-5" id="text-5-1-2-4">
<p>
Retas que se cruzam formando ângulo de 90°.
</p>

<p>
<b>Condição:</b>
</p>

<pre class="example" id="orgb0d42df">
a₁ × a₂ = -1
</pre>

<p>
Ou: a₂ = -1/a₁ (coeficientes são inversos opostos)
</p>

<p>
<b>Exemplo:</b> f(x) = 2x + 1 g(x) = -½x + 3
</p>

<p>
a₁ = 2, a₂ = -½ 2 × (-½) = -1 ✓
</p>

<p>
São perpendiculares.
</p>
</div>
</div>
</div>

<div id="outline-container-org3a9061e" class="outline-4">
<h4 id="org3a9061e"><span class="section-number-4">5.1.3.</span> Sistemas de Equações do 1º Grau</h4>
<div class="outline-text-4" id="text-5-1-3">
<p>
Resolver sistemas é encontrar o ponto de interseção entre duas retas.
</p>

<p>
<b>Sistema:</b>
</p>

<pre class="example" id="org2b39ab0">
{ ax + by = c
{ dx + ey = f
</pre>

<p>
<b>Métodos:</b>
</p>
</div>

<div id="outline-container-org25f18dd" class="outline-5">
<h5 id="org25f18dd"><span class="section-number-5">5.1.3.1.</span> Método da Substituição</h5>
<div class="outline-text-5" id="text-5-1-3-1">
<ol class="org-ol">
<li>Isolar uma variável em uma equação</li>
<li>Substituir na outra equação</li>
<li>Resolver e voltar para encontrar a segunda variável</li>
</ol>
</div>
</div>

<div id="outline-container-org1e77b4a" class="outline-5">
<h5 id="org1e77b4a"><span class="section-number-5">5.1.3.2.</span> Método da Adição</h5>
<div class="outline-text-5" id="text-5-1-3-2">
<ol class="org-ol">
<li>Multiplicar equações para anular uma variável</li>
<li>Somar as equações</li>
<li>Resolver para a variável restante</li>
<li>Substituir para encontrar a outra</li>
</ol>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgcce3f3b">
{ 2x + y = 7
{ x
- y = 2
</pre>

<p>
<b>Por adição:</b> Somando as equações: (2x + y) + (x
</p>
<ul class="org-ul">
<li>y) = 7 + 2 3x = 9 x = 3</li>
</ul>

<p>
Substituindo em x
</p>
<ul class="org-ul">
<li>y = 2: 3</li>
<li>y = 2 y = 1</li>
</ul>

<p>
<b>Solução:</b> (3, 1)
</p>

<p>
<b>Interpretação geométrica:</b>
</p>
<ul class="org-ul">
<li><b>Uma solução:</b> retas concorrentes</li>
<li><b>Infinitas soluções:</b> retas coincidentes</li>
<li><b>Nenhuma solução:</b> retas paralelas</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgfe38cbb" class="outline-4">
<h4 id="orgfe38cbb"><span class="section-number-4">5.1.4.</span> Função Definida por Mais de uma Sentença</h4>
<div class="outline-text-4" id="text-5-1-4">
<p>
Funções que têm expressões diferentes em intervalos diferentes.
</p>

<p>
<b>Formato:</b>
</p>

<pre class="example" id="org8cfd40d">
       ⎧ expressão 1, se condição 1
f(x) = ⎨ expressão 2, se condição 2
       ⎩ expressão 3, se condição 3
</pre>

<p>
<b>Exemplo 1:</b>
</p>

<pre class="example" id="org335b27c">
       ⎧ 2x + 1,  se x ≤ 0
f(x) = ⎨
       ⎩ -x + 3,  se x &gt; 0
</pre>

<p>
Para calcular f(-2): usa a primeira sentença (x ≤ 0) f(-2) = 2(-2) + 1 = -4 + 1 = -3
</p>

<p>
Para calcular f(3): usa a segunda sentença (x &gt; 0) f(3) = -3 + 3 = 0
</p>

<p>
<b>Gráfico:</b> combina duas semi-retas
</p>

<p>
*Exemplo 2
</p>
<ul class="org-ul">
<li>Tarifa progressiva:*</li>
</ul>

<pre class="example" id="orgc6b90e1">
        ⎧ 5x,       se 0 ≤ x ≤ 100
Custo = ⎨
        ⎩ 500 + 3(x-100),  se x &gt; 100
</pre>

<p>
Até 100 unidades: R$ 5 por unidade Acima de 100: R$ 500 fixo + R$ 3 por unidade excedente
</p>
</div>
</div>

<div id="outline-container-orge3305da" class="outline-4">
<h4 id="orge3305da"><span class="section-number-4">5.1.5.</span> Função Modular</h4>
<div class="outline-text-4" id="text-5-1-5">
<p>
<b>Módulo (ou valor absoluto)</b> de um número é sua distância até o zero.
</p>

<p>
<b>Notação:</b> |x|
</p>

<p>
<b>Definição:</b>
</p>

<pre class="example" id="orgebbf268">
       ⎧  x,   se x ≥ 0
|x| =  ⎨
       ⎩ -x,   se x &lt; 0
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>|5| = 5</li>
<li>|-3| = 3</li>
<li>|0| = 0</li>
</ul>

<p>
<b>Propriedades:</b> 1. |x| ≥ 0 (sempre não-negativo) 2. |x| = |-x| 3. |x · y| = |x| · |y| 4. |x/y| = |x|/|y| (y ≠ 0) 5. |x + y| ≤ |x| + |y| (desigualdade triangular)
</p>

<p>
<b>Função Modular:</b> f(x) = |x|
</p>

<p>
<b>Gráfico:</b> forma de “V”
</p>
<ul class="org-ul">
<li>Para x ≥ 0: f(x) = x (reta crescente)</li>
<li>Para x &lt; 0: f(x) = -x (reta decrescente)</li>
</ul>

<pre class="example" id="org0196b07">
    |
  3 |    /
  2 |   /|
  1 |  / |
    | /  |
----+----+----
 -2 |    2
</pre>

<p>
<b>Equações com módulo:</b>
</p>

<p>
<b>Exemplo:</b> |x
</p>
<ul class="org-ul">
<li>2| = 5</li>
</ul>

<p>
<b>Método:</b> módulo = distância x
</p>
<ul class="org-ul">
<li>2 = 5 ou x</li>
<li>2 = -5 x = 7 ou x = -3</li>
</ul>

<p>
<b>Soluções:</b> x = 7 ou x = -3
</p>

<p>
<b>Inequações com módulo:</b>
</p>

<p>
<b>Exemplo:</b> |x| &lt; 3
</p>

<p>
Significa: distância de x até 0 é menor que 3
</p>

<p>
<b>Solução:</b> -3 &lt; x &lt; 3
</p>

<p>
<b>Regra geral:</b>
</p>
<ul class="org-ul">
<li>|x| &lt; a → -a &lt; x &lt; a</li>
<li>|x| &gt; a → x &lt; -a ou x &gt; a</li>
</ul>
</div>
</div>

<div id="outline-container-org0091aee" class="outline-4">
<h4 id="org0091aee"><span class="section-number-4">5.1.6.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-5-1-6">
</div>
<div id="outline-container-orgedb3ec8" class="outline-5">
<h5 id="orgedb3ec8"><span class="section-number-5">5.1.6.1.</span> Problema 1: Táxi</h5>
<div class="outline-text-5" id="text-5-1-6-1">
<p>
Um táxi cobra R$ 5,00 de bandeirada + R$ 2,50 por km rodado.
</p>

<p>
<b>Função:</b> C(x) = 5 + 2,5x
</p>

<p>
<b>a) Quanto custa uma corrida de 12 km?</b> C(12) = 5 + 2,5(12) = 5 + 30 = R$ 35,00
</p>

<p>
<b>b) Quantos km podem ser rodados com R$ 30?</b> 30 = 5 + 2,5x 25 = 2,5x x = 10 km
</p>
</div>
</div>

<div id="outline-container-org3ee2f68" class="outline-5">
<h5 id="org3ee2f68"><span class="section-number-5">5.1.6.2.</span> Problema 2: Planos de Celular</h5>
<div class="outline-text-5" id="text-5-1-6-2">
<ul class="org-ul">
<li><b>Plano A:</b> R$ 50 fixos + R$ 0,50 por minuto</li>
<li><b>Plano B:</b> R$ 80 fixos + R$ 0,20 por minuto</li>
</ul>

<p>
<b>Funções:</b> A(x) = 50 + 0,5x B(x) = 80 + 0,2x
</p>

<p>
<b>Quando os planos custam o mesmo?</b> 50 + 0,5x = 80 + 0,2x 0,3x = 30 x = 100 minutos
</p>

<p>
<b>Interpretação:</b>
</p>
<ul class="org-ul">
<li>Menos de 100 min: Plano A é melhor</li>
<li>Mais de 100 min: Plano B é melhor</li>
<li>Exatamente 100 min: custam o mesmo</li>
</ul>
</div>
</div>

<div id="outline-container-org5143843" class="outline-5">
<h5 id="org5143843"><span class="section-number-5">5.1.6.3.</span> Problema 3: Conversão Temperatura</h5>
<div class="outline-text-5" id="text-5-1-6-3">
<p>
Converter Celsius (C) para Fahrenheit (F):
</p>

<p>
F = (9/5)C + 32
</p>

<p>
<b>a) 25°C em Fahrenheit:</b> F = (9/5)(25) + 32 = 45 + 32 = 77°F
</p>

<p>
<b>b) A que temperatura as escalas têm o mesmo valor?</b> C = F C = (9/5)C + 32 C
</p>
<ul class="org-ul">
<li>(9/5)C = 32 (-4/5)C = 32 C = -40°C = -40°F</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orga57e17e" class="outline-4">
<h4 id="orga57e17e"><span class="section-number-4">5.1.7.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-1-7">
</div>
<div id="outline-container-org0df118f" class="outline-5">
<h5 id="org0df118f"><span class="section-number-5">5.1.7.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-1-7-1">
<p>
Determine a posição relativa entre: f(x) = 3x
</p>
<ul class="org-ul">
<li>2 e g(x) = -x + 6</li>
</ul>

<p>
<b>Solução:</b> a₁ = 3, a₂ = -1 a₁ ≠ a₂ → <b>retas concorrentes</b>
</p>

<p>
Ponto de interseção: 3x
</p>
<ul class="org-ul">
<li>2 = -x + 6 4x = 8 x = 2 → y = 3(2)</li>
<li>2 = 4</li>
</ul>

<p>
<i>[Ver resposta 80 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org03fd404" class="outline-5">
<h5 id="org03fd404"><span class="section-number-5">5.1.7.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-1-7-2">
<p>
Resolva o sistema:
</p>

<pre class="example" id="org409ccf1">
{ 3x + 2y = 12
{ x
- y = 1
</pre>

<p>
<b>Solução (por substituição):</b> Da 2ª equação: x = y + 1
</p>

<p>
Substituindo na 1ª: 3(y + 1) + 2y = 12 3y + 3 + 2y = 12 5y = 9 y = 9/5
</p>

<p>
x = 9/5 + 1 = 14/5
</p>

<p>
<i>[Ver resposta 81 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgd74af78" class="outline-5">
<h5 id="orgd74af78"><span class="section-number-5">5.1.7.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-1-7-3">
<p>
Calcule f(-3) e f(2) para:
</p>

<pre class="example" id="orgc201e8b">
       ⎧ x + 5,   se x &lt; 0
f(x) = ⎨
       ⎩ 2x
- 1,  se x ≥ 0
</pre>

<p>
<b>Solução:</b>
</p>

<p>
f(-3): usa x + 5 (pois -3 &lt; 0) f(-3) = -3 + 5 = 2
</p>

<p>
f(2): usa 2x
</p>
<ul class="org-ul">
<li>1 (pois 2 ≥ 0) f(2) = 2(2)</li>
<li>1 = 3</li>
</ul>

<p>
<i>[Ver resposta 82 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3281ac0" class="outline-5">
<h5 id="org3281ac0"><span class="section-number-5">5.1.7.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-1-7-4">
<p>
Resolva: |2x
</p>
<ul class="org-ul">
<li>4| = 6</li>
</ul>

<p>
<b>Solução:</b> 2x
</p>
<ul class="org-ul">
<li>4 = 6 ou 2x</li>
<li>4 = -6 2x = 10 ou 2x = -2 x = 5 ou x = -1</li>
</ul>

<p>
<i>[Ver resposta 83 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org4f7f8f6" class="outline-5">
<h5 id="org4f7f8f6"><span class="section-number-5">5.1.7.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-1-7-5">
<p>
Resolva a inequação: |x + 1| &lt; 4
</p>

<p>
<b>Solução:</b> -4 &lt; x + 1 &lt; 4 -4
</p>
<ul class="org-ul">
<li>1 &lt; x &lt; 4</li>
<li>1 -5 &lt; x &lt; 3</li>
</ul>

<p>
<i>[Ver resposta 84 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org9d0f1fd" class="outline-4">
<h4 id="org9d0f1fd"><span class="section-number-4">5.1.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-1-8">
<ol class="org-ol">
<li><b>Posição de retas:</b> compare os coeficientes a</li>
<li><b>Perpendiculares:</b> a₁ × a₂ = -1</li>
<li><b>Sistema:</b> ponto de interseção entre retas</li>
<li><b>Função por partes:</b> veja qual condição o x satisfaz</li>
<li><b>Módulo |x| = a:</b> duas soluções (x = a ou x = -a)</li>
<li><b>|x| &lt; a:</b> -a &lt; x &lt; a (intervalo)</li>
<li><b>|x| &gt; a:</b> x &lt; -a ou x &gt; a (união de intervalos)</li>
<li><b>Problemas:</b> monte a função conforme o enunciado</li>
</ol>
</div>
</div>

<div id="outline-container-org1c8fce8" class="outline-4">
<h4 id="org1c8fce8"><span class="section-number-4">5.1.9.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-1-9">
<p>
<b>Posição Relativa:</b>
</p>
<ul class="org-ul">
<li>Concorrentes: a₁ ≠ a₂</li>
<li>Paralelas: a₁ = a₂, b₁ ≠ b₂</li>
<li>Coincidentes: a₁ = a₂, b₁ = b₂</li>
<li>Perpendiculares: a₁ × a₂ = -1</li>
</ul>

<p>
<b>Módulo:</b>
</p>
<ul class="org-ul">
<li>|x| = distância até zero</li>
<li>Sempre ≥ 0</li>
<li>|x| = { x se x≥0; -x se x&lt;0 }</li>
</ul>

<p>
<b>Funções por partes:</b>
</p>
<ul class="org-ul">
<li>Verificar a condição de x</li>
<li>Usar a expressão correspondente</li>
</ul>
</div>
</div>

<div id="outline-container-org78ca7cb" class="outline-4">
<h4 id="org78ca7cb"><span class="section-number-4">5.1.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-5-1-10">
<pre class="example" id="org453b7cd">
Posição Relativa de Retas:
f(x) = a₁x + b₁
g(x) = a₂x + b₂

Concorrentes: a₁ ≠ a₂
Paralelas: a₁ = a₂ e b₁ ≠ b₂
Coincidentes: a₁ = a₂ e b₁ = b₂
Perpendiculares: a₁ × a₂ = -1

Módulo:
       ⎧  x,   se x ≥ 0
|x| =  ⎨
       ⎩ -x,   se x &lt; 0

Equação: |x| = a → x = a ou x = -a

Inequações:
|x| &lt; a  →  -a &lt; x &lt; a
|x| &gt; a  →  x &lt; -a ou x &gt; a

Função Modular:
f(x) = |x|
Gráfico: forma de V
</pre>
</div>
</div>

<div id="outline-container-org711c467" class="outline-4">
<h4 id="org711c467"><span class="section-number-4">5.1.11.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-1-11">
<pre class="example" id="org9970706">
Posição de Retas:

Concorrentes:     Paralelas:    Perpendiculares:
    \\  /            |  |            |
     \\/             |  |           ―┼―
     /\\             |  |            |
    /  \\            |  |

(a₁≠a₂)      (a₁=a₂,b₁≠b₂)   (a₁×a₂=-1)

Função Modular f(x) = |x|:
      |
    2 |  /\\
    1 | /  \\
      |/    \\
   ───┼──────
   -2 |  1  2

Inequações com Módulo:
|x| &lt; 3:  ←─────●═══●─────→
               -3   3
               (intervalo)

|x| &gt; 3:  ●═══════←   →═══════●
          -3                  3
          (união)
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>aprofundamento de função afim)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org7b2c4ce" class="outline-3">`;

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
