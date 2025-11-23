<script setup lang="ts">
import { ref } from "vue";

const code = "qui-59";
const title = "Química: Leis Estequiométricas (Leis Ponderais)";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-5-3">
<ul class="org-ul">
<li>Química: Leis Estequiométricas (Leis Ponderais)</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-orgbac41c8" class="outline-4">
<h4 id="orgbac41c8"><span class="section-number-4">5.3.1.</span> Introdução às Leis Ponderais</h4>
<div class="outline-text-4" id="text-5-3-1">
<p>
<b>Leis ponderais:</b> leis que regem as <b>relações de massa</b> nas reações químicas
</p>

<p>
<b>Período:</b> final do século XVIII / início do século XIX
</p>

<p>
<b>Importância:</b> base da Química moderna, permitiram comprovar a teoria atômica
</p>

<p>
<b>Principais leis:</b> 1. Lei de Lavoisier (Conservação das Massas) 2. Lei de Proust (Proporções Constantes) 3. Lei de Dalton (Proporções Múltiplas)
</p>
</div>
</div>

<div id="outline-container-org73482f3" class="outline-4">
<h4 id="org73482f3"><span class="section-number-4">5.3.2.</span> Lei de Lavoisier (1785)</h4>
<div class="outline-text-4" id="text-5-3-2">
<p>
<b>Antoine Lavoisier (1743-1794):</b> “pai da Química moderna”
</p>

<p>
<b>Enunciado:</b> “Na natureza nada se cria, nada se perde, tudo se transforma.”
</p>

<p>
<b>Forma científica:</b> <b>“A soma das massas dos reagentes é igual à soma das massas dos produtos em um sistema fechado.”</b>
</p>

<pre class="example" id="orge9ab60a">
Σ m_reagentes = Σ m_produtos
</pre>

<p>
<b>Exemplos:</b>
</p>

<p>
<b>Reação: 2 H₂ + O₂ → 2 H₂O</b>
</p>
<ul class="org-ul">
<li>4 g de H₂ + 32 g de O₂ → 36 g de H₂O</li>
<li>4 + 32 = 36 ✓</li>
</ul>

<p>
<b>Reação: Fe + S → FeS</b>
</p>
<ul class="org-ul">
<li>56 g de Fe + 32 g de S → 88 g de FeS</li>
<li>56 + 32 = 88 ✓</li>
</ul>

<p>
<b>Experimento clássico:</b>
</p>

<pre class="example" id="org890fe75">
┌────────────────┐
│  Recipiente    │
│   fechado      │
│                │
│  reagentes ──► produtos │
│                │
└────────────────┘
Massa antes = Massa depois
</pre>

<p>
<b>Observação importante:</b>
</p>
<ul class="org-ul">
<li>Lei válida em <b>sistema fechado</b> (sem troca de matéria)</li>
<li>Em sistema aberto, parece violar (gás escapa, por exemplo)</li>
</ul>

<p>
<b>Aplicação:</b>
</p>
<ul class="org-ul">
<li>Permite calcular massa de reagente ou produto desconhecido</li>
</ul>

<p>
<b>Exemplo:</b> Na reação A + B → C, se 10 g de A reagem com B para formar 18 g de C, qual a massa de B?
</p>

<p>
m_A + m_B = m_C 10 + m_B = 18 m_B = 8 g
</p>
</div>
</div>

<div id="outline-container-org34155d3" class="outline-4">
<h4 id="org34155d3"><span class="section-number-4">5.3.3.</span> Lei de Proust (1797)</h4>
<div class="outline-text-4" id="text-5-3-3">
<p>
<b>Joseph Proust (1754-1826):</b> químico francês
</p>

<p>
<b>Enunciado:</b> <b>“Uma substância pura, qualquer que seja sua origem, apresenta sempre a mesma composição em massa.”</b>
</p>

<p>
<b>Também chamada:</b>
</p>
<ul class="org-ul">
<li>Lei das Proporções Constantes</li>
<li>Lei das Proporções Definidas</li>
</ul>

<p>
<b>Significado:</b>
</p>
<ul class="org-ul">
<li>A <b>proporção</b> entre as massas é sempre a mesma</li>
<li>Não importa a quantidade, a razão é constante</li>
</ul>

<p>
<b>Exemplo 1: Água (H₂O)</b>
</p>

<p>
Síntese da água: 2 H₂ + O₂ → 2 H₂O
</p>

