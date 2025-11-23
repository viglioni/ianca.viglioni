<script setup lang="ts">
import { ref } from "vue";

const code = "mat-6";
const title = "Matemática: Razão, Proporção e Proporcionalidade";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-1">
<ul class="org-ul">
<li>Matemática: Razão, Proporção e Proporcionalidade</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org67f0434" class="outline-4">
<h4 id="org67f0434"><span class="section-number-4">2.1.1.</span> O que é Razão?</h4>
<div class="outline-text-4" id="text-2-1-1">
<p>
<b>Definição:</b> Razão é a comparação entre duas grandezas por meio de uma divisão.
</p>

<p>
<b>Notação:</b>
</p>
<ul class="org-ul">
<li>Razão entre a e b: a/b ou a:b (lê-se “a está para b”)</li>
<li>a é o <b>antecedente</b></li>
<li>b é o <b>consequente</b> (b ≠ 0)</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
</div>

<div id="outline-container-org4684573" class="outline-5">
<h5 id="org4684573"><span class="section-number-5">2.1.1.1.</span> Exemplo 1</h5>
<div class="outline-text-5" id="text-2-1-1-1">
<p>
Em uma turma há 15 meninos e 10 meninas. Qual a razão entre meninos e meninas?
</p>

<p>
<b>Solução:</b> Razão = 15/10 = 3/2 (simplificando)
</p>

<p>
<b>Interpretação:</b> Para cada 3 meninos, há 2 meninas.
</p>
</div>
</div>

<div id="outline-container-org740788f" class="outline-5">
<h5 id="org740788f"><span class="section-number-5">2.1.1.2.</span> Exemplo 2</h5>
<div class="outline-text-5" id="text-2-1-1-2">
<p>
Um carro percorre 300 km em 4 horas. Qual a razão entre distância e tempo?
</p>

<p>
<b>Solução:</b> Razão = 300/4 = 75 km/h
</p>

<p>
<b>Interpretação:</b> A cada hora, o carro percorre 75 km (velocidade média).
</p>
</div>
</div>
</div>

<div id="outline-container-org3771dbf" class="outline-4">
<h4 id="org3771dbf"><span class="section-number-4">2.1.2.</span> Tipos Especiais de Razão</h4>
<div class="outline-text-4" id="text-2-1-2">
</div>
<div id="outline-container-org5b95ff0" class="outline-5">
<h5 id="org5b95ff0"><span class="section-number-5">2.1.2.1.</span> Escala</h5>
<div class="outline-text-5" id="text-2-1-2-1">
<p>
Razão entre a medida no desenho e a medida real.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org3d7eeac">
Escala = medida no desenho / medida real
</pre>

<p>
<b>Exemplo:</b> Em um mapa com escala 1:1.000.000, significa que 1 cm no mapa representa 1.000.000 cm (10 km) na realidade.
</p>

<ul class="org-ul">
<li>1:100 → 1 cm no desenho = 100 cm real = 1 m real</li>
<li>1:50.000 → 1 cm no mapa = 50.000 cm = 500 m = 0,5 km</li>
</ul>
</div>
</div>

<div id="outline-container-org11e5357" class="outline-5">
<h5 id="org11e5357"><span class="section-number-5">2.1.2.2.</span> Velocidade Média</h5>
<div class="outline-text-5" id="text-2-1-2-2">
<p>
Razão entre distância percorrida e tempo gasto.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org2864668">
v = d / t
</pre>

<p>
<b>Exemplo:</b> Um atleta corre 10 km em 50 minutos. v = 10 km / 50 min = 0,2 km/min = 12 km/h
</p>
</div>
</div>

<div id="outline-container-org8e9d768" class="outline-5">
<h5 id="org8e9d768"><span class="section-number-5">2.1.2.3.</span> Densidade Demográfica</h5>
<div class="outline-text-5" id="text-2-1-2-3">
<p>
Razão entre população e área.
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgc442af6">
d = população / área
</pre>

