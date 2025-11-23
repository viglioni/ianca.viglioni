<script setup lang="ts">
import { ref } from "vue";

const code = "fis-22";
const title = "Física: Leis de Newton";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-2">
<ul class="org-ul">
<li>Física: Leis de Newton</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org2f9d4ff" class="outline-4">
<h4 id="org2f9d4ff"><span class="section-number-4">5.2.1.</span> Dinâmica: O Estudo das Forças</h4>
<div class="outline-text-4" id="text-5-2-1">
<p>
<b>Cinemática</b> (estudada anteriormente): descreve o movimento sem se preocupar com suas causas.
</p>

<p>
<b>Dinâmica</b>: estuda as causas do movimento (as forças).
</p>

<p>
<b>Isaac Newton (1643-1727):</b>
</p>
<ul class="org-ul">
<li>Físico e matemático inglês</li>
<li>Publicou “Principia Mathematica” (1687)</li>
<li>Estabeleceu as três leis fundamentais da Dinâmica</li>
</ul>
</div>
</div>

<div id="outline-container-org6dc8e4a" class="outline-4">
<h4 id="org6dc8e4a"><span class="section-number-4">5.2.2.</span> Conceito de Força</h4>
<div class="outline-text-4" id="text-5-2-2">
<p>
<b>Força</b> é uma interação que pode:
</p>
<ul class="org-ul">
<li>Colocar um corpo em movimento</li>
<li>Parar um corpo em movimento</li>
<li>Mudar a direção do movimento</li>
<li>Deformar um corpo</li>
</ul>

<p>
<b>Características da Força (grandeza vetorial):</b>
</p>
<ul class="org-ul">
<li><b>Intensidade (módulo):</b> quão forte é</li>
<li><b>Direção:</b> linha de ação (horizontal, vertical, diagonal)</li>
<li><b>Sentido:</b> para onde aponta (direita/esquerda, cima/baixo)</li>
</ul>

<p>
<b>Unidade SI:</b> Newton (N)
</p>

<p>
<b>1 N</b> = força necessária para acelerar 1 kg a 1 m/s²
</p>

<p>
<b>Representação:</b>
</p>

<pre class="example" id="orgbd3f9d4">
    →
    F
    
Vetor força com:
- Comprimento: intensidade
- Reta: direção
- Seta: sentido
</pre>
</div>
</div>

<div id="outline-container-orgef34fc3" class="outline-4">
<h4 id="orgef34fc3"><span class="section-number-4">5.2.3.</span> 1ª Lei de Newton</h4>
<div class="outline-text-4" id="text-5-2-3">
<ul class="org-ul">
<li>Lei da Inércia</li>
</ul>

<blockquote>
<p>
“Um corpo em repouso tende a permanecer em repouso, e um corpo em movimento tende a permanecer em movimento retilíneo uniforme, a menos que uma força resultante atue sobre ele.”
</p>
</blockquote>

<p>
<b>Inércia:</b> tendência de um corpo em manter seu estado de movimento.
</p>

<p>
<b>Consequências:</b>
</p>
<ul class="org-ul">
<li>Corpo parado permanece parado (sem força resultante)</li>
<li>Corpo em movimento permanece em MRU (sem força resultante)</li>
<li>Massa é medida de inércia (quanto maior a massa, maior a inércia)</li>
</ul>

<p>
<b>Exemplos cotidianos:</b> 1. <b>Freada brusca:</b> passageiros são “jogados” para frente (inércia mantém movimento) 2. <b>Aceleração do carro:</b> passageiros são “pressionados” contra o banco (inércia resiste à mudança) 3. <b>Toalha de mesa puxada:</b> objetos tendem a ficar no lugar (inércia)
</p>

<p>
<b>Referenciais Inerciais:</b>
</p>
<ul class="org-ul">
<li>Sistemas onde a 1ª Lei é válida</li>
<li>Referenciais sem aceleração</li>
<li>Terra: aproximadamente inercial (pequenas acelerações desprezadas)</li>
</ul>

<p>
<b>Força Resultante Nula:</b>
</p>

<pre class="example" id="org7613d3e">
F_R = 0  →  v = constante (MRU ou repouso)
</pre>
</div>
</div>

<div id="outline-container-orgfb50b58" class="outline-4">
<h4 id="orgfb50b58"><span class="section-number-4">5.2.4.</span> 2ª Lei de Newton</h4>
<div class="outline-text-4" id="text-5-2-4">
<ul class="org-ul">
<li>Princípio Fundamental da Dinâmica</li>
</ul>

