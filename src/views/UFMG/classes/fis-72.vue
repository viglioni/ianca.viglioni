<script setup lang="ts">
import { ref } from "vue";

const code = "fis-72";
const title = "Física: Revisão Final";
const subject = "física";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-3-3">
<ul class="org-ul">
<li>Física: Revisão Final</li>
<li>Cinemática e Dinâmica</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org4f305f9" class="outline-4">
<h4 id="org4f305f9"><span class="section-number-4">3.3.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-3-3-1">
<p>
Consolidar movimento uniforme, uniformemente variado e Leis de Newton.
</p>
</div>
</div>

<div id="outline-container-org616649f" class="outline-4">
<h4 id="org616649f"><span class="section-number-4">3.3.2.</span> PARTE 1: Cinemática</h4>
<div class="outline-text-4" id="text-3-3-2">
<ul class="org-ul">
<li>Conceitos Fundamentais</li>
</ul>
<p>
<b>Posição (S):</b> localização do móvel
</p>
<ul class="org-ul">
<li>Unidade: m (metros)</li>
</ul>

<p>
<b>Deslocamento (ΔS):</b>
</p>

<pre class="example" id="org264611d">
ΔS = S_final
- S_inicial
</pre>

<p>
<b>Velocidade (v):</b>
</p>

<pre class="example" id="org23836df">
v = ΔS / Δt
Unidade: m/s (SI) ou km/h
</pre>

<p>
<b>Conversão:</b>
</p>

<pre class="example" id="org1bcd2ee">
km/h → m/s: dividir por 3,6
m/s → km/h: multiplicar por 3,6

Exemplo: 72 km/h = 72/3,6 = 20 m/s
</pre>

<p>
<b>Aceleração (a):</b>
</p>

<pre class="example" id="org28ed761">
a = Δv / Δt
Unidade: m/s²
</pre>
</div>
</div>

<div id="outline-container-orgb9e6fb7" class="outline-4">
<h4 id="orgb9e6fb7"><span class="section-number-4">3.3.3.</span> PARTE 2: Movimento Retilíneo Uniforme (MRU)</h4>
<div class="outline-text-4" id="text-3-3-3">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Velocidade constante (v = cte)</li>
<li>Aceleração nula (a = 0)</li>
<li>Trajetória reta</li>
</ul>

<p>
<b>Função horária:</b>
</p>

<pre class="example" id="org2ff2ff3">
S = S₀ + vt

Onde:
S = posição final
S₀ = posição inicial
v = velocidade (constante)
t = tempo
</pre>

<p>
<b>Gráficos:</b>
</p>

<p>
<b>S × t:</b> reta inclinada
</p>
<ul class="org-ul">
<li>Inclinação = velocidade</li>
</ul>

<p>
<b>v × t:</b> reta horizontal
</p>
<ul class="org-ul">
<li>Área = deslocamento</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgb4ead1f">
Um carro parte de S₀ = 10 m com v = 15 m/s.
Onde estará após 4 segundos?

S = 10 + 15(4) = 10 + 60 = 70 m
</pre>
</div>
</div>

<div id="outline-container-org306f5e2" class="outline-4">
<h4 id="org306f5e2"><span class="section-number-4">3.3.4.</span> PARTE 3: Movimento Retilíneo Uniformemente Variado (MRUV)</h4>
<div class="outline-text-4" id="text-3-3-4">
<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Aceleração constante (a = cte)</li>
<li>Velocidade varia linearmente</li>
<li>Trajetória reta</li>
</ul>

<p>
<b>Equações:</b>
</p>

<p>
<b>1. Velocidade:</b>
</p>

<pre class="example" id="org7c6107b">
v = v₀ + at
</pre>

<p>
<b>2. Posição (Sorvetão):</b>
</p>

<pre class="example" id="org25fe0a8">
S = S₀ + v₀t + (at²)/2
</pre>

<p>
<b>3. Torricelli (sem tempo):</b>
</p>