<p>
<b>Exemplo:</b> Um município com 50.000 habitantes e área de 250 km². d = 50.000 / 250 = 200 hab/km²
</p>
</div>
</div>
</div>

<div id="outline-container-orgf670652" class="outline-4">
<h4 id="orgf670652"><span class="section-number-4">2.1.3.</span> O que é Proporção?</h4>
<div class="outline-text-4" id="text-2-1-3">
<p>
<b>Definição:</b> Proporção é uma igualdade entre duas razões.
</p>

<p>
<b>Notação:</b>
</p>

<pre class="example" id="org3240196">
a/b = c/d  ou  a:b = c:d
</pre>

<p>
<b>Lê-se:</b> “a está para b assim como c está para d”
</p>

<p>
<b>Termos da proporção:</b>
</p>

<pre class="example" id="org4d91058">
a/b = c/d

a e d → extremos
b e c → meios
</pre>
</div>
</div>

<div id="outline-container-org3f50e60" class="outline-4">
<h4 id="org3f50e60"><span class="section-number-4">2.1.4.</span> Propriedade Fundamental das Proporções</h4>
<div class="outline-text-4" id="text-2-1-4">
<p>
<b>Em toda proporção, o produto dos meios é igual ao produto dos extremos.</b>
</p>

<pre class="example" id="org079f8be">
Se a/b = c/d, então a × d = b × c
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org2548cf4">
2/3 = 4/6

Verificação:
2 × 6 = 12 (produto dos extremos)
3 × 4 = 12 (produto dos meios)
12 = 12 ✓
</pre>

<p>
<b>Aplicação:</b> Essa propriedade é usada para encontrar um termo desconhecido.
</p>
</div>

<div id="outline-container-orgc5cc9f5" class="outline-5">
<h5 id="orgc5cc9f5"><span class="section-number-5">2.1.4.1.</span> Exemplo 1</h5>
<div class="outline-text-5" id="text-2-1-4-1">
<p>
Determine x na proporção: 3/5 = x/15
</p>

<p>
<b>Solução:</b> 3 × 15 = 5 × x 45 = 5x x = 45/5 x = 9
</p>
</div>
</div>

<div id="outline-container-org3316d2d" class="outline-5">
<h5 id="org3316d2d"><span class="section-number-5">2.1.4.2.</span> Exemplo 2</h5>
<div class="outline-text-5" id="text-2-1-4-2">
<p>
Determine x na proporção: 8/x = 2/7
</p>

<p>
<b>Solução:</b> 8 × 7 = x × 2 56 = 2x x = 56/2 x = 28
</p>
</div>
</div>
</div>

<div id="outline-container-orgc4c9911" class="outline-4">
<h4 id="orgc4c9911"><span class="section-number-4">2.1.5.</span> Outras Propriedades das Proporções</h4>
<div class="outline-text-4" id="text-2-1-5">
</div>
<div id="outline-container-org6f1e44b" class="outline-5">
<h5 id="org6f1e44b"><span class="section-number-5">2.1.5.1.</span> 1. Soma dos Antecedentes e Consequentes</h5>
<div class="outline-text-5" id="text-2-1-5-1">
<pre class="example" id="org3aa17c2">
Se a/b = c/d, então:

(a + c)/(b + d) = a/b = c/d
</pre>

<p>
<b>Exemplo:</b> Se 2/3 = 4/6, então (2+4)/(3+6) = 6/9 = 2/3 ✓
</p>
</div>
</div>

<div id="outline-container-orgbf76af7" class="outline-5">
<h5 id="orgbf76af7"><span class="section-number-5">2.1.5.2.</span> 2. Diferença dos Antecedentes e Consequentes</h5>
<div class="outline-text-5" id="text-2-1-5-2">
<pre class="example" id="org974ce46">
Se a/b = c/d, então:

(a
- c)/(b
- d) = a/b = c/d
</pre>
</div>
</div>

<div id="outline-container-org1a6c244" class="outline-5">
<h5 id="org1a6c244"><span class="section-number-5">2.1.5.3.</span> 3. Inverter os Termos</h5>
<div class="outline-text-5" id="text-2-1-5-3">
<pre class="example" id="org7c7525b">
Se a/b = c/d, então b/a = d/c
</pre>
</div>
</div>
</div>

<div id="outline-container-org417fb52" class="outline-4">
<h4 id="org417fb52"><span class="section-number-4">2.1.6.</span> Grandezas Proporcionais</h4>
<div class="outline-text-4" id="text-2-1-6">
</div>
<div id="outline-container-org9478999" class="outline-5">
<h5 id="org9478999"><span class="section-number-5">2.1.6.1.</span> Grandezas Diretamente Proporcionais</h5>
<div class="outline-text-5" id="text-2-1-6-1">
<p>
<b>Definição:</b> Duas grandezas são diretamente proporcionais quando, ao aumentar uma, a outra aumenta na mesma proporção (e vice-versa).
</p>

<p>
<b>Característica:</b> A razão entre valores correspondentes é constante (k).
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Quantidade de combustível e preço pago</li>
<li>Tempo de trabalho e salário</li>
<li>Velocidade constante: distância e tempo</li>
</ul>
</div>
</div>

<div id="outline-container-org74f2b08" class="outline-5">
<h5 id="org74f2b08"><span class="section-number-5">2.1.6.2.</span> Exemplo Prático</h5>
<div class="outline-text-5" id="text-2-1-6-2">
<p>
Se 2 kg de carne custam R$ 40, quanto custarão 5 kg?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org5785834">
2 kg ——— R$ 40
5 kg ——— x

2/5 = 40/x  (proporção)
2x = 5 × 40
2x = 200
x = 100
</pre>

<p>
<i>[Ver resposta 25 no final do documento]</i>
</p>

<p>
<b>Verificação:</b> A razão preço/quantidade é constante:
</p>
<ul class="org-ul">
<li>40/2 = 20 reais/kg</li>
<li>100/5 = 20 reais/kg ✓</li>
</ul>
</div>
</div>

<div id="outline-container-org58e4f3e" class="outline-5">
<h5 id="org58e4f3e"><span class="section-number-5">2.1.6.3.</span> Grandezas Inversamente Proporcionais</h5>
<div class="outline-text-5" id="text-2-1-6-3">
<p>
<b>Definição:</b> Duas grandezas são inversamente proporcionais quando, ao aumentar uma, a outra diminui na mesma proporção (e vice-versa).
</p>

<p>
<b>Característica:</b> O produto entre valores correspondentes é constante (k).
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Velocidade e tempo (para mesma distância)</li>
<li>Número de operários e tempo para completar obra</li>
<li>Número de torneiras e tempo para encher tanque</li>
</ul>
</div>
</div>

<div id="outline-container-orgda70521" class="outline-5">
<h5 id="orgda70521"><span class="section-number-5">2.1.6.4.</span> Exemplo Prático</h5>
<div class="outline-text-5" id="text-2-1-6-4">
<p>
Se 3 operários fazem uma obra em 12 dias, quantos dias levarão 6 operários?
</p>

<p>
<b>Solução:</b> Mais operários → menos dias (inversamente proporcionais)
</p>

<pre class="example" id="org71d1ef0">
3 operários ——— 12 dias
6 operários ——— x dias

3 × 12 = 6 × x (produto constante)
36 = 6x
x = 6
</pre>

<p>
<i>[Ver resposta 26 no final do documento]</i>
</p>