<blockquote>
<p>
“A força resultante aplicada a um corpo é igual ao produto de sua massa pela aceleração adquirida.”
</p>
</blockquote>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="orgdb0a343">
F_R = m × a
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>F_R: força resultante (N)</li>
<li>m: massa (kg)</li>
<li>a: aceleração (m/s²)</li>
</ul>

<p>
<b>Interpretação:</b>
</p>
<ul class="org-ul">
<li>Força e aceleração têm mesma direção e sentido</li>
<li>Quanto maior a força, maior a aceleração</li>
<li>Quanto maior a massa, menor a aceleração (para mesma força)</li>
</ul>

<p>
<b>Unidade de Força:</b>
</p>

<pre class="example" id="org44dcf0a">
1 N = 1 kg × 1 m/s²
</pre>

<p>
<b>Exemplos:</b>
</p>

<ol class="org-ol">
<li><b>Empurrando um carrinho:</b>
<ul class="org-ul">
<li>m = 10 kg, a = 2 m/s²</li>
<li>F = 10 × 2 = 20 N</li>
</ul></li>
<li><b>Carro acelerando:</b>
<ul class="org-ul">
<li>m = 1000 kg, F = 3000 N</li>
<li>a = F/m = 3000/1000 = 3 m/s²</li>
</ul></li>
</ol>

<p>
<b>Relação Massa-Peso:</b>
</p>
<ul class="org-ul">
<li><b>Massa (m):</b> quantidade de matéria (kg), não varia</li>
<li><b>Peso (P):</b> força gravitacional (N), varia com g</li>
</ul>

<pre class="example" id="org4e786a3">
P = m × g
</pre>

<p>
Na Terra: g ≈ 10 m/s² Pessoa de 60 kg: P = 60 × 10 = 600 N
</p>
</div>
</div>

<div id="outline-container-orgbbdd525" class="outline-4">
<h4 id="orgbbdd525"><span class="section-number-4">5.2.5.</span> 3ª Lei de Newton</h4>
<div class="outline-text-4" id="text-5-2-5">
<ul class="org-ul">
<li>Lei da Ação e Reação</li>
</ul>

<blockquote>
<p>
“Para toda ação existe uma reação de mesma intensidade, mesma direção e sentido contrário.”
</p>
</blockquote>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Ação e reação atuam em <b>corpos diferentes</b></li>
<li>São simultâneas (ocorrem ao mesmo tempo)</li>
<li>Mesma intensidade, mesma direção, sentidos opostos</li>
</ul>

<p>
<b>Exemplos:</b>
</p>

<ol class="org-ol">
<li><b>Livro sobre mesa:</b>
<ul class="org-ul">
<li>Ação: peso do livro sobre a mesa (↓)</li>
<li>Reação: força da mesa sobre o livro (↑)</li>
<li>Corpos diferentes: livro e mesa</li>
</ul></li>
<li><b>Empurrando parede:</b>
<ul class="org-ul">
<li>Ação: você empurra a parede (→)</li>
<li>Reação: parede empurra você (←)</li>
</ul></li>
<li><b>Foguete:</b>
<ul class="org-ul">
<li>Ação: gás expelido para baixo</li>
<li>Reação: foguete impulsionado para cima</li>
</ul></li>
<li><b>Remo no barco:</b>
<ul class="org-ul">
<li>Ação: remo empurra água para trás</li>
<li>Reação: água empurra barco para frente</li>
</ul></li>
</ol>

<p>
<b>IMPORTANTE:</b> Ação e reação NÃO se anulam porque atuam em corpos diferentes!
</p>
</div>
</div>

<div id="outline-container-org0bdb778" class="outline-4">
<h4 id="org0bdb778"><span class="section-number-4">5.2.6.</span> Principais Tipos de Força</h4>
<div class="outline-text-4" id="text-5-2-6">
</div>
<div id="outline-container-orgbd49747" class="outline-5">
<h5 id="orgbd49747"><span class="section-number-5">5.2.6.1.</span> 1. Força Peso (P)</h5>
<div class="outline-text-5" id="text-5-2-6-1">
<p>
Força gravitacional que atrai corpos para o centro da Terra.
</p>

<pre class="example" id="org58ffefd">
P = m × g
</pre>