<pre class="example" id="org334802a">
┌───────────┬─────────┬─────────┬─────────┐
│Experimento│  H₂ (g) │  O₂ (g) │ H₂O (g) │
├───────────┼─────────┼─────────┼─────────┤
│     1     │    2    │   16    │   18    │
│     2     │    4    │   32    │   36    │
│     3     │    8    │   64    │   72    │
└───────────┴─────────┴─────────┴─────────┘

Proporção: H₂ : O₂ : H₂O = 2 : 16 : 18 = 1 : 8 : 9
</pre>

<p>
<b>Sempre:</b> 1 g de H₂ reage com 8 g de O₂ para formar 9 g de H₂O
</p>

<p>
<b>Exemplo 2: Gás carbônico (CO₂)</b>
</p>

<p>
C + O₂ → CO₂
</p>

<pre class="example" id="org3d2c056">
┌───────────┬────────┬─────────┬─────────┐
│Experimento│  C (g) │  O₂ (g) │ CO₂ (g) │
├───────────┼────────┼─────────┼─────────┤
│     1     │   3    │    8    │   11    │
│     2     │   6    │   16    │   22    │
│     3     │  12    │   32    │   44    │
└───────────┴────────┴─────────┴─────────┘

Proporção: C : O₂ : CO₂ = 3 : 8 : 11
</pre>

<p>
<b>Sempre:</b> 3 g de C reagem com 8 g de O₂ para formar 11 g de CO₂
</p>

<p>
<b>Aplicação:</b>
</p>
<ul class="org-ul">
<li>Permite calcular massas em qualquer quantidade da reação</li>
<li>Base da estequiometria</li>
</ul>

<p>
<b>Exemplo de cálculo:</b> Se 3 g de C reagem com 8 g de O₂, quantos gramas de C reagem com 24 g de O₂?
</p>

<p>
Proporção: 3 g C / 8 g O₂ = x / 24 g O₂ x = (3 × 24) / 8 = 9 g de C
</p>
</div>
</div>

<div id="outline-container-org6361fee" class="outline-4">
<h4 id="org6361fee"><span class="section-number-4">5.3.4.</span> Lei de Dalton (1803)</h4>
<div class="outline-text-4" id="text-5-3-4">
<p>
<b>John Dalton (1766-1844):</b> químico e físico inglês
</p>

<p>
<b>Enunciado:</b> <b>“Quando dois elementos formam mais de um composto, as massas de um deles que se combinam com uma massa fixa do outro estão em uma razão de números inteiros e pequenos.”</b>
</p>

<p>
<b>Também chamada:</b> Lei das Proporções Múltiplas
</p>

<p>
<b>Contexto:</b>
</p>
<ul class="org-ul">
<li>Alguns elementos formam mais de um composto entre si</li>
<li>Ex: C + O pode formar CO ou CO₂</li>
<li>Ex: N + O pode formar NO, NO₂, N₂O, etc.</li>
</ul>

<p>
<b>Exemplo clássico: CO e CO₂</b>
</p>

<p>
<b>Monóxido de carbono (CO):</b>
</p>
<ul class="org-ul">
<li>12 g de C + 16 g de O → 28 g de CO</li>
<li>Proporção: C : O = 12 : 16 = 3 : 4</li>
</ul>

<p>
<b>Dióxido de carbono (CO₂):</b>
</p>
<ul class="org-ul">
<li>12 g de C + 32 g de O → 44 g de CO₂</li>
<li>Proporção: C : O = 12 : 32 = 3 : 8</li>
</ul>

<p>
<b>Comparando (massa fixa de C = 12 g):</b>
</p>

<pre class="example" id="org3070677">
┌──────────┬────────┬─────────┬────────┐
│ Composto │  C (g) │  O (g)  │  Razão │
├──────────┼────────┼─────────┼────────┤
│   CO     │   12   │   16    │  3:4   │
│   CO₂    │   12   │   32    │  3:8   │
└──────────┴────────┴─────────┴────────┘

Razão entre massas de O: 16 : 32 = 1 : 2 (números inteiros!)
</pre>

<p>
<b>Para massa fixa de C, o oxigênio está na proporção 1:2</b>
</p>

<p>
<b>Outro exemplo: Óxidos de nitrogênio</b>
</p>

<p>
<b>Fixando 14 g de N:</b>
</p>

