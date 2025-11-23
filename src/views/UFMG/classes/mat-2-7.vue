<script setup lang="ts">
import { ref } from "vue";

const code = "mat-2-7";
const title = "Matemática: MMC e MDC";
const subject = "matematica";
const themes = ["Funções","logaritmica"];
const dates = ["2025-12-02"];
const lessonContent = `<div class="outline-text-3" id="text-1-2">
<ul class="org-ul">
<li>Matemática: MMC e MDC</li>
<li>60min</li>
</ul>
</div>
<div id="outline-container-orgd45b392" class="outline-4">
<h4 id="orgd45b392"><span class="section-number-4">1.2.1.</span> O que é Divisibilidade?</h4>
<div class="outline-text-4" id="text-1-2-1">
<p>
Um número <b>a</b> é divisível por um número <b>b</b> quando a divisão de <b>a</b> por <b>b</b> é exata (resto zero).
</p>

<p>
<b>Notação:</b> b | a (lê-se “b divide a”)
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>15 é divisível por 3, pois 15 ÷ 3 = 5 (resto 0)</li>
<li>20 é divisível por 4, pois 20 ÷ 4 = 5 (resto 0)</li>
<li>17 NÃO é divisível por 3, pois 17 ÷ 3 = 5 (resto 2)</li>
</ul>
</div>
</div>

<div id="outline-container-org1ab5a57" class="outline-4">
<h4 id="org1ab5a57"><span class="section-number-4">1.2.2.</span> Critérios de Divisibilidade</h4>
<div class="outline-text-4" id="text-1-2-2">
</div>
<div id="outline-container-orgdfc2dff" class="outline-5">
<h5 id="orgdfc2dff"><span class="section-number-5">1.2.2.1.</span> Divisibilidade por 2</h5>
<div class="outline-text-5" id="text-1-2-2-1">
<p>
Um número é divisível por 2 se termina em 0, 2, 4, 6 ou 8 (número par).
</p>

<p>
<b>Exemplos:</b> 14, 28, 100, 456
</p>
</div>
</div>

<div id="outline-container-orgf53252e" class="outline-5">
<h5 id="orgf53252e"><span class="section-number-5">1.2.2.2.</span> Divisibilidade por 3</h5>
<div class="outline-text-5" id="text-1-2-2-2">
<p>
Um número é divisível por 3 se a soma de seus algarismos é divisível por 3.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>123 → 1 + 2 + 3 = 6 (divisível por 3) ✓</li>
<li>234 → 2 + 3 + 4 = 9 (divisível por 3) ✓</li>
<li>125 → 1 + 2 + 5 = 8 (NÃO divisível por 3) ✗</li>
</ul>
</div>
</div>

<div id="outline-container-org8e988cf" class="outline-5">
<h5 id="org8e988cf"><span class="section-number-5">1.2.2.3.</span> Divisibilidade por 4</h5>
<div class="outline-text-5" id="text-1-2-2-3">
<p>
Um número é divisível por 4 se os dois últimos algarismos formam um número divisível por 4.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>316 → 16 é divisível por 4 ✓</li>
<li>1028 → 28 é divisível por 4 ✓</li>
<li>1222 → 22 NÃO é divisível por 4 ✗</li>
</ul>
</div>
</div>

<div id="outline-container-org4aedfe7" class="outline-5">
<h5 id="org4aedfe7"><span class="section-number-5">1.2.2.4.</span> Divisibilidade por 5</h5>
<div class="outline-text-5" id="text-1-2-2-4">
<p>
Um número é divisível por 5 se termina em 0 ou 5.
</p>

<p>
<b>Exemplos:</b> 25, 30, 105, 500
</p>
</div>
</div>

<div id="outline-container-org9068e8c" class="outline-5">
<h5 id="org9068e8c"><span class="section-number-5">1.2.2.5.</span> Divisibilidade por 6</h5>
<div class="outline-text-5" id="text-1-2-2-5">
<p>
Um número é divisível por 6 se é divisível por 2 <b>E</b> por 3 simultaneamente.
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>36 → par (divisível por 2) e 3 + 6 = 9 (divisível por 3) ✓</li>
</ul>
</div>
</div>

<div id="outline-container-orgc87b206" class="outline-5">
<h5 id="orgc87b206"><span class="section-number-5">1.2.2.6.</span> Divisibilidade por 9</h5>
<div class="outline-text-5" id="text-1-2-2-6">
<p>
Um número é divisível por 9 se a soma de seus algarismos é divisível por 9.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>729 → 7 + 2 + 9 = 18 (divisível por 9) ✓</li>
<li>234 → 2 + 3 + 4 = 9 (divisível por 9) ✓</li>
</ul>
</div>
</div>

<div id="outline-container-org5821efe" class="outline-5">
<h5 id="org5821efe"><span class="section-number-5">1.2.2.7.</span> Divisibilidade por 10</h5>
<div class="outline-text-5" id="text-1-2-2-7">
<p>
Um número é divisível por 10 se termina em 0.
</p>

<p>
<b>Exemplos:</b> 30, 100, 250, 1000
</p>
</div>
</div>
</div>

<div id="outline-container-org52b380a" class="outline-4">
<h4 id="org52b380a"><span class="section-number-4">1.2.3.</span> Números Primos</h4>
<div class="outline-text-4" id="text-1-2-3">
<p>
Um número primo é um número natural maior que 1 que possui <b>exatamente dois divisores</b>: 1 e ele mesmo.
</p>

<p>
<b>Primeiros números primos:</b> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, &#x2026;
</p>

<p>
<b>Observações importantes:</b>
</p>
<ul class="org-ul">
<li>1 <b>NÃO</b> é primo (possui apenas um divisor)</li>
<li>2 é o <b>único</b> número primo par</li>
<li>Todo número natural maior que 1 é primo ou composto</li>
</ul>
</div>
</div>

<div id="outline-container-orgc470c8b" class="outline-4">
<h4 id="orgc470c8b"><span class="section-number-4">1.2.4.</span> Números Compostos</h4>
<div class="outline-text-4" id="text-1-2-4">
<p>
Um número composto é um número natural maior que 1 que possui <b>mais de dois divisores</b>.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>4 (divisores: 1, 2, 4)</li>
<li>6 (divisores: 1, 2, 3, 6)</li>
<li>9 (divisores: 1, 3, 9)</li>
<li>12 (divisores: 1, 2, 3, 4, 6, 12)</li>
</ul>
</div>
</div>

<div id="outline-container-org4a0edfe" class="outline-4">
<h4 id="org4a0edfe"><span class="section-number-4">1.2.5.</span> Decomposição em Fatores Primos (Fatoração)</h4>
<div class="outline-text-4" id="text-1-2-5">
<p>
Todo número composto pode ser escrito como produto de números primos. Essa representação é única.
</p>

<p>
<b>Método:</b> Dividir sucessivamente o número pelos menores primos possíveis até chegar a 1.
</p>
</div>

<div id="outline-container-org61e5933" class="outline-5">
<h5 id="org61e5933"><span class="section-number-5">1.2.5.1.</span> Exemplo 1: Fatorar 60</h5>
<div class="outline-text-5" id="text-1-2-5-1">
<pre class="example" id="org53df571">
60 | 2
30 | 2
15 | 3
 5 | 5
 1 |
</pre>

<p>
<b>Resultado:</b> 60 = 2² × 3 × 5
</p>
</div>
</div>

<div id="outline-container-org947008a" class="outline-5">
<h5 id="org947008a"><span class="section-number-5">1.2.5.2.</span> Exemplo 2: Fatorar 180</h5>
<div class="outline-text-5" id="text-1-2-5-2">
<pre class="example" id="orgebf2146">
180 | 2
 90 | 2
 45 | 3
 15 | 3
  5 | 5
  1 |
</pre>

<p>
<b>Resultado:</b> 180 = 2² × 3² × 5
</p>
</div>
</div>

<div id="outline-container-org202223a" class="outline-5">
<h5 id="org202223a"><span class="section-number-5">1.2.5.3.</span> Exemplo 3: Fatorar 100</h5>
<div class="outline-text-5" id="text-1-2-5-3">
<pre class="example" id="orgf0a93ff">
100 | 2
 50 | 2
 25 | 5
  5 | 5
  1 |
</pre>

<p>
<b>Resultado:</b> 100 = 2² × 5²
</p>
</div>
</div>
</div>

<div id="outline-container-orgf5071f3" class="outline-4">
<h4 id="orgf5071f3"><span class="section-number-4">1.2.6.</span> MDC</h4>
<div class="outline-text-4" id="text-1-2-6">
<ul class="org-ul">
<li>Máximo Divisor Comum</li>
</ul>
<p>
O <b>MDC</b> de dois ou mais números é o <b>maior</b> número que divide todos eles simultaneamente.
</p>
</div>

<div id="outline-container-org148cb46" class="outline-5">
<h5 id="org148cb46"><span class="section-number-5">1.2.6.1.</span> Método 1: Listar Divisores</h5>
<div class="outline-text-5" id="text-1-2-6-1">
<p>
<b>Exemplo:</b> MDC(12, 18)
</p>

<p>
Divisores de 12: 1, 2, 3, 4, 6, 12 Divisores de 18: 1, 2, 3, 6, 9, 18
</p>

<p>
Divisores comuns: 1, 2, 3, 6 <b>MDC(12, 18) = 6</b>
</p>
</div>
</div>

<div id="outline-container-org4f052db" class="outline-5">
<h5 id="org4f052db"><span class="section-number-5">1.2.6.2.</span> Método 2: Decomposição em Fatores Primos</h5>
<div class="outline-text-5" id="text-1-2-6-2">
<p>
<b>Regra:</b> O MDC é o produto dos fatores primos <b>comuns</b> com os <b>menores expoentes</b>.
</p>

<p>
<b>Exemplo:</b> MDC(60, 180)
</p>

<ul class="org-ul">
<li>60 = 2² × 3 × 5</li>
<li>180 = 2² × 3² × 5</li>
</ul>

<p>
Fatores comuns com menores expoentes:
</p>
<ul class="org-ul">
<li>2² (menor expoente entre 2² e 2²)</li>
<li>3¹ (menor expoente entre 3¹ e 3²)</li>
<li>5¹ (menor expoente entre 5¹ e 5¹)</li>
</ul>

<p>
<b>MDC(60, 180) = 2² × 3 × 5 = 4 × 3 × 5 = 60</b>
</p>
</div>
</div>

<div id="outline-container-org1541d1f" class="outline-5">
<h5 id="org1541d1f"><span class="section-number-5">1.2.6.3.</span> Método 3: Divisões Sucessivas (Algoritmo de Euclides)</h5>
<div class="outline-text-5" id="text-1-2-6-3">
<p>
Divide-se o maior pelo menor, depois o divisor pelo resto, repetindo até resto zero. O último divisor é o MDC.
</p>

<p>
<b>Exemplo:</b> MDC(48, 18)
</p>

<pre class="example" id="orgebda1ed">
48 ÷ 18 = 2 (resto 12)
18 ÷ 12 = 1 (resto 6)
12 ÷ 6 = 2 (resto 0)
</pre>

<p>
<b>MDC(48, 18) = 6</b>
</p>
</div>
</div>
</div>

<div id="outline-container-orga0ba582" class="outline-4">
<h4 id="orga0ba582"><span class="section-number-4">1.2.7.</span> Propriedades do MDC</h4>
<div class="outline-text-4" id="text-1-2-7">
<ol class="org-ol">
<li><b>MDC(a, b) = MDC(b, a)</b> (comutativo)</li>
<li><b>MDC(a, 1) = 1</b> (1 divide qualquer número)</li>
<li><b>MDC(a, 0) = a</b></li>
<li>Se <b>a | b</b>, então <b>MDC(a, b) = a</b></li>
<li><b>MDC(a, b) × MMC(a, b) = a × b</b></li>
</ol>
</div>
</div>

<div id="outline-container-org5f23d1f" class="outline-4">
<h4 id="org5f23d1f"><span class="section-number-4">1.2.8.</span> Números Primos entre Si</h4>
<div class="outline-text-4" id="text-1-2-8">
<p>
Dois números são <b>primos entre si</b> (ou coprimos) quando MDC = 1.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>MDC(8, 15) = 1 → 8 e 15 são primos entre si</li>
<li>MDC(9, 16) = 1 → 9 e 16 são primos entre si</li>
<li>MDC(12, 18) = 6 → 12 e 18 NÃO são primos entre si</li>
</ul>
</div>
</div>

<div id="outline-container-org2b76469" class="outline-4">
<h4 id="org2b76469"><span class="section-number-4">1.2.9.</span> MMC</h4>
<div class="outline-text-4" id="text-1-2-9">
<ul class="org-ul">
<li>Mínimo Múltiplo Comum</li>
</ul>
<p>
O <b>MMC</b> de dois ou mais números é o <b>menor</b> número (diferente de zero) que é múltiplo de todos eles.
</p>
</div>

<div id="outline-container-orga4170cd" class="outline-5">
<h5 id="orga4170cd"><span class="section-number-5">1.2.9.1.</span> Método 1: Listar Múltiplos</h5>
<div class="outline-text-5" id="text-1-2-9-1">
<p>
<b>Exemplo:</b> MMC(4, 6)
</p>

<p>
Múltiplos de 4: 4, 8, <b>12</b>, 16, 20, 24, &#x2026; Múltiplos de 6: 6, <b>12</b>, 18, 24, 30, &#x2026;
</p>

<p>
Múltiplos comuns: 12, 24, 36, &#x2026; <b>MMC(4, 6) = 12</b>
</p>
</div>
</div>

<div id="outline-container-orge7695ef" class="outline-5">
<h5 id="orge7695ef"><span class="section-number-5">1.2.9.2.</span> Método 2: Decomposição em Fatores Primos</h5>
<div class="outline-text-5" id="text-1-2-9-2">
<p>
<b>Regra:</b> O MMC é o produto de <b>todos os fatores primos</b> (comuns e não comuns) com os <b>maiores expoentes</b>.
</p>

<p>
<b>Exemplo:</b> MMC(12, 18)
</p>

<ul class="org-ul">
<li>12 = 2² × 3</li>
<li>18 = 2 × 3²</li>
</ul>

<p>
Todos os fatores com maiores expoentes:
</p>
<ul class="org-ul">
<li>2² (maior expoente entre 2² e 2¹)</li>
<li>3² (maior expoente entre 3¹ e 3²)</li>
</ul>

<p>
<b>MMC(12, 18) = 2² × 3² = 4 × 9 = 36</b>
</p>
</div>
</div>

<div id="outline-container-org817bafd" class="outline-5">
<h5 id="org817bafd"><span class="section-number-5">1.2.9.3.</span> Método 3: Decomposição Simultânea</h5>
<div class="outline-text-5" id="text-1-2-9-3">
<p>
Decompõe-se todos os números ao mesmo tempo, usando os primos que dividem pelo menos um deles.
</p>

<p>
<b>Exemplo:</b> MMC(12, 18, 30)
</p>

<pre class="example" id="orga6f07d9">
12, 18, 30 | 2
 6,  9, 15 | 2
 3,  9, 15 | 3
 1,  3,  5 | 3
 1,  1,  5 | 5
 1,  1,  1 |
</pre>

<p>
<b>MMC(12, 18, 30) = 2 × 2 × 3 × 3 × 5 = 180</b>
</p>
</div>
</div>
</div>

<div id="outline-container-orgf31ff72" class="outline-4">
<h4 id="orgf31ff72"><span class="section-number-4">1.2.10.</span> Propriedades do MMC</h4>
<div class="outline-text-4" id="text-1-2-10">
<ol class="org-ol">
<li><b>MMC(a, b) = MMC(b, a)</b> (comutativo)</li>
<li><b>MMC(a, 1) = a</b></li>
<li>Se <b>a | b</b>, então <b>MMC(a, b) = b</b></li>
<li><b>MMC(a, b) × MDC(a, b) = a × b</b></li>
<li><b>MMC(a, b, c) ≥ máximo{a, b, c}</b></li>
</ol>
</div>
</div>

<div id="outline-container-org7c1ba00" class="outline-4">
<h4 id="org7c1ba00"><span class="section-number-4">1.2.11.</span> Relação entre MDC e MMC</h4>
<div class="outline-text-4" id="text-1-2-11">
<p>
Para dois números a e b:
</p>

<p>
<b>MDC(a, b) × MMC(a, b) = a × b</b>
</p>

<p>
<b>Exemplo:</b> a = 12, b = 18
</p>
<ul class="org-ul">
<li>MDC(12, 18) = 6</li>
<li>MMC(12, 18) = 36</li>
<li>6 × 36 = 216</li>
<li>12 × 18 = 216 ✓</li>
</ul>

<p>
Essa propriedade permite calcular um quando se conhece o outro:
</p>

<p>
<b>MMC(a, b) = (a × b) / MDC(a, b)</b>
</p>

<p>
<b>MDC(a, b) = (a × b) / MMC(a, b)</b>
</p>
</div>
</div>

<div id="outline-container-org6699d09" class="outline-4">
<h4 id="org6699d09"><span class="section-number-4">1.2.12.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-1-2-12">
</div>
<div id="outline-container-org29c1c13" class="outline-5">
<h5 id="org29c1c13"><span class="section-number-5">1.2.12.1.</span> Problema de MMC</h5>
<div class="outline-text-5" id="text-1-2-12-1">
<p>
<b>Situação:</b> Dois ônibus partem juntos de um terminal. Um retorna a cada 12 minutos, o outro a cada 18 minutos. Depois de quanto tempo voltarão a partir juntos novamente?
</p>

<p>
<b>Solução:</b> MMC(12, 18)
</p>
<ul class="org-ul">
<li>12 = 2² × 3</li>
<li>18 = 2 × 3²</li>
<li>MMC = 2² × 3² = 36</li>
</ul>

<p>
<i>[Ver resposta 9 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org84919bd" class="outline-5">
<h5 id="org84919bd"><span class="section-number-5">1.2.12.2.</span> Problema de MDC</h5>
<div class="outline-text-5" id="text-1-2-12-2">
<p>
<b>Situação:</b> Uma empresa tem 60 canetas azuis e 48 canetas vermelhas. Quer fazer pacotes iguais usando todas as canetas, com o maior número possível de canetas por pacote. Quantas canetas terá cada pacote?
</p>

<p>
<b>Solução:</b> MDC(60, 48)
</p>
<ul class="org-ul">
<li>60 = 2² × 3 × 5</li>
<li>48 = 2⁴ × 3</li>
<li>MDC = 2² × 3 = 12</li>
</ul>

<p>
<i>[Ver resposta 10 no final do documento]</i>
</p>
<ul class="org-ul">
<li>Pacotes de azuis: 60 ÷ 12 = 5</li>
<li>Pacotes de vermelhas: 48 ÷ 12 = 4</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org4f2f883" class="outline-4">
<h4 id="org4f2f883"><span class="section-number-4">1.2.13.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-1-2-13">
</div>
<div id="outline-container-org4b854ec" class="outline-5">
<h5 id="org4b854ec"><span class="section-number-5">1.2.13.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-1-2-13-1">
<p>
Calcule MDC(48, 72) e MMC(48, 72).
</p>

<p>
<b>Solução:</b>
</p>
<ul class="org-ul">
<li>48 = 2⁴ × 3</li>
<li>72 = 2³ × 3²</li>
</ul>

<p>
MDC = 2³ × 3 = 8 × 3 = <b>24</b>
</p>

<p>
MMC = 2⁴ × 3² = 16 × 9 = <b>144</b>
</p>

<p>
<b>Verificação:</b> 24 × 144 = 3456 e 48 × 72 = 3456 ✓
</p>
</div>
</div>

<div id="outline-container-orgea218a8" class="outline-5">
<h5 id="orgea218a8"><span class="section-number-5">1.2.13.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-1-2-13-2">
<p>
Dois sinais luminosos acendem em intervalos de 15 e 20 segundos. Se acendem juntos agora, após quanto tempo voltarão a acender simultaneamente?
</p>

<p>
<b>Solução:</b> MMC(15, 20)
</p>
<ul class="org-ul">
<li>15 = 3 × 5</li>
<li>20 = 2² × 5</li>
<li>MMC = 2² × 3 × 5 = 60</li>
</ul>

<p>
<i>[Ver resposta 11 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orga756a4e" class="outline-5">
<h5 id="orga756a4e"><span class="section-number-5">1.2.13.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-1-2-13-3">
<p>
Determinar o menor número que, dividido por 12, 15 e 20, deixa resto 5.
</p>

<p>
<b>Solução:</b> 1. Calcular MMC(12, 15, 20)
</p>
<ul class="org-ul">
<li>12 = 2² × 3</li>
<li>15 = 3 × 5</li>
<li>20 = 2² × 5</li>
<li>MMC = 2² × 3 × 5 = 60</li>

<li id="2">Como o resto é 5, adicionar 5 ao MMC
<ul class="org-ul">
<li>Número = 60 + 5 = 65</li>
</ul></li>
</ul>

<p>
<i>[Ver resposta 12 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org459a112" class="outline-4">
<h4 id="org459a112"><span class="section-number-4">1.2.14.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-1-2-14">
<ol class="org-ol">
<li><b>Decomposição:</b> Sempre comece pela fatoração em primos</li>
<li>é o método mais confiável</li>
<li><b>MDC:</b> Fatores <b>comuns</b> com <b>menores</b> expoentes</li>
<li><b>MMC:</b> <b>Todos</b> os fatores com <b>maiores</b> expoentes</li>
<li><b>Verificação:</b> Use a relação MDC × MMC = a × b para conferir</li>
<li><b>Problemas:</b> MMC geralmente envolve “encontros” ou “repetições”; MDC envolve “dividir em partes iguais”</li>
<li><b>Primos pequenos:</b> Memorize os primos até 30 (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)</li>
</ol>
</div>
</div>

<div id="outline-container-org331fdc8" class="outline-4">
<h4 id="org331fdc8"><span class="section-number-4">1.2.15.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-1-2-15">
<p>
<b>Divisibilidade:</b>
</p>
<ul class="org-ul">
<li>2: termina em 0, 2, 4, 6, 8</li>
<li>3: soma dos algarismos divisível por 3</li>
<li>5: termina em 0 ou 5</li>
<li>10: termina em 0</li>
</ul>

<p>
<b>MDC e MMC:</b>
</p>
<ul class="org-ul">
<li>MDC: <b>maior</b> divisor <b>comum</b> → fatores comuns com menores expoentes</li>
<li>MMC: <b>menor</b> múltiplo <b>comum</b> → todos os fatores com maiores expoentes</li>
<li>MDC × MMC = a × b</li>
</ul>

<p>
<b>Tipos de problemas:</b>
</p>
<ul class="org-ul">
<li><b>MMC:</b> repetições, encontros, ciclos</li>
<li><b>MDC:</b> divisões iguais, maior tamanho possível</li>
</ul>
</div>
</div>

<div id="outline-container-org7509baf" class="outline-4">
<h4 id="org7509baf"><span class="section-number-4">1.2.16.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-1-2-16">
<pre class="example" id="orgec68d0a">
MDC(a, b) × MMC(a, b) = a × b

MMC(a, b) = (a × b) / MDC(a, b)

MDC(a, b) = (a × b) / MMC(a, b)

Decomposição:
- MDC → fatores COMUNS com MENORES expoentes
- MMC → TODOS os fatores com MAIORES expoentes
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 60 minutos <b>Nível de dificuldade:</b> Fundamental <b>Importância para a prova:</b> ⭐⭐⭐ (importante
</p>
<ul class="org-ul">
<li>frequente em problemas contextualizados)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgb2bc186" class="outline-3">`;

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