<pre class="example" id="orgd14ab40">
v² = v₀² + 2aΔS
</pre>

<p>
<b>Onde:</b>
</p>
<ul class="org-ul">
<li>S = posição final</li>
<li>S₀ = posição inicial</li>
<li>v = velocidade final</li>
<li>v₀ = velocidade inicial</li>
<li>a = aceleração</li>
<li>t = tempo</li>
<li>ΔS = deslocamento</li>
</ul>

<p>
<b>Exemplo completo:</b>
</p>

<p>
Um carro a 10 m/s acelera a 2 m/s² por 5 segundos. Calcule:
</p>

<p>
<b>a) Velocidade final:</b>
</p>

<pre class="example" id="orgaaae8b9">
v = v₀ + at = 10 + 2(5) = 10 + 10 = 20 m/s
</pre>

<p>
<b>b) Deslocamento:</b>
</p>

<pre class="example" id="org76f6d3c">
ΔS = v₀t + at²/2 = 10(5) + 2(5)²/2
ΔS = 50 + 2(25)/2 = 50 + 25 = 75 m
</pre>

<p>
<b>Ou por Torricelli:</b>
</p>

<pre class="example" id="orgd3323f5">
v² = v₀² + 2aΔS
20² = 10² + 2(2)ΔS
400 = 100 + 4ΔS
ΔS = 300/4 = 75 m ✓
</pre>
</div>
</div>

<div id="outline-container-orgf6ad31f" class="outline-4">
<h4 id="orgf6ad31f"><span class="section-number-4">3.3.5.</span> PARTE 4: Queda Livre e Lançamento Vertical</h4>
<div class="outline-text-4" id="text-3-3-5">
<p>
<b>Queda Livre:</b>
</p>
<ul class="org-ul">
<li>Movimento vertical</li>
<li>v₀ = 0 (solto do repouso)</li>
<li>a = g = 10 m/s² (para baixo)</li>
</ul>

<p>
<b>Equações:</b>
</p>

<pre class="example" id="orge5876f7">
v = gt
h = gt²/2
v² = 2gh
</pre>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgb346d8c">
Objeto cai de 80 m. Com que velocidade chega ao chão?

v² = 2gh = 2(10)(80) = 1600
v = 40 m/s
</pre>

<p>
<b>Lançamento Vertical para Cima:</b>
</p>
<ul class="org-ul">
<li>v₀ &gt; 0</li>
<li>a = −g = −10 m/s² (contra o movimento)</li>
<li>Altura máxima: v = 0</li>
</ul>

<p>
<b>Altura máxima:</b>
</p>

<pre class="example" id="orga16fa38">
h_máx = v₀² / (2g)
</pre>

<p>
<b>Tempo de subida:</b>
</p>

<pre class="example" id="orgba818c3">
t_subida = v₀ / g
</pre>

<p>
<b>Tempo total (subida + descida):</b>
</p>

<pre class="example" id="org44ecbe3">
t_total = 2v₀ / g
</pre>
</div>
</div>

<div id="outline-container-org6318319" class="outline-4">
<h4 id="org6318319"><span class="section-number-4">3.3.6.</span> PARTE 5: Dinâmica</h4>
<div class="outline-text-4" id="text-3-3-6">
<ul class="org-ul">
<li>Leis de Newton</li>
</ul>
<p>
<b>1ª Lei (Inércia):</b> “Todo corpo permanece em repouso ou em movimento retilíneo uniforme, a menos que seja obrigado a mudar por forças aplicadas.”
</p>

<p>
<b>Consequência:</b>
</p>
<ul class="org-ul">
<li>Sem força resultante → velocidade constante</li>
<li>F_R = 0 → a = 0</li>
</ul>

<p>
<b>2ª Lei (Fundamental):</b>
</p>

<pre class="example" id="orgb257ad4">
F_R = m · a

Onde:
F_R = força resultante (N)
m = massa (kg)
a = aceleração (m/s²)
</pre>