<ul class="org-ul">
<li><b>Direção:</b> vertical</li>
<li><b>Sentido:</b> para baixo (centro da Terra)</li>
<li><b>Intensidade:</b> P = mg</li>
</ul>
</div>
</div>

<div id="outline-container-orgeaa7d40" class="outline-5">
<h5 id="orgeaa7d40"><span class="section-number-5">5.2.6.2.</span> 2. Força Normal (N)</h5>
<div class="outline-text-5" id="text-5-2-6-2">
<p>
Força de contato perpendicular à superfície.
</p>

<ul class="org-ul">
<li><b>Direção:</b> perpendicular à superfície</li>
<li><b>Sentido:</b> “empurra” o corpo para fora da superfície</li>
<li><b>Intensidade:</b> varia conforme situação</li>
</ul>

<p>
<b>Casos:</b>
</p>

<p>
<b>a) Corpo sobre superfície horizontal (equilíbrio):</b>
</p>

<pre class="example" id="org04186fc">
N = P = mg
</pre>

<p>
<b>b) Corpo em plano inclinado:</b>
</p>

<pre class="example" id="org5449e49">
N = mg × cos(θ)
</pre>

<p>
<b>c) Corpo empurrado contra superfície vertical:</b>
</p>

<pre class="example" id="orgbe19705">
N = F (força aplicada)
</pre>
</div>
</div>

<div id="outline-container-org21ef7c6" class="outline-5">
<h5 id="org21ef7c6"><span class="section-number-5">5.2.6.3.</span> 3. Força de Tração (T)</h5>
<div class="outline-text-5" id="text-5-2-6-3">
<p>
Força transmitida por fios, cordas, cabos.
</p>

<ul class="org-ul">
<li><b>Direção:</b> ao longo do fio</li>
<li><b>Sentido:</b> puxa o corpo</li>
<li><b>Fio ideal:</b> inextensível e de massa desprezível</li>
</ul>
</div>
</div>

<div id="outline-container-org9eba2ee" class="outline-5">
<h5 id="org9eba2ee"><span class="section-number-5">5.2.6.4.</span> 4. Força de Atrito (F_at)</h5>
<div class="outline-text-5" id="text-5-2-6-4">
<p>
Força que se opõe ao movimento relativo entre superfícies em contato.
</p>

<p>
<b>Tipos:</b>
</p>

<p>
<b>a) Atrito Estático (F_at,e):</b>
</p>
<ul class="org-ul">
<li>Corpo em repouso</li>
<li>Impede início do movimento</li>
<li>Varia de 0 até máximo: F_at,e ≤ μ_e × N</li>
</ul>

<p>
<b>b) Atrito Cinético (F_at,c):</b>
</p>
<ul class="org-ul">
<li>Corpo em movimento</li>
<li>Sempre: F_at,c = μ_c × N</li>
</ul>

<p>
<b>Fórmulas:</b>
</p>

<pre class="example" id="orgadec7ff">
F_at,e (máximo) = μ_e × N
F_at,c = μ_c × N
</pre>

<p>
Onde:
</p>
<ul class="org-ul">
<li>μ_e: coeficiente de atrito estático</li>
<li>μ_c: coeficiente de atrito cinético</li>
<li>N: força normal</li>
<li>Geralmente: μ_e &gt; μ_c</li>
</ul>

<p>
<b>Características do atrito:</b>
</p>
<ul class="org-ul">
<li>Sempre oposto ao movimento (ou tendência)</li>
<li>Depende da natureza das superfícies (μ)</li>
<li>Depende da força normal (N)</li>
<li>NÃO depende da área de contato</li>
<li>NÃO depende da velocidade (atrito cinético)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgec75061" class="outline-4">
<h4 id="orgec75061"><span class="section-number-4">5.2.7.</span> Aplicações das Leis de Newton</h4>
<div class="outline-text-4" id="text-5-2-7">
</div>
<div id="outline-container-org0b27865" class="outline-5">
<h5 id="org0b27865"><span class="section-number-5">5.2.7.1.</span> Diagrama de Corpo Livre (DCL)</h5>
<div class="outline-text-5" id="text-5-2-7-1">
<p>
Representação de todas as forças que atuam em um corpo.
</p>

<p>
<b>Passos:</b> 1. Isolar o corpo 2. Representar todas as forças 3. Escolher eixos de referência 4. Aplicar F_R = ma em cada eixo
</p>

<p>
*Exemplo
</p>
<ul class="org-ul">
<li>Bloco sobre mesa:*</li>
</ul>

