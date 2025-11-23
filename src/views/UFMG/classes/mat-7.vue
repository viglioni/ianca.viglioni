<script setup lang="ts">
import { ref } from "vue";

const code = "mat-7";
const title = "Matemática: Notação Científica, Algarismos Significativos e Estimativa";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-2-2">
<ul class="org-ul">
<li>Matemática: Notação Científica, Algarismos Significativos e Estimativa</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-org0c2214c" class="outline-4">
<h4 id="org0c2214c"><span class="section-number-4">2.2.1.</span> Notação Científica</h4>
<div class="outline-text-4" id="text-2-2-1">
</div>
<div id="outline-container-orgaa2b841" class="outline-5">
<h5 id="orgaa2b841"><span class="section-number-5">2.2.1.1.</span> O que é?</h5>
<div class="outline-text-5" id="text-2-2-1-1">
<p>
<b>Notação científica</b> é uma forma padronizada de escrever números muito grandes ou muito pequenos, facilitando cálculos e comparações.
</p>

<p>
<b>Formato geral:</b>
</p>

<pre class="example" id="org71ed094">
N × 10ⁿ

Onde:
- N é um número tal que 1 ≤ N &lt; 10
- n é um número inteiro (expoente)
</pre>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>5.000.000 = 5 × 10⁶</li>
<li>0,00003 = 3 × 10⁻⁵</li>
<li>780.000 = 7,8 × 10⁵</li>
<li>0,0056 = 5,6 × 10⁻³</li>
</ul>
</div>
</div>

<div id="outline-container-org13f11f9" class="outline-5">
<h5 id="org13f11f9"><span class="section-number-5">2.2.1.2.</span> Por que usar?</h5>
<div class="outline-text-5" id="text-2-2-1-2">
<p>
<b>Vantagens:</b>
</p>
<ul class="org-ul">
<li>Facilita escrita de números extremos</li>
<li>Simplifica cálculos</li>
<li>Padroniza representação científica</li>
<li>Evita erros de zeros</li>
</ul>

<p>
<b>Exemplos práticos:</b>
</p>
<ul class="org-ul">
<li>Distância Terra-Sol: 150.000.000.000 m = 1,5 × 10¹¹ m</li>
<li>Massa do elétron: 0,000000000000000000000000000000911 kg = 9,11 × 10⁻³¹ kg</li>
<li>Velocidade da luz: 300.000.000 m/s = 3 × 10⁸ m/s</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org15e67eb" class="outline-4">
<h4 id="org15e67eb"><span class="section-number-4">2.2.2.</span> Como Converter para Notação Científica</h4>
<div class="outline-text-4" id="text-2-2-2">
</div>
<div id="outline-container-orgba87baf" class="outline-5">
<h5 id="orgba87baf"><span class="section-number-5">2.2.2.1.</span> Números Grandes (maiores que 1)</h5>
<div class="outline-text-5" id="text-2-2-2-1">
<p>
<b>Passos:</b> 1. Colocar a vírgula após o primeiro algarismo significativo 2. Contar quantas casas a vírgula andou para a esquerda 3. Esse número é o expoente positivo de 10
</p>

<p>
<b>Exemplo 1:</b> 45.000
</p>

<pre class="example" id="org58cd1e0">
45.000
↓ (mover vírgula para após o 4)
4,5000
Andou 4 casas → 4,5 × 10⁴
</pre>

<p>
<b>Exemplo 2:</b> 6.750.000
</p>

<pre class="example" id="org76deb29">
6.750.000
↓
6,750000
Andou 6 casas → 6,75 × 10⁶
</pre>
</div>
</div>

<div id="outline-container-org25a6627" class="outline-5">
<h5 id="org25a6627"><span class="section-number-5">2.2.2.2.</span> Números Pequenos (menores que 1)</h5>
<div class="outline-text-5" id="text-2-2-2-2">
<p>
<b>Passos:</b> 1. Colocar a vírgula após o primeiro algarismo diferente de zero 2. Contar quantas casas a vírgula andou para a direita 3. Esse número é o expoente negativo de 10
</p>