<p>
<b>Verificação:</b> O produto é constante:
</p>
<ul class="org-ul">
<li>3 × 12 = 36</li>
<li>6 × 6 = 36 ✓</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org72a23bf" class="outline-4">
<h4 id="org72a23bf"><span class="section-number-4">2.1.7.</span> Divisão em Partes Proporcionais</h4>
<div class="outline-text-4" id="text-2-1-7">
</div>
<div id="outline-container-org65663e6" class="outline-5">
<h5 id="org65663e6"><span class="section-number-5">2.1.7.1.</span> Divisão Diretamente Proporcional</h5>
<div class="outline-text-5" id="text-2-1-7-1">
<p>
Dividir um número em partes diretamente proporcionais a outros números.
</p>

<p>
<b>Método:</b> 1. Somar os números proporcionais 2. Dividir o total pela soma 3. Multiplicar o resultado por cada número
</p>

<p>
<b>Exemplo 1:</b> Dividir 120 em partes diretamente proporcionais a 2, 3 e 5.
</p>

<p>
<b>Solução:</b> 1. Soma: 2 + 3 + 5 = 10 2. Constante: 120 / 10 = 12 3. Partes:
</p>
<ul class="org-ul">
<li>1ª parte: 2 × 12 = 24</li>
<li>2ª parte: 3 × 12 = 36</li>
<li>3ª parte: 5 × 12 = 60</li>
</ul>

<p>
<b>Verificação:</b> 24 + 36 + 60 = 120 ✓
</p>

<p>
<b>Exemplo 2 (Prático):</b> Três sócios investiram R$ 10.000, R$ 15.000 e R$ 25.000 em um negócio. O lucro foi de R$ 30.000. Como dividir proporcionalmente ao investimento?
</p>

<p>
<b>Solução:</b> Investimentos: 10, 15, 25 (em milhares) Soma: 10 + 15 + 25 = 50 Constante: 30.000 / 50 = 600
</p>

<p>
Partes:
</p>
<ul class="org-ul">
<li>Sócio 1: 10 × 600 = R$ 6.000</li>
<li>Sócio 2: 15 × 600 = R$ 9.000</li>
<li>Sócio 3: 25 × 600 = R$ 15.000</li>
</ul>

<p>
<b>Verificação:</b> 6.000 + 9.000 + 15.000 = 30.000 ✓
</p>
</div>
</div>

<div id="outline-container-org15b690b" class="outline-5">
<h5 id="org15b690b"><span class="section-number-5">2.1.7.2.</span> Divisão Inversamente Proporcional</h5>
<div class="outline-text-5" id="text-2-1-7-2">
<p>
Dividir um número em partes inversamente proporcionais.
</p>

<p>
<b>Método:</b> 1. Inverter os números (usar recíprocos) 2. Aplicar divisão diretamente proporcional com os inversos
</p>

<p>
<b>Exemplo:</b> Dividir 220 em partes inversamente proporcionais a 2, 4 e 5.
</p>

<p>
<b>Solução:</b> 1. Inversos: 1/2, 1/4, 1/5 2. MMC(2, 4, 5) = 20 3. Transformar: 10, 5, 4 (multiplicando por 20) 4. Soma: 10 + 5 + 4 = 19 5. Constante: 220 / 19 ≈ 11,58 6. Partes:
</p>
<ul class="org-ul">
<li>1ª: 10 × 11,58 ≈ 115,8</li>
<li>2ª: 5 × 11,58 ≈ 57,9</li>
<li>3ª: 4 × 11,58 ≈ 46,3</li>
</ul>

<p>
Ou mais simples:
</p>

<ol class="org-ol">
<li>Inverter: inversamente a 2, 4, 5 → diretamente a 1/2, 1/4, 1/5</li>
<li>Denominador comum (20): 10, 5, 4</li>
<li>Dividir 220 proporcionalmente a 10, 5, 4 (como antes)</li>
</ol>
</div>
</div>
</div>