<p>
<b>NO (monóxido):</b>
</p>
<ul class="org-ul">
<li>14 g N + 16 g O → 30 g NO</li>
</ul>

<p>
<b>NO₂ (dióxido):</b>
</p>
<ul class="org-ul">
<li>14 g N + 32 g O → 46 g NO₂</li>
</ul>

<p>
<b>N₂O (óxido nitroso):</b>
</p>
<ul class="org-ul">
<li>28 g N + 16 g O → 44 g N₂O</li>
<li>Para 14 g N → 14 g N + 8 g O</li>
</ul>

<p>
<b>Razão das massas de O (para 14 g de N):</b>
</p>

<pre class="example" id="orga0d0346">
N₂O : NO : NO₂ = 8 : 16 : 32 = 1 : 2 : 4
</pre>

<p>
<b>Números inteiros e pequenos!</b>
</p>

<p>
<b>Significado:</b>
</p>
<ul class="org-ul">
<li>Comprova a teoria atômica (átomos se combinam em proporções inteiras)</li>
<li>Átomos são indivisíveis nas reações químicas</li>
</ul>
</div>
</div>

<div id="outline-container-orgf0b2db9" class="outline-4">
<h4 id="orgf0b2db9"><span class="section-number-4">5.3.5.</span> Relação entre as Leis</h4>
<div class="outline-text-4" id="text-5-3-5">
<p>
<b>Lei de Lavoisier:</b>
</p>
<ul class="org-ul">
<li>Conservação de massa</li>
<li>Massa total não muda</li>
</ul>

<p>
<b>Lei de Proust:</b>
</p>
<ul class="org-ul">
<li>Proporção constante</li>
<li>Mesma substância, mesma proporção</li>
</ul>

<p>
<b>Lei de Dalton:</b>
</p>
<ul class="org-ul">
<li>Substâncias diferentes entre mesmos elementos</li>
<li>Proporções múltiplas inteiras</li>
</ul>

<p>
<b>Juntas:</b> sustentam a teoria atômica de Dalton
</p>
</div>
</div>

<div id="outline-container-org2e4c004" class="outline-4">
<h4 id="org2e4c004"><span class="section-number-4">5.3.6.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-5-3-6">
</div>
<div id="outline-container-org407eec4" class="outline-5">
<h5 id="org407eec4"><span class="section-number-5">5.3.6.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-5-3-6-1">
<p>
(Lei de Lavoisier) Na reação A + B → C, 20 g de A reagem completamente com B para formar 50 g de C. Qual a massa de B?
</p>

<p>
<b>Solução:</b> m_A + m_B = m_C (Lavoisier) 20 + m_B = 50 m_B = 30 g
</p>