<p>
<b>Exemplo 1:</b> 0,0034
</p>

<pre class="example" id="orgc449270">
0,0034
  ↓ (mover vírgula para após o 3)
  3,4
Andou 3 casas → 3,4 × 10⁻³
</pre>

<p>
<b>Exemplo 2:</b> 0,000000812
</p>

<pre class="example" id="orgb4f4133">
0,000000812
       ↓
       8,12
Andou 7 casas → 8,12 × 10⁻⁷
</pre>
</div>
</div>
</div>

<div id="outline-container-org779c791" class="outline-4">
<h4 id="org779c791"><span class="section-number-4">2.2.3.</span> Como Converter de Notação Científica para Decimal</h4>
<div class="outline-text-4" id="text-2-2-3">
</div>
<div id="outline-container-org30c19c6" class="outline-5">
<h5 id="org30c19c6"><span class="section-number-5">2.2.3.1.</span> Expoente Positivo</h5>
<div class="outline-text-5" id="text-2-2-3-1">
<p>
Mover a vírgula para a <b>direita</b> n casas (adicionar zeros se necessário).
</p>

<p>
<b>Exemplo 1:</b> 3,7 × 10⁴
</p>

<pre class="example" id="org3f191d7">
3,7 × 10⁴
Mover 4 casas à direita
3,7000
37.000
</pre>

<p>
<b>Exemplo 2:</b> 5,23 × 10⁶ = 5.230.000
</p>
</div>
</div>

<div id="outline-container-orgbf60822" class="outline-5">
<h5 id="orgbf60822"><span class="section-number-5">2.2.3.2.</span> Expoente Negativo</h5>
<div class="outline-text-5" id="text-2-2-3-2">
<p>
Mover a vírgula para a <b>esquerda</b> n casas (adicionar zeros se necessário).
</p>

<p>
<b>Exemplo 1:</b> 4,5 × 10⁻³
</p>

<pre class="example" id="orgd2db943">
4,5 × 10⁻³
Mover 3 casas à esquerda
0,0045
</pre>

<p>
<b>Exemplo 2:</b> 8,1 × 10⁻⁵ = 0,000081
</p>
</div>
</div>
</div>

<div id="outline-container-org1831f7e" class="outline-4">
<h4 id="org1831f7e"><span class="section-number-4">2.2.4.</span> Operações com Notação Científica</h4>
<div class="outline-text-4" id="text-2-2-4">
</div>
<div id="outline-container-orge204f8a" class="outline-5">
<h5 id="orge204f8a"><span class="section-number-5">2.2.4.1.</span> Multiplicação</h5>
<div class="outline-text-5" id="text-2-2-4-1">
<p>
<b>Regra:</b> 1. Multiplicar os números N 2. Somar os expoentes 3. Ajustar para forma padrão se necessário
</p>

<p>
<b>Fórmula:</b> (a × 10ᵐ) × (b × 10ⁿ) = (a × b) × 10⁽ᵐ⁺ⁿ⁾
</p>

<p>
<b>Exemplo 1:</b>
</p>

<pre class="example" id="orge07e6f2">
(2 × 10³) × (3 × 10⁵)
= (2 × 3) × 10⁽³⁺⁵⁾
= 6 × 10⁸
</pre>

<p>
<b>Exemplo 2:</b>
</p>

<pre class="example" id="orgd7775fa">
(4 × 10⁴) × (5 × 10⁻²)
= (4 × 5) × 10⁽⁴⁺⁽⁻²⁾⁾
= 20 × 10²
= 2 × 10³  (ajustando: 20 = 2 × 10¹)
</pre>
</div>
</div>

<div id="outline-container-org6ab6ad9" class="outline-5">
<h5 id="org6ab6ad9"><span class="section-number-5">2.2.4.2.</span> Divisão</h5>
<div class="outline-text-5" id="text-2-2-4-2">
<p>
<b>Regra:</b> 1. Dividir os números N 2. Subtrair os expoentes 3. Ajustar para forma padrão se necessário
</p>

