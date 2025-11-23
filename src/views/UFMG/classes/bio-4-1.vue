<script setup lang="ts">
import { ref } from "vue";

const code = "bio-4-1";
const title = "Matemática: Conjuntos";
const subject = "biologia";
const themes = ["Célula"];
const dates = ["2025-12-09"];
const lessonContent = `<div class="outline-text-3" id="text-1-1">
<ul class="org-ul">
<li>Matemática: Conjuntos</li>
<li>120min</li>
</ul>
</div>
<div id="outline-container-org5db5c3b" class="outline-4">
<h4 id="org5db5c3b"><span class="section-number-4">1.1.1.</span> O que são Conjuntos?</h4>
<div class="outline-text-4" id="text-1-1-1">
<p>
Um <b>conjunto</b> é uma coleção de objetos distintos, chamados de <b>elementos</b>. Os conjuntos são fundamentais na matemática e servem como base para diversos outros conceitos.
</p>

<p>
<b>Notação:</b>
</p>
<ul class="org-ul">
<li>Conjuntos são representados por letras maiúsculas: A, B, C, etc.</li>
<li>Elementos são representados por letras minúsculas: a, b, c, etc.</li>
<li>Usamos chaves { } para listar os elementos</li>
</ul>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3, 4, 5}</li>
<li>B = {a, e, i, o, u}</li>
<li>C = {2, 4, 6, 8, 10}</li>
</ul>
</div>
</div>

<div id="outline-container-org511c500" class="outline-4">
<h4 id="org511c500"><span class="section-number-4">1.1.2.</span> Relação de Pertinência</h4>
<div class="outline-text-4" id="text-1-1-2">
<p>
Usamos os símbolos <b>∈</b> (pertence) e <b>∉</b> (não pertence) para indicar se um elemento faz parte de um conjunto.
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>3 ∈ A (3 pertence ao conjunto A)</li>
<li>7 ∉ A (7 não pertence ao conjunto A)</li>
<li>e ∈ B (e pertence ao conjunto B)</li>
</ul>
</div>
</div>

<div id="outline-container-org2574a54" class="outline-4">
<h4 id="org2574a54"><span class="section-number-4">1.1.3.</span> Conjuntos Numéricos Fundamentais</h4>
<div class="outline-text-4" id="text-1-1-3">
</div>
<div id="outline-container-orge934aad" class="outline-5">
<h5 id="orge934aad"><span class="section-number-5">1.1.3.1.</span> ℕ</h5>
<div class="outline-text-5" id="text-1-1-3-1">
<ul class="org-ul">
<li>Números Naturais</li>
</ul>
<p>
ℕ = {0, 1, 2, 3, 4, 5, &#x2026;}
</p>
<ul class="org-ul">
<li>Números inteiros não-negativos</li>
<li>Usados para contar</li>
<li>ℕ* = {1, 2, 3, 4, &#x2026;} (naturais sem o zero)</li>
</ul>
</div>
</div>

<div id="outline-container-org1f66470" class="outline-5">
<h5 id="org1f66470"><span class="section-number-5">1.1.3.2.</span> ℤ</h5>
<div class="outline-text-5" id="text-1-1-3-2">
<ul class="org-ul">
<li>Números Inteiros</li>
</ul>
<p>
ℤ = {&#x2026;, -3, -2, -1, 0, 1, 2, 3, &#x2026;}
</p>
<ul class="org-ul">
<li>Incluem os naturais e seus negativos</li>
<li>ℤ* = ℤ</li>
<li>{0} (inteiros sem o zero)</li>
<li>ℤ₊ = {0, 1, 2, 3, &#x2026;} (inteiros não-negativos)</li>
<li>ℤ₋ = {&#x2026;, -3, -2, -1, 0} (inteiros não-positivos)</li>
</ul>
</div>
</div>

<div id="outline-container-org21b692c" class="outline-5">
<h5 id="org21b692c"><span class="section-number-5">1.1.3.3.</span> ℚ</h5>
<div class="outline-text-5" id="text-1-1-3-3">
<ul class="org-ul">
<li>Números Racionais</li>
</ul>
<p>
ℚ = {p/q | p ∈ ℤ, q ∈ ℤ*}
</p>
<ul class="org-ul">
<li>Números que podem ser escritos como fração</li>
<li>Incluem decimais finitos e dízimas periódicas</li>
<li>Exemplos: 1/2, 0,5, 3,333&#x2026;, -2/3</li>
</ul>
</div>
</div>

<div id="outline-container-orgb49a91a" class="outline-5">
<h5 id="orgb49a91a"><span class="section-number-5">1.1.3.4.</span> 𝕀</h5>
<div class="outline-text-5" id="text-1-1-3-4">
<ul class="org-ul">
<li>Números Irracionais</li>
<li>Números que <b>NÃO</b> podem ser escritos como fração</li>
<li>Decimais infinitos e não-periódicos</li>
<li>Exemplos: π, √2, √3, e (número de Euler)</li>
</ul>
</div>
</div>

<div id="outline-container-org77c1586" class="outline-5">
<h5 id="org77c1586"><span class="section-number-5">1.1.3.5.</span> ℝ</h5>
<div class="outline-text-5" id="text-1-1-3-5">
<ul class="org-ul">
<li>Números Reais</li>
</ul>
<p>
ℝ = ℚ ∪ 𝕀
</p>
<ul class="org-ul">
<li>União de todos os números racionais e irracionais</li>
<li>Representam todos os pontos da reta numérica</li>
</ul>

<p>
<b>Diagrama de inclusão:</b>
</p>

<pre class="example" id="org174b3cc">
ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
</pre>
</div>
</div>
</div>

<div id="outline-container-org972f472" class="outline-4">
<h4 id="org972f472"><span class="section-number-4">1.1.4.</span> Tipos de Conjuntos Especiais</h4>
<div class="outline-text-4" id="text-1-1-4">
</div>
<div id="outline-container-org2545910" class="outline-5">
<h5 id="org2545910"><span class="section-number-5">1.1.4.1.</span> Conjunto Vazio</h5>
<div class="outline-text-5" id="text-1-1-4-1">
<ul class="org-ul">
<li>Conjunto sem elementos</li>
<li>Notação: ∅ ou { }</li>
<li>Exemplo: A = {x ∈ ℕ | x &lt; 0} = ∅</li>
</ul>
</div>
</div>

<div id="outline-container-org8dd36cd" class="outline-5">
<h5 id="org8dd36cd"><span class="section-number-5">1.1.4.2.</span> Conjunto Unitário</h5>
<div class="outline-text-5" id="text-1-1-4-2">
<ul class="org-ul">
<li>Conjunto com apenas um elemento</li>
<li>Exemplo: B = {5}</li>
</ul>
</div>
</div>

<div id="outline-container-orge37a5b4" class="outline-5">
<h5 id="orge37a5b4"><span class="section-number-5">1.1.4.3.</span> Conjunto Universo (U)</h5>
<div class="outline-text-5" id="text-1-1-4-3">
<ul class="org-ul">
<li>Conjunto que contém todos os elementos relevantes para um problema</li>
<li>Varia conforme o contexto</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org8db2533" class="outline-4">
<h4 id="org8db2533"><span class="section-number-4">1.1.5.</span> Subconjuntos</h4>
<div class="outline-text-4" id="text-1-1-5">
<p>
Um conjunto A é <b>subconjunto</b> de B (A ⊆ B) se todos os elementos de A também pertencem a B.
</p>

<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>Todo conjunto é subconjunto de si mesmo: A ⊆ A</li>
<li>O conjunto vazio é subconjunto de qualquer conjunto: ∅ ⊆ A</li>
<li>Se A ⊆ B e B ⊆ A, então A = B</li>
</ul>

<p>
<b>Subconjunto próprio:</b>
</p>
<ul class="org-ul">
<li>A ⊂ B significa que A ⊆ B e A ≠ B</li>
<li>Todos os elementos de A estão em B, mas B tem pelo menos um elemento que não está em A</li>
</ul>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3}</li>
<li>B = {1, 2, 3, 4, 5}</li>
<li>A ⊂ B (A é subconjunto próprio de B)</li>
</ul>
</div>
</div>

<div id="outline-container-org3e521f8" class="outline-4">
<h4 id="org3e521f8"><span class="section-number-4">1.1.6.</span> Operações entre Conjuntos</h4>
<div class="outline-text-4" id="text-1-1-6">
</div>
<div id="outline-container-org764ee80" class="outline-5">
<h5 id="org764ee80"><span class="section-number-5">1.1.6.1.</span> União (∪)</h5>
<div class="outline-text-5" id="text-1-1-6-1">
<p>
A união de A e B é o conjunto formado por elementos que pertencem a A <b>ou</b> a B (ou ambos).
</p>

<p>
<b>Notação:</b> A ∪ B = {x | x ∈ A ou x ∈ B}
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3}</li>
<li>B = {3, 4, 5}</li>
<li>A ∪ B = {1, 2, 3, 4, 5}</li>
</ul>

<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>A ∪ ∅ = A</li>
<li>A ∪ A = A</li>
<li>A ∪ B = B ∪ A (comutativa)</li>
</ul>
</div>
</div>

<div id="outline-container-org34a39ca" class="outline-5">
<h5 id="org34a39ca"><span class="section-number-5">1.1.6.2.</span> Interseção (∩)</h5>
<div class="outline-text-5" id="text-1-1-6-2">
<p>
A interseção de A e B é o conjunto formado por elementos que pertencem a A <b>e</b> a B simultaneamente.
</p>

<p>
<b>Notação:</b> A ∩ B = {x | x ∈ A e x ∈ B}
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3, 4}</li>
<li>B = {3, 4, 5, 6}</li>
<li>A ∩ B = {3, 4}</li>
</ul>

<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>A ∩ ∅ = ∅</li>
<li>A ∩ A = A</li>
<li>A ∩ B = B ∩ A (comutativa)</li>
</ul>

<p>
<b>Conjuntos disjuntos:</b>
</p>
<ul class="org-ul">
<li>Quando A ∩ B = ∅, dizemos que A e B são disjuntos</li>
</ul>
</div>
</div>

<div id="outline-container-orgdaef757" class="outline-5">
<h5 id="orgdaef757"><span class="section-number-5">1.1.6.3.</span> Diferença (−)</h5>
<div class="outline-text-5" id="text-1-1-6-3">
<p>
A diferença entre A e B é o conjunto dos elementos que pertencem a A mas <b>não</b> pertencem a B.
</p>

<p>
<b>Notação:</b> A − B = {x | x ∈ A e x ∉ B}
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3, 4, 5}</li>
<li>B = {3, 4, 5, 6, 7}</li>
<li>A − B = {1, 2}</li>
<li>B − A = {6, 7}</li>
</ul>

<p>
<b>Observação:</b> A − B ≠ B − A (não é comutativa)
</p>
</div>
</div>

<div id="outline-container-orgb8f971c" class="outline-5">
<h5 id="orgb8f971c"><span class="section-number-5">1.1.6.4.</span> Complementar (Aᶜ ou A')</h5>
<div class="outline-text-5" id="text-1-1-6-4">
<p>
O complementar de A em relação ao conjunto universo U é o conjunto de elementos que pertencem a U mas não pertencem a A.
</p>

<p>
<b>Notação:</b> Aᶜ = U − A = {x | x ∈ U e x ∉ A}
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}</li>
<li>A = {2, 4, 6, 8, 10}</li>
<li>Aᶜ = {1, 3, 5, 7, 9}</li>
</ul>

<p>
<b>Propriedades:</b>
</p>
<ul class="org-ul">
<li>(Aᶜ)ᶜ = A</li>
<li>A ∪ Aᶜ = U</li>
<li>A ∩ Aᶜ = ∅</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org12e7171" class="outline-4">
<h4 id="org12e7171"><span class="section-number-4">1.1.7.</span> Diagrama de Venn</h4>
<div class="outline-text-4" id="text-1-1-7">
<p>
Diagramas de Venn são representações visuais de conjuntos usando círculos ou elipses.
</p>

<pre class="example" id="orgb81af4d">
        DIAGRAMA DE VENN
- DOIS CONJUNTOS
        
           U (Universo)
    ┌─────────────────────────────────┐
    │                                 │
    │      ╭───────╮   ╭───────╮     │
    │     ╱         ╲ ╱         ╲    │
    │    │     A     X     B     │   │
    │    │           │           │   │
    │     ╲         ╱ ╲         ╱    │
    │      ╰───────╯   ╰───────╯     │
    │                                 │
    └─────────────────────────────────┘
    
    Legenda:
    • Região A apenas: A
- B (A ∩ B̄)
    • Região B apenas: B
- A (Ā ∩ B)
    • Interseção X: A ∩ B
    • União: A ∪ B (tudo dentro dos círculos)
    • Complemento: Fora dos círculos
</pre>

<p>
<b>Usos:</b>
</p>
<ul class="org-ul">
<li>Visualizar operações entre conjuntos</li>
<li>Resolver problemas de contagem</li>
<li>Compreender relações entre conjuntos</li>
</ul>

<p>
<b>Exemplo de problema:</b>
</p>
<ul class="org-ul">
<li>Em uma turma de 40 alunos:</li>
<li>25 estudam Inglês</li>
<li>20 estudam Espanhol</li>
<li>10 estudam ambas as línguas</li>
<li>Quantos não estudam nenhuma das duas?</li>
</ul>

<p>
<b>Solução usando Venn:</b>
</p>
<ul class="org-ul">
<li>Apenas Inglês: 25</li>
<li>10 = 15</li>
<li>Apenas Espanhol: 20</li>
<li>10 = 10</li>
<li>Ambas: 10</li>
<li>Nenhuma: 40</li>
<li>(15 + 10 + 10) = 5</li>
</ul>
</div>
</div>

<div id="outline-container-org7d14c96" class="outline-4">
<h4 id="org7d14c96"><span class="section-number-4">1.1.8.</span> Intervalos Numéricos</h4>
<div class="outline-text-4" id="text-1-1-8">
<p>
Intervalos são subconjuntos especiais dos números reais, definidos por desigualdades.
</p>
</div>

<div id="outline-container-org64d2a7c" class="outline-5">
<h5 id="org64d2a7c"><span class="section-number-5">1.1.8.1.</span> Intervalo Fechado [a, b]</h5>
<div class="outline-text-5" id="text-1-1-8-1">
<ul class="org-ul">
<li>[a, b] = {x ∈ ℝ | a ≤ x ≤ b}</li>
<li>Inclui os extremos a e b</li>
<li>Representação gráfica: ●━━━━━●</li>
</ul>
</div>
</div>

<div id="outline-container-org973d266" class="outline-5">
<h5 id="org973d266"><span class="section-number-5">1.1.8.2.</span> Intervalo Aberto (a, b)</h5>
<div class="outline-text-5" id="text-1-1-8-2">
<ul class="org-ul">
<li>(a, b) = {x ∈ ℝ | a &lt; x &lt; b}</li>
<li>Não inclui os extremos</li>
<li>Representação gráfica: ○━━━━━○</li>
</ul>
</div>
</div>

<div id="outline-container-org85990e3" class="outline-5">
<h5 id="org85990e3"><span class="section-number-5">1.1.8.3.</span> Intervalo Fechado-Aberto [a, b)</h5>
<div class="outline-text-5" id="text-1-1-8-3">
<ul class="org-ul">
<li>[a, b) = {x ∈ ℝ | a ≤ x &lt; b}</li>
<li>Inclui a, não inclui b</li>
<li>Representação gráfica: ●━━━━━○</li>
</ul>
</div>
</div>

<div id="outline-container-org175923a" class="outline-5">
<h5 id="org175923a"><span class="section-number-5">1.1.8.4.</span> Intervalo Aberto-Fechado (a, b]</h5>
<div class="outline-text-5" id="text-1-1-8-4">
<ul class="org-ul">
<li>(a, b] = {x ∈ ℝ | a &lt; x ≤ b}</li>
<li>Não inclui a, inclui b</li>
<li>Representação gráfica: ○━━━━━●</li>
</ul>

<pre class="example" id="orgbb7eeee">
    REPRESENTAÇÃO DE INTERVALOS NA RETA NUMÉRICA

    [a, b]
- Intervalo Fechado (inclui ambos extremos)
    ────●═══════════●────────────────────────────
        a           b
    
    (a, b)
- Intervalo Aberto (exclui ambos extremos)
    ────○───────────○────────────────────────────
        a           b
    
    [a, b)
- Fechado à esquerda, Aberto à direita
    ────●═══════════○────────────────────────────
        a           b
    
    (a, b]
- Aberto à esquerda, Fechado à direita
    ────○───────────●────────────────────────────
        a           b
    
    [a, +∞)
- Intervalo ilimitado à direita
    ────●═══════════════════════════════════════→
        a
    
    (-∞, b]
- Intervalo ilimitado à esquerda
    ←═══════════════●────────────────────────────
                    b
    
    Símbolos: ● = inclui ponto    ○ = exclui ponto
              ═ = pertence        ─ = não pertence
</pre>
</div>
</div>

<div id="outline-container-org41bcbb9" class="outline-5">
<h5 id="org41bcbb9"><span class="section-number-5">1.1.8.5.</span> Intervalos Infinitos</h5>
<div class="outline-text-5" id="text-1-1-8-5">
<ul class="org-ul">
<li>[a, +∞) = {x ∈ ℝ | x ≥ a}</li>
<li>(a, +∞) = {x ∈ ℝ | x &gt; a}</li>
<li>(−∞, b] = {x ∈ ℝ | x ≤ b}</li>
<li>(−∞, b) = {x ∈ ℝ | x &lt; b}</li>
<li>(−∞, +∞) = ℝ</li>
</ul>

<p>
<b>Observação:</b> Infinito nunca é incluído, por isso sempre usamos parênteses
</p>
</div>
</div>
</div>

<div id="outline-container-org27e0344" class="outline-4">
<h4 id="org27e0344"><span class="section-number-4">1.1.9.</span> Operações com Intervalos</h4>
<div class="outline-text-4" id="text-1-1-9">
</div>
<div id="outline-container-orgf7c773c" class="outline-5">
<h5 id="orgf7c773c"><span class="section-number-5">1.1.9.1.</span> União de intervalos</h5>
<div class="outline-text-5" id="text-1-1-9-1">
<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A = [1, 5]</li>
<li>B = [3, 8]</li>
<li>A ∪ B = [1, 8]</li>
</ul>

<p>
<b>Intervalos disjuntos:</b>
</p>
<ul class="org-ul">
<li>C = [1, 3]</li>
<li>D = [5, 7]</li>
<li>C ∪ D = [1, 3] ∪ [5, 7] (união não forma intervalo único)</li>
</ul>
</div>
</div>

<div id="outline-container-org2db0118" class="outline-5">
<h5 id="org2db0118"><span class="section-number-5">1.1.9.2.</span> Interseção de intervalos</h5>
<div class="outline-text-5" id="text-1-1-9-2">
<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>A = [1, 5]</li>
<li>B = [3, 8]</li>
<li>A ∩ B = [3, 5]</li>
</ul>

<p>
<b>Intervalos disjuntos:</b>
</p>
<ul class="org-ul">
<li>C = [1, 3]</li>
<li>D = [5, 7]</li>
<li>C ∩ D = ∅</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org97e1639" class="outline-4">
<h4 id="org97e1639"><span class="section-number-4">1.1.10.</span> Cardinalidade</h4>
<div class="outline-text-4" id="text-1-1-10">
<p>
A <b>cardinalidade</b> de um conjunto é o número de elementos que ele possui.
</p>

<p>
<b>Notação:</b> n(A) ou |A| ou #A
</p>

<p>
<b>Exemplos:</b>
</p>
<ul class="org-ul">
<li>A = {1, 2, 3, 4, 5} → n(A) = 5</li>
<li>B = {a, e, i, o, u} → n(B) = 5</li>
<li>∅ → n(∅) = 0</li>
</ul>
</div>

<div id="outline-container-org458f67d" class="outline-5">
<h5 id="org458f67d"><span class="section-number-5">1.1.10.1.</span> Fórmula para União de Conjuntos</h5>
<div class="outline-text-5" id="text-1-1-10-1">
<p>
Para dois conjuntos A e B:
</p>

<p>
<b>n(A ∪ B) = n(A) + n(B) − n(A ∩ B)</b>
</p>

<p>
<b>Exemplo:</b>
</p>
<ul class="org-ul">
<li>n(A) = 30</li>
<li>n(B) = 25</li>
<li>n(A ∩ B) = 10</li>
<li>n(A ∪ B) = 30 + 25 − 10 = 45</li>
</ul>
</div>
</div>

<div id="outline-container-org0cb3d8c" class="outline-5">
<h5 id="org0cb3d8c"><span class="section-number-5">1.1.10.2.</span> Fórmula para Três Conjuntos</h5>
<div class="outline-text-5" id="text-1-1-10-2">
<p>
<b>n(A ∪ B ∪ C) = n(A) + n(B) + n(C) − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) + n(A ∩ B ∩ C)</b>
</p>
</div>
</div>
</div>

<div id="outline-container-orge453fc0" class="outline-4">
<h4 id="orge453fc0"><span class="section-number-4">1.1.11.</span> Exercícios Resolvidos</h4>
<div class="outline-text-4" id="text-1-1-11">
</div>
<div id="outline-container-orgb6d6cb3" class="outline-5">
<h5 id="orgb6d6cb3"><span class="section-number-5">1.1.11.1.</span> Exercício 1</h5>
<div class="outline-text-5" id="text-1-1-11-1">
<p>
Dados os conjuntos A = {1, 2, 3, 4, 5} e B = {4, 5, 6, 7, 8}, determine:
</p>

<ol class="org-ol">
<li>A ∪ B <i>[Ver resposta 1 no final do documento]</i></li>

<li>A ∩ B <i>[Ver resposta 2 no final do documento]</i></li>

<li>A − B <i>[Ver resposta 3 no final do documento]</i></li>

<li>B − A <i>[Ver resposta 4 no final do documento]</i></li>
</ol>
</div>
</div>

<div id="outline-container-org8fae0ee" class="outline-5">
<h5 id="org8fae0ee"><span class="section-number-5">1.1.11.2.</span> Exercício 2</h5>
<div class="outline-text-5" id="text-1-1-11-2">
<p>
Em uma escola com 100 alunos:
</p>
<ul class="org-ul">
<li>60 praticam futebol</li>
<li>50 praticam vôlei</li>
<li>30 praticam ambos</li>
<li>Quantos não praticam nenhum dos dois esportes?</li>
</ul>

<p>
<b>Solução:</b>
</p>
<ul class="org-ul">
<li>Apenas futebol: 60 − 30 = 30</li>
<li>Apenas vôlei: 50 − 30 = 20</li>
<li>Ambos: 30</li>
<li>Total que pratica algum esporte: 30 + 20 + 30 = 80</li>
<li>Nenhum esporte: 100 − 80 = 20</li>
</ul>

<p>
<i>[Ver resposta 5 no final do documento]</i>
</p>
</div>
</div>

<div id="outline-container-org91e5dfc" class="outline-5">
<h5 id="org91e5dfc"><span class="section-number-5">1.1.11.3.</span> Exercício 3</h5>
<div class="outline-text-5" id="text-1-1-11-3">
<p>
Escreva os intervalos na forma de conjunto e represente na reta:
</p>

<ol class="org-ol">
<li>[−2, 5] <i>[Ver resposta 6 no final do documento]</i></li>

<li>(3, +∞) <i>[Ver resposta 7 no final do documento]</i></li>

<li>(−∞, 1] <i>[Ver resposta 8 no final do documento]</i></li>
</ol>
</div>
</div>
</div>

<div id="outline-container-orgfd54b2c" class="outline-4">
<h4 id="orgfd54b2c"><span class="section-number-4">1.1.12.</span> Dicas para a Prova</h4>
<div class="outline-text-4" id="text-1-1-12">
<ol class="org-ol">
<li><b>Leia com atenção</b> se o intervalo é aberto ou fechado</li>
<li><b>Use diagramas de Venn</b> para problemas de contagem</li>
<li><b>Lembre-se das propriedades</b> das operações</li>
<li><b>Cuidado com o conjunto vazio</b></li>
<li>é subconjunto de todos os conjuntos</li>
<li><b>Na fórmula da união</b>, não esqueça de subtrair a interseção para evitar contar elementos duas vezes</li>
</ol>
</div>
</div>

<div id="outline-container-org6f93663" class="outline-4">
<h4 id="org6f93663"><span class="section-number-4">1.1.13.</span> Conceitos-Chave para Memorizar</h4>
<div class="outline-text-4" id="text-1-1-13">
<ul class="org-ul">
<li><b>Pertinência:</b> ∈ (elemento pertence ao conjunto)</li>
<li><b>Inclusão:</b> ⊆ (conjunto está contido em outro)</li>
<li><b>União:</b> ∪ (elementos em A <b>ou</b> B)</li>
<li><b>Interseção:</b> ∩ (elementos em A <b>e</b> B)</li>
<li><b>Diferença:</b> − (elementos em A mas não em B)</li>
<li><b>Complementar:</b> Aᶜ (elementos do universo que não estão em A)</li>
<li><b>Conjunto vazio:</b> ∅ (sem elementos)</li>
<li><b>Subconjunto de qualquer conjunto:</b> ∅ ⊆ A sempre</li>
</ul>
</div>
</div>

<div id="outline-container-orgc7d4911" class="outline-4">
<h4 id="orgc7d4911"><span class="section-number-4">1.1.14.</span> Fórmulas Essenciais</h4>
<div class="outline-text-4" id="text-1-1-14">
<pre class="example" id="orgc003e91">
n(A ∪ B) = n(A) + n(B) − n(A ∩ B)

n(A ∪ B ∪ C) = n(A) + n(B) + n(C) 
                − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) 
                + n(A ∩ B ∩ C)

Aᶜ = U − A

ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
</pre>

<hr />

<p>
<b>Tempo de estudo recomendado:</b> 120 minutos <b>Nível de dificuldade:</b> Fundamental <b>Importância para a prova:</b> ⭐⭐⭐⭐ (muito importante
</p>
<ul class="org-ul">
<li>base para funções)</li>
</ul>
</div>
</div>
</div>

<div id="outline-container-org9354b20" class="outline-3">`;

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
