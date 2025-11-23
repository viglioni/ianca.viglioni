<script setup lang="ts">
import { ref } from "vue";

const code = "mat-53";
const title = "Matemática: Trigonometria no Triângulo Retângulo";
const subject = "matemática";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-1">
<ul class="org-ul">
<li>Matemática: Trigonometria no Triângulo Retângulo</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-org7b3e767" class="outline-4">
<h4 id="org7b3e767"><span class="section-number-4">4.1.1.</span> </h4>
<div class="outline-text-4" id="text-4-1-1">
<pre class="example" id="org992eaf4">
    RAZÕES TRIGONOMÉTRICAS
- TRIÂNGULO RETÂNGULO
    
              hipotenusa
                 c
               ╱ │
             ╱   │
           ╱ θ   │ b (cateto oposto)
         ╱       │
       ╱_________│
            a
      (cateto adjacente)
    
    Definições em relação ao ângulo θ:
    
    sen θ = cateto oposto    =  b
            ─────────────       ─
            hipotenusa          c
    
    cos θ = cateto adjacente =  a
            ────────────────    ─
            hipotenusa          c
    
    tan θ = cateto oposto    =  b   = sen θ
            ─────────────       ─     ─────
            cateto adjacente    a     cos θ
    
    
    TRIÂNGULOS NOTÁVEIS:
    
    30°-60°-90°:                 45°-45°-90°:
    
         2                            √2
        ╱│                           ╱│
       ╱ │√3                        ╱ │
      ╱60°│                        ╱45°│ 1
     ╱    │                       ╱    │
    ╱30°__│                      ╱45°__│
       1                            1
    
    sen 30° = 1/2              sen 45° = √2/2
    cos 30° = √3/2             cos 45° = √2/2
    tan 30° = √3/3             tan 45° = 1
    
    sen 60° = √3/2
    cos 60° = 1/2
    tan 60° = √3
    
    
    TABELA TRIGONOMÉTRICA:
    
    ┌───────┬────────┬────────┬────────┐
    │ Ângulo│  sen   │  cos   │  tan   │
    ├───────┼────────┼────────┼────────┤
    │  0°   │   0    │   1    │   0    │
    │ 30°   │  1/2   │  √3/2  │  √3/3  │
    │ 45°   │  √2/2  │  √2/2  │   1    │
    │ 60°   │  √3/2  │  1/2   │   √3   │
    │ 90°   │   1    │   0    │   ∞    │
    └───────┴────────┴────────┴────────┘
    
    Relação Fundamental: sen²θ + cos²θ = 1
</pre>
</div>
</div>

<div id="outline-container-org82293b4" class="outline-4">
<h4 id="org82293b4"><span class="section-number-4">4.1.2.</span> Introdução à Trigonometria</h4>
<div class="outline-text-4" id="text-4-1-2">
<p>
<b>Trigonometria:</b> estudo das relações entre ângulos e lados de triângulos
</p>

<p>
<b>Origem:</b> medição de terras, astronomia, navegação
</p>

<p>
<b>Aplicações:</b> engenharia, física, arquitetura, GPS
</p>
</div>
</div>

<div id="outline-container-org1c5730b" class="outline-4">
<h4 id="org1c5730b"><span class="section-number-4">4.1.3.</span> Triângulo Retângulo</h4>
<div class="outline-text-4" id="text-4-1-3">
<ul class="org-ul">
<li>Revisão</li>
</ul>
<p>
<b>Elementos:</b>
</p>
<ul class="org-ul">
<li><b>Hipotenusa (a):</b> lado oposto ao ângulo reto (maior lado)</li>
<li><b>Catetos (b e c):</b> lados que formam o ângulo reto</li>
<li><b>Ângulos:</b> um ângulo de 90° + dois ângulos agudos</li>
</ul>

<pre class="example" id="org109a9ce">
   C
   |\\
   | \\
b  |  \\ a (hipotenusa)
   |   \\
   |____\\
  A  c  B
</pre>