<pre class="example" id="org766f8fa">
  ↑ N
  |
[bloco]
  |
  ↓ P
</pre>
</div>
</div>

<div id="outline-container-org0896c0c" class="outline-5">
<h5 id="org0896c0c"><span class="section-number-5">5.2.7.2.</span> Problemas Típicos</h5>
<div class="outline-text-5" id="text-5-2-7-2">
<p>
<b>1. Corpo em movimento sobre superfície horizontal:</b>
</p>

<pre class="example" id="org92b7198">
F_R = F_aplicada
- F_atrito
ma = F
- μN
ma = F
- μmg
a = (F
- μmg)/m
</pre>

<p>
<b>2. Plano inclinado sem atrito:</b>
</p>

<pre class="example" id="org16d0517">
a = g × sen(θ)
</pre>

<p>
<b>3. Dois corpos ligados por fio:</b>
</p>
<ul class="org-ul">
<li>Tração é igual em ambos (fio ideal)</li>
<li>Aceleração é igual em ambos (fio inextensível)</li>
<li>Montar equações para cada corpo</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-orgb5160cb" class="outline-4">
<h4 id="orgb5160cb"><span class="section-number-4">5.2.8.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-2-8">
</div>
<div id="outline-container-org0ac7884" class="outline-5">
<h5 id="org0ac7884"><span class="section-number-5">5.2.8.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-2-8-1">
<p>
Um corpo de massa 5 kg está sob ação de uma força resultante de 20 N. Calcule sua aceleração.
</p>

<p>
<b>Solução:</b> F_R = ma 20 = 5a a = 4 m/s²
</p>

<p>
<i>[Ver resposta 85 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org23b24bd" class="outline-5">
<h5 id="org23b24bd"><span class="section-number-5">5.2.8.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-2-8-2">
<p>
Uma pessoa de 70 kg está em um elevador. Calcule a força normal nos casos: a) Elevador em repouso ou MRU b) Elevador subindo com a = 2 m/s² c) Elevador descendo com a = 2 m/s²
</p>

