# 11/18 - Dia 1

## Aula 1 - Matemática: Conjuntos - 120min

### O que são Conjuntos?

Um **conjunto** é uma coleção de objetos distintos, chamados de **elementos**. Os conjuntos são fundamentais na matemática e servem como base para diversos outros conceitos.

**Notação:**
- Conjuntos são representados por letras maiúsculas: A, B, C, etc.
- Elementos são representados por letras minúsculas: a, b, c, etc.
- Usamos chaves { } para listar os elementos

**Exemplos:**
- A = {1, 2, 3, 4, 5}
- B = {a, e, i, o, u}
- C = {2, 4, 6, 8, 10}

### Relação de Pertinência

Usamos os símbolos **∈** (pertence) e **∉** (não pertence) para indicar se um elemento faz parte de um conjunto.

**Exemplos:**
- 3 ∈ A (3 pertence ao conjunto A)
- 7 ∉ A (7 não pertence ao conjunto A)
- e ∈ B (e pertence ao conjunto B)

### Conjuntos Numéricos Fundamentais

#### ℕ - Números Naturais
ℕ = {0, 1, 2, 3, 4, 5, ...}
- Números inteiros não-negativos
- Usados para contar
- ℕ* = {1, 2, 3, 4, ...} (naturais sem o zero)

#### ℤ - Números Inteiros
ℤ = {..., -3, -2, -1, 0, 1, 2, 3, ...}
- Incluem os naturais e seus negativos
- ℤ* = ℤ - {0} (inteiros sem o zero)
- ℤ₊ = {0, 1, 2, 3, ...} (inteiros não-negativos)
- ℤ₋ = {..., -3, -2, -1, 0} (inteiros não-positivos)

#### ℚ - Números Racionais
ℚ = {p/q | p ∈ ℤ, q ∈ ℤ*}
- Números que podem ser escritos como fração
- Incluem decimais finitos e dízimas periódicas
- Exemplos: 1/2, 0,5, 3,333..., -2/3

#### 𝕀 - Números Irracionais
- Números que **NÃO** podem ser escritos como fração
- Decimais infinitos e não-periódicos
- Exemplos: π, √2, √3, e (número de Euler)

#### ℝ - Números Reais
ℝ = ℚ ∪ 𝕀
- União de todos os números racionais e irracionais
- Representam todos os pontos da reta numérica

**Diagrama de inclusão:**
```
ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
```

### Tipos de Conjuntos Especiais

#### Conjunto Vazio
- Conjunto sem elementos
- Notação: ∅ ou { }
- Exemplo: A = {x ∈ ℕ | x < 0} = ∅

#### Conjunto Unitário
- Conjunto com apenas um elemento
- Exemplo: B = {5}

#### Conjunto Universo (U)
- Conjunto que contém todos os elementos relevantes para um problema
- Varia conforme o contexto

### Subconjuntos

Um conjunto A é **subconjunto** de B (A ⊆ B) se todos os elementos de A também pertencem a B.

**Propriedades:**
- Todo conjunto é subconjunto de si mesmo: A ⊆ A
- O conjunto vazio é subconjunto de qualquer conjunto: ∅ ⊆ A
- Se A ⊆ B e B ⊆ A, então A = B

**Subconjunto próprio:**
- A ⊂ B significa que A ⊆ B e A ≠ B
- Todos os elementos de A estão em B, mas B tem pelo menos um elemento que não está em A

**Exemplo:**
- A = {1, 2, 3}
- B = {1, 2, 3, 4, 5}
- A ⊂ B (A é subconjunto próprio de B)

### Operações entre Conjuntos

#### União (∪)
A união de A e B é o conjunto formado por elementos que pertencem a A **ou** a B (ou ambos).

**Notação:** A ∪ B = {x | x ∈ A ou x ∈ B}

**Exemplo:**
- A = {1, 2, 3}
- B = {3, 4, 5}
- A ∪ B = {1, 2, 3, 4, 5}

**Propriedades:**
- A ∪ ∅ = A
- A ∪ A = A
- A ∪ B = B ∪ A (comutativa)

#### Interseção (∩)
A interseção de A e B é o conjunto formado por elementos que pertencem a A **e** a B simultaneamente.

**Notação:** A ∩ B = {x | x ∈ A e x ∈ B}

**Exemplo:**
- A = {1, 2, 3, 4}
- B = {3, 4, 5, 6}
- A ∩ B = {3, 4}

**Propriedades:**
- A ∩ ∅ = ∅
- A ∩ A = A
- A ∩ B = B ∩ A (comutativa)

**Conjuntos disjuntos:**
- Quando A ∩ B = ∅, dizemos que A e B são disjuntos

#### Diferença (−)
A diferença entre A e B é o conjunto dos elementos que pertencem a A mas **não** pertencem a B.

**Notação:** A − B = {x | x ∈ A e x ∉ B}

**Exemplo:**
- A = {1, 2, 3, 4, 5}
- B = {3, 4, 5, 6, 7}
- A − B = {1, 2}
- B − A = {6, 7}

**Observação:** A − B ≠ B − A (não é comutativa)

#### Complementar (Aᶜ ou A')
O complementar de A em relação ao conjunto universo U é o conjunto de elementos que pertencem a U mas não pertencem a A.

**Notação:** Aᶜ = U − A = {x | x ∈ U e x ∉ A}

**Exemplo:**
- U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
- A = {2, 4, 6, 8, 10}
- Aᶜ = {1, 3, 5, 7, 9}

**Propriedades:**
- (Aᶜ)ᶜ = A
- A ∪ Aᶜ = U
- A ∩ Aᶜ = ∅

### Diagrama de Venn

Diagramas de Venn são representações visuais de conjuntos usando círculos ou elipses.

**Usos:**
- Visualizar operações entre conjuntos
- Resolver problemas de contagem
- Compreender relações entre conjuntos

**Exemplo de problema:**
- Em uma turma de 40 alunos:
  - 25 estudam Inglês
  - 20 estudam Espanhol
  - 10 estudam ambas as línguas
  - Quantos não estudam nenhuma das duas?

**Solução usando Venn:**
- Apenas Inglês: 25 - 10 = 15
- Apenas Espanhol: 20 - 10 = 10
- Ambas: 10
- Nenhuma: 40 - (15 + 10 + 10) = 5

### Intervalos Numéricos

Intervalos são subconjuntos especiais dos números reais, definidos por desigualdades.

#### Intervalo Fechado [a, b]
- [a, b] = {x ∈ ℝ | a ≤ x ≤ b}
- Inclui os extremos a e b
- Representação gráfica: ●━━━━━●

#### Intervalo Aberto (a, b)
- (a, b) = {x ∈ ℝ | a < x < b}
- Não inclui os extremos
- Representação gráfica: ○━━━━━○

#### Intervalo Fechado-Aberto [a, b)
- [a, b) = {x ∈ ℝ | a ≤ x < b}
- Inclui a, não inclui b
- Representação gráfica: ●━━━━━○

#### Intervalo Aberto-Fechado (a, b]
- (a, b] = {x ∈ ℝ | a < x ≤ b}
- Não inclui a, inclui b
- Representação gráfica: ○━━━━━●

#### Intervalos Infinitos
- [a, +∞) = {x ∈ ℝ | x ≥ a}
- (a, +∞) = {x ∈ ℝ | x > a}
- (−∞, b] = {x ∈ ℝ | x ≤ b}
- (−∞, b) = {x ∈ ℝ | x < b}
- (−∞, +∞) = ℝ

**Observação:** Infinito nunca é incluído, por isso sempre usamos parênteses

### Operações com Intervalos

#### União de intervalos
**Exemplo:**
- A = [1, 5]
- B = [3, 8]
- A ∪ B = [1, 8]

**Intervalos disjuntos:**
- C = [1, 3]
- D = [5, 7]
- C ∪ D = [1, 3] ∪ [5, 7] (união não forma intervalo único)

#### Interseção de intervalos
**Exemplo:**
- A = [1, 5]
- B = [3, 8]
- A ∩ B = [3, 5]

**Intervalos disjuntos:**
- C = [1, 3]
- D = [5, 7]
- C ∩ D = ∅

### Cardinalidade

A **cardinalidade** de um conjunto é o número de elementos que ele possui.

**Notação:** n(A) ou |A| ou #A

**Exemplos:**
- A = {1, 2, 3, 4, 5} → n(A) = 5
- B = {a, e, i, o, u} → n(B) = 5
- ∅ → n(∅) = 0

#### Fórmula para União de Conjuntos
Para dois conjuntos A e B:

**n(A ∪ B) = n(A) + n(B) − n(A ∩ B)**

**Exemplo:**
- n(A) = 30
- n(B) = 25
- n(A ∩ B) = 10
- n(A ∪ B) = 30 + 25 − 10 = 45

#### Fórmula para Três Conjuntos
**n(A ∪ B ∪ C) = n(A) + n(B) + n(C) − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) + n(A ∩ B ∩ C)**

### Exercícios Resolvidos

#### Exercício 1
Dados os conjuntos A = {1, 2, 3, 4, 5} e B = {4, 5, 6, 7, 8}, determine:

a) A ∪ B
**Resposta:** {1, 2, 3, 4, 5, 6, 7, 8}

b) A ∩ B
**Resposta:** {4, 5}

c) A − B
**Resposta:** {1, 2, 3}

d) B − A
**Resposta:** {6, 7, 8}

#### Exercício 2
Em uma escola com 100 alunos:
- 60 praticam futebol
- 50 praticam vôlei
- 30 praticam ambos
- Quantos não praticam nenhum dos dois esportes?

**Solução:**
- Apenas futebol: 60 − 30 = 30
- Apenas vôlei: 50 − 30 = 20
- Ambos: 30
- Total que pratica algum esporte: 30 + 20 + 30 = 80
- Nenhum esporte: 100 − 80 = 20

**Resposta:** 20 alunos

#### Exercício 3
Escreva os intervalos na forma de conjunto e represente na reta:

a) [−2, 5]
**Resposta:** {x ∈ ℝ | −2 ≤ x ≤ 5}

b) (3, +∞)
**Resposta:** {x ∈ ℝ | x > 3}

c) (−∞, 1]
**Resposta:** {x ∈ ℝ | x ≤ 1}

### Dicas para a Prova

1. **Leia com atenção** se o intervalo é aberto ou fechado
2. **Use diagramas de Venn** para problemas de contagem
3. **Lembre-se das propriedades** das operações
4. **Cuidado com o conjunto vazio** - é subconjunto de todos os conjuntos
5. **Na fórmula da união**, não esqueça de subtrair a interseção para evitar contar elementos duas vezes

### Conceitos-Chave para Memorizar

- **Pertinência:** ∈ (elemento pertence ao conjunto)
- **Inclusão:** ⊆ (conjunto está contido em outro)
- **União:** ∪ (elementos em A **ou** B)
- **Interseção:** ∩ (elementos em A **e** B)
- **Diferença:** − (elementos em A mas não em B)
- **Complementar:** Aᶜ (elementos do universo que não estão em A)
- **Conjunto vazio:** ∅ (sem elementos)
- **Subconjunto de qualquer conjunto:** ∅ ⊆ A sempre

### Fórmulas Essenciais

```
n(A ∪ B) = n(A) + n(B) − n(A ∩ B)

n(A ∪ B ∪ C) = n(A) + n(B) + n(C) 
                − n(A ∩ B) − n(A ∩ C) − n(B ∩ C) 
                + n(A ∩ B ∩ C)

Aᶜ = U − A

ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
```

---

**Tempo de estudo recomendado:** 120 minutos
**Nível de dificuldade:** Fundamental
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - base para funções)

## Aula 2 - Matemática: MMC e MDC - 60min

### O que é Divisibilidade?

Um número **a** é divisível por um número **b** quando a divisão de **a** por **b** é exata (resto zero).

**Notação:** b | a (lê-se "b divide a")

**Exemplos:**
- 15 é divisível por 3, pois 15 ÷ 3 = 5 (resto 0)
- 20 é divisível por 4, pois 20 ÷ 4 = 5 (resto 0)
- 17 NÃO é divisível por 3, pois 17 ÷ 3 = 5 (resto 2)

### Critérios de Divisibilidade

#### Divisibilidade por 2
Um número é divisível por 2 se termina em 0, 2, 4, 6 ou 8 (número par).

**Exemplos:** 14, 28, 100, 456

#### Divisibilidade por 3
Um número é divisível por 3 se a soma de seus algarismos é divisível por 3.

**Exemplos:**
- 123 → 1 + 2 + 3 = 6 (divisível por 3) ✓
- 234 → 2 + 3 + 4 = 9 (divisível por 3) ✓
- 125 → 1 + 2 + 5 = 8 (NÃO divisível por 3) ✗

#### Divisibilidade por 4
Um número é divisível por 4 se os dois últimos algarismos formam um número divisível por 4.

**Exemplos:**
- 316 → 16 é divisível por 4 ✓
- 1028 → 28 é divisível por 4 ✓
- 1222 → 22 NÃO é divisível por 4 ✗

#### Divisibilidade por 5
Um número é divisível por 5 se termina em 0 ou 5.

**Exemplos:** 25, 30, 105, 500

#### Divisibilidade por 6
Um número é divisível por 6 se é divisível por 2 **E** por 3 simultaneamente.

**Exemplo:**
- 36 → par (divisível por 2) e 3 + 6 = 9 (divisível por 3) ✓

#### Divisibilidade por 9
Um número é divisível por 9 se a soma de seus algarismos é divisível por 9.

**Exemplos:**
- 729 → 7 + 2 + 9 = 18 (divisível por 9) ✓
- 234 → 2 + 3 + 4 = 9 (divisível por 9) ✓

#### Divisibilidade por 10
Um número é divisível por 10 se termina em 0.

**Exemplos:** 30, 100, 250, 1000

### Números Primos

Um número primo é um número natural maior que 1 que possui **exatamente dois divisores**: 1 e ele mesmo.

**Primeiros números primos:**
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, ...

**Observações importantes:**
- 1 **NÃO** é primo (possui apenas um divisor)
- 2 é o **único** número primo par
- Todo número natural maior que 1 é primo ou composto

### Números Compostos

Um número composto é um número natural maior que 1 que possui **mais de dois divisores**.

**Exemplos:**
- 4 (divisores: 1, 2, 4)
- 6 (divisores: 1, 2, 3, 6)
- 9 (divisores: 1, 3, 9)
- 12 (divisores: 1, 2, 3, 4, 6, 12)

### Decomposição em Fatores Primos (Fatoração)

Todo número composto pode ser escrito como produto de números primos. Essa representação é única.

**Método:**
Dividir sucessivamente o número pelos menores primos possíveis até chegar a 1.

#### Exemplo 1: Fatorar 60
```
60 | 2
30 | 2
15 | 3
 5 | 5
 1 |
```

**Resultado:** 60 = 2² × 3 × 5

#### Exemplo 2: Fatorar 180
```
180 | 2
 90 | 2
 45 | 3
 15 | 3
  5 | 5
  1 |
```

**Resultado:** 180 = 2² × 3² × 5

#### Exemplo 3: Fatorar 100
```
100 | 2
 50 | 2
 25 | 5
  5 | 5
  1 |
```

**Resultado:** 100 = 2² × 5²

### MDC - Máximo Divisor Comum

O **MDC** de dois ou mais números é o **maior** número que divide todos eles simultaneamente.

#### Método 1: Listar Divisores

**Exemplo:** MDC(12, 18)

Divisores de 12: 1, 2, 3, 4, 6, 12
Divisores de 18: 1, 2, 3, 6, 9, 18

Divisores comuns: 1, 2, 3, 6
**MDC(12, 18) = 6**

#### Método 2: Decomposição em Fatores Primos

**Regra:** O MDC é o produto dos fatores primos **comuns** com os **menores expoentes**.

**Exemplo:** MDC(60, 180)

- 60 = 2² × 3 × 5
- 180 = 2² × 3² × 5

Fatores comuns com menores expoentes:
- 2² (menor expoente entre 2² e 2²)
- 3¹ (menor expoente entre 3¹ e 3²)
- 5¹ (menor expoente entre 5¹ e 5¹)

**MDC(60, 180) = 2² × 3 × 5 = 4 × 3 × 5 = 60**

#### Método 3: Divisões Sucessivas (Algoritmo de Euclides)

Divide-se o maior pelo menor, depois o divisor pelo resto, repetindo até resto zero. O último divisor é o MDC.

**Exemplo:** MDC(48, 18)

```
48 ÷ 18 = 2 (resto 12)
18 ÷ 12 = 1 (resto 6)
12 ÷ 6 = 2 (resto 0)
```

**MDC(48, 18) = 6**

### Propriedades do MDC

1. **MDC(a, b) = MDC(b, a)** (comutativo)
2. **MDC(a, 1) = 1** (1 divide qualquer número)
3. **MDC(a, 0) = a**
4. Se **a | b**, então **MDC(a, b) = a**
5. **MDC(a, b) × MMC(a, b) = a × b**

### Números Primos entre Si

Dois números são **primos entre si** (ou coprimos) quando MDC = 1.

**Exemplos:**
- MDC(8, 15) = 1 → 8 e 15 são primos entre si
- MDC(9, 16) = 1 → 9 e 16 são primos entre si
- MDC(12, 18) = 6 → 12 e 18 NÃO são primos entre si

### MMC - Mínimo Múltiplo Comum

O **MMC** de dois ou mais números é o **menor** número (diferente de zero) que é múltiplo de todos eles.

#### Método 1: Listar Múltiplos

**Exemplo:** MMC(4, 6)

Múltiplos de 4: 4, 8, **12**, 16, 20, 24, ...
Múltiplos de 6: 6, **12**, 18, 24, 30, ...

Múltiplos comuns: 12, 24, 36, ...
**MMC(4, 6) = 12**

#### Método 2: Decomposição em Fatores Primos

**Regra:** O MMC é o produto de **todos os fatores primos** (comuns e não comuns) com os **maiores expoentes**.

**Exemplo:** MMC(12, 18)

- 12 = 2² × 3
- 18 = 2 × 3²

Todos os fatores com maiores expoentes:
- 2² (maior expoente entre 2² e 2¹)
- 3² (maior expoente entre 3¹ e 3²)

**MMC(12, 18) = 2² × 3² = 4 × 9 = 36**

#### Método 3: Decomposição Simultânea

Decompõe-se todos os números ao mesmo tempo, usando os primos que dividem pelo menos um deles.

**Exemplo:** MMC(12, 18, 30)

```
12, 18, 30 | 2
 6,  9, 15 | 2
 3,  9, 15 | 3
 1,  3,  5 | 3
 1,  1,  5 | 5
 1,  1,  1 |
```

**MMC(12, 18, 30) = 2 × 2 × 3 × 3 × 5 = 180**

### Propriedades do MMC

1. **MMC(a, b) = MMC(b, a)** (comutativo)
2. **MMC(a, 1) = a**
3. Se **a | b**, então **MMC(a, b) = b**
4. **MMC(a, b) × MDC(a, b) = a × b**
5. **MMC(a, b, c) ≥ máximo{a, b, c}**

### Relação entre MDC e MMC

Para dois números a e b:

**MDC(a, b) × MMC(a, b) = a × b**

**Exemplo:** a = 12, b = 18
- MDC(12, 18) = 6
- MMC(12, 18) = 36
- 6 × 36 = 216
- 12 × 18 = 216 ✓

Essa propriedade permite calcular um quando se conhece o outro:

**MMC(a, b) = (a × b) / MDC(a, b)**

**MDC(a, b) = (a × b) / MMC(a, b)**

### Aplicações Práticas

#### Problema de MMC
**Situação:** Dois ônibus partem juntos de um terminal. Um retorna a cada 12 minutos, o outro a cada 18 minutos. Depois de quanto tempo voltarão a partir juntos novamente?

**Solução:** MMC(12, 18)
- 12 = 2² × 3
- 18 = 2 × 3²
- MMC = 2² × 3² = 36

**Resposta:** Após 36 minutos

#### Problema de MDC
**Situação:** Uma empresa tem 60 canetas azuis e 48 canetas vermelhas. Quer fazer pacotes iguais usando todas as canetas, com o maior número possível de canetas por pacote. Quantas canetas terá cada pacote?

**Solução:** MDC(60, 48)
- 60 = 2² × 3 × 5
- 48 = 2⁴ × 3
- MDC = 2² × 3 = 12

**Resposta:** 12 canetas por pacote
- Pacotes de azuis: 60 ÷ 12 = 5
- Pacotes de vermelhas: 48 ÷ 12 = 4

### Exercícios Resolvidos

#### Exercício 1
Calcule MDC(48, 72) e MMC(48, 72).

**Solução:**
- 48 = 2⁴ × 3
- 72 = 2³ × 3²

MDC = 2³ × 3 = 8 × 3 = **24**

MMC = 2⁴ × 3² = 16 × 9 = **144**

**Verificação:** 24 × 144 = 3456 e 48 × 72 = 3456 ✓

#### Exercício 2
Dois sinais luminosos acendem em intervalos de 15 e 20 segundos. Se acendem juntos agora, após quanto tempo voltarão a acender simultaneamente?

**Solução:**
MMC(15, 20)
- 15 = 3 × 5
- 20 = 2² × 5
- MMC = 2² × 3 × 5 = 60

**Resposta:** 60 segundos (1 minuto)

#### Exercício 3
Determinar o menor número que, dividido por 12, 15 e 20, deixa resto 5.

**Solução:**
1. Calcular MMC(12, 15, 20)
   - 12 = 2² × 3
   - 15 = 3 × 5
   - 20 = 2² × 5
   - MMC = 2² × 3 × 5 = 60

2. Como o resto é 5, adicionar 5 ao MMC
   - Número = 60 + 5 = 65

**Resposta:** 65

### Dicas para a Prova

1. **Decomposição:** Sempre comece pela fatoração em primos - é o método mais confiável
2. **MDC:** Fatores **comuns** com **menores** expoentes
3. **MMC:** **Todos** os fatores com **maiores** expoentes
4. **Verificação:** Use a relação MDC × MMC = a × b para conferir
5. **Problemas:** MMC geralmente envolve "encontros" ou "repetições"; MDC envolve "dividir em partes iguais"
6. **Primos pequenos:** Memorize os primos até 30 (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

### Conceitos-Chave para Memorizar

**Divisibilidade:**
- 2: termina em 0, 2, 4, 6, 8
- 3: soma dos algarismos divisível por 3
- 5: termina em 0 ou 5
- 10: termina em 0

**MDC e MMC:**
- MDC: **maior** divisor **comum** → fatores comuns com menores expoentes
- MMC: **menor** múltiplo **comum** → todos os fatores com maiores expoentes
- MDC × MMC = a × b

**Tipos de problemas:**
- **MMC:** repetições, encontros, ciclos
- **MDC:** divisões iguais, maior tamanho possível

### Fórmulas Essenciais

```
MDC(a, b) × MMC(a, b) = a × b

MMC(a, b) = (a × b) / MDC(a, b)

MDC(a, b) = (a × b) / MMC(a, b)

Decomposição:
- MDC → fatores COMUNS com MENORES expoentes
- MMC → TODOS os fatores com MAIORES expoentes
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Fundamental
**Importância para a prova:** ⭐⭐⭐ (importante - frequente em problemas contextualizados)

## Aula 3 - Física: Grandezas Vetoriais, Escalares e Vetores - 90min

### O que são Grandezas Físicas?

**Grandezas físicas** são propriedades que podem ser medidas e quantificadas. Elas são classificadas em dois tipos principais: escalares e vetoriais.

### Grandezas Escalares

**Definição:** Grandezas que ficam completamente determinadas por um **valor numérico** (módulo) e uma **unidade de medida**.

**Características:**
- Precisam apenas de um número e uma unidade
- Não possuem direção ou sentido
- Podem ser somadas algebricamente (soma comum)

**Exemplos:**

| Grandeza | Exemplo | Unidade (SI) |
|----------|---------|--------------|
| Tempo | 5 segundos | s |
| Massa | 10 quilogramas | kg |
| Temperatura | 25 graus Celsius | °C |
| Energia | 100 joules | J |
| Volume | 2 litros | L ou m³ |
| Densidade | 1000 kg/m³ | kg/m³ |
| Pressão | 101325 Pa | Pa |
| Trabalho | 50 J | J |
| Potência | 100 W | W |
| Carga elétrica | 5 C | C |

**Operações com escalares:**
- Soma: 5 kg + 3 kg = 8 kg
- Subtração: 10 m - 4 m = 6 m
- Multiplicação: 2 × 5 s = 10 s

### Grandezas Vetoriais

**Definição:** Grandezas que necessitam de **módulo** (intensidade), **direção** e **sentido** para serem completamente determinadas.

**Características:**
- Precisam de valor numérico, direção e sentido
- São representadas por vetores (setas)
- Não podem ser somadas algebricamente (usam regras vetoriais)

**Exemplos:**

| Grandeza | Exemplo | Unidade (SI) |
|----------|---------|--------------|
| Deslocamento | 10 m para leste | m |
| Velocidade | 20 m/s para norte | m/s |
| Aceleração | 5 m/s² para cima | m/s² |
| Força | 50 N para baixo | N |
| Quantidade de movimento | 100 kg·m/s horizontal | kg·m/s |
| Impulso | 10 N·s vertical | N·s |
| Campo elétrico | 500 N/C para direita | N/C |
| Campo magnético | 0,5 T perpendicular | T |

**Exemplo prático:**
- **Escalar:** "Andei 5 km" (distância)
- **Vetorial:** "Andei 5 km para o norte" (deslocamento)

### Elementos de um Vetor

Um vetor é representado graficamente por uma **seta** e possui três características fundamentais:

#### 1. Módulo (ou Intensidade)
- É o "tamanho" do vetor
- Representa o valor numérico da grandeza
- Corresponde ao comprimento da seta
- Notação: |v⃗| ou v

#### 2. Direção
- É a reta sobre a qual o vetor está orientado
- Exemplos: horizontal, vertical, diagonal, inclinada 30° com a horizontal

#### 3. Sentido
- É a orientação do vetor ao longo da direção
- Indicado pela ponta da seta
- Exemplos: para cima/baixo, esquerda/direita, norte/sul/leste/oeste

**Representação gráfica:**
```
      ↑
      |  Módulo (tamanho da seta)
      |
      •  Origem (ponto de aplicação)
     
Direção: vertical
Sentido: para cima
```

### Notação de Vetores

**Forma algébrica:**
- v⃗ (vetor v com seta em cima)
- **v** (vetor v em negrito)
- |v⃗| = módulo do vetor v

**Exemplo:**
- F⃗ = força (vetor)
- |F⃗| = 10 N (módulo da força)

### Sistemas de Coordenadas

#### Sistema Cartesiano (2D)
- Eixo x (horizontal): direita (+), esquerda (-)
- Eixo y (vertical): cima (+), baixo (-)

#### Pontos Cardeais
- Norte (N): +y
- Sul (S): -y
- Leste (L ou E): +x
- Oeste (O ou W): -x

### Componentes de um Vetor

Todo vetor pode ser decomposto em **componentes** ao longo dos eixos coordenados.

**Para um vetor v⃗ no plano xy:**

- **Componente x:** vₓ = |v⃗| · cos θ
- **Componente y:** vᵧ = |v⃗| · sen θ

Onde θ é o ângulo que o vetor faz com o eixo x.

**Módulo a partir das componentes:**
|v⃗| = √(vₓ² + vᵧ²)

**Ângulo a partir das componentes:**
tan θ = vᵧ / vₓ

**Exemplo:**
Um vetor de módulo 10 m faz 30° com a horizontal.

- vₓ = 10 · cos 30° = 10 · 0,866 = 8,66 m
- vᵧ = 10 · sen 30° = 10 · 0,5 = 5 m

**Verificação:**
|v⃗| = √(8,66² + 5²) = √(75 + 25) = √100 = 10 m ✓

### Operações com Vetores

#### 1. Adição de Vetores

**Regra do Paralelogramo:**
- Coloca-se os vetores com a mesma origem
- Completa-se um paralelogramo
- A diagonal representa a soma (resultante)

**Regra do Polígono (método ponta-cabeça):**
- Coloca-se a origem do segundo vetor na extremidade do primeiro
- O vetor resultante vai da origem do primeiro à extremidade do último
- Mais prático para vários vetores

**Método das componentes:**
1. Decompor cada vetor em componentes x e y
2. Somar as componentes x: Rₓ = v₁ₓ + v₂ₓ
3. Somar as componentes y: Rᵧ = v₁ᵧ + v₂ᵧ
4. Calcular o módulo: |R⃗| = √(Rₓ² + Rᵧ²)

**Exemplo:**
v₁⃗ = (3, 4) e v₂⃗ = (1, 2)

R⃗ = v₁⃗ + v₂⃗ = (3+1, 4+2) = (4, 6)

|R⃗| = √(4² + 6²) = √(16 + 36) = √52 ≈ 7,2

#### 2. Subtração de Vetores

**v₁⃗ - v₂⃗ = v₁⃗ + (-v₂⃗)**

O vetor -v₂⃗ tem mesmo módulo e direção que v₂⃗, mas sentido oposto.

**Método das componentes:**
- Rₓ = v₁ₓ - v₂ₓ
- Rᵧ = v₁ᵧ - v₂ᵧ

**Exemplo:**
v₁⃗ = (5, 3) e v₂⃗ = (2, 1)

R⃗ = v₁⃗ - v₂⃗ = (5-2, 3-1) = (3, 2)

#### 3. Multiplicação por Escalar

Multiplicar um vetor por um número k:

- Se k > 0: mesma direção e sentido, módulo multiplicado por k
- Se k < 0: mesma direção, sentido oposto, módulo multiplicado por |k|
- Se k = 0: vetor nulo

**Exemplo:**
v⃗ = (2, 3)

2v⃗ = (4, 6) → módulo dobrado, mesma direção e sentido
-v⃗ = (-2, -3) → mesmo módulo, sentido oposto

### Casos Especiais de Adição Vetorial

#### Vetores na Mesma Direção e Mesmo Sentido
|R⃗| = |v₁⃗| + |v₂⃗|

**Exemplo:** 5 N + 3 N = 8 N (na mesma direção)

#### Vetores na Mesma Direção e Sentidos Opostos
|R⃗| = ||v₁⃗| - |v₂⃗||

**Exemplo:** 5 N - 3 N = 2 N (direção do maior)

#### Vetores Perpendiculares (90°)
|R⃗| = √(|v₁⃗|² + |v₂⃗|²) (Teorema de Pitágoras)

**Exemplo:**
v₁⃗ = 3 m (horizontal)
v₂⃗ = 4 m (vertical)
|R⃗| = √(3² + 4²) = √(9 + 16) = √25 = 5 m

**Ângulo:**
tan θ = 4/3 → θ = arctan(4/3) ≈ 53,1°

#### Vetores com Ângulo θ entre Eles
|R⃗| = √(|v₁⃗|² + |v₂⃗|² + 2|v₁⃗||v₂⃗|cos θ)

**Lei dos Cossenos**

### Unidades de Medida no SI

**Sistema Internacional de Unidades (SI):**

| Grandeza | Unidade | Símbolo |
|----------|---------|---------|
| Comprimento | metro | m |
| Massa | quilograma | kg |
| Tempo | segundo | s |
| Velocidade | metro por segundo | m/s |
| Aceleração | metro por segundo ao quadrado | m/s² |
| Força | newton | N (kg·m/s²) |
| Energia | joule | J (N·m) |
| Potência | watt | W (J/s) |

**Conversões comuns:**
- 1 km = 1000 m
- 1 h = 3600 s
- 1 km/h = 1/3,6 m/s ≈ 0,278 m/s
- 1 m/s = 3,6 km/h

### Exercícios Resolvidos

#### Exercício 1
Classifique as grandezas em escalares ou vetoriais:
a) Temperatura
b) Velocidade
c) Massa
d) Força
e) Energia

**Resposta:**
a) Escalar
b) Vetorial
c) Escalar
d) Vetorial
e) Escalar

#### Exercício 2
Um vetor tem módulo 20 m e faz ângulo de 60° com a horizontal. Determine suas componentes.

**Solução:**
- vₓ = 20 · cos 60° = 20 · 0,5 = 10 m
- vᵧ = 20 · sen 60° = 20 · 0,866 = 17,32 m

**Resposta:** vₓ = 10 m, vᵧ ≈ 17,3 m

#### Exercício 3
Dois vetores perpendiculares têm módulos 6 m e 8 m. Determine o módulo da resultante.

**Solução:**
Como são perpendiculares, usamos Pitágoras:
|R⃗| = √(6² + 8²) = √(36 + 64) = √100 = 10 m

**Resposta:** 10 m

#### Exercício 4
Um carro percorre 30 km para o norte e depois 40 km para o leste. Qual o módulo do deslocamento resultante?

**Solução:**
Vetores perpendiculares:
|R⃗| = √(30² + 40²) = √(900 + 1600) = √2500 = 50 km

**Ângulo com o norte:**
tan θ = 40/30 = 4/3
θ = arctan(4/3) ≈ 53,1° para o leste

**Resposta:** 50 km a 53,1° do norte em direção ao leste (ou nordeste)

#### Exercício 5
Dados v₁⃗ = (4, 3) e v₂⃗ = (1, -2), calcule:
a) v₁⃗ + v₂⃗
b) v₁⃗ - v₂⃗
c) |v₁⃗|

**Solução:**
a) v₁⃗ + v₂⃗ = (4+1, 3-2) = (5, 1)

b) v₁⃗ - v₂⃗ = (4-1, 3-(-2)) = (3, 5)

c) |v₁⃗| = √(4² + 3²) = √(16 + 9) = √25 = 5

#### Exercício 6
Converta 72 km/h para m/s.

**Solução:**
72 km/h = 72 ÷ 3,6 = 20 m/s

Ou:
72 km/h = 72.000 m / 3600 s = 20 m/s

**Resposta:** 20 m/s

### Valores Notáveis de Seno e Cosseno

Memorize para facilitar os cálculos:

| Ângulo | sen θ | cos θ | tan θ |
|--------|-------|-------|-------|
| 0° | 0 | 1 | 0 |
| 30° | 1/2 = 0,5 | √3/2 ≈ 0,866 | √3/3 ≈ 0,577 |
| 45° | √2/2 ≈ 0,707 | √2/2 ≈ 0,707 | 1 |
| 60° | √3/2 ≈ 0,866 | 1/2 = 0,5 | √3 ≈ 1,732 |
| 90° | 1 | 0 | ∞ |

### Dicas para a Prova

1. **Identificação:** Pergunte-se "precisa de direção?". Se sim, é vetorial
2. **Decomposição:** Use sempre sen e cos corretamente (cos para x, sen para y)
3. **Perpendiculares:** Lembre-se de Pitágoras
4. **Conversões:** km/h → m/s: divida por 3,6; m/s → km/h: multiplique por 3,6
5. **Desenhe:** Sempre que possível, faça um esboço dos vetores
6. **Ângulos notáveis:** Memorize sen 30°, cos 30°, sen 60°, cos 60°, sen 45°, cos 45°

### Conceitos-Chave para Memorizar

**Escalares vs Vetoriais:**
- **Escalar:** só precisa de número + unidade (massa, tempo, temperatura)
- **Vetorial:** precisa de módulo, direção e sentido (força, velocidade, deslocamento)

**Componentes:**
- vₓ = |v⃗| · cos θ
- vᵧ = |v⃗| · sen θ
- |v⃗| = √(vₓ² + vᵧ²)

**Casos especiais:**
- Mesmo sentido: soma simples
- Sentidos opostos: subtração (sinal do maior)
- Perpendiculares: Pitágoras

### Fórmulas Essenciais

```
Componentes de um vetor:
vₓ = |v⃗| · cos θ
vᵧ = |v⃗| · sen θ

Módulo a partir das componentes:
|v⃗| = √(vₓ² + vᵧ²)

Ângulo:
tan θ = vᵧ / vₓ

Adição vetorial (componentes):
R⃗ = v₁⃗ + v₂⃗
Rₓ = v₁ₓ + v₂ₓ
Rᵧ = v₁ᵧ + v₂ᵧ

Vetores perpendiculares:
|R⃗| = √(|v₁⃗|² + |v₂⃗|²)

Lei dos Cossenos (ângulo θ entre vetores):
|R⃗| = √(|v₁⃗|² + |v₂⃗|² + 2|v₁⃗||v₂⃗|cos θ)

Conversões:
1 km/h = 1/3,6 m/s
1 m/s = 3,6 km/h
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - base para toda a cinemática e dinâmica)

## Aula 4 - Química: Propriedades das Substâncias - 90min

### O que são Propriedades das Substâncias?

As **propriedades das substâncias** são características que permitem identificar, diferenciar e classificar diferentes materiais. Dividem-se em:

- **Propriedades físicas:** podem ser observadas sem alterar a composição da substância
- **Propriedades químicas:** relacionadas ao comportamento da substância em reações químicas

### Propriedades Físicas Gerais

São propriedades comuns a toda matéria, independente da substância:

#### Massa
- Quantidade de matéria de um corpo
- Unidade SI: quilograma (kg)
- Não varia com a localização

#### Volume
- Espaço ocupado por um corpo
- Unidade SI: metro cúbico (m³)
- Também: litro (L), mililitro (mL)
- 1 L = 1000 mL = 1 dm³ = 0,001 m³

#### Inércia
- Tendência de um corpo manter seu estado de movimento ou repouso
- Relacionada à massa (quanto maior a massa, maior a inércia)

#### Impenetrabilidade
- Dois corpos não podem ocupar o mesmo lugar no espaço ao mesmo tempo

### Propriedades Físicas Específicas

São características particulares de cada substância, usadas para identificação:

### 1. Densidade (d ou ρ)

**Definição:** Relação entre a massa e o volume de uma substância.

**Fórmula:**
```
d = m / V
```

Onde:
- d = densidade
- m = massa
- V = volume

**Unidades comuns:**
- g/cm³
- kg/m³
- g/mL

**Conversão:** 1 g/cm³ = 1 g/mL = 1000 kg/m³

**Exemplos de densidades (a 20°C):**

| Substância | Densidade (g/cm³) |
|------------|-------------------|
| Ouro | 19,3 |
| Chumbo | 11,3 |
| Ferro | 7,87 |
| Alumínio | 2,70 |
| Água | 1,00 |
| Gelo | 0,92 |
| Etanol | 0,79 |
| Gasolina | 0,70 |
| Ar | 0,0013 |

**Observações importantes:**
- A densidade da água é 1 g/cm³ (referência)
- Substâncias com d < 1 g/cm³ flutuam na água
- Substâncias com d > 1 g/cm³ afundam na água
- O gelo flutua porque d(gelo) < d(água)

#### Exemplo 1
Um bloco de ferro tem massa 78,7 g e volume 10 cm³. Qual sua densidade?

**Solução:**
d = m / V = 78,7 g / 10 cm³ = 7,87 g/cm³

#### Exemplo 2
Qual a massa de 500 mL de etanol? (d = 0,79 g/mL)

**Solução:**
d = m / V
0,79 = m / 500
m = 0,79 × 500 = 395 g

#### Exemplo 3
Um cubo de gelo (d = 0,92 g/cm³) flutua ou afunda na água?

**Resposta:** Flutua, pois 0,92 < 1,00

### 2. Temperatura de Fusão (TF ou PF)

**Definição:** Temperatura na qual uma substância pura passa do estado sólido para o líquido (ou vice-versa).

**Características:**
- Específica para cada substância pura
- Permanece constante durante toda a fusão
- À pressão de 1 atm (nível do mar)

**Exemplos:**

| Substância | TF (°C) a 1 atm |
|------------|-----------------|
| Tungstênio | 3422 |
| Ferro | 1535 |
| Ouro | 1064 |
| Alumínio | 660 |
| Chumbo | 327 |
| Água | 0 |
| Mercúrio | -39 |
| Etanol | -114 |

**Curva de aquecimento:**
```
Temperatura
   ↑
   |     Líquido
   |----------------
TF |     Fusão (platô)
   |----------------
   |     Sólido
   |________________→ Tempo
```

**Observações:**
- Durante a fusão, T permanece constante
- Substâncias puras têm TF definida
- Misturas fundem em faixa de temperatura

### 3. Temperatura de Ebulição (TE ou PE)

**Definição:** Temperatura na qual uma substância passa do estado líquido para o gasoso com formação de bolhas em todo o líquido.

**Características:**
- Específica para cada substância pura
- Permanece constante durante toda a ebulição
- Varia com a pressão (menor pressão → menor TE)

**Exemplos:**

| Substância | TE (°C) a 1 atm |
|------------|-----------------|
| Água | 100 |
| Etanol | 78 |
| Acetona | 56 |
| Éter | 35 |
| Mercúrio | 357 |
| Ferro | 2750 |
| Ouro | 2856 |
| Oxigênio | -183 |
| Nitrogênio | -196 |

**Influência da altitude:**
- Quanto maior a altitude, menor a pressão atmosférica
- Menor pressão → menor temperatura de ebulição
- No nível do mar: água ferve a 100°C
- A 3000 m de altitude: água ferve a ~90°C

**Evaporação vs Ebulição:**

| Evaporação | Ebulição |
|------------|----------|
| Ocorre na superfície | Ocorre em todo o líquido |
| Qualquer temperatura | Temperatura específica |
| Processo lento | Processo rápido |
| Sem bolhas | Com bolhas |

### 4. Solubilidade

**Definição:** Capacidade de uma substância (soluto) se dissolver em outra (solvente) a uma dada temperatura.

**Unidades comuns:**
- g soluto / 100 g solvente
- g/L
- mol/L

**Coeficiente de solubilidade (Cs):**
Quantidade máxima de soluto que dissolve em 100 g de solvente a determinada temperatura.

**Classificação das soluções:**

| Tipo | Característica |
|------|----------------|
| **Insaturada** | Quantidade de soluto < Cs (pode dissolver mais) |
| **Saturada** | Quantidade de soluto = Cs (equilíbrio) |
| **Supersaturada** | Quantidade de soluto > Cs (instável) |

**Exemplos de solubilidade em água (20°C):**

| Substância | Solubilidade (g/100g H₂O) |
|------------|---------------------------|
| NaCl (sal) | 36 |
| Açúcar | 200 |
| KNO₃ | 32 |
| CaCO₃ | 0,0013 (pouco solúvel) |

**Fatores que afetam a solubilidade:**

#### Temperatura
- **Sólidos em líquidos:** geralmente aumenta com a temperatura
- **Gases em líquidos:** diminui com a temperatura

#### Natureza do soluto e solvente
- **"Semelhante dissolve semelhante"**
- Polar dissolve polar
- Apolar dissolve apolar
- Exemplos:
  - Água (polar) dissolve sal (polar) ✓
  - Água (polar) NÃO dissolve óleo (apolar) ✗
  - Gasolina (apolar) dissolve óleo (apolar) ✓

#### Pressão (para gases)
- Aumenta a pressão → aumenta a solubilidade de gases
- Lei de Henry

### Outras Propriedades Físicas Importantes

#### Ponto de Congelamento
- Temperatura na qual líquido passa a sólido
- Para substâncias puras: PF = PC (ponto de fusão = ponto de congelamento)

#### Viscosidade
- Resistência ao escoamento
- Mel > água > álcool

#### Dureza
- Resistência ao risco
- Escala de Mohs (1 a 10)
- Diamante: 10 (mais duro)
- Talco: 1 (menos duro)

#### Maleabilidade
- Capacidade de ser transformado em lâminas
- Ouro é muito maleável

#### Ductilidade
- Capacidade de ser transformado em fios
- Cobre é muito dúctil

#### Cor e Brilho
- Características visuais
- Podem ajudar na identificação

### Substância Pura vs Mistura

**Substância Pura:**
- Composição fixa e definida
- Propriedades físicas constantes
- TF e TE constantes durante as mudanças de estado
- Exemplos: H₂O, NaCl, Fe, O₂

**Mistura:**
- Composição variável
- Propriedades dependem da proporção
- TF e TE variam durante as mudanças de estado
- Exemplos: ar, água do mar, sangue, gasolina

**Gráficos de mudança de estado:**

```
Substância Pura:           Mistura:
T ↑                        T ↑
  |    Vapor                 |      Vapor
  |____                      |  ____/
  | Eb                       | /Ebulição
  |____                      |/
  | Líquido                  |   Líquido
  |____                      |____
  | Fu                       | ___/
  |____                      |/Fusão
  | Sólido                   | Sólido
  |_____→ tempo              |_____→ tempo
  
 Platôs constantes       Faixas de temperatura
```

### Exercícios Resolvidos

#### Exercício 1
Um objeto de 200 g ocupa volume de 25 cm³. Calcule sua densidade e identifique o material (consulte a tabela).

**Solução:**
d = m / V = 200 g / 25 cm³ = 8 g/cm³

Consultando a tabela: densidade próxima ao ferro (7,87 g/cm³).
**Resposta:** Provavelmente ferro ou liga ferrosa.

#### Exercício 2
Quantos gramas de sal (NaCl) podem ser dissolvidos em 500 g de água a 20°C? (Cs = 36 g/100g H₂O)

**Solução:**
Se 100 g H₂O dissolvem 36 g NaCl
500 g H₂O dissolvem x g NaCl

x = (500 × 36) / 100 = 180 g

**Resposta:** 180 g de sal

#### Exercício 3
Qual a massa de 2 L de gasolina? (d = 0,70 g/mL)

**Solução:**
2 L = 2000 mL

d = m / V
0,70 = m / 2000
m = 0,70 × 2000 = 1400 g = 1,4 kg

**Resposta:** 1,4 kg

#### Exercício 4
Por que o gelo flutua na água?

**Resposta:** Porque a densidade do gelo (0,92 g/cm³) é menor que a densidade da água líquida (1,00 g/cm³). Essa propriedade é incomum e fundamental para a vida aquática.

#### Exercício 5
Em uma cidade a 1500 m de altitude, a água ferve antes ou depois de 100°C?

**Resposta:** Antes. A pressão atmosférica é menor em altitudes elevadas, portanto a temperatura de ebulição diminui (aproximadamente 95°C a 1500 m).

### Dicas para a Prova

1. **Densidade:** Memorize que água = 1 g/cm³ (referência)
2. **Flutuação:** d < d(água) = flutua; d > d(água) = afunda
3. **Conversões:** 1 g/cm³ = 1 g/mL; 1 L = 1000 mL
4. **TF e TE:** Substâncias puras têm valores constantes; misturas têm faixas
5. **Solubilidade:** Geralmente aumenta com temperatura (sólidos); diminui com temperatura (gases)
6. **Semelhante dissolve semelhante:** polar + polar; apolar + apolar
7. **Altitude:** Maior altitude → menor TE da água

### Conceitos-Chave para Memorizar

**Densidade:**
- d = m / V
- Água = 1 g/cm³
- d < 1 → flutua
- d > 1 → afunda

**Temperaturas de mudança de estado:**
- **TF (fusão):** sólido ↔ líquido
- **TE (ebulição):** líquido → vapor
- Substância pura: T constante
- Mistura: faixa de T

**Solubilidade:**
- Sólidos: ↑ T → ↑ solubilidade
- Gases: ↑ T → ↓ solubilidade
- Polar dissolve polar
- Apolar dissolve apolar

### Fórmulas Essenciais

```
Densidade:
d = m / V

Conversões:
1 g/cm³ = 1 g/mL = 1000 kg/m³
1 L = 1000 mL = 1 dm³

Solubilidade:
Cs = massa do soluto / massa do solvente × 100
(geralmente em g soluto / 100 g solvente)

Água:
- d = 1 g/cm³ (líquida a 4°C)
- TF = 0°C (a 1 atm)
- TE = 100°C (a 1 atm)
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - cai frequentemente em questões contextualizadas)

## Aula 5 - Química: Processos de Separação de Misturas - 60min

### O que são Misturas?

**Mistura:** União de duas ou mais substâncias, onde cada uma mantém suas propriedades químicas.

**Tipos de misturas:**

#### Misturas Homogêneas (Soluções)
- Apresentam aspecto uniforme
- Uma única fase visível
- Componentes não distinguíveis a olho nu
- Exemplos: água + sal, ar, álcool + água, vinagre

#### Misturas Heterogêneas
- Apresentam aspecto não-uniforme
- Duas ou mais fases visíveis
- Componentes distinguíveis
- Exemplos: água + óleo, água + areia, granito

**Fase:** Cada porção visualmente homogênea de uma mistura

**Exemplos:**
- Água + óleo: 2 fases (heterogênea)
- Água + sal dissolvido: 1 fase (homogênea)
- Água + gelo + óleo: 3 fases (heterogênea)

### Por que Separar Misturas?

- Obter substâncias puras
- Purificar produtos
- Isolar componentes úteis
- Tratamento de água e efluentes
- Processos industriais
- Análises químicas

### Processos de Separação de Misturas Heterogêneas

### 1. Catação

**Princípio:** Separação manual dos componentes

**Quando usar:** Componentes sólidos grandes e facilmente distinguíveis

**Exemplos:**
- Separar feijões estragados
- Retirar impurezas de grãos
- Separar pedras de arroz
- Reciclagem (separar plásticos, metais, vidros)

**Vantagens:** Simples, não requer equipamentos
**Desvantagens:** Lento, não serve para partículas pequenas

### 2. Peneiração (Tamisação)

**Princípio:** Separação por diferença de tamanho usando peneiras/tamises

**Quando usar:** Sólidos com partículas de tamanhos diferentes

**Exemplos:**
- Separar areia de pedregulhos
- Peneirar farinha
- Separar grãos na agricultura
- Construção civil (separar agregados)

**Equipamento:** Peneira ou tamis (malha com furos de tamanho definido)

**Vantagens:** Simples e eficiente para diferenças de tamanho
**Desvantagens:** Só funciona para sólidos de tamanhos diferentes

### 3. Ventilação (Levigação)

**Princípio:** Separação por diferença de densidade usando corrente de ar

**Quando usar:** Sólido mais leve + sólido mais denso

**Exemplos:**
- Separar cascas de grãos
- Separar palha de cereais
- Limpeza de grãos de café
- Separar areia (mais densa) de serragem (menos densa)

**Processo:** Corrente de ar arrasta o material menos denso

### 4. Flotação

**Princípio:** Separação por diferença de densidade usando líquido

**Quando usar:** Sólido menos denso + sólido mais denso, usando água

**Exemplos:**
- Separar plástico de vidro em reciclagem
- Separar serragem de areia
- Mineração (separar minérios)

**Processo:**
1. Adiciona-se água à mistura
2. Material menos denso flutua
3. Material mais denso afunda
4. Coleta-se separadamente

**Aplicação industrial:** Enriquecimento de minérios com uso de reagentes que alteram a densidade superficial

### 5. Separação Magnética

**Princípio:** Separação usando ímã para atrair materiais magnéticos

**Quando usar:** Materiais magnéticos (ferro, níquel, cobalto) + materiais não-magnéticos

**Exemplos:**
- Separar ferro de enxofre
- Separar limalha de ferro de areia
- Reciclagem (separar metais ferrosos)
- Indústria de alimentos (remover partículas metálicas)

**Equipamento:** Ímã ou eletroímã

**Vantagens:** Rápida e eficiente
**Limitações:** Só funciona com materiais magnéticos

### 6. Dissolução Fracionada

**Princípio:** Usar um solvente que dissolve apenas um dos componentes

**Quando usar:** Um sólido solúvel + um sólido insolúvel no mesmo solvente

**Exemplos:**
- Separar sal (solúvel) de areia (insolúvel) usando água
- Separar açúcar de serragem

**Processo:**
1. Adiciona-se o solvente (ex: água)
2. Um componente dissolve, outro não
3. Filtra-se para separar o sólido insolúvel
4. Evapora-se o solvente para recuperar o sólido dissolvido

### 7. Filtração (Filtração Simples)

**Princípio:** Separar sólido de líquido usando material poroso

**Quando usar:** Sólido insolúvel + líquido

**Exemplos:**
- Coar café
- Filtrar água
- Separar areia da água
- Tratamento de água e esgoto

**Equipamentos:**
- **Simples:** Coador, papel de filtro, tecido
- **Laboratório:** Funil + papel de filtro + suporte

**Processo:**
1. Mistura passa pelo filtro
2. Sólido fica retido (resíduo)
3. Líquido passa (filtrado)

**Tipos especiais:**

#### Filtração a Vácuo
- Usa bomba de vácuo para acelerar
- Mais rápida que filtração simples
- Usada em laboratórios

#### Filtração sob Pressão
- Usa pressão para forçar passagem
- Exemplos: Filtros de água domésticos, tratamento industrial

### 8. Decantação

**Princípio:** Separar por diferença de densidade, deixando em repouso

**Quando usar:** Líquido + sólido insolúvel OU dois líquidos imiscíveis

#### Decantação Sólido-Líquido
- Deixa-se em repouso
- Sólido mais denso decanta (vai para o fundo)
- Líquido sobrenadante é vertido ou sifonado

**Exemplos:**
- Tratamento de água (floculação + decantação)
- Deixar água barrenta decantar

#### Decantação Líquido-Líquido
- Usa **funil de separação (funil de bromo)**
- Líquidos imiscíveis (que não se misturam)
- Líquido mais denso fica embaixo

**Exemplos:**
- Separar água e óleo
- Separar água e gasolina
- Extração de petróleo

**Processo com funil de separação:**
1. Coloca-se a mistura no funil
2. Aguarda-se a separação das fases
3. Abre-se a torneira e coleta-se o líquido de baixo
4. Fecha-se a torneira quando chegar ao líquido de cima
5. Retira-se o líquido de cima pela parte superior

### 9. Centrifugação

**Princípio:** Acelerar a decantação por rotação em alta velocidade

**Quando usar:** Quando a decantação natural é muito lenta

**Exemplos:**
- Separar sangue (células + plasma)
- Centrifugar roupa em máquina de lavar
- Análises clínicas (separar componentes do sangue, urina)
- Separar creme de leite

**Equipamento:** Centrífuga

**Vantagens:** Muito mais rápida que decantação simples
**Aplicação:** Essencial em laboratórios médicos e de pesquisa

### Processos de Separação de Misturas Homogêneas

### 10. Evaporação

**Princípio:** Evaporar completamente o solvente, deixando o soluto

**Quando usar:** Sólido dissolvido + líquido volátil (quando não precisamos do líquido)

**Exemplos:**
- Obter sal marinho (salinas)
- Evaporar água para obter sal de cozinha
- Secagem natural de roupas

**Processo:**
- Pode ser natural (sol, vento)
- Ou por aquecimento

**Desvantagem:** Perde-se o líquido

### 11. Destilação Simples

**Princípio:** Separar por diferença de temperatura de ebulição, com recuperação do líquido

**Quando usar:** Sólido dissolvido + líquido OU líquidos com diferença grande de TE

**Exemplos:**
- Destilar água (obter água destilada)
- Separar água de sal dissolvido
- Produzir água potável do mar

**Equipamento:**
- Balão de destilação
- Condensador (serpentina resfriada)
- Termômetro
- Recipiente coletor

**Processo:**
1. Aquece-se a mistura no balão
2. Líquido com menor TE evapora primeiro
3. Vapor sobe e entra no condensador
4. Condensador resfria o vapor, que volta ao estado líquido
5. Líquido destilado é coletado
6. Sólido (ou líquido de maior TE) fica no balão

**Resultados:**
- **Destilado:** Líquido que foi vaporizado e condensado (purificado)
- **Resíduo:** Material que ficou no balão

### 12. Destilação Fracionada

**Princípio:** Separar líquidos com temperaturas de ebulição próximas

**Quando usar:** Mistura de líquidos miscíveis com TEs diferentes mas próximas

**Exemplos:**
- Separar componentes do petróleo (gasolina, querosene, diesel, etc.)
- Separar álcool de água (produção de cachaça, whisky)
- Separar componentes do ar liquefeito (O₂, N₂, gases nobres)
- Produção de bebidas destiladas

**Equipamento:** Similar à destilação simples, mas com **coluna de fracionamento**

**Coluna de fracionamento:**
- Torre com obstáculos ou pratos
- Permite múltiplas evaporações e condensações
- Aumenta a eficiência da separação

**Processo (petróleo):**
```
          Topo (mais frio)
              ↑
         Gás (GLP)
              ↑
         Gasolina (~100-150°C)
              ↑
         Querosene (~150-250°C)
              ↑
         Diesel (~250-350°C)
              ↑
         Óleos lubrificantes
              ↑
         Asfalto (resíduo)
         
         Base (mais quente)
```

- Substâncias com menor TE saem no topo
- Substâncias com maior TE saem na base

**Diferença entre destilações:**
- **Simples:** Sólido + líquido OU líquidos com TEs muito diferentes
- **Fracionada:** Líquidos miscíveis com TEs próximas

### Quadro Resumo dos Processos

| Processo | Tipo de Mistura | Princípio | Exemplo |
|----------|----------------|-----------|---------|
| **Catação** | Heterogênea (S+S) | Manual | Feijão + impurezas |
| **Peneiração** | Heterogênea (S+S) | Tamanho | Areia + pedras |
| **Ventilação** | Heterogênea (S+S) | Densidade + ar | Grãos + cascas |
| **Flotação** | Heterogênea (S+S) | Densidade + água | Plástico + vidro |
| **Separação Magnética** | Heterogênea (S+S) | Magnetismo | Ferro + areia |
| **Dissolução Fracionada** | Heterogênea (S+S) | Solubilidade | Sal + areia |
| **Filtração** | Heterogênea (S+L) | Porosidade | Café + pó |
| **Decantação** | Heterogênea (S+L ou L+L) | Densidade | Água + óleo |
| **Centrifugação** | Heterogênea (S+L) | Força centrífuga | Sangue |
| **Evaporação** | Homogênea (S+L) | Volatilização | Salina |
| **Destilação Simples** | Homogênea (S+L ou L+L) | TE muito diferentes | Água + sal |
| **Destilação Fracionada** | Homogênea (L+L) | TEs próximas | Petróleo |

**Legenda:** S = Sólido, L = Líquido

### Processos Combinados

Na prática, muitas separações requerem combinação de processos:

**Exemplo 1: Sal + Areia + Água**
1. Dissolução fracionada (água dissolve sal, não dissolve areia)
2. Filtração (separa areia)
3. Evaporação ou Destilação (recupera sal da água)

**Exemplo 2: Água barrenta**
1. Decantação (remove sólidos maiores)
2. Filtração (remove sólidos menores)
3. Cloração/purificação (tratamento químico)

**Exemplo 3: Petróleo bruto**
1. Decantação (remove água e impurezas)
2. Destilação fracionada (separa componentes)

### Aplicações no Cotidiano e Indústria

**Tratamento de água:**
- Floculação → Decantação → Filtração → Cloração

**Mineração:**
- Flotação para concentrar minérios
- Separação magnética de minério de ferro

**Petroquímica:**
- Destilação fracionada do petróleo

**Alimentos:**
- Filtração de sucos
- Destilação de bebidas alcoólicas
- Peneiração de farinhas

**Saúde:**
- Centrifugação de sangue
- Filtração de medicamentos

### Exercícios Resolvidos

#### Exercício 1
Qual processo usado para separar:
a) Ferro + enxofre
b) Água + óleo
c) Água + álcool
d) Sal + água

**Resposta:**
a) Separação magnética
b) Decantação (funil de separação)
c) Destilação fracionada
d) Destilação simples ou evaporação

#### Exercício 2
Você tem uma mistura de água, areia e sal. Descreva os processos para separar os três componentes.

**Solução:**
1. **Dissolução fracionada:** Adicionar água para dissolver o sal
2. **Filtração:** Separar a areia (fica retida no filtro)
3. **Destilação simples:** Separar água (destilado) e sal (resíduo)

Resultado: Areia seca, sal seco, água destilada

#### Exercício 3
Por que o petróleo precisa de destilação fracionada e não simples?

**Resposta:** Porque o petróleo é uma mistura de muitos hidrocarbonetos com temperaturas de ebulição próximas. A destilação fracionada, com sua coluna de fracionamento, permite separar eficientemente esses componentes com TEs similares. A destilação simples não seria eficiente para isso.

#### Exercício 4
Em uma salina, que processo é usado para obter sal do mar?

**Resposta:** Evaporação. A água do mar é colocada em tanques rasos e exposta ao sol. A água evapora naturalmente, deixando o sal cristalizado.

### Dicas para a Prova

1. **Identifique o tipo de mistura:** Homogênea ou heterogênea?
2. **Identifique os estados físicos:** Sólido-sólido, sólido-líquido, líquido-líquido?
3. **Pense na propriedade diferente:** Tamanho? Densidade? Solubilidade? TE? Magnetismo?
4. **Processos combinados:** Problemas complexos geralmente requerem vários processos
5. **Destilação:** Simples (TEs muito diferentes) vs Fracionada (TEs próximas)
6. **Funil de separação:** Sempre para líquidos imiscíveis

### Conceitos-Chave para Memorizar

**Misturas Heterogêneas (sólido-sólido):**
- Catação: manual
- Peneiração: tamanho
- Ventilação/Levigação: densidade + ar
- Flotação: densidade + água
- Separação magnética: magnetismo
- Dissolução fracionada: solubilidade

**Misturas Heterogêneas (sólido-líquido):**
- Filtração: porosidade
- Decantação: densidade + repouso
- Centrifugação: densidade + rotação

**Misturas Heterogêneas (líquido-líquido):**
- Decantação com funil de separação

**Misturas Homogêneas:**
- Evaporação: perde o líquido
- Destilação simples: recupera o líquido (TEs muito diferentes)
- Destilação fracionada: líquidos com TEs próximas

### Tabela Rápida de Decisão

```
Tenho uma mistura...

Heterogênea?
  ├─ Sólido + Sólido?
  │   ├─ Tamanhos diferentes? → Peneiração
  │   ├─ Um é magnético? → Separação magnética
  │   ├─ Densidades diferentes? → Flotação ou Ventilação
  │   ├─ Um é solúvel em água? → Dissolução fracionada
  │   └─ Partículas grandes? → Catação
  │
  ├─ Sólido + Líquido?
  │   ├─ Rápido? → Centrifugação
  │   └─ Normal? → Filtração ou Decantação
  │
  └─ Líquido + Líquido (imiscíveis)? → Decantação (funil)

Homogênea?
  ├─ Não preciso do líquido? → Evaporação
  ├─ TEs muito diferentes? → Destilação simples
  └─ TEs próximas? → Destilação fracionada
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - questões contextualizadas e práticas)

---

# 11/19 - Dia 2

## Aula 6 - Matemática: Razão, Proporção e Proporcionalidade - 90min

### O que é Razão?

**Definição:** Razão é a comparação entre duas grandezas por meio de uma divisão.

**Notação:**
- Razão entre a e b: a/b ou a:b (lê-se "a está para b")
- a é o **antecedente**
- b é o **consequente** (b ≠ 0)

**Exemplos:**

#### Exemplo 1
Em uma turma há 15 meninos e 10 meninas. Qual a razão entre meninos e meninas?

**Solução:**
Razão = 15/10 = 3/2 (simplificando)

**Interpretação:** Para cada 3 meninos, há 2 meninas.

#### Exemplo 2
Um carro percorre 300 km em 4 horas. Qual a razão entre distância e tempo?

**Solução:**
Razão = 300/4 = 75 km/h

**Interpretação:** A cada hora, o carro percorre 75 km (velocidade média).

### Tipos Especiais de Razão

#### Escala
Razão entre a medida no desenho e a medida real.

**Fórmula:**
```
Escala = medida no desenho / medida real
```

**Exemplo:**
Em um mapa com escala 1:1.000.000, significa que 1 cm no mapa representa 1.000.000 cm (10 km) na realidade.

- 1:100 → 1 cm no desenho = 100 cm real = 1 m real
- 1:50.000 → 1 cm no mapa = 50.000 cm = 500 m = 0,5 km

#### Velocidade Média
Razão entre distância percorrida e tempo gasto.

**Fórmula:**
```
v = d / t
```

**Exemplo:**
Um atleta corre 10 km em 50 minutos.
v = 10 km / 50 min = 0,2 km/min = 12 km/h

#### Densidade Demográfica
Razão entre população e área.

**Fórmula:**
```
d = população / área
```

**Exemplo:**
Um município com 50.000 habitantes e área de 250 km².
d = 50.000 / 250 = 200 hab/km²

### O que é Proporção?

**Definição:** Proporção é uma igualdade entre duas razões.

**Notação:**
```
a/b = c/d  ou  a:b = c:d
```

**Lê-se:** "a está para b assim como c está para d"

**Termos da proporção:**
```
a/b = c/d

a e d → extremos
b e c → meios
```

### Propriedade Fundamental das Proporções

**Em toda proporção, o produto dos meios é igual ao produto dos extremos.**

```
Se a/b = c/d, então a × d = b × c
```

**Exemplo:**
```
2/3 = 4/6

Verificação:
2 × 6 = 12 (produto dos extremos)
3 × 4 = 12 (produto dos meios)
12 = 12 ✓
```

**Aplicação:** Essa propriedade é usada para encontrar um termo desconhecido.

#### Exemplo 1
Determine x na proporção: 3/5 = x/15

**Solução:**
3 × 15 = 5 × x
45 = 5x
x = 45/5
x = 9

#### Exemplo 2
Determine x na proporção: 8/x = 2/7

**Solução:**
8 × 7 = x × 2
56 = 2x
x = 56/2
x = 28

### Outras Propriedades das Proporções

#### 1. Soma dos Antecedentes e Consequentes
```
Se a/b = c/d, então:

(a + c)/(b + d) = a/b = c/d
```

**Exemplo:**
Se 2/3 = 4/6, então (2+4)/(3+6) = 6/9 = 2/3 ✓

#### 2. Diferença dos Antecedentes e Consequentes
```
Se a/b = c/d, então:

(a - c)/(b - d) = a/b = c/d
```

#### 3. Inverter os Termos
```
Se a/b = c/d, então b/a = d/c
```

### Grandezas Proporcionais

#### Grandezas Diretamente Proporcionais

**Definição:** Duas grandezas são diretamente proporcionais quando, ao aumentar uma, a outra aumenta na mesma proporção (e vice-versa).

**Característica:** A razão entre valores correspondentes é constante (k).

**Exemplos:**
- Quantidade de combustível e preço pago
- Tempo de trabalho e salário
- Velocidade constante: distância e tempo

#### Exemplo Prático
Se 2 kg de carne custam R$ 40, quanto custarão 5 kg?

**Solução:**
```
2 kg ——— R$ 40
5 kg ——— x

2/5 = 40/x  (proporção)
2x = 5 × 40
2x = 200
x = 100
```

**Resposta:** R$ 100

**Verificação:** A razão preço/quantidade é constante:
- 40/2 = 20 reais/kg
- 100/5 = 20 reais/kg ✓

#### Grandezas Inversamente Proporcionais

**Definição:** Duas grandezas são inversamente proporcionais quando, ao aumentar uma, a outra diminui na mesma proporção (e vice-versa).

**Característica:** O produto entre valores correspondentes é constante (k).

**Exemplos:**
- Velocidade e tempo (para mesma distância)
- Número de operários e tempo para completar obra
- Número de torneiras e tempo para encher tanque

#### Exemplo Prático
Se 3 operários fazem uma obra em 12 dias, quantos dias levarão 6 operários?

**Solução:**
Mais operários → menos dias (inversamente proporcionais)

```
3 operários ——— 12 dias
6 operários ——— x dias

3 × 12 = 6 × x (produto constante)
36 = 6x
x = 6
```

**Resposta:** 6 dias

**Verificação:** O produto é constante:
- 3 × 12 = 36
- 6 × 6 = 36 ✓

### Divisão em Partes Proporcionais

#### Divisão Diretamente Proporcional

Dividir um número em partes diretamente proporcionais a outros números.

**Método:**
1. Somar os números proporcionais
2. Dividir o total pela soma
3. Multiplicar o resultado por cada número

**Exemplo 1:**
Dividir 120 em partes diretamente proporcionais a 2, 3 e 5.

**Solução:**
1. Soma: 2 + 3 + 5 = 10
2. Constante: 120 / 10 = 12
3. Partes:
   - 1ª parte: 2 × 12 = 24
   - 2ª parte: 3 × 12 = 36
   - 3ª parte: 5 × 12 = 60

**Verificação:** 24 + 36 + 60 = 120 ✓

**Exemplo 2 (Prático):**
Três sócios investiram R$ 10.000, R$ 15.000 e R$ 25.000 em um negócio. O lucro foi de R$ 30.000. Como dividir proporcionalmente ao investimento?

**Solução:**
Investimentos: 10, 15, 25 (em milhares)
Soma: 10 + 15 + 25 = 50
Constante: 30.000 / 50 = 600

Partes:
- Sócio 1: 10 × 600 = R$ 6.000
- Sócio 2: 15 × 600 = R$ 9.000
- Sócio 3: 25 × 600 = R$ 15.000

**Verificação:** 6.000 + 9.000 + 15.000 = 30.000 ✓

#### Divisão Inversamente Proporcional

Dividir um número em partes inversamente proporcionais.

**Método:**
1. Inverter os números (usar recíprocos)
2. Aplicar divisão diretamente proporcional com os inversos

**Exemplo:**
Dividir 220 em partes inversamente proporcionais a 2, 4 e 5.

**Solução:**
1. Inversos: 1/2, 1/4, 1/5
2. MMC(2, 4, 5) = 20
3. Transformar: 10, 5, 4 (multiplicando por 20)
4. Soma: 10 + 5 + 4 = 19
5. Constante: 220 / 19 ≈ 11,58
6. Partes:
   - 1ª: 10 × 11,58 ≈ 115,8
   - 2ª: 5 × 11,58 ≈ 57,9
   - 3ª: 4 × 11,58 ≈ 46,3

Ou mais simples:

1. Inverter: inversamente a 2, 4, 5 → diretamente a 1/2, 1/4, 1/5
2. Denominador comum (20): 10, 5, 4
3. Dividir 220 proporcionalmente a 10, 5, 4 (como antes)

### Regra de Três Simples

Método prático para resolver problemas com grandezas proporcionais.

#### Regra de Três Simples Direta

Quando as grandezas são diretamente proporcionais.

**Método:**
1. Montar a proporção
2. Multiplicar cruzado
3. Resolver a equação

**Exemplo:**
Se 5 cadernos custam R$ 30, quanto custarão 8 cadernos?

**Solução:**
```
Cadernos    Preço
   5    ———   30
   8    ———    x

↓aumenta    ↑aumenta (direta)

5/8 = 30/x
5x = 8 × 30
5x = 240
x = 48
```

**Resposta:** R$ 48

#### Regra de Três Simples Inversa

Quando as grandezas são inversamente proporcionais.

**Método:**
1. Identificar que são inversas
2. Inverter uma das colunas
3. Multiplicar cruzado

**Exemplo:**
Se 4 máquinas fazem um trabalho em 6 dias, quantos dias levarão 8 máquinas?

**Solução:**
```
Máquinas    Dias
   4    ———   6
   8    ———   x

↑aumenta    ↓diminui (inversa)

4/8 = x/6  (inverti a coluna dos dias!)
4 × 6 = 8 × x
24 = 8x
x = 3
```

**Resposta:** 3 dias

**Macete:** Se são inversas, inverta uma coluna antes de montar a proporção!

### Exercícios Resolvidos

#### Exercício 1
A razão entre as idades de João e Maria é 3/4. Se João tem 21 anos, qual a idade de Maria?

**Solução:**
```
J/M = 3/4
21/M = 3/4
3M = 21 × 4
3M = 84
M = 28
```

**Resposta:** Maria tem 28 anos.

#### Exercício 2
Um mapa tem escala 1:2.000.000. Se a distância entre duas cidades no mapa é 5 cm, qual a distância real?

**Solução:**
```
1 cm no mapa ——— 2.000.000 cm real
5 cm no mapa ——— x

x = 5 × 2.000.000 = 10.000.000 cm = 100 km
```

**Resposta:** 100 km

#### Exercício 3
Dividir 450 em partes diretamente proporcionais a 2, 3 e 4.

**Solução:**
Soma: 2 + 3 + 4 = 9
Constante: 450 / 9 = 50

Partes:
- 2 × 50 = 100
- 3 × 50 = 150
- 4 × 50 = 200

**Verificação:** 100 + 150 + 200 = 450 ✓

#### Exercício 4
Uma torneira enche um tanque em 10 horas. Quantas torneiras iguais serão necessárias para encher o tanque em 4 horas?

**Solução:**
Inversamente proporcionais (mais torneiras → menos tempo)

```
Torneiras    Horas
   1     ———   10
   x     ———    4

1/x = 4/10  (inverti!)
1 × 10 = x × 4
10 = 4x
x = 2,5
```

**Resposta:** 2,5 torneiras. Como não existe meia torneira, seriam necessárias 3 torneiras.

#### Exercício 5
Se 6 livros custam R$ 90, quanto custarão 10 livros?

**Solução:**
Diretamente proporcionais

```
6/10 = 90/x
6x = 900
x = 150
```

**Resposta:** R$ 150

### Dicas para a Prova

1. **Identifique o tipo:** Direta ou inversa?
   - ↑↑ ou ↓↓ → Direta
   - ↑↓ ou ↓↑ → Inversa

2. **Regra de três inversa:** Inverta UMA das colunas antes de calcular

3. **Proporção fundamental:** produto dos meios = produto dos extremos

4. **Divisão proporcional:** 
   - Some os valores proporcionais
   - Divida o total pela soma
   - Multiplique por cada valor

5. **Escala:** medida no desenho / medida real

6. **Sempre verifique:** Confira se sua resposta faz sentido no contexto

### Conceitos-Chave para Memorizar

**Razão:**
- a/b (a está para b)
- Comparação por divisão

**Proporção:**
- a/b = c/d
- Produto dos meios = produto dos extremos
- a × d = b × c

**Grandezas:**
- **Diretamente proporcionais:** ↑↑ ou ↓↓ (razão constante)
- **Inversamente proporcionais:** ↑↓ ou ↓↑ (produto constante)

**Regra de três:**
- **Direta:** monta e calcula direto
- **Inversa:** inverte uma coluna primeiro

### Fórmulas Essenciais

```
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
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - cai muito em questões contextualizadas)

## Aula 7 - Matemática: Notação Científica, Algarismos Significativos e Estimativa - 60min

### Notação Científica

#### O que é?

**Notação científica** é uma forma padronizada de escrever números muito grandes ou muito pequenos, facilitando cálculos e comparações.

**Formato geral:**
```
N × 10ⁿ

Onde:
- N é um número tal que 1 ≤ N < 10
- n é um número inteiro (expoente)
```

**Exemplos:**
- 5.000.000 = 5 × 10⁶
- 0,00003 = 3 × 10⁻⁵
- 780.000 = 7,8 × 10⁵
- 0,0056 = 5,6 × 10⁻³

#### Por que usar?

**Vantagens:**
- Facilita escrita de números extremos
- Simplifica cálculos
- Padroniza representação científica
- Evita erros de zeros

**Exemplos práticos:**
- Distância Terra-Sol: 150.000.000.000 m = 1,5 × 10¹¹ m
- Massa do elétron: 0,000000000000000000000000000000911 kg = 9,11 × 10⁻³¹ kg
- Velocidade da luz: 300.000.000 m/s = 3 × 10⁸ m/s

### Como Converter para Notação Científica

#### Números Grandes (maiores que 1)

**Passos:**
1. Colocar a vírgula após o primeiro algarismo significativo
2. Contar quantas casas a vírgula andou para a esquerda
3. Esse número é o expoente positivo de 10

**Exemplo 1:** 45.000

```
45.000
↓ (mover vírgula para após o 4)
4,5000
Andou 4 casas → 4,5 × 10⁴
```

**Exemplo 2:** 6.750.000

```
6.750.000
↓
6,750000
Andou 6 casas → 6,75 × 10⁶
```

#### Números Pequenos (menores que 1)

**Passos:**
1. Colocar a vírgula após o primeiro algarismo diferente de zero
2. Contar quantas casas a vírgula andou para a direita
3. Esse número é o expoente negativo de 10

**Exemplo 1:** 0,0034

```
0,0034
  ↓ (mover vírgula para após o 3)
  3,4
Andou 3 casas → 3,4 × 10⁻³
```

**Exemplo 2:** 0,000000812

```
0,000000812
       ↓
       8,12
Andou 7 casas → 8,12 × 10⁻⁷
```

### Como Converter de Notação Científica para Decimal

#### Expoente Positivo

Mover a vírgula para a **direita** n casas (adicionar zeros se necessário).

**Exemplo 1:** 3,7 × 10⁴

```
3,7 × 10⁴
Mover 4 casas à direita
3,7000
37.000
```

**Exemplo 2:** 5,23 × 10⁶ = 5.230.000

#### Expoente Negativo

Mover a vírgula para a **esquerda** n casas (adicionar zeros se necessário).

**Exemplo 1:** 4,5 × 10⁻³

```
4,5 × 10⁻³
Mover 3 casas à esquerda
0,0045
```

**Exemplo 2:** 8,1 × 10⁻⁵ = 0,000081

### Operações com Notação Científica

#### Multiplicação

**Regra:**
1. Multiplicar os números N
2. Somar os expoentes
3. Ajustar para forma padrão se necessário

**Fórmula:** (a × 10ᵐ) × (b × 10ⁿ) = (a × b) × 10⁽ᵐ⁺ⁿ⁾

**Exemplo 1:**
```
(2 × 10³) × (3 × 10⁵)
= (2 × 3) × 10⁽³⁺⁵⁾
= 6 × 10⁸
```

**Exemplo 2:**
```
(4 × 10⁴) × (5 × 10⁻²)
= (4 × 5) × 10⁽⁴⁺⁽⁻²⁾⁾
= 20 × 10²
= 2 × 10³  (ajustando: 20 = 2 × 10¹)
```

#### Divisão

**Regra:**
1. Dividir os números N
2. Subtrair os expoentes
3. Ajustar para forma padrão se necessário

**Fórmula:** (a × 10ᵐ) ÷ (b × 10ⁿ) = (a ÷ b) × 10⁽ᵐ⁻ⁿ⁾

**Exemplo 1:**
```
(8 × 10⁶) ÷ (2 × 10³)
= (8 ÷ 2) × 10⁽⁶⁻³⁾
= 4 × 10³
```

**Exemplo 2:**
```
(6 × 10⁴) ÷ (3 × 10⁷)
= (6 ÷ 3) × 10⁽⁴⁻⁷⁾
= 2 × 10⁻³
```

#### Adição e Subtração

**Regra:** Só é prático somar/subtrair se os expoentes forem **iguais**.

1. Igualar os expoentes (se necessário)
2. Somar ou subtrair os números N
3. Manter o expoente comum

**Exemplo 1:** (mesmo expoente)
```
(3 × 10⁵) + (2 × 10⁵)
= (3 + 2) × 10⁵
= 5 × 10⁵
```

**Exemplo 2:** (expoentes diferentes)
```
(5 × 10⁴) + (3 × 10³)
Igualar expoentes:
(5 × 10⁴) + (0,3 × 10⁴)
= (5 + 0,3) × 10⁴
= 5,3 × 10⁴
```

### Algarismos Significativos

#### O que são?

**Algarismos significativos** são todos os dígitos que têm significado na precisão de uma medida.

#### Regras para Identificar

**1. Todos os dígitos diferentes de zero são significativos**
- 245 → 3 algarismos significativos
- 1,234 → 4 algarismos significativos

**2. Zeros entre dígitos diferentes de zero são significativos**
- 1007 → 4 algarismos significativos
- 50,03 → 4 algarismos significativos

**3. Zeros à esquerda NÃO são significativos** (apenas indicam posição)
- 0,0025 → 2 algarismos significativos (2 e 5)
- 0,0400 → 3 algarismos significativos (4, 0, 0)

**4. Zeros à direita:**
- **Com vírgula:** são significativos
  - 2,50 → 3 algarismos significativos
  - 100,0 → 4 algarismos significativos
  
- **Sem vírgula:** podem ser ambíguos
  - 1500 → 2, 3 ou 4? (depende do contexto)
  - Melhor usar notação científica: 1,5 × 10³ (2 sig.) ou 1,50 × 10³ (3 sig.)

#### Exemplos de Contagem

| Número | Algarismos Significativos | Quantidade |
|--------|---------------------------|------------|
| 123 | 1, 2, 3 | 3 |
| 0,0056 | 5, 6 | 2 |
| 1,020 | 1, 0, 2, 0 | 4 |
| 500 | 5 (ambíguo) | 1, 2 ou 3 |
| 5,00 × 10² | 5, 0, 0 | 3 |
| 0,0700 | 7, 0, 0 | 3 |
| 1005 | 1, 0, 0, 5 | 4 |

#### Operações com Algarismos Significativos

**Multiplicação e Divisão:**
O resultado deve ter o **mesmo número** de algarismos significativos que o fator com **menos** algarismos significativos.

**Exemplo:**
```
2,5 (2 sig.) × 3,147 (4 sig.)
= 7,8675
Arredondando para 2 sig. → 7,9
```

**Adição e Subtração:**
O resultado deve ter o mesmo número de **casas decimais** que a medida com **menos** casas decimais.

**Exemplo:**
```
12,5 (1 casa decimal)
+  0,123 (3 casas decimais)
_______
12,623 → arredondar para 1 casa → 12,6
```

### Arredondamento

**Regra básica:**
- Se o dígito seguinte for < 5: arredondar para baixo
- Se o dígito seguinte for ≥ 5: arredondar para cima

**Exemplos:**
- 3,14 arredondado para 1 casa decimal → 3,1
- 3,16 arredondado para 1 casa decimal → 3,2
- 3,15 arredondado para 1 casa decimal → 3,2
- 2,748 arredondado para 2 sig. → 2,7

### Estimativa e Ordem de Grandeza

#### Ordem de Grandeza

**Definição:** A ordem de grandeza de um número é a potência de 10 mais próxima dele.

**Método:**
1. Escrever em notação científica: N × 10ⁿ
2. Se N < √10 ≈ 3,16 → ordem = 10ⁿ
3. Se N ≥ √10 ≈ 3,16 → ordem = 10ⁿ⁺¹

**Exemplos:**

**Exemplo 1:** 2.500
```
2.500 = 2,5 × 10³
2,5 < 3,16
Ordem de grandeza: 10³
```

**Exemplo 2:** 7.000
```
7.000 = 7 × 10³
7 > 3,16
Ordem de grandeza: 10⁴
```

**Exemplo 3:** 0,002
```
0,002 = 2 × 10⁻³
2 < 3,16
Ordem de grandeza: 10⁻³
```

#### Estimativas

**Uso prático:** Fazer cálculos aproximados rapidamente.

**Técnicas:**
1. Arredondar para valores convenientes
2. Usar potências de 10
3. Simplificar frações

**Exemplo 1:**
Estimar: 48 × 23

```
Aproximar:
50 × 20 = 1.000

(Valor real: 1.104)
```

**Exemplo 2:**
Estimar a população de células em 1 kg de tecido humano, sabendo que uma célula tem massa de 10⁻¹² kg.

```
Número de células ≈ massa total / massa por célula
≈ 1 / 10⁻¹²
= 10¹² células
```

### Exercícios Resolvidos

#### Exercício 1
Escreva em notação científica:
a) 350.000
b) 0,00045
c) 12.000.000.000

**Resposta:**
a) 3,5 × 10⁵
b) 4,5 × 10⁻⁴
c) 1,2 × 10¹⁰

#### Exercício 2
Escreva em forma decimal:
a) 6,2 × 10⁴
b) 3,8 × 10⁻³

**Resposta:**
a) 62.000
b) 0,0038

#### Exercício 3
Calcule: (2 × 10⁵) × (4 × 10³)

**Solução:**
```
= (2 × 4) × 10⁽⁵⁺³⁾
= 8 × 10⁸
```

#### Exercício 4
Calcule: (9 × 10⁷) ÷ (3 × 10⁴)

**Solução:**
```
= (9 ÷ 3) × 10⁽⁷⁻⁴⁾
= 3 × 10³
```

#### Exercício 5
Quantos algarismos significativos têm:
a) 0,0034
b) 1,200
c) 1050

**Resposta:**
a) 2 (3 e 4)
b) 4 (1, 2, 0, 0)
c) 3 ou 4 (ambíguo sem vírgula; melhor usar notação científica)

#### Exercício 6
Determine a ordem de grandeza de 8.000.

**Solução:**
```
8.000 = 8 × 10³
8 > 3,16
Ordem de grandeza: 10⁴
```

### Dicas para a Prova

1. **Notação científica:** 1 ≤ N < 10 sempre
2. **Expoente positivo:** número grande (> 1)
3. **Expoente negativo:** número pequeno (< 1)
4. **Multiplicação:** soma expoentes
5. **Divisão:** subtrai expoentes
6. **Algarismos significativos:** zeros à esquerda NÃO contam
7. **Ordem de grandeza:** use √10 ≈ 3,16 como referência
8. **Estimativa:** arredonde para facilitar cálculos mentais

### Conceitos-Chave para Memorizar

**Notação Científica:**
- Formato: N × 10ⁿ (1 ≤ N < 10)
- Grande → expoente positivo
- Pequeno → expoente negativo

**Operações:**
- Multiplicação: (a × 10ᵐ) × (b × 10ⁿ) = (a×b) × 10⁽ᵐ⁺ⁿ⁾
- Divisão: (a × 10ᵐ) ÷ (b × 10ⁿ) = (a÷b) × 10⁽ᵐ⁻ⁿ⁾

**Algarismos Significativos:**
- Zeros à esquerda: NÃO
- Zeros entre dígitos: SIM
- Zeros à direita com vírgula: SIM
- Zeros à direita sem vírgula: AMBÍGUO

**Ordem de Grandeza:**
- N < 3,16 → 10ⁿ
- N ≥ 3,16 → 10ⁿ⁺¹

### Fórmulas Essenciais

```
Notação Científica:
N × 10ⁿ  onde 1 ≤ N < 10

Multiplicação:
(a × 10ᵐ) × (b × 10ⁿ) = (a × b) × 10⁽ᵐ⁺ⁿ⁾

Divisão:
(a × 10ᵐ) ÷ (b × 10ⁿ) = (a ÷ b) × 10⁽ᵐ⁻ⁿ⁾

Ordem de Grandeza:
N × 10ⁿ
Se N < √10 (≈ 3,16) → 10ⁿ
Se N ≥ √10 (≈ 3,16) → 10ⁿ⁺¹

Constantes úteis:
Velocidade da luz: c = 3 × 10⁸ m/s
Massa do elétron: mₑ = 9,11 × 10⁻³¹ kg
Carga do elétron: e = 1,6 × 10⁻¹⁹ C
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (importante - frequente em questões de Ciências da Natureza)

## Aula 8 - Física: Cinemática - MRU (Movimento Retilíneo Uniforme) - 90min

### O que é Cinemática?

**Cinemática** é o ramo da Física que estuda o movimento dos corpos sem se preocupar com as causas (forças). Foca em descrever **como** os corpos se movem.

**Grandezas cinemáticas:**
- Posição
- Deslocamento
- Velocidade
- Aceleração
- Tempo

### Conceitos Fundamentais

#### Referencial

**Definição:** Sistema de coordenadas em relação ao qual descrevemos o movimento.

**Importância:** O movimento é relativo - depende do referencial escolhido.

**Exemplo:**
- Você sentado em um trem em movimento:
  - Em relação ao trem: está parado
  - Em relação à Terra: está em movimento

#### Trajetória

**Definição:** Linha que une todas as posições ocupadas pelo corpo durante o movimento.

**Tipos:**
- Retilínea (linha reta)
- Curvilínea (curva)
- Circular

**Depende do referencial:** A trajetória pode mudar conforme o referencial.

#### Posição (S)

**Definição:** Localização do corpo em relação ao referencial.

**Unidade SI:** metro (m)

**Notação:**
- S = posição em instante genérico
- S₀ = posição inicial (em t = 0)
- S_f = posição final

**Exemplo:**
```
Origem (0)     10m      20m      30m
    |-----------|---------|---------|
              S₀=10m            S=25m
```

#### Deslocamento (ΔS)

**Definição:** Variação de posição entre dois instantes.

**Fórmula:**
```
ΔS = S_f - S₀
```

**Características:**
- Pode ser positivo (movimento no sentido positivo)
- Pode ser negativo (movimento no sentido negativo)
- Pode ser zero (voltou à posição inicial)

**Diferença entre deslocamento e distância percorrida:**
- **Deslocamento:** variação de posição (vetorial)
- **Distância percorrida:** total percorrido (escalar)

**Exemplo:**
Uma pessoa sai da posição 10 m, vai até 30 m e volta para 15 m.
- Distância percorrida: 20 m + 15 m = 35 m
- Deslocamento: 15 m - 10 m = 5 m

#### Velocidade

**Definição:** Grandeza que indica a rapidez e o sentido do movimento.

**Unidade SI:** m/s (metro por segundo)

**Outras unidades:** km/h, cm/s

**Conversão importante:**
- 1 m/s = 3,6 km/h
- 1 km/h = 1/3,6 m/s ≈ 0,278 m/s

**Para converter:**
- km/h → m/s: dividir por 3,6
- m/s → km/h: multiplicar por 3,6

### Movimento Retilíneo Uniforme (MRU)

#### Definição

**MRU** é o movimento em que:
- Trajetória é uma **reta**
- Velocidade é **constante** (não muda)
- Não há aceleração (a = 0)

**Características:**
- Percorre distâncias iguais em intervalos de tempo iguais
- Velocidade instantânea = velocidade média

#### Velocidade no MRU

Como a velocidade é constante:

**v = constante**

**Fórmula da velocidade:**
```
v = ΔS / Δt

Onde:
- v = velocidade (m/s ou km/h)
- ΔS = deslocamento (m ou km)
- Δt = intervalo de tempo (s ou h)
```

**Desenvolvendo:**
```
v = (S - S₀) / (t - t₀)

Se t₀ = 0:
v = (S - S₀) / t
```

#### Função Horária da Posição no MRU

**Equação fundamental do MRU:**
```
S = S₀ + vt

Onde:
- S = posição final (m)
- S₀ = posição inicial (m)
- v = velocidade (m/s)
- t = tempo (s)
```

**Esta é uma função do 1º grau:** S(t) = S₀ + vt

**Significado dos termos:**
- **S₀:** posição quando t = 0 (coeficiente linear)
- **v:** velocidade (coeficiente angular - inclinação da reta)

#### Gráficos do MRU

### 1. Gráfico S × t (Posição × Tempo)

**Característica:** Reta (função do 1º grau)

```
S ↑
  |      /
  |    /    ← v > 0 (movimento progressivo)
  |  /
  |/___________→ t
 S₀

S ↑
  |\
  |  \      ← v < 0 (movimento retrógrado)
  |    \
  |______\_____→ t
        S₀
```

**Interpretações:**
- **Inclinação (coeficiente angular):** valor da velocidade
  - Reta mais inclinada = maior velocidade
  - Inclinação positiva = v > 0
  - Inclinação negativa = v < 0
  
- **Coeficiente linear:** posição inicial (S₀)

- **Velocidade a partir do gráfico:**
  ```
  v = ΔS / Δt = (S₂ - S₁) / (t₂ - t₁)
  ```

### 2. Gráfico v × t (Velocidade × Tempo)

**Característica:** Reta horizontal (velocidade constante)

```
v ↑
  |________
  |        |______→ t
  0
  
Velocidade constante = MRU
```

**Área sob o gráfico:**
A área entre a reta e o eixo do tempo representa o **deslocamento**.

```
Área = base × altura = t × v = ΔS
```

### Movimento Progressivo e Retrógrado

#### Movimento Progressivo
- **v > 0** (velocidade positiva)
- Corpo se afasta da origem
- Posição aumenta com o tempo

#### Movimento Retrógrado
- **v < 0** (velocidade negativa)
- Corpo se aproxima da origem
- Posição diminui com o tempo

**Observação:** O sinal da velocidade indica o sentido, não se o corpo está "rápido" ou "lento".

### Encontro de Móveis

Dois móveis se encontram quando ocupam a mesma posição no mesmo instante.

**Condição de encontro:**
```
S₁ = S₂
```

**Método:**
1. Escrever a função horária de cada móvel
2. Igualar as posições
3. Resolver a equação para encontrar t
4. Substituir t em uma das equações para encontrar S

**Exemplo:**
Móvel A: S_A = 10 + 5t
Móvel B: S_B = 50 + 2t

Encontro:
```
10 + 5t = 50 + 2t
5t - 2t = 50 - 10
3t = 40
t = 40/3 ≈ 13,3 s

Posição do encontro:
S = 10 + 5(40/3) = 10 + 200/3 ≈ 76,7 m
```

### Exercícios Resolvidos

#### Exercício 1
Um carro percorre 180 km em 2 horas. Qual sua velocidade média?

**Solução:**
```
v = ΔS / Δt
v = 180 km / 2 h
v = 90 km/h
```

**Em m/s:**
```
v = 90 / 3,6 = 25 m/s
```

#### Exercício 2
Um móvel parte da posição 20 m com velocidade constante de 5 m/s. Determine:
a) A função horária da posição
b) A posição em t = 10 s
c) O instante em que passa pela posição 70 m

**Solução:**

a) **Função horária:**
```
S = S₀ + vt
S = 20 + 5t
```

b) **Posição em t = 10 s:**
```
S = 20 + 5(10)
S = 20 + 50
S = 70 m
```

c) **Instante em que S = 70 m:**
```
70 = 20 + 5t
50 = 5t
t = 10 s
```

#### Exercício 3
Dois carros partem simultaneamente de posições diferentes. O carro A parte da posição 0 com velocidade 20 m/s. O carro B parte da posição 100 m com velocidade 15 m/s, ambos no mesmo sentido. Quando e onde o carro A alcança o carro B?

**Solução:**

Funções horárias:
```
Carro A: S_A = 0 + 20t = 20t
Carro B: S_B = 100 + 15t
```

Encontro (S_A = S_B):
```
20t = 100 + 15t
20t - 15t = 100
5t = 100
t = 20 s
```

Posição do encontro:
```
S = 20(20) = 400 m
```

**Resposta:** Os carros se encontram após 20 s na posição 400 m.

#### Exercício 4
Um trem de 200 m de comprimento atravessa uma ponte de 300 m com velocidade constante de 20 m/s. Quanto tempo leva para atravessar completamente a ponte?

**Solução:**

Para atravessar completamente, o trem deve percorrer:
```
Distância = comprimento da ponte + comprimento do trem
ΔS = 300 + 200 = 500 m
```

Tempo:
```
v = ΔS / Δt
20 = 500 / Δt
Δt = 500 / 20
Δt = 25 s
```

**Resposta:** 25 segundos

#### Exercício 5
Converta 108 km/h para m/s.

**Solução:**
```
v = 108 / 3,6 = 30 m/s
```

#### Exercício 6
Um gráfico S × t mostra uma reta que passa pelos pontos (0, 10) e (5, 35). Determine:
a) A posição inicial
b) A velocidade
c) A função horária

**Solução:**

a) **Posição inicial:** S₀ = 10 m (quando t = 0)

b) **Velocidade:**
```
v = ΔS / Δt = (35 - 10) / (5 - 0)
v = 25 / 5
v = 5 m/s
```

c) **Função horária:**
```
S = S₀ + vt
S = 10 + 5t
```

### Aplicações Práticas do MRU

**1. Esteiras rolantes:** movimento uniforme
**2. Trens e metrôs:** aproximação de MRU em trechos retos
**3. Objetos em órbita:** movimento aproximadamente uniforme
**4. Luz no vácuo:** MRU perfeito (c = 3 × 10⁸ m/s)

### Dicas para a Prova

1. **Conversão:** Sempre verifique as unidades! km/h ↔ m/s (÷ ou × 3,6)
2. **Sinais:** Velocidade negativa = movimento retrógrado
3. **Gráfico S×t:** Inclinação = velocidade
4. **Gráfico v×t:** Área = deslocamento
5. **Encontro:** Igualar as posições (S₁ = S₂)
6. **Distância vs Deslocamento:** Cuidado com a diferença
7. **Função horária:** S = S₀ + vt (sempre!)

### Conceitos-Chave para Memorizar

**MRU:**
- Movimento retilíneo
- Velocidade constante
- Aceleração = 0
- Distâncias iguais em tempos iguais

**Fórmulas:**
- v = ΔS / Δt
- S = S₀ + vt

**Gráficos:**
- **S × t:** reta inclinada
- **v × t:** reta horizontal

**Sinais:**
- v > 0: progressivo (afasta da origem)
- v < 0: retrógrado (aproxima da origem)

### Fórmulas Essenciais

```
Velocidade (constante no MRU):
v = ΔS / Δt = (S - S₀) / t

Função Horária da Posição:
S = S₀ + vt

Conversão de unidades:
1 m/s = 3,6 km/h
km/h → m/s: dividir por 3,6
m/s → km/h: multiplicar por 3,6

Encontro de móveis:
S₁ = S₂
(igualar as funções horárias)

Deslocamento:
ΔS = S_final - S_inicial

Área no gráfico v×t:
Área = deslocamento = v × t
```

### Resumo Visual

```
MRU - Características:
┌─────────────────────────────────┐
│ Trajetória: RETA                │
│ Velocidade: CONSTANTE           │
│ Aceleração: ZERO                │
│ Equação: S = S₀ + vt           │
└─────────────────────────────────┘

Gráfico S×t        Gráfico v×t
    S ↑                v ↑
      |  /               |____
      | /                |    
      |/___→ t           |____→ t
     S₀                  0
   (reta)            (horizontal)
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base para toda cinemática)

## Aula 9 - Química: Modelos Atômicos - 90min

### Evolução Histórica dos Modelos Atômicos

Os modelos atômicos evoluíram ao longo do tempo conforme novas descobertas científicas foram feitas. Cada modelo representou um avanço na compreensão da estrutura da matéria.

### 1. Modelo de Dalton (1803) - "Bola de Bilhar"

#### Contexto Histórico
John Dalton foi o primeiro a propor um modelo atômico baseado em evidências experimentais, retomando a ideia dos filósofos gregos Leucipo e Demócrito.

#### Características do Modelo

**Postulados de Dalton:**
1. Toda matéria é formada por átomos
2. Átomos são partículas **indivisíveis** e **indestrutíveis**
3. Átomos de um mesmo elemento são **idênticos** (mesma massa e propriedades)
4. Átomos de elementos diferentes têm massas e propriedades diferentes
5. Átomos se combinam em proporções fixas para formar compostos
6. Numa reação química, átomos são **rearranjados**, não criados ou destruídos

#### Representação

```
    ○
  Esfera
  maciça,
  indivisível
```

**Analogia:** Bola de bilhar sólida e indivisível

#### Acertos
- Átomos realmente existem
- Átomos de um elemento são praticamente idênticos
- Lei da conservação da massa
- Leis das proporções definidas

#### Limitações
- Átomo **não** é indivisível (possui partículas subatômicas)
- **Não** explica fenômenos elétricos
- **Não** explica a existência de íons
- **Não** considera isótopos (átomos do mesmo elemento com massas diferentes)

### 2. Modelo de Thomson (1897) - "Pudim de Passas"

#### Descoberta do Elétron

J.J. Thomson descobriu o **elétron** usando tubo de raios catódicos, provando que o átomo **não** é indivisível.

**Experimento:**
- Raios catódicos (feixes de elétrons) eram desviados por campos elétricos
- Demonstrou que existem partículas negativas menores que o átomo

#### Características do Modelo

**Descrição:**
- Átomo é uma **esfera positiva** (como o pudim)
- **Elétrons** (negativos) estão **incrustados** na esfera (como passas no pudim)
- Átomo é **eletricamente neutro** (carga positiva = carga negativa)

#### Representação

```
    ╭─────╮
   │ e⁻ e⁻ │
   │e⁻   e⁻│  ← Esfera positiva
   │ e⁻ e⁻ │     com elétrons
    ╰─────╯      dispersos
```

**Analogia:** Pudim de passas ou panetone

#### Acertos
- Átomo **possui** partículas subatômicas
- Existência do **elétron**
- Átomo é **eletricamente neutro**

#### Limitações
- **Não** explica a existência do núcleo
- **Não** explica por que elétrons não são atraídos pela carga positiva
- **Não** explica os espectros atômicos
- Experimento de Rutherford provou que estava errado

### 3. Modelo de Rutherford (1911) - "Sistema Planetário"

#### Experimento da Lâmina de Ouro

**Experimento:**
1. Bombardeou uma fina lâmina de ouro com partículas alfa (α - positivas)
2. Maioria das partículas atravessou a lâmina
3. Algumas partículas sofreram pequenos desvios
4. Poucas partículas (1 em 10.000) foram **repelidas** (voltaram)

**Observações:**

```
Partículas α → → → → → →
                ↗  →  ↘
Lâmina de ouro ═════════
                →  →  →

Maioria: atravessa
Algumas: desviam levemente  
Raras: voltam (repelidas)
```

**Conclusões de Rutherford:**
- Átomo é praticamente **vazio** (maioria atravessa)
- Existe um **núcleo** pequeno, denso e **positivo** (repele partículas α)
- Elétrons estão fora do núcleo, em uma **eletrosfera**

#### Características do Modelo

**Descrição:**
- Átomo possui um **núcleo central** pequeno, denso e **positivo**
- **Elétrons** (negativos) giram ao redor do núcleo em **órbitas circulares**
- Átomo é praticamente **vazio**
- A maioria da massa está concentrada no núcleo

#### Representação

```
        e⁻ ←
         ↑
    (+) ← Núcleo (prótons)
         ↓
        e⁻ →
    
  Elétrons orbitando
```

**Analogia:** Sistema solar (sol = núcleo, planetas = elétrons)

#### Acertos
- Existência do **núcleo atômico**
- Átomo é praticamente **vazio**
- **Prótons** no núcleo
- Conceito de **eletrosfera**

#### Limitações
- **Não** explica por que elétrons não caem no núcleo
  - Segundo a física clássica, elétrons em órbita perderiam energia e cairiam no núcleo
- **Não** explica os **espectros** atômicos discretos
- **Não** explica a estabilidade do átomo

**Problema fundamental:**
Elétron em movimento circular emite radiação eletromagnética → perde energia → deveria cair no núcleo (mas não cai!)

### 4. Modelo de Rutherford-Bohr (1913) - "Modelo Quântico"

#### Contexto

Niels Bohr aperfeiçoou o modelo de Rutherford incorporando ideias da **física quântica**.

#### Postulados de Bohr

**1. Órbitas Estacionárias (Níveis de Energia)**
- Elétrons giram em **órbitas circulares** ao redor do núcleo
- Essas órbitas têm **energias definidas** (quantizadas)
- Enquanto na órbita, elétron **não** perde energia (órbita estacionária)

**2. Níveis de Energia (Camadas)**
- Órbitas são chamadas de **níveis de energia** ou **camadas**
- Identificadas por números: n = 1, 2, 3, 4, 5, 6, 7...
- Ou por letras: K, L, M, N, O, P, Q

```
Camadas:  K   L   M   N   O   P   Q
Níveis:   1   2   3   4   5   6   7
Energia: baixa ───────────→ alta
```

**3. Salto Quântico**
- Elétron pode **saltar** de uma órbita para outra
- Ao **absorver** energia: salta para nível mais externo (excitação)
- Ao **emitir** energia: volta para nível mais interno (desexcitação)
- Energia emitida ou absorvida é na forma de **fóton** (luz)

**Fórmula da energia do fóton:**
```
ΔE = E_final - E_inicial = hf

Onde:
- ΔE = variação de energia
- h = constante de Planck
- f = frequência da radiação
```

#### Explicação dos Espectros Atômicos

**Espectro de emissão:**
- Elétron excitado volta para nível menor
- Emite luz de frequência específica
- Cada elemento tem espectro único (impressão digital)

```
Elétron salta:
n=3 → n=2: emite luz vermelha
n=4 → n=2: emite luz azul
n=5 → n=2: emite luz violeta
```

#### Distribuição Eletrônica (Diagrama de Linus Pauling)

**Número máximo de elétrons por camada:**
```
Fórmula: 2n²

K (n=1): 2 × 1² = 2 elétrons
L (n=2): 2 × 2² = 8 elétrons
M (n=3): 2 × 3² = 18 elétrons
N (n=4): 2 × 4² = 32 elétrons
```

**Ordem de preenchimento (Diagrama de Pauling):**
```
1s²
2s² 2p⁶
3s² 3p⁶ 3d¹⁰
4s² 4p⁶ 4d¹⁰ 4f¹⁴
5s² 5p⁶ 5d¹⁰ 5f¹⁴
6s² 6p⁶ 6d¹⁰
7s² 7p⁶
```

**Ordem energética:**
1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p < 6s < 4f < 5d < 6p < 7s...

#### Representação

```
        n=3 ─────○
       n=2 ───○
      n=1 ─○
         (+)
    
  Níveis quantizados
  Saltos quânticos
```

#### Acertos
- Explica os **espectros** atômicos
- Explica a **estabilidade** do átomo
- Conceito de **níveis de energia**
- Quantização da energia

#### Limitações
- Funciona bem só para **hidrogênio** (1 elétron)
- **Não** explica átomos com muitos elétrons
- Órbitas circulares são uma simplificação
- Substituído por modelos quânticos mais complexos

### 5. Modelo Quântico Atual (Schrödinger, 1926)

#### Desenvolvimento

Baseado na **mecânica quântica** desenvolvida por Schrödinger, Heisenberg e outros.

#### Conceitos Principais

**1. Princípio da Incerteza de Heisenberg**
- Impossível determinar simultaneamente posição e velocidade exatas do elétron
- Elétron tem comportamento **dual**: onda e partícula

**2. Orbitais (Nuvens Eletrônicas)**
- Não existem **órbitas** definidas
- Existem **orbitais**: regiões de probabilidade de encontrar o elétron
- Orbital = nuvem eletrônica onde é provável encontrar elétrons

**3. Números Quânticos**
Quatro números descrevem cada elétron:

**n** = número quântico principal (camada, nível de energia)
- n = 1, 2, 3, 4...

**ℓ** = número quântico secundário (subcamada, formato do orbital)
- ℓ = 0, 1, 2, 3... (n-1)
- s (ℓ=0), p (ℓ=1), d (ℓ=2), f (ℓ=3)

**m** = número quântico magnético (orientação do orbital)
- m = -ℓ ... 0 ... +ℓ

**s** = número quântico spin (rotação do elétron)
- s = +½ ou -½

**Formas dos orbitais:**
- **s:** esférico (1 orbital)
- **p:** halteres (3 orbitais)
- **d:** complexo (5 orbitais)
- **f:** muito complexo (7 orbitais)

#### Acertos
- Modelo atual, mais preciso
- Explica todos os átomos
- Base da química moderna
- Prediz ligações químicas

### Partículas Subatômicas

| Partícula | Símbolo | Carga | Massa | Localização |
|-----------|---------|-------|-------|-------------|
| **Próton** | p⁺ | +1 | 1 u | Núcleo |
| **Nêutron** | n⁰ | 0 | 1 u | Núcleo |
| **Elétron** | e⁻ | -1 | ~1/1836 u | Eletrosfera |

**Observações:**
- Prótons e nêutrons têm massa similar (~1 u)
- Elétron tem massa desprezível comparado ao próton
- Átomo neutro: nº prótons = nº elétrons
- Número de massa A = prótons + nêutrons

### Comparação dos Modelos

| Modelo | Ano | Principais Características |
|--------|-----|---------------------------|
| **Dalton** | 1803 | Esfera maciça indivisível |
| **Thomson** | 1897 | Pudim de passas, descobriu elétron |
| **Rutherford** | 1911 | Núcleo positivo + eletrosfera |
| **Bohr** | 1913 | Níveis de energia, saltos quânticos |
| **Quântico** | 1926 | Orbitais, mecânica quântica |

### Exercícios Resolvidos

#### Exercício 1
Qual modelo atômico compara o átomo a um "pudim de passas"?

**Resposta:** Modelo de Thomson

#### Exercício 2
Qual experimento levou Rutherford a propor o núcleo atômico?

**Resposta:** Experimento da lâmina de ouro (bombardeamento com partículas alfa)

#### Exercício 3
Explique por que o modelo de Rutherford não explicava a estabilidade do átomo.

**Resposta:** Segundo a física clássica, elétrons em movimento circular deveriam emitir radiação eletromagnética, perder energia e cair no núcleo. Como isso não acontece, o modelo não explicava por que o átomo é estável.

#### Exercício 4
Qual modelo introduziu o conceito de níveis de energia quantizados?

**Resposta:** Modelo de Bohr (Rutherford-Bohr)

#### Exercício 5
Quantos elétrons cabem na camada M (n=3)?

**Solução:**
```
2n² = 2 × 3² = 2 × 9 = 18 elétrons
```

**Resposta:** 18 elétrons

#### Exercício 6
Identifique o erro: "No modelo de Dalton, o átomo possui prótons e elétrons."

**Resposta:** ERRO. No modelo de Dalton, o átomo era considerado indivisível, portanto não possuía partículas subatômicas. Os prótons e elétrons foram descobertos posteriormente (elétron por Thomson, próton por Rutherford).

### Dicas para a Prova

1. **Ordem cronológica:** Dalton → Thomson → Rutherford → Bohr → Quântico
2. **Dalton:** indivisível (errado depois)
3. **Thomson:** descobriu o elétron, pudim de passas
4. **Rutherford:** núcleo positivo, experimento da lâmina de ouro
5. **Bohr:** níveis de energia, espectros atômicos
6. **Quântico:** orbitais, nuvens eletrônicas
7. **Camadas:** 2n² elétrons no máximo
8. **Cada modelo melhorou o anterior**, não invalidou completamente

### Conceitos-Chave para Memorizar

**Evolução:**
Dalton → Thomson → Rutherford → Bohr → Quântico

**Cada modelo:**
- **Dalton:** bola de bilhar
- **Thomson:** pudim de passas (descobriu e⁻)
- **Rutherford:** núcleo + eletrosfera (lâmina de ouro)
- **Bohr:** níveis de energia (espectros)
- **Quântico:** orbitais (atual)

**Partículas:**
- **Próton:** carga +1, massa 1 u, núcleo
- **Nêutron:** carga 0, massa 1 u, núcleo
- **Elétron:** carga -1, massa ≈0, eletrosfera

**Camadas:**
- K, L, M, N, O, P, Q
- Máximo: 2n²

### Linha do Tempo Essencial

```
1803 - Dalton: átomo indivisível
         ↓
1897 - Thomson: descobre elétron
         ↓
1911 - Rutherford: núcleo atômico
         ↓
1913 - Bohr: níveis de energia
         ↓
1926 - Quântico: orbitais
```

### Tabela Resumo

```
┌─────────────┬──────────────────────────┐
│   Modelo    │    Característica        │
├─────────────┼──────────────────────────┤
│ Dalton      │ Esfera maciça            │
│ Thomson     │ Pudim de passas + e⁻     │
│ Rutherford  │ Núcleo + eletrosfera     │
│ Bohr        │ Órbitas quantizadas      │
│ Quântico    │ Orbitais/nuvens (atual)  │
└─────────────┴──────────────────────────┘
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base para química geral)

## Aula 10 - Filosofia: Lógica - Argumento, Validade e Falácia - 60min

### O que é Lógica?

**Lógica** é o ramo da Filosofia que estuda os princípios do raciocínio correto e da argumentação válida.

**Objetivo da lógica:**
- Distinguir raciocínios válidos de raciocínios inválidos
- Analisar a estrutura dos argumentos
- Identificar erros de raciocínio (falácias)

**Importância:**
- Fundamental para o pensamento crítico
- Base da matemática, ciências e filosofia
- Ajuda a evitar manipulações argumentativas
- Essencial para debates e discussões racionais

### O que é um Argumento?

**Argumento** é um conjunto de proposições (afirmações) em que algumas (premissas) servem de razão ou justificativa para outra (conclusão).

**Estrutura básica:**
```
Premissa 1
Premissa 2
...
Premissa n
─────────────
Conclusão
```

**Exemplo:**
```
Premissa 1: Todos os homens são mortais
Premissa 2: Sócrates é homem
─────────────────────────────────────
Conclusão: Logo, Sócrates é mortal
```

### Proposições

**Proposição** é uma afirmação que pode ser verdadeira ou falsa.

**Características:**
- Expressa um conteúdo que pode ser julgado (verdadeiro ou falso)
- Declarativa (afirmativa ou negativa)
- Não é pergunta, ordem ou exclamação

**Exemplos de proposições:**
- "O céu é azul" (verdadeiro)
- "2 + 2 = 5" (falso)
- "Brasília é a capital do Brasil" (verdadeiro)

**Não são proposições:**
- "Que horas são?" (pergunta)
- "Feche a porta!" (ordem)
- "Que lindo!" (exclamação)
- "x > 5" (sentença aberta - depende do valor de x)

### Premissas e Conclusão

#### Premissas
- São as **razões** ou **evidências** apresentadas
- Servem de **suporte** para a conclusão
- Podem ser verdadeiras ou falsas

#### Conclusão
- É a **afirmação** que se pretende estabelecer
- Aquilo que se quer **provar** ou **demonstrar**
- Deve ser apoiada pelas premissas

**Indicadores de premissas:**
- porque, pois, uma vez que, dado que, visto que, já que

**Indicadores de conclusão:**
- logo, portanto, então, assim, consequentemente, por isso

**Exemplo:**
"**Visto que** todos os mamíferos são animais de sangue quente **e** as baleias são mamíferos, **logo** as baleias são animais de sangue quente."

- Premissa 1: Todos os mamíferos são animais de sangue quente
- Premissa 2: As baleias são mamíferos
- Conclusão: As baleias são animais de sangue quente

### Validade de um Argumento

**Argumento válido:** É aquele em que, **se** as premissas forem verdadeiras, a conclusão **necessariamente** será verdadeira.

**Importante:** 
- Validade é sobre a **estrutura** do argumento, não sobre a verdade das premissas
- Um argumento pode ser válido mesmo com premissas falsas
- O que importa é: **SE** as premissas fossem verdadeiras, a conclusão seria verdadeira?

#### Exemplo de Argumento Válido

```
Premissa 1: Todos os cães são mamíferos
Premissa 2: Rex é um cão
───────────────────────────────────
Conclusão: Rex é mamífero
```

**Válido:** Se as premissas são verdadeiras, a conclusão necessariamente é verdadeira.

#### Exemplo de Argumento Inválido

```
Premissa 1: Todos os cães são mamíferos
Premissa 2: Rex é mamífero
───────────────────────────────────
Conclusão: Rex é cão
```

**Inválido:** Mesmo que as premissas sejam verdadeiras, a conclusão pode ser falsa (Rex pode ser um gato, por exemplo).

### Verdade vs Validade

**Diferença crucial:**

| Conceito | Aplica-se a | Significado |
|----------|-------------|-------------|
| **Verdade** | Proposições | Uma afirmação corresponde à realidade |
| **Validade** | Argumentos | A conclusão decorre logicamente das premissas |

**Possibilidades:**

1. **Argumento válido com premissas e conclusão verdadeiras** ✓ (ideal - argumento sólido)
2. **Argumento válido com premissas falsas e conclusão verdadeira** (válido, mas não confiável)
3. **Argumento válido com premissas falsas e conclusão falsa** (válido, mas não confiável)
4. **Argumento inválido** (independente da verdade das proposições)

**Exemplo de argumento válido mas com premissa falsa:**
```
Premissa 1: Todos os peixes voam (FALSO)
Premissa 2: O tubarão é um peixe (VERDADEIRO)
────────────────────────────────────────────
Conclusão: O tubarão voa (FALSO)
```
**Válido:** SE a premissa 1 fosse verdadeira, a conclusão seria verdadeira. A estrutura é correta.

### Argumento Sólido (Sound)

**Argumento sólido** = argumento **válido** + premissas **verdadeiras**

É o argumento ideal:
- Estrutura correta (válido)
- Premissas verdadeiras
- Conclusão necessariamente verdadeira

### Tipos de Argumentos

#### 1. Argumento Dedutivo

**Definição:** A conclusão está **contida** nas premissas; a conclusão não traz informação nova.

**Característica:** Se válido e premissas verdadeiras, conclusão é **necessariamente** verdadeira.

**Exemplo:**
```
Todos os A são B
x é A
────────────
x é B
```

**Exemplo concreto:**
```
Todos os metais conduzem eletricidade
O cobre é metal
───────────────────────────────────
O cobre conduz eletricidade
```

#### 2. Argumento Indutivo

**Definição:** A conclusão **generaliza** a partir de casos particulares; traz informação nova.

**Característica:** Mesmo com premissas verdadeiras, conclusão é apenas **provável**.

**Exemplo:**
```
Cisne 1 é branco
Cisne 2 é branco
Cisne 3 é branco
(observei 1000 cisnes brancos)
──────────────────────────────
Todos os cisnes são brancos (?)
```

**Problema:** Pode ser refutado por um contraexemplo (cisnes negros existem na Austrália).

#### 3. Argumento por Analogia

**Definição:** Conclui que algo é verdadeiro com base em semelhanças com outra situação.

**Exemplo:**
```
A Terra tem água e vida
Marte tem (ou teve) água
───────────────────────────
Marte pode ter (ou ter tido) vida
```

### Falácias

**Falácia** é um erro de raciocínio que torna um argumento inválido, mesmo que pareça convincente.

**Tipos principais:**

#### 1. Falácia do Apelo à Autoridade (Ad Verecundiam)

**Erro:** Aceitar algo como verdadeiro apenas porque uma autoridade disse, sem analisar os argumentos.

**Exemplo:**
"O ator famoso X disse que este produto emagrece, então deve ser verdade."

**Por que é falácia:** Atores não são especialistas em nutrição.

**Quando NÃO é falácia:** Citar um especialista relevante com argumento ("Segundo o oncologista Dr. Y, fumar aumenta risco de câncer porque...")

#### 2. Falácia Ad Hominem (Ataque à Pessoa)

**Erro:** Atacar a pessoa em vez de refutar o argumento.

**Exemplo:**
"Você não pode falar sobre honestidade porque já foi preso."

**Por que é falácia:** A validade do argumento independe de quem o apresenta.

#### 3. Falácia do Apelo à Emoção (Ad Misericordiam, Ad Populum)

**Erro:** Usar emoções (piedade, medo, popularidade) em vez de razões lógicas.

**Exemplos:**
- **Ad Misericordiam (piedade):** "Professor, não me reprove, minha mãe vai ficar muito triste!"
- **Ad Populum (popularidade):** "Todo mundo usa drogas, logo não é errado."
- **Apelo ao medo:** "Se você não votar em mim, o país vai acabar!"

#### 4. Petição de Princípio (Raciocínio Circular)

**Erro:** A conclusão já está pressuposta nas premissas.

**Exemplo:**
"Deus existe porque está escrito na Bíblia, e a Bíblia é verdadeira porque é a palavra de Deus."

**Por que é falácia:** Usa a conclusão (Deus existe) para justificar a premissa (Bíblia é verdadeira).

#### 5. Falsa Causa (Post Hoc Ergo Propter Hoc)

**Erro:** Assumir que porque B veio depois de A, então A causou B.

**Exemplo:**
"Usei este amuleto e passei na prova, logo o amuleto me deu sorte."

**Por que é falácia:** Correlação não implica causalidade.

#### 6. Falso Dilema (Falsa Dicotomia)

**Erro:** Apresentar apenas duas opções quando existem mais.

**Exemplo:**
"Ou você está comigo ou contra mim."

**Por que é falácia:** Pode-se ser neutro, ou ter posição intermediária.

#### 7. Generalização Apressada

**Erro:** Concluir algo geral a partir de poucos casos.

**Exemplo:**
"Conheci dois franceses arrogantes, logo todos os franceses são arrogantes."

**Por que é falácia:** Amostra muito pequena para generalizar.

#### 8. Espantalho (Straw Man)

**Erro:** Distorcer o argumento do oponente para atacar uma versão mais fraca.

**Exemplo:**
- A: "Devemos ter controle de armas mais rigoroso."
- B: "Você quer desarmar toda a população e deixar todos indefesos!"

**Por que é falácia:** B distorceu o argumento de A.

#### 9. Derrapagem (Slippery Slope)

**Erro:** Afirmar que uma ação levará inevitavelmente a consequências extremas.

**Exemplo:**
"Se legalizarmos a maconha, em breve terão cocaína e heroína em todas as esquinas!"

**Por que é falácia:** Não há necessariamente essa cadeia inevitável.

### Princípios Lógicos Fundamentais

#### 1. Princípio da Identidade
**A é A**

Uma coisa é igual a si mesma.

#### 2. Princípio da Não-Contradição
**A não pode ser A e não-A ao mesmo tempo e no mesmo sentido**

Uma proposição não pode ser verdadeira e falsa simultaneamente.

**Exemplo:** "Está chovendo" e "Não está chovendo" não podem ser ambas verdadeiras ao mesmo tempo no mesmo lugar.

#### 3. Princípio do Terceiro Excluído
**Ou A ou não-A (não há terceira opção)**

Uma proposição é verdadeira ou falsa, não há meio termo.

### Exercícios Resolvidos

#### Exercício 1
Identifique as premissas e a conclusão:
"Todos os mamíferos têm coração. As baleias são mamíferos. Portanto, as baleias têm coração."

**Resposta:**
- Premissa 1: Todos os mamíferos têm coração
- Premissa 2: As baleias são mamíferos
- Conclusão: As baleias têm coração

#### Exercício 2
O argumento abaixo é válido ou inválido?
"Todos os gatos são felinos. Todos os felinos são carnívoros. Logo, todos os gatos são carnívoros."

**Resposta:** **Válido.** Se as premissas são verdadeiras, a conclusão necessariamente é verdadeira.

#### Exercício 3
Identifique a falácia: "Você não pode criticar o governo porque não é político."

**Resposta:** **Ad Hominem** (ataque à pessoa). O fato de não ser político não invalida a crítica.

#### Exercício 4
Identifique a falácia: "Ou você apoia este projeto ou é contra o progresso da cidade."

**Resposta:** **Falso Dilema**. Pode-se ter ressalvas ao projeto sem ser contra o progresso.

#### Exercício 5
Este argumento é válido? "Alguns políticos são corruptos. João é político. Logo, João é corrupto."

**Resposta:** **Inválido.** "Alguns" não significa "todos". João pode ser um político honesto.

### Dicas para a Prova

1. **Validade ≠ Verdade:** Validade é estrutura; verdade é correspondência com a realidade
2. **Identifique indicadores:** "logo", "portanto" → conclusão; "porque", "pois" → premissa
3. **Falácias comuns:** Ad Hominem, Apelo à Autoridade, Falso Dilema
4. **Argumento válido:** SE premissas verdadeiras → conclusão necessariamente verdadeira
5. **Argumento sólido:** Válido + premissas verdadeiras
6. **Atenção a "todos", "alguns", "nenhum":** mudam completamente a validade

### Conceitos-Chave para Memorizar

**Argumento:**
- Premissas (razões) + Conclusão (o que se quer provar)

**Validade:**
- Estrutura correta
- SE premissas verdadeiras → conclusão necessariamente verdadeira
- Não depende da verdade das premissas

**Argumento Sólido:**
- Válido + Premissas verdadeiras

**Falácias principais:**
- **Ad Hominem:** ataca a pessoa
- **Apelo à Autoridade:** autoridade sem expertise
- **Apelo à Emoção:** manipula emoções
- **Falso Dilema:** só duas opções (quando há mais)
- **Petição de Princípio:** circular
- **Falsa Causa:** confunde correlação com causalidade
- **Espantalho:** distorce argumento alheio

### Tabela Resumo

```
┌──────────────────┬───────────────────────────┐
│    Conceito      │        Definição          │
├──────────────────┼───────────────────────────┤
│ Proposição       │ Afirmação V ou F          │
│ Premissa         │ Razão/suporte             │
│ Conclusão        │ O que se quer provar      │
│ Validade         │ Estrutura correta         │
│ Verdade          │ Corresponde à realidade   │
│ Argumento Sólido │ Válido + premissas V      │
│ Falácia          │ Erro de raciocínio        │
└──────────────────┴───────────────────────────┘
```

### Estrutura Básica de Análise

**Para analisar um argumento:**

1. **Identificar:** Quais são as premissas? Qual é a conclusão?
2. **Avaliar a validade:** A conclusão decorre logicamente das premissas?
3. **Avaliar a verdade:** As premissas são verdadeiras?
4. **Identificar falácias:** Há erros de raciocínio?
5. **Conclusão:** O argumento é sólido (válido + premissas verdadeiras)?

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (importante - pensamento crítico é essencial)

---

# 11/20 - Dia 3

## Aula 11 - Matemática: Expressões Algébricas, Produtos Notáveis e Fatoração - 120min

### O que são Expressões Algébricas?

**Expressão algébrica** é uma combinação de números, letras (variáveis) e operações matemáticas (+, -, ×, ÷, potenciação, radiciação).

**Exemplos:**
- 2x + 3
- x² - 5x + 6
- 3ab - 2a + b
- (x + y)²

**Termos:**
- **Variável:** Letra que representa um número desconhecido (x, y, a, b, etc.)
- **Coeficiente:** Número que multiplica a variável
- **Termo:** Parte da expressão separada por + ou -
- **Monômio:** Expressão com um único termo
- **Polinômio:** Expressão com dois ou mais termos

### Monômios

**Definição:** Expressão algébrica com apenas um termo.

**Estrutura:** coeficiente × parte literal

**Exemplos:**
- 5x (coeficiente 5, parte literal x)
- -3x² (coeficiente -3, parte literal x²)
- 2ab³ (coeficiente 2, parte literal ab³)
- 7 (monômio constante)

**Grau do monômio:** Soma dos expoentes das variáveis.

**Exemplos:**
- 5x → grau 1
- 3x² → grau 2
- 2x³y² → grau 5 (3+2)
- -4a²b³c → grau 6 (2+3+1)

### Operações com Monômios

#### Adição e Subtração

**Regra:** Só podemos somar/subtrair monômios **semelhantes** (mesma parte literal).

**Exemplos:**

**Semelhantes (podem somar/subtrair):**
- 3x + 5x = 8x
- 7x² - 2x² = 5x²
- 4ab + 3ab - ab = 6ab

**Não semelhantes (NÃO podem somar/subtrair):**
- 3x + 5y (não dá para simplificar)
- 2x² + 3x (não dá para simplificar)

#### Multiplicação

**Regra:**
1. Multiplicar os coeficientes
2. Multiplicar as partes literais (somar os expoentes de mesma base)

**Exemplos:**
- (3x) · (2x) = 6x²
- (2x²) · (4x³) = 8x⁵
- (5a) · (2b) = 10ab
- (2x²y) · (3xy²) = 6x³y³

#### Divisão

**Regra:**
1. Dividir os coeficientes
2. Dividir as partes literais (subtrair os expoentes de mesma base)

**Exemplos:**
- 12x⁵ ÷ 3x² = 4x³
- 8x³y² ÷ 2xy = 4x²y
- 15a⁴ ÷ 5a² = 3a²

### Polinômios

**Definição:** Expressão algébrica com dois ou mais termos.

**Tipos especiais:**
- **Binômio:** 2 termos (x + 3, a - b)
- **Trinômio:** 3 termos (x² + 2x + 1)

**Grau do polinômio:** Maior grau entre seus termos.

**Exemplo:**
P(x) = 3x⁴ - 2x³ + x - 5

- Termos: 3x⁴, -2x³, x, -5
- Graus: 4, 3, 1, 0
- **Grau do polinômio: 4**

### Operações com Polinômios

#### Adição e Subtração

**Regra:** Somar/subtrair termos semelhantes.

**Exemplo 1:**
(3x² + 2x - 1) + (x² - 5x + 3)

= 3x² + x² + 2x - 5x - 1 + 3
= 4x² - 3x + 2

**Exemplo 2:**
(5x² + 3x - 2) - (2x² - x + 4)

= 5x² + 3x - 2 - 2x² + x - 4
= 3x² + 4x - 6

**Atenção:** Ao subtrair, troque todos os sinais do segundo polinômio!

#### Multiplicação

**Regra:** Multiplicar cada termo do primeiro polinômio por cada termo do segundo (propriedade distributiva).

**Exemplo 1:** Monômio × Polinômio
2x · (3x² - 5x + 1)

= 2x · 3x² + 2x · (-5x) + 2x · 1
= 6x³ - 10x² + 2x

**Exemplo 2:** Binômio × Binômio
(x + 3)(x + 2)

= x · x + x · 2 + 3 · x + 3 · 2
= x² + 2x + 3x + 6
= x² + 5x + 6

**Exemplo 3:** Binômio × Trinômio
(x + 2)(x² - 3x + 1)

= x · x² + x · (-3x) + x · 1 + 2 · x² + 2 · (-3x) + 2 · 1
= x³ - 3x² + x + 2x² - 6x + 2
= x³ - x² - 5x + 2

### Produtos Notáveis

**Produtos notáveis** são multiplicações de expressões algébricas que aparecem com frequência e têm fórmulas prontas.

### 1. Quadrado da Soma

**(a + b)² = a² + 2ab + b²**

**Em palavras:** "O quadrado do primeiro, mais duas vezes o primeiro vezes o segundo, mais o quadrado do segundo"

**Exemplos:**

**(x + 3)²**
= x² + 2 · x · 3 + 3²
= x² + 6x + 9

**(2x + 5)²**
= (2x)² + 2 · 2x · 5 + 5²
= 4x² + 20x + 25

**(a + b)²**
= a² + 2ab + b²

**Erro comum:** (a + b)² ≠ a² + b²
**Correto:** (a + b)² = a² + 2ab + b²

### 2. Quadrado da Diferença

**(a - b)² = a² - 2ab + b²**

**Em palavras:** "O quadrado do primeiro, menos duas vezes o primeiro vezes o segundo, mais o quadrado do segundo"

**Exemplos:**

**(x - 2)²**
= x² - 2 · x · 2 + 2²
= x² - 4x + 4

**(3x - 4)²**
= (3x)² - 2 · 3x · 4 + 4²
= 9x² - 24x + 16

**(a - b)²**
= a² - 2ab + b²

**Observação:** Note que o último termo é sempre positivo!

### 3. Produto da Soma pela Diferença

**(a + b)(a - b) = a² - b²**

**Em palavras:** "O quadrado do primeiro menos o quadrado do segundo"

**Exemplos:**

**(x + 5)(x - 5)**
= x² - 5²
= x² - 25

**(2x + 3)(2x - 3)**
= (2x)² - 3²
= 4x² - 9

**(7 + y)(7 - y)**
= 7² - y²
= 49 - y²

**Aplicação prática:** Cálculo mental!

**Exemplo:** 103 × 97
= (100 + 3)(100 - 3)
= 100² - 3²
= 10000 - 9
= 9991

### 4. Cubo da Soma

**(a + b)³ = a³ + 3a²b + 3ab² + b³**

**Exemplo:**
(x + 2)³
= x³ + 3x²(2) + 3x(2²) + 2³
= x³ + 6x² + 12x + 8

### 5. Cubo da Diferença

**(a - b)³ = a³ - 3a²b + 3ab² - b³**

**Exemplo:**
(x - 1)³
= x³ - 3x²(1) + 3x(1²) - 1³
= x³ - 3x² + 3x - 1

### Resumo dos Produtos Notáveis

```
(a + b)² = a² + 2ab + b²

(a - b)² = a² - 2ab + b²

(a + b)(a - b) = a² - b²

(a + b)³ = a³ + 3a²b + 3ab² + b³

(a - b)³ = a³ - 3a²b + 3ab² - b³
```

### Fatoração

**Fatoração** é o processo inverso da multiplicação: transformar uma soma/subtração em um produto.

**Por que fatorar?**
- Simplificar expressões
- Resolver equações
- Facilitar cálculos
- Encontrar raízes de funções

### Casos de Fatoração

### 1. Fator Comum em Evidência

**Regra:** Identificar o fator que aparece em todos os termos e colocá-lo em evidência.

**Exemplos:**

**6x + 9**
= 3(2x + 3)  → fator comum: 3

**4x² - 8x**
= 4x(x - 2)  → fator comum: 4x

**3x³ + 6x² - 9x**
= 3x(x² + 2x - 3)  → fator comum: 3x

**ax + ay**
= a(x + y)  → fator comum: a

**Método:**
1. Identificar o maior fator comum (MDC dos coeficientes e menor expoente das variáveis comuns)
2. Dividir cada termo pelo fator comum
3. Escrever como produto

### 2. Agrupamento

**Regra:** Agrupar termos que têm fatores comuns.

**Exemplos:**

**ax + bx + ay + by**
= x(a + b) + y(a + b)
= (a + b)(x + y)

**2x + 2y + mx + my**
= 2(x + y) + m(x + y)
= (x + y)(2 + m)

**x³ + x² + x + 1**
= x²(x + 1) + 1(x + 1)
= (x + 1)(x² + 1)

### 3. Trinômio Quadrado Perfeito

**Regra:** Reconhecer os produtos notáveis de quadrado.

**Forma:** a² + 2ab + b² = (a + b)²
**Forma:** a² - 2ab + b² = (a - b)²

**Como identificar:**
1. Primeiro e último termos são quadrados perfeitos
2. Termo do meio = 2 × √(primeiro) × √(último)

**Exemplos:**

**x² + 6x + 9**
- x² é quadrado de x
- 9 é quadrado de 3
- 6x = 2 · x · 3 ✓
- **Resposta:** (x + 3)²

**x² - 10x + 25**
- x² é quadrado de x
- 25 é quadrado de 5
- 10x = 2 · x · 5 ✓
- **Resposta:** (x - 5)²

**4x² + 12x + 9**
- 4x² é quadrado de 2x
- 9 é quadrado de 3
- 12x = 2 · 2x · 3 ✓
- **Resposta:** (2x + 3)²

### 4. Diferença de Quadrados

**Regra:** a² - b² = (a + b)(a - b)

**Exemplos:**

**x² - 25**
= x² - 5²
= (x + 5)(x - 5)

**9x² - 16**
= (3x)² - 4²
= (3x + 4)(3x - 4)

**a² - b²**
= (a + b)(a - b)

**49 - y²**
= 7² - y²
= (7 + y)(7 - y)

### 5. Trinômio do Tipo x² + Sx + P

**Forma:** x² + Sx + P

**Fatoração:** (x + a)(x + b)

**Onde:**
- S = soma (a + b)
- P = produto (a · b)

**Método:**
1. Encontrar dois números que:
   - **Somados** dão o coeficiente de x
   - **Multiplicados** dão o termo independente
2. Escrever como (x + a)(x + b)

**Exemplos:**

**x² + 7x + 12**

Procurar dois números que:
- Somam 7
- Multiplicam 12

Números: 3 e 4
- 3 + 4 = 7 ✓
- 3 · 4 = 12 ✓

**Resposta:** (x + 3)(x + 4)

**x² - 5x + 6**

Procurar dois números que:
- Somam -5
- Multiplicam 6

Números: -2 e -3
- (-2) + (-3) = -5 ✓
- (-2) · (-3) = 6 ✓

**Resposta:** (x - 2)(x - 3)

**x² + x - 12**

Procurar dois números que:
- Somam 1
- Multiplicam -12

Números: 4 e -3
- 4 + (-3) = 1 ✓
- 4 · (-3) = -12 ✓

**Resposta:** (x + 4)(x - 3)

**x² - 7x + 10**

Números: -5 e -2
- (-5) + (-2) = -7 ✓
- (-5) · (-2) = 10 ✓

**Resposta:** (x - 5)(x - 2)

### 6. Diferença de Cubos

**a³ - b³ = (a - b)(a² + ab + b²)**

**Exemplo:**
x³ - 8
= x³ - 2³
= (x - 2)(x² + 2x + 4)

### 7. Soma de Cubos

**a³ + b³ = (a + b)(a² - ab + b²)**

**Exemplo:**
x³ + 27
= x³ + 3³
= (x + 3)(x² - 3x + 9)

### Exercícios Resolvidos

#### Exercício 1
Desenvolva (2x + 3)²

**Solução:**
(2x + 3)² = (2x)² + 2(2x)(3) + 3²
= 4x² + 12x + 9

#### Exercício 2
Desenvolva (x - 5)(x + 5)

**Solução:**
(x - 5)(x + 5) = x² - 5²
= x² - 25

#### Exercício 3
Fatore: 3x² + 6x

**Solução:**
Fator comum: 3x
3x² + 6x = 3x(x + 2)

#### Exercício 4
Fatore: x² - 16

**Solução:**
Diferença de quadrados:
x² - 16 = x² - 4²
= (x + 4)(x - 4)

#### Exercício 5
Fatore: x² + 8x + 16

**Solução:**
Trinômio quadrado perfeito:
- x² (quadrado de x)
- 16 (quadrado de 4)
- 8x = 2 · x · 4 ✓

x² + 8x + 16 = (x + 4)²

#### Exercício 6
Fatore: x² - 5x - 6

**Solução:**
Procurar dois números que somam -5 e multiplicam -6:
- Números: -6 e 1
- (-6) + 1 = -5 ✓
- (-6) · 1 = -6 ✓

x² - 5x - 6 = (x - 6)(x + 1)

#### Exercício 7
Simplifique: (x + 3)² - (x - 3)²

**Solução:**
Método 1 (desenvolver):
(x + 3)² - (x - 3)²
= (x² + 6x + 9) - (x² - 6x + 9)
= x² + 6x + 9 - x² + 6x - 9
= 12x

Método 2 (diferença de quadrados):
(x + 3)² - (x - 3)²
= [(x+3) + (x-3)][(x+3) - (x-3)]
= [2x][6]
= 12x

#### Exercício 8
Calcule 52² usando produtos notáveis.

**Solução:**
52² = (50 + 2)²
= 50² + 2(50)(2) + 2²
= 2500 + 200 + 4
= 2704

#### Exercício 9
Calcule 98 × 102 usando produtos notáveis.

**Solução:**
98 × 102 = (100 - 2)(100 + 2)
= 100² - 2²
= 10000 - 4
= 9996

#### Exercício 10
Fatore completamente: 2x³ + 8x² + 8x

**Solução:**
Passo 1: Fator comum
2x³ + 8x² + 8x = 2x(x² + 4x + 4)

Passo 2: Trinômio quadrado perfeito
x² + 4x + 4 = (x + 2)²

**Resposta final:** 2x(x + 2)²

### Aplicações Práticas

#### Simplificação de Frações Algébricas

**Exemplo:**
Simplifique: (x² - 9)/(x² + 6x + 9)

**Solução:**
Numerador: x² - 9 = (x + 3)(x - 3)
Denominador: x² + 6x + 9 = (x + 3)²

= (x + 3)(x - 3) / (x + 3)²
= (x - 3) / (x + 3)

#### Resolução de Equações

**Exemplo:**
Resolva: x² - 5x + 6 = 0

**Solução:**
Fatorando: (x - 2)(x - 3) = 0

Para o produto ser zero, um dos fatores deve ser zero:
x - 2 = 0  →  x = 2
ou
x - 3 = 0  →  x = 3

**Resposta:** S = {2, 3}

### Dicas para a Prova

1. **Produtos notáveis:** Memorize as 5 fórmulas principais
2. **Quadrado da soma/diferença:** O último termo é sempre positivo!
3. **Diferença de quadrados:** Resultado não tem termo do meio
4. **Fatoração:** Sempre comece procurando fator comum
5. **Trinômio x² + Sx + P:** Procure dois números que somam S e multiplicam P
6. **Verificação:** Multiplique de volta para conferir a fatoração
7. **Sinais:** Preste muita atenção aos sinais, principalmente ao subtrair polinômios

### Conceitos-Chave para Memorizar

**Produtos Notáveis:**
- (a + b)² = a² + 2ab + b²
- (a - b)² = a² - 2ab + b²
- (a + b)(a - b) = a² - b²

**Fatoração:**
- **Fator comum:** ax + ay = a(x + y)
- **Diferença de quadrados:** a² - b² = (a + b)(a - b)
- **Trinômio quadrado perfeito:** a² ± 2ab + b² = (a ± b)²
- **Trinômio x² + Sx + P:** procure números que somam S e multiplicam P

**Erros comuns a evitar:**
- (a + b)² ≠ a² + b² → correto: a² + 2ab + b²
- (a - b)² ≠ a² - b² → correto: a² - 2ab + b²

### Fórmulas Essenciais

```
Produtos Notáveis:

(a + b)² = a² + 2ab + b²
(a - b)² = a² - 2ab + b²
(a + b)(a - b) = a² - b²
(a + b)³ = a³ + 3a²b + 3ab² + b³
(a - b)³ = a³ - 3a²b + 3ab² - b³

Fatoração:

Fator comum: ax + ay = a(x + y)
Diferença de quadrados: a² - b² = (a + b)(a - b)
Trinômio quadrado perfeito: a² ± 2ab + b² = (a ± b)²
Diferença de cubos: a³ - b³ = (a - b)(a² + ab + b²)
Soma de cubos: a³ + b³ = (a + b)(a² - ab + b²)
```

### Tabela de Fatoração Rápida

```
┌─────────────────────────┬────────────────────────┐
│      Expressão          │      Fatoração         │
├─────────────────────────┼────────────────────────┤
│ x² - 4                  │ (x + 2)(x - 2)         │
│ x² - 9                  │ (x + 3)(x - 3)         │
│ x² - 16                 │ (x + 4)(x - 4)         │
│ x² - 25                 │ (x + 5)(x - 5)         │
│ x² + 2x + 1             │ (x + 1)²               │
│ x² - 2x + 1             │ (x - 1)²               │
│ x² + 4x + 4             │ (x + 2)²               │
│ x² - 4x + 4             │ (x - 2)²               │
│ x² + 6x + 9             │ (x + 3)²               │
│ x² - 6x + 9             │ (x - 3)²               │
└─────────────────────────┴────────────────────────┘
```

### Estratégia de Resolução

**Ao fatorar, siga esta ordem:**

1. **Fator comum em evidência** (sempre tente primeiro!)
2. **Diferença de quadrados** (a² - b²)
3. **Trinômio quadrado perfeito** (a² ± 2ab + b²)
4. **Trinômio x² + Sx + P** (procure dois números)
5. **Agrupamento** (se tiver 4 termos)
6. **Diferença/soma de cubos** (menos comum)

**Sempre verifique multiplicando de volta!**

---

**Tempo de estudo recomendado:** 120 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base para equações e funções)

## Aula 12 - Física: Cinemática - MRUV e Queda Livre - 90min

### Recordando: MRU vs MRUV

**MRU (Movimento Retilíneo Uniforme):**
- Velocidade **constante**
- Aceleração = 0
- Equação: s = s₀ + vt

**MRUV (Movimento Retilíneo Uniformemente Variado):**
- Velocidade **variável**
- Aceleração **constante** (≠ 0)
- Movimento em linha reta com aceleração uniforme

### O que é Aceleração?

**Aceleração** é a taxa de variação da velocidade em relação ao tempo.

**Definição:**
```
a = Δv / Δt = (v - v₀) / t
```

Onde:
- a = aceleração
- v = velocidade final
- v₀ = velocidade inicial
- Δv = variação da velocidade
- t = intervalo de tempo

**Unidade no SI:** m/s² (metros por segundo ao quadrado)

**Interpretação:**
- a = 2 m/s² significa que a velocidade aumenta 2 m/s a cada segundo
- a = -3 m/s² significa que a velocidade diminui 3 m/s a cada segundo (desaceleração)

**Exemplo:**
Um carro parte do repouso e atinge 20 m/s em 5 segundos. Qual sua aceleração?

a = (v - v₀) / t = (20 - 0) / 5 = 4 m/s²

### Tipos de Movimento Acelerado

#### Aceleração Positiva (a > 0)
- Movimento **acelerado**
- Velocidade aumenta
- v e a têm o mesmo sinal

**Exemplo:** Carro acelerando para frente

#### Aceleração Negativa (a < 0)
- Movimento **retardado** ou **desacelerado**
- Velocidade diminui em módulo
- v e a têm sinais opostos

**Exemplo:** Carro freando

**Observação importante:**
- Aceleração negativa ≠ sempre desaceleração
- O que importa é a relação entre os sinais de v e a:
  - **Mesmos sinais:** acelerado
  - **Sinais opostos:** retardado

### Equações do MRUV

No MRUV, temos 4 equações principais (chamadas de "equações horárias"):

### 1. Função Horária da Velocidade

**v = v₀ + at**

Onde:
- v = velocidade no instante t
- v₀ = velocidade inicial
- a = aceleração
- t = tempo

**Uso:** Encontrar a velocidade em qualquer instante.

**Exemplo:**
Um móvel parte com v₀ = 10 m/s e acelera a 2 m/s². Qual a velocidade em t = 5s?

v = 10 + 2(5) = 10 + 10 = 20 m/s

### 2. Função Horária da Posição (Equação de Torricelli com tempo)

**s = s₀ + v₀t + (1/2)at²**

Onde:
- s = posição no instante t
- s₀ = posição inicial
- v₀ = velocidade inicial
- a = aceleração
- t = tempo

**Uso:** Encontrar a posição em qualquer instante.

**Exemplo:**
Um móvel parte de s₀ = 0 com v₀ = 5 m/s e a = 2 m/s². Qual a posição em t = 4s?

s = 0 + 5(4) + (1/2)(2)(4²)
s = 0 + 20 + (1)(16)
s = 36 m

### 3. Equação de Torricelli (sem tempo)

**v² = v₀² + 2aΔs**

Onde:
- v = velocidade final
- v₀ = velocidade inicial
- a = aceleração
- Δs = deslocamento (s - s₀)

**Uso:** Relacionar velocidade e deslocamento **sem usar o tempo**.

**Exemplo:**
Um carro a 10 m/s acelera a 2 m/s² por 50 m. Qual a velocidade final?

v² = 10² + 2(2)(50)
v² = 100 + 200
v² = 300
v = √300 ≈ 17,3 m/s

### 4. Velocidade Média

**v_m = (v₀ + v) / 2**

**Válida apenas para MRUV** (movimento uniformemente variado)

**Exemplo:**
Um móvel parte com 10 m/s e chega a 30 m/s. Qual a velocidade média?

v_m = (10 + 30) / 2 = 20 m/s

### Resumo das Equações do MRUV

```
1. v = v₀ + at

2. s = s₀ + v₀t + (1/2)at²

3. v² = v₀² + 2aΔs

4. v_m = (v₀ + v) / 2
```

### Como Escolher a Equação Certa?

**Analise o que você tem e o que quer descobrir:**

| Tem | Quer | Use |
|-----|------|-----|
| v₀, a, t | v | v = v₀ + at |
| v₀, a, t | s | s = s₀ + v₀t + (1/2)at² |
| v₀, a, Δs | v | v² = v₀² + 2aΔs |
| v₀, v | v_m | v_m = (v₀ + v) / 2 |
| v₀, v, a | t | v = v₀ + at |
| v₀, v, a | Δs | v² = v₀² + 2aΔs |

**Dica:** Se o problema **não menciona tempo**, use Torricelli (v² = v₀² + 2aΔs)!

### Gráficos do MRUV

#### Gráfico v × t (Velocidade × Tempo)

**Características:**
- Reta inclinada
- Inclinação = aceleração
- Área sob a curva = deslocamento

```
v ↑
  |     /
  |    /  (a > 0, movimento acelerado)
  |   /
  |  /
  | /
  |/___________→ t
```

```
v ↑
  |\
  | \   (a < 0, movimento retardado)
  |  \
  |   \
  |    \
  |_____\______→ t
```

**Inclinação = aceleração:**
- Reta crescente → a > 0
- Reta decrescente → a < 0
- Quanto mais inclinada, maior o módulo de a

**Área sob a curva = deslocamento:**
Δs = área do trapézio (ou triângulo + retângulo)

#### Gráfico s × t (Posição × Tempo)

**Características:**
- Parábola (função do 2° grau)
- Concavidade determina o sinal de a

```
s ↑
  |      /
  |     /
  |    /     (a > 0, concavidade para cima)
  |   /
  |  /
  |_/___________→ t
```

```
s ↑
  |\
  | \____
  |      \___   (a < 0, concavidade para baixo)
  |          \
  |           \
  |____________→ t
```

**Concavidade:**
- Para cima (∪) → a > 0
- Para baixo (∩) → a < 0

#### Gráfico a × t (Aceleração × Tempo)

**Características:**
- Reta horizontal (aceleração constante)
- Área sob a curva = variação da velocidade

```
a ↑
  |____________
  |            (a constante e positiva)
  |
  |____________→ t
```

### Queda Livre

**Definição:** Movimento vertical de um corpo abandonado no vácuo (ou desprezando resistência do ar), sob ação exclusiva da gravidade.

**Características:**
- Movimento uniformemente variado (MRUV)
- Aceleração = g (aceleração da gravidade)
- g ≈ 10 m/s² (aproximação)
- g = 9,8 m/s² (valor mais preciso)

**Orientação:**
- **Para baixo (↓):** consideramos positivo → g = +10 m/s²
- **Para cima (↑):** consideramos negativo → g = -10 m/s²

### Equações da Queda Livre

Mesmas equações do MRUV, substituindo **a por g**:

```
1. v = v₀ + gt

2. h = h₀ + v₀t + (1/2)gt²

3. v² = v₀² + 2gΔh

4. v_m = (v₀ + v) / 2
```

**Convenção usual:**
- Eixo y positivo para **cima**
- g = -10 m/s² (gravidade aponta para baixo)
- Altura h ao invés de posição s

### Casos Especiais de Queda Livre

#### 1. Objeto Abandonado (v₀ = 0)

**Exemplo:** Soltar uma pedra do alto de um prédio

- v₀ = 0
- g = 10 m/s² (para baixo)

**Equações simplificadas:**
- v = gt
- h = (1/2)gt²
- v² = 2gh

**Exemplo:**
Uma pedra é solta de uma altura de 20 m. Com que velocidade atinge o solo? (g = 10 m/s²)

v² = v₀² + 2gΔh
v² = 0 + 2(10)(20)
v² = 400
v = 20 m/s

**Tempo de queda:**
h = (1/2)gt²
20 = (1/2)(10)t²
20 = 5t²
t² = 4
t = 2 s

#### 2. Lançamento Vertical para Baixo (v₀ > 0)

**Exemplo:** Arremessar uma bola para baixo

- v₀ > 0 (velocidade inicial para baixo)
- g = 10 m/s² (mesma direção)
- Movimento acelerado

#### 3. Lançamento Vertical para Cima (v₀ > 0)

**Exemplo:** Arremessar uma bola para cima

**Convenção:**
- Eixo positivo: para cima
- v₀ > 0 (para cima)
- g = -10 m/s² (para baixo)

**Fases do movimento:**

**Subida:**
- v diminui (movimento retardado)
- v e g têm sinais opostos
- No ponto mais alto: v = 0

**Descida:**
- v aumenta em módulo (movimento acelerado)
- v e g têm mesmo sinal
- Velocidade ao retornar = velocidade inicial (em módulo)

**Altura máxima:**
No ponto mais alto, v = 0

v² = v₀² + 2g(-h_max)
0 = v₀² - 2gh_max
h_max = v₀² / (2g)

**Tempo de subida:**
v = v₀ + gt
0 = v₀ - gt_subida
t_subida = v₀ / g

**Tempo total (subida + descida):**
t_total = 2 × t_subida = 2v₀ / g

**Simetria:**
- Tempo de subida = tempo de descida
- Velocidade ao retornar = velocidade inicial (em módulo, mas sentido oposto)

### Exercícios Resolvidos

#### Exercício 1
Um carro parte do repouso com aceleração constante de 2 m/s². Calcule:
a) A velocidade após 10 s
b) A distância percorrida em 10 s

**Solução:**
Dados: v₀ = 0, a = 2 m/s², t = 10 s

a) v = v₀ + at
   v = 0 + 2(10)
   v = 20 m/s

b) s = s₀ + v₀t + (1/2)at²
   s = 0 + 0 + (1/2)(2)(10²)
   s = 0 + 0 + 100
   s = 100 m

#### Exercício 2
Um móvel tem velocidade inicial de 20 m/s e desacelera a -4 m/s². Quanto tempo leva para parar?

**Solução:**
Dados: v₀ = 20 m/s, a = -4 m/s², v = 0 (parar)

v = v₀ + at
0 = 20 + (-4)t
4t = 20
t = 5 s

#### Exercício 3
Um carro a 15 m/s freia com desaceleração de 3 m/s². Qual a distância percorrida até parar?

**Solução:**
Dados: v₀ = 15 m/s, v = 0, a = -3 m/s²

**Não temos t, use Torricelli!**

v² = v₀² + 2aΔs
0 = 15² + 2(-3)Δs
0 = 225 - 6Δs
6Δs = 225
Δs = 37,5 m

#### Exercício 4
Uma pedra é solta do alto de um edifício de 45 m. Calcule:
a) O tempo de queda
b) A velocidade ao atingir o solo
(Use g = 10 m/s²)

**Solução:**
Dados: h = 45 m, v₀ = 0, g = 10 m/s²

a) h = (1/2)gt²
   45 = (1/2)(10)t²
   45 = 5t²
   t² = 9
   t = 3 s

b) v = gt (pois v₀ = 0)
   v = 10(3)
   v = 30 m/s

**Ou usando Torricelli:**
v² = 0 + 2(10)(45)
v² = 900
v = 30 m/s

#### Exercício 5
Uma bola é lançada verticalmente para cima com v₀ = 30 m/s. Calcule:
a) Altura máxima
b) Tempo para atingir altura máxima
c) Tempo total no ar
(Use g = 10 m/s²)

**Solução:**
Dados: v₀ = 30 m/s, g = -10 m/s² (para cima)

a) Na altura máxima, v = 0
   v² = v₀² + 2g(-h_max)
   0 = 30² + 2(-10)h_max
   0 = 900 - 20h_max
   20h_max = 900
   h_max = 45 m

b) v = v₀ + gt
   0 = 30 + (-10)t
   10t = 30
   t = 3 s

c) t_total = 2 × t_subida = 2 × 3 = 6 s

#### Exercício 6
Dois móveis partem do mesmo ponto. O primeiro tem velocidade constante de 20 m/s. O segundo parte do repouso com aceleração de 4 m/s². Quando o segundo alcança o primeiro?

**Solução:**
**Móvel 1 (MRU):** s₁ = 20t
**Móvel 2 (MRUV):** s₂ = 0 + 0 + (1/2)(4)t² = 2t²

**Quando se encontram:** s₁ = s₂
20t = 2t²
2t² - 20t = 0
2t(t - 10) = 0

t = 0 (início) ou t = 10 s

**Resposta:** Após 10 segundos

**Posição do encontro:**
s = 20(10) = 200 m

#### Exercício 7
Um trem viaja a 72 km/h quando o maquinista vê um obstáculo. Ele freia com desaceleração de 2 m/s². A que distância mínima do obstáculo ele deve iniciar a frenagem para não colidir?

**Solução:**
Primeiro, converter: 72 km/h = 72/3,6 = 20 m/s

Dados: v₀ = 20 m/s, v = 0, a = -2 m/s²

v² = v₀² + 2aΔs
0 = 20² + 2(-2)Δs
0 = 400 - 4Δs
4Δs = 400
Δs = 100 m

**Resposta:** Deve começar a frear pelo menos 100 m antes do obstáculo.

### Dicas para a Prova

1. **Identifique o tipo de movimento:** MRU (v constante) ou MRUV (a constante)?
2. **Liste os dados:** v₀, v, a, t, Δs - o que você tem? O que quer?
3. **Sem tempo no problema?** Use Torricelli: v² = v₀² + 2aΔs
4. **Queda livre:** Use g = 10 m/s² (ou 9,8 se especificado)
5. **Atenção aos sinais:**
   - Defina um referencial (positivo para cima ou para baixo)
   - Mantenha consistência
6. **Conversão:** km/h → m/s: divida por 3,6
7. **Gráficos:**
   - v×t: inclinação = a, área = Δs
   - s×t: concavidade indica sinal de a
8. **Lançamento vertical:** No ponto mais alto, v = 0

### Conceitos-Chave para Memorizar

**MRUV:**
- Aceleração constante (≠ 0)
- Velocidade varia uniformemente
- 4 equações principais

**Queda Livre:**
- MRUV com a = g
- g ≈ 10 m/s²
- Abandonado: v₀ = 0
- Lançado para cima: no topo v = 0

**Sinais:**
- Movimento acelerado: v e a mesmo sinal
- Movimento retardado: v e a sinais opostos

**Gráficos:**
- v×t: reta (inclinação = a)
- s×t: parábola (concavidade mostra sinal de a)
- a×t: reta horizontal

### Fórmulas Essenciais

```
Equações do MRUV:

v = v₀ + at

s = s₀ + v₀t + (1/2)at²

v² = v₀² + 2aΔs  (Torricelli - sem tempo)

v_m = (v₀ + v) / 2  (válida só para MRUV)

Queda Livre (substitua a por g):

v = v₀ + gt

h = h₀ + v₀t + (1/2)gt²

v² = v₀² + 2gΔh

Altura máxima (lançamento vertical):
h_max = v₀² / (2g)

Tempo de subida:
t_subida = v₀ / g

Tempo total:
t_total = 2v₀ / g

Conversão:
km/h → m/s: dividir por 3,6
m/s → km/h: multiplicar por 3,6
```

### Tabela Resumo

```
┌──────────────────┬─────────────────────────────┐
│   Grandeza       │        MRUV                 │
├──────────────────┼─────────────────────────────┤
│ Velocidade       │ Variável (uniformemente)    │
│ Aceleração       │ Constante (≠ 0)             │
│ Gráfico v×t      │ Reta inclinada              │
│ Gráfico s×t      │ Parábola                    │
│ Gráfico a×t      │ Reta horizontal             │
└──────────────────┴─────────────────────────────┘

┌──────────────────────┬────────────────────────┐
│   Situação           │     Equação Ideal      │
├──────────────────────┼────────────────────────┤
│ Tem t, quer v        │ v = v₀ + at            │
│ Tem t, quer s        │ s = s₀ + v₀t + ½at²   │
│ NÃO tem t            │ v² = v₀² + 2aΔs        │
│ Quer v_média         │ v_m = (v₀ + v) / 2     │
└──────────────────────┴────────────────────────┘
```

### Erros Comuns a Evitar

1. **Confundir MRU com MRUV**
   - MRU: s = s₀ + vt (sem termo at²)
   - MRUV: s = s₀ + v₀t + (1/2)at²

2. **Esquecer o (1/2) na equação do espaço**
   - Correto: s = s₀ + v₀t + **(1/2)**at²
   - Errado: s = s₀ + v₀t + at²

3. **Usar v_m = (v₀+v)/2 no MRU**
   - Só vale para MRUV!
   - No MRU, v_m = v (constante)

4. **Sinais inconsistentes**
   - Defina um referencial e mantenha!
   - Para cima: g = -10 m/s²
   - Para baixo: g = +10 m/s²

5. **Não converter km/h para m/s**
   - Sempre converta para SI!
   - 72 km/h = 20 m/s

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - cai muito em vestibulares)

## Aula 13 - Química: Estrutura Atômica e Radioatividade - 90min

### Estrutura do Átomo

**Átomo** é a menor partícula que caracteriza um elemento químico. É formado por três partículas fundamentais:

#### Partículas Subatômicas

| Partícula | Símbolo | Carga | Massa (u) | Localização |
|-----------|---------|-------|-----------|-------------|
| **Próton** | p⁺ | +1 | 1 | Núcleo |
| **Nêutron** | n⁰ | 0 | 1 | Núcleo |
| **Elétron** | e⁻ | -1 | ~0 (1/1836) | Eletrosfera |

**Observações:**
- Prótons e nêutrons têm massa semelhante
- Elétrons têm massa desprezível comparada aos prótons/nêutrons
- Átomo neutro: número de prótons = número de elétrons

### Representação do Átomo

**Número Atômico (Z):**
- Número de prótons no núcleo
- Identifica o elemento químico
- Em átomo neutro: Z = número de prótons = número de elétrons

**Número de Massa (A):**
- Soma de prótons e nêutrons no núcleo
- A = Z + N (onde N = número de nêutrons)

**Notação:**
```
  A
 X
  Z

Onde:
X = símbolo do elemento
A = número de massa
Z = número atômico
```

**Exemplo:**
```
  23
 Na    →  Sódio
  11

Z = 11 (11 prótons e 11 elétrons)
A = 23
N = A - Z = 23 - 11 = 12 nêutrons
```

### Íons

**Íon** é um átomo ou grupo de átomos que perdeu ou ganhou elétrons, adquirindo carga elétrica.

#### Cátion (íon positivo)
- Átomo que **perdeu** elétrons
- Carga positiva
- Geralmente metais

**Exemplo:**
Na → Na⁺ + e⁻

- Na: 11 prótons, 11 elétrons (neutro)
- Na⁺: 11 prótons, 10 elétrons (cátion)

#### Ânion (íon negativo)
- Átomo que **ganhou** elétrons
- Carga negativa
- Geralmente ametais

**Exemplo:**
Cl + e⁻ → Cl⁻

- Cl: 17 prótons, 17 elétrons (neutro)
- Cl⁻: 17 prótons, 18 elétrons (ânion)

### Isótopos, Isóbaros e Isótonos

#### Isótopos
**Mesmo elemento (mesmo Z), diferentes massas (diferente A)**
- Mesmo número de prótons
- Diferente número de nêutrons

**Exemplo:** Isótopos do Carbono
- ¹²C₆: 6 prótons, 6 nêutrons
- ¹³C₆: 6 prótons, 7 nêutrons
- ¹⁴C₆: 6 prótons, 8 nêutrons

**Aplicação:** Carbono-14 (¹⁴C) é usado para datação de fósseis

#### Isóbaros
**Elementos diferentes (diferente Z), mesma massa (mesmo A)**
- Diferente número de prótons
- Mesma massa total

**Exemplo:**
- ⁴⁰K₁₉: 19 prótons, 21 nêutrons
- ⁴⁰Ca₂₀: 20 prótons, 20 nêutrons

#### Isótonos
**Elementos diferentes (diferente Z), mesmo número de nêutrons**

**Exemplo:**
- ¹⁴C₆: 6 prótons, 8 nêutrons
- ¹⁵N₇: 7 prótons, 8 nêutrons

### Resumo - ISO

```
┌─────────────┬────────┬────────┬──────────┐
│             │   Z    │   A    │    N     │
├─────────────┼────────┼────────┼──────────┤
│ Isótopos    │ Igual  │ Diferente│ Diferente│
│ Isóbaros    │Diferente│ Igual  │ Diferente│
│ Isótonos    │Diferente│Diferente│  Igual   │
└─────────────┴────────┴────────┴──────────┘
```

### Massa Atômica e Massa Molecular

#### Massa Atômica (MA)
- Massa de um átomo medida em unidades de massa atômica (u)
- 1 u = 1/12 da massa do átomo de ¹²C

**Para isótopos:** Média ponderada das massas dos isótopos naturais

**Exemplo:** Cloro natural
- ³⁵Cl (75%) → massa = 35 u
- ³⁷Cl (25%) → massa = 37 u

MA(Cl) = (35 × 75 + 37 × 25) / 100
MA(Cl) = (2625 + 925) / 100
MA(Cl) = 35,5 u

#### Massa Molecular (MM)
Soma das massas atômicas dos átomos que formam a molécula.

**Exemplo:** H₂O
- H: 1 u (2 átomos)
- O: 16 u (1 átomo)

MM(H₂O) = 2(1) + 1(16) = 18 u

### Distribuição Eletrônica

Os elétrons estão distribuídos em **camadas** ou **níveis de energia** ao redor do núcleo.

#### Camadas Eletrônicas

| Camada | Nome | Nº máximo de elétrons |
|--------|------|-----------------------|
| 1 | K | 2 |
| 2 | L | 8 |
| 3 | M | 18 |
| 4 | N | 32 |
| 5 | O | 32 |
| 6 | P | 18 |
| 7 | Q | 8 |

**Fórmula geral:** Máximo = 2n² (onde n = número da camada)

#### Distribuição por Camadas (Diagrama de Pauling)

**Ordem de preenchimento (Diagrama de Linus Pauling):**

```
1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹⁰ 5p⁶ 6s² 4f¹⁴ 5d¹⁰ 6p⁶ 7s²...
```

**Regra prática:**
1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → 5s → 4d → 5p → 6s → 4f → 5d → 6p → 7s...

**Capacidade dos subníveis:**
- s: até 2 elétrons
- p: até 6 elétrons
- d: até 10 elétrons
- f: até 14 elétrons

#### Exemplos de Distribuição

**Exemplo 1: Sódio (Na, Z = 11)**

11 elétrons para distribuir:
- 1s²: 2 elétrons (restam 9)
- 2s²: 2 elétrons (restam 7)
- 2p⁶: 6 elétrons (restam 1)
- 3s¹: 1 elétron

**Configuração:** 1s² 2s² 2p⁶ 3s¹

**Por camadas:** K=2, L=8, M=1

**Exemplo 2: Cloro (Cl, Z = 17)**

17 elétrons:
- 1s² 2s² 2p⁶ 3s² 3p⁵

**Por camadas:** K=2, L=8, M=7

**Exemplo 3: Cálcio (Ca, Z = 20)**

20 elétrons:
- 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²

**Por camadas:** K=2, L=8, M=8, N=2

### Camada de Valência

**Camada de valência** é a camada mais externa (última camada com elétrons).

- Determina as propriedades químicas
- Responsável pelas ligações químicas
- Elétrons da última camada = elétrons de valência

**Exemplos:**
- Na (K=2, L=8, M=1): 1 elétron de valência
- Cl (K=2, L=8, M=7): 7 elétrons de valência
- He (K=2): 2 elétrons de valência (camada completa)

### Radioatividade

**Radioatividade** é a emissão espontânea de partículas e/ou energia por núcleos atômicos instáveis.

#### Descoberta
- **Henri Becquerel (1896):** Descobriu a radioatividade do urânio
- **Marie e Pierre Curie:** Isolaram rádio e polônio

### Tipos de Emissões Radioativas

#### 1. Partículas Alfa (α)

**Constituição:** Núcleo de hélio (²He₄)
- 2 prótons + 2 nêutrons
- Carga: +2
- Massa: 4 u

**Poder de penetração:** Baixo (barrada por folha de papel)

**Equação:**
```
  A         A-4           4
 X    →    Y      +      He
  Z         Z-2           2
```

**Exemplo:**
²³⁸U₉₂ → ²³⁴Th₉₀ + ⁴He₂

- Perde 2 prótons (Z diminui 2)
- Perde 2 nêutrons (A diminui 4)

#### 2. Partículas Beta (β)

**Constituição:** Elétron de alta energia (⁰e₋₁) ou pósitron (⁰e₊₁)

**Beta negativo (β⁻):**
- Nêutron se transforma em próton + elétron
- n⁰ → p⁺ + e⁻
- Carga: -1
- Massa: ~0

**Poder de penetração:** Médio (barrada por placa de alumínio)

**Equação:**
```
  A         A          0
 X    →    Y    +     e
  Z         Z+1       -1
```

**Exemplo:**
¹⁴C₆ → ¹⁴N₇ + ⁰e₋₁

- Ganha 1 próton (Z aumenta 1)
- Perde 1 nêutron
- A permanece igual

**Beta positivo (β⁺):**
- Próton se transforma em nêutron + pósitron
- Menos comum

#### 3. Raios Gama (γ)

**Constituição:** Radiação eletromagnética de alta energia

- Sem massa
- Sem carga
- Acompanha emissões α ou β

**Poder de penetração:** Alto (atravessa a maioria dos materiais; barrada por chumbo grosso)

**Equação:**
```
  A         A
 X*   →    X    +   γ
  Z         Z
```

(* indica núcleo excitado)

- Z e A não mudam
- Apenas libera energia

### Resumo das Emissões

```
┌──────────┬─────────┬──────┬───────────────┬──────────────┐
│ Emissão  │ Símbolo │Carga │    Massa      │  Penetração  │
├──────────┼─────────┼──────┼───────────────┼──────────────┤
│ Alfa     │ ⁴He₂ (α)│  +2  │      4 u      │    Baixa     │
│ Beta (-)│ ⁰e₋₁ (β⁻)│  -1  │     ~0        │    Média     │
│ Gama     │    γ    │   0  │      0        │    Alta      │
└──────────┴─────────┴──────┴───────────────┴──────────────┘
```

### Leis da Radioatividade

#### Lei de Soddy (1ª Lei)
**Emissão alfa:** Z diminui 2, A diminui 4

#### Lei de Soddy-Fajans-Russell (2ª Lei)
**Emissão beta:** Z aumenta 1, A permanece igual

### Meia-Vida (t₁/₂)

**Definição:** Tempo necessário para que metade dos átomos de uma amostra radioativa se desintegre.

**Fórmula:**
```
N = N₀ × (1/2)ⁿ

ou

N = N₀ × (1/2)^(t/t₁/₂)
```

Onde:
- N = quantidade final
- N₀ = quantidade inicial
- n = número de meias-vidas
- t = tempo decorrido
- t₁/₂ = meia-vida

**Exemplo:**

Uma amostra de 80 g de um isótopo radioativo com meia-vida de 10 anos. Quanto resta após 30 anos?

t/t₁/₂ = 30/10 = 3 meias-vidas

N = 80 × (1/2)³
N = 80 × 1/8
N = 10 g

**Evolução:**
- 0 anos: 80 g
- 10 anos (1 meia-vida): 40 g
- 20 anos (2 meias-vidas): 20 g
- 30 anos (3 meias-vidas): 10 g

### Aplicações da Radioatividade

#### Medicina
- **Radioterapia:** Tratamento de câncer
- **Radiografia:** Diagnóstico por imagem
- **Medicina nuclear:** Traçadores radioativos (iodo-131 para tireoide)

#### Indústria
- **Esterilização:** Alimentos e equipamentos médicos
- **Medição de espessura:** Controle de qualidade

#### Datação
- **Carbono-14:** Datação de fósseis (até 50.000 anos)
- **Urânio-238:** Datação de rochas (milhões/bilhões de anos)

#### Energia
- **Usinas nucleares:** Geração de energia elétrica

### Fissão e Fusão Nuclear

#### Fissão Nuclear
**Divisão de um núcleo pesado em núcleos menores, com liberação de energia**

- Usado em usinas nucleares e bombas atômicas
- Exemplo: ²³⁵U + nêutron → fragmentos + nêutrons + energia

**Reação em cadeia:** Nêutrons liberados causam novas fissões

#### Fusão Nuclear
**União de núcleos leves formando núcleo mais pesado, com liberação de energia**

- Ocorre no Sol e estrelas
- Fonte de energia das estrelas
- Exemplo: ²H + ³H → ⁴He + nêutron + energia

**Energia liberada é maior que na fissão!**

### Exercícios Resolvidos

#### Exercício 1
Um átomo possui 17 prótons, 18 nêutrons e 17 elétrons. Determine:
a) Número atômico (Z)
b) Número de massa (A)
c) Representação

**Solução:**
a) Z = número de prótons = 17
b) A = Z + N = 17 + 18 = 35
c) ³⁵Cl₁₇ (Cloro-35)

#### Exercício 2
O íon Ca²⁺ possui 20 prótons. Quantos elétrons possui?

**Solução:**
Cátion +2 = perdeu 2 elétrons

Átomo neutro: 20 prótons, 20 elétrons
Ca²⁺: 20 prótons, 18 elétrons

**Resposta:** 18 elétrons

#### Exercício 3
Faça a distribuição eletrônica do Oxigênio (O, Z = 8).

**Solução:**
8 elétrons: 1s² 2s² 2p⁴

**Por camadas:** K=2, L=6

**Elétrons de valência:** 6 (camada L)

#### Exercício 4
Identifique o tipo de relação entre:
a) ¹²C₆ e ¹⁴C₆
b) ⁴⁰K₁₉ e ⁴⁰Ca₂₀
c) ¹⁴C₆ e ¹⁵N₇

**Solução:**
a) Mesmo Z (6), diferente A → **Isótopos**
b) Diferente Z, mesmo A (40) → **Isóbaros**
c) Z=6 (8n), Z=7 (8n) → mesmo N=8 → **Isótonos**

#### Exercício 5
Complete a equação: ²³⁸U₉₂ → ? + ⁴He₂

**Solução:**
Emissão alfa (perde 2p e 2n):

Z: 92 - 2 = 90
A: 238 - 4 = 234

**Resposta:** ²³⁴Th₉₀ (Tório-234)

Equação completa: ²³⁸U₉₂ → ²³⁴Th₉₀ + ⁴He₂

#### Exercício 6
Complete: ¹⁴C₆ → ? + ⁰e₋₁

**Solução:**
Emissão beta (ganha 1p):

Z: 6 + 1 = 7
A: 14 (permanece)

**Resposta:** ¹⁴N₇ (Nitrogênio-14)

Equação: ¹⁴C₆ → ¹⁴N₇ + ⁰e₋₁

#### Exercício 7
Uma amostra de 100 g de um elemento radioativo tem meia-vida de 5 anos. Qual a massa após 15 anos?

**Solução:**
n = t/t₁/₂ = 15/5 = 3 meias-vidas

N = 100 × (1/2)³
N = 100 × 1/8
N = 12,5 g

**Resposta:** 12,5 g

#### Exercício 8
Calcule a massa atômica do cloro, sabendo que na natureza há 75% de ³⁵Cl e 25% de ³⁷Cl.

**Solução:**
MA = (35 × 75 + 37 × 25) / 100
MA = (2625 + 925) / 100
MA = 3550 / 100
MA = 35,5 u

**Resposta:** 35,5 u

### Dicas para a Prova

1. **Número atômico (Z)** define o elemento - não muda em íons
2. **Íons:** Cátion perde e⁻, ânion ganha e⁻
3. **Isótopos:** Mesmo elemento, massas diferentes (Ex: C-12, C-14)
4. **Distribuição eletrônica:** Siga a ordem de Pauling
5. **Alfa:** perde 2p e 2n (Z-2, A-4)
6. **Beta:** ganha 1p (Z+1, A igual)
7. **Gama:** só energia (Z e A não mudam)
8. **Meia-vida:** N = N₀ × (1/2)ⁿ
9. **Conversões:** 1 u ≈ 1,66 × 10⁻²⁴ g

### Conceitos-Chave para Memorizar

**Estrutura atômica:**
- Prótons: +1, no núcleo
- Nêutrons: 0, no núcleo
- Elétrons: -1, na eletrosfera
- Z = prótons = elétrons (átomo neutro)
- A = prótons + nêutrons

**Íons:**
- Cátion: perdeu e⁻ (carga +)
- Ânion: ganhou e⁻ (carga -)

**ISO:**
- Isótopos: mesmo Z
- Isóbaros: mesmo A
- Isótonos: mesmo N

**Radioatividade:**
- α: ⁴He₂ (perde 2p, 2n)
- β⁻: ⁰e₋₁ (ganha 1p)
- γ: energia (sem mudança)

### Fórmulas Essenciais

```
Estrutura Atômica:

A = Z + N

N = A - Z

Z = prótons = elétrons (átomo neutro)

Distribuição eletrônica:
Máximo por camada = 2n²

Radioatividade:

Emissão alfa:
  A         A-4           4
 X    →    Y      +      He
  Z         Z-2           2

Emissão beta:
  A         A          0
 X    →    Y    +     e
  Z         Z+1       -1

Meia-vida:
N = N₀ × (1/2)ⁿ

ou

N = N₀ × (1/2)^(t/t₁/₂)

Massa atômica (isótopos):
MA = Σ(massa × abundância) / 100
```

### Tabela Resumo - Partículas

```
┌────────────┬────────┬────────┬──────────────┐
│ Partícula  │ Carga  │  Massa │ Localização  │
├────────────┼────────┼────────┼──────────────┤
│ Próton     │   +1   │   1 u  │   Núcleo     │
│ Nêutron    │    0   │   1 u  │   Núcleo     │
│ Elétron    │   -1   │  ~0    │ Eletrosfera  │
└────────────┴────────┴────────┴──────────────┘

┌────────────┬────────┬────────┬──────────────┐
│  Emissão   │ Carga  │  Massa │  Penetração  │
├────────────┼────────┼────────┼──────────────┤
│ Alfa (α)   │   +2   │   4 u  │    Baixa     │
│ Beta (β⁻)  │   -1   │   ~0   │    Média     │
│ Gama (γ)   │    0   │    0   │    Alta      │
└────────────┴────────┴────────┴──────────────┘
```

### Aplicações Práticas

**Medicina:**
- Iodo-131: Tratamento de tireoide
- Cobalto-60: Radioterapia
- Tecnécio-99m: Diagnóstico por imagem

**Datação:**
- C-14: Fósseis (meia-vida 5.730 anos)
- U-238: Rochas (meia-vida 4,5 bilhões de anos)

**Energia:**
- Fissão de U-235: Usinas nucleares
- Fusão: Energia do Sol

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base para tabela periódica e ligações químicas)

## Aula 14 - Sociologia: Métodos de Pesquisa - 60min

### O que é Pesquisa em Sociologia?

A **pesquisa sociológica** é o processo sistemático de investigação de fenômenos sociais utilizando métodos científicos para compreender a realidade social.

**Objetivo:** Analisar, compreender e explicar comportamentos, relações e estruturas sociais.

### Método Científico nas Ciências Sociais

**Etapas básicas:**
1. **Definição do problema:** O que queremos investigar?
2. **Revisão bibliográfica:** O que já foi estudado sobre o tema?
3. **Formulação de hipóteses:** Quais são nossas suposições iniciais?
4. **Coleta de dados:** Como vamos obter informações?
5. **Análise dos dados:** O que os dados revelam?
6. **Conclusões:** As hipóteses foram confirmadas ou refutadas?

### Tipos de Pesquisa

#### 1. Quanto aos Objetivos

**Pesquisa Exploratória:**
- Primeiro contato com o tema
- Familiarização com o objeto de estudo
- Geralmente qualitativa
- **Exemplo:** Estudo inicial sobre uso de redes sociais por idosos

**Pesquisa Descritiva:**
- Descreve características de um fenômeno
- Identifica relações entre variáveis
- **Exemplo:** Levantamento sobre perfil socioeconômico de estudantes universitários

**Pesquisa Explicativa:**
- Busca explicar causas e consequências
- Identifica fatores determinantes
- **Exemplo:** Análise das causas da evasão escolar em determinada região

#### 2. Quanto à Abordagem

**Pesquisa Qualitativa:**
- Foco na compreensão profunda
- Análise de significados, motivações, valores
- Amostras menores
- Dados não numéricos
- Interpretação subjetiva

**Características:**
- Subjetiva
- Descritiva
- Processo indutivo (do particular para o geral)
- Holística (visão do todo)

**Pesquisa Quantitativa:**
- Foco em dados numéricos e estatísticos
- Mensurável e objetivo
- Amostras grandes
- Análise estatística
- Generalização de resultados

**Características:**
- Objetiva
- Numérica
- Processo dedutivo (do geral para o particular)
- Verificação de hipóteses

### Comparação: Qualitativa vs Quantitativa

```
┌────────────────────┬─────────────────┬─────────────────┐
│   Aspecto          │  Qualitativa    │  Quantitativa   │
├────────────────────┼─────────────────┼─────────────────┤
│ Objetivo           │ Compreender     │ Mensurar        │
│ Dados              │ Textos, imagens │ Números         │
│ Amostra            │ Pequena         │ Grande          │
│ Análise            │ Interpretativa  │ Estatística     │
│ Generalização      │ Limitada        │ Ampla           │
│ Pergunta-chave     │ Por quê? Como?  │ Quanto? Quantos?│
└────────────────────┴─────────────────┴─────────────────┘
```

**Observação:** Muitas pesquisas usam **abordagem mista** (quali-quanti), combinando ambos os métodos.

### Principais Métodos e Técnicas de Pesquisa

### 1. Pesquisa Bibliográfica

**Definição:** Análise de material já publicado (livros, artigos, teses).

**Quando usar:**
- Base para qualquer pesquisa
- Conhecer o estado da arte
- Fundamentação teórica

**Vantagens:**
- Acesso a grande volume de informação
- Baixo custo
- Visão ampla do tema

**Desvantagens:**
- Dependência da qualidade das fontes
- Dados podem estar desatualizados

### 2. Pesquisa Documental

**Definição:** Análise de documentos que não receberam tratamento analítico.

**Fontes:**
- Documentos oficiais (leis, decretos)
- Relatórios institucionais
- Cartas, diários
- Fotografias, vídeos
- Registros estatísticos

**Diferença da bibliográfica:** Documentos sem análise prévia vs publicações acadêmicas analisadas.

### 3. Observação

**Definição:** Técnica de coleta de dados através da observação direta de comportamentos e situações.

#### Observação Participante
- Pesquisador **integra-se** ao grupo estudado
- Vivência direta da realidade
- Antropologia e etnografia

**Exemplo:** Pesquisador convive com comunidade indígena para estudar seus costumes.

**Vantagens:**
- Compreensão profunda
- Acesso a informações não verbalizadas

**Desvantagens:**
- Risco de perder objetividade
- Demorado
- Difícil generalização

#### Observação Não-Participante
- Pesquisador **observa sem participar**
- Mantém distanciamento
- Menos interferência

**Exemplo:** Observar interações em sala de aula sem se envolver.

#### Observação Sistemática
- Estruturada e planejada
- Uso de protocolos de observação
- Mais objetiva

#### Observação Assistemática
- Livre, sem roteiro rígido
- Exploratória
- Mais flexível

### 4. Entrevista

**Definição:** Coleta de dados através de diálogo direto entre pesquisador e entrevistado.

#### Entrevista Estruturada
- Roteiro fixo de perguntas
- Padronizada
- Facilita comparação
- Mais objetiva

**Exemplo:** Questionário com perguntas fechadas aplicado da mesma forma a todos.

#### Entrevista Semiestruturada
- Roteiro flexível
- Permite aprofundamento
- Combina perguntas abertas e fechadas
- **Mais comum em pesquisas qualitativas**

#### Entrevista Não-Estruturada (Livre)
- Sem roteiro rígido
- Conversa informal
- Exploratória
- Muito flexível

**Vantagens das entrevistas:**
- Informações detalhadas
- Esclarecimento de dúvidas imediato
- Adaptação ao entrevistado

**Desvantagens:**
- Demorado
- Custo alto
- Risco de viés do entrevistador

### 5. Questionário

**Definição:** Instrumento com perguntas escritas para autopreenchimento.

**Tipos de perguntas:**

**Fechadas:**
- Alternativas predefinidas
- Fácil tabulação
- Análise quantitativa
- **Exemplo:** Qual sua faixa etária? ( ) 18-25 ( ) 26-35 ( ) 36-45

**Abertas:**
- Resposta livre
- Análise qualitativa
- Informação detalhada
- **Exemplo:** O que você pensa sobre educação pública?

**Vantagens:**
- Alcance grande (especialmente online)
- Baixo custo
- Anonimato (respostas mais sinceras)
- Padronização

**Desvantagens:**
- Taxa de retorno pode ser baixa
- Sem esclarecimento de dúvidas
- Impossível aprofundar

### 6. Estudo de Caso

**Definição:** Investigação profunda de um caso específico (indivíduo, grupo, comunidade, organização).

**Características:**
- Foco em um caso particular
- Análise detalhada e contextualizada
- Múltiplas fontes de dados

**Exemplo:** Estudo sobre uma escola específica que implementou método pedagógico inovador.

**Vantagens:**
- Compreensão profunda
- Riqueza de detalhes
- Flexibilidade

**Desvantagens:**
- Difícil generalização
- Risco de viés
- Demorado

### 7. Pesquisa de Campo (Survey)

**Definição:** Coleta de dados diretamente no local onde ocorre o fenômeno.

**Características:**
- Contato direto com a realidade
- Dados primários
- Geralmente quantitativa

**Exemplo:** Levantamento sobre condições de trabalho em fábricas de determinada região.

### 8. Pesquisa Experimental

**Definição:** Manipulação de variáveis para verificar relações de causa e efeito.

**Menos comum em Sociologia** (mais em Psicologia), mas possível.

**Exemplo:** Estudo sobre como diferentes formatos de mensagem influenciam comportamento de voto.

### 9. História de Vida

**Definição:** Narrativa biográfica a partir do relato do próprio sujeito.

**Características:**
- Qualitativa
- Trajetória individual em contexto social
- Memória e experiência

**Exemplo:** Histórias de vida de migrantes para entender processos migratórios.

### 10. Grupos Focais (Focus Group)

**Definição:** Discussão em grupo sobre tema específico, mediada pelo pesquisador.

**Características:**
- 6-12 participantes
- Interação entre participantes
- Diversidade de opiniões
- Qualitativa

**Exemplo:** Grupo focal com jovens para discutir percepções sobre violência urbana.

**Vantagens:**
- Interação gera insights
- Rápido
- Custo menor que entrevistas individuais

**Desvantagens:**
- Pode haver dominância de alguns participantes
- Dificuldade de generalização

### Amostragem

**Amostra:** Subconjunto da população total que será efetivamente estudado.

**População (universo):** Totalidade de indivíduos/elementos que se quer estudar.

#### Tipos de Amostragem

**Probabilística (Aleatória):**
- Todos têm chance conhecida de serem selecionados
- Permite generalização estatística
- Mais rigorosa

**Tipos:**
- **Aleatória simples:** Sorteio
- **Estratificada:** Divisão em estratos (ex: por idade, renda)
- **Por conglomerados:** Grupos (ex: escolas, bairros)

**Não-probabilística:**
- Seleção intencional ou por conveniência
- Não permite generalização estatística
- Comum em pesquisas qualitativas

**Tipos:**
- **Por conveniência:** Mais acessíveis
- **Intencional (proposital):** Escolha baseada em critérios
- **Bola de neve:** Indicação de participantes por outros participantes

### Ética na Pesquisa

**Princípios fundamentais:**

1. **Consentimento Informado:** Participantes devem concordar voluntariamente
2. **Confidencialidade:** Proteger identidade dos participantes
3. **Anonimato:** Quando possível, não identificar participantes
4. **Não maleficência:** Não causar danos
5. **Beneficência:** Pesquisa deve trazer benefícios
6. **Veracidade:** Honestidade nos dados e resultados

**Comitê de Ética em Pesquisa (CEP):**
- Avalia projetos de pesquisa
- Garante direitos dos participantes

### Exemplos Práticos de Aplicação

#### Exemplo 1: Pesquisa sobre Evasão Escolar

**Objetivo:** Compreender causas da evasão escolar em escola pública

**Abordagem:** Quali-quanti (mista)

**Métodos:**
1. **Quantitativo:** Questionário com alunos evadidos (perfil, motivos)
2. **Qualitativo:** Entrevistas semiestruturadas com professores e gestores
3. **Documental:** Análise de registros escolares (frequência, notas)

#### Exemplo 2: Pesquisa sobre Uso de Redes Sociais

**Objetivo:** Analisar padrões de uso de redes sociais por jovens

**Abordagem:** Quantitativa

**Método:**
- **Survey online:** Questionário com perguntas fechadas sobre tempo de uso, plataformas, finalidades

**Amostragem:** Probabilística estratificada por idade (15-18, 19-24)

### Autores e Conceitos Importantes

#### Max Weber - Compreensão (Verstehen)
- Sociologia deve **compreender** o sentido das ações sociais
- Método qualitativo e interpretativo

#### Émile Durkheim - Fato Social
- Sociologia deve tratar fatos sociais como **coisas**
- Método objetivo e quantitativo
- Estatísticas sociais

#### Pesquisa-Ação (Kurt Lewin)
- Pesquisa com intervenção prática
- Transformação da realidade estudada
- Participação ativa dos sujeitos

### Exercícios Resolvidos

#### Exercício 1
Qual a diferença entre pesquisa bibliográfica e documental?

**Resposta:**
- **Bibliográfica:** Analisa material já publicado e com tratamento analítico (livros, artigos científicos, teses)
- **Documental:** Analisa documentos sem tratamento analítico prévio (cartas, registros, relatórios, fotos)

#### Exercício 2
Classifique as pesquisas:

a) Estudo sobre quantos jovens entre 18-25 anos votam regularmente
b) Investigação sobre os significados da religião para moradores de comunidade
c) Análise da relação entre nível educacional e renda familiar

**Resposta:**
a) **Quantitativa** (dados numéricos, mensurável)
b) **Qualitativa** (significados, compreensão)
c) **Quantitativa** (correlação estatística entre variáveis)

#### Exercício 3
Um pesquisador deseja estudar o cotidiano de trabalhadores em uma fábrica. Ele passa 6 meses trabalhando na fábrica como operário. Que tipo de observação é essa?

**Resposta:** **Observação participante** - o pesquisador integra-se ao grupo estudado.

#### Exercício 4
Identifique a técnica adequada:

a) Coletar opiniões de grande número de pessoas sobre política pública
b) Compreender trajetória de vida de ex-moradores de rua
c) Discutir com grupo percepções sobre novo projeto urbano

**Resposta:**
a) **Questionário** (survey) - alcance amplo, quantitativo
b) **História de vida** ou **entrevista em profundidade** - narrativa biográfica
c) **Grupo focal** - discussão em grupo

#### Exercício 5
Uma pesquisa quer saber se programa social reduziu pobreza em determinado município. Que tipo de pesquisa é?

**Resposta:** **Pesquisa explicativa** - busca explicar causas e efeitos (programa → redução da pobreza).

### Dicas para a Prova

1. **Qualitativa vs Quantitativa:**
   - Qualitativa: compreensão, significados, "por quê?"
   - Quantitativa: mensuração, números, "quanto?"

2. **Observação participante:** Pesquisador integra-se ao grupo

3. **Entrevista vs Questionário:**
   - Entrevista: diálogo direto
   - Questionário: autopreenchimento

4. **Amostragem:**
   - Probabilística: generalização possível
   - Não-probabilística: qualitativa, intencional

5. **Ética:** Consentimento, confidencialidade, não causar danos

6. **Métodos mistos:** Combinam quali e quanti

### Conceitos-Chave para Memorizar

**Abordagens:**
- **Qualitativa:** compreensão, interpretação, subjetiva
- **Quantitativa:** mensuração, estatística, objetiva

**Métodos principais:**
- Observação (participante/não-participante)
- Entrevista (estruturada/semiestruturada/livre)
- Questionário (survey)
- Estudo de caso
- Grupos focais
- História de vida

**Tipos de pesquisa:**
- Exploratória: familiarização
- Descritiva: descrever
- Explicativa: explicar causas

**Amostragem:**
- Probabilística: aleatória, representativa
- Não-probabilística: intencional, conveniência

### Quadro-Resumo

```
┌─────────────────────┬──────────────────────────────┐
│     Método          │      Características         │
├─────────────────────┼──────────────────────────────┤
│ Bibliográfica       │ Material publicado           │
│ Documental          │ Documentos sem análise       │
│ Observação          │ Observar comportamentos      │
│ Entrevista          │ Diálogo direto               │
│ Questionário        │ Autopreenchimento            │
│ Estudo de caso      │ Caso específico profundo     │
│ Grupo focal         │ Discussão em grupo           │
│ História de vida    │ Narrativa biográfica         │
└─────────────────────┴──────────────────────────────┘

┌─────────────────────┬─────────────┬──────────────┐
│   Característica    │ Qualitativa │ Quantitativa │
├─────────────────────┼─────────────┼──────────────┤
│ Dados               │ Textos      │ Números      │
│ Objetivo            │ Compreender │ Mensurar     │
│ Amostra             │ Pequena     │ Grande       │
│ Generalização       │ Limitada    │ Ampla        │
│ Processo            │ Indutivo    │ Dedutivo     │
└─────────────────────┴─────────────┴──────────────┘
```

### Aplicação Prática

**Situação:** Você quer pesquisar sobre bullying na escola

**Abordagem mista:**

1. **Quantitativa:**
   - Survey com alunos: frequência, tipos, locais
   - Questionário fechado
   - Análise estatística

2. **Qualitativa:**
   - Entrevistas com vítimas e agressores: motivações, sentimentos
   - Observação no recreio: comportamentos
   - Compreensão profunda

**Resultado:** Visão completa (números + significados)

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (importante - pensamento científico em Ciências Sociais)

## Aula 15 - Português: Concordância Verbal e Nominal - 60min

### O que é Concordância?

**Concordância** é a relação de conformidade entre palavras de uma frase. Existem dois tipos:

- **Concordância Verbal:** Entre verbo e sujeito
- **Concordância Nominal:** Entre substantivo e seus modificadores (artigo, adjetivo, numeral, pronome)

### Concordância Verbal

O **verbo concorda com o sujeito** em número (singular/plural) e pessoa (1ª, 2ª, 3ª).

#### Regra Geral

**Sujeito simples:** Verbo concorda com o núcleo do sujeito.

**Exemplos:**
- O aluno estuda. (singular)
- Os alunos estudam. (plural)
- A casa é bonita. (singular)
- As casas são bonitas. (plural)

### Casos Especiais de Concordância Verbal

#### 1. Sujeito Composto (mais de um núcleo)

**Antes do verbo:** Verbo no **plural**

- O pai e a mãe viajaram.
- João e Maria chegaram cedo.

**Depois do verbo:** Duas opções

a) **Plural** (mais comum)
- Chegaram o pai e a mãe.

b) **Concorda com o núcleo mais próximo**
- Chegou o pai e a mãe. (menos usado)

#### 2. Sujeito Composto com Pessoas Diferentes

**Prioridade:** 1ª pessoa > 2ª pessoa > 3ª pessoa

- Eu (1ª) + tu (2ª) = nós (1ª pessoa plural)
- Eu (1ª) + ele (3ª) = nós (1ª pessoa plural)
- Tu (2ª) + ele (3ª) = vós (2ª pessoa plural) ou vocês (3ª plural - mais comum)

**Exemplos:**
- Eu e tu **somos** amigos. (nós)
- Eu e ele **somos** colegas. (nós)
- Tu e Maria **sois/são** inteligentes. (vós/vocês)

#### 3. Sujeito Composto Resumido por Pronome

Verbo concorda com o **pronome resumitivo**.

- Pais, filhos, avós, **ninguém** saiu. (singular - ninguém)
- Livros, cadernos, canetas, **tudo** estava na mesa. (singular - tudo)

#### 4. Expressões Partitivas (parte de, metade de, maioria de)

**Duas opções:**

a) Concorda com a expressão (singular)
- A maioria **chegou** cedo.
- A metade **saiu**.

b) Concorda com o complemento (mais comum)
- A maioria dos alunos **chegaram** cedo.
- A metade das pessoas **saíram**.

#### 5. Porcentagem

**Com numeral:** Concorda com o número

- 1% **chegou**. (singular)
- 50% **chegaram**. (plural)

**Com complemento:** Concorda com complemento

- 1% dos alunos **chegou/chegaram**.
- 50% da população **votou**.
- 50% dos eleitores **votaram**.

#### 6. Sujeito Coletivo

**Coletivo sem complemento:** Singular

- A multidão **gritou**.
- O bando **fugiu**.

**Coletivo com complemento:** Duas opções

a) Singular (com o coletivo)
- Um bando de pássaros **voou**.

b) Plural (com o complemento - mais comum)
- Um bando de pássaros **voaram**.

#### 7. Pronomes Indefinidos/Interrogativos + "de nós/vós"

**Qual/Quais, algum, nenhum, qual** + de nós/vós

a) **Pronome no singular:** verbo no singular
- Qual de nós **viajará**?

b) **Pronome no plural:** verbo concorda com pronome OU com "nós/vós"
- Quais de nós **viajarão**? (com "quais")
- Quais de nós **viajaremos**? (com "nós")

#### 8. Pronomes Relativos "que" e "quem"

**QUE:** Verbo concorda com o **antecedente**

- Fui eu que **fiz**. (antecedente: eu)
- Fomos nós que **fizemos**. (antecedente: nós)

**QUEM:** Duas opções

a) Concordar com "quem" (3ª pessoa singular)
- Fui eu quem **fez**.

b) Concordar com antecedente
- Fui eu quem **fiz**.

#### 9. Expressões "mais de um", "menos de dois"

**Mais de um:** Geralmente **singular**

- Mais de um aluno **faltou**.

**Exceção - reciprocidade:** Plural
- Mais de um deputado **agrediram-se**. (ação recíproca)

**Menos de dois:** **Plural**

- Menos de dois metros **bastam**.

#### 10. Sujeito Oracional (oração como sujeito)

Verbo da oração principal fica na **3ª pessoa do singular**.

- **É necessário** que todos participem.
- **Convém** estudar mais.
- **Parece** que vai chover.

#### 11. Verbos Impessoais (sem sujeito)

Ficam sempre na **3ª pessoa do singular**.

**HAVER (no sentido de existir, ocorrer, tempo decorrido):**
- **Há** muitas pessoas aqui. (= existem)
- **Havia** dez alunos. (= existiam)
- **Há** dois anos não o vejo. (tempo)

**FAZER (tempo decorrido, clima):**
- **Faz** dois meses que saí.
- **Faz** dias frios aqui.

**SER (horas, datas, distância):**
- **É** uma hora. / **São** duas horas.
- **É** dia 15. / **São** 15 de novembro.
- Daqui até lá **são** 10 km.

#### 12. Sujeito "se" (indeterminado)

Com **VTI, VL ou VI + SE:** 3ª pessoa **singular**

- **Precisa-se** de funcionários. (VTI)
- **Vive-se** bem aqui. (VI)

Com **VTD ou VTDI + SE (voz passiva):** Concorda com sujeito

- **Vendem-se** casas. (= casas são vendidas)
- **Aluga-se** apartamento. (= apartamento é alugado)
- **Consertam-se** relógios. (= relógios são consertados)

#### 13. Parecer + Infinitivo

**Duas construções corretas:**

a) "Parecer" varia, infinitivo fixo
- As crianças **parecem** gostar de brincar.

b) "Parecer" fixo, infinitivo varia
- As crianças **parece** gostarem de brincar.

**Ambas corretas!**

#### 14. Nomes Próprios no Plural

**Com artigo plural:** Verbo no plural

- **Os Estados Unidos** são poderosos.
- **Os Andes** ficam na América do Sul.

**Sem artigo ou artigo singular:** Verbo no singular

- **Estados Unidos** é poderoso.
- **Minas Gerais** produz leite.

### Concordância Nominal

**Regra geral:** Artigo, adjetivo, pronome e numeral concordam com o substantivo em gênero (masculino/feminino) e número (singular/plural).

**Exemplos:**
- O menino bonito
- A menina bonita
- Os meninos bonitos
- As meninas bonitas

### Casos Especiais de Concordância Nominal

#### 1. Adjetivo com Mais de um Substantivo

**Adjetivo ANTES:** Concorda com o mais **próximo**

- Lindo dia e tarde.
- Linda tarde e dia.

**Adjetivo DEPOIS:**

a) **Plural** (concordância geral - mais comum)
- Dia e tarde **lindos**.

b) **Concorda com o mais próximo**
- Dia e tarde **linda**.

**Se um substantivo for feminino e outro masculino, adjetivo no masculino plural:**
- A casa e o carro **novos**.

#### 2. Um Adjetivo para Vários Substantivos do Mesmo Gênero

**Plural ou concorda com o mais próximo:**

- Comprei livro e caderno **novo**. (próximo)
- Comprei livro e caderno **novos**. (plural)

#### 3. Anexo, Incluso, Mesmo, Próprio

**Concordam com o substantivo:**

- A foto está **anexa**.
- Os documentos estão **anexos**.
- Ela **mesma** fez.
- Eles **próprios** disseram.

**Atenção:** "Em anexo" é invariável
- Os documentos seguem **em anexo**.

#### 4. Bastante

**Adjetivo (= suficiente):** Varia

- Há **bastantes** razões.
- Comida **bastante**.

**Advérbio (= muito):** Invariável

- Eles são **bastante** inteligentes.
- Estudamos **bastante**.

#### 5. Meio

**Adjetivo (= metade):** Varia

- **Meia** garrafa.
- **Meios** estranhos.

**Advérbio (= um pouco):** Invariável

- Ela está **meio** cansada. (um pouco cansada)
- Elas estão **meio** tristes.

#### 6. Quite, Alerta

**Quite:** Varia
- Estou **quite**.
- Estamos **quites**.

**Alerta:** Invariável (advérbio)
- Fiquem **alerta**.
- Soldados **alerta**.

#### 7. É Proibido, É Necessário, É Bom

**SEM artigo:** Invariável (expressão impessoal)

- **É proibido** entrada.
- **É necessário** paciência.
- **É bom** cerveja gelada.

**COM artigo:** Varia

- **É proibida a** entrada.
- **É necessária a** paciência.
- **É boa a** cerveja gelada.

#### 8. Menos, Pseudo

**Sempre invariáveis:**

- **Menos** problemas.
- **Menos** alunas.
- **Pseudo** intelectuais.
- **Pseudo** ciência.

#### 9. Possível

**Com expressões "o mais, o menos, o melhor, o pior":**

**Artigo singular:** Possível no singular

- A casa **o mais confortável possível**.

**Artigo plural:** Possível no plural

- Casas **as mais confortáveis possíveis**.

### Exercícios Resolvidos

#### Exercício 1
Complete com a forma correta:

a) A maioria dos alunos _______ (chegar) cedo.
b) Mais de um candidato _______ (desistir).
c) _______ (Haver) muitas pessoas na festa.

**Resposta:**
a) **chegou** ou **chegaram** (ambas corretas)
b) **desistiu** (mais de um → singular)
c) **Havia** (haver = existir → sempre singular)

#### Exercício 2
Corrija se necessário:

a) Fazem dois anos que não o vejo.
b) Houveram muitos problemas.
c) Podem haver soluções.

**Resposta:**
a) **Faz** dois anos (fazer = tempo → impessoal, singular)
b) **Houve** muitos problemas (haver = existir → impessoal, singular)
c) **Pode haver** soluções (haver impessoal não varia; "poder" fica singular)

#### Exercício 3
Complete:

a) Vende-se casas / Vendem-se casas
b) Precisa-se de funcionários / Precisam-se de funcionários
c) Aluga-se apartamentos / Alugam-se apartamentos

**Resposta:**
a) **Vendem-se** casas (VTD + se = voz passiva, concorda)
b) **Precisa-se** de funcionários (VTI + se = indeterminado, singular)
c) **Alugam-se** apartamentos (VTD + se = voz passiva, concorda)

#### Exercício 4
Concordância nominal:

a) A casa e o carro _______ (novo).
b) Seguem _______ (anexo) os documentos.
c) Ela está _______ (meio) nervosa.

**Resposta:**
a) **novos** (masculino plural quando há gêneros diferentes)
b) **anexos** (concorda com "documentos")
c) **meio** (advérbio = um pouco → invariável)

#### Exercício 5
Complete:

a) É _______ (proibido) entrada.
b) É _______ (proibido) a entrada.
c) Elas _______ (mesmo) fizeram.

**Resposta:**
a) **proibido** (sem artigo → invariável)
b) **proibida** (com artigo → varia)
c) **mesmas** (concorda com "elas")

### Dicas para a Prova

1. **Sujeito composto antes do verbo:** Plural
2. **Haver = existir:** Sempre singular (havia, houve, há)
3. **Fazer = tempo:** Sempre singular (faz, fazia)
4. **VTD + se:** Concorda (vendem-se casas)
5. **VTI + se:** Singular (precisa-se de)
6. **Meio (advérbio):** Invariável (meio cansada)
7. **Anexo:** Varia (documentos anexos)
8. **"É proibido" sem artigo:** Invariável
9. **Mais de um:** Singular (mais de um saiu)
10. **Menos de dois:** Plural (menos de dois metros)

### Conceitos-Chave para Memorizar

**Concordância Verbal:**
- Verbo concorda com sujeito em número e pessoa
- Sujeito composto: plural
- Verbos impessoais: 3ª singular (haver, fazer)
- VTD + se: concorda; VTI + se: singular

**Concordância Nominal:**
- Adjetivo concorda com substantivo
- Anexo, incluso, mesmo, próprio: variam
- Meio (advérbio): invariável
- Bastante (advérbio): invariável
- É proibido (sem artigo): invariável

### Resumo - Verbos Impessoais

```
┌──────────────┬─────────────────┬──────────────┐
│    Verbo     │     Sentido     │  Concordância│
├──────────────┼─────────────────┼──────────────┤
│ HAVER        │ Existir         │  Singular    │
│ HAVER        │ Tempo decorrido │  Singular    │
│ FAZER        │ Tempo decorrido │  Singular    │
│ FAZER        │ Clima/fenômeno  │  Singular    │
│ SER          │ Horas/datas     │  Varia       │
└──────────────┴─────────────────┴──────────────┘
```

### Quadro - Partícula SE

```
┌──────────┬─────────────────┬──────────────────┐
│   Verbo  │    Com SE       │   Concordância   │
├──────────┼─────────────────┼──────────────────┤
│   VTD    │ Voz passiva     │ Concorda com suj.│
│   VTI    │ Indeterminado   │ 3ª sing. sempre  │
│   VI     │ Indeterminado   │ 3ª sing. sempre  │
│   VL     │ Indeterminado   │ 3ª sing. sempre  │
└──────────┴─────────────────┴──────────────────┘

Exemplos:
VTD: Vendem-se casas (= casas são vendidas)
VTI: Precisa-se de ajuda (sujeito indeterminado)
```

### Macetes

**HAVER:**
"Há pessoas" = "Existem pessoas" → SEMPRE singular quando = existir

**FAZER (tempo):**
"Faz anos" → NUNCA "fazem anos"

**VTD + SE:**
Se dá para passar para voz passiva, concorda!
- Vendem-se casas = Casas são vendidas → CONCORDA

**MEIO:**
Se puder trocar por "um pouco" → invariável
- Ela está meio (um pouco) cansada

**É PROIBIDO:**
Tem "a/o" na frente? → Varia
Não tem? → Não varia

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - cai muito em vestibulares e redações)

---

# 11/21 - Dia 4

## Aula 16 - Matemática: Função Afim - Parte 1 - 120min

### O que é Função?

**Função** é uma relação entre dois conjuntos (domínio e contradomínio) onde cada elemento do domínio está associado a um único elemento do contradomínio.

**Notação:** f: A → B (lê-se "f de A em B")
- f(x) = y (lê-se "f de x igual a y")
- x: variável independente (entrada)
- y: variável dependente (saída)

**Exemplo prático:**
- Preço de laranjas: f(x) = 5x
- x = número de laranjas
- f(x) = preço total
- f(3) = 5(3) = 15 reais

### Função Afim (ou Função do 1º Grau)

**Definição:** Função afim é toda função f: ℝ → ℝ da forma:

```
f(x) = ax + b
```

Onde:
- **a** e **b** são números reais
- **a ≠ 0** (se a = 0, é função constante)
- **a**: coeficiente angular (taxa de variação)
- **b**: coeficiente linear (valor inicial, quando x = 0)

**Exemplos:**
- f(x) = 2x + 3 (a = 2, b = 3)
- f(x) = -x + 5 (a = -1, b = 5)
- f(x) = 3x (a = 3, b = 0)
- f(x) = -4 + 2x (a = 2, b = -4)

### Coeficientes da Função Afim

#### Coeficiente Linear (b)

**Representa:**
- Valor de f(x) quando x = 0
- Ponto onde a reta corta o eixo y
- Valor inicial

**Exemplo:**
f(x) = 2x + 3
f(0) = 2(0) + 3 = 3
Ponto (0, 3) no eixo y

#### Coeficiente Angular (a)

**Representa:**
- Taxa de variação da função
- Inclinação da reta
- Quanto y varia quando x aumenta 1 unidade

**Interpretação:**
- a > 0: função crescente
- a < 0: função decrescente
- |a| maior: reta mais inclinada

**Exemplo:**
f(x) = 2x + 3
Quando x aumenta 1, y aumenta 2
- f(0) = 3
- f(1) = 5 (aumentou 2)
- f(2) = 7 (aumentou 2)

### Casos Especiais

#### Função Linear (b = 0)

f(x) = ax

- Passa pela origem (0, 0)
- Proporcionalidade direta

**Exemplos:**
- f(x) = 3x
- f(x) = -2x

#### Função Constante (a = 0)

f(x) = b

- Reta horizontal
- Valor sempre igual a b
- **Tecnicamente não é função afim** (a deve ser ≠ 0)

**Exemplo:**
- f(x) = 5 (sempre vale 5)

#### Função Identidade (a = 1, b = 0)

f(x) = x

- Bissetriz do 1º e 3º quadrantes
- Ângulo de 45° com os eixos
- f(x) = x para todo x

### Gráfico da Função Afim

**O gráfico é sempre uma RETA.**

#### Como Construir o Gráfico

**Método 1: Dois pontos**

Basta encontrar 2 pontos e traçar a reta.

**Pontos mais fáceis:**
1. **Quando x = 0:** f(0) = b → ponto (0, b)
2. **Quando f(x) = 0:** Zero da função → ponto (raiz, 0)

**Exemplo:** f(x) = 2x - 4

**Ponto 1:** x = 0
f(0) = 2(0) - 4 = -4 → (0, -4)

**Ponto 2:** f(x) = 0
0 = 2x - 4
2x = 4
x = 2 → (2, 0)

Traçar reta pelos pontos (0, -4) e (2, 0).

**Método 2: Tabela de valores**

Escolher valores de x e calcular f(x).

| x | f(x) = 2x - 4 |
|---|---------------|
| 0 | -4 |
| 1 | -2 |
| 2 | 0 |
| 3 | 2 |

### Análise do Gráfico

#### Função Crescente (a > 0)

```
y ↑
  |     /
  |    /
  |   /
  |  /
  | /
  |/___________→ x
```

- Da esquerda para direita: sobe
- Quanto maior x, maior f(x)

**Exemplos:**
- f(x) = 2x + 1
- f(x) = 0,5x - 3

#### Função Decrescente (a < 0)

```
y ↑
  |\
  | \
  |  \
  |   \
  |    \
  |_____\______→ x
```

- Da esquerda para direita: desce
- Quanto maior x, menor f(x)

**Exemplos:**
- f(x) = -3x + 2
- f(x) = -x + 4

### Zero ou Raiz da Função

**Zero da função:** Valor de x para o qual f(x) = 0.

**Como encontrar:**
f(x) = 0
ax + b = 0
ax = -b
**x = -b/a**

**Interpretação geométrica:**
- Ponto onde a reta corta o eixo x
- Coordenadas: (-b/a, 0)

**Exemplo 1:**
f(x) = 2x - 6
0 = 2x - 6
2x = 6
x = 3

Raiz: x = 3 (ponto (3, 0))

**Exemplo 2:**
f(x) = -x + 5
0 = -x + 5
x = 5

Raiz: x = 5 (ponto (5, 0))

### Estudo do Sinal da Função

**Determinar para quais valores de x:**
- f(x) > 0 (função positiva)
- f(x) = 0 (função nula)
- f(x) < 0 (função negativa)

**Método:**
1. Encontrar a raiz (x = -b/a)
2. Analisar o sinal de acordo com a

#### Função Crescente (a > 0)

```
      ++++++++++
─────────●─────────→ x
  -------  raiz
```

- x < raiz: f(x) < 0 (negativo)
- x = raiz: f(x) = 0
- x > raiz: f(x) > 0 (positivo)

**Exemplo:** f(x) = 2x - 4
Raiz: x = 2

- x < 2: f(x) < 0
- x = 2: f(x) = 0
- x > 2: f(x) > 0

#### Função Decrescente (a < 0)

```
  -------
─────────●─────────→ x
      ++++++++++
       raiz
```

- x < raiz: f(x) > 0 (positivo)
- x = raiz: f(x) = 0
- x > raiz: f(x) < 0 (negativo)

**Exemplo:** f(x) = -x + 3
Raiz: x = 3

- x < 3: f(x) > 0
- x = 3: f(x) = 0
- x > 3: f(x) < 0

### Taxa de Variação

**Taxa de variação:** Quanto a função varia quando x varia.

**Fórmula:**
```
a = Δy / Δx = (y₂ - y₁) / (x₂ - x₁)
```

**Interpretação:**
- a = 2: a cada 1 unidade que x aumenta, y aumenta 2
- a = -3: a cada 1 unidade que x aumenta, y diminui 3

**Exemplo:**
Dois pontos: (1, 3) e (4, 9)

a = (9 - 3) / (4 - 1) = 6 / 3 = 2

Taxa de variação: 2 (função cresce 2 unidades de y para cada unidade de x)

### Determinando a Função Afim

#### Caso 1: Dados a e b

**Direto:** f(x) = ax + b

**Exemplo:** a = 3, b = -2
f(x) = 3x - 2

#### Caso 2: Dados dois pontos

**Método:**
1. Calcular a: a = (y₂ - y₁) / (x₂ - x₁)
2. Substituir um ponto em f(x) = ax + b para encontrar b

**Exemplo:**
Pontos: (1, 5) e (3, 11)

**Passo 1:** Calcular a
a = (11 - 5) / (3 - 1) = 6 / 2 = 3

**Passo 2:** Encontrar b (usando ponto (1, 5))
5 = 3(1) + b
5 = 3 + b
b = 2

**Função:** f(x) = 3x + 2

**Verificação com o outro ponto (3, 11):**
f(3) = 3(3) + 2 = 9 + 2 = 11 ✓

#### Caso 3: Dados raiz e um ponto

**Método:**
1. Raiz → f(raiz) = 0 → ponto (raiz, 0)
2. Usar dois pontos (raiz e ponto dado)

**Exemplo:**
Raiz: x = 2, ponto: (0, -4)

**Passo 1:** a = (-4 - 0) / (0 - 2) = -4 / -2 = 2

**Passo 2:** Usando (0, -4)
-4 = 2(0) + b
b = -4

**Função:** f(x) = 2x - 4

### Interseção de Retas

**Ponto de interseção:** Onde duas funções têm o mesmo valor.

**Método:** Igualar as funções

f(x) = g(x)

**Exemplo:**
f(x) = 2x + 1
g(x) = -x + 4

2x + 1 = -x + 4
3x = 3
x = 1

f(1) = 2(1) + 1 = 3

**Ponto de interseção:** (1, 3)

### Inequações do 1º Grau

**Resolver inequações usando o estudo do sinal.**

**Exemplo 1:**
2x - 4 > 0

Raiz: 2x - 4 = 0 → x = 2
a = 2 > 0 (crescente)

Estudo do sinal:
- x < 2: negativo
- x > 2: positivo

**Solução:** x > 2 ou (2, +∞)

**Exemplo 2:**
-x + 3 ≥ 0

Raiz: x = 3
a = -1 < 0 (decrescente)

Estudo do sinal:
- x < 3: positivo
- x > 3: negativo

**Solução:** x ≤ 3 ou (-∞, 3]

### Aplicações Práticas

#### Exemplo 1: Conversão de Temperatura

Celsius para Fahrenheit: F = 1,8C + 32

- C = 0°: F = 32°F
- C = 100°: F = 212°F

**Pergunta:** Qual temperatura tem o mesmo valor em °C e °F?

C = F
C = 1,8C + 32
C - 1,8C = 32
-0,8C = 32
C = -40°C

**Resposta:** -40°C = -40°F

#### Exemplo 2: Custo de Táxi

Bandeirada: R$ 5,00
Por km: R$ 3,00/km

**Função:** C(x) = 3x + 5

onde x = distância em km

**Pergunta:** Quanto custa uma corrida de 12 km?
C(12) = 3(12) + 5 = 36 + 5 = R$ 41,00

#### Exemplo 3: Plano de Celular

Plano A: R$ 50 fixo + R$ 0,50/min
Plano B: R$ 30 fixo + R$ 1,00/min

A(x) = 50 + 0,5x
B(x) = 30 + 1,0x

**Pergunta:** A partir de quantos minutos o Plano A é mais vantajoso?

A(x) < B(x)
50 + 0,5x < 30 + 1,0x
50 - 30 < 1,0x - 0,5x
20 < 0,5x
x > 40

**Resposta:** Plano A é melhor a partir de 40 minutos.

### Exercícios Resolvidos

#### Exercício 1
Determine a função afim f(x) = ax + b sabendo que f(2) = 5 e f(4) = 11.

**Solução:**
Pontos: (2, 5) e (4, 11)

a = (11 - 5) / (4 - 2) = 6 / 2 = 3

5 = 3(2) + b
5 = 6 + b
b = -1

**Resposta:** f(x) = 3x - 1

#### Exercício 2
Encontre o zero da função f(x) = -2x + 8.

**Solução:**
0 = -2x + 8
2x = 8
x = 4

**Resposta:** Zero em x = 4

#### Exercício 3
Estude o sinal de f(x) = 3x - 9.

**Solução:**
Raiz: 3x - 9 = 0 → x = 3
a = 3 > 0 (crescente)

- x < 3: f(x) < 0 (negativo)
- x = 3: f(x) = 0
- x > 3: f(x) > 0 (positivo)

#### Exercício 4
Determine o ponto de interseção das retas f(x) = 2x - 1 e g(x) = -x + 5.

**Solução:**
2x - 1 = -x + 5
3x = 6
x = 2

y = 2(2) - 1 = 3

**Resposta:** Ponto (2, 3)

#### Exercício 5
Resolva a inequação: 4x - 8 ≤ 0

**Solução:**
Raiz: 4x = 8 → x = 2
a = 4 > 0 (crescente)

f(x) ≤ 0 → região negativa ou zero

**Resposta:** x ≤ 2 ou (-∞, 2]

### Dicas para a Prova

1. **Gráfico é sempre reta** (função do 1º grau)
2. **a > 0:** crescente; **a < 0:** decrescente
3. **Raiz:** x = -b/a (onde corta eixo x)
4. **b:** onde corta eixo y (quando x = 0)
5. **Dois pontos determinam uma reta** (e a função)
6. **Estudo do sinal:** use a raiz + crescente/decrescente
7. **Inequação:** estudo do sinal da função
8. **Interseção:** igualar as funções

### Conceitos-Chave para Memorizar

**Função Afim:**
- f(x) = ax + b (a ≠ 0)
- Gráfico: reta
- a: coeficiente angular (taxa de variação)
- b: coeficiente linear (intercepto em y)

**Comportamento:**
- a > 0: crescente
- a < 0: decrescente
- |a| maior: mais inclinada

**Zero/Raiz:**
- x = -b/a
- Ponto (−b/a, 0)

**Estudo do sinal:**
- Crescente: − 0 +
- Decrescente: + 0 −

### Fórmulas Essenciais

```
Função Afim:
f(x) = ax + b (a ≠ 0)

Coeficiente angular:
a = Δy/Δx = (y₂ - y₁)/(x₂ - x₁)

Zero da função:
f(x) = 0
x = -b/a

Casos especiais:
Função linear: f(x) = ax (b = 0)
Função identidade: f(x) = x (a = 1, b = 0)
Função constante: f(x) = b (a = 0)

Ponto de interseção:
f(x) = g(x)
```

### Resumo Visual

```
┌─────────────┬──────────────┬──────────────┐
│  Sinal de a │   Gráfico    │ Comportamento│
├─────────────┼──────────────┼──────────────┤
│   a > 0     │      /       │  Crescente   │
│   a < 0     │      \       │  Decrescente │
└─────────────┴──────────────┴──────────────┘

┌──────────────┬─────────────────────────────┐
│  Coeficiente │        Significado          │
├──────────────┼─────────────────────────────┤
│      a       │ Taxa de variação/Inclinação │
│      b       │ Valor inicial (x=0)         │
│    -b/a      │ Raiz/Zero da função         │
└──────────────┴─────────────────────────────┘
```

---

**Tempo de estudo recomendado:** 120 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base para todas as funções)

## Aula 17 - Física: Movimento Circular - 75min

### O que é Movimento Circular?

**Movimento Circular** é o movimento de um corpo que descreve uma trajetória circular ou curva. É um dos movimentos mais comuns na natureza e na tecnologia: rodas, engrenagens, planetas, elétrons, etc.

**Características principais:**
- Trajetória: circunferência ou arco de círculo
- Direção da velocidade: sempre tangente à trajetória
- Pode ser uniforme (velocidade constante) ou variado

### Movimento Circular Uniforme (MCU)

No **MCU**, o corpo percorre arcos iguais em tempos iguais. A **velocidade escalar** é constante, mas a **velocidade vetorial** muda constantemente de direção.

**Propriedades do MCU:**
- Velocidade escalar constante: |v| = constante
- Velocidade vetorial varia (direção muda)
- Existe aceleração centrípeta (direcionada ao centro)

### Grandezas Angulares

#### Posição Angular (θ)
Ângulo que o raio vetor forma com uma referência.

**Unidades:**
- **Radiano (rad):** unidade SI
- **Grau (°):** 360° = 2π rad
- **Volta completa:** 2π rad = 360°

**Conversão:**
- 180° = π rad
- 1 rad ≈ 57,3°
- θ (rad) = θ (graus) × π/180

#### Deslocamento Angular (Δθ)
Variação da posição angular.
Δθ = θ_final - θ_inicial

#### Velocidade Angular (ω)
Taxa de variação da posição angular.

**Fórmula:**
```
ω = Δθ/Δt
```

**Unidades:**
- rad/s (SI)
- rpm (rotações por minuto)
- rps (rotações por segundo)

**No MCU:** ω = constante

**Conversões:**
- 1 rpm = 2π/60 rad/s ≈ 0,105 rad/s
- 1 rps = 2π rad/s ≈ 6,28 rad/s

#### Período (T)
Tempo para completar uma volta completa.

**Fórmula:**
```
T = 2π/ω
```

**Unidade:** segundos (s)

#### Frequência (f)
Número de voltas por unidade de tempo.

**Fórmula:**
```
f = 1/T
f = ω/2π
```

**Unidades:**
- Hz (hertz) = 1/s = 1 volta/segundo
- rpm (rotações por minuto)

**Relação:**
```
f × T = 1
```

### Relação entre Grandezas Lineares e Angulares

#### Arco Percorrido (s)
```
s = θ × R
```
Onde:
- s: comprimento do arco (m)
- θ: ângulo em radianos (rad)
- R: raio da trajetória (m)

#### Velocidade Linear (v)
```
v = ω × R
```

Onde:
- v: velocidade linear (m/s)
- ω: velocidade angular (rad/s)
- R: raio (m)

**Para uma volta completa:**
```
v = 2πR/T
v = 2πRf
```

### Aceleração Centrípeta (a_cp)

No MCU, existe aceleração mesmo com velocidade escalar constante, pois a **direção** da velocidade muda.

**Aceleração Centrípeta:**
- **Direção:** sempre apontando para o centro
- **Módulo:** constante no MCU

**Fórmulas:**
```
a_cp = v²/R
a_cp = ω²R
a_cp = 4π²R/T²
a_cp = 4π²Rf²
```

Onde:
- a_cp: aceleração centrípeta (m/s²)
- v: velocidade linear (m/s)
- R: raio (m)
- ω: velocidade angular (rad/s)
- T: período (s)
- f: frequência (Hz)

### Movimento Circular Uniformemente Variado (MCUV)

Quando a velocidade angular varia uniformemente.

**Aceleração Angular (α):**
```
α = Δω/Δt
```

**Funções do MCUV:**
```
ω = ω₀ + αt
θ = θ₀ + ω₀t + αt²/2
ω² = ω₀² + 2αΔθ
```

**Analogia com MUV:**
| Linear (MUV) | Angular (MCUV) |
|--------------|----------------|
| s (posição)  | θ (posição angular) |
| v (velocidade) | ω (vel. angular) |
| a (aceleração) | α (acel. angular) |
| v = v₀ + at  | ω = ω₀ + αt |
| s = s₀ + v₀t + at²/2 | θ = θ₀ + ω₀t + αt²/2 |

**No MCUV também existe:**
- Aceleração centrípeta (varia com ω)
- Aceleração tangencial: a_t = α × R

### Exercícios Resolvidos

#### Exercício 1
Um CD gira a 120 rpm. Calcule:
a) A frequência em Hz
b) O período
c) A velocidade angular em rad/s

**Solução:**

a) f = 120 rpm = 120/60 = 2 Hz

b) T = 1/f = 1/2 = 0,5 s

c) ω = 2πf = 2π(2) = 4π rad/s ≈ 12,56 rad/s

**Respostas:** a) 2 Hz; b) 0,5 s; c) 4π rad/s

#### Exercício 2
Uma roda de raio 0,5 m gira com velocidade angular de 10 rad/s. Determine:
a) A velocidade linear de um ponto na periferia
b) A aceleração centrípeta

**Solução:**

a) v = ωR = 10 × 0,5 = 5 m/s

b) a_cp = ω²R = (10)² × 0,5 = 100 × 0,5 = 50 m/s²

Ou: a_cp = v²/R = 25/0,5 = 50 m/s²

**Respostas:** a) 5 m/s; b) 50 m/s²

#### Exercício 3
Um satélite completa uma órbita circular de raio 7000 km em 90 minutos. Calcule sua velocidade linear.

**Solução:**

T = 90 min = 90 × 60 = 5400 s
R = 7000 km = 7 × 10⁶ m

v = 2πR/T = 2π(7 × 10⁶)/5400
v = 14π × 10⁶/5400
v ≈ 8148 m/s ≈ 8,15 km/s

**Resposta:** ≈ 8,15 km/s

#### Exercício 4
(UFMG) Uma roda gigante tem 10 m de raio e completa uma volta em 40 s. A aceleração centrípeta de um passageiro é aproximadamente:

**Solução:**

R = 10 m
T = 40 s

a_cp = 4π²R/T² = 4π²(10)/(40)²
a_cp = 40π²/1600 = π²/40
a_cp ≈ 9,87/40 ≈ 0,25 m/s²

**Resposta:** ≈ 0,25 m/s²

### Dicas para a Prova

1. **Sempre converta rpm para rad/s ou Hz** quando necessário
2. **Radianos:** θ deve estar em radianos em s = θR
3. **Período e frequência:** f = 1/T (são inversamente proporcionais)
4. **Velocidade no MCU:** v = ωR (relaciona linear e angular)
5. **Aceleração centrípeta:** sempre aponta para o centro, existe mesmo com v constante
6. **MCU vs MCUV:** MCU tem ω constante; MCUV tem α constante
7. **Unidades:** cuidado com km → m, min → s, rpm → rad/s
8. **Analogia MUV-MCUV:** todas as equações são análogas

### Conceitos-Chave para Memorizar

**Grandezas Angulares:**
- θ: posição angular (rad)
- ω: velocidade angular (rad/s)
- α: aceleração angular (rad/s²)
- T: período (s)
- f: frequência (Hz)

**Relações:**
- f = 1/T
- ω = 2πf = 2π/T
- 1 volta = 2π rad = 360°

**Linear ↔ Angular:**
- s = θR
- v = ωR
- a_t = αR

**Aceleração Centrípeta (MCU):**
- a_cp = v²/R
- a_cp = ω²R
- Direção: para o centro

### Fórmulas Essenciais

```
Velocidade Angular:
ω = Δθ/Δt
ω = 2π/T = 2πf

Período e Frequência:
T = 1/f
f = 1/T

Conversões:
1 volta = 2π rad = 360°
1 rpm = 2π/60 rad/s

Relação Linear-Angular:
s = θR (θ em radianos)
v = ωR

Aceleração Centrípeta:
a_cp = v²/R
a_cp = ω²R
a_cp = 4π²R/T²

MCUV:
ω = ω₀ + αt
θ = θ₀ + ω₀t + αt²/2
ω² = ω₀² + 2αΔθ
```

### Resumo Visual

```
┌─────────────────┬─────────────┬────────────┐
│   Grandeza      │   Símbolo   │  Unidade   │
├─────────────────┼─────────────┼────────────┤
│ Pos. Angular    │      θ      │   rad      │
│ Vel. Angular    │      ω      │   rad/s    │
│ Acel. Angular   │      α      │   rad/s²   │
│ Período         │      T      │     s      │
│ Frequência      │      f      │    Hz      │
└─────────────────┴─────────────┴────────────┘

Relações MCU:
        ω
       ↗ ↖
      /   \
     f  -  T
    (f = 1/T)

Aceleração Centrípeta:
     ↑ v
    ← • → a_cp (sempre para o centro)
     ↓
```

---

**Tempo de estudo recomendado:** 75 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - conceitos fundamentais de cinemática)

## Aula 18 - Química: Tabela Periódica - 90min

### A Tabela Periódica Moderna

A **Tabela Periódica** é uma organização sistemática de todos os elementos químicos conhecidos, arranjados em ordem crescente de **número atômico (Z)**.

**História:**
- **Mendeleev (1869):** primeira tabela periódica (ordem de massa atômica)
- Previu propriedades de elementos ainda não descobertos
- **Moseley (1913):** reorganizou por número atômico (Lei Periódica Moderna)

**Lei Periódica Moderna:**
> "As propriedades físicas e químicas dos elementos são funções periódicas de seus números atômicos."

### Estrutura da Tabela Periódica

#### Períodos (Linhas Horizontais)
São as **7 linhas horizontais** da tabela.

**Período indica:**
- Número de camadas eletrônicas (níveis de energia)
- Elementos do mesmo período têm o mesmo número de camadas

**Exemplos:**
- **Período 1:** H, He (1 camada: K)
- **Período 2:** Li, Be, B, C, N, O, F, Ne (2 camadas: K, L)
- **Período 3:** Na, Mg, Al, Si, P, S, Cl, Ar (3 camadas: K, L, M)

#### Famílias ou Grupos (Colunas Verticais)
São as **18 colunas verticais** da tabela.

**Família indica:**
- Número de elétrons na camada de valência (última camada)
- Elementos da mesma família têm propriedades químicas semelhantes

**Principais famílias:**

| Grupo | Nome | Elétrons Valência | Características |
|-------|------|-------------------|-----------------|
| 1 (IA) | Metais Alcalinos | 1 | Muito reativos, moles, baixa densidade |
| 2 (IIA) | Metais Alcalino-Terrosos | 2 | Reativos, mais duros que alcalinos |
| 13 (IIIA) | Família do Boro | 3 | Propriedades variadas |
| 14 (IVA) | Família do Carbono | 4 | Base da química orgânica |
| 15 (VA) | Família do Nitrogênio | 5 | Não-metais importantes |
| 16 (VIA) | Calcogênios | 6 | Oxigênio e enxofre são essenciais |
| 17 (VIIA) | Halogênios | 7 | Muito reativos, formam sais |
| 18 (VIIIA) | Gases Nobres | 8 (exceto He: 2) | Inertes, estáveis |

**Nomenclaturas:**
- **Antiga:** IA, IIA, IIIA... VIIIA
- **Moderna (IUPAC):** 1, 2, 3... 18

#### Elementos Representativos, Transição e Transição Interna

**Elementos Representativos:**
- Grupos 1, 2, 13, 14, 15, 16, 17, 18
- Famílias A (notação antiga)
- Camadas de valência: s ou p

**Elementos de Transição:**
- Grupos 3 a 12
- Famílias B (notação antiga)
- Camadas de valência: d (e também s)
- Todos são metais

**Elementos de Transição Interna:**
- **Lantanídeos:** elementos 57-71
- **Actinídeos:** elementos 89-103
- Camadas de valência: f (e também d e s)
- Colocados separadamente na tabela

### Classificação dos Elementos

#### Metais
**Características:**
- Brilho metálico
- Condutores de calor e eletricidade
- Maleáveis e dúcteis
- Sólidos (exceto Hg - mercúrio)
- Tendência a perder elétrons (formar cátions)

**Localização:** maioria da tabela (lado esquerdo e centro)

**Exemplos:** Na, Fe, Cu, Au, Ag, Al, Zn

#### Não-Metais (Ametais)
**Características:**
- Sem brilho metálico
- Isolantes (maus condutores)
- Quebradiços no estado sólido
- Estados variados (sólidos, líquidos, gasosos)
- Tendência a ganhar elétrons (formar ânions)

**Localização:** canto superior direito

**Exemplos:** C, N, O, P, S, Cl, Br (líquido)

#### Semimetais (Metaloides)
**Características:**
- Propriedades intermediárias
- Semicondutores
- Importantes para eletrônica

**Localização:** "escada" entre metais e não-metais

**Exemplos:** B, Si, Ge, As, Sb, Te, (Po)

#### Gases Nobres
**Características:**
- Inertes (muito estáveis)
- Não formam ligações facilmente
- Camada de valência completa
- Todos são gases

**Exemplos:** He, Ne, Ar, Kr, Xe, Rn

### Distribuição Eletrônica e Posição na Tabela

A distribuição eletrônica determina a posição do elemento:

**Regras:**
1. **Último nível ocupado** → Período (número de camadas)
2. **Elétrons na camada de valência** → Família

**Subnível mais energético:**
- **s ou p:** elemento representativo (família A)
- **d:** elemento de transição (família B)
- **f:** transição interna

**Exemplos:**

**Sódio (Na, Z = 11):**
- Distribuição: 1s² 2s² 2p⁶ 3s¹
- Camadas: K=2, L=8, M=1 → **3 camadas** → Período 3
- Valência: 1 elétron → **Grupo 1** (IA) - Metais Alcalinos

**Cloro (Cl, Z = 17):**
- Distribuição: 1s² 2s² 2p⁶ 3s² 3p⁵
- Camadas: K=2, L=8, M=7 → **3 camadas** → Período 3
- Valência: 7 elétrons → **Grupo 17** (VIIA) - Halogênios

**Ferro (Fe, Z = 26):**
- Distribuição: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶
- Camadas: 4 → Período 4
- Subnível mais energético: 3d → **Elemento de transição**

### Propriedades Periódicas e Aperiódicas

**Propriedades Periódicas:** variam periodicamente com o número atômico

**Propriedades Aperiódicas:** não seguem periodicidade (ex: massa atômica)

*Estudaremos as propriedades periódicas detalhadamente na próxima aula (Aula 23).*

### Exercícios Resolvidos

#### Exercício 1
Um elemento químico tem número atômico 19. Determine:
a) Sua distribuição eletrônica
b) Seu período
c) Sua família
d) Sua classificação (metal, não-metal, etc.)

**Solução:**

a) Z = 19 → 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹

b) 4 camadas (K, L, M, N) → **Período 4**

c) 1 elétron na valência → **Grupo 1 (IA)** - Metais Alcalinos

d) Grupo 1, lado esquerdo → **Metal alcalino**

*É o elemento Potássio (K)*

**Respostas:** a) 1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹; b) Período 4; c) Grupo 1 (IA); d) Metal alcalino

#### Exercício 2
Qual família tem 7 elétrons na camada de valência? Quais suas principais características?

**Solução:**

7 elétrons na valência → **Grupo 17 (VIIA) - Halogênios**

**Características:**
- Muito reativos
- Formam sais com metais
- Ganham 1 elétron facilmente (formam ânions -1)
- Elementos: F, Cl, Br, I, At

**Resposta:** Halogênios (Grupo 17/VIIA); muito reativos, formam sais

#### Exercício 3
(UFMG) Um elemento X está no 3º período e tem 5 elétrons na camada de valência. Determine:
a) Sua distribuição eletrônica
b) Sua família
c) Seu número atômico

**Solução:**

3º período: 3 camadas (K, L, M)
5 elétrons na valência: M tem 5 elétrons

Distribuição:
K = 2
L = 8
M = 5

a) 1s² 2s² 2p⁶ 3s² 3p³

b) 5 elétrons → **Grupo 15 (VA)** - Família do Nitrogênio

c) Z = 2 + 8 + 5 = **15** (Fósforo - P)

**Respostas:** a) 1s² 2s² 2p⁶ 3s² 3p³; b) Grupo 15 (VA); c) Z = 15 (Fósforo)

#### Exercício 4
Classifique os elementos em metal, não-metal, semimetal ou gás nobre:
a) Grupo 1
b) Grupo 18
c) Silício (Si)
d) Oxigênio (O)

**Solução:**

a) Grupo 1 (IA) → **Metais alcalinos** (metal)

b) Grupo 18 (VIIIA) → **Gases nobres**

c) Si: localizado na "escada" → **Semimetal**

d) O: canto superior direito → **Não-metal** (ametal)

**Respostas:** a) Metal; b) Gás nobre; c) Semimetal; d) Não-metal

### Dicas para a Prova

1. **Período = número de camadas** (níveis de energia)
2. **Família = elétrons na valência** (última camada)
3. **Grupos principais:** 1 (alcalinos), 2 (alcalino-terrosos), 17 (halogênios), 18 (gases nobres)
4. **Metais:** maioria (esquerda/centro); **não-metais:** canto superior direito
5. **Semimetais:** "escada" entre metais e não-metais
6. **Transição:** grupos 3-12 (todos metais, subnível d)
7. **Gases nobres:** extremamente estáveis (valência completa)
8. **Distribuição eletrônica** determina tudo: período e família

### Conceitos-Chave para Memorizar

**Organização:**
- **Horizontal (Períodos):** 7 linhas = número de camadas
- **Vertical (Grupos/Famílias):** 18 colunas = elétrons de valência

**Famílias importantes:**
- Grupo 1: Metais Alcalinos (1 e⁻ valência)
- Grupo 2: Alcalino-Terrosos (2 e⁻)
- Grupo 17: Halogênios (7 e⁻)
- Grupo 18: Gases Nobres (8 e⁻, exceto He)

**Classificação:**
- Metais: esquerda/centro (perdem e⁻)
- Não-metais: direita superior (ganham e⁻)
- Semimetais: "escada" (semicondutores)
- Gases nobres: grupo 18 (inertes)

**Lei Periódica:**
Propriedades variam periodicamente com número atômico (Z)

### Fórmulas e Conceitos Essenciais

```
Número Atômico (Z):
Determina a posição na tabela

Distribuição Eletrônica → Posição:
Último nível → Período
Elétrons valência → Família

Valência por Grupo:
Grupo 1: 1 elétron
Grupo 2: 2 elétrons
Grupo 13: 3 elétrons
Grupo 14: 4 elétrons
Grupo 15: 5 elétrons
Grupo 16: 6 elétrons
Grupo 17: 7 elétrons
Grupo 18: 8 elétrons (He: 2)

Subnível mais energético:
s ou p → Representativo (A)
d → Transição (B)
f → Transição interna
```

### Resumo Visual

```
Estrutura da Tabela Periódica:

PERÍODOS (1-7)
↓
1  IA ──────────────────────── VIIIA
2  IIA                          gases
3  Metais  Transição  Não-met. nobres
4  alcal.  (B)        Semimet.
5          3-12       IIIA-VIIA
6  
7  Lantanídeos (f)
   Actinídeos (f)

Classificação:
┌──────────┬─────────────────────┐
│ Posição  │  Classificação      │
├──────────┼─────────────────────┤
│ Esquerda │ Metais              │
│ Centro   │ Transição (metais)  │
│ "Escada" │ Semimetais          │
│ Direita  │ Não-metais          │
│ Grupo 18 │ Gases Nobres        │
└──────────┴─────────────────────┘

Principais Famílias:
Grupo 1:  Metais Alcalinos (1e⁻)
Grupo 2:  Alcalino-Terrosos (2e⁻)
Grupo 17: Halogênios (7e⁻) [reativos]
Grupo 18: Gases Nobres (8e⁻) [inertes]
```

### Tabela de Referência - Famílias

```
┌───────┬──────────────────┬──────┬──────────────┐
│ Grupo │ Nome             │ Val. │ Exemplos     │
├───────┼──────────────────┼──────┼──────────────┤
│  1    │ Alcalinos        │  1   │ Li,Na,K,Rb,Cs│
│  2    │ Alcalino-Terrosos│  2   │ Be,Mg,Ca,Sr,Ba│
│  13   │ Boro             │  3   │ B,Al,Ga,In   │
│  14   │ Carbono          │  4   │ C,Si,Ge,Sn,Pb│
│  15   │ Nitrogênio       │  5   │ N,P,As,Sb,Bi │
│  16   │ Calcogênios      │  6   │ O,S,Se,Te,Po │
│  17   │ Halogênios       │  7   │ F,Cl,Br,I,At │
│  18   │ Gases Nobres     │ 8(2) │ He,Ne,Ar,Kr  │
└───────┴──────────────────┴──────┴──────────────┘
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Fundamental
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base de toda química)

## Aula 19 - Geografia: Cartografia - Parte 1 - 75min

### O que é Cartografia?

**Cartografia** é a ciência e a arte de representar graficamente a superfície terrestre através de mapas, cartas e plantas.

**Função principal:**
- Representar em 2D (papel/tela) um espaço 3D (Terra)
- Facilitar a localização e orientação
- Representar fenômenos geográficos

**Aplicações:**
- Navegação e orientação
- Planejamento urbano e territorial
- Estudos ambientais
- Análise geopolítica
- GPS e tecnologia

### Evolução da Cartografia

**Cartografia Antiga:**
- Mapas rudimentares (babilônios, egípcios)
- Ptolomeu (século II): mapas com coordenadas
- Idade Média: mapas religiosos (T-O)

**Era dos Descobrimentos (séc. XV-XVI):**
- Grandes navegações exigiram mapas precisos
- Portulanos (mapas náuticos)
- Mercator: projeção cilíndrica (1569)

**Cartografia Moderna:**
- Satélites (décadas 1960-70)
- SIG - Sistemas de Informação Geográfica
- GPS - Sistema de Posicionamento Global
- Sensoriamento remoto
- Cartografia digital

### Orientação e Localização

#### Pontos Cardeais
Formas básicas de orientação:

**Principais:**
- **N (Norte):** direção do Polo Norte
- **S (Sul):** direção do Polo Sul
- **L ou E (Leste):** onde o Sol nasce
- **O ou W (Oeste):** onde o Sol se põe

**Colaterais:**
- **NE (Nordeste):** entre Norte e Leste
- **NO ou NW (Noroeste):** entre Norte e Oeste
- **SE (Sudeste):** entre Sul e Leste
- **SO ou SW (Sudoeste):** entre Sul e Oeste

**Subcolaterais:**
- NNE, ENE, ESE, SSE, SSO, OSO, ONO, NNO

#### Rosa dos Ventos
Figura que representa os pontos cardeais, colaterais e subcolaterais.

```
         N
        NNO NNE
     NO       NE
    ONO   •   ENE
   O            E
    OSO   •   ESE
     SO       SE
        SSO SSE
         S
```

#### Métodos de Orientação

**1. Pelo Sol:**
- Sol nasce no Leste (L/E)
- Sol se põe no Oeste (O/W)
- Ao meio-dia (Hemisfério Sul): Sol ao Norte

**2. Pela Lua:**
- Crescente (C): lado iluminado indica Oeste
- Minguante (D invertido): lado iluminado indica Leste

**3. Pelo Cruzeiro do Sul (Hemisfério Sul):**
- Prolongar 4,5 vezes o eixo maior
- Traçar perpendicular ao horizonte
- Ponto indica Sul

**4. Pela Bússola:**
- Agulha magnética aponta para Norte magnético
- Declinação magnética: diferença entre Norte geográfico e magnético

### Coordenadas Geográficas

Sistema de localização absoluta baseado em linhas imaginárias.

#### Latitude
**Definição:** distância angular de um ponto em relação à Linha do Equador.

**Características:**
- Varia de 0° a 90°
- **0°:** Linha do Equador
- **90° N:** Polo Norte
- **90° S:** Polo Sul
- Paralelos: linhas paralelas ao Equador

**Paralelos Principais:**
- Equador: 0°
- Trópico de Câncer: 23°27' N
- Trópico de Capricórnio: 23°27' S
- Círculo Polar Ártico: 66°33' N
- Círculo Polar Antártico: 66°33' S

**Hemisférios:**
- Norte ou Setentrional (acima do Equador)
- Sul ou Meridional (abaixo do Equador)

#### Longitude
**Definição:** distância angular de um ponto em relação ao Meridiano de Greenwich.

**Características:**
- Varia de 0° a 180°
- **0°:** Meridiano de Greenwich (Londres)
- **180°:** Linha Internacional da Data (Pacífico)
- **0° a 180° W (Oeste):** a oeste de Greenwich
- **0° a 180° E (Leste):** a leste de Greenwich
- Meridianos: linhas que vão de polo a polo

**Hemisférios:**
- Ocidental (a oeste de Greenwich)
- Oriental (a leste de Greenwich)

#### Coordenadas Geográficas
Combinação de latitude e longitude para localização precisa.

**Formato:**
- Latitude: graus, minutos, segundos (N ou S)
- Longitude: graus, minutos, segundos (E ou W)

**Exemplos:**
- Belo Horizonte: 19°55'15" S, 43°56'16" W
- São Paulo: 23°33' S, 46°38' W
- Paris: 48°51' N, 2°21' E

**Conversão:**
- 1° (grau) = 60' (minutos)
- 1' (minuto) = 60" (segundos)

### Fusos Horários

A Terra gira 360° em 24 horas → 15° por hora.

**Fuso Horário:** divisão da Terra em 24 faixas de 15° de longitude.

**Características:**
- Referência: Meridiano de Greenwich (0°)
- A cada 15° de longitude = 1 hora de diferença
- **Leste:** horário adiantado (adiciona horas)
- **Oeste:** horário atrasado (subtrai horas)

**Linha Internacional da Data (180°):**
- Divisor de datas
- Atravessando de Oeste para Leste: avança 1 dia
- Atravessando de Leste para Oeste: retrocede 1 dia

**Brasil:**
- 4 fusos horários (reduzidos para 4 em 2008, depois 3 em 2013)
- Atualmente: 3 fusos (após mudanças)
- Brasília: GMT -3 (UTC -3)

### Escala

**Escala** é a relação entre a distância no mapa e a distância real na superfície.

**Tipos:**

#### Escala Numérica
Expressa por uma fração ou razão.

**Formato:**
```
1:100.000  ou  1/100.000
```

**Significado:**
- 1 cm no mapa = 100.000 cm na realidade
- 1 cm no mapa = 1.000 m = 1 km

**Interpretação:**
- **Denominador grande** (ex: 1:1.000.000) → Escala pequena → Área grande, poucos detalhes
- **Denominador pequeno** (ex: 1:10.000) → Escala grande → Área pequena, muitos detalhes

#### Escala Gráfica
Representação visual com uma barra graduada.

```
|----|----|----|----|
0    1    2    3    4 km
```

### Exercícios Resolvidos

#### Exercício 1
Uma cidade está localizada a 30° de latitude Sul e 45° de longitude Oeste. Em quais hemisférios ela está?

**Solução:**

Latitude Sul → **Hemisfério Sul (Meridional)**
Longitude Oeste → **Hemisfério Ocidental (Oeste)**

**Resposta:** Hemisférios Sul e Ocidental

#### Exercício 2
Calcule a diferença de horário entre duas cidades:
- Cidade A: 15° W
- Cidade B: 60° W

**Solução:**

Diferença de longitude: 60° - 15° = 45°

Diferença de tempo: 45° ÷ 15°/h = 3 horas

Cidade B está mais a Oeste → horário atrasado

**Resposta:** 3 horas de diferença (B está 3h atrasada em relação a A)

#### Exercício 3
Em um mapa de escala 1:500.000, a distância entre duas cidades é de 8 cm. Qual a distância real?

**Solução:**

Escala: 1 cm no mapa = 500.000 cm real

Distância real: 8 × 500.000 = 4.000.000 cm

Convertendo:
4.000.000 cm = 40.000 m = 40 km

**Resposta:** 40 km

#### Exercício 4
Uma cidade está a 120° Leste de Greenwich. Quando em Greenwich são 12h, que horas são na cidade?

**Solução:**

120° Leste → horário adiantado

Diferença: 120° ÷ 15° = 8 horas

Horário na cidade: 12h + 8h = 20h

**Resposta:** 20 horas (8h da noite)

### Dicas para a Prova

1. **Latitude:** 0° (Equador) a 90° (Polos), N ou S
2. **Longitude:** 0° (Greenwich) a 180°, E ou W
3. **Leste = adiantado** (soma horas); **Oeste = atrasado** (subtrai)
4. **Fuso horário:** 15° = 1 hora
5. **Escala grande:** denominador pequeno, mais detalhes
6. **Escala pequena:** denominador grande, menos detalhes
7. **Paralelos principais:** Equador (0°), Trópicos (23°27'), Círculos Polares (66°33')
8. **Conversão escala:** 1 cm × escala = distância real (em cm)

### Conceitos-Chave para Memorizar

**Orientação:**
- Cardeais: N, S, L/E, O/W
- Colaterais: NE, NO, SE, SO
- Sol: nasce L, põe O

**Coordenadas:**
- Latitude: paralelos (horizontal), 0°-90° N/S
- Longitude: meridianos (vertical), 0°-180° E/W
- Equador: 0° latitude
- Greenwich: 0° longitude

**Fusos:**
- 15° = 1 hora
- Leste: + horas
- Oeste: - horas
- 180°: Linha da Data

**Escala:**
- Numérica: 1:X
- Grande escala = pequeno denominador = mais detalhes
- Pequena escala = grande denominador = menos detalhes

### Fórmulas Essenciais

```
Fuso Horário:
Diferença de horas = Δlongitude ÷ 15°

Leste de Greenwich: + horas
Oeste de Greenwich: - horas

Distância Real (escala):
D_real = D_mapa × escala

Exemplo: escala 1:100.000
D_real (cm) = D_mapa (cm) × 100.000

Conversões:
1° = 60'
1' = 60"
100.000 cm = 1.000 m = 1 km
```

### Resumo Visual

```
Coordenadas Geográficas:

        90°N (Polo Norte)
           |
    Círculo Polar Ártico 66°33'N
           |
    Trópico de Câncer 23°27'N
           |
0° ←─── EQUADOR ────→ 0°
           |
    Trópico de Capricórnio 23°27'S
           |
    Círculo Polar Antártico 66°33'S
           |
        90°S (Polo Sul)

    180°W ← Greenwich → 180°E
             (0°)

Escala:
┌────────────────┬──────────┬──────────┐
│ Tipo           │ Área     │ Detalhes │
├────────────────┼──────────┼──────────┤
│ Grande         │ Pequena  │  Muitos  │
│ (ex: 1:10.000) │          │          │
├────────────────┼──────────┼──────────┤
│ Pequena        │ Grande   │  Poucos  │
│ (ex: 1:1.000.000)│        │          │
└────────────────┴──────────┴──────────┘

Fusos Horários:
360° ÷ 24h = 15°/hora

OESTE ← Greenwich → LESTE
 (-h)      (0°)      (+h)
```

---

**Tempo de estudo recomendado:** 75 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - base da Geografia)

## Aula 20 - Ciências Humanas: Antiguidade Oriental - 60min

### As Civilizações do Oriente Antigo

As primeiras grandes civilizações humanas surgiram no **Oriente Próximo** e **Médio**, nas regiões férteis próximas a grandes rios.

**Características comuns:**
- **Modo de Produção Asiático** (ou Despotismo Oriental)
- Poder centralizado (teocracia)
- Economia agrícola baseada em grandes rios
- Obras hidráulicas monumentais
- Sociedades estratificadas
- Politeísmo (exceto hebreus)
- Escrita desenvolvida

**Principais civilizações:**
1. Mesopotâmia
2. Egito
3. Hebreus
4. Fenícios
5. Persas

### Mesopotâmia: "Entre Rios"

**Localização:** entre os rios Tigre e Eufrates (atual Iraque)

**Significado:** Mesopotâmia = "entre rios" (grego)

#### Povos Mesopotâmicos

**1. Sumérios (4000-2000 a.C.)**
- Primeiros habitantes
- **Cidades-Estado:** Ur, Uruk, Lagash
- **Invenções:** escrita cuneiforme, roda, arado
- Zigurates (templos em degraus)

**2. Acádios (2350-2150 a.C.)**
- Liderados por **Sargão I**
- Primeiro império unificado
- Língua semita

**3. Amoritas/Babilônios (1900-1600 a.C.)**
- Capital: **Babilônia**
- **Hamurabi:** "Código de Hamurabi" (Lei de Talião: "olho por olho, dente por dente")
- Desenvolvimento matemático e astronômico

**4. Assírios (1300-612 a.C.)**
- Guerreiros temidos
- Exército poderoso com cavalaria
- Capital: Nínive
- Biblioteca de Assurbanipal

**5. Caldeus/2º Império Babilônico (612-539 a.C.)**
- **Nabucodonosor II**
- Jardins Suspensos da Babilônia (Maravilha do Mundo)
- Torre de Babel
- Cativeiro da Babilônia (judeus)

#### Características da Mesopotâmia

**Política:**
- Teocracia: rei como representante dos deuses
- Cidades-Estado (Sumérios)
- Impérios unificados (posteriores)

**Religião:**
- Politeísmo
- Deuses associados a forças naturais
- Zigurates: templos monumentais
- Adivinhação e astrologia

**Economia:**
- Agricultura (trigo, cevada)
- Comércio (caravanas)
- Artesanato

**Sociedade:**
Hierarquizada:
1. Rei e família real
2. Sacerdotes e nobres
3. Comerciantes e artesãos
4. Camponeses livres
5. Escravos

**Legado:**
- Escrita cuneiforme
- Código de Hamurabi (direito)
- Astronomia e matemática (base 60: minutos, segundos)
- Roda

### Egito: Dádiva do Nilo

**Localização:** nordeste da África, às margens do Rio Nilo

**"O Egito é uma dádiva do Nilo"** (Heródoto)

#### Períodos da História Egípcia

**1. Período Pré-Dinástico (até 3200 a.C.)**
- Formação dos nomos (pequenos reinos)
- Alto Egito (sul) e Baixo Egito (norte)

**2. Período Dinástico Antigo (3200-2300 a.C.)**
- **Menés/Narmer:** unificação do Egito
- Faraós das primeiras dinastias

**3. Antigo Império (2700-2200 a.C.)**
- "Era das Pirâmides"
- **Grandes Pirâmides de Gizé** (Quéops, Quéfren, Mikerinos)
- Poder centralizado do faraó

**4. Médio Império (2100-1750 a.C.)**
- Expansão territorial
- Invasão dos Hicsos (asiáticos com cavalos e carros de guerra)

**5. Novo Império (1580-1080 a.C.)**
- Expulsão dos Hicsos
- Apogeu do Egito
- Faraós importantes: Tutmés III, **Akhenaton** (monoteísmo temporário), **Tutancâmon**, **Ramsés II**
- Templos de Abu Simbel, Luxor, Karnak

**6. Período de Decadência (após 1080 a.C.)**
- Invasões: assírios, persas, macedônios (Alexandre), romanos

#### Características do Egito

**Política:**
- **Teocracia:** Faraó = deus vivo (filho de Rá)
- Poder absoluto e hereditário
- Administração centralizada

**Religião:**
- **Politeísmo**
- Deuses principais: Rá (Sol), Osíris (morte/ressurreição), Ísis, Hórus, Anúbis, Thot
- **Crença na vida após a morte**
- **Mumificação:** preservação do corpo
- **Livro dos Mortos:** guia para o além

**Sociedade:**
Pirâmide social:
1. **Faraó:** deus-rei
2. **Sacerdotes e nobres**
3. **Escribas** (detinham conhecimento da escrita)
4. **Soldados**
5. **Artesãos e comerciantes**
6. **Camponeses (felás)**
7. **Escravos**

**Economia:**
- **Agricultura:** base (trigo, cevada, linho)
- Cheias do Nilo fertilizavam o solo
- Comércio (Mediterrâneo, Núbia)
- Servidão coletiva (camponeses trabalhavam nas obras públicas)

**Cultura:**
- **Escrita hieroglífica** (sagrada)
- **Escrita hierática** (simplificada)
- **Escrita demótica** (popular)
- **Pedra de Roseta:** permitiu decifrar hieróglifos (Champollion)

**Arquitetura:**
- Pirâmides (túmulos dos faraós)
- Templos monumentais
- Esfinges

**Ciências:**
- Matemática (geometria, cálculos)
- Medicina (mumificação → anatomia)
- Astronomia (calendário de 365 dias)

### Hebreus: Povo Monoteísta

**Localização:** Palestina (Canaã)

**Principal característica:** **Monoteísmo** (culto a um único deus: Javé/Yahweh)

#### História dos Hebreus

**Patriarcas (2000-1750 a.C.):**
- **Abraão:** saída de Ur (Mesopotâmia) para Canaã
- **Isaac** e **Jacó (Israel)**
- 12 tribos de Israel

**Êxodo (1750-1250 a.C.):**
- Migração para o Egito (fome)
- Escravização no Egito
- **Moisés:** libertação e êxodo
- **Dez Mandamentos** (Monte Sinai)
- Retorno a Canaã (Terra Prometida)

**Juízes (1250-1010 a.C.):**
- Líderes religiosos e militares
- Luta contra filisteus

**Reino Unificado (1010-926 a.C.):**
- **Saul:** primeiro rei
- **Davi:** conquistou Jerusalém (capital)
- **Salomão:** apogeu, construiu o Templo de Jerusalém

**Cisma (926 a.C.):**
- **Reino de Israel** (norte, 10 tribos) - capital: Samaria
- **Reino de Judá** (sul, 2 tribos) - capital: Jerusalém

**Diásporas:**
- **Cativeiro da Babilônia** (586-539 a.C.): Nabucodonosor destruiu Jerusalém
- **Dominação romana** (70 d.C.): destruição do Segundo Templo, dispersão

**Legado:**
- Monoteísmo (base do judaísmo, cristianismo, islamismo)
- Bíblia (Torá/Antigo Testamento)
- Valores éticos (Dez Mandamentos)

### Fenícios: Navegadores e Comerciantes

**Localização:** costa do Mediterrâneo (atual Líbano)

**Principais cidades:** Biblos, Tiro, Sídon

**Características:**
- **Talassocracia:** poder baseado no mar
- Comércio marítimo (Mediterrâneo)
- Navegadores habilidosos
- Não formaram império unificado (cidades-Estado independentes)

**Atividades:**
- Comércio de púrpura (corante extraído de moluscos)
- Madeira (cedro do Líbano)
- Vidro
- Navegação e fundação de colônias (Cartago)

**Legado:**
- **Alfabeto fonético** (22 letras consonantais)
- Base dos alfabetos grego e latino

### Persas: Grande Império

**Localização:** Planalto Iraniano

**Fundação:** Ciro, o Grande (550 a.C.)

**Extensão:** maior império da Antiguidade (até conquista de Alexandre)

**Características:**
- **Satrapias:** províncias governadas por sátrapas
- **Tolerância religiosa** (permitiam cultos locais)
- Estrada Real (comunicação)
- Correios eficientes

**Religião:**
- **Zoroastrismo (Masdeísmo)**
- Dualismo: Ahura-Mazda (bem) vs. Arimã (mal)
- Livro sagrado: Avesta

**Queda:**
- Alexandre Magno (330 a.C.)

### Exercícios Resolvidos

#### Exercício 1
Qual a principal diferença religiosa entre os hebreus e as outras civilizações orientais?

**Resposta:**
Os hebreus praticavam o **monoteísmo** (crença em um único deus: Javé), enquanto todas as outras civilizações orientais eram **politeístas** (cultuavam vários deuses).

#### Exercício 2
(UFMG adaptada) O Código de Hamurabi, criado na Mesopotâmia, é conhecido por estabelecer qual princípio?

**Resposta:**
A **Lei de Talião**: "olho por olho, dente por dente" - princípio de que a punição deveria ser proporcional ao crime cometido.

#### Exercício 3
Por que o Egito era chamado de "dádiva do Nilo"?

**Resposta:**
Porque a civilização egípcia dependia totalmente do Rio Nilo. As **cheias periódicas** do rio fertilizavam o solo, permitindo a agricultura em meio ao deserto. Sem o Nilo, o Egito seria apenas deserto árido e inabitável.

#### Exercício 4
Qual o principal legado dos fenícios para a humanidade?

**Resposta:**
O **alfabeto fonético** (22 letras consonantais), que serviu de base para os alfabetos grego e latino, utilizados até hoje.

### Dicas para a Prova

1. **Mesopotâmia:** "entre rios" (Tigre e Eufrates), Código de Hamurabi
2. **Egito:** Nilo, pirâmides, faraó = deus, mumificação
3. **Hebreus:** ÚNICOS monoteístas, Moisés, Dez Mandamentos
4. **Fenícios:** comércio marítimo, alfabeto
5. **Persas:** maior império, satrapias, zoroastrismo
6. **Modo de Produção Asiático:** poder centralizado, obras hidráulicas, servidão coletiva
7. **Escrita:** cuneiforme (Mesopotâmia), hieroglífica (Egito), alfabética (fenícios)

### Conceitos-Chave para Memorizar

**Civilizações e Características:**

**Mesopotâmia:**
- Rios: Tigre e Eufrates
- Escrita cuneiforme
- Código de Hamurabi
- Zigurates

**Egito:**
- Rio: Nilo
- Faraó = deus
- Pirâmides e mumificação
- Hieróglifos

**Hebreus:**
- Monoteísmo (Javé)
- Moisés e Êxodo
- Dez Mandamentos
- Diáspora

**Fenícios:**
- Comércio marítimo
- Alfabeto fonético
- Púrpura

**Persas:**
- Grande Império
- Satrapias
- Zoroastrismo

### Resumo Visual

```
Civilizações Orientais:

MESOPOTÂMIA          EGITO
  Tigre/Eufrates       Nilo
  Cuneiforme        Hieróglifos
  Hamurabi            Faraó
  Politeísmo        Politeísmo
  
HEBREUS             FENÍCIOS
  Monoteísmo        Comércio
  Javé              Alfabeto
  Moisés            Navegação
  
PERSAS
  Grande Império
  Satrapias
  Zoroastrismo

Linha do Tempo:
4000aC  Sumérios
3200aC  Unificação Egito
2000aC  Abraão (hebreus)
1750aC  Hamurabi
1250aC  Êxodo (Moisés)
1000aC  Davi e Salomão
550aC   Império Persa (Ciro)
```

### Tabela Comparativa

```
┌─────────────┬────────────┬────────────┬──────────┐
│ Civilização │    Rio     │  Escrita   │ Religião │
├─────────────┼────────────┼────────────┼──────────┤
│Mesopotâmia  │Tigre/Eufr. │ Cuneiforme │  Poli    │
│Egito        │   Nilo     │ Hieróglifos│  Poli    │
│Hebreus      │  Jordão    │ Alfabética │  Mono    │
│Fenícios     │Mediterrâneo│ Alfabética │  Poli    │
│Persas       │  Vários    │ Cuneiforme │Zoroastr. │
└─────────────┴────────────┴────────────┴──────────┘
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - base da História Antiga)

# 11/22 - Dia 5

## Aula 21 - Matemática: Função Afim - Parte 2 - 120min

### Revisão: Função Afim

Na Aula 16, estudamos os conceitos básicos da função afim:
- f(x) = ax + b (a ≠ 0)
- Coeficientes a (angular) e b (linear)
- Gráfico: reta
- Zero, crescimento/decrescimento, estudo do sinal

**Nesta aula, aprofundaremos:**
- Posição relativa entre retas
- Sistemas de equações via funções
- Aplicações e problemas contextualizados
- Função modular
- Inequações mais complexas

### Posição Relativa entre Duas Retas

Dadas duas funções afins f(x) = a₁x + b₁ e g(x) = a₂x + b₂:

#### 1. Retas Concorrentes
Retas que se cruzam em um único ponto.

**Condição:**
```
a₁ ≠ a₂  (coeficientes angulares diferentes)
```

**Ponto de interseção:**
Resolver f(x) = g(x)

**Exemplo:**
f(x) = 2x + 1
g(x) = -x + 4

2x + 1 = -x + 4
3x = 3
x = 1 → y = 3

Ponto de interseção: (1, 3)

#### 2. Retas Paralelas
Retas que não se cruzam (mesma inclinação, posições diferentes).

**Condição:**
```
a₁ = a₂  e  b₁ ≠ b₂
```

**Exemplo:**
f(x) = 3x + 2
g(x) = 3x - 5

Ambas têm a = 3, mas b diferentes → paralelas

#### 3. Retas Coincidentes
Mesma reta (todos os pontos em comum).

**Condição:**
```
a₁ = a₂  e  b₁ = b₂
```

**Exemplo:**
f(x) = 2x + 3
g(x) = 2x + 3

São a mesma função → retas coincidentes

#### 4. Retas Perpendiculares
Retas que se cruzam formando ângulo de 90°.

**Condição:**
```
a₁ × a₂ = -1
```

Ou: a₂ = -1/a₁ (coeficientes são inversos opostos)

**Exemplo:**
f(x) = 2x + 1
g(x) = -½x + 3

a₁ = 2, a₂ = -½
2 × (-½) = -1 ✓

São perpendiculares.

### Sistemas de Equações do 1º Grau

Resolver sistemas é encontrar o ponto de interseção entre duas retas.

**Sistema:**
```
{ ax + by = c
{ dx + ey = f
```

**Métodos:**

#### Método da Substituição
1. Isolar uma variável em uma equação
2. Substituir na outra equação
3. Resolver e voltar para encontrar a segunda variável

#### Método da Adição
1. Multiplicar equações para anular uma variável
2. Somar as equações
3. Resolver para a variável restante
4. Substituir para encontrar a outra

**Exemplo:**
```
{ 2x + y = 7
{ x - y = 2
```

**Por adição:**
Somando as equações:
(2x + y) + (x - y) = 7 + 2
3x = 9
x = 3

Substituindo em x - y = 2:
3 - y = 2
y = 1

**Solução:** (3, 1)

**Interpretação geométrica:**
- **Uma solução:** retas concorrentes
- **Infinitas soluções:** retas coincidentes
- **Nenhuma solução:** retas paralelas

### Função Definida por Mais de uma Sentença

Funções que têm expressões diferentes em intervalos diferentes.

**Formato:**
```
       ⎧ expressão 1, se condição 1
f(x) = ⎨ expressão 2, se condição 2
       ⎩ expressão 3, se condição 3
```

**Exemplo 1:**
```
       ⎧ 2x + 1,  se x ≤ 0
f(x) = ⎨
       ⎩ -x + 3,  se x > 0
```

Para calcular f(-2): usa a primeira sentença (x ≤ 0)
f(-2) = 2(-2) + 1 = -4 + 1 = -3

Para calcular f(3): usa a segunda sentença (x > 0)
f(3) = -3 + 3 = 0

**Gráfico:** combina duas semi-retas

**Exemplo 2 - Tarifa progressiva:**
```
        ⎧ 5x,       se 0 ≤ x ≤ 100
Custo = ⎨
        ⎩ 500 + 3(x-100),  se x > 100
```

Até 100 unidades: R$ 5 por unidade
Acima de 100: R$ 500 fixo + R$ 3 por unidade excedente

### Função Modular

**Módulo (ou valor absoluto)** de um número é sua distância até o zero.

**Notação:** |x|

**Definição:**
```
       ⎧  x,   se x ≥ 0
|x| =  ⎨
       ⎩ -x,   se x < 0
```

**Exemplos:**
- |5| = 5
- |-3| = 3
- |0| = 0

**Propriedades:**
1. |x| ≥ 0 (sempre não-negativo)
2. |x| = |-x|
3. |x · y| = |x| · |y|
4. |x/y| = |x|/|y| (y ≠ 0)
5. |x + y| ≤ |x| + |y| (desigualdade triangular)

**Função Modular:**
f(x) = |x|

**Gráfico:** forma de "V"
- Para x ≥ 0: f(x) = x (reta crescente)
- Para x < 0: f(x) = -x (reta decrescente)

```
    |
  3 |    /
  2 |   /|
  1 |  / |
    | /  |
----+----+----
 -2 |    2
```

**Equações com módulo:**

**Exemplo:** |x - 2| = 5

**Método:** módulo = distância
x - 2 = 5  ou  x - 2 = -5
x = 7     ou  x = -3

**Soluções:** x = 7 ou x = -3

**Inequações com módulo:**

**Exemplo:** |x| < 3

Significa: distância de x até 0 é menor que 3

**Solução:** -3 < x < 3

**Regra geral:**
- |x| < a  →  -a < x < a
- |x| > a  →  x < -a  ou  x > a

### Aplicações Práticas

#### Problema 1: Táxi
Um táxi cobra R$ 5,00 de bandeirada + R$ 2,50 por km rodado.

**Função:** C(x) = 5 + 2,5x

**a) Quanto custa uma corrida de 12 km?**
C(12) = 5 + 2,5(12) = 5 + 30 = R$ 35,00

**b) Quantos km podem ser rodados com R$ 30?**
30 = 5 + 2,5x
25 = 2,5x
x = 10 km

#### Problema 2: Planos de Celular
- **Plano A:** R$ 50 fixos + R$ 0,50 por minuto
- **Plano B:** R$ 80 fixos + R$ 0,20 por minuto

**Funções:**
A(x) = 50 + 0,5x
B(x) = 80 + 0,2x

**Quando os planos custam o mesmo?**
50 + 0,5x = 80 + 0,2x
0,3x = 30
x = 100 minutos

**Interpretação:**
- Menos de 100 min: Plano A é melhor
- Mais de 100 min: Plano B é melhor
- Exatamente 100 min: custam o mesmo

#### Problema 3: Conversão Temperatura
Converter Celsius (C) para Fahrenheit (F):

F = (9/5)C + 32

**a) 25°C em Fahrenheit:**
F = (9/5)(25) + 32 = 45 + 32 = 77°F

**b) A que temperatura as escalas têm o mesmo valor?**
C = F
C = (9/5)C + 32
C - (9/5)C = 32
(-4/5)C = 32
C = -40°C = -40°F

### Exercícios Resolvidos

#### Exercício 1
Determine a posição relativa entre:
f(x) = 3x - 2  e  g(x) = -x + 6

**Solução:**
a₁ = 3, a₂ = -1
a₁ ≠ a₂ → **retas concorrentes**

Ponto de interseção:
3x - 2 = -x + 6
4x = 8
x = 2 → y = 3(2) - 2 = 4

**Resposta:** Concorrentes, intersectam em (2, 4)

#### Exercício 2
Resolva o sistema:
```
{ 3x + 2y = 12
{ x - y = 1
```

**Solução (por substituição):**
Da 2ª equação: x = y + 1

Substituindo na 1ª:
3(y + 1) + 2y = 12
3y + 3 + 2y = 12
5y = 9
y = 9/5

x = 9/5 + 1 = 14/5

**Resposta:** x = 14/5, y = 9/5 ou (2,8; 1,8)

#### Exercício 3
Calcule f(-3) e f(2) para:
```
       ⎧ x + 5,   se x < 0
f(x) = ⎨
       ⎩ 2x - 1,  se x ≥ 0
```

**Solução:**

f(-3): usa x + 5 (pois -3 < 0)
f(-3) = -3 + 5 = 2

f(2): usa 2x - 1 (pois 2 ≥ 0)
f(2) = 2(2) - 1 = 3

**Respostas:** f(-3) = 2; f(2) = 3

#### Exercício 4
Resolva: |2x - 4| = 6

**Solução:**
2x - 4 = 6  ou  2x - 4 = -6
2x = 10    ou  2x = -2
x = 5      ou  x = -1

**Resposta:** x = 5 ou x = -1

#### Exercício 5
Resolva a inequação: |x + 1| < 4

**Solução:**
-4 < x + 1 < 4
-4 - 1 < x < 4 - 1
-5 < x < 3

**Resposta:** -5 < x < 3  ou  x ∈ (-5, 3)

### Dicas para a Prova

1. **Posição de retas:** compare os coeficientes a
2. **Perpendiculares:** a₁ × a₂ = -1
3. **Sistema:** ponto de interseção entre retas
4. **Função por partes:** veja qual condição o x satisfaz
5. **Módulo |x| = a:** duas soluções (x = a ou x = -a)
6. **|x| < a:** -a < x < a (intervalo)
7. **|x| > a:** x < -a ou x > a (união de intervalos)
8. **Problemas:** monte a função conforme o enunciado

### Conceitos-Chave para Memorizar

**Posição Relativa:**
- Concorrentes: a₁ ≠ a₂
- Paralelas: a₁ = a₂, b₁ ≠ b₂
- Coincidentes: a₁ = a₂, b₁ = b₂
- Perpendiculares: a₁ × a₂ = -1

**Módulo:**
- |x| = distância até zero
- Sempre ≥ 0
- |x| = { x se x≥0; -x se x<0 }

**Funções por partes:**
- Verificar a condição de x
- Usar a expressão correspondente

### Fórmulas Essenciais

```
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
       ⎩ -x,   se x < 0

Equação: |x| = a → x = a ou x = -a

Inequações:
|x| < a  →  -a < x < a
|x| > a  →  x < -a ou x > a

Função Modular:
f(x) = |x|
Gráfico: forma de V
```

### Resumo Visual

```
Posição de Retas:

Concorrentes:     Paralelas:    Perpendiculares:
    \  /            |  |            |
     \/             |  |           ―┼―
     /\             |  |            |
    /  \            |  |

(a₁≠a₂)      (a₁=a₂,b₁≠b₂)   (a₁×a₂=-1)

Função Modular f(x) = |x|:
      |
    2 |  /\
    1 | /  \
      |/    \
   ───┼──────
   -2 |  1  2

Inequações com Módulo:
|x| < 3:  ←─────●═══●─────→
               -3   3
               (intervalo)

|x| > 3:  ●═══════←   →═══════●
          -3                  3
          (união)
```

---

**Tempo de estudo recomendado:** 120 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - aprofundamento de função afim)

## Aula 22 - Física: Leis de Newton - 90min

### Dinâmica: O Estudo das Forças

**Cinemática** (estudada anteriormente): descreve o movimento sem se preocupar com suas causas.

**Dinâmica**: estuda as causas do movimento (as forças).

**Isaac Newton (1643-1727):**
- Físico e matemático inglês
- Publicou "Principia Mathematica" (1687)
- Estabeleceu as três leis fundamentais da Dinâmica

### Conceito de Força

**Força** é uma interação que pode:
- Colocar um corpo em movimento
- Parar um corpo em movimento
- Mudar a direção do movimento
- Deformar um corpo

**Características da Força (grandeza vetorial):**
- **Intensidade (módulo):** quão forte é
- **Direção:** linha de ação (horizontal, vertical, diagonal)
- **Sentido:** para onde aponta (direita/esquerda, cima/baixo)

**Unidade SI:** Newton (N)

**1 N** = força necessária para acelerar 1 kg a 1 m/s²

**Representação:**
```
    →
    F
    
Vetor força com:
- Comprimento: intensidade
- Reta: direção
- Seta: sentido
```

### 1ª Lei de Newton - Lei da Inércia

> "Um corpo em repouso tende a permanecer em repouso, e um corpo em movimento tende a permanecer em movimento retilíneo uniforme, a menos que uma força resultante atue sobre ele."

**Inércia:** tendência de um corpo em manter seu estado de movimento.

**Consequências:**
- Corpo parado permanece parado (sem força resultante)
- Corpo em movimento permanece em MRU (sem força resultante)
- Massa é medida de inércia (quanto maior a massa, maior a inércia)

**Exemplos cotidianos:**
1. **Freada brusca:** passageiros são "jogados" para frente (inércia mantém movimento)
2. **Aceleração do carro:** passageiros são "pressionados" contra o banco (inércia resiste à mudança)
3. **Toalha de mesa puxada:** objetos tendem a ficar no lugar (inércia)

**Referenciais Inerciais:**
- Sistemas onde a 1ª Lei é válida
- Referenciais sem aceleração
- Terra: aproximadamente inercial (pequenas acelerações desprezadas)

**Força Resultante Nula:**
```
F_R = 0  →  v = constante (MRU ou repouso)
```

### 2ª Lei de Newton - Princípio Fundamental da Dinâmica

> "A força resultante aplicada a um corpo é igual ao produto de sua massa pela aceleração adquirida."

**Fórmula:**
```
F_R = m × a
```

Onde:
- F_R: força resultante (N)
- m: massa (kg)
- a: aceleração (m/s²)

**Interpretação:**
- Força e aceleração têm mesma direção e sentido
- Quanto maior a força, maior a aceleração
- Quanto maior a massa, menor a aceleração (para mesma força)

**Unidade de Força:**
```
1 N = 1 kg × 1 m/s²
```

**Exemplos:**

1. **Empurrando um carrinho:**
   - m = 10 kg, a = 2 m/s²
   - F = 10 × 2 = 20 N

2. **Carro acelerando:**
   - m = 1000 kg, F = 3000 N
   - a = F/m = 3000/1000 = 3 m/s²

**Relação Massa-Peso:**
- **Massa (m):** quantidade de matéria (kg), não varia
- **Peso (P):** força gravitacional (N), varia com g

```
P = m × g
```

Na Terra: g ≈ 10 m/s²
Pessoa de 60 kg: P = 60 × 10 = 600 N

### 3ª Lei de Newton - Lei da Ação e Reação

> "Para toda ação existe uma reação de mesma intensidade, mesma direção e sentido contrário."

**Características:**
- Ação e reação atuam em **corpos diferentes**
- São simultâneas (ocorrem ao mesmo tempo)
- Mesma intensidade, mesma direção, sentidos opostos

**Exemplos:**

1. **Livro sobre mesa:**
   - Ação: peso do livro sobre a mesa (↓)
   - Reação: força da mesa sobre o livro (↑)
   - Corpos diferentes: livro e mesa

2. **Empurrando parede:**
   - Ação: você empurra a parede (→)
   - Reação: parede empurra você (←)

3. **Foguete:**
   - Ação: gás expelido para baixo
   - Reação: foguete impulsionado para cima

4. **Remo no barco:**
   - Ação: remo empurra água para trás
   - Reação: água empurra barco para frente

**IMPORTANTE:**
Ação e reação NÃO se anulam porque atuam em corpos diferentes!

### Principais Tipos de Força

#### 1. Força Peso (P)
Força gravitacional que atrai corpos para o centro da Terra.

```
P = m × g
```

- **Direção:** vertical
- **Sentido:** para baixo (centro da Terra)
- **Intensidade:** P = mg

#### 2. Força Normal (N)
Força de contato perpendicular à superfície.

- **Direção:** perpendicular à superfície
- **Sentido:** "empurra" o corpo para fora da superfície
- **Intensidade:** varia conforme situação

**Casos:**

**a) Corpo sobre superfície horizontal (equilíbrio):**
```
N = P = mg
```

**b) Corpo em plano inclinado:**
```
N = mg × cos(θ)
```

**c) Corpo empurrado contra superfície vertical:**
```
N = F (força aplicada)
```

#### 3. Força de Tração (T)
Força transmitida por fios, cordas, cabos.

- **Direção:** ao longo do fio
- **Sentido:** puxa o corpo
- **Fio ideal:** inextensível e de massa desprezível

#### 4. Força de Atrito (F_at)
Força que se opõe ao movimento relativo entre superfícies em contato.

**Tipos:**

**a) Atrito Estático (F_at,e):**
- Corpo em repouso
- Impede início do movimento
- Varia de 0 até máximo: F_at,e ≤ μ_e × N

**b) Atrito Cinético (F_at,c):**
- Corpo em movimento
- Sempre: F_at,c = μ_c × N

**Fórmulas:**
```
F_at,e (máximo) = μ_e × N
F_at,c = μ_c × N
```

Onde:
- μ_e: coeficiente de atrito estático
- μ_c: coeficiente de atrito cinético
- N: força normal
- Geralmente: μ_e > μ_c

**Características do atrito:**
- Sempre oposto ao movimento (ou tendência)
- Depende da natureza das superfícies (μ)
- Depende da força normal (N)
- NÃO depende da área de contato
- NÃO depende da velocidade (atrito cinético)

### Aplicações das Leis de Newton

#### Diagrama de Corpo Livre (DCL)
Representação de todas as forças que atuam em um corpo.

**Passos:**
1. Isolar o corpo
2. Representar todas as forças
3. Escolher eixos de referência
4. Aplicar F_R = ma em cada eixo

**Exemplo - Bloco sobre mesa:**
```
      ↑ N
      |
    [bloco]
      |
      ↓ P
```

#### Problemas Típicos

**1. Corpo em movimento sobre superfície horizontal:**
```
F_R = F_aplicada - F_atrito
ma = F - μN
ma = F - μmg
a = (F - μmg)/m
```

**2. Plano inclinado sem atrito:**
```
a = g × sen(θ)
```

**3. Dois corpos ligados por fio:**
- Tração é igual em ambos (fio ideal)
- Aceleração é igual em ambos (fio inextensível)
- Montar equações para cada corpo

### Exercícios Resolvidos

#### Exercício 1
Um corpo de massa 5 kg está sob ação de uma força resultante de 20 N. Calcule sua aceleração.

**Solução:**
F_R = ma
20 = 5a
a = 4 m/s²

**Resposta:** 4 m/s²

#### Exercício 2
Uma pessoa de 70 kg está em um elevador. Calcule a força normal nos casos:
a) Elevador em repouso ou MRU
b) Elevador subindo com a = 2 m/s²
c) Elevador descendo com a = 2 m/s²

(Considere g = 10 m/s²)

**Solução:**

a) Equilíbrio (a = 0):
N - P = 0
N = P = mg = 70 × 10 = 700 N

b) Subindo acelerado (a = 2 m/s² ↑):
F_R = ma (para cima)
N - P = ma
N = P + ma = 700 + 70(2) = 700 + 140 = 840 N

c) Descendo acelerado (a = 2 m/s² ↓):
F_R = ma (para baixo)
P - N = ma
N = P - ma = 700 - 140 = 560 N

**Respostas:** a) 700 N; b) 840 N; c) 560 N

#### Exercício 3
Um bloco de 10 kg está em repouso sobre uma superfície (μ_e = 0,4, μ_c = 0,3). Aplica-se uma força horizontal de 30 N. O bloco se move? Se sim, qual a aceleração? (g = 10 m/s²)

**Solução:**

Força normal: N = P = mg = 10 × 10 = 100 N

Atrito estático máximo:
F_at,e (máx) = μ_e × N = 0,4 × 100 = 40 N

Força aplicada (30 N) < Atrito máximo (40 N)

**Bloco NÃO se move** (atrito segura)

**Resposta:** Não se move; a = 0

#### Exercício 4
(Continuação do anterior) Se a força aplicada for 50 N, qual a aceleração?

**Solução:**

F_aplicada (50 N) > F_at,e (máx) (40 N) → bloco se move

Com movimento, usa atrito cinético:
F_at,c = μ_c × N = 0,3 × 100 = 30 N

F_R = F_aplicada - F_at,c
ma = 50 - 30
10a = 20
a = 2 m/s²

**Resposta:** a = 2 m/s²

#### Exercício 5
(UFMG) Um livro está sobre uma mesa. Identifique os pares ação-reação.

**Solução:**

**Par 1 (peso do livro):**
- Ação: Terra atrai livro (peso do livro ↓)
- Reação: Livro atrai Terra (↑)

**Par 2 (contato livro-mesa):**
- Ação: Livro pressiona mesa (↓)
- Reação: Mesa pressiona livro (Normal ↑)

**IMPORTANTE:** Peso e Normal do livro NÃO são par ação-reação (atuam no mesmo corpo).

### Dicas para a Prova

1. **1ª Lei:** F_R = 0 → v = constante (MRU ou repouso)
2. **2ª Lei:** F_R = ma (sempre!)
3. **3ª Lei:** par ação-reação em corpos diferentes
4. **DCL:** desenhar TODAS as forças no corpo
5. **Peso:** sempre mg (para baixo)
6. **Normal:** perpendicular à superfície
7. **Atrito:** oposto ao movimento; F_at = μN
8. **Ação-reação:** mesma intensidade, opostas, corpos diferentes

### Conceitos-Chave para Memorizar

**Leis de Newton:**
1. **Inércia:** corpo mantém estado (F_R = 0 → v = cte)
2. **F = ma:** força causa aceleração
3. **Ação-Reação:** forças em pares, corpos diferentes

**Forças:**
- Peso: P = mg (↓)
- Normal: perpendicular à superfície
- Tração: ao longo do fio
- Atrito: F_at = μN (oposto ao movimento)

**Massa vs Peso:**
- Massa: quantidade de matéria (kg)
- Peso: força gravitacional (N), P = mg

### Fórmulas Essenciais

```
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
```

### Resumo Visual

```
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
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base de toda Dinâmica)

## Aula 23 - Química: Propriedades Periódicas - 90min

### Revisão: Tabela Periódica

Na Aula 18, estudamos a organização da Tabela Periódica:
- Períodos (linhas): indicam número de camadas
- Famílias/Grupos (colunas): indicam elétrons de valência
- Classificação: metais, não-metais, semimetais, gases nobres

**Nesta aula:** propriedades que variam periodicamente na tabela.

### O que são Propriedades Periódicas?

**Propriedades Periódicas** são características dos elementos que variam de forma regular conforme a posição na Tabela Periódica.

**Variam conforme:**
- Número atômico (Z)
- Período (número de camadas)
- Família (elétrons de valência)

**Principais propriedades periódicas:**
1. Raio Atômico
2. Energia de Ionização
3. Afinidade Eletrônica
4. Eletronegatividade
5. Eletropositividade (Caráter Metálico)

### 1. Raio Atômico

**Definição:** medida do tamanho do átomo (distância do núcleo até a eletrosfera mais externa).

**Unidade:** picômetro (pm) ou ångström (Å)
- 1 Å = 10⁻¹⁰ m = 100 pm

#### Variação na Tabela Periódica

**Na mesma família (coluna) - de cima para baixo:**
```
AUMENTA ↓
```

**Por quê?**
- Mais camadas eletrônicas
- Elétrons mais distantes do núcleo

**Exemplo:** Família 1 (Alcalinos)
- Li (2 camadas) < Na (3 camadas) < K (4 camadas) < Rb < Cs

**No mesmo período (linha) - da esquerda para direita:**
```
DIMINUI →
```

**Por quê?**
- Mesmo número de camadas
- Mais prótons no núcleo → maior atração
- Elétrons são puxados mais para perto

**Exemplo:** Período 3
- Na > Mg > Al > Si > P > S > Cl > Ar

#### Resumo Visual - Raio Atômico

```
Tabela Periódica:

DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │ │
AUMENTA│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIOR raio: canto inferior esquerdo (Fr, Cs)
MENOR raio: canto superior direito (He, F, Ne)
```

#### Raio Iônico

**Cátion (íon positivo):** perdeu elétrons
- **Menor** que o átomo neutro
- Menos repulsão eletrônica

**Exemplo:** Na (raio maior) → Na⁺ (raio menor)

**Ânion (íon negativo):** ganhou elétrons
- **Maior** que o átomo neutro
- Mais repulsão eletrônica

**Exemplo:** Cl (raio menor) → Cl⁻ (raio maior)

**Regra geral:**
```
Cátion < Átomo neutro < Ânion
```

### 2. Energia de Ionização (EI ou PI)

**Definição:** energia necessária para **remover** um elétron de um átomo gasoso no estado fundamental.

```
X(g) + energia → X⁺(g) + e⁻
```

**Unidade:** eV (elétron-volt) ou kJ/mol

**Ionizações sucessivas:**
- **1ª EI:** remover o 1º elétron
- **2ª EI:** remover o 2º elétron (SEMPRE maior que a 1ª)
- **3ª EI:** remover o 3º elétron

**Cada ionização sucessiva requer MAIS energia.**

#### Variação na Tabela Periódica

**Na mesma família (coluna) - de cima para baixo:**
```
DIMINUI ↓
```

**Por quê?**
- Raio maior → elétrons mais distantes
- Mais fácil remover (menos atração nuclear)

**No mesmo período (linha) - da esquerda para direita:**
```
AUMENTA →
```

**Por quê?**
- Raio menor → elétrons mais próximos do núcleo
- Mais difícil remover (maior atração nuclear)

#### Resumo Visual - Energia de Ionização

```
Tabela Periódica:

AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │ │
DIMINUI│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIOR EI: canto superior direito (He, Ne, F)
MENOR EI: canto inferior esquerdo (Fr, Cs)
```

**Exceções importantes:**
- **Gases nobres:** EI muito alta (estáveis)
- **Metais alcalinos:** EI muito baixa (perdem elétron facilmente)

### 3. Afinidade Eletrônica (AE)

**Definição:** energia **liberada** quando um átomo gasoso **ganha** um elétron.

```
X(g) + e⁻ → X⁻(g) + energia
```

**Unidade:** eV ou kJ/mol

**Valores:**
- Geralmente negativos (processo exotérmico - libera energia)
- Quanto mais negativo, maior a afinidade (mais favorável)

#### Variação na Tabela Periódica

**Segue padrão semelhante à Energia de Ionização:**

**Na família:** DIMINUI de cima para baixo ↓
**No período:** AUMENTA da esquerda para direita →

**Maior AE (mais negativa):** Halogênios (Grupo 17)
- Cl, F, Br (ganham elétron facilmente)

**Menor AE:** Metais alcalinos e gases nobres
- Gases nobres: estáveis, não querem elétrons

#### Resumo Visual - Afinidade Eletrônica

```
AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │ Hal│X│← gases nobres (AE≈0)
DIMINUI│ │ │ógn.│ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIOR AE: Halogênios (Cl, F, Br)
MENOR AE: Gases nobres, metais alcalinos
```

### 4. Eletronegatividade (EN)

**Definição:** tendência de um átomo em **atrair elétrons** em uma ligação química.

**Escala de Pauling:**
- **F (flúor):** 4,0 (mais eletronegativo)
- **Fr (frâncio):** 0,7 (menos eletronegativo)
- **Gases nobres:** não têm valor (não fazem ligações)

#### Variação na Tabela Periódica

**Na família:** DIMINUI de cima para baixo ↓
**No período:** AUMENTA da esquerda para direita →

**Padrão similar à Energia de Ionização e Afinidade Eletrônica.**

#### Resumo Visual - Eletronegatividade

```
AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │F│← 4,0 (máximo)
DIMINUI│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
Fr ────┴─┴─┴────┴─┘
0,7

MAIS eletronegativo: F > O > N > Cl
MENOS eletronegativo: Fr, Cs (metais alcalinos)
```

**Sequência decorar:**
```
F > O > N > Cl > Br > I > S > C > H
4,0  3,5  3,0  3,0
```

**Aplicação:**
- **Diferença de EN:** determina tipo de ligação
  - ΔEN = 0: ligação covalente apolar
  - 0 < ΔEN < 1,7: ligação covalente polar
  - ΔEN ≥ 1,7: ligação iônica

### 5. Eletropositividade ou Caráter Metálico

**Definição:** tendência de um átomo em **perder elétrons** (formar cátions).

**Também chamado:**
- Caráter metálico
- Reatividade metálica

#### Variação na Tabela Periódica

**OPOSTO da Eletronegatividade:**

**Na família:** AUMENTA de cima para baixo ↓
**No período:** DIMINUI da esquerda para direita ←

#### Resumo Visual - Eletropositividade

```
DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │Fr Cs    │ │
AUMENTA│ │ │    │ │
     ↓ │ │ │    │ │
       │ │ │    │ │
       └─┴─┴────┴─┘

MAIS eletropositivo: Fr, Cs (metais alcalinos)
MENOS eletropositivo: F, O, N (não-metais)
```

**Relação:**
- **Metais:** alta eletropositividade (perdem elétrons)
- **Não-metais:** alta eletronegatividade (ganham elétrons)

### Comparação das Propriedades Periódicas

| Propriedade | Mesmo Período (→) | Mesma Família (↓) | Máximo | Mínimo |
|-------------|-------------------|-------------------|--------|--------|
| **Raio Atômico** | Diminui | Aumenta | Fr, Cs | He, F |
| **Energia de Ionização** | Aumenta | Diminui | He, Ne | Fr, Cs |
| **Afinidade Eletrônica** | Aumenta | Diminui | Cl, F | Gases nobres |
| **Eletronegatividade** | Aumenta | Diminui | F (4,0) | Fr (0,7) |
| **Eletropositividade** | Diminui | Aumenta | Fr, Cs | F, O |

### Exercícios Resolvidos

#### Exercício 1
Compare o raio atômico:
a) Na e K
b) Na e Cl

**Solução:**

a) Na (Período 3) e K (Período 4) - mesma família (Grupo 1)
Na família, raio aumenta para baixo.
**K > Na**

b) Na e Cl - mesmo período (Período 3)
No período, raio diminui para a direita.
**Na > Cl**

**Respostas:** a) K > Na; b) Na > Cl

#### Exercício 2
Ordene em ordem crescente de energia de ionização: F, Cl, Br

**Solução:**

Mesma família (Grupo 17 - Halogênios)
Na família, EI diminui para baixo.

F (Período 2) > Cl (Período 3) > Br (Período 4)

**Resposta:** Br < Cl < F

#### Exercício 3
Qual elemento é mais eletronegativo: C, N, O ou F?

**Solução:**

Todos no Período 2.
No período, EN aumenta para a direita.

**F > O > N > C**

**Resposta:** F (flúor) - 4,0 na escala de Pauling

#### Exercício 4
(UFMG) Compare o tamanho: Na, Na⁺, Cl, Cl⁻

**Solução:**

Na → Na⁺ (perdeu elétron): cátion é menor
Cl → Cl⁻ (ganhou elétron): ânion é maior

Na e Cl estão no mesmo período (3): Na > Cl

Ordem: **Na⁺ < Na < Cl < Cl⁻**

**Resposta:** Na⁺ < Na < Cl < Cl⁻

#### Exercício 5
Explique por que a 2ª energia de ionização é sempre maior que a 1ª.

**Solução:**

Após remover o 1º elétron:
- Átomo vira cátion (+)
- Menos elétrons → menos repulsão
- Raio diminui
- Elétrons mais atraídos pelo núcleo

**Resultado:** 2ª ionização requer MAIS energia (elétron está mais fortemente ligado).

**Resposta:** Porque no cátion os elétrons estão mais próximos e mais fortemente atraídos pelo núcleo.

### Dicas para a Prova

1. **Raio atômico:** ↓ na família, ← no período (oposto das demais)
2. **EI, AE, EN:** mesmo padrão (↑ direita, ↓ baixo)
3. **Eletropositividade:** oposto de eletronegatividade
4. **F:** mais eletronegativo (4,0)
5. **Cátion < átomo neutro < ânion** (tamanho)
6. **2ª EI > 1ª EI** (sempre!)
7. **Halogênios:** alta afinidade eletrônica
8. **Gases nobres:** alta EI, baixa AE (estáveis)

### Conceitos-Chave para Memorizar

**Padrões Gerais:**

**Grupo (↓):**
- Raio: AUMENTA
- EI, AE, EN: DIMINUI
- Eletropositividade: AUMENTA

**Período (→):**
- Raio: DIMINUI
- EI, AE, EN: AUMENTA
- Eletropositividade: DIMINUI

**Extremos:**
- **F:** maior EN (4,0), menor raio (entre os reativos)
- **Fr/Cs:** maior raio, menor EN, maior eletropositividade
- **He:** menor raio absoluto, maior EI
- **Halogênios:** maior AE

### Resumo Visual Completo

```
TABELA PERIÓDICA - TENDÊNCIAS

         RAIO ATÔMICO
         DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │ │
AUMENTA│ │ │    │ │
     ↓ │ │ │    │ │
       └─┴─┴────┴─┘

     EI, AE, EN
      AUMENTA →
       ┌─┬─┬────┬─┐
     ↓ │ │ │    │F│ MAX
DIMINUI│ │ │    │ │
     ↓ │ │ │    │ │
       └─┴─┴────┴─┘
Fr/Cs MIN

 ELETROPOSITIVIDADE
    DIMINUI →
       ┌─┬─┬────┬─┐
     ↓ │Fr Cs    │ │ MAX
AUMENTA│ │ │    │ │
     ↓ │ │ │    │F│ MIN
       └─┴─┴────┴─┘
```

### Tabela Resumo

```
┌───────────────────┬───────────┬───────────┬────────┐
│    Propriedade    │  Período  │  Família  │  Max   │
│                   │    (→)    │    (↓)    │        │
├───────────────────┼───────────┼───────────┼────────┤
│ Raio Atômico      │  Diminui  │  Aumenta  │ Fr, Cs │
│ Energia Ionização │  Aumenta  │  Diminui  │  He    │
│ Afinidade Eletr.  │  Aumenta  │  Diminui  │  Cl, F │
│ Eletronegatividade│  Aumenta  │  Diminui  │  F(4,0)│
│ Eletropositividade│  Diminui  │  Aumenta  │ Fr, Cs │
└───────────────────┴───────────┴───────────┴────────┘

Tamanho de Íons:
Cátion⁺ < Átomo neutro < Ânion⁻

Eletronegatividade (decorar):
F > O > N > Cl > Br > I > S > C > H
4,0  3,5  3,0  3,0
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - muito cobrado!)

## Aula 24 - Geografia: Cartografia - Parte 2 - 60min

### Revisão: Cartografia Parte 1

Na Aula 19, estudamos:
- Orientação (pontos cardeais, Rosa dos Ventos)
- Coordenadas geográficas (latitude e longitude)
- Fusos horários
- Escala (numérica e gráfica)

**Nesta aula:** projeções cartográficas, tipos de mapas e representações.

### Projeções Cartográficas

**Problema fundamental:** representar uma superfície esférica (Terra) em um plano (mapa) sempre causa **distorções**.

**Projeção Cartográfica:** técnica matemática para transferir a superfície curva da Terra para um plano.

**Distorções inevitáveis:**
- **Forma** (deformação dos contornos)
- **Área** (tamanho relativo)
- **Distância** (comprimentos)
- **Ângulo/direção**

**Importante:** NENHUMA projeção é perfeita! Cada uma tem vantagens e distorções.

### Tipos de Projeções

#### 1. Quanto à Superfície de Projeção

**a) Projeção Cilíndrica**
- Terra projetada sobre um cilindro
- Cilindro depois "desenrolado"
- **Distorções:** aumentam perto dos polos
- **Preserva:** direções (ângulos)
- **Uso:** navegação, mapas-múndi

**Exemplo:** Projeção de Mercator

```
   Cilindro
      ║║
    ╱ ║║ ╲
   │ Terra│
    ╲ ║║ ╱
      ║║
      
Desenrolado: [────────────]
```

**b) Projeção Cônica**
- Terra projetada sobre um cone
- Cone depois "desenrolado"
- **Distorções:** menores em latitudes médias
- **Preserva:** formas em regiões específicas
- **Uso:** mapas de continentes, países

```
      /\
     /  \
    / Terra
   /____  \
```

**c) Projeção Azimutal (ou Plana)**
- Terra projetada sobre um plano tangente
- **Distorções:** aumentam do centro para as bordas
- **Preserva:** distâncias a partir do centro
- **Uso:** mapas polares, rotas aéreas

```
     ┌─────┐
     │Plano│
     └──┬──┘
      Terra
```

#### 2. Quanto às Propriedades Preservadas

**a) Projeção Conforme**
- Preserva **ângulos e formas** locais
- **Distorce áreas** (especialmente em altas latitudes)
- **Exemplo:** Mercator

**b) Projeção Equivalente**
- Preserva **áreas** (proporções corretas)
- **Distorce formas**
- **Exemplo:** Peters, Mollweide

**c) Projeção Equidistante**
- Preserva **distâncias** a partir de um ponto
- **Distorce áreas e formas**
- **Exemplo:** Azimutal equidistante

### Principais Projeções

#### Projeção de Mercator (1569)

**Tipo:** Cilíndrica conforme

**Características:**
- Paralelos e meridianos formam ângulos retos
- **Preserva:** formas e ângulos (navegação)
- **Distorce:** áreas (altas latitudes muito exageradas)

**Distorções:**
- Groenlândia parece maior que a África (na realidade, África é 14× maior)
- Polos aparecem infinitamente grandes (não representados)

**Uso:**
- Navegação marítima (mantém rumos constantes)
- Mapas-múndi tradicionais

**Crítica:**
- **Eurocentrismo:** Europa no centro, exagerada
- Distorce percepção geopolítica

#### Projeção de Peters (1973)

**Tipo:** Cilíndrica equivalente

**Características:**
- **Preserva:** áreas (proporções corretas)
- **Distorce:** formas (continentes "esticados" verticalmente)

**Objetivo:**
- Crítica à Mercator
- Valorizar países tropicais e do Sul (tamanhos reais)

**Uso:**
- Mapas temáticos
- Representação mais justa das áreas

**Comparação Mercator vs Peters:**
- **Mercator:** Europa e América do Norte exageradas
- **Peters:** África e América do Sul em tamanho real

#### Projeção de Robinson

**Tipo:** Pseudo-cilíndrica

**Características:**
- **Compromisso:** minimiza todas as distorções
- Não preserva perfeitamente nada, mas equilibra
- Meridianos curvos (não retilíneos)

**Uso:**
- Mapas-múndi gerais
- Adotada por National Geographic, ONU

#### Projeção Azimutal Polar

**Tipo:** Plana/Azimutal

**Características:**
- Centro: Polo Norte ou Polo Sul
- Meridianos: raios do centro
- Paralelos: círculos concêntricos

**Uso:**
- Mapas polares
- Geopolítica do Ártico

### Tipos de Representações Cartográficas

#### Mapa
Representação plana da superfície terrestre em escala pequena (grande área).

**Exemplos:**
- Mapa-múndi
- Mapa do Brasil
- Mapa político da América do Sul

#### Carta
Representação em escala média.

**Uso:** finalidades técnicas, científicas, navegação.

**Exemplo:** cartas náuticas, topográficas

#### Planta
Representação em escala grande (pequena área, muitos detalhes).

**Exemplos:**
- Planta de cidade
- Planta de bairro
- Planta arquitetônica

**Resumo:**
```
MAPA: escala pequena (1:1.000.000) - país, continente
CARTA: escala média (1:100.000) - região
PLANTA: escala grande (1:10.000) - cidade, bairro
```

### Elementos de um Mapa

Todo mapa deve conter:

1. **Título:** assunto representado
2. **Legenda:** significado dos símbolos
3. **Escala:** relação mapa/realidade
4. **Orientação:** Rosa dos Ventos ou seta Norte
5. **Fonte:** origem dos dados
6. **Coordenadas:** latitude/longitude (opcional)

### Tipos de Mapas Temáticos

#### Mapa Físico
Representa relevo, hidrografia, vegetação.

**Cores convencionais:**
- **Verde:** planícies, baixas altitudes
- **Amarelo/laranja:** planaltos
- **Marrom/vermelho:** montanhas
- **Azul:** água (oceanos, rios, lagos)
- **Branco:** neve, gelo

#### Mapa Político
Representa divisões administrativas (países, estados, municípios).

**Elementos:**
- Fronteiras
- Capitais
- Cidades principais

#### Mapa Econômico
Representa atividades econômicas, recursos, produção.

**Exemplos:**
- Agricultura (cultivos)
- Indústria (localização)
- Recursos minerais

#### Mapa Demográfico
Representa população.

**Temas:**
- Densidade demográfica
- Distribuição populacional
- Migrações

#### Mapa Climático
Representa climas, temperaturas, chuvas.

### Curvas de Nível

**Definição:** linhas que unem pontos de mesma altitude.

**Características:**
- Equidistância vertical constante (ex: 10 m, 50 m)
- **Curvas próximas:** relevo íngreme (montanha)
- **Curvas afastadas:** relevo suave (planície)
- Nunca se cruzam

**Uso:** mapas topográficos, engenharia

```
Vista de cima:      Vista de perfil:
   ___                  /\
  /   \                /  \
 /     \              /    \
|       |            /______\
 \     /            
  \___/              

Curvas de nível    Montanha
```

### Sensoriamento Remoto e Tecnologias

**Sensoriamento Remoto:** obtenção de informações sobre a superfície terrestre sem contato direto.

**Tecnologias:**

1. **Satélites:**
   - Imagens de alta resolução
   - Monitoramento ambiental
   - Clima e meteorologia

2. **GPS (Global Positioning System):**
   - Localização precisa por satélites
   - Navegação
   - Mapeamento

3. **SIG (Sistema de Informação Geográfica):**
   - Software para análise espacial
   - Cruzamento de dados geográficos
   - Planejamento urbano e ambiental

4. **Drones:**
   - Mapeamento de pequenas áreas
   - Alta precisão

### Exercícios Resolvidos

#### Exercício 1
Qual projeção é mais adequada para navegação marítima? Por quê?

**Resposta:**
**Projeção de Mercator**. Porque preserva ângulos e formas, permitindo traçar rotas de rumo constante (loxodrômicas). Apesar de distorcer áreas, mantém as direções corretas, essencial para navegação.

#### Exercício 2
Compare as projeções de Mercator e Peters quanto à representação da África.

**Resposta:**
- **Mercator:** África aparece menor que a Groenlândia (distorção de área)
- **Peters:** África em tamanho real, muito maior que Groenlândia (preserva área)
  
A África tem 30 milhões km², Groenlândia 2 milhões km². Peters mostra proporção correta.

#### Exercício 3
Em um mapa, curvas de nível estão muito próximas. O que isso indica?

**Resposta:**
Relevo **íngreme** (montanhoso). Curvas próximas significam que a altitude varia muito em pequena distância horizontal, caracterizando terreno inclinado.

#### Exercício 4
(UFMG) Qual tipo de representação tem maior escala: mapa, carta ou planta?

**Resposta:**
**Planta** (escala grande, ex: 1:10.000).

Lembre-se: escala grande = denominador pequeno = área pequena = mais detalhes.

### Dicas para a Prova

1. **Projeção cilíndrica:** distorce polos (Mercator, Peters)
2. **Mercator:** preserva formas, distorce áreas
3. **Peters:** preserva áreas, distorce formas
4. **Curvas próximas:** relevo íngreme
5. **Escala grande:** planta (mais detalhes)
6. **Escala pequena:** mapa (menos detalhes)
7. **Mapa temático:** representa um tema específico
8. **SIG, GPS, satélites:** tecnologias modernas

### Conceitos-Chave para Memorizar

**Projeções:**
- **Mercator:** conforme (ângulos), navegação, distorce áreas
- **Peters:** equivalente (áreas), crítica ao eurocentrismo
- **Robinson:** compromisso, equilíbrio

**Tipos:**
- Cilíndrica: distorce polos
- Cônica: latitudes médias
- Azimutal: centrada em ponto

**Representações:**
- Mapa: escala pequena (país, continente)
- Carta: escala média (região)
- Planta: escala grande (cidade, bairro)

**Curvas de Nível:**
- Próximas: íngreme
- Afastadas: suave

### Resumo Visual

```
PROJEÇÕES:

Cilíndrica (Mercator):
 ║Terra║
 ║ ↓   ║
[────────] Polos distorcidos

Peters (Equivalente):
[────────] Áreas corretas
    ↕      Formas esticadas

Cônica:
   /\
  /Te\ 
 /__rra_\ Latitudes médias

Azimutal:
   ┌─┐
 ┌─┴─┴─┐  Centro = polo
 └─────┘

CURVAS DE NÍVEL:

Íngreme:  Suave:
 ___        ___
 ___
 ___        ___
 ___
           ___
```

### Tabela Comparativa

```
┌──────────┬───────────┬──────────┬──────────┐
│ Projeção │   Tipo    │ Preserva │ Distorce │
├──────────┼───────────┼──────────┼──────────┤
│ Mercator │ Cilíndrica│ Ângulos  │  Áreas   │
│ Peters   │ Cilíndrica│  Áreas   │  Formas  │
│ Robinson │Pseudo-cil.│Equilíbrio│  Pouco   │
│ Azimutal │   Plana   │Distâncias│  Bordas  │
└──────────┴───────────┴──────────┴──────────┘

Escala:
┌────────┬──────────────┬──────────┬─────────┐
│  Tipo  │    Escala    │   Área   │Detalhes │
├────────┼──────────────┼──────────┼─────────┤
│  MAPA  │Pequena(1:1M) │  Grande  │  Poucos │
│ CARTA  │Média(1:100k) │  Média   │  Médios │
│ PLANTA │Grande(1:10k) │ Pequena  │  Muitos │
└────────┴──────────────┴──────────┴─────────┘
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - interpretação de mapas)

## Aula 25 - Português: Tempo e Modo Verbais - 60min

### O que são Verbos?

**Verbo** é a classe de palavras que indica **ação**, **estado** ou **fenômeno da natureza**, situando-os no tempo.

**Exemplos:**
- Ação: correr, estudar, escrever
- Estado: ser, estar, permanecer
- Fenômeno: chover, nevar, trovejar

**O verbo é o núcleo da oração!**

### Estrutura do Verbo

**Verbo = RADICAL + VOGAL TEMÁTICA + DESINÊNCIAS**

**Exemplo:** cant**ávamos**
- **RADICAL:** cant- (parte invariável, traz o significado)
- **VOGAL TEMÁTICA:** -a- (indica conjugação)
- **DESINÊNCIA MODO-TEMPORAL:** -va- (indica tempo e modo)
- **DESINÊNCIA NÚMERO-PESSOAL:** -mos (indica pessoa e número)

### Conjugações

Verbos são classificados em **3 conjugações** pela vogal temática:

| Conjugação | Vogal Temática | Exemplos |
|------------|----------------|----------|
| **1ª** | -A- | cant**a**r, am**a**r, estud**a**r |
| **2ª** | -E- | vend**e**r, com**e**r, beb**e**r |
| **3ª** | -I- | part**i**r, sorr**i**r, dorm**i**r |

**Exceção:** verbos **pôr** (e derivados: compor, repor) → 2ª conjugação (antigamente "poer")

### Flexões Verbais

Os verbos flexionam em:

1. **NÚMERO:** singular, plural
2. **PESSOA:** 1ª, 2ª, 3ª
3. **TEMPO:** presente, passado (pretérito), futuro
4. **MODO:** indicativo, subjuntivo, imperativo
5. **VOZ:** ativa, passiva, reflexiva (estudaremos depois)

### Pessoas Verbais

| Pessoa | Singular | Plural |
|--------|----------|--------|
| **1ª** | eu | nós |
| **2ª** | tu | vós |
| **3ª** | ele/ela | eles/elas |

**Observação:** no Brasil, usa-se muito "você" (3ª pessoa) em vez de "tu" (2ª pessoa).

### Modos Verbais

**Modo** indica a **atitude** do falante em relação ao que está dizendo.

#### 1. Modo Indicativo
Expressa **certeza, fato real** (afirmação, negação, pergunta).

**Uso:** ações concretas, situações reais.

**Exemplos:**
- Eu **estudo** todos os dias. (certeza)
- Ela **viajou** ontem. (fato)
- Vocês **chegarão** cedo? (pergunta sobre fato)

#### 2. Modo Subjuntivo
Expressa **dúvida, possibilidade, desejo, hipótese**.

**Uso:** ações incertas, dependentes de condições.

**Exemplos:**
- Espero que ele **estude**. (desejo)
- Se eu **pudesse**, viajaria. (hipótese)
- Talvez eles **venham**. (dúvida)

**Palavras indicadoras:** espero que, talvez, se, caso, quando (futuro)

#### 3. Modo Imperativo
Expressa **ordem, pedido, conselho**.

**Uso:** dar comandos, instruções.

**Exemplos:**
- **Estude** mais! (ordem)
- **Venha** aqui, por favor. (pedido)
- **Tenha** cuidado. (conselho)

**Formas:**
- **Imperativo afirmativo:** Faça isso!
- **Imperativo negativo:** Não faça isso!

### Tempos Verbais no Modo Indicativo

#### Presente do Indicativo
Ação que ocorre **no momento da fala** ou **habitualmente**.

**Usos:**
1. Momento presente: Eu **estudo** agora.
2. Ação habitual: Ela **acorda** cedo todos os dias.
3. Verdade universal: A Terra **gira** em torno do Sol.
4. Presente histórico: Em 1500, Cabral **chega** ao Brasil.

**Conjugação - verbo CANTAR:**
- eu cant**o**
- tu cant**as**
- ele cant**a**
- nós cant**amos**
- vós cant**ais**
- eles cant**am**

#### Pretérito Perfeito
Ação **concluída** no passado.

**Uso:** fato pontual, acabado.

**Exemplos:**
- Eu **estudei** ontem.
- Eles **chegaram** às 8h.

**Conjugação - CANTAR:**
- eu cant**ei**
- tu cant**aste**
- ele cant**ou**
- nós cant**amos**
- vós cant**astes**
- eles cant**aram**

#### Pretérito Imperfeito
Ação **contínua, habitual ou inacabada** no passado.

**Usos:**
1. Ação habitual: Eu **estudava** todos os dias quando era criança.
2. Ação contínua: Ela **lia** quando eu cheguei.
3. Descrição: O dia **estava** lindo.

**Conjugação - CANTAR:**
- eu cant**ava**
- tu cant**avas**
- ele cant**ava**
- nós cant**ávamos**
- vós cant**áveis**
- eles cant**avam**

**Diferença Perfeito vs Imperfeito:**
- **Perfeito:** Eu **li** o livro. (ação concluída)
- **Imperfeito:** Eu **lia** o livro. (ação em andamento/habitual)

#### Pretérito Mais-que-Perfeito
Ação **anterior** a outra ação no passado.

**Uso:** passado do passado.

**Exemplo:**
Quando cheguei, ele já **saíra**. (saiu antes de eu chegar)

**Conjugação - CANTAR:**
- eu cant**ara**
- tu cant**aras**
- ele cant**ara**
- nós cant**áramos**
- vós cant**áreis**
- eles cant**aram**

**Forma composta (mais usada):**
tinha/havia + particípio
- Quando cheguei, ele já **tinha saído**.

#### Futuro do Presente
Ação que **vai acontecer**.

**Uso:** previsão, promessa.

**Exemplos:**
- Eu **estudarei** amanhã.
- Eles **viajarão** no mês que vem.

**Conjugação - CANTAR:**
- eu cantar**ei**
- tu cantar**ás**
- ele cantar**á**
- nós cantar**emos**
- vós cantar**eis**
- eles cantar**ão**

#### Futuro do Pretérito
Ação **futura em relação a um momento passado**; também expressa **condição**.

**Usos:**
1. Futuro do passado: Ele disse que **viria**. (viria = futuro em relação ao passado)
2. Condição: Se eu pudesse, **viajaria**. (condição)
3. Incerteza/dúvida: Será que ela **estaria** em casa? (dúvida educada)

**Conjugação - CANTAR:**
- eu cantar**ia**
- tu cantar**ias**
- ele cantar**ia**
- nós cantar**íamos**
- vós cantar**íeis**
- eles cantar**iam**

### Tempos do Modo Subjuntivo

#### Presente do Subjuntivo
Exprime **dúvida, desejo** no presente ou futuro.

**Palavras-chave:** que, espero que, talvez

**Exemplos:**
- Espero que ele **estude**.
- Talvez eu **viaje** amanhã.

**Conjugação - CANTAR:**
- que eu cant**e**
- que tu cant**es**
- que ele cant**e**
- que nós cant**emos**
- que vós cant**eis**
- que eles cant**em**

**Dica:** geralmente acompanha "que"

#### Pretérito Imperfeito do Subjuntivo
Exprime **hipótese, condição** no passado.

**Palavras-chave:** se, caso

**Exemplos:**
- Se eu **estudasse**, passaria.
- Caso ele **viesse**, ficaríamos felizes.

**Conjugação - CANTAR:**
- se eu cant**asse**
- se tu cant**asses**
- se ele cant**asse**
- se nós cant**ássemos**
- se vós cant**ásseis**
- se eles cant**assem**

**Terminação:** sempre -**sse**

#### Futuro do Subjuntivo
Exprime **ação futura incerta, hipotética**.

**Palavras-chave:** quando, se, assim que (futuro)

**Exemplos:**
- Quando eu **chegar**, te ligo.
- Se você **estudar**, passará.

**Conjugação - CANTAR:**
- quando eu cant**ar**
- quando tu cant**ares**
- quando ele cant**ar**
- quando nós cant**armos**
- quando vós cant**ardes**
- quando eles cant**arem**

**Dica:** formado a partir da 3ª pessoa do plural do pretérito perfeito (cantaram → cantar)

### Modo Imperativo

#### Imperativo Afirmativo
Ordem, pedido afirmativo.

**Formação:**
- **TU e VÓS:** vem do Presente do Indicativo (sem S em TU)
- **VOCÊ, NÓS, VOCÊS:** vem do Presente do Subjuntivo

**Exemplo - CANTAR:**
- cant**a** tu (indica → cant**as** → tira S)
- cant**e** você (subj.)
- cant**emos** nós (subj.)
- cant**ai** vós (indica → cant**ais**)
- cant**em** vocês (subj.)

#### Imperativo Negativo
Ordem negativa.

**Formação:** TODO do Presente do Subjuntivo

**Exemplo - CANTAR:**
- não cant**es** tu
- não cant**e** você
- não cant**emos** nós
- não cant**eis** vós
- não cant**em** vocês

**IMPORTANTE:** NÃO há imperativo para EU!

### Exercícios Resolvidos

#### Exercício 1
Identifique o tempo e modo verbal:
a) Eu estudava muito quando era criança.
b) Espero que você venha à festa.
c) Se eu pudesse, viajaria.

**Solução:**

a) estudava: Pretérito Imperfeito do Indicativo (ação habitual no passado)

b) venha: Presente do Subjuntivo (desejo: "espero que")

c) pudesse: Pretérito Imperfeito do Subjuntivo (hipótese: "se")
   viajaria: Futuro do Pretérito do Indicativo (condição)

#### Exercício 2
Conjugue o verbo PARTIR no Presente do Indicativo.

**Solução:**
- eu part**o**
- tu part**es**
- ele part**e**
- nós part**imos**
- vós part**is**
- eles part**em**

#### Exercício 3
Complete: "Quando você _______ (chegar), me avise."

**Solução:**
"Quando você **chegar**, me avise."

**Tempo:** Futuro do Subjuntivo (ação futura incerta: "quando")

#### Exercício 4
Passe para o Imperativo Afirmativo (você): "Você estuda."

**Solução:**
"**Estude** você."

**Formação:** Presente do Subjuntivo (que você estude → estude)

#### Exercício 5
Qual a diferença:
a) Ele viajou.
b) Ele viajava.

**Solução:**

a) **Pretérito Perfeito:** ação concluída, pontual ("Ele viajou ontem.")

b) **Pretérito Imperfeito:** ação habitual ou contínua ("Ele viajava todos os meses." ou "Ele viajava quando o vi.")

### Dicas para a Prova

1. **Indicativo:** certeza, fatos reais
2. **Subjuntivo:** dúvida, desejo, hipótese (que, se, talvez)
3. **Imperativo:** ordem, pedido (sem EU)
4. **Perfeito:** ação concluída (-ei, -ou, -aram)
5. **Imperfeito:** ação contínua/habitual (-ava, -ia)
6. **Futuro do Pretérito:** condição (-ia: faria, seria)
7. **Subjuntivo Imperfeito:** sempre -sse (estudasse, fizesse)
8. **Futuro do Subjuntivo:** quando, se futuro (estudar, fizer)

### Conceitos-Chave para Memorizar

**Modos:**
- **Indicativo:** certeza
- **Subjuntivo:** dúvida, desejo
- **Imperativo:** ordem

**Pretéritos (Indicativo):**
- **Perfeito:** acabou (estudei)
- **Imperfeito:** contínuo/habitual (estudava)
- **Mais-que-Perfeito:** passado do passado (estudara/tinha estudado)

**Futuros (Indicativo):**
- **Futuro do Presente:** vai acontecer (estudarei)
- **Futuro do Pretérito:** condição (estudaria)

**Subjuntivo (palavras-chave):**
- **Presente:** que, talvez
- **Imperfeito:** se, caso
- **Futuro:** quando, se (futuro)

### Tabelas de Conjugação

```
MODO INDICATIVO - CANTAR

Presente:       Pret. Perfeito:  Pret. Imperf.:
eu cant-o       cant-ei          cant-ava
tu cant-as      cant-aste        cant-avas
ele cant-a      cant-ou          cant-ava
nós cant-amos   cant-amos        cant-ávamos
vós cant-ais    cant-astes       cant-áveis
eles cant-am    cant-aram        cant-avam

Fut. Presente:  Fut. Pretérito:
cantar-ei       cantar-ia
cantar-ás       cantar-ias
cantar-á        cantar-ia
cantar-emos     cantar-íamos
cantar-eis      cantar-íeis
cantar-ão       cantar-iam

MODO SUBJUNTIVO - CANTAR

Presente:          Pret. Imperf.:   Futuro:
que eu cant-e      se eu cant-asse  quando eu cant-ar
que tu cant-es     se tu cant-asses quando tu cant-ares
que ele cant-e     se ele cant-asse quando ele cant-ar
que nós cant-emos  se nós cant-ássemos quando nós cant-armos
que vós cant-eis   se vós cant-ásseis quando vós cant-ardes
que eles cant-em   se eles cant-assem quando eles cant-arem

MODO IMPERATIVO - CANTAR

Afirmativo:    Negativo:
—              —
cant-a tu      não cant-es tu
cant-e você    não cant-e você
cant-emos nós  não cant-emos nós
cant-ai vós    não cant-eis vós
cant-em vocês  não cant-em vocês
```

### Resumo Visual

```
MODOS VERBAIS:

INDICATIVO (certeza)
├─ Presente (agora)
├─ Pretérito Perfeito (acabou)
├─ Pretérito Imperfeito (contínuo)
├─ Pretérito Mais-que-Perf. (antes do passado)
├─ Futuro do Presente (vai acontecer)
└─ Futuro do Pretérito (condição)

SUBJUNTIVO (dúvida)
├─ Presente (que, talvez)
├─ Pretérito Imperfeito (se, -sse)
└─ Futuro (quando futuro)

IMPERATIVO (ordem)
├─ Afirmativo (Faça!)
└─ Negativo (Não faça!)

Palavras-chave Subjuntivo:
QUE, TALVEZ → Presente
SE, CASO → Imperfeito (-sse)
QUANDO, SE (futuro) → Futuro
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - base da conjugação verbal)

# 11/23 - Dia 6

## Aula 26 - Matemática: Função Quadrática - Parte 1 - 120min

### O que é Função Quadrática?

**Função Quadrática** (ou função do 2º grau) é toda função do tipo:

```
f(x) = ax² + bx + c
```

Onde:
- **a, b, c:** coeficientes reais
- **a ≠ 0** (se a = 0, vira função afim)
- **x:** variável
- **Grau:** 2 (maior expoente)

**Exemplos:**
- f(x) = x² - 4x + 3 (a=1, b=-4, c=3)
- f(x) = -2x² + 5x (a=-2, b=5, c=0)
- f(x) = 3x² - 7 (a=3, b=0, c=-7)
- f(x) = -x² (a=-1, b=0, c=0)

### Gráfico da Função Quadrática: Parábola

O gráfico de f(x) = ax² + bx + c é uma **parábola**.

**Características:**
- Curva simétrica
- Possui eixo de simetria (reta vertical)
- Tem um ponto de máximo ou mínimo (vértice)

#### Concavidade da Parábola

Depende do sinal de **a**:

**a > 0 (positivo):**
- Concavidade para **cima** (∪)
- Parábola "sorri"
- Tem ponto de **mínimo**

```
    /   \
   /  V  \
  /       \
```

**a < 0 (negativo):**
- Concavidade para **baixo** (∩)
- Parábola "triste"
- Tem ponto de **máximo**

```
  \       /
   \  ^  /
    \   /
```

**Regra prática:**
- **a > 0:** parábola "feliz" ∪ (mínimo)
- **a < 0:** parábola "triste" ∩ (máximo)

### Zeros (ou Raízes) da Função

**Zeros da função:** valores de x onde f(x) = 0 (onde a parábola corta o eixo x).

**Encontrar os zeros:**
Resolver a equação ax² + bx + c = 0

#### Fórmula de Bhaskara

```
x = (-b ± √Δ) / 2a

Onde: Δ = b² - 4ac  (discriminante)
```

**Discriminante (Δ ou Delta):**
Determina o número de raízes reais.

**Δ > 0:** duas raízes reais e distintas (x₁ ≠ x₂)
- Parábola corta o eixo x em 2 pontos

**Δ = 0:** uma raiz real (ou duas iguais: x₁ = x₂)
- Parábola toca o eixo x em 1 ponto (vértice no eixo)

**Δ < 0:** nenhuma raiz real
- Parábola não corta o eixo x

#### Visualização

```
Δ > 0 (2 raízes):        Δ = 0 (1 raiz):       Δ < 0 (0 raízes):
    /\                       /\                      ___
   /  \                     /  \                    /   \
  /____\                   /____\                  |_____|
 x₁    x₂                   x₁                    (sem raiz)
 
  (a<0)                    (a<0)                    (a<0)

  \____/                   \____/                   _____
   \  /                     \  /                   \   /
    \/                       \/                     \_/
   x₁ x₂                     x₁                  (sem raiz)
   
  (a>0)                    (a>0)                    (a>0)
```

### Coeficientes e suas Funções

#### Coeficiente a
- Determina **concavidade** (a>0: ∪; a<0: ∩)
- Quanto maior |a|, mais "fechada" a parábola
- Quanto menor |a|, mais "aberta" a parábola

#### Coeficiente c
- Indica onde a parábola **corta o eixo y**
- Quando x = 0: f(0) = c
- **Ponto:** (0, c)

#### Coeficiente b
- Influencia a posição horizontal da parábola
- Relacionado ao eixo de simetria

### Vértice da Parábola

**Vértice (V):** ponto de máximo (a<0) ou mínimo (a>0) da parábola.

**Coordenadas do vértice:**
```
x_v = -b / 2a

y_v = -Δ / 4a  ou  y_v = f(x_v)
```

**Vértice:** V(x_v, y_v)

**Eixo de simetria:** reta vertical x = x_v

**Importância:**
- **Máximo/Mínimo** da função
- Centro da simetria
- Ponto fundamental para esboçar o gráfico

### Relações entre Raízes e Coeficientes

Se x₁ e x₂ são as raízes de ax² + bx + c = 0:

**Soma das raízes:**
```
x₁ + x₂ = -b/a
```

**Produto das raízes:**
```
x₁ · x₂ = c/a
```

**Forma fatorada (se existem raízes reais):**
```
f(x) = a(x - x₁)(x - x₂)
```

### Forma Canônica (ou Forma de Vértice)

```
f(x) = a(x - x_v)² + y_v
```

Onde (x_v, y_v) é o vértice.

**Vantagem:** mostra claramente o vértice.

### Exemplos Resolvidos

#### Exemplo 1
Determine as raízes de f(x) = x² - 5x + 6

**Solução:**
a = 1, b = -5, c = 6

Δ = b² - 4ac = (-5)² - 4(1)(6) = 25 - 24 = 1

x = (-b ± √Δ) / 2a = (5 ± 1) / 2

x₁ = (5 + 1)/2 = 3
x₂ = (5 - 1)/2 = 2

**Raízes:** x = 2 ou x = 3

**Verificação:**
f(2) = 4 - 10 + 6 = 0 ✓
f(3) = 9 - 15 + 6 = 0 ✓

#### Exemplo 2
Calcule o vértice de f(x) = -x² + 4x - 3

**Solução:**
a = -1, b = 4, c = -3

x_v = -b/2a = -4/2(-1) = -4/(-2) = 2

y_v = f(2) = -(2)² + 4(2) - 3 = -4 + 8 - 3 = 1

**Vértice:** V(2, 1)

Como a = -1 < 0, é ponto de **máximo**.

#### Exemplo 3
Esboce o gráfico de f(x) = x² - 4x + 3

**Solução:**

**1. Concavidade:**
a = 1 > 0 → concavidade para cima ∪ (mínimo)

**2. Raízes:**
Δ = 16 - 12 = 4
x = (4 ± 2)/2
x₁ = 1, x₂ = 3

**3. Corte eixo y:**
c = 3 → ponto (0, 3)

**4. Vértice:**
x_v = -(-4)/2(1) = 2
y_v = f(2) = 4 - 8 + 3 = -1
V(2, -1)

**Gráfico:**
```
      |
    3 •(0,3)
      |
    1 |___
      |   \
   -1 |    •V(2,-1)
      |   /
   ---|---•---•---
      | 1 2 3
```

### Exercícios Resolvidos

#### Exercício 1
Determine a, b, c e a concavidade:
f(x) = -2x² + 3x - 1

**Solução:**
a = -2 (concavidade para baixo ∩)
b = 3
c = -1

**Resposta:** a=-2, b=3, c=-1; concavidade para baixo

#### Exercício 2
Quantas raízes reais tem f(x) = x² - 2x + 5?

**Solução:**
Δ = (-2)² - 4(1)(5) = 4 - 20 = -16 < 0

**Resposta:** Nenhuma raiz real (Δ < 0)

#### Exercício 3
As raízes de uma função quadrática são 2 e 5. Se a = 1, qual a função?

**Solução:**
Forma fatorada: f(x) = a(x - x₁)(x - x₂)

f(x) = 1(x - 2)(x - 5)
f(x) = (x - 2)(x - 5)
f(x) = x² - 5x - 2x + 10
f(x) = x² - 7x + 10

**Resposta:** f(x) = x² - 7x + 10

**Verificação usando relações:**
x₁ + x₂ = 2 + 5 = 7 = -b/a → b = -7 ✓
x₁ · x₂ = 2 × 5 = 10 = c/a → c = 10 ✓

#### Exercício 4
Determine o valor máximo de f(x) = -x² + 6x - 5

**Solução:**
a = -1 < 0 → tem máximo (vértice)

x_v = -6/2(-1) = 3

y_v = f(3) = -9 + 18 - 5 = 4

**Valor máximo:** 4 (no ponto x = 3)

**Resposta:** Máximo = 4 em x = 3

#### Exercício 5
Uma função quadrática tem vértice V(2, -1) e passa pelo ponto (0, 3). Determine a função.

**Solução:**
Forma canônica: f(x) = a(x - x_v)² + y_v

f(x) = a(x - 2)² - 1

Passa por (0, 3):
3 = a(0 - 2)² - 1
3 = 4a - 1
4a = 4
a = 1

**Função:** f(x) = (x - 2)² - 1

Expandindo:
f(x) = x² - 4x + 4 - 1 = x² - 4x + 3

**Resposta:** f(x) = x² - 4x + 3

### Dicas para a Prova

1. **a > 0:** ∪ (mínimo); **a < 0:** ∩ (máximo)
2. **Δ > 0:** 2 raízes; **Δ = 0:** 1 raiz; **Δ < 0:** 0 raízes
3. **c:** corte com eixo y (ponto (0, c))
4. **Vértice:** x_v = -b/2a, depois calcular y_v = f(x_v)
5. **Bhaskara:** decorar x = (-b ± √Δ) / 2a
6. **Soma raízes:** -b/a; **Produto raízes:** c/a
7. **Forma fatorada:** f(x) = a(x - x₁)(x - x₂)
8. **Esboço:** concavidade + raízes + vértice + (0,c)

### Conceitos-Chave para Memorizar

**Função Quadrática:**
- f(x) = ax² + bx + c (a ≠ 0)
- Gráfico: parábola

**Concavidade:**
- a > 0: ∪ (mínimo)
- a < 0: ∩ (máximo)

**Discriminante (Δ):**
- Δ = b² - 4ac
- Δ > 0: 2 raízes
- Δ = 0: 1 raiz
- Δ < 0: 0 raízes

**Vértice:**
- V(x_v, y_v)
- x_v = -b/2a
- y_v = -Δ/4a ou f(x_v)
- Ponto de máximo/mínimo

**Raízes:**
- x = (-b ± √Δ) / 2a

### Fórmulas Essenciais

```
Função Quadrática:
f(x) = ax² + bx + c  (a ≠ 0)

Discriminante:
Δ = b² - 4ac

Fórmula de Bhaskara:
x = (-b ± √Δ) / 2a

Vértice:
x_v = -b / 2a
y_v = -Δ / 4a  ou  y_v = f(x_v)

Relações:
Soma: x₁ + x₂ = -b/a
Produto: x₁ · x₂ = c/a

Formas:
Padrão: f(x) = ax² + bx + c
Fatorada: f(x) = a(x - x₁)(x - x₂)
Canônica: f(x) = a(x - x_v)² + y_v

Interpretações:
c: corte com eixo y
raízes: cortes com eixo x
vértice: máximo (a<0) ou mínimo (a>0)
```

### Resumo Visual

```
PARÁBOLA:

a > 0 (mínimo):        a < 0 (máximo):
    /\                     \  /
   /  \V                    \/V
  /____\                    /\
               
Δ e Raízes:

Δ > 0:  \_____/      Δ = 0:  \___/      Δ < 0:   ___
         x₁  x₂               x           \   /
        2 raízes             1 raiz       0 raízes

Elementos:
         eixo simetria
              |
       V(x_v,y_v)
      /|\
     / | \
    /  |  \
   x₁  |  x₂
       |
    (0,c)

Concavidade (memorizar):
a > 0: ∪  "feliz" (mínimo)
a < 0: ∩  "triste" (máximo)
```

### Tabela Resumo

```
┌─────────┬──────────┬──────────┬─────────────┐
│  Delta  │  Raízes  │  Gráfico │ Observação  │
├─────────┼──────────┼──────────┼─────────────┤
│  Δ > 0  │    2     │ Corta 2x │ x₁ ≠ x₂     │
│  Δ = 0  │    1     │ Toca 1x  │ x₁ = x₂     │
│  Δ < 0  │    0     │Não corta │ Sem raiz    │
└─────────┴──────────┴──────────┴─────────────┘

┌─────────┬───────────┬─────────────────┐
│Coef.    │ Significado│   Informação    │
├─────────┼───────────┼─────────────────┤
│   a     │Concavidade│ >0:∪ / <0:∩     │
│   b     │Posição    │ Relacionado x_v │
│   c     │Corte eixo y│ Ponto (0,c)    │
└─────────┴───────────┴─────────────────┘
```

---

**Tempo de estudo recomendado:** 120 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - muito cobrado!)

## Aula 27 - Matemática: Exercícios de Funções - 90min

### Objetivo desta Aula

Esta aula é dedicada à **prática intensiva** de exercícios sobre as funções estudadas até agora:
- Função Afim (1º grau)
- Função Quadrática (2º grau)

**Foco:** consolidar conhecimentos, ganhar velocidade e identificar padrões de questões.

### Bloco 1: Função Afim - Exercícios

#### Exercício 1
Determine a função afim f(x) = ax + b sabendo que f(2) = 5 e f(-1) = -4.

**Solução:**

Sistema:
```
{ 2a + b = 5
{ -a + b = -4
```

Subtraindo a 2ª da 1ª:
3a = 9 → a = 3

Substituindo em -a + b = -4:
-3 + b = -4 → b = -1

**Resposta:** f(x) = 3x - 1

**Verificação:**
f(2) = 6 - 1 = 5 ✓
f(-1) = -3 - 1 = -4 ✓

#### Exercício 2
Uma reta passa pelos pontos A(1, 3) e B(4, 9). Determine sua equação.

**Solução:**

Coeficiente angular:
a = (y₂ - y₁)/(x₂ - x₁) = (9 - 3)/(4 - 1) = 6/3 = 2

Usando ponto A(1, 3):
y = ax + b
3 = 2(1) + b
b = 1

**Resposta:** y = 2x + 1 ou f(x) = 2x + 1

#### Exercício 3
Determine o zero da função f(x) = -3x + 12.

**Solução:**

f(x) = 0
-3x + 12 = 0
-3x = -12
x = 4

**Resposta:** x = 4

#### Exercício 4
Resolva a inequação: 2x - 5 > 3x + 1

**Solução:**

2x - 5 > 3x + 1
2x - 3x > 1 + 5
-x > 6
x < -6  (inverte ao multiplicar por -1)

**Resposta:** x < -6  ou  x ∈ (-∞, -6)

#### Exercício 5
Determine para quais valores de x a função f(x) = -2x + 8 é positiva.

**Solução:**

**Método 1 - Algebricamente:**
f(x) > 0
-2x + 8 > 0
-2x > -8
x < 4

**Método 2 - Estudo do sinal:**
Zero: -2x + 8 = 0 → x = 4
a = -2 < 0 (decrescente)

```
    +  |  -
   ────•────
       4
```

f(x) > 0 quando x < 4

**Resposta:** x < 4  ou  x ∈ (-∞, 4)

#### Exercício 6
(UFMG) Duas funções afins f(x) = 2x + 1 e g(x) = -x + 7 se intersectam em qual ponto?

**Solução:**

f(x) = g(x)
2x + 1 = -x + 7
3x = 6
x = 2

y = 2(2) + 1 = 5

**Resposta:** Ponto (2, 5)

### Bloco 2: Função Quadrática - Exercícios

#### Exercício 7
Determine as raízes de f(x) = x² - 7x + 10.

**Solução:**

a = 1, b = -7, c = 10

Δ = (-7)² - 4(1)(10) = 49 - 40 = 9

x = (7 ± 3)/2

x₁ = 10/2 = 5
x₂ = 4/2 = 2

**Resposta:** x = 2 ou x = 5

**Alternativa - Fatoração:**
x² - 7x + 10 = 0
Procurar dois números que somam 7 e multiplicam 10: 2 e 5
(x - 2)(x - 5) = 0
x = 2 ou x = 5

#### Exercício 8
Calcule o vértice de f(x) = 2x² - 8x + 6.

**Solução:**

a = 2, b = -8, c = 6

x_v = -b/2a = 8/4 = 2

y_v = f(2) = 2(4) - 8(2) + 6 = 8 - 16 + 6 = -2

**Vértice:** V(2, -2)

Como a = 2 > 0, é ponto de **mínimo**.

**Resposta:** V(2, -2) - ponto de mínimo

#### Exercício 9
Para quais valores de k a equação x² - 4x + k = 0 tem duas raízes reais e distintas?

**Solução:**

Para duas raízes distintas: Δ > 0

Δ = b² - 4ac
Δ = (-4)² - 4(1)(k)
Δ = 16 - 4k

Condição: 16 - 4k > 0
16 > 4k
k < 4

**Resposta:** k < 4

#### Exercício 10
Uma função quadrática tem raízes 1 e 4, e seu gráfico passa pelo ponto (0, -8). Determine a função.

**Solução:**

Forma fatorada: f(x) = a(x - 1)(x - 4)

Passa por (0, -8):
-8 = a(0 - 1)(0 - 4)
-8 = a(-1)(-4)
-8 = 4a
a = -2

f(x) = -2(x - 1)(x - 4)

Expandindo:
f(x) = -2(x² - 5x + 4)
f(x) = -2x² + 10x - 8

**Resposta:** f(x) = -2x² + 10x - 8

**Verificação:**
f(0) = -8 ✓
f(1) = -2 + 10 - 8 = 0 ✓
f(4) = -32 + 40 - 8 = 0 ✓

#### Exercício 11
Determine o valor máximo de f(x) = -x² + 4x + 5.

**Solução:**

a = -1 < 0 → tem máximo

x_v = -4/2(-1) = 2

y_v = f(2) = -4 + 8 + 5 = 9

**Resposta:** Valor máximo = 9 (em x = 2)

#### Exercício 12
(UFMG) O gráfico da função f(x) = x² - 6x + 8 está inteiramente acima do eixo x?

**Solução:**

Para estar acima do eixo x, não pode ter raízes reais (Δ < 0).

Δ = (-6)² - 4(1)(8) = 36 - 32 = 4 > 0

Tem 2 raízes reais → **cruza** o eixo x.

**Resposta:** Não, pois Δ > 0 (tem raízes reais, cruza o eixo x)

### Bloco 3: Exercícios Integrados

#### Exercício 13
Resolva o sistema:
```
{ y = 2x - 1
{ y = x² - 4x + 3
```

**Solução:**

Igualando:
2x - 1 = x² - 4x + 3
0 = x² - 6x + 4
x² - 6x + 4 = 0

Δ = 36 - 16 = 20

x = (6 ± √20)/2 = (6 ± 2√5)/2 = 3 ± √5

x₁ = 3 + √5
x₂ = 3 - √5

Para cada x, calcular y = 2x - 1:

y₁ = 2(3 + √5) - 1 = 5 + 2√5
y₂ = 2(3 - √5) - 1 = 5 - 2√5

**Resposta:** Pontos (3+√5, 5+2√5) e (3-√5, 5-2√5)

#### Exercício 14
Uma bola é lançada verticalmente para cima. Sua altura h (em metros) em função do tempo t (em segundos) é dada por h(t) = -5t² + 20t + 1.

a) Qual a altura máxima atingida?
b) Em que instante atinge essa altura?
c) Quando a bola atinge o solo (h = 0)?

**Solução:**

a = -5, b = 20, c = 1

**a) Altura máxima = y_v:**

t_v = -20/2(-5) = 20/10 = 2 s

h_v = -5(4) + 20(2) + 1 = -20 + 40 + 1 = 21 m

**b) Instante:** t = 2 s

**c) Solo (h = 0):**

-5t² + 20t + 1 = 0

Dividindo por -5:
t² - 4t - 0,2 = 0

Ou usando Bhaskara na original:
Δ = 400 + 20 = 420

t = (-20 ± √420)/(-10)
t = (20 ± √420)/10

√420 ≈ 20,49

t₁ = (20 + 20,49)/10 ≈ 4,05 s (válido)
t₂ = (20 - 20,49)/10 ≈ -0,05 s (descartado: negativo)

**Respostas:** 
a) 21 m
b) 2 s
c) aproximadamente 4,05 s

#### Exercício 15
Determine o conjunto solução da inequação x² - 5x + 6 ≤ 0.

**Solução:**

**1. Raízes:**
x² - 5x + 6 = 0
Δ = 25 - 24 = 1
x = (5 ± 1)/2
x₁ = 2, x₂ = 3

**2. Concavidade:**
a = 1 > 0 (parábola para cima)

**3. Esboço:**
```
  \____/
   2  3
```

**4. f(x) ≤ 0:**
Região negativa ou zero (dentro da parábola)

**Resposta:** 2 ≤ x ≤ 3  ou  x ∈ [2, 3]

#### Exercício 16
(UFMG) A soma e o produto das raízes de 2x² - 6x + k = 0 são, respectivamente, 3 e 2. Determine k.

**Solução:**

Usando relações de Girard:

Soma: x₁ + x₂ = -b/a = 6/2 = 3 ✓ (confere)

Produto: x₁ · x₂ = c/a
2 = k/2
k = 4

**Resposta:** k = 4

**Verificação:**
2x² - 6x + 4 = 0
x² - 3x + 2 = 0
Raízes: 1 e 2
Soma: 3 ✓
Produto: 2 ✓

### Bloco 4: Desafios

#### Exercício 17
Determine a função quadrática cujo vértice é V(1, -4) e que passa pelo ponto (3, 0).

**Solução:**

Forma canônica: f(x) = a(x - 1)² - 4

Passa por (3, 0):
0 = a(3 - 1)² - 4
0 = 4a - 4
a = 1

f(x) = (x - 1)² - 4
f(x) = x² - 2x + 1 - 4
f(x) = x² - 2x - 3

**Resposta:** f(x) = x² - 2x - 3

#### Exercício 18
Para que valores de m a parábola y = x² - 2mx + 9 não intercepta o eixo x?

**Solução:**

Não interceptar eixo x: Δ < 0

Δ = b² - 4ac
Δ = (-2m)² - 4(1)(9)
Δ = 4m² - 36

Condição: 4m² - 36 < 0
4m² < 36
m² < 9
-3 < m < 3

**Resposta:** -3 < m < 3  ou  m ∈ (-3, 3)

### Dicas Finais para Resolução

**Função Afim:**
1. Dois pontos → sistema ou coeficiente angular
2. Zero → igualar a zero
3. Estudo do sinal → zero + crescimento/decrescimento
4. Inequação → estudo do sinal

**Função Quadrática:**
1. Raízes → Bhaskara ou fatoração
2. Vértice → fórmulas ou f(x_v)
3. Δ → número de raízes
4. Máximo/mínimo → vértice + sinal de a
5. Inequação → raízes + estudo do sinal

**Estratégias:**
- **Leia o enunciado com atenção**
- **Identifique o que é pedido**
- **Organize os dados**
- **Escolha o método mais adequado**
- **Verifique a resposta quando possível**

### Checklist de Conhecimentos

Após esta aula, você deve ser capaz de:

**Função Afim:**
- ✓ Determinar função dados dois pontos
- ✓ Calcular zero da função
- ✓ Fazer estudo do sinal
- ✓ Resolver inequações
- ✓ Determinar ponto de interseção entre retas
- ✓ Identificar posição relativa (paralelas, perpendiculares)

**Função Quadrática:**
- ✓ Calcular discriminante e raízes
- ✓ Determinar vértice
- ✓ Identificar máximo/mínimo
- ✓ Esboçar gráfico
- ✓ Usar forma fatorada
- ✓ Usar relações de Girard
- ✓ Resolver inequações quadráticas
- ✓ Aplicar em problemas contextualizados

### Resumo de Fórmulas Importantes

```
FUNÇÃO AFIM: f(x) = ax + b
- Zero: x = -b/a
- Coef. angular: a = Δy/Δx
- Crescente: a > 0
- Decrescente: a < 0

FUNÇÃO QUADRÁTICA: f(x) = ax² + bx + c
- Δ = b² - 4ac
- Raízes: x = (-b ± √Δ)/2a
- Vértice: x_v = -b/2a, y_v = f(x_v)
- Concavidade: a>0 (∪), a<0 (∩)
- Soma raízes: -b/a
- Produto raízes: c/a
- Forma fatorada: a(x - x₁)(x - x₂)
- Forma canônica: a(x - x_v)² + y_v

INEQUAÇÕES:
- Fazer estudo do sinal
- Usar raízes + concavidade
- Responder conforme pedido (≤, ≥, <, >)
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - prática intensiva!)

## Aula 28 - Biologia: Origem da Vida - 60min

### Introdução: Como a Vida Surgiu?

A **origem da vida** é uma das questões mais fascinantes da ciência. Como moléculas inanimadas deram origem a seres vivos?

**Perguntas fundamentais:**
- Quando surgiu a vida na Terra?
- Como surgiram os primeiros seres vivos?
- Quais eram as condições da Terra primitiva?

**Estimativa:** A vida surgiu há aproximadamente **3,5 bilhões de anos**.

### Teorias sobre a Origem da Vida

#### 1. Abiogênese (Geração Espontânea) - REFUTADA

**Conceito:** A vida poderia surgir espontaneamente da matéria bruta (não-viva).

**Exemplos históricos:**
- Moscas surgindo de carne podre
- Ratos nascendo de roupa suja + grãos
- Sapos surgindo da lama

**Defensores:** Aristóteles, van Helmont

**Refutação:**

**Francesco Redi (1668):**
- **Experimento:** Carne em frascos abertos vs. fechados com gaze
- **Resultado:** Moscas só apareceram nos frascos abertos (ovos depositados)
- **Conclusão:** Moscas vêm de outras moscas, não da carne

**Needham vs. Spallanzani (século XVIII):**
- **Needham:** caldo aquecido + frasco fechado → microrganismos (abiogênese?)
- **Spallanzani:** caldo fervido + frasco selado → sem microrganismos
- **Crítica a Spallanzani:** ar (princípio vital) foi excluído

**Louis Pasteur (1860s) - EXPERIMENTO DEFINITIVO:**
- **Frasco pescoço de cisne:** permite entrada de ar, mas não de microrganismos
- Caldo aquecido permanece estéril (até inclinar e tocar o "pescoço")
- **Conclusão:** Microrganismos vêm de outros microrganismos (biogênese)

**Lei da Biogênese:** Todo ser vivo origina-se de outro ser vivo preexistente.

#### 2. Panspermia Cósmica

**Conceito:** A vida na Terra veio do espaço (meteoritos, cometas).

**Argumentos:**
- Moléculas orgânicas encontradas em meteoritos
- Micro-organismos extremófilos resistem a condições extremas

**Problema:** NÃO explica a origem da vida, apenas seu transporte!

**Status:** Possível, mas não resolve a questão fundamental.

#### 3. Evolução Química (Hipótese mais aceita)

**Conceito:** A vida surgiu gradualmente por reações químicas na Terra primitiva.

**Defensores:** Oparin (URSS) e Haldane (Inglaterra), década de 1920.

**Etapas:**
1. Formação de moléculas orgânicas simples
2. Formação de moléculas complexas (proteínas, ácidos nucleicos)
3. Formação de coacervados (protocélulas)
4. Surgimento dos primeiros seres vivos

### A Terra Primitiva (há 4 bilhões de anos)

**Condições:**

1. **Atmosfera redutora (sem O₂):**
   - Composição: CH₄ (metano), NH₃ (amônia), H₂O (vapor), H₂ (hidrogênio)
   - SEM oxigênio livre (O₂)
   - SEM camada de ozônio (O₃)

2. **Intensa atividade vulcânica:**
   - Liberação de gases
   - Altas temperaturas

3. **Tempestades elétricas frequentes:**
   - Descargas elétricas constantes

4. **Radiação UV intensa:**
   - Sem proteção de ozônio

5. **Mares primitivos (sopa primordial):**
   - Água + moléculas orgânicas dissolvidas

### Experimento de Miller-Urey (1953)

**Objetivo:** Testar se moléculas orgânicas podem surgir das condições da Terra primitiva.

**Aparato:**
- Frasco com água (oceano)
- Mistura gasosa: CH₄, NH₃, H₂O, H₂ (atmosfera primitiva)
- Descargas elétricas (simulando raios)
- Aquecimento e condensação (ciclo de evaporação)

**Resultado:**
Após 1 semana, formaram-se **aminoácidos** (blocos de proteínas) e outras moléculas orgânicas.

**Conclusão:**
Moléculas orgânicas PODEM ser formadas abioticamente em condições da Terra primitiva.

**Importância:**
Demonstrou experimentalmente a viabilidade da evolução química.

**Observação:**
Descobertas recentes sugerem que a atmosfera primitiva tinha mais CO₂ e N₂, mas experimentos similares também produziram moléculas orgânicas.

### Etapas da Evolução Química

#### 1. Formação de Monômeros
Moléculas simples → aminoácidos, nucleotídeos, açúcares, ácidos graxos

**Fontes de energia:**
- Descargas elétricas (raios)
- Radiação UV
- Calor vulcânico

#### 2. Formação de Polímeros
Monômeros → proteínas, ácidos nucleicos (RNA, DNA)

**Condições:**
- Concentração em poças rasas (evaporação)
- Superfícies minerais catalíticas (argilas)

#### 3. Formação de Agregados Moleculares

**Coacervados (Oparin):**
- Aglomerados de moléculas orgânicas em meio aquoso
- Separados do meio por uma "membrana"
- Podem captar moléculas e crescer
- NÃO são seres vivos (sem material genético, reprodução)

**Microesferas proteicas (Fox):**
- Gotículas formadas por proteínas aquecidas
- Semelhantes a células primitivas

#### 4. Surgimento do Material Genético

**Problema fundamental:** O que veio primeiro, DNA ou proteínas?
- DNA precisa de proteínas (enzimas) para replicar
- Proteínas precisam de DNA para serem sintetizadas

**Hipótese do Mundo de RNA:**
- **RNA** veio primeiro (antes de DNA e proteínas)
- RNA pode:
  - Armazenar informação genética (como DNA)
  - Catalisar reações (como enzimas) → **ribozimas**
- Posteriormente, DNA (mais estável) assumiu armazenamento
- Proteínas assumiram catálise

### Primeiros Seres Vivos

**Características:**
1. **Procariontes:** sem núcleo
2. **Unicelulares:** uma única célula
3. **Anaeróbicos:** não usavam O₂ (ainda não havia)
4. **Heterotróficos:** consumiam moléculas orgânicas do ambiente

**Tipo provável:** semelhantes a bactérias primitivas

**Nutrição inicial - Heterotrofismo:**
- Consumiam moléculas orgânicas da "sopa primordial"
- Fermentação (anaeróbica)

**Surgimento da Fotossíntese - Autotrofismo:**
- Cianobactérias (há ~3,5 bilhões de anos)
- Produzem O₂ como subproduto
- **Grande Oxidação (há ~2,4 bi anos):** acúmulo de O₂ na atmosfera
- Formação da camada de ozônio

**Consequências do O₂:**
- Extinção de muitos anaeróbicos
- Surgimento da respiração aeróbica (mais eficiente)
- Proteção contra radiação UV (ozônio)

### Resumo das Teorias

```
┌────────────────┬─────────────────────────┬──────────┐
│    Teoria      │      Descrição          │  Status  │
├────────────────┼─────────────────────────┼──────────┤
│  Abiogênese    │ Geração espontânea      │ REFUTADA │
│                │ (matéria bruta→vida)    │          │
├────────────────┼─────────────────────────┼──────────┤
│  Biogênese     │ Vida vem de vida        │  ACEITA  │
│                │ (Pasteur)               │  (atual) │
├────────────────┼─────────────────────────┼──────────┤
│  Panspermia    │ Vida veio do espaço     │ Possível │
│                │                         │(não resolve)│
├────────────────┼─────────────────────────┼──────────┤
│Evolução Química│ Reações químicas        │MAIS ACEITA│
│(Oparin-Haldane)│ gradualmente→vida       │          │
└────────────────┴─────────────────────────┴──────────┘
```

### Exercícios Resolvidos

#### Exercício 1
Explique por que o experimento de Pasteur com o frasco pescoço de cisne refutou definitivamente a abiogênese.

**Resposta:**
O frasco permitia a entrada de ar (refutando a crítica de que faltava "princípio vital"), mas não de microrganismos (que ficavam presos nas curvas do pescoço). O caldo permaneceu estéril, provando que microrganismos não surgem espontaneamente, mas vêm de outros microrganismos já existentes.

#### Exercício 2
Qual a importância do experimento de Miller-Urey para a teoria da evolução química?

**Resposta:**
Demonstrou experimentalmente que moléculas orgânicas (aminoácidos) podem ser formadas abioticamente a partir de moléculas inorgânicas simples nas condições da Terra primitiva, validando a hipótese de Oparin-Haldane.

#### Exercício 3
Por que os primeiros seres vivos eram necessariamente anaeróbicos?

**Resposta:**
Porque a atmosfera primitiva não continha oxigênio livre (O₂). O oxigênio só passou a existir na atmosfera após o surgimento da fotossíntese pelas cianobactérias, há aproximadamente 3,5 bilhões de anos.

#### Exercício 4
(UFMG) Qual a principal hipótese para explicar o que surgiu primeiro: DNA, RNA ou proteínas?

**Resposta:**
**Hipótese do Mundo de RNA**: o RNA teria surgido primeiro, pois pode tanto armazenar informação genética (como DNA) quanto catalisar reações (como proteínas/enzimas), através de ribozimas.

### Dicas para a Prova

1. **Abiogênese:** REFUTADA por Pasteur
2. **Biogênese:** vida vem de vida (princípio atual)
3. **Pasteur:** frasco pescoço de cisne (definitivo)
4. **Miller-Urey:** simulou Terra primitiva, produziu aminoácidos
5. **Atmosfera primitiva:** SEM O₂ (redutora)
6. **Primeiros seres:** procariontes, unicelulares, anaeróbicos, heterotróficos
7. **Mundo de RNA:** RNA veio antes de DNA e proteínas
8. **Cianobactérias:** primeiras fotossintetizantes, produziram O₂

### Conceitos-Chave para Memorizar

**Teorias Históricas:**
- **Abiogênese:** geração espontânea (REFUTADA)
- **Biogênese:** vida de vida (ACEITA)
- **Panspermia:** vida do espaço (não explica origem)
- **Evolução Química:** Oparin-Haldane (MAIS ACEITA)

**Experimentos:**
- **Redi:** carne com gaze (moscas)
- **Pasteur:** pescoço de cisne (definitivo)
- **Miller-Urey:** Terra primitiva → aminoácidos

**Terra Primitiva:**
- Atmosfera: CH₄, NH₃, H₂O, H₂ (SEM O₂!)
- Energia: raios, UV, vulcões
- Oceanos: "sopa primordial"

**Primeiros Seres:**
- Procariontes
- Unicelulares
- Anaeróbicos
- Heterotróficos

**Sequência:**
Moléculas simples → polímeros → coacervados → material genético (RNA) → células primitivas → fotossíntese → O₂ → vida atual

### Linha do Tempo

```
4,6 bi anos: Formação da Terra
4 bi anos: Terra primitiva (atmosfera redutora)
3,5-3,8 bi anos: Primeiros seres vivos (fósseis)
3,5 bi anos: Cianobactérias (fotossíntese)
2,4 bi anos: Grande Oxidação (O₂ na atmosfera)
2 bi anos: Primeiros eucariontes
600 mi anos: Seres multicelulares
HOJE: Biodiversidade atual
```

### Resumo Visual

```
ORIGEM DA VIDA - EVOLUÇÃO QUÍMICA

Terra Primitiva (sem O₂)
        ↓
Energia (raios, UV, calor)
        ↓
Moléculas Orgânicas Simples
(aminoácidos, nucleotídeos)
        ↓
Polímeros
(proteínas, RNA, DNA)
        ↓
Coacervados/Protocélulas
(agregados moleculares)
        ↓
Primeiros Seres Vivos
(procariontes, anaeróbicos, heterotróficos)
        ↓
Fotossíntese (cianobactérias)
        ↓
O₂ na atmosfera
        ↓
Vida aeróbica + Ozônio
        ↓
Evolução da Biodiversidade

EXPERIMENTO DE PASTEUR:
    ╱╲
   │  │  ← pescoço de cisne
   │  │
   ╲  ╱
    │ │ ← caldo estéril
    └─┘
(ar entra, microrganismos não)
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - conceito fundamental de Biologia)

## Aula 29 - Ciências Humanas: Grécia e Roma Antigas - 90min

### A Civilização Grega Antiga

**Localização:** Península Balcânica (sudeste da Europa) e ilhas do Mar Egeu

**Período:** c. 2000 a.C. - 146 a.C. (conquista romana)

**Importância:** Base da civilização ocidental (filosofia, democracia, ciências, artes)

#### Períodos da História Grega

**1. Período Homérico (1200-800 a.C.)**
- Após queda da civilização micênica
- Comunidades gentílicas (genos)
- Poemas homéricos: Ilíada e Odisseia

**2. Período Arcaico (800-500 a.C.)**
- Formação das **pólis** (cidades-Estado)
- Colonização do Mediterrâneo
- Legisladores (Sólon, Draco)

**3. Período Clássico (500-338 a.C.)**
- **Apogeu da Grécia**
- Guerras Médicas (contra persas)
- Democracia ateniense
- Péricles, Sócrates, Platão, Aristóteles
- Guerra do Peloponeso (Atenas vs. Esparta)

**4. Período Helenístico (338-146 a.C.)**
- Macedônia domina Grécia (Filipe II)
- **Alexandre Magno:** imenso império
- Helenismo: fusão cultura grega + oriental
- Conquista romana (146 a.C.)

### As Pólis (Cidades-Estado)

**Pólis:** cidade-Estado independente, centro político, econômico e religioso.

**Características:**
- Independência política
- **Acrópole:** parte alta, fortificada, templos
- **Ágora:** praça pública, mercado, assembleias
- Territórios agrícolas ao redor

**Principais pólis:** Atenas e Esparta (modelos opostos)

#### Atenas: Democracia e Cultura

**Localização:** Ática (litoral)

**Economia:**
- Comércio marítimo
- Artesanato
- Agricultura (oliva, uvas)

**Sociedade:**
1. **Cidadãos:** homens livres, nascidos em Atenas (apenas eles tinham direitos políticos)
2. **Metecos:** estrangeiros (sem direitos políticos, pagavam impostos)
3. **Escravos:** maioria da população (trabalho pesado, doméstico)

**Política - Democracia Ateniense (séc. V a.C.):**

**Principais instituições:**
- **Eclésia (Assembleia):** todos os cidadãos votam leis
- **Bulé (Conselho dos 500):** prepara leis
- **Arcontes:** magistrados
- **Helieu:** tribunal popular
- **Estrategos:** comandantes militares (eleitos)

**Reformadores:**
- **Sólon (594 a.C.):** aboliu escravidão por dívidas, reformas sociais
- **Clístenes (508 a.C.):** fundador da democracia, dividiu Ática em demos
- **Péricles (461-429 a.C.):** apogeu da democracia, pagamento por cargos públicos

**IMPORTANTE:**
- Democracia **direta** (cidadãos votam diretamente)
- Mas **limitada:** só homens livres atenienses (excluía mulheres, metecos, escravos)
- ~10% da população eram cidadãos

**Cultura:**
- **Filosofia:** Sócrates, Platão, Aristóteles
- **Teatro:** Sófocles, Ésquilo, Eurípides (tragédias); Aristófanes (comédia)
- **Arquitetura:** Partenon (templo de Atena)
- **Educação:** valorização da retórica, filosofia, artes

#### Esparta: Militarismo

**Localização:** Lacônia (Peloponeso)

**Economia:**
- Agricultura (terras férteis)
- Trabalho dos hilotas (servos)

**Sociedade:**
1. **Espartanos (esparciatas):** cidadãos guerreiros (minoria)
2. **Periecos:** livres, sem direitos políticos (comércio, artesanato)
3. **Hilotas:** servos, maioria oprimida (trabalho agrícola)

**Política - Oligarquia Militar:**
- **Diarquia:** 2 reis (militares, religiosos)
- **Gerúsia:** conselho de anciãos (28 + 2 reis)
- **Ápela:** assembleia (pouco poder)
- **Éforos:** 5 magistrados (fiscalizam reis)

**Educação Espartana (Ágoge):**
- Aos 7 anos: meninos levados para treinamento militar
- Vida em comunidade, disciplina rígida
- Objetivo: formar guerreiros perfeitos
- Meninas: educação física (mães saudáveis)

**Características:**
- Sociedade militarista
- Xenofobia (isolamento)
- Disciplina extrema
- Pouca produção cultural

**Comparação Atenas vs. Esparta:**
```
┌─────────────┬──────────────┬──────────────┐
│             │    ATENAS    │   ESPARTA    │
├─────────────┼──────────────┼──────────────┤
│  Política   │  Democracia  │  Oligarquia  │
│  Economia   │   Comércio   │  Agricultura │
│  Sociedade  │   Aberta     │   Fechada    │
│  Educação   │ Artes, filos.│   Militar    │
│   Foco      │   Cultura    │   Guerra     │
└─────────────┴──────────────┴──────────────┘
```

### Legado Grego

**Filosofia:**
- Sócrates: "Conhece-te a ti mesmo"
- Platão: Teoria das Ideias, República
- Aristóteles: lógica, ética, política, ciências

**Democracia:**
- Participação dos cidadãos
- Igualdade perante a lei (isonomia)

**Ciências:**
- Pitágoras (matemática)
- Hipócrates (medicina)
- Arquimedes (física)

**Artes:**
- Teatro (tragédia, comédia)
- Escultura (proporção, beleza)
- Arquitetura (Partenon, colunas)

**Jogos Olímpicos:**
- Origem: 776 a.C., Olímpia
- Homenagem a Zeus
- Trégua sagrada durante jogos

### Civilização Romana Antiga

**Localização:** Península Itálica (Roma, às margens do Rio Tibre)

**Período:** 753 a.C. (lenda da fundação) - 476 d.C. (queda de Roma Ocidental)

#### Períodos da História Romana

**1. Monarquia (753-509 a.C.)**
- 7 reis (últimos 3 etruscos)
- Patrícios vs. Plebeus
- 509 a.C.: expulsão do último rei (Tarquínio, o Soberbo)

**2. República (509-27 a.C.)**
- Expansão territorial (Mediterrâneo)
- Guerras Púnicas (vs. Cartago) - Aníbal
- Conflito Patrícios vs. Plebeus
- Crise: Guerra Civil, triunviratos
- Júlio César assassinado (44 a.C.)

**3. Império (27 a.C. - 476 d.C.)**
- **Augusto:** primeiro imperador (27 a.C.)
- Pax Romana (paz e prosperidade)
- Expansão máxima (Trajano, séc. II)
- Crise do século III
- Divisão (395 d.C.): Ocidente e Oriente
- **476 d.C.:** queda de Roma Ocidental (invasões bárbaras)

### Sociedade Romana

**República e Império:**

1. **Patrícios:** aristocracia, grandes proprietários (minoria)
2. **Plebeus:** maioria livre (comerciantes, artesãos, pequenos agricultores)
3. **Escravos:** base da economia (prisioneiros de guerra, dívidas)
4. **Clientes:** dependentes de patrícios (proteção em troca de apoio)

**Conflito Patrícios vs. Plebeus:**
- Plebeus lutaram por direitos políticos
- **Lei das XII Tábuas (450 a.C.):** primeiras leis escritas
- **Tribunos da Plebe:** representantes dos plebeus (veto)
- Gradualmente, plebeus conquistaram igualdade jurídica

### Política Romana - República

**Instituições:**

**1. Senado:**
- ~300 membros (ex-magistrados, vitalícios)
- Controle da política externa, finanças
- Grande poder (oligarquia patrício-plebeia)

**2. Magistraturas (cursus honorum):**
- **Cônsules (2):** chefes do executivo, comandantes militares (1 ano)
- **Pretores:** justiça
- **Censores:** censo, moral pública
- **Edis:** obras públicas, jogos
- **Questores:** finanças

**3. Assembleias:**
- **Centuriata:** eleição de cônsules, declaração de guerra
- **Tributa:** leis
- **Plebeia (Concílio da Plebe):** só plebeus, elegiam tribunos

**Características:**
- República aristocrática (Senado domina)
- Sistema de freios e contrapesos
- Magistraturas anuais (evitar tirania)

### Expansão Romana

**Conquistas:**
1. **Itália** (séc. V-III a.C.)
2. **Mediterrâneo Ocidental:** Guerras Púnicas vs. Cartago (264-146 a.C.)
3. **Mediterrâneo Oriental:** Grécia, Ásia Menor, Egito (séc. II-I a.C.)
4. **Gália** (França): Júlio César (58-50 a.C.)
5. **Britânia** (Inglaterra): Império

**Consequências da expansão:**
- Afluxo de riquezas e escravos
- Concentração de terras (latifúndios)
- Empobrecimento de pequenos agricultores
- Crescimento urbano (plebe urbana)
- Crise social e política

### Legado Romano

**Direito:**
- **Direito Romano:** base dos sistemas jurídicos ocidentais
- Conceitos: pessoa jurídica, contratos, propriedade

**Língua:**
- **Latim:** origem das línguas românicas (português, espanhol, francês, italiano, romeno)

**Engenharia e Arquitetura:**
- Aquedutos, estradas (vias romanas)
- Arco, abóbada, cúpula
- Coliseu, Panteão

**Administração:**
- Organização burocrática
- Exército profissional

**Cristianismo:**
- Surgiu no Império Romano
- Oficializado (Teodósio, 380 d.C.)
- Igreja Católica (estrutura romana)

### Exercícios Resolvidos

#### Exercício 1
Compare a democracia ateniense com as democracias modernas.

**Resposta:**
**Semelhanças:** participação popular, igualdade perante a lei.

**Diferenças:**
- **Atenas:** democracia **direta** (cidadãos votam leis diretamente); **restrita** (só homens livres atenienses, ~10%)
- **Moderna:** democracia **representativa** (eleição de representantes); **universal** (todos adultos)

#### Exercício 2
Por que Esparta era considerada uma sociedade militarista?

**Resposta:**
Toda a sociedade espartana girava em torno da guerra: educação militar obrigatória desde os 7 anos (ágoge), cidadãos eram guerreiros em tempo integral, Estado controlava a vida dos cidadãos para manter superioridade militar, necessário para controlar os hilotas (servos, maioria oprimida).

#### Exercício 3
(UFMG) Qual a importância da Lei das XII Tábuas para a República Romana?

**Resposta:**
Foi a primeira codificação das leis romanas por escrito (450 a.C.), conquista dos plebeus. Antes, as leis eram orais e conhecidas apenas pelos patrícios, que as interpretavam arbitrariamente. A escrita tornou as leis públicas e conhecidas, garantindo maior igualdade jurídica.

#### Exercício 4
Explique a expressão "Roma: do Mediterrâneo ao Mare Nostrum".

**Resposta:**
**Mare Nostrum** ("Nosso Mar" em latim) era como os romanos chamavam o Mar Mediterrâneo após dominá-lo completamente. Reflete a expansão romana que transformou o Mediterrâneo em um "lago romano", com todas as suas margens sob controle de Roma.

### Dicas para a Prova

1. **Atenas:** democracia (direta, mas restrita), cultura, filosofia
2. **Esparta:** oligarquia militar, ágoge, hilotas
3. **Pólis:** cidade-Estado independente
4. **Democracia ateniense:** limitada (só homens livres atenienses)
5. **República Romana:** Senado (oligarquia), magistraturas, expansão
6. **Patrícios vs. Plebeus:** luta por direitos (Lei XII Tábuas, tribunos)
7. **Legado grego:** filosofia, democracia, ciências, artes
8. **Legado romano:** direito, latim, engenharia, administração

### Conceitos-Chave para Memorizar

**Grécia:**
- **Pólis:** cidade-Estado
- **Atenas:** democracia, cultura, comércio
- **Esparta:** oligarquia, militarismo, agricultura
- **Períodos:** Homérico, Arcaico, Clássico, Helenístico
- **Legado:** filosofia, democracia, teatro, olimpíadas

**Roma:**
- **Períodos:** Monarquia, República, Império
- **República:** Senado, magistrados, expansão
- **Sociedade:** patrícios, plebeus, escravos
- **Conflito:** patrícios vs. plebeus (Lei XII Tábuas)
- **Legado:** direito, latim, engenharia, cristianismo

### Resumo Visual

```
GRÉCIA ANTIGA:

        Pólis (cidades-Estado)
           /         \
       ATENAS       ESPARTA
     Democracia    Oligarquia
      Cultura       Militar
      Comércio     Agricultura
      
Legado: Filosofia, Democracia, Ciências, Artes

ROMA ANTIGA:

Monarquia → República → Império
(753-509)   (509-27aC)  (27aC-476dC)

República:
  Senado (poder)
  Magistrados (cônsules, pretores...)
  Assembleias
  
Sociedade:
  Patrícios × Plebeus
  Escravos (base econômica)
  
Legado: Direito, Latim, Engenharia, Cristianismo
```

### Tabela Comparativa

```
┌───────────┬──────────────┬──────────────┐
│           │    ATENAS    │   ESPARTA    │
├───────────┼──────────────┼──────────────┤
│ Governo   │  Democracia  │  Oligarquia  │
│ Economia  │   Comércio   │ Agricultura  │
│ Educação  │Artes, Filoso.│   Militar    │
│ Sociedade │    Aberta    │   Fechada    │
│ Mulheres  │   Reclusas   │ Mais livres  │
│ Valores   │Cultura, razão│ Honra, força │
└───────────┴──────────────┴──────────────┘

ROMA - PERÍODOS:
┌───────────┬────────────┬──────────────┐
│  Período  │  Governo   │  Destaque    │
├───────────┼────────────┼──────────────┤
│Monarquia  │    Reis    │  Fundação    │
│(753-509aC)│            │              │
├───────────┼────────────┼──────────────┤
│República  │   Senado   │  Expansão    │
│(509-27aC) │Magistrados │ Mediterrâneo │
├───────────┼────────────┼──────────────┤
│ Império   │ Imperadores│Apogeu+Queda  │
│(27aC-476) │            │              │
└───────────┴────────────┴──────────────┘
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - base da História Antiga)

---

# 🎉 PARABÉNS! SEMANA 1 COMPLETA! 🎉

Você concluiu as **29 aulas** da primeira semana de estudos (18/11 a 23/11)!

**Progresso:** 29/96 lições concluídas (30,2%)

**O que você estudou esta semana:**
- ✅ Matemática: Conjuntos, Razão, Notação, Álgebra, Função Afim (1 e 2), Função Quadrática, Exercícios
- ✅ Física: Vetores, MRU, MRUV, Movimento Circular, Leis de Newton
- ✅ Química: Propriedades da Matéria, Separação, Modelos Atômicos, Estrutura Atômica, Tabela Periódica, Propriedades Periódicas
- ✅ Geografia: Cartografia (1 e 2)
- ✅ Biologia: Origem da Vida
- ✅ Ciências Humanas: Antiguidade Oriental, Grécia e Roma
- ✅ Filosofia: Lógica
- ✅ Sociologia: Métodos de Pesquisa
- ✅ Português: Concordância Verbal/Nominal, Tempo e Modo Verbais

**Próximos passos:**
- Descanso no domingo (24/11)!
- Período de férias: 26/11 a 02/12 (revisão e aprofundamento)
- Semana 2: 03/12 a 07/12
- Semana 3 (final): 09/12 a 13/12
- **PROVA: 14/12 - SÁBADO**

**Continue firme nos estudos! Você está no caminho certo! 💪📚**