<p>
<b>Teorema de Pitágoras:</b>
</p>

<pre class="example" id="org7c53501">
a² = b² + c²
</pre>
</div>
</div>

<div id="outline-container-org979964d" class="outline-4">
<h4 id="org979964d"><span class="section-number-4">4.1.4.</span> Razões Trigonométricas</h4>
<div class="outline-text-4" id="text-4-1-4">
<p>
<b>Para um ângulo agudo θ (theta) em um triângulo retângulo:</b>
</p>

<p>
<b>1. Seno (sen θ):</b>
</p>

<pre class="example" id="org0c17aa3">
sen θ = cateto oposto / hipotenusa
sen θ = CO / H
</pre>

<p>
<b>2. Cosseno (cos θ):</b>
</p>

<pre class="example" id="orgeac1898">
cos θ = cateto adjacente / hipotenusa
cos θ = CA / H
</pre>

<p>
<b>3. Tangente (tan θ ou tg θ):</b>
</p>

<pre class="example" id="org37b3df2">
tan θ = cateto oposto / cateto adjacente
tan θ = CO / CA
</pre>

<p>
<b>Mnemônico: SOH-CAH-TOA</b>
</p>
<ul class="org-ul">
<li>*S*eno = *O*posto / *H*ipotenusa</li>
<li>*C*osseno = *A*djacente / *H*ipotenusa</li>
<li>*T*angente = *O*posto / *A*djacente</li>
</ul>
</div>
</div>

<div id="outline-container-org2d8ef6c" class="outline-4">
<h4 id="org2d8ef6c"><span class="section-number-4">4.1.5.</span> Identificando Catetos</h4>
<div class="outline-text-4" id="text-4-1-5">
<p>
<b>Cateto oposto:</b> lado oposto ao ângulo considerado <b>Cateto adjacente:</b> lado ao lado do ângulo (que não é a hipotenusa)
</p>

<p>
<b>Exemplo:</b>
</p>

<pre class="example" id="orge01a902">
   C
   |\\
   | \\
5  |  \\ 13
   |   \\
   |____\\
  A  12  B
</pre>

<p>
Para o ângulo em B:
</p>
<ul class="org-ul">
<li>Cateto oposto = 5 (AC)</li>
<li>Cateto adjacente = 12 (AB)</li>
<li>Hipotenusa = 13</li>
</ul>

<p>
sen B = 5/13 cos B = 12/13 tan B = 5/12
</p>
</div>
</div>

<div id="outline-container-orgfc02dd8" class="outline-4">
<h4 id="orgfc02dd8"><span class="section-number-4">4.1.6.</span> Ângulos Notáveis (30°, 45°, 60°)</h4>
<div class="outline-text-4" id="text-4-1-6">
<p>
<b>Valores para memorizar:</b>
</p>

<pre class="example" id="orgfb0c471">
┌────────┬────────┬────────┬────────┐
│ Ângulo │  Seno  │Cosseno │Tangente│
├────────┼────────┼────────┼────────┤
│  30°   │  1/2   │ √3/2   │ √3/3   │
│  45°   │ √2/2   │ √2/2   │   1    │
│  60°   │ √3/2   │  1/2   │  √3    │
└────────┴────────┴────────┴────────┘
</pre>

<p>
<b>Tabela completa com valores decimais:</b>
</p>

<pre class="example" id="org639e7e6">
┌────────┬────────┬────────┬────────┐
│ Ângulo │  sen   │  cos   │  tan   │
├────────┼────────┼────────┼────────┤
│  30°   │  0,5   │  0,87  │  0,58  │
│  45°   │  0,71  │  0,71  │  1,0   │
│  60°   │  0,87  │  0,5   │  1,73  │
└────────┴────────┴────────┴────────┘
</pre>

<p>
<b>Dica de memorização:</b>
</p>
<ul class="org-ul">
<li><b>sen 30° = 1/2, sen 60° = √3/2</b> (opostos!)</li>
<li><b>cos 30° = √3/2, cos 60° = 1/2</b> (opostos!)</li>
<li><b>sen 45° = cos 45° = √2/2</b> (iguais!)</li>
<li><b>tan 45° = 1</b> (catetos iguais!)</li>
</ul>
</div>
</div>