<div id="outline-container-orgaa7d740" class="outline-4">
<h4 id="orgaa7d740"><span class="section-number-4">2.1.8.</span> Regra de Três Simples</h4>
<div class="outline-text-4" id="text-2-1-8">
<p>
Método prático para resolver problemas com grandezas proporcionais.
</p>
</div>

<div id="outline-container-org98ee1f2" class="outline-5">
<h5 id="org98ee1f2"><span class="section-number-5">2.1.8.1.</span> Regra de Três Simples Direta</h5>
<div class="outline-text-5" id="text-2-1-8-1">
<p>
Quando as grandezas são diretamente proporcionais.
</p>

<p>
<b>Método:</b> 1. Montar a proporção 2. Multiplicar cruzado 3. Resolver a equação
</p>

<p>
<b>Exemplo:</b> Se 5 cadernos custam R$ 30, quanto custarão 8 cadernos?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org0719a52">
Cadernos    Preço
   5    ———   30
   8    ———    x

↓aumenta    ↑aumenta (direta)

5/8 = 30/x
5x = 8 × 30
5x = 240
x = 48
</pre>

<p>
<i>[Ver resposta 27 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgedba271" class="outline-5">
<h5 id="orgedba271"><span class="section-number-5">2.1.8.2.</span> Regra de Três Simples Inversa</h5>
<div class="outline-text-5" id="text-2-1-8-2">
<p>
Quando as grandezas são inversamente proporcionais.
</p>

<p>
<b>Método:</b> 1. Identificar que são inversas 2. Inverter uma das colunas 3. Multiplicar cruzado
</p>

<p>
<b>Exemplo:</b> Se 4 máquinas fazem um trabalho em 6 dias, quantos dias levarão 8 máquinas?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org438b410">
Máquinas    Dias
   4    ———   6
   8    ———   x

↑aumenta    ↓diminui (inversa)

4/8 = x/6  (inverti a coluna dos dias!)
4 × 6 = 8 × x
24 = 8x
x = 3
</pre>

<p>
<i>[Ver resposta 28 no final do documento]</i>
</p>

<p>
<b>Macete:</b> Se são inversas, inverta uma coluna antes de montar a proporção!
</p>
</div>
</div>
</div>

<div id="outline-container-orgc5b9374" class="outline-4">
<h4 id="orgc5b9374"><span class="section-number-4">2.1.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-1-9">
</div>
<div id="outline-container-org849dba4" class="outline-5">
<h5 id="org849dba4"><span class="section-number-5">2.1.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-1-9-1">
<p>
A razão entre as idades de João e Maria é 3/4. Se João tem 21 anos, qual a idade de Maria?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org06c1d2d">
J/M = 3/4
21/M = 3/4
3M = 21 × 4
3M = 84
M = 28
</pre>

<p>
<i>[Ver resposta 29 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgee98f41" class="outline-5">
<h5 id="orgee98f41"><span class="section-number-5">2.1.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-1-9-2">
<p>
Um mapa tem escala 1:2.000.000. Se a distância entre duas cidades no mapa é 5 cm, qual a distância real?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org85cd3fb">
1 cm no mapa ——— 2.000.000 cm real
5 cm no mapa ——— x

x = 5 × 2.000.000 = 10.000.000 cm = 100 km
</pre>

<p>
<i>[Ver resposta 30 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orge2e797e" class="outline-5">
<h5 id="orge2e797e"><span class="section-number-5">2.1.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-1-9-3">
<p>
Dividir 450 em partes diretamente proporcionais a 2, 3 e 4.
</p>

<p>
<b>Solução:</b> Soma: 2 + 3 + 4 = 9 Constante: 450 / 9 = 50
</p>

<p>
Partes:
</p>
<ul class="org-ul">
<li>2 × 50 = 100</li>
<li>3 × 50 = 150</li>
<li>4 × 50 = 200</li>
</ul>

<p>
<b>Verificação:</b> 100 + 150 + 200 = 450 ✓
</p>
</div>
</div>

<div id="outline-container-org538e37d" class="outline-5">
<h5 id="org538e37d"><span class="section-number-5">2.1.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-1-9-4">
<p>
Uma torneira enche um tanque em 10 horas. Quantas torneiras iguais serão necessárias para encher o tanque em 4 horas?
</p>

<p>
<b>Solução:</b> Inversamente proporcionais (mais torneiras → menos tempo)
</p>

<pre class="example" id="org3644471">
Torneiras    Horas
   1     ———   10
   x     ———    4

1/x = 4/10  (inverti!)
1 × 10 = x × 4
10 = 4x
x = 2,5
</pre>

<p>
<i>[Ver resposta 31 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgf3c28d3" class="outline-5">
<h5 id="orgf3c28d3"><span class="section-number-5">2.1.9.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-1-9-5">
<p>
Se 6 livros custam R$ 90, quanto custarão 10 livros?
</p>

<p>
<b>Solução:</b> Diretamente proporcionais
</p>

<pre class="example" id="org6a4a44e">
6/10 = 90/x
6x = 900
x = 150
</pre>

<p>
<i>[Ver resposta 32 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-orgf603229" class="outline-4">
<h4 id="orgf603229"><span class="section-number-4">2.1.10.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-1-10">
<ol class="org-ol">
<li><b>Identifique o tipo:</b> Direta ou inversa?

<ul class="org-ul">
<li>↑↑ ou ↓↓ → Direta</li>
<li>↑↓ ou ↓↑ → Inversa</li>
</ul></li>

<li><b>Regra de três inversa:</b> Inverta UMA das colunas antes de calcular</li>

<li><b>Proporção fundamental:</b> produto dos meios = produto dos extremos</li>

<li><b>Divisão proporcional:</b>

<ul class="org-ul">
<li>Some os valores proporcionais</li>
<li>Divida o total pela soma</li>
<li>Multiplique por cada valor</li>
</ul></li>

<li><b>Escala:</b> medida no desenho / medida real</li>

<li><b>Sempre verifique:</b> Confira se sua resposta faz sentido no contexto</li>
</ol>
</div>
</div>

<div id="outline-container-org475ad45" class="outline-4">
<h4 id="org475ad45"><span class="section-number-4">2.1.11.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-1-11">
<p>
<b>Razão:</b>
</p>
<ul class="org-ul">
<li>a/b (a está para b)</li>
<li>Comparação por divisão</li>
</ul>

<p>
<b>Proporção:</b>
</p>
<ul class="org-ul">
<li>a/b = c/d</li>
<li>Produto dos meios = produto dos extremos</li>
<li>a × d = b × c</li>
</ul>

<p>
<b>Grandezas:</b>
</p>
<ul class="org-ul">
<li><b>Diretamente proporcionais:</b> ↑↑ ou ↓↓ (razão constante)</li>
<li><b>Inversamente proporcionais:</b> ↑↓ ou ↓↑ (produto constante)</li>
</ul>

<p>
<b>Regra de três:</b>
</p>
<ul class="org-ul">
<li><b>Direta:</b> monta e calcula direto</li>
<li><b>Inversa:</b> inverte uma coluna primeiro</li>
</ul>
</div>
</div>

<div id="outline-container-orgbeac549" class="outline-4">
<h4 id="orgbeac549"><span class="section-number-4">2.1.12.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-1-12">
<pre class="example" id="org78436a3">
Razão:
r = a/b

Proporção:
a/b = c/d  →  a × d = b × c

Escala:
E = medida desenho / medida real

Velocidade média:
v = distância / tempo

Densidade demográfica:
d = população / área

Regra de três simples:
Direta: a/b = c/x
Inversa: a/b = x/c (inverte!)

Divisão proporcional:
Total / Soma das partes = Constante
Cada parte = Número × Constante
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>cai muito em questões contextualizadas)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orga01f5a8" class="outline-3">`;

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