<p>
(Considere g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<ol class="org-ol">
<li>Equilíbrio (a = 0): N</li>
<li>P = 0 N = P = mg = 70 × 10 = 700 N</li>

<li>Subindo acelerado (a = 2 m/s² ↑): F_R = ma (para cima) N</li>
<li>P = ma N = P + ma = 700 + 70(2) = 700 + 140 = 840 N</li>

<li>Descendo acelerado (a = 2 m/s² ↓): F_R = ma (para baixo) P</li>
<li>N = ma N = P</li>
<li>ma = 700</li>
<li>140 = 560 N</li>
</ol>

<p>
<i>[Ver resposta 86 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgdcf13ff" class="outline-5">
<h5 id="orgdcf13ff"><span class="section-number-5">5.2.8.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-2-8-3">
<p>
Um bloco de 10 kg está em repouso sobre uma superfície (μ_e = 0,4, μ_c = 0,3). Aplica-se uma força horizontal de 30 N. O bloco se move? Se sim, qual a aceleração? (g = 10 m/s²)
</p>

<p>
<b>Solução:</b>
</p>

<p>
Força normal: N = P = mg = 10 × 10 = 100 N
</p>

<p>
Atrito estático máximo: F_at,e (máx) = μ_e × N = 0,4 × 100 = 40 N
</p>

<p>
Força aplicada (30 N) &lt; Atrito máximo (40 N)
</p>

<p>
<b>Bloco NÃO se move</b> (atrito segura)
</p>

<p>
<i>[Ver resposta 87 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org60a99c0" class="outline-5">
<h5 id="org60a99c0"><span class="section-number-5">5.2.8.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-2-8-4">
<p>
(Continuação do anterior) Se a força aplicada for 50 N, qual a aceleração?
</p>

<p>
<b>Solução:</b>
</p>

<p>
F_aplicada (50 N) &gt; F_at,e (máx) (40 N) → bloco se move
</p>

<p>
Com movimento, usa atrito cinético: F_at,c = μ_c × N = 0,3 × 100 = 30 N
</p>

<p>
F_R = F_aplicada
</p>
<ul class="org-ul">
<li>F_at,c ma = 50</li>
<li>30 10a = 20 a = 2 m/s²</li>
</ul>

<p>
<i>[Ver resposta 88 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org2a89966" class="outline-5">
<h5 id="org2a89966"><span class="section-number-5">5.2.8.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-2-8-5">
<p>
(UFMG) Um livro está sobre uma mesa. Identifique os pares ação-reação.
</p>

<p>
<b>Solução:</b>
</p>

<p>
<b>Par 1 (peso do livro):</b>
</p>
<ul class="org-ul">
<li>Ação: Terra atrai livro (peso do livro ↓)</li>
<li>Reação: Livro atrai Terra (↑)</li>
</ul>

<p>
<b>Par 2 (contato livro-mesa):</b>
</p>
<ul class="org-ul">
<li>Ação: Livro pressiona mesa (↓)</li>
<li>Reação: Mesa pressiona livro (Normal ↑)</li>
</ul>

<p>
<b>IMPORTANTE:</b> Peso e Normal do livro NÃO são par ação-reação (atuam no mesmo corpo).
</p>
</div>
</div>
</div>

<div id="outline-container-org635e615" class="outline-4">
<h4 id="org635e615"><span class="section-number-4">5.2.9.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-2-9">
<ol class="org-ol">
<li><b>1ª Lei:</b> F_R = 0 → v = constante (MRU ou repouso)</li>
<li><b>2ª Lei:</b> F_R = ma (sempre!)</li>
<li><b>3ª Lei:</b> par ação-reação em corpos diferentes</li>
<li><b>DCL:</b> desenhar TODAS as forças no corpo</li>
<li><b>Peso:</b> sempre mg (para baixo)</li>
<li><b>Normal:</b> perpendicular à superfície</li>
<li><b>Atrito:</b> oposto ao movimento; F_at = μN</li>
<li><b>Ação-reação:</b> mesma intensidade, opostas, corpos diferentes</li>
</ol>
</div>
</div>

<div id="outline-container-org8ae38f8" class="outline-4">
<h4 id="org8ae38f8"><span class="section-number-4">5.2.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-2-10">
<p>
<b>Leis de Newton:</b> 1. <b>Inércia:</b> corpo mantém estado (F_R = 0 → v = cte) 2. <b>F = ma:</b> força causa aceleração 3. <b>Ação-Reação:</b> forças em pares, corpos diferentes
</p>

<p>
<b>Forças:</b>
</p>
<ul class="org-ul">
<li>Peso: P = mg (↓)</li>
<li>Normal: perpendicular à superfície</li>
<li>Tração: ao longo do fio</li>
<li>Atrito: F_at = μN (oposto ao movimento)</li>
</ul>

<p>
<b>Massa vs Peso:</b>
</p>
<ul class="org-ul">
<li>Massa: quantidade de matéria (kg)</li>
<li>Peso: força gravitacional (N), P = mg</li>
</ul>
</div>
</div>

<div id="outline-container-org19f5f3d" class="outline-4">
<h4 id="org19f5f3d"><span class="section-number-4">5.2.11.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-5-2-11">
<pre class="example" id="org5169d4b">
2ª Lei de Newton:
F_R = m × a

Peso:
P = m × g
(Terra: g ≈ 10 m/s²)

Força Normal (horizontal):
N = P = mg

Força de Atrito:
F_at,estático (máx) = μ_e × N
F_at,cinético = μ_c × N

Plano Inclinado (sem atrito):
a = g × sen(θ)
N = mg × cos(θ)

Unidades:
Força: Newton (N)
1 N = 1 kg·m/s²
Massa: kg
Aceleração: m/s²
</pre>
</div>
</div>

<div id="outline-container-orgf96b8e7" class="outline-4">
<h4 id="orgf96b8e7"><span class="section-number-4">5.2.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-2-12">
<pre class="example" id="org6f38578">
Leis de Newton:

1ª LEI (Inércia):
F_R = 0 → [═══→] MRU ou repouso

2ª LEI (F=ma):
  F →    acelera
[bloco]  ───────→ a
  m

3ª LEI (Ação-Reação):
[A] →← [B]
Ação  Reação
(corpos diferentes!)

Diagrama de Corpo Livre:
      ↑ N (normal)
      |
  →F [corpo] F_at←
      |
      ↓ P (peso)

Atrito:
┌──────────┬─────────────────┐
│   Tipo   │    Fórmula      │
├──────────┼─────────────────┤
│ Estático │ F ≤ μ_e × N     │
│ Cinético │ F = μ_c × N     │
└──────────┴─────────────────┘
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base de toda Dinâmica)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org066a717" class="outline-3">`;

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