<div id="outline-container-org4ac7bbc" class="outline-4">
<h4 id="org4ac7bbc"><span class="section-number-4">4.1.7.</span> Triângulos Especiais</h4>
<div class="outline-text-4" id="text-4-1-7">
<p>
<b>Triângulo 30-60-90:</b>
</p>

<pre class="example" id="org97d1ef9">
  60°
  |\\
  | \\
1 |  \\ 2
  |   \\
  |____\\
 30° √3
</pre>

<ul class="org-ul">
<li>Lados na razão 1 : √3 : 2</li>
</ul>

<p>
<b>Triângulo 45-45-90:</b>
</p>

<pre class="example" id="org7ba5874">
  45°
  |\\
  | \\
1 |  \\ √2
  |   \\
  |____\\
 45°  1
</pre>

<ul class="org-ul">
<li>Lados na razão 1 : 1 : √2</li>
</ul>
</div>
</div>

<div id="outline-container-orgd753cb8" class="outline-4">
<h4 id="orgd753cb8"><span class="section-number-4">4.1.8.</span> Relações Fundamentais</h4>
<div class="outline-text-4" id="text-4-1-8">
<p>
<b>1. Relação Fundamental:</b>
</p>

<pre class="example" id="orgac6a624">
sen²θ + cos²θ = 1
</pre>

<p>
<b>2. Tangente em função de seno e cosseno:</b>
</p>

<pre class="example" id="orgd485b2c">
tan θ = sen θ / cos θ
</pre>

<p>
<b>3. Ângulos complementares:</b>
</p>

<pre class="example" id="orgab89451">
sen θ = cos (90°
- θ)
cos θ = sen (90°
- θ)
</pre>

<p>
Exemplo: sen 30° = cos 60° = 0,5
</p>
</div>
</div>

<div id="outline-container-org8cd637c" class="outline-4">
<h4 id="org8cd637c"><span class="section-number-4">4.1.9.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-4-1-9">
</div>
<div id="outline-container-org8f5ae52" class="outline-5">
<h5 id="org8f5ae52"><span class="section-number-5">4.1.9.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-4-1-9-1">
<p>
Em um triângulo retângulo, a hipotenusa mede 10 cm e um dos ângulos mede 30°. Calcule os catetos.
</p>

<p>
<b>Solução:</b> Cateto oposto ao ângulo de 30°: sen 30° = CO / 10 0,5 = CO / 10 CO = 5 cm
</p>

<p>
Cateto adjacente: cos 30° = CA / 10 0,87 = CA / 10 CA = 8,7 cm (ou √3/2 × 10 = 5√3 cm)
</p>