<p>
<b>Unidade de força:</b> Newton (N)
</p>

<pre class="example" id="org9623485">
1 N = 1 kg · m/s²
</pre>

<p>
<b>Importante:</b>
</p>
<ul class="org-ul">
<li>Força e aceleração têm mesma direção e sentido</li>
<li>Maior massa → menor aceleração (mesma força)</li>
</ul>

<p>
<b>3ª Lei (Ação e Reação):</b> “Para toda ação há uma reação de mesma intensidade, mesma direção e sentido oposto.”
</p>

<p>
<b>Características:</b>
</p>
<ul class="org-ul">
<li>Agem em corpos diferentes</li>
<li>Não se anulam</li>
<li>São simultâneas</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>Empurrar parede → parede empurra de volta</li>
<li>Foguete expele gases → gases empurram foguete</li>
</ul>
</div>
</div>

<div id="outline-container-org33cee0f" class="outline-4">
<h4 id="org33cee0f"><span class="section-number-4">3.3.7.</span> PARTE 6: Força Peso</h4>
<div class="outline-text-4" id="text-3-3-7">
<p>
<b>Definição:</b> força da gravidade sobre um corpo
</p>

<p>
<b>Fórmula:</b>
</p>

<pre class="example" id="org4d54f5e">
P = m · g

Onde:
P = peso (N)
m = massa (kg)
g = gravidade (≈ 10 m/s²)
</pre>

<p>
<b>Importante:</b>
</p>
<ul class="org-ul">
<li>Peso é FORÇA (medida em N)</li>
<li>Massa é quantidade de matéria (medida em kg)</li>
<li>Peso varia com g, massa não</li>
</ul>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orgd994bcd">
Massa: 60 kg
Na Terra (g = 10 m/s²): P = 60 × 10 = 600 N
Na Lua (g = 1,6 m/s²): P = 60 × 1,6 = 96 N
</pre>
</div>
</div>

<div id="outline-container-org266ae72" class="outline-4">
<h4 id="org266ae72"><span class="section-number-4">3.3.8.</span> PARTE 7: Força Normal e Atrito</h4>
<div class="outline-text-4" id="text-3-3-8">
<p>
<b>Força Normal (N):</b>
</p>
<ul class="org-ul">
<li>Perpendicular à superfície</li>
<li>Reação da superfície ao contato</li>
</ul>

<p>
<b>Em superfície horizontal:</b>
</p>

<pre class="example" id="orgb266d72">
N = P = mg
</pre>

<p>
<b>Força de Atrito (F_at):</b>
</p>

<p>
<b>Atrito estático:</b> impede início do movimento
</p>

<pre class="example" id="org807438c">
F_at ≤ μ_e · N
</pre>

<p>
<b>Atrito cinético:</b> atua durante o movimento
</p>

<pre class="example" id="org3c80781">
F_at = μ_c · N

Onde:
μ = coeficiente de atrito (sem unidade)
</pre>

<p>
<b>Importante:</b>
</p>
<ul class="org-ul">
<li>Atrito sempre opõe-se ao movimento</li>
<li>μ_estático &gt; μ_cinético (mais difícil tirar do repouso)</li>
</ul>
</div>
</div>

<div id="outline-container-org19ca81f" class="outline-4">
<h4 id="org19ca81f"><span class="section-number-4">3.3.9.</span> Questões de Fixação</h4>
<div class="outline-text-4" id="text-3-3-9">
</div>
<div id="outline-container-org540b103" class="outline-5">
<h5 id="org540b103"><span class="section-number-5">3.3.9.1.</span> Questão 1</h5>
<div class="outline-text-5" id="text-3-3-9-1">
<p>
Um móvel em MRU parte de S₀ = 20 m com v = 5 m/s. Onde está em t = 6 s?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org4bf06ec">
S = 20 + 5(6) = 20 + 30 = 50 m
</pre>
</div>
</div>