<p>
<b>Fórmula:</b> (a × 10ᵐ) ÷ (b × 10ⁿ) = (a ÷ b) × 10⁽ᵐ⁻ⁿ⁾
</p>

<p>
<b>Exemplo 1:</b>
</p>

<pre class="example" id="org34c5441">
(8 × 10⁶) ÷ (2 × 10³)
= (8 ÷ 2) × 10⁽⁶⁻³⁾
= 4 × 10³
</pre>

<p>
<b>Exemplo 2:</b>
</p>

<pre class="example" id="org994a217">
(6 × 10⁴) ÷ (3 × 10⁷)
= (6 ÷ 3) × 10⁽⁴⁻⁷⁾
= 2 × 10⁻³
</pre>
</div>
</div>

<div id="outline-container-org27b9b06" class="outline-5">
<h5 id="org27b9b06"><span class="section-number-5">2.2.4.3.</span> Adição e Subtração</h5>
<div class="outline-text-5" id="text-2-2-4-3">
<p>
<b>Regra:</b> Só é prático somar/subtrair se os expoentes forem <b>iguais</b>.
</p>

<ol class="org-ol">
<li>Igualar os expoentes (se necessário)</li>
<li>Somar ou subtrair os números N</li>
<li>Manter o expoente comum</li>
</ol>

<p>
<b>Exemplo 1:</b> (mesmo expoente)
</p>

<pre class="example" id="orge463849">
(3 × 10⁵) + (2 × 10⁵)
= (3 + 2) × 10⁵
= 5 × 10⁵
</pre>

<p>
<b>Exemplo 2:</b> (expoentes diferentes)
</p>

<pre class="example" id="org262df8a">
(5 × 10⁴) + (3 × 10³)
Igualar expoentes:
(5 × 10⁴) + (0,3 × 10⁴)
= (5 + 0,3) × 10⁴
= 5,3 × 10⁴
</pre>
</div>
</div>
</div>

<div id="outline-container-org7fc7b0e" class="outline-4">
<h4 id="org7fc7b0e"><span class="section-number-4">2.2.5.</span> Algarismos Significativos</h4>
<div class="outline-text-4" id="text-2-2-5">
</div>
<div id="outline-container-org7525634" class="outline-5">
<h5 id="org7525634"><span class="section-number-5">2.2.5.1.</span> O que são?</h5>
<div class="outline-text-5" id="text-2-2-5-1">
<p>
<b>Algarismos significativos</b> são todos os dígitos que têm significado na precisão de uma medida.
</p>
</div>
</div>

<div id="outline-container-org1c91f77" class="outline-5">
<h5 id="org1c91f77"><span class="section-number-5">2.2.5.2.</span> Regras para Identificar</h5>
<div class="outline-text-5" id="text-2-2-5-2">
<p>
<b>1. Todos os dígitos diferentes de zero são significativos</b>
</p>
<ul class="org-ul">
<li>245 → 3 algarismos significativos</li>
<li>1,234 → 4 algarismos significativos</li>
</ul>

<p>
<b>2. Zeros entre dígitos diferentes de zero são significativos</b>
</p>
<ul class="org-ul">
<li>1007 → 4 algarismos significativos</li>
<li>50,03 → 4 algarismos significativos</li>
</ul>

<p>
<b>3. Zeros à esquerda NÃO são significativos</b> (apenas indicam posição)
</p>
<ul class="org-ul">
<li>0,0025 → 2 algarismos significativos (2 e 5)</li>
<li>0,0400 → 3 algarismos significativos (4, 0, 0)</li>
</ul>

<p>
<b>4. Zeros à direita:</b>
</p>
<ul class="org-ul">
<li><b>Com vírgula:</b> são significativos</li>
<li>2,50 → 3 algarismos significativos</li>
<li>100,0 → 4 algarismos significativos</li>

<li><b>Sem vírgula:</b> podem ser ambíguos
<ul class="org-ul">
<li>1500 → 2, 3 ou 4? (depende do contexto)</li>
<li>Melhor usar notação científica: 1,5 × 10³ (2 sig.) ou 1,50 × 10³ (3 sig.)</li>
</ul></li>
</ul>
</div>
</div>