<p>
<i>[Ver resposta 36 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org7d6341a" class="outline-5">
<h5 id="org7d6341a"><span class="section-number-5">4.1.9.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-4-1-9-2">
<p>
(UFMG) Uma escada de 6 m está apoiada em uma parede, formando 60° com o solo. Qual a altura alcançada na parede?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgecc8fb4">
  |
  |\\ 6m
h |  \\
  |   \\
  |____\\
    60°
</pre>

<p>
sen 60° = h / 6 √3/2 = h / 6 h = 6 × √3/2 = 3√3 ≈ 5,2 m
</p>

<p>
<i>[Ver resposta 37 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org2b9344d" class="outline-5">
<h5 id="org2b9344d"><span class="section-number-5">4.1.9.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-4-1-9-3">
<p>
Calcule x no triângulo:
</p>

<pre class="example" id="org258adda">
  |\\
  | \\
8 |  \\ x
  |   \\
  |____\\
   45°
</pre>

<p>
<b>Solução:</b> sen 45° = 8 / x √2/2 = 8 / x x = 8 / (√2/2) = 16/√2 = 16√2/2 = 8√2 cm
</p>

<p>
Ou usando cos: cos 45° = CA / x √2/2 = CA / x Como é 45-45-90, CA = 8 também Pitágoras: x² = 8² + 8² = 128 x = √128 = 8√2 cm
</p>

<p>
<i>[Ver resposta 38 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org94934c1" class="outline-5">
<h5 id="org94934c1"><span class="section-number-5">4.1.9.4.</span> Exercício 4</h5>
<div class="outline-text-5" id="text-4-1-9-4">
<p>
Em um triângulo retângulo, os catetos medem 3 e 4. Calcule o seno do menor ângulo.
</p>

<p>
<b>Solução:</b> Hipotenusa: a² = 3² + 4² = 25 → a = 5
</p>

<p>
Menor ângulo é oposto ao menor cateto (3) sen θ = 3/5 = 0,6
</p>

<p>
<i>[Ver resposta 39 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org6bf10a7" class="outline-5">
<h5 id="org6bf10a7"><span class="section-number-5">4.1.9.5.</span> Exercício 5</h5>
<div class="outline-text-5" id="text-4-1-9-5">
<p>
Calcule tan 30° usando sen e cos.
</p>

<p>
<b>Solução:</b> tan θ = sen θ / cos θ tan 30° = (1/2) / (√3/2) = 1/2 × 2/√3 = 1/√3 = √3/3
</p>

<p>
<i>[Ver resposta 40 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org27f1c9d" class="outline-5">
<h5 id="org27f1c9d"><span class="section-number-5">4.1.9.6.</span> Exercício 6</h5>
<div class="outline-text-5" id="text-4-1-9-6">
<p>
Uma rampa tem 15 m de comprimento e faz 30° com o horizontal. Qual a altura da rampa?
</p>

<p>
<b>Solução:</b> sen 30° = h / 15 0,5 = h / 15 h = 7,5 m
</p>

<p>
<i>[Ver resposta 41 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-orgcde3fb7" class="outline-5">
<h5 id="orgcde3fb7"><span class="section-number-5">4.1.9.7.</span> Exercício 7</h5>
<div class="outline-text-5" id="text-4-1-9-7">
<p>
Sabendo que sen θ = 0,6 e cos θ = 0,8, calcule tan θ.
</p>

<p>
<b>Solução:</b> tan θ = sen θ / cos θ = 0,6 / 0,8 = 0,75
</p>

<p>
Ou: tan θ = 3/5 ÷ 4/5 = 3/4 = 0,75
</p>

<p>
<i>[Ver resposta 42 no final do documento]</i>
</p>
</div>
</div>
</div>

<div id="outline-container-org739c656" class="outline-4">
<h4 id="org739c656"><span class="section-number-4">4.1.10.</span> Aplicações Práticas</h4>
<div class="outline-text-4" id="text-4-1-10">
<p>
<b>1. Construção civil:</b>
</p>
<ul class="org-ul">
<li>Inclinação de telhados</li>
<li>Rampas de acessibilidade</li>
<li>Escadas</li>
</ul>

<p>
<b>2. Navegação:</b>
</p>
<ul class="org-ul">
<li>Determinar distâncias</li>
<li>Calcular altitudes</li>
</ul>

<p>
<b>3. Topografia:</b>
</p>
<ul class="org-ul">
<li>Medição de terrenos</li>
<li>Alturas de montanhas</li>
</ul>

<p>
<b>4. Astronomia:</b>
</p>
<ul class="org-ul">
<li>Distâncias entre corpos celestes</li>
<li>Ângulos de elevação</li>
</ul>
</div>
</div>

<div id="outline-container-org344ecd9" class="outline-4">
<h4 id="org344ecd9"><span class="section-number-4">4.1.11.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-4-1-11">
<ol class="org-ol">
<li><b>SOH-CAH-TOA:</b> memorize!</li>
<li><b>Ângulos notáveis:</b> decore a tabela 30°, 45°, 60°</li>
<li><b>Identifique:</b> qual cateto é oposto? Qual é adjacente?</li>
<li><b>Hipotenusa:</b> sempre o maior lado (oposto ao ângulo de 90°)</li>
<li><b>sen²θ + cos²θ = 1</b> (relação fundamental)</li>
<li><b>tan θ = sen θ / cos θ</b></li>
<li><b>Triângulo 3-4-5:</b> terna pitagórica útil</li>
<li><b>Desenhe o triângulo</b> quando possível</li>
</ol>
</div>
</div>

<div id="outline-container-org72a2f12" class="outline-4">
<h4 id="org72a2f12"><span class="section-number-4">4.1.12.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-4-1-12">
<p>
<b>Razões Trigonométricas:</b>
</p>
<ul class="org-ul">
<li>sen θ = oposto / hipotenusa</li>
<li>cos θ = adjacente / hipotenusa</li>
<li>tan θ = oposto / adjacente</li>
</ul>

<p>
<b>Ângulos Notáveis:</b>
</p>
<ul class="org-ul">
<li>sen 30° = 1/2, cos 30° = √3/2, tan 30° = √3/3</li>
<li>sen 45° = √2/2, cos 45° = √2/2, tan 45° = 1</li>
<li>sen 60° = √3/2, cos 60° = 1/2, tan 60° = √3</li>
</ul>

<p>
<b>Relações:</b>
</p>
<ul class="org-ul">
<li>sen²θ + cos²θ = 1</li>
<li>tan θ = sen θ / cos θ</li>
<li>sen θ = cos (90°</li>
<li>θ)</li>
</ul>
</div>
</div>

<div id="outline-container-orgff89c7b" class="outline-4">
<h4 id="orgff89c7b"><span class="section-number-4">4.1.13.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-1-13">
<pre class="example" id="org1af7901">
Razões Trigonométricas:

sen θ = cateto oposto / hipotenusa
cos θ = cateto adjacente / hipotenusa
tan θ = cateto oposto / cateto adjacente

Relação Fundamental:
sen²θ + cos²θ = 1

Tangente:
tan θ = sen θ / cos θ

Ângulos Complementares:
sen θ = cos (90°
- θ)
cos θ = sen (90°
- θ)

Ângulos Notáveis:
┌────────┬────────┬────────┬────────┐
│   θ    │  sen   │  cos   │  tan   │
├────────┼────────┼────────┼────────┤
│  30°   │  1/2   │ √3/2   │ √3/3   │
│  45°   │ √2/2   │ √2/2   │   1    │
│  60°   │ √3/2   │  1/2   │  √3    │
└────────┴────────┴────────┴────────┘

Teorema de Pitágoras:
a² = b² + c²
(onde a = hipotenusa)
</pre>
</div>
</div>

<div id="outline-container-org9e918b8" class="outline-4">
<h4 id="org9e918b8"><span class="section-number-4">4.1.14.</span> Resumo Visual</h4>
<div class="outline-text-4" id="text-4-1-14">
<pre class="example" id="org2982859">
TRIÂNGULO RETÂNGULO:

       C
       |\\
       | \\
   CO  |  \\ H (hipotenusa)
       |   \\
       |θ___\\
      A  CA  B

sen θ = CO / H
cos θ = CA / H
tan θ = CO / CA

SOH-CAH-TOA:
Seno = Oposto/Hipotenusa
Cosseno = Adjacente/Hipotenusa
Tangente = Oposto/Adjacente

ÂNGULOS NOTÁVEIS:

30°-60°-90°:      45°-45°-90°:
    60°               45°
    |\\                |\\
    | \\               | \\
  1 |  \\ 2          1 |  \\ √2
    |   \\             |   \\
    |____\\            |____\\
   30° √3            45°  1

RELAÇÃO FUNDAMENTAL:
  sen²θ + cos²θ = 1
       ___
      /   \\
     /     \\
   sen²    cos²
    \\_____/
       1
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Médio-Alto <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (essencial
</p>
<ul class="org-ul">
<li>base para trigonometria avançada)</li>
</ul>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgb312386" class="outline-3">`;

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