<p>
<i>[Ver resposta 69 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgc922d95" class="outline-5">
<h5 id="orgc922d95"><span class="section-number-5">5.3.6.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-5-3-6-2">
<p>
(Lei de Proust) Na síntese de água, 4 g de H₂ reagem com 32 g de O₂. Quantos gramas de H₂ reagem com 80 g de O₂?
</p>

<p>
<b>Solução:</b> Proporção: 4 g H₂ / 32 g O₂ = x / 80 g O₂
</p>

<p>
x = (4 × 80) / 32 = 320 / 32 = 10 g
</p>

<p>
<i>[Ver resposta 70 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgdef7d7a" class="outline-5">
<h5 id="orgdef7d7a"><span class="section-number-5">5.3.6.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-5-3-6-3">
<p>
(Lei de Proust) Em certa reação, 7 g de A reagem com 8 g de B. Se usarmos 21 g de A, quanto de B será necessário?
</p>

<p>
<b>Solução:</b> Proporção constante (Proust): 7 g A / 8 g B = 21 g A / x
</p>

<p>
x = (8 × 21) / 7 = 24 g
</p>

<p>
<i>[Ver resposta 71 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org370204f" class="outline-5">
<h5 id="org370204f"><span class="section-number-5">5.3.6.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-5-3-6-4">
<p>
(UFMG
</p>
<ul class="org-ul">
<li>Lei de Dalton) O enxofre forma com o oxigênio dois compostos: SO₂ e SO₃. Em SO₂, 32 g de S combinam com 32 g de O. Em SO₃, 32 g de S combinam com 48 g de O. Verifique a Lei de Dalton.</li>
</ul>

<p>
<b>Solução:</b> Massa fixa de S = 32 g
</p>

<p>
Massas de O:
</p>
<ul class="org-ul">
<li>SO₂: 32 g</li>
<li>SO₃: 48 g</li>
</ul>

<p>
Razão: 32 : 48 = 2 : 3 (números inteiros!)
</p>

<p>
<i>[Ver resposta 72 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgb86e124" class="outline-5">
<h5 id="orgb86e124"><span class="section-number-5">5.3.6.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-5-3-6-5">
<p>
(Lei de Lavoisier) Um pedaço de magnésio de 12 g é queimado ao ar, formando 20 g de óxido de magnésio. Qual a massa de oxigênio que reagiu?
</p>

<p>
<b>Solução:</b> Mg + O₂ → MgO
</p>

<p>
m_Mg + m_O₂ = m_MgO 12 + m_O₂ = 20 m_O₂ = 8 g
</p>

<p>
<i>[Ver resposta 73 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org3a1d6a2" class="outline-5">
<h5 id="org3a1d6a2"><span class="section-number-5">5.3.6.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-5-3-6-6">
<p>
(Lei de Proust) Na decomposição de 100 g de carbonato de cálcio (CaCO₃), obtêm-se 56 g de óxido de cálcio (CaO) e 44 g de dióxido de carbono (CO₂). Decompondo 250 g de CaCO₃, quanto de CaO será obtido?
</p>

<p>
<b>Solução:</b> Proporção (Proust): 100 g CaCO₃ → 56 g CaO 250 g CaCO₃ → x
</p>

<p>
x = (56 × 250) / 100 = 140 g
</p>

<p>
<i>[Ver resposta 74 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org1818dcb" class="outline-5">
<h5 id="org1818dcb"><span class="section-number-5">5.3.6.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-5-3-6-7">
<p>
(Aplicação) Carbono e oxigênio formam CO e CO₂. Em CO, 3 g de C combinam com 4 g de O. Em CO₂, 3 g de C combinam com 8 g de O. Qual lei é exemplificada? Verifique.
</p>

<p>
<b>Solução:</b> Massa fixa de C = 3 g Massas de O: 4 g e 8 g Razão: 4 : 8 = 1 : 2 (inteiros!)
</p>

<p>
<i>[Ver resposta 75 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org78cba80" class="outline-4">
<h4 id="org78cba80"><span class="section-number-4">5.3.7.</span> Aplicações das Leis Ponderais</h4>
<div class="outline-text-4" id="text-5-3-7">
<p>
<b>1. Cálculos estequiométricos:</b>
</p>
<ul class="org-ul">
<li>Determinar quantidades de reagentes necessários</li>
<li>Prever quantidade de produtos</li>
</ul>

<p>
<b>2. Controle de qualidade:</b>
</p>
<ul class="org-ul">
<li>Verificar pureza de substâncias</li>
<li>Detectar adulterações</li>
</ul>

<p>
<b>3. Indústria:</b>
</p>
<ul class="org-ul">
<li>Otimizar processos</li>
<li>Reduzir desperdícios</li>
</ul>

<p>
<b>4. Pesquisa:</b>
</p>
<ul class="org-ul">
<li>Identificar substâncias</li>
<li>Determinar fórmulas moleculares</li>
</ul>
</div>
</div>

<div id="outline-container-org571dc59" class="outline-4">
<h4 id="org571dc59"><span class="section-number-4">5.3.8.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-5-3-8">
<ol class="org-ol">
<li><b>Lavoisier:</b> massa reagentes = massa produtos</li>
<li><b>Sistema fechado:</b> essencial para Lavoisier</li>
<li><b>Proust:</b> proporção constante para mesma substância</li>
<li><b>Dalton:</b> proporções inteiras entre compostos diferentes</li>
<li><b>Sempre organize:</b> o que é dado? O que é pedido?</li>
<li><b>Use regra de três</b> para Proust</li>
<li><b>Verifique unidades</b> (todas em gramas?)</li>
<li><b>Massa total conservada</b> (Lavoisier)</li>
</ol>
</div>
</div>

<div id="outline-container-orgdef8740" class="outline-4">
<h4 id="orgdef8740"><span class="section-number-4">5.3.9.</span> Diferenças entre as Leis</h4>
<div class="outline-text-4" id="text-5-3-9">
<pre class="example" id="org5f26456">
┌───────────┬──────────────────────────────────┐
│    Lei    │         O que diz?               │
├───────────┼──────────────────────────────────┤
│ Lavoisier │ Massa se conserva (mesma reação) │
│  Proust   │ Proporção constante (mesma subst)│
│  Dalton   │ Proporções inteiras (subst difer)│
└───────────┴──────────────────────────────────┘
</pre>
</div>
</div>

<div id="outline-container-org4441f13" class="outline-4">
<h4 id="org4441f13"><span class="section-number-4">5.3.10.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-5-3-10">
<p>
<b>Lei de Lavoisier:</b>
</p>
<ul class="org-ul">
<li>“Nada se cria, nada se perde, tudo se transforma”</li>
<li>Σ m_reagentes = Σ m_produtos</li>
<li>Sistema fechado</li>
</ul>

<p>
<b>Lei de Proust:</b>
</p>
<ul class="org-ul">
<li>Proporção constante</li>
<li>Mesma substância, mesma proporção em massa</li>
<li>Permite cálculos por regra de três</li>
</ul>

<p>
<b>Lei de Dalton:</b>
</p>
<ul class="org-ul">
<li>Proporções múltiplas</li>
<li>Massa fixa de um elemento</li>
<li>Razão de números inteiros entre massas do outro</li>
</ul>
</div>
</div>

<div id="outline-container-org14adaaf" class="outline-4">
<h4 id="org14adaaf"><span class="section-number-4">5.3.11.</span> Fórmulas e Relações Essenciais</h4>
<div class="outline-text-4" id="text-5-3-11">
<pre class="example" id="org79b2fff">
Lei de Lavoisier (Conservação das Massas):
Σ m_reagentes = Σ m_produtos

Em uma reação: A + B → C + D
m_A + m_B = m_C + m_D

Lei de Proust (Proporções Constantes):
Para uma substância AB:
m_A / m_B = constante

Exemplo: H₂O
m_H / m_O = 1 / 8 (sempre!)

Lei de Dalton (Proporções Múltiplas):
Para compostos diferentes entre mesmos elementos:
Massa fixa de A, massas de B em razão de inteiros

Exemplo: CO e CO₂ (fixando C)
m_O (em CO) / m_O (em CO₂) = 1/2

Cálculos com Proust:
m₁/m₂ = m₃/m₄

Exemplo:
7 g A / 8 g B = 21 g A / x
x = (8 × 21) / 7 = 24 g
</pre>
</div>
</div>

<div id="outline-container-orgc6f93a3" class="outline-4">
<h4 id="orgc6f93a3"><span class="section-number-4">5.3.12.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-5-3-12">
<pre class="example" id="orgc504bea">
LEIS PONDERAIS:

LAVOISIER (Conservação):
  Reagentes → Produtos
  10g + 5g  →  15g
   └─────┬─────┘
    Massa conservada!

PROUST (Proporções Constantes):
  H₂O sempre:
  H : O = 1 : 8
  
  2g + 16g → 18g  ✓
  4g + 32g → 36g  ✓
  1g +  8g →  9g  ✓

DALTON (Proporções Múltiplas):
  CO:  12g C + 16g O
  CO₂: 12g C + 32g O
        └──┬──┘
       fixo │
            └─► 16:32 = 1:2 (inteiros!)

LINHA DO TEMPO:
1785 ─ Lavoisier (Conservação)
  │
1797 ─ Proust (Proporções Constantes)
  │
1803 ─ Dalton (Proporções Múltiplas)
  │
  └──► Teoria Atômica de Dalton
</pre>
</div>
</div>

<div id="outline-container-org36d7e56" class="outline-4">
<h4 id="org36d7e56"><span class="section-number-4">5.3.13.</span> Resumo Comparativo</h4>
<div class="outline-text-4" id="text-5-3-13">
<pre class="example" id="org18486bd">
┌──────────┬─────────────┬─────────────────────┐
│   Lei    │    Foco     │      Exemplo        │
├──────────┼─────────────┼─────────────────────┤
│Lavoisier │ Conservação │ 10g+5g → 15g        │
│          │             │                     │
│ Proust   │ Proporção   │ H₂O: H:O = 1:8      │
│          │ constante   │ (sempre!)           │
│          │             │                     │
│ Dalton   │ Múltiplas   │ CO/CO₂: O em 1:2    │
│          │ proporções  │ (fixando C)         │
└──────────┴─────────────┴─────────────────────┘
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base da estequiometria e cálculos!)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-org151ea4d" class="outline-3">`;

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