<div id="outline-container-org9be0dd9" class="outline-5">
<h5 id="org9be0dd9"><span class="section-number-5">2.2.5.3.</span> Exemplos de Contagem</h5>
<div class="outline-text-5" id="text-2-2-5-3">
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Número</th>
<th scope="col" class="org-left">Algarismos Significativos</th>
<th scope="col" class="org-right">Quantidade</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">123</td>
<td class="org-left">1, 2, 3</td>
<td class="org-right">3</td>
</tr>

<tr>
<td class="org-left">0,0056</td>
<td class="org-left">5, 6</td>
<td class="org-right">2</td>
</tr>

<tr>
<td class="org-left">1,020</td>
<td class="org-left">1, 0, 2, 0</td>
<td class="org-right">4</td>
</tr>

<tr>
<td class="org-left">500</td>
<td class="org-left">5 (ambíguo)</td>
<td class="org-right">1, 2 ou 3</td>
</tr>

<tr>
<td class="org-left">5,00 × 10²</td>
<td class="org-left">5, 0, 0</td>
<td class="org-right">3</td>
</tr>

<tr>
<td class="org-left">0,0700</td>
<td class="org-left">7, 0, 0</td>
<td class="org-right">3</td>
</tr>

<tr>
<td class="org-left">1005</td>
<td class="org-left">1, 0, 0, 5</td>
<td class="org-right">4</td>
</tr>
</tbody>
</table>
</div>
</div>

<div id="outline-container-org00ccd6b" class="outline-5">
<h5 id="org00ccd6b"><span class="section-number-5">2.2.5.4.</span> Operações com Algarismos Significativos</h5>
<div class="outline-text-5" id="text-2-2-5-4">
<p>
<b>Multiplicação e Divisão:</b> O resultado deve ter o <b>mesmo número</b> de algarismos significativos que o fator com <b>menos</b> algarismos significativos.
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgd906028">
2,5 (2 sig.) × 3,147 (4 sig.)
= 7,8675
Arredondando para 2 sig. → 7,9
</pre>

<p>
<b>Adição e Subtração:</b> O resultado deve ter o mesmo número de <b>casas decimais</b> que a medida com <b>menos</b> casas decimais.
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="org22e96d0">
12,5 (1 casa decimal)
+  0,123 (3 casas decimais)
_______
12,623 → arredondar para 1 casa → 12,6
</pre>
</div>
</div>
</div>

<div id="outline-container-org7e1570d" class="outline-4">
<h4 id="org7e1570d"><span class="section-number-4">2.2.6.</span> Arredondamento</h4>
<div class="outline-text-4" id="text-2-2-6">
<p>
<b>Regra básica:</b>
</p>
<ul class="org-ul">
<li>Se o dígito seguinte for &lt; 5: arredondar para baixo</li>
<li>Se o dígito seguinte for ≥ 5: arredondar para cima</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>3,14 arredondado para 1 casa decimal → 3,1</li>
<li>3,16 arredondado para 1 casa decimal → 3,2</li>
<li>3,15 arredondado para 1 casa decimal → 3,2</li>
<li>2,748 arredondado para 2 sig. → 2,7</li>
</ul>
</div>
</div>

<div id="outline-container-org8e7318b" class="outline-4">
<h4 id="org8e7318b"><span class="section-number-4">2.2.7.</span> Estimativa e Ordem de Grandeza</h4>
<div class="outline-text-4" id="text-2-2-7">
</div>
<div id="outline-container-org3dd0e2f" class="outline-5">
<h5 id="org3dd0e2f"><span class="section-number-5">2.2.7.1.</span> Ordem de Grandeza</h5>
<div class="outline-text-5" id="text-2-2-7-1">
<p>
<b>Definição:</b> A ordem de grandeza de um número é a potência de 10 mais próxima dele.
</p>