<div id="outline-container-orga59c5d5" class="outline-5">
<h5 id="orga59c5d5"><span class="section-number-5">3.3.9.2.</span> Questão 2</h5>
<div class="outline-text-5" id="text-3-3-9-2">
<p>
Um carro freia de 20 m/s para 0 m/s em 4 s. Qual a aceleração?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orgc0d9124">
a = Δv/Δt = (0
- 20)/4 = -20/4 = -5 m/s²
(negativa = freando)
</pre>
</div>
</div>

<div id="outline-container-orgb6f515e" class="outline-5">
<h5 id="orgb6f515e"><span class="section-number-5">3.3.9.3.</span> Questão 3</h5>
<div class="outline-text-5" id="text-3-3-9-3">
<p>
Objeto cai por 3 s. Qual a velocidade final? (g = 10 m/s²)
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="orga86e41b">
v = gt = 10(3) = 30 m/s
</pre>
</div>
</div>

<div id="outline-container-orge5975f6" class="outline-5">
<h5 id="orge5975f6"><span class="section-number-5">3.3.9.4.</span> Questão 4</h5>
<div class="outline-text-5" id="text-3-3-9-4">
<p>
Calcule o peso de uma pessoa de 80 kg. (g = 10 m/s²)
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org3521db4">
P = mg = 80 × 10 = 800 N
</pre>
</div>
</div>

<div id="outline-container-org98c1a5c" class="outline-5">
<h5 id="org98c1a5c"><span class="section-number-5">3.3.9.5.</span> Questão 5</h5>
<div class="outline-text-5" id="text-3-3-9-5">
<p>
Uma força de 50 N atua em um corpo de 10 kg. Qual a aceleração?
</p>

<p>
<b>Resposta:</b>
</p>

<pre class="example" id="org86b88e5">
F = ma
50 = 10a
a = 5 m/s²
</pre>
</div>
</div>
</div>

<div id="outline-container-org0b7b3bc" class="outline-4">
<h4 id="org0b7b3bc"><span class="section-number-4">3.3.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-3-3-10">
<ul class="org-ul">
<li>Resumo</li>
</ul>
<pre class="example" id="orgd256d76">
CONCEITOS:
v = ΔS/Δt
a = Δv/Δt

Conversão: km/h ↔ m/s (÷ ou × 3,6)

MRU:
S = S₀ + vt

MRUV:
v = v₀ + at
S = S₀ + v₀t + at²/2
v² = v₀² + 2aΔS

QUEDA LIVRE (v₀ = 0):
v = gt
h = gt²/2
v² = 2gh

LANÇAMENTO VERTICAL:
h_máx = v₀²/(2g)
t_subida = v₀/g

DINÂMICA:
F_R = ma  (2ª Lei)
P = mg  (Peso)
F_at = μN  (Atrito)

DADOS:
g = 10 m/s²
</pre>
</div>
</div>

<div id="outline-container-org756510f" class="outline-4">
<h4 id="org756510f"><span class="section-number-4">3.3.11.</span> Checklist de Revisão</h4>
<div class="outline-text-4" id="text-3-3-11">
<ul class="org-ul">
<li class="off"><code>[&#xa0;]</code> Sei a fórmula do MRU e resolver problemas</li>
<li class="off"><code>[&#xa0;]</code> Sei as 3 equações do MRUV</li>
<li class="off"><code>[&#xa0;]</code> Sei quando usar cada equação do MRUV</li>
<li class="off"><code>[&#xa0;]</code> Sei resolver problemas de queda livre</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular altura máxima em lançamento vertical</li>
<li class="off"><code>[&#xa0;]</code> Sei as 3 Leis de Newton</li>
<li class="off"><code>[&#xa0;]</code> Sei aplicar F = ma</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular peso (P = mg)</li>
<li class="off"><code>[&#xa0;]</code> Sei a diferença entre massa e peso</li>
<li class="off"><code>[&#xa0;]</code> Sei converter km/h ↔ m/s</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio (revisão) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (sempre cai!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-org9043a1d" class="outline-3">`;

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
