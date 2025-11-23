<script setup lang="ts">
import { ref } from "vue";

const code = "qui-77";
const title = "Química: Revisão Geral";
const subject = "química";
const themes = ["Conjuntos"];
const dates = ["2025-11-18"];
const lessonContent = `<div class="outline-text-3" id="text-4-3">
<ul class="org-ul">
<li>Química: Revisão Geral</li>
<li>Todos os Conceitos</li>
<li>90min</li>
</ul>
</div>
<div id="outline-container-org7328440" class="outline-4">
<h4 id="org7328440"><span class="section-number-4">4.3.1.</span> Objetivo da Revisão</h4>
<div class="outline-text-4" id="text-4-3-1">
<p>
Revisão abrangente de TODOS os tópicos de Química: átomos, tabela periódica, ligações, estequiometria e funções.
</p>
</div>
</div>

<div id="outline-container-org5e7e268" class="outline-4">
<h4 id="org5e7e268"><span class="section-number-4">4.3.2.</span> BLOCO 1: Estrutura Atômica e Modelos (15min)</h4>
<div class="outline-text-4" id="text-4-3-2">
<p>
<b>Evolução dos modelos:</b>
</p>

<pre class="example" id="orgd4815d8">
Dalton → Bola maciça
Thomson → Pudim de passas (descobriu e⁻)
Rutherford → Planetário (descobriu núcleo)
Bohr → Níveis de energia (K,L,M,N,O,P,Q)
Atual → Orbitais (probabilidade)
</pre>

<p>
<b>Partículas subatômicas:</b>
</p>

<pre class="example" id="org682f6a6">
Próton (p⁺): carga +1, massa ~1 u, no núcleo
Nêutron (n⁰): carga 0, massa ~1 u, no núcleo
Elétron (e⁻): carga -1, massa ~1/1836 u, eletrosfera
</pre>

<p>
<b>Notação: ᴬᴢX</b>
</p>

<pre class="example" id="orgc0bc293">
Z = número atômico = prótons = elétrons (átomo neutro)
A = número de massa = prótons + nêutrons
N = nêutrons = A
- Z
</pre>

<p>
<b>Isótopos, Isóbaros, Isótonos:</b>
</p>

<pre class="example" id="orgbe87375">
Isótopos: mesmo Z, A diferente (mesmo elemento)
  Ex: ¹²C e ¹⁴C

Isóbaros: mesmo A, Z diferente
  Ex: ⁴⁰K e ⁴⁰Ca

Isótonos: mesmo N (nêutrons)
  Ex: ¹⁴C e ¹⁵N (ambos 7 nêutrons)
</pre>

<p>
<b>Íons:</b>
</p>

<pre class="example" id="orgf4647d2">
Cátion: perde e⁻ (carga +)
  Ex: Na⁺ (perdeu 1 e⁻)

Ânion: ganha e⁻ (carga -)
  Ex: Cl⁻ (ganhou 1 e⁻)
</pre>
</div>
</div>

<div id="outline-container-org85e2f9b" class="outline-4">
<h4 id="org85e2f9b"><span class="section-number-4">4.3.3.</span> BLOCO 2: Tabela Periódica (20min)</h4>
<div class="outline-text-4" id="text-4-3-3">
<pre class="example" id="orgd653317">
    TABELA PERIÓDICA
- ESTRUTURA SIMPLIFICADA
    
    Grupos (colunas verticais): 1 a 18
    Períodos (linhas horizontais): 1 a 7
    
    ┌─────┬──────────────────────────────────────┬───┐
    │  1  │                                      │ 18│
    │ H   │        Grupos 13-17                  │ He│
    ├─────┼────┬─────────────────────────┬───────┼───┤
    │ 2   │ 2  │                         │       │   │
    │Li Be│    │     3  4  5  6  7  8    │   13-17   │
    ├─────┤    │                         │           │
    │ 3   │    │     Metais de           │  p        │
    │Na Mg│    │     Transição           │  Block    │
    ├─────┤    │     (grupos 3-12)       │           │
    │ 4   │    │                         │           │
    │K Ca │    │                         │           │
    ├─────┤    │                         │           │
    │ 5-7 │    │                         │           │
    │ ... │    │                         │           │
    └─────┴────┴─────────────────────────┴───────────┘
    
    FAMÍLIAS IMPORTANTES:
    • Grupo 1 (IA): Metais Alcalinos (Li, Na, K...)
    • Grupo 2 (IIA): Metais Alcalino-Terrosos (Be, Mg, Ca...)
    • Grupo 13 (IIIA): Família do Boro
    • Grupo 14 (IVA): Família do Carbono
    • Grupo 15 (VA): Família do Nitrogênio
    • Grupo 16 (VIA): Calcogênios (O, S...)
    • Grupo 17 (VIIA): Halogênios (F, Cl, Br, I...)
    • Grupo 18 (VIIIA): Gases Nobres (He, Ne, Ar...)
    
    ORGANIZAÇÃO:
    • Número atômico (Z): número de prótons
    • Período = número de camadas eletrônicas
    • Grupo = número de elétrons na camada de valência
    
    PROPRIEDADES PERIÓDICAS:
    → Aumenta →
    ┌────────────────┐
    │ Raio Atômico   │ ↓ Aumenta ↓
    │ Eletronegat.   │
    │ Energia Ioniz. │
    └────────────────┘
</pre>

<p>
<b>Organização:</b>
</p>

<pre class="example" id="orge0b551d">
7 períodos (linhas) = número de camadas eletrônicas
18 grupos (colunas) = propriedades semelhantes
</pre>

<p>
<b>Famílias principais:</b>
</p>

<pre class="example" id="orgbf9449b">
Grupo 1: Metais Alcalinos (Li, Na, K, Rb, Cs, Fr)
  - 1 e⁻ na camada de valência
  - Muito reativos

Grupo 2: Metais Alcalino-Terrosos (Be, Mg, Ca, Sr, Ba, Ra)
  - 2 e⁻ na camada de valência

Grupo 13: Família do Boro (B, Al, Ga, In, Tl)
Grupo 14: Família do Carbono (C, Si, Ge, Sn, Pb)
Grupo 15: Família do Nitrogênio (N, P, As, Sb, Bi)

Grupo 16: Calcogênios (O, S, Se, Te, Po)
  - 6 e⁻ na camada de valência

Grupo 17: Halogênios (F, Cl, Br, I, At)
  - 7 e⁻ na camada de valência
  - Muito reativos

Grupo 18: Gases Nobres (He, Ne, Ar, Kr, Xe, Rn)
  - 8 e⁻ na camada de valência (completa!)
  - Inertes (não reagem)
</pre>

<p>
<b>Classificação:</b>
</p>

<pre class="example" id="org866593b">
Metais: maioria, lado esquerdo e centro
  - Brilhantes, condutores, maleáveis

Não-metais (ametais): lado direito superior
  - C, N, O, P, S, Se, F, Cl, Br, I

Semimetais: B, Si, Ge, As, Sb, Te, Po, At
  - Propriedades intermediárias
</pre>

<p>
<b>Propriedades Periódicas:</b>
</p>

<pre class="example" id="orgc4769f1">
RAIO ATÔMICO:
↑ Na família (mais camadas)
← No período (mais prótons, mais atração)

ENERGIA DE IONIZAÇÃO:
↓ Na família (e⁻ mais afastados)
→ No período (mais atração nuclear)

ELETRONEGATIVIDADE:
↓ Na família
→ No período

Mais eletronegativo: F (flúor)
Ordem: F &gt; O &gt; N &gt; Cl

Menos eletronegativo: Fr (frâncio)
</pre>
</div>
</div>

<div id="outline-container-orgc8ddd11" class="outline-4">
<h4 id="orgc8ddd11"><span class="section-number-4">4.3.4.</span> BLOCO 3: Ligações Químicas (15min)</h4>
<div class="outline-text-4" id="text-4-3-4">
<p>
<b>Regra do Octeto:</b>
</p>

<pre class="example" id="orgb44979a">
Átomos tendem a ter 8 e⁻ na camada de valência
(exceto H e He: 2 e⁻)
</pre>

<p>
<b>Ligação Iônica:</b>
</p>

<pre class="example" id="org5ef918c">
Metal + Não-metal
Transferência de e⁻
Cátion + Ânion
Alta temperatura de fusão
Conduz eletricidade quando fundido ou em solução

Exemplos: NaCl, CaO, MgCl₂
</pre>

<p>
<b>Ligação Covalente:</b>
</p>

<pre class="example" id="org754c73f">
Não-metal + Não-metal
Compartilhamento de e⁻
Moléculas
Temperatura de fusão mais baixa

Exemplos: H₂, O₂, H₂O, CO₂, CH₄
</pre>

<p>
<b>Ligação Metálica:</b>
</p>

<pre class="example" id="org0e42a2b">
Metal + Metal
"Mar de elétrons"
Conduz eletricidade e calor
Maleável, dúctil

Exemplos: Fe, Cu, Al, Au, Ag
</pre>
</div>
</div>

<div id="outline-container-orgd4cab16" class="outline-4">
<h4 id="orgd4cab16"><span class="section-number-4">4.3.5.</span> BLOCO 4: Estequiometria (25min)</h4>
<div class="outline-text-4" id="text-4-3-5">
<p>
<b>Conceito de Mol:</b>
</p>

<pre class="example" id="org3590175">
1 mol = 6,02 × 10²³ entidades

Constante de Avogadro:
Nᴀ = 6,02 × 10²³ /mol
</pre>

<p>
<b>Massa Molar (M):</b>
</p>

<pre class="example" id="orgf6887f5">
Massa de 1 mol
Unidade: g/mol
Valor numérico = massa atômica/molecular
</pre>

<p>
<b>Relações fundamentais:</b>
</p>

<pre class="example" id="org7e51147">
n = m/M        (número de mols)
m = n × M      (massa)
N = n × Nᴀ     (número de partículas)
V = n × 22,4 L (volume em CNTP)
</pre>

<p>
<b>Leis Ponderais:</b>
</p>

<pre class="example" id="orga0b5972">
Lavoisier (Conservação das Massas):
  m_reagentes = m_produtos
  "Nada se cria, nada se perde"

Proust (Proporções Constantes):
  Mesma substância, mesma proporção

Dalton (Proporções Múltiplas):
  Compostos diferentes, proporções inteiras
</pre>

<p>
<b>Cálculos estequiométricos:</b>
</p>

<p>
<b>Tipo 1: Massa → Massa</b>
</p>

<pre class="example" id="orgc55a668">
Exemplo: N₂ + 3H₂ → 2NH₃
Quantos g de NH₃ a partir de 28 g de N₂?

M(N₂) = 28 g/mol, M(NH₃) = 17 g/mol

1 mol N₂ : 2 mol NH₃
28 g N₂ : 34 g NH₃

28 g N₂ produz 34 g NH₃
</pre>

<p>
<b>Tipo 2: Volume → Volume (CNTP)</b>
</p>

<pre class="example" id="org8ece199">
Proporção volumétrica = proporção molar

N₂ + 3H₂ → 2NH₃
1 volume : 3 volumes : 2 volumes

30 L H₂ produz quantos L de NH₃?
3 L : 2 L
30 L : x
x = 20 L NH₃
</pre>
</div>
</div>

<div id="outline-container-org6f586d8" class="outline-4">
<h4 id="org6f586d8"><span class="section-number-4">4.3.6.</span> BLOCO 5: Funções Inorgânicas (10min)</h4>
<div class="outline-text-4" id="text-4-3-6">
<p>
<b>Ácidos:</b>
</p>

<pre class="example" id="orgb5d1745">
Liberam H⁺ em água
pH &lt; 7
Azeda papel tornassol azul

Exemplos:
HCl
- ácido clorídrico
H₂SO₄
- ácido sulfúrico
HNO₃
- ácido nítrico
H₃PO₄
- ácido fosfórico
</pre>

<p>
<b>Bases:</b>
</p>

<pre class="example" id="org3df32b3">
Liberam OH⁻ em água
pH &gt; 7
Avermelha fenolftaleína

Exemplos:
NaOH
- hidróxido de sódio
Ca(OH)₂
- hidróxido de cálcio
NH₄OH
- hidróxido de amônio
</pre>

<p>
<b>Sais:</b>
</p>

<pre class="example" id="org6978cd9">
Cátion + Ânion
Produto de neutralização (ácido + base)

Exemplos:
NaCl
- cloreto de sódio
K₂SO₄
- sulfato de potássio
CaCO₃
- carbonato de cálcio
</pre>

<p>
<b>Óxidos:</b>
</p>

<pre class="example" id="org014d958">
Elemento + Oxigênio

Exemplos:
CO₂
- dióxido de carbono
H₂O
- água (óxido de hidrogênio)
Fe₂O₃
- óxido de ferro III
</pre>

<p>
<b>pH e pOH:</b>
</p>

<pre class="example" id="orgd672246">
pH &lt; 7: ácido
pH = 7: neutro
pH &gt; 7: básico

pH + pOH = 14
</pre>
</div>
</div>

<div id="outline-container-orgc00d6f4" class="outline-4">
<h4 id="orgc00d6f4"><span class="section-number-4">4.3.7.</span> BLOCO 6: Separação de Misturas (5min)</h4>
<div class="outline-text-4" id="text-4-3-7">
<pre class="example" id="orgb783801">
Filtração: sólido + líquido (retenção em filtro)
Decantação: líquidos imiscíveis ou sólido + líquido
Destilação simples: líquido + sólido dissolvido
Destilação fracionada: líquidos miscíveis (PEs diferentes)
Centrifugação: acelera separação sólido + líquido
Evaporação: líquido volátil + sólido
</pre>
</div>
</div>

<div id="outline-container-org0fe7280" class="outline-4">
<h4 id="org0fe7280"><span class="section-number-4">4.3.8.</span> Problemas Mistos</h4>
<div class="outline-text-4" id="text-4-3-8">
<ul class="org-ul">
<li>Treino Final</li>
</ul>
</div>
<div id="outline-container-org60d4fb4" class="outline-5">
<h5 id="org60d4fb4"><span class="section-number-5">4.3.8.1.</span> Problema 1</h5>
<div class="outline-text-5" id="text-4-3-8-1">
<p>
Quantos nêutrons tem ³⁹₁₉K?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgfced4d0">
N = A
- Z = 39
- 19 = 20 nêutrons
</pre>
</div>
</div>

<div id="outline-container-orge5f8ed8" class="outline-5">
<h5 id="orge5f8ed8"><span class="section-number-5">4.3.8.2.</span> Problema 2</h5>
<div class="outline-text-5" id="text-4-3-8-2">
<p>
Qual mais eletronegativo: F ou Cl?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgb8bec7f">
F (flúor)
- está mais acima no grupo 17
F &gt; Cl
</pre>
</div>
</div>

<div id="outline-container-org7ffc58c" class="outline-5">
<h5 id="org7ffc58c"><span class="section-number-5">4.3.8.3.</span> Problema 3</h5>
<div class="outline-text-5" id="text-4-3-8-3">
<p>
Que tipo de ligação forma NaCl?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org9250492">
Na = metal
Cl = não-metal
Ligação IÔNICA
</pre>
</div>
</div>

<div id="outline-container-org31e8669" class="outline-5">
<h5 id="org31e8669"><span class="section-number-5">4.3.8.4.</span> Problema 4</h5>
<div class="outline-text-5" id="text-4-3-8-4">
<p>
Quantos mols há em 180 g de H₂O? (M = 18 g/mol)
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="org4582b2c">
n = m/M = 180/18 = 10 mols
</pre>
</div>
</div>

<div id="outline-container-orgdeb1aa6" class="outline-5">
<h5 id="orgdeb1aa6"><span class="section-number-5">4.3.8.5.</span> Problema 5</h5>
<div class="outline-text-5" id="text-4-3-8-5">
<p>
Na reação 2H₂ + O₂ → 2H₂O, se 4 g de H₂ reagem, quantos g de H₂O se formam?
</p>

<p>
<b>Solução:</b>
</p>

<pre class="example" id="orgf8e28f5">
M(H₂) = 2 g/mol, M(H₂O) = 18 g/mol

2 mol H₂ : 2 mol H₂O
4 g H₂ : 36 g H₂O

4 g H₂ produz 36 g H₂O
</pre>
</div>
</div>
</div>

<div id="outline-container-orgaad4d02" class="outline-4">
<h4 id="orgaad4d02"><span class="section-number-4">4.3.9.</span> Dados para Memorizar</h4>
<div class="outline-text-4" id="text-4-3-9">
<p>
<b>Massas atômicas:</b>
</p>

<pre class="example" id="org162af8d">
H = 1    C = 12   N = 14   O = 16
Na = 23  Cl = 35,5   Ca = 40   S = 32
</pre>

<p>
<b>Massas molares comuns:</b>
</p>

<pre class="example" id="org2495543">
H₂O = 18 g/mol
CO₂ = 44 g/mol
NaCl = 58,5 g/mol
O₂ = 32 g/mol
H₂ = 2 g/mol
</pre>

<p>
<b>Constantes:</b>
</p>

<pre class="example" id="org7455531">
Nᴀ = 6,02 × 10²³ /mol
V_molar (CNTP) = 22,4 L/mol
</pre>
</div>
</div>

<div id="outline-container-orgeaaa2bd" class="outline-4">
<h4 id="orgeaaa2bd"><span class="section-number-4">4.3.10.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-4-3-10">
<ul class="org-ul">
<li>RESUMO COMPLETO</li>
</ul>
<pre class="example" id="org3e5f8f0">
ESTRUTURA ATÔMICA:
Z = prótons
A = Z + N
N = A
- Z

ESTEQUIOMETRIA:
n = m/M
m = n × M
N = n × Nᴀ
V = n × 22,4 L (CNTP)

Leis:
Lavoisier: m_reagentes = m_produtos
Proust: proporção constante
Dalton: proporções múltiplas

pH:
pH + pOH = 14
pH &lt; 7: ácido
pH = 7: neutro
pH &gt; 7: básico

PROPRIEDADES PERIÓDICAS:
Raio: ↑ família, ← período
E. ionização: ↓ família, → período
Eletronegatividade: ↓ família, → período
Mais eletronegativo: F
</pre>
</div>
</div>

<div id="outline-container-org4765697" class="outline-4">
<h4 id="org4765697"><span class="section-number-4">4.3.11.</span> Checklist Final</h4>
<div class="outline-text-4" id="text-4-3-11">
<ul class="org-ul">
<li>Química</li>
<li class="off"><code>[&#xa0;]</code> Sei a evolução dos modelos atômicos</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular número de nêutrons (N = A</li>
<li>Z)</li>
<li class="off"><code>[&#xa0;]</code> Sei diferenciar isótopos, isóbaros, isótonos</li>
<li class="off"><code>[&#xa0;]</code> Conheço as principais famílias da tabela periódica</li>
<li class="off"><code>[&#xa0;]</code> Sei as tendências das propriedades periódicas</li>
<li class="off"><code>[&#xa0;]</code> Sei que F é o mais eletronegativo</li>
<li class="off"><code>[&#xa0;]</code> Sei diferenciar ligações iônica, covalente e metálica</li>
<li class="off"><code>[&#xa0;]</code> Sei calcular número de mols (n = m/M)</li>
<li class="off"><code>[&#xa0;]</code> Sei fazer cálculos estequiométricos</li>
<li class="off"><code>[&#xa0;]</code> Sei as três leis ponderais</li>
<li class="off"><code>[&#xa0;]</code> Sei classificar ácidos, bases, sais e óxidos</li>
<li class="off"><code>[&#xa0;]</code> Sei a relação pH + pOH = 14</li>
<li class="off"><code>[&#xa0;]</code> Memorizei massas molares comuns</li>
</ul>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 90 minutos <b>Nível de dificuldade:</b> Médio-Alto (revisão abrangente) <b>Importância para a prova:</b> ⭐⭐⭐⭐⭐ (TODO o conteúdo!)
</p>

<hr />
</div>
</div>
</div>

<div id="outline-container-orgbfc14ce" class="outline-3">`;

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