<p>
<b>Método:</b> 1. Escrever em notação científica: N × 10ⁿ 2. Se N &lt; √10 ≈ 3,16 → ordem = 10ⁿ 3. Se N ≥ √10 ≈ 3,16 → ordem = 10ⁿ⁺¹
</p>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Exemplo 1:</b> 2.500
</p>

<pre class="example" id="orgab41490">
2.500 = 2,5 × 10³
2,5 &lt; 3,16
Ordem de grandeza: 10³
</pre>

<p>
<b>Exemplo 2:</b> 7.000
</p>

<pre class="example" id="orgfd0279a">
7.000 = 7 × 10³
7 &gt; 3,16
Ordem de grandeza: 10⁴
</pre>

<p>
<b>Exemplo 3:</b> 0,002
</p>

<pre class="example" id="org673918d">
0,002 = 2 × 10⁻³
2 &lt; 3,16
Ordem de grandeza: 10⁻³
</pre>
</div>
</div>

<div id="outline-container-org2420551" class="outline-5">
<h5 id="org2420551"><span class="section-number-5">2.2.7.2.</span> Estimativas</h5>
<div class="outline-text-5" id="text-2-2-7-2">
<p>
<b>Uso prático:</b> Fazer cálculos aproximados rapidamente.
</p>

<p>
<b>Técnicas:</b> 1. Arredondar para valores convenientes 2. Usar potências de 10 3. Simplificar frações
</p>

<p>
<b>Exemplo 1:</b> Estimar: 48 × 23
</p>

<pre class="example" id="org46e6f5b">
Aproximar:
50 × 20 = 1.000

(Valor real: 1.104)
</pre>

<p>
<b>Exemplo 2:</b> Estimar a população de células em 1 kg de tecido humano, sabendo que uma célula tem massa de 10⁻¹² kg.
</p>

<pre class="example" id="org1e0c350">
Número de células ≈ massa total / massa por célula
≈ 1 / 10⁻¹²
= 10¹² células
</pre>
</div>
</div>
</div>

<div id="outline-container-orgd8de916" class="outline-4">
<h4 id="orgd8de916"><span class="section-number-4">2.2.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-2-2-8">
</div>
<div id="outline-container-org195c581" class="outline-5">
<h5 id="org195c581"><span class="section-number-5">2.2.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-2-2-8-1">
<p>
Escreva em notação científica: a) 350.000 b) 0,00045 c) 12.000.000.000
</p>

<p>
<b>Resposta:</b> a) 3,5 × 10⁵ b) 4,5 × 10⁻⁴ c) 1,2 × 10¹⁰
</p>
</div>
</div>

<div id="outline-container-org3329e99" class="outline-5">
<h5 id="org3329e99"><span class="section-number-5">2.2.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-2-2-8-2">
<p>
Escreva em forma decimal: a) 6,2 × 10⁴ b) 3,8 × 10⁻³
</p>

<p>
<b>Resposta:</b> a) 62.000 b) 0,0038
</p>
</div>
</div>

<div id="outline-container-org61fb513" class="outline-5">
<h5 id="org61fb513"><span class="section-number-5">2.2.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-2-2-8-3">
<p>
Calcule: (2 × 10⁵) × (4 × 10³)
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgf328031">
= (2 × 4) × 10⁽⁵⁺³⁾
= 8 × 10⁸
</pre>
</div>
</div>

<div id="outline-container-org968b067" class="outline-5">
<h5 id="org968b067"><span class="section-number-5">2.2.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-2-2-8-4">
<p>
Calcule: (9 × 10⁷) ÷ (3 × 10⁴)
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org7c80bb7">
= (9 ÷ 3) × 10⁽⁷⁻⁴⁾
= 3 × 10³
</pre>
</div>
</div>

<div id="outline-container-orgdf0700d" class="outline-5">
<h5 id="orgdf0700d"><span class="section-number-5">2.2.8.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-2-2-8-5">
<p>
Quantos algarismos significativos têm: a) 0,0034 b) 1,200 c) 1050
</p>

<p>
<b>Resposta:</b> a) 2 (3 e 4) b) 4 (1, 2, 0, 0) c) 3 ou 4 (ambíguo sem vírgula; melhor usar notação científica)
</p>
</div>
</div>

<div id="outline-container-org0e70bc8" class="outline-5">
<h5 id="org0e70bc8"><span class="section-number-5">2.2.8.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-2-2-8-6">
<p>
Determine a ordem de grandeza de 8.000.
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org621614a">
8.000 = 8 × 10³
8 &gt; 3,16
Ordem de grandeza: 10⁴
</pre>
</div>
</div>
</div>

<div id="outline-container-orgd6c4e8d" class="outline-4">
<h4 id="orgd6c4e8d"><span class="section-number-4">2.2.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-2-2-9">
<ol class="org-ol">
<li><b>Notação científica:</b> 1 ≤ N &lt; 10 sempre</li>
<li><b>Expoente positivo:</b> número grande (&gt; 1)</li>
<li><b>Expoente negativo:</b> número pequeno (&lt; 1)</li>
<li><b>Multiplicação:</b> soma expoentes</li>
<li><b>Divisão:</b> subtrai expoentes</li>
<li><b>Algarismos significativos:</b> zeros à esquerda NÃO contam</li>
<li><b>Ordem de grandeza:</b> use √10 ≈ 3,16 como referência</li>
<li><b>Estimativa:</b> arredonde para facilitar cálculos mentais</li>
</ol>
</div>
</div>

<div id="outline-container-orga46117a" class="outline-4">
<h4 id="orga46117a"><span class="section-number-4">2.2.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-2-2-10">
<p>
<b>Notação Científica:</b>
</p>
<ul class="org-ul">
<li>Formato: N × 10ⁿ (1 ≤ N &lt; 10)</li>
<li>Grande → expoente positivo</li>
<li>Pequeno → expoente negativo</li>
</ul>

<p>
<b>Operações:</b>
</p>
<ul class="org-ul">
<li>Multiplicação: (a × 10ᵐ) × (b × 10ⁿ) = (a×b) × 10⁽ᵐ⁺ⁿ⁾</li>
<li>Divisão: (a × 10ᵐ) ÷ (b × 10ⁿ) = (a÷b) × 10⁽ᵐ⁻ⁿ⁾</li>
</ul>

<p>
<b>Algarismos Significativos:</b>
</p>
<ul class="org-ul">
<li>Zeros à esquerda: NÃO</li>
<li>Zeros entre dígitos: SIM</li>
<li>Zeros à direita com vírgula: SIM</li>
<li>Zeros à direita sem vírgula: AMBÍGUO</li>
</ul>

<p>
<b>Ordem de Grandeza:</b>
</p>
<ul class="org-ul">
<li>N &lt; 3,16 → 10ⁿ</li>
<li>N ≥ 3,16 → 10ⁿ⁺¹</li>
</ul>
</div>
</div>

<div id="outline-container-org7cb7044" class="outline-4">
<h4 id="org7cb7044"><span class="section-number-4">2.2.11.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-2-2-11">
<pre class="example" id="orgdf1d169">
Notação Científica:
N × 10ⁿ  onde 1 ≤ N &lt; 10

Multiplicação:
(a × 10ᵐ) × (b × 10ⁿ) = (a × b) × 10⁽ᵐ⁺ⁿ⁾

Divisão:
(a × 10ᵐ) ÷ (b × 10ⁿ) = (a ÷ b) × 10⁽ᵐ⁻ⁿ⁾

Ordem de Grandeza:
N × 10ⁿ
Se N &lt; √10 (≈ 3,16) → 10ⁿ
Se N ≥ √10 (≈ 3,16) → 10ⁿ⁺¹

Constantes úteis:
Velocidade da luz: c = 3 × 10⁸ m/s
Massa do elétron: mₑ = 9,11 × 10⁻³¹ kg
Carga do elétron: e = 1,6 × 10⁻¹⁹ C
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐ (importante
</p>
<ul class="org-ul">
<li>frequente em questões de Ciências da Natureza)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org42b9994" class="outline-3">`;

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
