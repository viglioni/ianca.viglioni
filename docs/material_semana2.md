# Material de Estudo - Período de Férias (26/11 - 02/12)

**Objetivo:** Revisão leve e aprofundamento em tópicos-chave (2h/dia)

---

# 11/26 - Férias Dia 1

## Aula 30 - Matemática: Função Quadrática - Parte 2 (Zeros, Máximo/Mínimo, Estudo do Sinal) - 90min

### Revisão: Função Quadrática Parte 1

Na Aula 26, estudamos:
- Definição: f(x) = ax² + bx + c
- Gráfico: parábola
- Concavidade (a > 0: ∪; a < 0: ∩)
- Discriminante (Δ) e número de raízes
- Fórmula de Bhaskara
- Vértice básico

**Nesta aula:** Aprofundar zeros, máximo/mínimo e estudo do sinal.

### Zeros da Função Quadrática (Revisão Aprofundada)

**Zeros (raízes):** valores de x onde f(x) = 0.

#### Métodos para Encontrar Zeros

**1. Fórmula de Bhaskara (método geral):**
```
Δ = b² - 4ac

x = (-b ± √Δ) / 2a
```

**2. Soma e Produto (Relações de Girard):**
```
x₁ + x₂ = -b/a
x₁ · x₂ = c/a
```

**Uso:** Se conhecemos a soma e produto, podemos encontrar as raízes sem Bhaskara.

**Exemplo:**
Raízes somam 7 e multiplicam 10.

x₁ + x₂ = 7
x₁ · x₂ = 10

Equação do 2º grau: x² - (soma)x + (produto) = 0
x² - 7x + 10 = 0

Raízes: 2 e 5 (verificar: 2+5=7, 2×5=10 ✓)

**3. Fatoração (quando possível):**

ax² + bx + c = a(x - x₁)(x - x₂)

**Exemplo:**
x² - 5x + 6 = 0
(x - 2)(x - 3) = 0
x = 2 ou x = 3

**4. Completamento de quadrados:**

Útil para encontrar vértice e zeros simultaneamente.

**Exemplo:**
x² - 4x + 3 = 0
x² - 4x = -3
x² - 4x + 4 = -3 + 4
(x - 2)² = 1
x - 2 = ±1
x = 3 ou x = 1

### Máximo e Mínimo da Função

O vértice da parábola é ponto de **máximo** ou **mínimo** da função.

#### Vértice: V(xᵥ, yᵥ)

**Coordenadas:**
```
xᵥ = -b / 2a

yᵥ = -Δ / 4a
ou
yᵥ = f(xᵥ)
```

**Interpretação:**

**Se a > 0 (parábola para cima ∪):**
- Vértice é ponto de **MÍNIMO**
- yᵥ = valor mínimo da função
- f(x) ≥ yᵥ para todo x

**Se a < 0 (parábola para baixo ∩):**
- Vértice é ponto de **MÁXIMO**
- yᵥ = valor máximo da função
- f(x) ≤ yᵥ para todo x

#### Imagem da Função

**Se a > 0:**
Im(f) = [yᵥ, +∞) = {y ∈ ℝ | y ≥ yᵥ}

**Se a < 0:**
Im(f) = (-∞, yᵥ] = {y ∈ ℝ | y ≤ yᵥ}

### Estudo do Sinal da Função Quadrática


```
    ESTUDO DO SINAL - FUNÇÃO QUADRÁTICA f(x) = ax² + bx + c

    Caso 1: a > 0 e Δ > 0 (duas raízes x₁ e x₂)
    
         f(x)
          │      ╱│╲
          │     ╱ │ ╲
    ──────┼────────────────── x
         x₁    xᵥ    x₂
    
    Sinal:  +  │ - │ +
            ────x₁───x₂────
            >0  =0 <0 =0 >0
    
    
    Caso 2: a > 0 e Δ = 0 (uma raiz dupla)
    
         f(x)
          │      ╱│╲
          │     ╱ │ ╲
    ──────┼─────(V)────── x
              x₁=x₂
    
    Sinal:  + │ +
            ──x₁──
            >0 =0 >0
    
    
    Caso 3: a > 0 e Δ < 0 (sem raízes)
    
         f(x)
          │      ╱╲
          │     ╱  ╲
    ──────┼─────────── x
          │   (V)
    
    Sinal: sempre +
           (f(x) > 0 para todo x)
    
    
    Caso 4: a < 0 e Δ > 0 (duas raízes)
    
         f(x)
         x₁   xᵥ   x₂
    ──────┼────────────── x
          │   ╲ │ ╱
          │    ╲│╱
    
    Sinal:  -  │ + │ -
            ────x₁───x₂────
            <0  =0 >0 =0 <0
    
    RESUMO:
    • a > 0: parábola ∪ (positivo nas "pontas")
    • a < 0: parábola ∩ (negativo nas "pontas")
    • Entre as raízes: sinal oposto ao de "a"
```


**Estudar o sinal:** determinar para quais valores de x a função é positiva, negativa ou zero.

**Método:**
1. Calcular as raízes (se existirem)
2. Observar a concavidade (sinal de a)
3. Analisar os intervalos

#### Caso 1: Δ > 0 (duas raízes distintas: x₁ e x₂)

Assumindo x₁ < x₂:

**Se a > 0 (parábola ∪):**
```
f(x) > 0: x < x₁ ou x > x₂  (fora das raízes)
f(x) = 0: x = x₁ ou x = x₂  (nas raízes)
f(x) < 0: x₁ < x < x₂        (entre as raízes)
```

**Gráfico:**
```
  +    +
  \___/
 x₁   x₂
 
 + + + 0 - - - 0 + + +
     x₁     x₂
```

**Se a < 0 (parábola ∩):**
```
f(x) > 0: x₁ < x < x₂        (entre as raízes)
f(x) = 0: x = x₁ ou x = x₂  (nas raízes)
f(x) < 0: x < x₁ ou x > x₂  (fora das raízes)
```

**Gráfico:**
```
 x₁/‾‾‾\x₂
  -    -
  
 - - - 0 + + + 0 - - -
     x₁     x₂
```

#### Caso 2: Δ = 0 (uma raiz: x₁ = x₂ = xᵥ)

**Se a > 0:**
```
f(x) > 0: x ≠ xᵥ  (para todo x exceto xᵥ)
f(x) = 0: x = xᵥ  (só no vértice)
f(x) < 0: nunca
```

**Se a < 0:**
```
f(x) > 0: nunca
f(x) = 0: x = xᵥ  (só no vértice)
f(x) < 0: x ≠ xᵥ  (para todo x exceto xᵥ)
```

#### Caso 3: Δ < 0 (sem raízes reais)

**Se a > 0:**
```
f(x) > 0: para todo x ∈ ℝ
f(x) = 0: nunca
f(x) < 0: nunca
```

**Se a < 0:**
```
f(x) > 0: nunca
f(x) = 0: nunca
f(x) < 0: para todo x ∈ ℝ
```

### Inequações do 2º Grau

Resolver inequações usando estudo do sinal.

**Tipos:**
- ax² + bx + c > 0
- ax² + bx + c ≥ 0
- ax² + bx + c < 0
- ax² + bx + c ≤ 0

**Método:**
1. Igualar a zero e encontrar raízes
2. Esboçar parábola (concavidade)
3. Identificar região pedida

**Exemplo 1:**
Resolver: x² - 5x + 6 < 0

**Passo 1: Raízes**
x² - 5x + 6 = 0
(x - 2)(x - 3) = 0
x₁ = 2, x₂ = 3

**Passo 2: Concavidade**
a = 1 > 0 → ∪

**Passo 3: Esboço**
```
  \___/
  2   3
```

**Passo 4: f(x) < 0 (região negativa)**
Entre as raízes: 2 < x < 3

*[Ver resposta 1 no final do documento]*

**Exemplo 2:**
Resolver: -x² + 4x - 3 ≥ 0

**Passo 1: Raízes**
-x² + 4x - 3 = 0
Multiplicando por -1: x² - 4x + 3 = 0
(x - 1)(x - 3) = 0
x₁ = 1, x₂ = 3

**Passo 2: Concavidade**
a = -1 < 0 → ∩

**Passo 3: Esboço**
```
 1/‾‾‾\3
  -   -
```

**Passo 4: f(x) ≥ 0 (região positiva ou zero)**
Entre as raízes (incluindo): 1 ≤ x ≤ 3

*[Ver resposta 2 no final do documento]*

### Exercícios Resolvidos

#### Exercício 1
Determine o valor máximo de f(x) = -2x² + 8x - 6.

**Solução:**
a = -2 < 0 → tem máximo

xᵥ = -8/2(-2) = -8/(-4) = 2

yᵥ = f(2) = -2(4) + 8(2) - 6 = -8 + 16 - 6 = 2

*[Ver resposta 3 no final do documento]*

#### Exercício 2
Para quais valores de x a função f(x) = x² - 6x + 8 é negativa?

**Solução:**

**Raízes:**
Δ = 36 - 32 = 4
x = (6 ± 2)/2
x₁ = 2, x₂ = 4

**Concavidade:** a = 1 > 0 → ∪

**f(x) < 0:** entre as raízes

*[Ver resposta 4 no final do documento]*

#### Exercício 3
Resolva: x² - 4x + 4 ≥ 0

**Solução:**

**Raízes:**
Δ = 16 - 16 = 0
x = 4/2 = 2 (raiz dupla)

**Concavidade:** a = 1 > 0 → ∪

**Análise:** Δ = 0 e a > 0
- Toca o eixo x apenas em x = 2
- É sempre positiva ou zero

**f(x) ≥ 0:** para todo x ∈ ℝ

*[Ver resposta 5 no final do documento]*

#### Exercício 4
(UFMG) Qual a imagem da função f(x) = x² - 4x + 5?

**Solução:**

a = 1 > 0 → mínimo

xᵥ = 4/2 = 2

yᵥ = f(2) = 4 - 8 + 5 = 1

**Imagem:** [yᵥ, +∞) = [1, +∞)

*[Ver resposta 6 no final do documento]*

#### Exercício 5
Determine para quais valores de k a função f(x) = x² - 6x + k tem valor mínimo igual a 1.

**Solução:**

a = 1 > 0 → mínimo

yᵥ = 1 (dado)

yᵥ = -Δ/4a
1 = -(b² - 4ac)/4(1)
1 = -(36 - 4k)/4
4 = -(36 - 4k)
4 = -36 + 4k
4k = 40
k = 10

*[Ver resposta 7 no final do documento]*

**Verificação:**
f(x) = x² - 6x + 10
xᵥ = 3
yᵥ = 9 - 18 + 10 = 1 ✓

### Dicas para a Prova

1. **Estudo do sinal:** raízes + concavidade
2. **Δ > 0 e a > 0:** negativa entre as raízes
3. **Δ > 0 e a < 0:** positiva entre as raízes
4. **Inequações:** use estudo do sinal
5. **Máximo:** a < 0, valor = yᵥ
6. **Mínimo:** a > 0, valor = yᵥ
7. **≥ ou ≤:** incluir raízes (colchete [])
8. **> ou <:** excluir raízes (parêntese ())

### Conceitos-Chave para Memorizar

**Vértice:**
- xᵥ = -b/2a
- yᵥ = -Δ/4a ou f(xᵥ)
- Máximo se a < 0
- Mínimo se a > 0

**Estudo do Sinal (Δ > 0):**
- a > 0: negativa entre raízes
- a < 0: positiva entre raízes

**Imagem:**
- a > 0: [yᵥ, +∞)
- a < 0: (-∞, yᵥ]

**Inequações:**
1. Encontrar raízes
2. Esboçar parábola
3. Identificar região

### Fórmulas Essenciais

```
Vértice:
xᵥ = -b / 2a
yᵥ = -Δ / 4a  ou  yᵥ = f(xᵥ)

Máximo/Mínimo:
a > 0: mínimo = yᵥ
a < 0: máximo = yᵥ

Imagem:
a > 0: Im = [yᵥ, +∞)
a < 0: Im = (-∞, yᵥ]

Estudo do Sinal (Δ > 0, x₁ < x₂):
a > 0:
  f(x) > 0: x < x₁ ou x > x₂
  f(x) < 0: x₁ < x < x₂
  
a < 0:
  f(x) > 0: x₁ < x < x₂
  f(x) < 0: x < x₁ ou x > x₂
```

### Resumo Visual

```
ESTUDO DO SINAL:

Δ > 0, a > 0 (∪):
  + + + + +
  \      /
   \____/
    x₁  x₂
    
+ 0 - - - 0 +
 x₁       x₂

Δ > 0, a < 0 (∩):
    x₁  x₂
   /‾‾‾‾\
  /      \
  - - - - -
  
- 0 + + + 0 -
 x₁       x₂

INEQUAÇÕES:
< ou >: parêntese ( )
≤ ou ≥: colchete [ ]
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - muito cobrado!)

## Aula 31 - Química: Ligações Químicas - Parte 1 (Ligação Iônica) - 30min

### Introdução: Por que Átomos se Ligam?

A maioria dos átomos na natureza **não existe isolada**, mas **ligada** a outros átomos.

**Por quê?**
- Átomos isolados geralmente são **instáveis**
- Ligações químicas levam à **estabilidade**

**Regra do Octeto (ou Teoria do Octeto):**
> Átomos tendem a ganhar, perder ou compartilhar elétrons para adquirir **8 elétrons na camada de valência** (configuração de gás nobre).

**Exceções:**
- **Hélio (He):** estável com 2 elétrons (camada K completa)
- **Hidrogênio (H):** estável com 2 elétrons (dueto)
- Alguns elementos do 3º período podem expandir octeto

**Gases Nobres:**
- Já têm 8 elétrons na valência (He tem 2)
- São **estáveis** e **inertes** (não fazem ligações facilmente)
- Exemplos: He (2), Ne (2,8), Ar (2,8,8)

### Tipos de Ligações Químicas

**Principais tipos:**
1. **Ligação Iônica** (ou eletrovalente)
2. **Ligação Covalente** (ou molecular)
3. **Ligação Metálica**

**Classificação depende:**
- Tipo de átomo envolvido (metal, não-metal, semimetal)
- Diferença de eletronegatividade

### Ligação Iônica

**Definição:** Ligação entre **metal e não-metal** através da **transferência de elétrons**.

**Características:**
- Metal **perde** elétrons → forma **cátion** (+)
- Não-metal **ganha** elétrons → forma **ânion** (-)
- Atração eletrostática entre íons de cargas opostas

**Condições:**
- Grande diferença de eletronegatividade (ΔEN ≥ 1,7)
- Metal (baixa EN) + Não-metal (alta EN)

#### Formação da Ligação Iônica

**Exemplo 1: Cloreto de Sódio (NaCl)**

**Sódio (Na, Z = 11):**
- Distribuição: 2, 8, 1
- 1 elétron na valência
- Tende a **perder 1 e⁻** → Na⁺ (2, 8) - estável

**Cloro (Cl, Z = 17):**
- Distribuição: 2, 8, 7
- 7 elétrons na valência
- Tende a **ganhar 1 e⁻** → Cl⁻ (2, 8, 8) - estável

**Ligação:**
```
Na → Na⁺ + e⁻  (perde)
Cl + e⁻ → Cl⁻  (ganha)

Na⁺ + Cl⁻ → NaCl
```

**Resultado:** Cristal iônico de NaCl (sal de cozinha)

**Exemplo 2: Óxido de Magnésio (MgO)**

**Magnésio (Mg, Z = 12):**
- Distribuição: 2, 8, 2
- Perde 2 e⁻ → Mg²⁺ (2, 8)

**Oxigênio (O, Z = 8):**
- Distribuição: 2, 6
- Ganha 2 e⁻ → O²⁻ (2, 8)

**Ligação:**
```
Mg → Mg²⁺ + 2e⁻
O + 2e⁻ → O²⁻

Mg²⁺ + O²⁻ → MgO
```

**Exemplo 3: Cloreto de Cálcio (CaCl₂)**

**Cálcio (Ca, Z = 20):**
- Distribuição: 2, 8, 8, 2
- Perde 2 e⁻ → Ca²⁺

**Cloro (Cl, Z = 17):**
- Ganha 1 e⁻ → Cl⁻

**Problema:** Ca perde 2 e⁻, mas cada Cl ganha apenas 1 e⁻!

**Solução:** **2 átomos de Cl** para 1 átomo de Ca

```
Ca → Ca²⁺ + 2e⁻
2Cl + 2e⁻ → 2Cl⁻

Ca²⁺ + 2Cl⁻ → CaCl₂
```

**Fórmula:** CaCl₂ (1 Ca para 2 Cl)

### Propriedades dos Compostos Iônicos

**1. Estado físico:**
- **Sólidos** à temperatura ambiente
- Cristais iônicos (arranjo ordenado de íons)

**2. Ponto de fusão e ebulição:**
- **Altos** (fortes atrações eletrostáticas)
- Exemplo: NaCl funde a 801°C

**3. Condutividade elétrica:**
- **Sólidos:** NÃO conduzem (íons fixos no retículo)
- **Fundidos ou dissolvidos:** CONDUZEM (íons livres)

**4. Solubilidade:**
- Geralmente **solúveis em água** (solvente polar)
- Insolúveis em solventes apolares (gasolina, etc.)

**5. Dureza:**
- Duros, mas **quebradiços** (fraturam facilmente)

### Fórmula de Compostos Iônicos

**Regra:** Número total de cargas positivas = número total de cargas negativas

**Método prático (troca de valências):**

Cátion A^(m+) + Ânion B^(n-) → A_n B_m

**Exemplos:**

1. **Al³⁺ + O²⁻**
   - Troca: Al₂O₃
   - Óxido de alumínio

2. **Fe³⁺ + S²⁻**
   - Troca: Fe₂S₃
   - Sulfeto de ferro III

3. **Na⁺ + SO₄²⁻**
   - Troca: Na₂SO₄
   - Sulfato de sódio

**Simplificação:** Se houver divisor comum, simplifique.

Exemplo: Ca²⁺ + O²⁻ → Ca₂O₂ → **CaO** (simplificado)

### Exercícios Resolvidos

#### Exercício 1
O que acontece com os átomos de sódio (Na) e cloro (Cl) ao formarem NaCl?

**Resposta:**
- **Na (2,8,1):** perde 1 elétron → Na⁺ (2,8) - cátion
- **Cl (2,8,7):** ganha 1 elétron → Cl⁻ (2,8,8) - ânion
- Formam ligação iônica por atração eletrostática entre Na⁺ e Cl⁻

#### Exercício 2
Determine a fórmula do composto formado entre alumínio (Al³⁺) e oxigênio (O²⁻).

**Solução:**
Troca de valências:
Al³⁺ → índice 2
O²⁻ → índice 3

**Fórmula:** Al₂O₃

*[Ver resposta 8 no final do documento]*

#### Exercício 3
Por que o sal de cozinha (NaCl) conduz eletricidade quando dissolvido em água, mas não no estado sólido?

**Resposta:**
- **Sólido:** íons estão fixos no retículo cristalino, não podem se mover, NÃO conduzem
- **Dissolvido:** íons ficam livres na solução, podem se mover e transportar carga, CONDUZEM eletricidade

#### Exercício 4
(UFMG) Qual o tipo de ligação entre magnésio (Mg) e cloro (Cl)?

**Resposta:**
**Ligação iônica**. 
- Mg é metal (perde elétrons)
- Cl é não-metal (ganha elétrons)
- Grande diferença de eletronegatividade
- Fórmula: MgCl₂

### Dicas para a Prova

1. **Ligação iônica:** metal + não-metal
2. **Transferência** de elétrons (não compartilhamento)
3. **Metal perde** → cátion (+)
4. **Não-metal ganha** → ânion (-)
5. **Propriedades:** sólidos, altos PF/PE, conduzem fundidos/dissolvidos
6. **Fórmula:** total de cargas + = total de cargas -
7. **Regra do octeto:** 8 elétrons na valência (estável)
8. **Gases nobres:** já estáveis (8 e⁻)

### Conceitos-Chave para Memorizar

**Ligação Iônica:**
- Metal + Não-metal
- Transferência de elétrons
- Formação de íons
- Atração eletrostática

**Íons:**
- **Cátion:** íon positivo (perdeu e⁻)
- **Ânion:** íon negativo (ganhou e⁻)

**Propriedades:**
- Sólidos cristalinos
- Altos PF e PE
- Conduzem fundidos/dissolvidos
- Solúveis em água

**Fórmula:**
- Troca de valências
- Cargas balanceadas

### Resumo Visual

```
LIGAÇÃO IÔNICA:

Metal (baixa EN)  +  Não-metal (alta EN)
        ↓                    ↓
    Perde e⁻            Ganha e⁻
        ↓                    ↓
     Cátion⁺              Ânion⁻
        ↓                    ↓
        └────────┬───────────┘
          Atração eletrostática
                 ↓
          Composto Iônico

Exemplo:
Na (2,8,1) → Na⁺ (2,8) + e⁻
Cl (2,8,7) + e⁻ → Cl⁻ (2,8,8)

Na⁺ + Cl⁻ → NaCl

Propriedades:
├─ Sólidos (cristais)
├─ Altos PF/PE
├─ Conduzem fundidos/dissolvidos
└─ Solúveis em H₂O
```

---

**Tempo de estudo recomendado:** 30 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - ligações são fundamentais!)

# 11/27 - Férias Dia 2

## Aula 32 - Matemática: Função Quadrática - Parte 3 (Inequações e Sistemas) - 90min

### Revisão: Função Quadrática

Já estudamos:
- **Parte 1 (Aula 26):** Definição, gráfico, raízes (Bhaskara), vértice
- **Parte 2 (Aula 30):** Zeros, máximo/mínimo, estudo do sinal básico

**Nesta aula:** Inequações mais complexas e sistemas envolvendo função quadrática.

### Inequações do 2º Grau - Aprofundamento

#### Inequações-Produto

**Formato:** (ax² + bx + c)(dx² + ex + f) > 0 (ou <, ≥, ≤)

**Método:**
1. Estudar o sinal de cada fator separadamente
2. Fazer quadro de sinais
3. Multiplicar os sinais
4. Responder conforme pedido

**Exemplo:**
(x² - 4)(x² - 9) ≤ 0

**Passo 1: Estudar cada fator**

**Fator 1:** x² - 4
- Raízes: x = ±2
- a = 1 > 0 (∪)
- Sinal: + | - | +
         -2   2

**Fator 2:** x² - 9
- Raízes: x = ±3
- a = 1 > 0 (∪)
- Sinal: + | - | +
         -3   3

**Passo 2: Quadro de sinais**
```
        -3   -2    2    3
x²-4:   +    +  0  -  0  +  +
x²-9:   +  0 -    -    -  0  +
────────────────────────────────
Produto: + 0 -  0  +  0  - 0  +
```

**Passo 3: Produto ≤ 0** (negativo ou zero)

Intervalos: [-3, -2] ∪ [2, 3]

*[Ver resposta 9 no final do documento]*

#### Inequações-Quociente

**Formato:** (ax² + bx + c)/(dx² + ex + f) > 0

**Método:**
1. Estudar sinal do numerador
2. Estudar sinal do denominador
3. Quadro de sinais (dividir sinais)
4. **IMPORTANTE:** Denominador ≠ 0 (excluir raízes do denominador)

**Exemplo:**
(x² - 1)/(x² - 4) ≥ 0

**Numerador:** x² - 1
- Raízes: x = ±1
- a = 1 > 0
- Sinal: + | - | +
         -1   1

**Denominador:** x² - 4
- Raízes: x = ±2 (EXCLUIR da resposta!)
- a = 1 > 0
- Sinal: + | - | +
         -2   2

**Quadro:**
```
          -2   -1    1    2
Numer.:   +    + 0  - 0  +    +
Denom.:   + ≠0 -    -    - ≠0 +
────────────────────────────────
Quoc.:    +  ∅ - 0  + 0  -  ∅  +
```

**Quociente ≥ 0:** positivo ou zero

*[Ver resposta 10 no final do documento]*

**Observe:** -2 e 2 EXCLUÍDOS (denominador zero), -1 e 1 INCLUÍDOS (numerador zero)

#### Inequações Simultâneas

**Formato:** Sistema de inequações

**Exemplo:**
```
{ x² - 5x + 6 < 0
{ x² - 4 ≥ 0
```

**Resolver cada uma:**

**1ª inequação:** x² - 5x + 6 < 0
- Raízes: 2 e 3
- a > 0 → negativa entre raízes
- S₁ = (2, 3)

**2ª inequação:** x² - 4 ≥ 0
- Raízes: -2 e 2
- a > 0 → positiva fora raízes (ou nas raízes)
- S₂ = (-∞, -2] ∪ [2, +∞)

**Interseção S₁ ∩ S₂:**
```
S₁:    ═══════(───)═══════
              2   3
              
S₂: ══════]       [════════
         -2       2
         
S₁∩S₂:          [─)
                2 3
```

*[Ver resposta 11 no final do documento]*

### Sistemas de Equações do 2º Grau

#### Sistema Linear-Quadrático

**Formato:**
```
{ y = ax + b         (reta)
{ y = cx² + dx + e   (parábola)
```

**Método:** Substituição

**Exemplo:**
```
{ y = 2x + 1
{ y = x² - 2x + 3
```

**Substituição:**
2x + 1 = x² - 2x + 3
0 = x² - 4x + 2
x² - 4x + 2 = 0

**Bhaskara:**
Δ = 16 - 8 = 8
x = (4 ± √8)/2 = (4 ± 2√2)/2 = 2 ± √2

x₁ = 2 + √2
x₂ = 2 - √2

**Encontrar y:**
y₁ = 2(2 + √2) + 1 = 5 + 2√2
y₂ = 2(2 - √2) + 1 = 5 - 2√2

**Soluções:**
- (2 + √2, 5 + 2√2)
- (2 - √2, 5 - 2√2)

**Interpretação geométrica:** Pontos onde a reta intercepta a parábola.

#### Sistema Quadrático-Quadrático

**Formato:**
```
{ y = ax² + bx + c
{ y = dx² + ex + f
```

**Exemplo:**
```
{ y = x² - 4
{ y = -x² + 2x + 4
```

**Igualando:**
x² - 4 = -x² + 2x + 4
2x² - 2x - 8 = 0
x² - x - 4 = 0

Δ = 1 + 16 = 17
x = (1 ± √17)/2

E assim por diante...

### Aplicações - Problemas Contextualizados

#### Problema 1: Geometria
Um retângulo tem perímetro 20 cm e área 24 cm². Quais suas dimensões?

**Solução:**

Sejam x e y os lados.

```
{ 2x + 2y = 20  →  x + y = 10  →  y = 10 - x
{ xy = 24
```

Substituindo:
x(10 - x) = 24
10x - x² = 24
x² - 10x + 24 = 0

Fatorando:
(x - 4)(x - 6) = 0
x = 4 ou x = 6

Se x = 4: y = 6
Se x = 6: y = 4

*[Ver resposta 12 no final do documento]*

#### Problema 2: Movimento (Física)
Um projétil é lançado verticalmente. Sua altura h(t) em metros no tempo t (segundos) é dada por:

h(t) = -5t² + 20t + 5

a) Qual a altura máxima?
b) Quando atinge o solo (h = 0)?

**Solução:**

a) **Altura máxima = yᵥ**

a = -5, b = 20, c = 5

tᵥ = -20/2(-5) = 20/10 = 2 s

hᵥ = -5(4) + 20(2) + 5 = -20 + 40 + 5 = 25 m

**Máxima: 25 m** (em t = 2 s)

b) **h = 0:**

-5t² + 20t + 5 = 0
t² - 4t - 1 = 0

Δ = 16 + 4 = 20

t = (4 ± √20)/2 = (4 ± 2√5)/2 = 2 ± √5

t₁ = 2 - √5 ≈ -0,24 s (descartado: negativo)
t₂ = 2 + √5 ≈ 4,24 s ✓

*[Ver resposta 13 no final do documento]*

#### Problema 3: Economia
Uma empresa descobriu que o lucro L (em mil reais) ao vender x unidades é dado por:

L(x) = -x² + 40x - 300

a) Quantas unidades deve vender para lucro máximo?
b) Qual o lucro máximo?
c) Para quais quantidades há prejuízo (L < 0)?

**Solução:**

a = -1, b = 40, c = -300

a) **xᵥ = -40/2(-1) = 20 unidades**

b) **Lᵥ = -(20)² + 40(20) - 300**
   = -400 + 800 - 300 = 100

**Lucro máximo: 100 mil reais**

c) **L < 0:**

Raízes:
Δ = 1600 - 1200 = 400
x = (40 ± 20)/2
x₁ = 10, x₂ = 30

a = -1 < 0 (∩): negativa fora das raízes

**Prejuízo:** x < 10 ou x > 30

Mas x ≥ 0 (não há quantidade negativa):

*[Ver resposta 14 no final do documento]*

### Exercícios Resolvidos

#### Exercício 1
Resolva: (x - 2)(x² - 9) > 0

**Solução:**

**Fator 1:** x - 2
- Raiz: x = 2
- Sinal: - | +
          2

**Fator 2:** x² - 9
- Raízes: x = ±3
- Sinal: + | - | +
         -3   3

**Quadro:**
```
      -3    2    3
x-2:  -  -  -  0 +  +
x²-9: + 0 -    - 0 +
──────────────────────
Prod: - 0 +  0 - 0 +
```

**Produto > 0:** (-3, 2) ∪ (3, +∞)

*[Ver resposta 15 no final do documento]*

#### Exercício 2
Resolva: (x² - 4)/(x - 3) ≤ 0

**Solução:**

**Numerador:** x² - 4
- Raízes: ±2
- Sinal: + | - | +
         -2   2

**Denominador:** x - 3
- Raiz: 3 (EXCLUIR)
- Sinal: - | +
          3

**Quadro:**
```
      -2    2    3
Num.: + 0 - 0 +    +
Den.: -   -   - ≠0 +
──────────────────────
Quo.: - 0 + 0 -  ∅  +
```

**Quociente ≤ 0:** [-2, 2] ∪ (2, 3)

Simplificando: [-2, 2] ∪ (2, 3) = [-2, 3)

*[Ver resposta 16 no final do documento]*

(3 excluído pois anula denominador)

#### Exercício 3
Determine os pontos de interseção de y = x² e y = 2x + 3.

**Solução:**

x² = 2x + 3
x² - 2x - 3 = 0
(x - 3)(x + 1) = 0
x = 3 ou x = -1

**Para x = 3:** y = 9
**Para x = -1:** y = 1

*[Ver resposta 17 no final do documento]*

### Dicas para a Prova

1. **Inequação-produto:** quadro de sinais e multiplicar
2. **Inequação-quociente:** EXCLUIR raízes do denominador
3. **≥ ou ≤:** incluir raízes do numerador (não do denominador!)
4. **Sistema simultâneo:** interseção das soluções
5. **Problema contextualizado:** montar função a partir do enunciado
6. **Máximo/mínimo:** sempre vértice (yᵥ)
7. **Geometria:** cuidado com dimensões positivas
8. **Física:** tempo negativo não tem sentido (descartar)

### Conceitos-Chave para Memorizar

**Inequação-Produto:**
- Quadro de sinais
- Multiplicar sinais dos fatores

**Inequação-Quociente:**
- Dividir sinais
- Denominador ≠ 0 (excluir da resposta)

**Sistema Linear-Quadrático:**
- Substituição
- 0, 1 ou 2 soluções

**Problemas:**
- Identificar variáveis
- Montar equação/sistema
- Resolver
- Interpretar (descartar soluções sem sentido físico)

### Fórmulas Essenciais

```
Quadro de Sinais:
1. Encontrar raízes de cada fator
2. Determinar sinal de cada fator
3. Combinar sinais (× para produto, ÷ para quociente)
4. Ler região pedida

Inequação-Quociente:
Numerador = 0: pode incluir (se ≥ ou ≤)
Denominador = 0: SEMPRE excluir (∅)

Sistema de Inequações:
Resolver cada uma → Interseção S₁ ∩ S₂

Aplicações:
- Perímetro retângulo: 2(x + y)
- Área retângulo: xy
- Altura projétil: h(t) = -gt²/2 + v₀t + h₀
```

### Resumo Visual

```
INEQUAÇÃO-PRODUTO: (f₁)(f₂) > 0

        raízes f₁  raízes f₂
f₁:     ─────0────0─────
f₂:     ──0─────────0───
        ───────────────
Prod:   [combinar sinais]

INEQUAÇÃO-QUOCIENTE: f₁/f₂ ≥ 0

Num:    ────0────0────  (pode incluir)
Den:    ──≠0────────≠0  (EXCLUIR sempre)
        ──────────────
Quo:    [dividir sinais]

SISTEMA:
S₁:  ════(────)════
S₂:  ══════[──────)══

S₁∩S₂:    [──)  (interseção)
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - inequações sempre caem!)

## Aula 33 - Química: Ligações Químicas - Parte 2 (Ligação Covalente) - 30min

### Revisão: Ligações Químicas

Na Aula 31, estudamos:
- **Ligação Iônica:** metal + não-metal, transferência de elétrons, íons

**Nesta aula:** Ligação Covalente (molecular)

### Ligação Covalente

**Definição:** Ligação entre **não-metais** através do **compartilhamento de elétrons**.

**Características:**
- Não-metal + Não-metal
- **Compartilham** elétrons (não transferem)
- Formam **moléculas**
- Pequena diferença de eletronegatividade (ΔEN < 1,7)

**Objetivo:** Ambos os átomos atingem configuração de gás nobre (regra do octeto ou dueto).

### Formação da Ligação Covalente

#### Exemplo 1: Hidrogênio (H₂)

**H (Z = 1):**
- Distribuição: 1
- Precisa de 1 elétron para completar (dueto: 2 elétrons)

**Ligação:**
```
H • + • H  →  H : H  ou  H─H
```

Cada H compartilha 1 elétron → ambos ficam com 2 elétrons (estáveis)

**Fórmula molecular:** H₂

**Fórmula estrutural:** H─H (traço = par de elétrons compartilhado)

#### Exemplo 2: Cloro (Cl₂)

**Cl (Z = 17):**
- Distribuição: 2, 8, 7
- Precisa de 1 elétron para completar octeto (8)

**Representação de Lewis:**
```
:Cl· + ·Cl:  →  :Cl:Cl:  ou  Cl─Cl
```

Cada Cl compartilha 1 elétron → ambos com 8 elétrons na valência

**Fórmula molecular:** Cl₂

#### Exemplo 3: Água (H₂O)

**O (Z = 8):**
- Distribuição: 2, 6
- Precisa de 2 elétrons

**H:**
- Precisa de 1 elétron (cada)

**Ligação:**
```
    ·O·
   H   H
   
Cada H compartilha 1 elétron com O
O compartilha 2 elétrons (1 com cada H)
```

**Fórmula estrutural:**
```
  H─O─H
```

O tem 8 elétrons (2 ligações + 4 não-ligantes)
Cada H tem 2 elétrons

#### Exemplo 4: Amônia (NH₃)

**N (Z = 7):**
- Distribuição: 2, 5
- Precisa de 3 elétrons

**H:** precisa de 1 (cada um)

**Fórmula estrutural:**
```
    H
    │
  H─N─H
```

N faz 3 ligações (compartilha 6 elétrons) + 2 não-ligantes = 8 total

#### Exemplo 5: Metano (CH₄)

**C (Z = 6):**
- Distribuição: 2, 4
- Precisa de 4 elétrons

**Fórmula estrutural:**
```
    H
    │
  H─C─H
    │
    H
```

C faz 4 ligações → 8 elétrons (octeto completo)

### Tipos de Ligações Covalentes

#### 1. Ligação Simples
Um par de elétrons compartilhado.

**Representação:** A─B

**Exemplos:**
- H─H
- Cl─Cl
- H─O─H

#### 2. Ligação Dupla
Dois pares de elétrons compartilhados.

**Representação:** A═B

**Exemplo: Oxigênio (O₂)**

**O:** 2, 6 (precisa de 2 elétrons)

```
:O::O:  ou  O═O
```

Cada O compartilha 2 elétrons (4 no total) → ligação dupla

#### 3. Ligação Tripla
Três pares de elétrons compartilhados.

**Representação:** A≡B

**Exemplo: Nitrogênio (N₂)**

**N:** 2, 5 (precisa de 3 elétrons)

```
:N:::N:  ou  N≡N
```

Cada N compartilha 3 elétrons (6 no total) → ligação tripla

**Outro exemplo: Gás carbônico (CO₂)**

```
O═C═O
```

C faz duas ligações duplas (4 pares = 8 elétrons)

### Polaridade das Ligações Covalentes

#### Ligação Covalente Apolar

**Condição:** ΔEN = 0 (átomos iguais ou eletronegatividades iguais)

**Características:**
- Elétrons compartilhados **igualmente**
- Sem polo positivo/negativo

**Exemplos:**
- H₂, O₂, N₂, Cl₂ (moléculas diatômicas iguais)
- CH₄ (simetria molecular)

#### Ligação Covalente Polar

**Condição:** 0 < ΔEN < 1,7 (átomos diferentes)

**Características:**
- Elétrons compartilhados **desigualmente**
- Átomo mais eletronegativo "puxa" mais os elétrons
- Forma **polos:** δ⁺ (parcialmente positivo) e δ⁻ (parcialmente negativo)

**Exemplos:**
- **HCl:** Cl mais eletronegativo → H^(δ+)─Cl^(δ-)
- **H₂O:** O mais eletronegativo → H^(δ+)─O^(δ-)─H^(δ+)

**Dipolo elétrico:** representado por seta → apontando para polo negativo

```
H → Cl
  ↑
 dipolo
```

### Geometria Molecular (Introdução)

A **forma tridimensional** da molécula influencia propriedades.

**Exemplos:**

**Linear:** CO₂ (O═C═O) - 180°

**Angular:** H₂O
```
  H
   \
    O  (104,5°)
   /
  H
```

**Trigonal plana:** BF₃ - 120°

**Tetraédrica:** CH₄
```
    H
    │
  H─C─H  (109,5°)
    │
    H
```

**Piramidal:** NH₃

(Aprofundaremos geometria em aulas futuras)

### Propriedades dos Compostos Covalentes (Moleculares)

**1. Estado físico:**
- **Gases** ou **líquidos** à temperatura ambiente (maioria)
- Alguns sólidos (açúcar, gelo)

**2. Ponto de fusão e ebulição:**
- **Baixos** (forças intermoleculares fracas)
- Exceção: macromoléculas (diamante, quartzo)

**3. Condutividade elétrica:**
- **NÃO conduzem** (não têm íons livres)
- Exceção: grafite (estrutura especial)

**4. Solubilidade:**
- Polares: solúveis em solventes polares (água)
- Apolares: solúveis em solventes apolares (gasolina)
- "Semelhante dissolve semelhante"

### Comparação: Ligação Iônica vs. Covalente

```
┌──────────────┬──────────────┬──────────────┐
│              │    IÔNICA    │  COVALENTE   │
├──────────────┼──────────────┼──────────────┤
│ Átomos       │Metal+Não-met.│Não-metal+Não │
│ Processo     │ Transferência│Compartilhamento│
│ Formam       │    Íons      │  Moléculas   │
│ Estado físico│   Sólidos    │ Gases/Líquidos│
│ PF/PE        │    Altos     │    Baixos    │
│ Condutividade│Fund/Dissol.  │  Não conduz  │
│ Exemplo      │    NaCl      │     H₂O      │
└──────────────┴──────────────┴──────────────┘
```

### Exercícios Resolvidos

#### Exercício 1
Represente a fórmula estrutural do F₂ (Z do F = 9).

**Solução:**

F: 2, 7 (precisa de 1 elétron)

```
:F: + :F:  →  :F:F:  ou  F─F
```

*[Ver resposta 18 no final do documento]*

#### Exercício 2
Quantas ligações o carbono faz na molécula CO₂?

**Solução:**

C: 2, 4 (precisa de 4 elétrons = 4 ligações)

Estrutura: O═C═O

C faz **2 ligações duplas** (total: 4 ligações)

*[Ver resposta 19 no final do documento]*

#### Exercício 3
A ligação H─Cl é polar ou apolar? Por quê?

**Solução:**

H e Cl são átomos **diferentes**
Cl é **mais eletronegativo** que H
ΔEN > 0

*[Ver resposta 20 no final do documento]*

#### Exercício 4
(UFMG) Qual o tipo de ligação em cada substância:
a) NaCl
b) H₂
c) CaO

**Solução:**

a) **NaCl:** Na (metal) + Cl (não-metal) → **Iônica**

b) **H₂:** H + H (não-metais iguais) → **Covalente apolar**

c) **CaO:** Ca (metal) + O (não-metal) → **Iônica**

### Dicas para a Prova

1. **Ligação covalente:** não-metal + não-metal
2. **Compartilhamento** de elétrons (não transferência)
3. **Ligação simples:** 1 par (─)
4. **Ligação dupla:** 2 pares (═)
5. **Ligação tripla:** 3 pares (≡)
6. **Apolar:** ΔEN = 0 (átomos iguais ou simétricos)
7. **Polar:** 0 < ΔEN < 1,7 (átomos diferentes)
8. **Propriedades:** baixos PF/PE, não conduzem

### Conceitos-Chave para Memorizar

**Ligação Covalente:**
- Não-metal + Não-metal
- Compartilhamento de elétrons
- Formam moléculas

**Tipos:**
- Simples: ─ (1 par)
- Dupla: ═ (2 pares)
- Tripla: ≡ (3 pares)

**Polaridade:**
- Apolar: ΔEN = 0
- Polar: 0 < ΔEN < 1,7

**Propriedades (molecular):**
- Baixos PF/PE
- Gases ou líquidos
- Não conduzem eletricidade

### Resumo Visual

```
LIGAÇÃO COVALENTE:

Não-metal  +  Não-metal
     ↓            ↓
 Compartilham elétrons
          ↓
      Moléculas

Exemplos:
H · + · H  →  H:H  →  H─H  (H₂)

:Cl· + ·Cl: → :Cl:Cl: → Cl─Cl (Cl₂)

·Ö· + H + H → H:Ö:H → H─O─H (H₂O)
              

Tipos de Ligação:
Simples:  A─B   (1 par)
Dupla:    A═B   (2 pares)
Tripla:   A≡B   (3 pares)

Polaridade:
Apolar:  H─H  (ΔEN = 0)
         Cl─Cl

Polar:   H^δ+─Cl^δ-  (ΔEN > 0)
         H^δ+─O^δ-─H^δ+
```

---

**Tempo de estudo recomendado:** 30 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - ligação covalente é fundamental!)

# 11/28 - Férias Dia 3

## Aula 34 - Matemática: Função Exponencial - Parte 1 (Potenciação e Propriedades) - 90min

### Introdução: Crescimento Exponencial

**Problemas que envolvem crescimento/decrescimento muito rápido:**
- População de bactérias (duplica a cada hora)
- Juros compostos (dinheiro cresce exponencialmente)
- Desintegração radioativa (decaimento exponencial)

Esses fenômenos são modelados por **funções exponenciais**.

### Revisão: Potenciação

#### Definição

**Potência:** a^n (a elevado a n)
- **Base:** a
- **Expoente:** n
- **Resultado:** potência

**Exemplos:**
- 2³ = 2 × 2 × 2 = 8
- 5² = 5 × 5 = 25
- 10⁴ = 10.000

#### Casos Especiais

**Expoente zero:**
```
a⁰ = 1  (para a ≠ 0)
```

Exemplos: 5⁰ = 1, 100⁰ = 1

**Expoente um:**
```
a¹ = a
```

**Expoente negativo:**
```
a^(-n) = 1/a^n
```

Exemplos:
- 2^(-3) = 1/2³ = 1/8
- 5^(-2) = 1/5² = 1/25

**Expoente fracionário:**
```
a^(m/n) = ⁿ√(a^m)
```

Exemplos:
- 4^(1/2) = √4 = 2
- 8^(2/3) = ³√(8²) = ³√64 = 4
- 27^(1/3) = ³√27 = 3

### Propriedades da Potenciação

#### 1. Multiplicação de Mesma Base
```
a^m × a^n = a^(m+n)
```

**Exemplos:**
- 2³ × 2² = 2^(3+2) = 2⁵ = 32
- x⁴ × x³ = x⁷

**Regra:** Mantém a base, soma os expoentes.

#### 2. Divisão de Mesma Base
```
a^m / a^n = a^(m-n)
```

**Exemplos:**
- 5⁷ / 5⁴ = 5^(7-4) = 5³ = 125
- x⁸ / x³ = x⁵

**Regra:** Mantém a base, subtrai os expoentes.

#### 3. Potência de Potência
```
(a^m)^n = a^(m×n)
```

**Exemplos:**
- (2³)² = 2^(3×2) = 2⁶ = 64
- (x²)⁵ = x^(2×5) = x¹⁰

**Regra:** Mantém a base, multiplica os expoentes.

#### 4. Potência de Produto
```
(a × b)^n = a^n × b^n
```

**Exemplos:**
- (2 × 3)² = 2² × 3² = 4 × 9 = 36
- (xy)³ = x³y³

#### 5. Potência de Quociente
```
(a/b)^n = a^n / b^n
```

**Exemplos:**
- (2/3)² = 2²/3² = 4/9
- (x/y)⁴ = x⁴/y⁴

### Equações Exponenciais Simples

**Equação exponencial:** incógnita no expoente.

**Formato:** a^x = b

#### Método 1: Bases Iguais

Se conseguirmos escrever ambos os lados com a mesma base:

```
a^x = a^y  →  x = y
```

**Exemplo 1:**
2^x = 8

8 = 2³

2^x = 2³

**x = 3**

**Exemplo 2:**
5^(x+1) = 25

25 = 5²

5^(x+1) = 5²

x + 1 = 2

**x = 1**

**Exemplo 3:**
3^(2x) = 1/9

1/9 = 1/3² = 3^(-2)

3^(2x) = 3^(-2)

2x = -2

**x = -1**

**Exemplo 4:**
4^x = 32

Bases diferentes, mas podem ser escritas como potências de 2:

4 = 2²
32 = 2⁵

(2²)^x = 2⁵

2^(2x) = 2⁵

2x = 5

**x = 5/2**

#### Casos com Soma/Produto no Expoente

**Exemplo 5:**
2^(x+2) = 2^x + 12

Não podemos igualar expoentes diretamente!

**Estratégia:** Fatorar

2^(x+2) = 2^x × 2² = 4 × 2^x

4 × 2^x = 2^x + 12

4 × 2^x - 2^x = 12

3 × 2^x = 12

2^x = 4

2^x = 2²

**x = 2**

### Inequações Exponenciais Simples

**Formato:** a^x > b (ou <, ≥, ≤)

**Regra depende da base:**

**Se a > 1:** função crescente
- a^x > a^y  →  x > y

**Se 0 < a < 1:** função decrescente
- a^x > a^y  →  x < y (inverte!)

**Exemplo 1:**
2^x > 8

2^x > 2³

Base 2 > 1 (crescente) → mantém sinal

**x > 3**

**Exemplo 2:**
(1/2)^x ≥ 4

(1/2)^x ≥ (1/2)^(-2)

Base 1/2 < 1 (decrescente) → **inverte** sinal

**x ≤ -2**

### Gráfico da Função Exponencial (Introdução)

**Função exponencial:** f(x) = a^x  (a > 0, a ≠ 1)

#### Caso 1: a > 1 (Crescente)

**Exemplo:** f(x) = 2^x

```
x  | f(x)
-2 | 1/4
-1 | 1/2
 0 | 1
 1 | 2
 2 | 4
 3 | 8
```

**Gráfico:**
```
     |
   8 |         •
   4 |       •
   2 |     •
   1 |   •─────────
 1/2 | •
     |______________
     -2  0  2
```

**Características:**
- **Crescente**
- Passa por (0, 1)
- Eixo x é **assíntota horizontal** (nunca toca)
- Sempre positiva (f(x) > 0)

#### Caso 2: 0 < a < 1 (Decrescente)

**Exemplo:** f(x) = (1/2)^x

```
x  | f(x)
-2 | 4
-1 | 2
 0 | 1
 1 | 1/2
 2 | 1/4
```

**Gráfico:**
```
     |
   4 | •
   2 |  •
   1 |───•─────
 1/2 |     •
     |       •
     |______________
     -2  0  2
```

**Características:**
- **Decrescente**
- Passa por (0, 1)
- Eixo x é assíntota
- Sempre positiva

### Exercícios Resolvidos

#### Exercício 1
Calcule:
a) 2⁵
b) 3^(-2)
c) 16^(1/2)

**Soluções:**

a) 2⁵ = 2 × 2 × 2 × 2 × 2 = 32

b) 3^(-2) = 1/3² = 1/9

c) 16^(1/2) = √16 = 4

*[Ver resposta 21 no final do documento]*

#### Exercício 2
Simplifique: 2⁷ × 2³ / 2⁴

**Solução:**

= 2^(7+3) / 2⁴
= 2¹⁰ / 2⁴
= 2^(10-4)
= 2⁶
= 64

*[Ver resposta 22 no final do documento]*

#### Exercício 3
Resolva: 3^x = 81

**Solução:**

81 = 3⁴

3^x = 3⁴

**x = 4**

#### Exercício 4
Resolva: 2^(x-1) = 1/8

**Solução:**

1/8 = 1/2³ = 2^(-3)

2^(x-1) = 2^(-3)

x - 1 = -3

**x = -2**

#### Exercício 5
Resolva a inequação: 5^x < 125

**Solução:**

125 = 5³

5^x < 5³

Base 5 > 1 (crescente) → mantém sinal

**x < 3**

*[Ver resposta 23 no final do documento]*

#### Exercício 6
Simplifique: (x²y³)² / (xy)⁴

**Solução:**

= (x²)²(y³)² / x⁴y⁴
= x⁴y⁶ / x⁴y⁴
= x^(4-4) y^(6-4)
= x⁰y²
= y²

*[Ver resposta 24 no final do documento]*

### Dicas para a Prova

1. **a⁰ = 1** (sempre)
2. **a^(-n) = 1/a^n** (expoente negativo = inverso)
3. **Multiplicação:** soma expoentes (mesma base)
4. **Divisão:** subtrai expoentes
5. **(a^m)^n = a^(m×n)**
6. **Equação a^x = a^y:** x = y
7. **Inequação e a > 1:** mantém sinal
8. **Inequação e 0 < a < 1:** inverte sinal
9. **Gráfico:** sempre passa por (0, 1)

### Conceitos-Chave para Memorizar

**Potenciação:**
- a^n = a × a × ... × a (n vezes)
- a⁰ = 1
- a^(-n) = 1/a^n
- a^(m/n) = ⁿ√(a^m)

**Propriedades (mesma base):**
- a^m × a^n = a^(m+n)
- a^m / a^n = a^(m-n)
- (a^m)^n = a^(m×n)

**Equação Exponencial:**
- a^x = a^y → x = y

**Inequação:**
- a > 1: crescente (mantém sinal)
- 0 < a < 1: decrescente (inverte sinal)

**Gráfico:**
- Passa por (0, 1)
- Sempre f(x) > 0
- Eixo x é assíntota

### Fórmulas Essenciais

```
Propriedades de Potenciação:
a^m × a^n = a^(m+n)
a^m / a^n = a^(m-n)
(a^m)^n = a^(mn)
(ab)^n = a^n b^n
(a/b)^n = a^n / b^n

Casos Especiais:
a⁰ = 1
a¹ = a
a^(-n) = 1/a^n
a^(1/n) = ⁿ√a
a^(m/n) = ⁿ√(a^m)

Equação:
a^x = a^y  ⟹  x = y

Inequação:
a > 1:     a^x > a^y  ⟹  x > y
0 < a < 1: a^x > a^y  ⟹  x < y
```

### Resumo Visual

```
PROPRIEDADES:

Multiplicação:    Divisão:
2³ × 2² = 2⁵     2⁵ / 2² = 2³
↑soma expoentes   ↑subtrai

Potência de Potência:
(2³)² = 2⁶
    ↑multiplica

GRÁFICOS:

a > 1 (crescente):   0 < a < 1 (decresc.):
     |                     |
   • |                   • |
  •  |(0,1)        (0,1)|  •
 •───•                 •───• 
     |                     |
─────┼─────           ─────┼─────
     
Sempre > 0           Sempre > 0
Passa por (0,1)      Passa por (0,1)
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - função exponencial é muito cobrada!)

## Aula 35 - Química: Ligações Químicas - Parte 3 (Ligação Metálica) - 30min

### Revisão: Ligações Químicas

Já estudamos:
- **Aula 31:** Ligação Iônica (metal + não-metal, transferência)
- **Aula 33:** Ligação Covalente (não-metal + não-metal, compartilhamento)

**Nesta aula:** Ligação Metálica

### Ligação Metálica

**Definição:** Ligação entre **átomos de metais**, formando estruturas sólidas metálicas.

**Onde ocorre:**
- Metais puros: Fe, Cu, Au, Ag, Al, Na, etc.
- Ligas metálicas: bronze (Cu + Sn), aço (Fe + C), latão (Cu + Zn)

### Modelo do "Mar de Elétrons"

**Teoria:**
- Átomos metálicos perdem elétrons da camada de valência
- Formam **cátions** (+) fixos em posições
- Elétrons livres ("deslocalizados") movem-se livremente
- **"Mar de elétrons":** elétrons circulam entre os cátions

**Representação:**
```
  ⁺   ⁺   ⁺   ⁺
 e⁻ e⁻ e⁻ e⁻ e⁻
  ⁺   ⁺   ⁺   ⁺
 e⁻ e⁻ e⁻ e⁻ e⁻
  ⁺   ⁺   ⁺   ⁺
```

**Cátions (+):** núcleos dos átomos metálicos
**e⁻:** elétrons livres, móveis

**Atração:**
- Cátions (+) atraem elétrons (-)
- Elétrons mantêm os cátions unidos
- **Ligação metálica:** atração entre cátions e mar de elétrons

### Propriedades dos Metais

As propriedades dos metais são explicadas pelo modelo do mar de elétrons.

#### 1. Condutividade Elétrica

**Característica:** Metais **conduzem eletricidade** muito bem.

**Explicação:**
- Elétrons livres movem-se facilmente
- Ao aplicar diferença de potencial (voltagem), elétrons fluem
- **Corrente elétrica** = fluxo de elétrons

**Aplicações:** Fios elétricos (Cu, Al)

**Melhores condutores:** Ag (prata), Cu (cobre), Au (ouro)

#### 2. Condutividade Térmica

**Característica:** Metais conduzem **calor** eficientemente.

**Explicação:**
- Elétrons livres transportam energia térmica rapidamente
- Vibração dos cátions também contribui

**Aplicações:** Panelas (Al, Fe), dissipadores de calor (Cu)

#### 3. Maleabilidade

**Característica:** Metais podem ser **martelados** em lâminas finas sem quebrar.

**Explicação:**
- Cátions podem deslizar uns sobre os outros
- Mar de elétrons "se ajusta" à nova posição
- Ligação não é rompida

**Exemplos:** Folhas de alumínio, ouro batido

#### 4. Ductilidade

**Característica:** Metais podem ser **esticados** em fios.

**Explicação:**
- Mesma razão da maleabilidade
- Cátions deslizam, elétrons mantêm ligação

**Exemplos:** Fios de cobre, arame

#### 5. Brilho Metálico

**Característica:** Metais têm **superfície brilhante** quando polidos.

**Explicação:**
- Elétrons livres absorvem e re-emitem luz (reflexão)
- Aparecem "brilhantes"

**Aplicações:** Espelhos (Ag), joias (Au, Ag)

#### 6. Estado Físico e Pontos de Fusão/Ebulição

**Característica:** 
- Maioria são **sólidos** à temperatura ambiente (exceto Hg - mercúrio)
- Pontos de fusão/ebulição **variados** (geralmente médios a altos)

**Explicação:**
- Ligações metálicas são fortes (mas menos que iônicas)
- Dependem do número de elétrons de valência e tamanho do átomo

**Exemplos:**
- **Altos PF:** W (tungstênio) - 3422°C
- **Baixos PF:** Hg (mercúrio) - líquido (-39°C), Ga (gálio) - 30°C

#### 7. Densidade

**Característica:** Muitos metais são **densos**.

**Explicação:**
- Átomos empacotados compactamente no retículo cristalino

**Exemplos:**
- **Mais densos:** Os (ósmio), Ir (irídio), Pt (platina), Au (ouro)
- **Menos densos:** Li (lítio), Na (sódio), K (potássio)

### Ligas Metálicas

**Liga metálica:** mistura de dois ou mais metais (ou metal + não-metal).

**Objetivo:** Melhorar propriedades (dureza, resistência à corrosão, etc.)

**Exemplos:**

| Liga | Composição | Uso |
|------|------------|-----|
| **Aço** | Fe + C (carbono) | Construção, ferramentas |
| **Bronze** | Cu + Sn (estanho) | Esculturas, moedas antigas |
| **Latão** | Cu + Zn (zinco) | Instrumentos musicais |
| **Ouro 18k** | Au (75%) + Cu/Ag (25%) | Joias (ouro puro é mole) |
| **Aço inox** | Fe + Cr + Ni | Talheres, equipamentos |

**Vantagens das ligas:**
- **Mais duras** que metais puros
- Resistência à **corrosão**
- Podem ser **mais baratas**
- Propriedades **ajustáveis**

### Resumo: Três Tipos de Ligação

```
┌──────────┬─────────┬──────────┬──────────┐
│          │ IÔNICA  │COVALENTE │ METÁLICA │
├──────────┼─────────┼──────────┼──────────┤
│  Átomos  │Metal+   │Não-metal │  Metais  │
│          │Não-metal│+Não-metal│          │
├──────────┼─────────┼──────────┼──────────┤
│ Processo │Transfer.│Compartil.│Mar de e⁻ │
├──────────┼─────────┼──────────┼──────────┤
│  Formam  │  Íons   │Moléculas │  Rede    │
│          │cristais │          │ cristalina│
├──────────┼─────────┼──────────┼──────────┤
│   PF/PE  │  Altos  │  Baixos  │ Variados │
├──────────┼─────────┼──────────┼──────────┤
│Condutiv. │Fund/Dis.│   Não    │   Sim    │
│ Elétrica │         │          │ (sempre) │
├──────────┼─────────┼──────────┼──────────┤
│ Exemplo  │  NaCl   │   H₂O    │   Fe     │
└──────────┴─────────┴──────────┴──────────┘
```

### Exercícios Resolvidos

#### Exercício 1
Por que metais conduzem eletricidade, mas compostos iônicos sólidos não?

**Resposta:**
**Metais:** têm elétrons livres que se movem facilmente, transportando carga.

**Iônicos sólidos:** íons estão **fixos** no retículo cristalino, não podem se mover. Só conduzem quando fundidos ou dissolvidos (íons ficam livres).

#### Exercício 2
Explique por que o ouro usado em joias é geralmente uma liga (ouro 18k) e não ouro puro.

**Resposta:**
Ouro puro (24k) é muito **mole e maleável**, deformando facilmente. A liga com cobre ou prata (18k = 75% Au + 25% outros) torna o material **mais duro e resistente**, adequado para joias.

#### Exercício 3
Qual o tipo de ligação presente em:
a) Fe (ferro)
b) H₂O (água)
c) KCl (cloreto de potássio)

**Respostas:**

a) **Metálica** (Fe é metal)

b) **Covalente** (H e O são não-metais)

c) **Iônica** (K é metal, Cl é não-metal)

#### Exercício 4
(UFMG) Por que o cobre é usado em fios elétricos?

**Resposta:**
Cobre tem excelente **condutividade elétrica** (elétrons livres), é **maleável** e **ductil** (pode ser esticado em fios), e tem custo relativamente baixo comparado à prata (melhor condutor).

### Dicas para a Prova

1. **Ligação metálica:** entre metais
2. **Mar de elétrons:** elétrons livres, móveis
3. **Conduzem eletricidade:** sempre (elétrons livres)
4. **Maleáveis e dúcteis:** cátions deslizam
5. **Brilho metálico:** elétrons refletem luz
6. **Ligas:** mistura de metais (melhoram propriedades)
7. **Comparar ligações:** iônica, covalente, metálica
8. **Hg:** único metal líquido (temperatura ambiente)

### Conceitos-Chave para Memorizar

**Ligação Metálica:**
- Entre metais
- Mar de elétrons livres
- Cátions fixos + elétrons móveis

**Propriedades dos Metais:**
- Condutividade elétrica (elétrons livres)
- Condutividade térmica
- Maleabilidade (martelar)
- Ductilidade (esticar)
- Brilho metálico
- Sólidos (maioria)

**Ligas Metálicas:**
- Mistura de metais
- Melhoram propriedades
- Exemplos: aço, bronze, latão

### Resumo Visual

```
LIGAÇÃO METÁLICA:

Metal  +  Metal  →  Retículo Metálico
  ↓        ↓
Perdem valência
  ↓
Cátions ⁺ + Mar de elétrons e⁻

Modelo:
   ⁺   ⁺   ⁺   ⁺
  e⁻ e⁻ e⁻ e⁻ e⁻  ← elétrons livres
   ⁺   ⁺   ⁺   ⁺
  e⁻ e⁻ e⁻ e⁻ e⁻
   ⁺   ⁺   ⁺   ⁺

Propriedades:
├─ Conduzem eletricidade (e⁻ livres)
├─ Conduzem calor
├─ Maleáveis (cátions deslizam)
├─ Dúcteis (esticam)
├─ Brilho (reflexão luz)
└─ Sólidos (maioria)

COMPARAÇÃO LIGAÇÕES:

IÔNICA:     Metal → Não-metal
            Transferência
            
COVALENTE:  Não-metal → Não-metal
            Compartilhamento
            
METÁLICA:   Metal → Metal
            Mar de elétrons
```

---

**Tempo de estudo recomendado:** 30 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (importante - completa o estudo de ligações!)

# 11/29 - Férias Dia 4

## Aula 36 - Matemática: Função Exponencial - Parte 2 (Equações, Gráficos e Crescimento) - 90min

### Revisão: Função Exponencial Parte 1

Na Aula 34, estudamos:
- Potenciação e propriedades
- Equações exponenciais simples (bases iguais)
- Inequações básicas
- Gráfico introdutório

**Nesta aula:** Equações mais complexas, gráficos detalhados e aplicações.

### Definição de Função Exponencial

**Função Exponencial:**
```
f(x) = a^x
```

Onde:
- **a:** base (a > 0 e a ≠ 1)
- **x:** expoente (variável)

**Por que a > 0 e a ≠ 1?**
- **a > 0:** evitar resultados indefinidos (ex: (-2)^(1/2))
- **a ≠ 1:** pois 1^x = 1 (constante, não exponencial)

**Forma geral:**
```
f(x) = b · a^(cx + d) + e
```

Mas começamos com a forma básica: f(x) = a^x

### Propriedades da Função Exponencial

**1. Domínio:** D(f) = ℝ (todos os reais)

**2. Imagem:** Im(f) = ℝ₊* = (0, +∞)
- Função sempre positiva: f(x) > 0 para todo x

**3. Intercepto com eixo y:**
- Quando x = 0: f(0) = a⁰ = 1
- Sempre passa pelo ponto **(0, 1)**

**4. Não intercepta eixo x:**
- Nunca f(x) = 0 (sempre positiva)
- Eixo x é **assíntota horizontal**

**5. Injetora:**
- Se a^x₁ = a^x₂, então x₁ = x₂
- Cada valor de y corresponde a único valor de x

**6. Monotonia (crescimento):**
- **a > 1:** estritamente crescente
- **0 < a < 1:** estritamente decrescente

### Gráficos Detalhados


```
    GRÁFICOS DA FUNÇÃO EXPONENCIAL: f(x) = aˣ

    Caso 1: a > 1 (CRESCENTE)        Caso 2: 0 < a < 1 (DECRESCENTE)
    
         y                                y
         │                                │
       4 │         ╱                    4 │╲
         │        ╱                       │ ╲
       3 │       ╱                      3 │  ╲
         │      ╱                         │   ╲
       2 │     ╱                        2 │    ╲
         │    ╱                           │     ╲
       1 ├───●─────────── x             1 ├──────●──── x
         │  (0,1)                         │     (0,1)
    ─────┼──────────────                ─────┼──────────
         0                                    0

    Propriedades Comuns:
    • Sempre passa por (0, 1)
    • Sempre f(x) > 0 (acima do eixo x)
    • Domínio: ℝ (todos os reais)
    • Imagem: (0, +∞) (apenas positivos)
    • NÃO tem raízes (não corta eixo x)
    
    Se a > 1:                       Se 0 < a < 1:
    • Função CRESCENTE              • Função DECRESCENTE
    • x → +∞, f(x) → +∞            • x → +∞, f(x) → 0
    • x → -∞, f(x) → 0             • x → -∞, f(x) → +∞
```


#### Caso 1: a > 1 (Função Crescente)

**Exemplos:** f(x) = 2^x, f(x) = 3^x, f(x) = 10^x

**Características:**
- Cresce rapidamente para x > 0
- Aproxima-se de 0 para x → -∞
- Passa por (0, 1)

**Tabela (f(x) = 2^x):**
```
x  | -3  | -2  | -1  |  0  |  1  |  2  |  3  
f(x)| 1/8 | 1/4 | 1/2 |  1  |  2  |  4  |  8
```

**Gráfico:**
```
    |
  8 |           •
  4 |         •
  2 |       •
  1 |•─────•─────────
1/2 |  •
1/4 | •
    |•________________
   -3  -1  0  1  2  3
```

**Quanto maior a base, mais "vertical" a curva:**
- 10^x cresce mais rápido que 2^x

#### Caso 2: 0 < a < 1 (Função Decrescente)

**Exemplos:** f(x) = (1/2)^x, f(x) = (1/3)^x

**Características:**
- Decresce rapidamente para x > 0
- Aproxima-se de 0 para x → +∞
- Passa por (0, 1)

**Tabela (f(x) = (1/2)^x):**
```
x  | -3  | -2  | -1  |  0  |  1  |  2  |  3
f(x)|  8  |  4  |  2  |  1  | 1/2 | 1/4 | 1/8
```

**Gráfico:**
```
    |
  8 |•
  4 | •
  2 |  •
  1 |───•─────•
1/2 |       •  
1/4 |         •
    |___________•____
   -3  -1  0  1  2  3
```

**Relação importante:**
```
(1/a)^x = a^(-x)
```

Então: f(x) = (1/2)^x é reflexão de g(x) = 2^x em relação ao eixo y

### Equações Exponenciais Avançadas

#### Técnica 1: Substituição

**Quando aparece a mesma base com expoentes relacionados.**

**Exemplo 1:**
4^x - 2^x - 2 = 0

**Observar:** 4^x = (2²)^x = 2^(2x) = (2^x)²

**Substituição:** y = 2^x

y² - y - 2 = 0

(y - 2)(y + 1) = 0

y = 2 ou y = -1

**Voltar para x:**

2^x = 2 → x = 1 ✓

2^x = -1 → impossível (2^x > 0) ✗

*[Ver resposta 25 no final do documento]*

**Exemplo 2:**
9^x - 4·3^x + 3 = 0

9^x = (3²)^x = (3^x)²

**Substituição:** y = 3^x

y² - 4y + 3 = 0

(y - 1)(y - 3) = 0

y = 1 ou y = 3

3^x = 1 = 3⁰ → x = 0
3^x = 3 = 3¹ → x = 1

*[Ver resposta 26 no final do documento]*

#### Técnica 2: Bases Diferentes mas Relacionadas

**Exemplo:**
2^(x+1) + 2^(x-1) = 5

**Fatorar usando propriedades:**

2^(x+1) = 2·2^x
2^(x-1) = 2^x/2

2·2^x + 2^x/2 = 5

Multiplicar por 2:

4·2^x + 2^x = 10

5·2^x = 10

2^x = 2 = 2¹

**x = 1**

#### Técnica 3: Logaritmo (introdução)

Para equações como 2^x = 5, precisaremos de logaritmos (próximas aulas).

### Inequações Exponenciais Avançadas

**Exemplo 1:**
2^(2x) - 5·2^x + 4 ≤ 0

**Substituição:** y = 2^x (y > 0)

y² - 5y + 4 ≤ 0

**Raízes:** (y - 1)(y - 4) = 0
y = 1 ou y = 4

**Estudo do sinal:** a = 1 > 0 (parábola ∪)
```
  \____/
  1    4
```

y² - 5y + 4 ≤ 0: **1 ≤ y ≤ 4**

**Voltar para x:**

1 ≤ 2^x ≤ 4

2⁰ ≤ 2^x ≤ 2²

**0 ≤ x ≤ 2**

*[Ver resposta 27 no final do documento]*

### Aplicações: Crescimento e Decaimento Exponencial

#### Aplicação 1: Crescimento Populacional

Uma população de bactérias dobra a cada hora. Inicialmente há 100 bactérias.

**Modelo:**
```
P(t) = P₀ · 2^t
P(t) = 100 · 2^t
```

Onde:
- P(t): população após t horas
- P₀ = 100: população inicial
- Base 2: dobra a cada hora

**a) Quantas bactérias após 5 horas?**

P(5) = 100 · 2⁵ = 100 · 32 = 3.200 bactérias

**b) Quando atinge 12.800 bactérias?**

100 · 2^t = 12.800

2^t = 128 = 2⁷

t = 7 horas

#### Aplicação 2: Decaimento Radioativo

Uma substância radioativa tem meia-vida de 10 anos (metade se desintegra a cada 10 anos).

**Modelo:**
```
M(t) = M₀ · (1/2)^(t/10)
```

Se M₀ = 800g:

**a) Massa após 30 anos?**

M(30) = 800 · (1/2)^(30/10)
      = 800 · (1/2)³
      = 800 · 1/8
      = 100g

**b) Quando resta 100g?**

800 · (1/2)^(t/10) = 100

(1/2)^(t/10) = 1/8 = (1/2)³

t/10 = 3

t = 30 anos

#### Aplicação 3: Juros Compostos

Capital inicial de R$ 1.000 aplicado a 10% ao ano (juros compostos).

**Modelo:**
```
M(t) = C · (1 + i)^t
M(t) = 1000 · (1,1)^t
```

**Após 5 anos:**

M(5) = 1000 · (1,1)⁵ ≈ 1000 · 1,61 ≈ R$ 1.610

### Exercícios Resolvidos

#### Exercício 1
Resolva: 5^(2x) - 25 = 0

**Solução:**

5^(2x) = 25 = 5²

2x = 2

**x = 1**

#### Exercício 2
Determine o conjunto solução: 3^x > 27

**Solução:**

3^x > 3³

Base 3 > 1 (crescente) → mantém sinal

**x > 3**

**S = (3, +∞)**

#### Exercício 3
Resolva: 2^(x+2) + 2^x = 20

**Solução:**

2^(x+2) = 2² · 2^x = 4 · 2^x

4·2^x + 2^x = 20

5·2^x = 20

2^x = 4 = 2²

**x = 2**

#### Exercício 4
Uma população de 500 bactérias triplica a cada 2 horas. Quantas bactérias após 6 horas?

**Solução:**

P(t) = 500 · 3^(t/2)

P(6) = 500 · 3^(6/2) = 500 · 3³ = 500 · 27 = 13.500

*[Ver resposta 28 no final do documento]*

### Dicas para a Prova

1. **Sempre passa por (0, 1)**
2. **Sempre positiva:** f(x) > 0
3. **a > 1:** crescente; **0 < a < 1:** decrescente
4. **Substituição:** quando aparece (a^x)²
5. **Fatorar:** 2^(x+1) = 2 · 2^x
6. **Crescimento:** base > 1
7. **Decaimento:** base entre 0 e 1
8. **Juros compostos:** M = C(1+i)^t

### Conceitos-Chave para Memorizar

**Função Exponencial:**
- f(x) = a^x (a > 0, a ≠ 1)
- Domínio: ℝ
- Imagem: (0, +∞)
- Passa por (0, 1)

**Comportamento:**
- a > 1: crescente
- 0 < a < 1: decrescente

**Técnicas de Resolução:**
- Bases iguais: igualar expoentes
- Substituição: y = a^x
- Fatorar: usar propriedades

**Aplicações:**
- Crescimento: P(t) = P₀ · a^t (a > 1)
- Decaimento: M(t) = M₀ · a^t (0 < a < 1)
- Juros: M = C(1+i)^t

### Fórmulas Essenciais

```
Função Exponencial:
f(x) = a^x  (a > 0, a ≠ 1)

Propriedades:
- D(f) = ℝ
- Im(f) = ℝ₊* = (0, +∞)
- f(0) = 1
- a > 1: crescente
- 0 < a < 1: decrescente

Transformações:
a^(x+n) = a^n · a^x
a^(x-n) = a^x / a^n
(a^m)^x = a^(mx)

Aplicações:
Crescimento: P(t) = P₀ · a^t
Decaimento: M(t) = M₀ · (1/2)^(t/T)  [T = meia-vida]
Juros Compostos: M = C(1 + i)^t
```

### Resumo Visual

```
GRÁFICOS:

a > 1 (crescente):     0 < a < 1 (decresc.):
      |                      |
    8 |        •           8 |•
    4 |      •             4 | •
    2 |    •               2 |  •
    1 |──•──               1 |───•──
      |•                     |       •
    ──┼────────           ──┼────────
      
CRESCIMENTO:           DECAIMENTO:
P(t) = P₀ · a^t       M(t) = M₀ · a^t
(a > 1)               (0 < a < 1)

  •                      •
    •                  •
      •              •
        •          •
          •      •

SUBSTITUIÇÃO:
4^x = (2^x)²
9^x = (3^x)²
Se y = a^x, então a^(2x) = y²
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - aplicações são muito cobradas!)

## Aula 37 - Física: Forças Especiais - Peso, Normal e Atrito (Revisão e Aprofundamento) - 30min

### Revisão: Leis de Newton

Na Aula 22, estudamos as Leis de Newton e tipos básicos de forças.

**Nesta aula:** Aprofundamento em forças especiais e aplicações.

### Força Peso (P)

**Definição:** Força gravitacional que a Terra exerce sobre um corpo.

**Fórmula:**
```
P = m · g
```

Onde:
- P: peso (N - newtons)
- m: massa (kg)
- g: aceleração da gravidade (m/s²)

**Na Terra:** g ≈ 10 m/s² (ou 9,8 m/s² para maior precisão)

**Características:**
- **Direção:** vertical
- **Sentido:** para baixo (centro da Terra)
- **Ponto de aplicação:** centro de gravidade do corpo

**Diferença Massa vs. Peso:**

| Massa (m) | Peso (P) |
|-----------|----------|
| Quantidade de matéria | Força gravitacional |
| Escalar (kg) | Vetor (N) |
| NÃO varia | VARIA com g |
| Mesma em qualquer lugar | Diferente em planetas |

**Exemplos:**

Pessoa com 60 kg:
- **Terra:** P = 60 × 10 = 600 N
- **Lua:** g_Lua ≈ 1,6 m/s² → P = 60 × 1,6 = 96 N
- **Massa:** 60 kg (não muda!)

### Força Normal (N)

**Definição:** Força de reação da superfície, perpendicular ao contato.

**Características:**
- **Direção:** perpendicular à superfície
- **Sentido:** "empurra" o corpo para fora da superfície
- **Intensidade:** varia conforme situação

**NÃO é sempre igual ao peso!**

#### Caso 1: Superfície Horizontal (equilíbrio vertical)

```
    ↑ N
    |
  [corpo]
    |
    ↓ P
```

**Equilíbrio vertical:**
ΣF_y = 0
N - P = 0
**N = P = mg**

#### Caso 2: Corpo em Aceleração Vertical

**a) Elevador subindo acelerado (a ↑):**

```
    ↑ N
    |
  [corpo] ↑ a
    |
    ↓ P
```

F_R = ma (para cima)
N - P = ma
**N = P + ma = m(g + a)**

Normal **maior** que peso (sensação de "mais pesado")

**b) Elevador descendo acelerado (a ↓):**

F_R = ma (para baixo)
P - N = ma
**N = P - ma = m(g - a)**

Normal **menor** que peso (sensação de "mais leve")

**c) Queda livre (a = g ↓):**

N = m(g - g) = 0

**N = 0** (ausência de peso, "flutuação")

#### Caso 3: Plano Inclinado

```
        N ↑ (perp. ao plano)
       /|
      / |
   [corpo]
    / | \
   /  |  \ P_y (paralela)
  /   |   \
 /    ↓    \
/   P_x     \ θ
──────────────
```

**Decomposição do peso:**
- P_x = P · sen(θ) = mg sen(θ) (paralelo ao plano)
- P_y = P · cos(θ) = mg cos(θ) (perpendicular ao plano)

**Equilíbrio perpendicular:**
**N = P_y = mg cos(θ)**

#### Caso 4: Corpo Pressionado Contra Parede

```
Parede
  │ ← N
  │
  │ [corpo] → F (força aplicada)
  │
```

**N = F** (força aplicada horizontalmente)

### Força de Atrito (F_at)

**Definição:** Força que se opõe ao movimento relativo entre superfícies em contato.

**Características:**
- **Direção:** paralela às superfícies
- **Sentido:** oposto ao movimento (ou tendência)
- **Origem:** irregularidades microscópicas das superfícies

#### Atrito Estático (F_at,e)

**Quando:** corpo em repouso, tende a se mover mas ainda está parado.

**Características:**
- Varia de 0 até máximo
- **F_at,e ≤ μ_e · N**

**Força de atrito estático máximo:**
```
F_at,e(máx) = μ_e · N
```

**μ_e:** coeficiente de atrito estático (adimensional)

**Exemplo:**
Empurrando caixa com força crescente:
- Força pequena: caixa não move (F_at = F_aplicada)
- Aumenta força: atrito aumenta
- Atinge F_at(máx): caixa está prestes a deslizar
- Ultrapassa F_at(máx): caixa começa a deslizar

#### Atrito Cinético (F_at,c)

**Quando:** corpo em movimento.

**Fórmula:**
```
F_at,c = μ_c · N
```

**μ_c:** coeficiente de atrito cinético

**Observações:**
- Valor constante (não varia)
- Geralmente μ_c < μ_e (mais fácil manter movimento que iniciar)

#### Fatores que Influenciam o Atrito

**Depende de:**
- **Natureza das superfícies:** μ (coeficiente)
- **Força normal:** N

**NÃO depende de:**
- Área de contato
- Velocidade (atrito cinético)

### Aplicações

#### Problema 1
Um bloco de 10 kg está sobre uma superfície horizontal. μ_e = 0,4 e μ_c = 0,3. Qual a força mínima para:
a) Tirar o bloco do repouso?
b) Mantê-lo em movimento?
(g = 10 m/s²)

**Solução:**

N = P = mg = 10 × 10 = 100 N

a) **Força para tirar do repouso:**
F ≥ F_at,e(máx) = μ_e · N = 0,4 × 100 = 40 N

**F ≥ 40 N**

b) **Manter em movimento:**
F = F_at,c = μ_c · N = 0,3 × 100 = 30 N

**F = 30 N**

#### Problema 2
Bloco de 5 kg em plano inclinado de 30°. Determine a normal e a componente paralela do peso.
(g = 10 m/s²)

**Solução:**

P = 5 × 10 = 50 N

**Normal:**
N = mg cos(30°) = 50 × (√3/2) ≈ 50 × 0,87 ≈ 43,5 N

**Componente paralela:**
P_x = mg sen(30°) = 50 × 0,5 = 25 N

### Exercícios Resolvidos

#### Exercício 1
Qual o peso de um corpo de massa 8 kg na Terra (g = 10 m/s²)?

**Solução:**
P = mg = 8 × 10 = 80 N

*[Ver resposta 29 no final do documento]*

#### Exercício 2
Uma pessoa de 70 kg está em um elevador que sobe com aceleração de 2 m/s². Qual a normal? (g = 10 m/s²)

**Solução:**

Elevador subindo acelerado:
N = m(g + a) = 70(10 + 2) = 70 × 12 = 840 N

*[Ver resposta 30 no final do documento]*

#### Exercício 3
(UFMG) Um bloco está em repouso sobre uma mesa. A força normal é:
a) Sempre igual ao peso
b) Par ação-reação do peso
c) Força de reação da mesa

*[Ver resposta 31 no final do documento]*

**Importante:** Normal NÃO é par ação-reação do peso!
- Peso: Terra atrai bloco
- Reação do peso: Bloco atrai Terra

### Dicas para a Prova

1. **Peso:** sempre P = mg (para baixo)
2. **Normal:** perpendicular à superfície
3. **N = P:** só em superfície horizontal sem aceleração vertical
4. **Plano inclinado:** N = mg cos(θ)
5. **Atrito estático:** F_at ≤ μ_e N (varia)
6. **Atrito cinético:** F_at = μ_c N (constante)
7. **μ_e > μ_c:** iniciar movimento é mais difícil
8. **Atrito:** sempre oposto ao movimento

### Conceitos-Chave para Memorizar

**Peso:**
- P = mg
- Vertical, para baixo
- Varia com g

**Normal:**
- Perpendicular à superfície
- Varia conforme situação
- Horizontal: N = P
- Inclinado: N = mg cos(θ)

**Atrito:**
- Opõe movimento
- Estático: F_at ≤ μ_e N
- Cinético: F_at = μ_c N
- μ_e > μ_c

### Fórmulas Essenciais

```
Peso:
P = m · g

Normal (casos):
Horizontal: N = P = mg
Elevador (↑a): N = m(g + a)
Elevador (↓a): N = m(g - a)
Plano inclinado: N = mg cos(θ)

Atrito:
Estático (máx): F_at,e = μ_e · N
Cinético: F_at,c = μ_c · N

Plano Inclinado:
P_paralela = mg sen(θ)
P_perpendicular = mg cos(θ)
```

### Resumo Visual

```
PESO:
    [corpo]
       |
       ↓ P = mg
       
NORMAL:

Horizontal:    Inclinado (θ):
  ↑ N             N ↑
  |              /|
[corpo]      [corpo]
  |            /
  ↓ P         / P
           θ
           
ATRITO:

Estático:           Cinético:
[corpo] → F_apl   [corpo] → v
←F_at (varia)     ←F_at (constante)

F_at ≤ μ_e·N      F_at = μ_c·N
```

---

**Tempo de estudo recomendado:** 30 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - forças são essenciais!)

# 11/30 - Férias Dia 5

## Aula 38 - Matemática: Função Logarítmica - Parte 1 (Definição e Logaritmo Decimal/Natural) - 90min

### Introdução: O Problema Inverso

**Problema:** Resolver 2^x = 8 é fácil (x = 3).

**Mas e 2^x = 5?** Não conseguimos escrever 5 como potência de 2!

**Solução:** Usar **logaritmos**.

### Definição de Logaritmo

**Logaritmo** é o expoente ao qual devemos elevar a base para obter um número.

**Definição formal:**
```
log_a b = x  ⟺  a^x = b
```

Onde:
- **a:** base (a > 0, a ≠ 1)
- **b:** logaritmando (b > 0)
- **x:** logaritmo

**Lê-se:** "Logaritmo de b na base a é igual a x"

**Significado:** "a elevado a x é igual a b"

### Exemplos Básicos

**Exemplo 1:** log₂ 8 = ?

"2 elevado a quanto dá 8?"
2³ = 8
**log₂ 8 = 3**

**Exemplo 2:** log₅ 125 = ?

5³ = 125
**log₅ 125 = 3**

**Exemplo 3:** log₁₀ 100 = ?

10² = 100
**log₁₀ 100 = 2**

**Exemplo 4:** log₃ (1/9) = ?

3^x = 1/9 = 1/3² = 3⁻²
**log₃ (1/9) = -2**

**Exemplo 5:** log₄ 2 = ?

4^x = 2
(2²)^x = 2
2^(2x) = 2¹
2x = 1
**log₄ 2 = 1/2**

### Casos Especiais

#### 1. Logaritmo de 1
```
log_a 1 = 0  (para qualquer a)
```

**Por quê?** a⁰ = 1

**Exemplos:**
- log₅ 1 = 0
- log₁₀ 1 = 0

#### 2. Logaritmo da Base
```
log_a a = 1  (para qualquer a)
```

**Por quê?** a¹ = a

**Exemplos:**
- log₇ 7 = 1
- log₁₀ 10 = 1

#### 3. Potência da Base
```
log_a (a^n) = n
```

**Exemplos:**
- log₂ (2⁵) = 5
- log₃ (3⁻²) = -2

#### 4. Base Elevada ao Logaritmo
```
a^(log_a b) = b
```

**Exemplo:**
2^(log₂ 5) = 5

### Condições de Existência

**Para log_a b existir:**

1. **a > 0 e a ≠ 1** (base positiva e diferente de 1)
2. **b > 0** (logaritmando positivo)

**Consequências:**
- log₂ (-4): NÃO existe (logaritmando negativo)
- log₁ 5: NÃO existe (base = 1)
- log₋₂ 8: NÃO existe (base negativa)
- log₂ 0: NÃO existe (logaritmando = 0)

### Logaritmo Decimal (Base 10)

**Logaritmo decimal:** log₁₀ b

**Notação simplificada:**
```
log b = log₁₀ b
```

Quando a base não aparece, é base 10!

**Exemplos:**
- log 100 = log₁₀ 100 = 2 (pois 10² = 100)
- log 1000 = 3 (pois 10³ = 1000)
- log 0,01 = -2 (pois 10⁻² = 0,01)

**Aplicações:**
- Escala Richter (terremotos)
- pH (acidez)
- Decibéis (som)
- Ordens de grandeza

### Logaritmo Natural (Base e)

**Número de Euler:**
```
e ≈ 2,718281828...
```

**Logaritmo natural:** log_e b

**Notação:**
```
ln b = log_e b
```

**Lê-se:** "ene de b" ou "logaritmo natural de b"

**Exemplos:**
- ln e = 1 (pois e¹ = e)
- ln e² = 2
- ln 1 = 0

**Aplicações:**
- Crescimento populacional
- Juros compostos contínuos
- Decaimento radioativo
- Cálculo (derivadas, integrais)

**Por que "natural"?**
Aparece naturalmente em problemas de crescimento/decaimento contínuo.

### Relação entre Logaritmo e Exponencial

**Funções inversas:**

Se f(x) = a^x (exponencial)
Então f⁻¹(x) = log_a x (logarítmica)

**Propriedade fundamental:**
```
y = a^x  ⟺  x = log_a y
```

**Consequências:**
- log_a (a^x) = x
- a^(log_a x) = x

### Gráfico da Função Logarítmica (Introdução)

**Função:** f(x) = log_a x

#### Caso 1: a > 1

**Exemplo:** f(x) = log₂ x

```
x    | 1/4 | 1/2 | 1  | 2  | 4  | 8
log₂x| -2  | -1  | 0  | 1  | 2  | 3
```

**Gráfico:**
```
    |
  3 |           •
  2 |       •
  1 |   • 
  0 |─•─────────
 -1 | •
 -2 |•
    |____________
      1  2  4  8
```

**Características:**
- **Crescente**
- Passa por (1, 0)
- Eixo y é assíntota vertical
- Domínio: x > 0
- Imagem: ℝ

#### Caso 2: 0 < a < 1

**Exemplo:** f(x) = log_(1/2) x

**Características:**
- **Decrescente**
- Passa por (1, 0)
- Eixo y é assíntota

### Exercícios Resolvidos

#### Exercício 1
Calcule:
a) log₅ 25
b) log₃ 27
c) log₁₀ 0,001

**Soluções:**

a) 5^x = 25 = 5² → **x = 2**

b) 3^x = 27 = 3³ → **x = 3**

c) 10^x = 0,001 = 1/1000 = 10⁻³ → **x = -3**

#### Exercício 2
Determine o valor de log₄ 8.

**Solução:**

4^x = 8
(2²)^x = 2³
2^(2x) = 2³
2x = 3
**x = 3/2**

#### Exercício 3
Calcule: log₇ 1 + log₇ 7 + log₇ 49

**Solução:**

log₇ 1 = 0
log₇ 7 = 1
log₇ 49 = log₇ (7²) = 2

Soma: 0 + 1 + 2 = **3**

#### Exercício 4
Para quais valores de x existe log₂ (x - 3)?

**Solução:**

**Condição:** logaritmando > 0

x - 3 > 0
**x > 3**

#### Exercício 5
Simplifique: 3^(log₃ 10)

**Solução:**

Propriedade: a^(log_a b) = b

**3^(log₃ 10) = 10**

### Dicas para a Prova

1. **log_a b = x ⟺ a^x = b** (definição!)
2. **log_a 1 = 0** (sempre)
3. **log_a a = 1** (sempre)
4. **log_a (a^n) = n**
5. **a^(log_a b) = b**
6. **log b = log₁₀ b** (base 10)
7. **ln b = log_e b** (base e)
8. **Condições:** a > 0, a ≠ 1, b > 0

### Conceitos-Chave para Memorizar

**Definição:**
- log_a b = x ⟺ a^x = b
- a: base
- b: logaritmando
- x: logaritmo

**Casos Especiais:**
- log_a 1 = 0
- log_a a = 1
- log_a (a^n) = n
- a^(log_a b) = b

**Bases Especiais:**
- log b = log₁₀ b (decimal)
- ln b = log_e b (natural)

**Condições:**
- a > 0, a ≠ 1
- b > 0

### Fórmulas Essenciais

```
Definição:
log_a b = x  ⟺  a^x = b

Casos Especiais:
log_a 1 = 0
log_a a = 1
log_a (a^n) = n
a^(log_a b) = b

Logaritmos Especiais:
log b = log₁₀ b  (decimal)
ln b = log_e b   (natural, e ≈ 2,718)

Condições de Existência:
a > 0, a ≠ 1
b > 0
```

### Resumo Visual

```
DEFINIÇÃO:

log_a b = x
     ↓
   a^x = b
   
"a elevado a x dá b"

EXEMPLOS:
log₂ 8 = 3  porque  2³ = 8
log₁₀ 100 = 2  porque  10² = 100

GRÁFICO (a > 1):
    |
  2 |       •
  1 |   •
  0 |─•──────
 -1 | •
    |____________
      1  2  4

- Crescente (a > 1)
- Passa por (1,0)
- Assíntota: x = 0
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - logaritmos são fundamentais!)

## Aula 39 - Física: Plano Inclinado - 30min

### Introdução

**Plano inclinado:** superfície plana formando ângulo θ com a horizontal.

**Exemplos:** rampas, ladeiras, escorregadores

**Importância:** Combina conceitos de forças, decomposição vetorial, atrito.

### Forças no Plano Inclinado

```
        N ↑ (normal)
       /|
      / |
   [m]  |
    / | \
   /  |  \ F_at (atrito, se houver)
  /   |   \
 /    ↓    \
/     P     \ θ
──────────────
```

**Forças atuantes:**
1. **Peso (P):** vertical, para baixo (P = mg)
2. **Normal (N):** perpendicular ao plano
3. **Atrito (F_at):** paralelo ao plano, opõe movimento

### Decomposição do Peso

Como o peso é vertical mas o plano é inclinado, decompomos P:

**Componentes do peso:**

```
P_x = P sen(θ) = mg sen(θ)  (paralela ao plano, "desce")
P_y = P cos(θ) = mg cos(θ)  (perpendicular ao plano)
```

**Diagrama:**
```
        P_y
         ↑
         |
         |___P_x →
        /θ
       /
      / P
```

**Memorização:**
- **P_x (paralela):** sen(θ) - "sobe" com θ
- **P_y (perpendicular):** cos(θ) - "desce" com θ

### Força Normal no Plano Inclinado

**Equilíbrio perpendicular ao plano:**

Não há movimento perpendicular → ΣF_perp = 0

**N - P_y = 0**

```
N = P_y = P cos(θ) = mg cos(θ)
```

**Importante:** N ≠ P (diferente da superfície horizontal!)

**Observação:** Quanto maior θ, menor N.

### Casos de Movimento

#### Caso 1: Plano Inclinado SEM Atrito

**Forças paralelas ao plano:**
- P_x (desce)

**2ª Lei de Newton (paralelo ao plano):**

```
F_R = ma
P_x = ma
mg sen(θ) = ma
a = g sen(θ)
```

**Aceleração:**
```
a = g sen(θ)  (descendo o plano)
```

**Observações:**
- Aceleração independe da massa!
- θ = 0°: a = 0 (horizontal)
- θ = 90°: a = g (queda livre)

#### Caso 2: Plano Inclinado COM Atrito

**Forças paralelas:**
- P_x (desce)
- F_at (sobe, opõe movimento)

**Atrito:**
F_at = μN = μ mg cos(θ)

**2ª Lei (descendo):**
```
mg sen(θ) - μ mg cos(θ) = ma
a = g(sen(θ) - μ cos(θ))
```

**Condição para descer:**
sen(θ) > μ cos(θ)
**tan(θ) > μ**

Se tan(θ) ≤ μ: corpo não desce (atrito segura)

#### Caso 3: Corpo Empurrado Plano Acima

**Força aplicada F (paralela ao plano, subindo):**

**Subindo:**
```
F - P_x - F_at = ma
F - mg sen(θ) - μ mg cos(θ) = ma
```

### Aplicações

#### Problema 1
Bloco de 10 kg em plano inclinado de 30°, sem atrito. Qual a aceleração?
(g = 10 m/s²)

**Solução:**

a = g sen(30°) = 10 × 0,5 = 5 m/s²

*[Ver resposta 32 no final do documento]*

#### Problema 2
Mesmo bloco, mesma inclinação, μ = 0,2. Qual a aceleração?

**Solução:**

a = g(sen(θ) - μ cos(θ))
a = 10(sen(30°) - 0,2 × cos(30°))
a = 10(0,5 - 0,2 × 0,87)
a = 10(0,5 - 0,174)
a = 10 × 0,326
a ≈ 3,26 m/s²

*[Ver resposta 33 no final do documento]*

#### Problema 3
Determine a normal de um bloco de 5 kg em plano de 60°.
(g = 10 m/s²)

**Solução:**

N = mg cos(60°) = 5 × 10 × 0,5 = 25 N

*[Ver resposta 34 no final do documento]*

### Exercícios Resolvidos

#### Exercício 1
Em um plano inclinado de 45° sem atrito, um corpo de 2 kg tem qual aceleração? (g = 10 m/s²)

**Solução:**

a = g sen(45°) = 10 × (√2/2) ≈ 10 × 0,7 = 7 m/s²

*[Ver resposta 35 no final do documento]*

#### Exercício 2
(UFMG) Qual a força normal em um corpo de 8 kg em plano de 30°?

**Solução:**

N = mg cos(30°) = 8 × 10 × (√3/2) ≈ 80 × 0,87 ≈ 69,6 N

*[Ver resposta 36 no final do documento]*

### Dicas para a Prova

1. **Decompor peso:** P_x = mg sen(θ), P_y = mg cos(θ)
2. **Normal:** N = mg cos(θ) (não é igual a P!)
3. **Sem atrito:** a = g sen(θ)
4. **Com atrito:** a = g(sen(θ) - μ cos(θ))
5. **Ângulos notáveis:** saber sen/cos de 30°, 45°, 60°
6. **Aceleração independe da massa** (sem atrito)
7. **Maior θ:** maior aceleração, menor normal

### Conceitos-Chave para Memorizar

**Decomposição do Peso:**
- P_x = mg sen(θ) (paralela)
- P_y = mg cos(θ) (perpendicular)

**Normal:**
- N = mg cos(θ)

**Aceleração:**
- Sem atrito: a = g sen(θ)
- Com atrito: a = g(sen(θ) - μ cos(θ))

### Fórmulas Essenciais

```
Plano Inclinado (ângulo θ):

Decomposição do Peso:
P_x = mg sen(θ)  (paralela ao plano)
P_y = mg cos(θ)  (perpendicular)

Normal:
N = mg cos(θ)

Aceleração (sem atrito):
a = g sen(θ)

Atrito:
F_at = μN = μ mg cos(θ)

Aceleração (com atrito):
a = g(sen(θ) - μ cos(θ))

Ângulos Notáveis:
sen(30°) = 1/2 = 0,5
cos(30°) = √3/2 ≈ 0,87
sen(45°) = cos(45°) = √2/2 ≈ 0,7
sen(60°) = √3/2 ≈ 0,87
cos(60°) = 1/2 = 0,5
```

### Resumo Visual

```
PLANO INCLINADO:

        N ↑
       /|
      / |
   [m]  |
    /   |
   /    ↓ P_y = mg cos(θ)
  / P_x = mg sen(θ) →
 /      
/ θ     
────────

Decomposição:
        P_y ↑
         |
         |
        θ|___→ P_x
        /
       / P ↓

P_x "desce" - sen(θ)
P_y "comprime" - cos(θ)

SEM ATRITO:       COM ATRITO:
a = g sen(θ)      a = g(sen-μcos)
```

---

**Tempo de estudo recomendado:** 30 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐ (muito importante - aplicação prática de forças!)

# 12/01 - Férias Dia 6

## Aula 40 - Matemática: Função Logarítmica - Parte 2 (Propriedades e Equações) - 90min

### Revisão: Logaritmos Parte 1

Na Aula 38, estudamos:
- Definição: log_a b = x ⟺ a^x = b
- Casos especiais: log_a 1 = 0, log_a a = 1
- Logaritmo decimal (log) e natural (ln)
- Condições de existência

**Nesta aula:** Propriedades operatórias e equações logarítmicas.

### Propriedades Operatórias dos Logaritmos

#### 1. Logaritmo do Produto
```
log_a (b · c) = log_a b + log_a c
```

**"Logaritmo do produto = soma dos logaritmos"**

**Exemplos:**
- log₂ (8 × 4) = log₂ 8 + log₂ 4 = 3 + 2 = 5
- log (100 × 10) = log 100 + log 10 = 2 + 1 = 3

**Aplicação:**
log₅ 50 = log₅ (5 × 10) = log₅ 5 + log₅ 10 = 1 + log₅ 10

#### 2. Logaritmo do Quociente
```
log_a (b/c) = log_a b - log_a c
```

**"Logaritmo do quociente = diferença dos logaritmos"**

**Exemplos:**
- log₂ (16/4) = log₂ 16 - log₂ 4 = 4 - 2 = 2
- log (1000/10) = log 1000 - log 10 = 3 - 1 = 2

#### 3. Logaritmo da Potência
```
log_a (b^n) = n · log_a b
```

**"Logaritmo da potência = expoente × logaritmo"**

**Exemplos:**
- log₂ (8³) = 3 · log₂ 8 = 3 × 3 = 9
- log (100²) = 2 · log 100 = 2 × 2 = 4
- log₃ (√9) = log₃ (9^(1/2)) = (1/2) · log₃ 9 = (1/2) × 2 = 1

#### 4. Mudança de Base
```
log_a b = (log_c b) / (log_c a)
```

**Casos particulares:**

**Para base 10:**
```
log_a b = (log b) / (log a)
```

**Para base e:**
```
log_a b = (ln b) / (ln a)
```

**Consequência importante:**
```
log_a b = 1 / log_b a
```

**Exemplos:**

log₂ 5 = (log 5) / (log 2) ≈ 0,699 / 0,301 ≈ 2,32

log₅ 2 = 1 / log₂ 5 ≈ 1 / 2,32 ≈ 0,43

### Aplicações das Propriedades

#### Exemplo 1: Simplificar
log 2 + log 5

**Solução:**
= log (2 × 5)
= log 10
= 1

#### Exemplo 2: Simplificar
log₃ 81 - log₃ 9

**Solução:**
= log₃ (81/9)
= log₃ 9
= log₃ (3²)
= 2

#### Exemplo 3: Calcular
log₂ 5 + log₂ 8 - log₂ 10

**Solução:**
= log₂ (5 × 8 / 10)
= log₂ (40/10)
= log₂ 4
= log₂ (2²)
= 2

#### Exemplo 4: Simplificar
2 log 5 + log 4

**Solução:**
= log (5²) + log 4
= log 25 + log 4
= log (25 × 4)
= log 100
= 2

### Equações Logarítmicas

**Equação logarítmica:** incógnita dentro do logaritmo ou como logaritmo.

#### Tipo 1: log_a f(x) = k

**Método:** Passar para forma exponencial

**Exemplo:**
log₂ (x + 1) = 3

2³ = x + 1
8 = x + 1
**x = 7**

**Verificação:** log₂ (7 + 1) = log₂ 8 = 3 ✓

#### Tipo 2: log_a f(x) = log_a g(x)

**Método:** Igualar argumentos (se bases iguais)

**Exemplo:**
log₅ (2x - 3) = log₅ (x + 1)

2x - 3 = x + 1
x = 4

**Verificação de condições:**
2x - 3 > 0 → x > 3/2 ✓
x + 1 > 0 → x > -1 ✓
x = 4 satisfaz ambas

*[Ver resposta 37 no final do documento]*

#### Tipo 3: Equações com Propriedades

**Exemplo 1:**
log x + log (x - 3) = 1

**Solução:**
log [x(x - 3)] = 1
log (x² - 3x) = 1

x² - 3x = 10¹
x² - 3x - 10 = 0
(x - 5)(x + 2) = 0

x = 5 ou x = -2

**Verificar condições:**
- x > 0 ✓ (x = 5)  ✗ (x = -2)
- x - 3 > 0 → x > 3 ✓ (x = 5)  ✗ (x = -2)

*[Ver resposta 38 no final do documento]*

**Exemplo 2:**
log₂ x - log₂ (x - 1) = 1

log₂ [x/(x - 1)] = 1

x/(x - 1) = 2¹

x = 2(x - 1)
x = 2x - 2
x = 2

**Verificação:** x = 2 > 0 ✓, x - 1 = 1 > 0 ✓

*[Ver resposta 39 no final do documento]*

#### Tipo 4: Substituição

**Exemplo:**
(log x)² - 3 log x + 2 = 0

**Substituição:** y = log x

y² - 3y + 2 = 0
(y - 1)(y - 2) = 0
y = 1 ou y = 2

**Voltar para x:**
log x = 1 → x = 10¹ = 10
log x = 2 → x = 10² = 100

*[Ver resposta 40 no final do documento]*

### Inequações Logarítmicas

**Regra depende da base:**

**Se a > 1:** função crescente
```
log_a f(x) > log_a g(x)  →  f(x) > g(x)
```

**Se 0 < a < 1:** função decrescente
```
log_a f(x) > log_a g(x)  →  f(x) < g(x)  (inverte!)
```

**Exemplo 1:**
log₂ (x + 1) > log₂ 5

Base 2 > 1 (crescente) → mantém sinal

x + 1 > 5
x > 4

**Condição:** x + 1 > 0 → x > -1

**Interseção:** x > 4

*[Ver resposta 41 no final do documento]*

**Exemplo 2:**
log_(1/2) x < log_(1/2) 4

Base 1/2 < 1 (decrescente) → **inverte**

x > 4

**Condição:** x > 0

**Interseção:** x > 4

*[Ver resposta 42 no final do documento]*

### Gráfico da Função Logarítmica


```
    GRÁFICOS DA FUNÇÃO LOGARÍTMICA: f(x) = logₐ x

    Caso 1: a > 1 (CRESCENTE)        Caso 2: 0 < a < 1 (DECRESCENTE)
    
         y                                y
         │                                │
       2 │     ╱                        2 │     ╲
         │    ╱                           │      ╲
       1 ├───●─────────               1 ├───●────────
         │  (1,0)                         │  (1,0)
    ─────●──────────── x              ─────●──────────── x
         1│ ╱                              1│  ╲
       -1│╱                             -1 │   ╲
         │                                 │    ╲
    
    Propriedades Comuns:
    • Sempre passa por (1, 0)
    • Domínio: (0, +∞) (apenas x > 0)
    • Imagem: ℝ (todos os reais)
    • Assíntota vertical: x = 0 (eixo y)
    • NÃO existe log de número ≤ 0
    
    Se a > 1:                       Se 0 < a < 1:
    • Função CRESCENTE              • Função DECRESCENTE
    • Inversa de aˣ com a > 1      • Inversa de aˣ com 0 < a < 1
    
    SIMETRIA: log e exp são simétricas em relação à reta y = x
```


**f(x) = log_a x**

**Características:**
- **Domínio:** x > 0 (ℝ₊*)
- **Imagem:** ℝ (todos os reais)
- **Intercepto com eixo x:** (1, 0) - sempre!
- **Assíntota vertical:** x = 0 (eixo y)
- **a > 1:** crescente
- **0 < a < 1:** decrescente

**Relação com exponencial:**
```
Se f(x) = a^x
Então f⁻¹(x) = log_a x
```

Gráficos são simétricos em relação à reta y = x.

### Exercícios Resolvidos

#### Exercício 1
Simplifique: log₅ 25 + log₅ 5 - log₅ 125

**Solução:**
= 2 + 1 - 3
= 0

#### Exercício 2
Calcule: log 2 + log 50

**Solução:**
= log (2 × 50)
= log 100
= 2

#### Exercício 3
Resolva: log₃ (x² - 8) = 2

**Solução:**
x² - 8 = 3²
x² - 8 = 9
x² = 17
x = ±√17

**Condição:** x² - 8 > 0 → x² > 8

Ambos √17 e -√17 satisfazem (pois 17 > 8)

*[Ver resposta 43 no final do documento]*

#### Exercício 4
Resolva: log x + log (x + 3) = 1

**Solução:**
log [x(x + 3)] = 1
x² + 3x = 10
x² + 3x - 10 = 0
(x + 5)(x - 2) = 0

x = -5 ou x = 2

**Condições:**
x > 0: apenas x = 2 ✓
x + 3 > 0: x > -3, ambos satisfazem, mas x = -5 já foi eliminado

*[Ver resposta 44 no final do documento]*

#### Exercício 5
Calcule log₈ 2.

**Solução:**

**Método 1 - Definição:**
8^x = 2
(2³)^x = 2¹
2^(3x) = 2¹
3x = 1
x = 1/3

**Método 2 - Mudança de base:**
log₈ 2 = (log 2)/(log 8) = (log 2)/(log 2³) = (log 2)/(3 log 2) = 1/3

*[Ver resposta 45 no final do documento]*

### Dicas para a Prova

1. **Produto:** log(ab) = log a + log b
2. **Quociente:** log(a/b) = log a - log b
3. **Potência:** log(a^n) = n log a
4. **Mudança de base:** log_a b = (log b)/(log a)
5. **Equação log_a f = log_a g:** f = g (igualar)
6. **Inequação e a > 1:** mantém sinal
7. **Inequação e 0 < a < 1:** inverte sinal
8. **Sempre verificar condições:** logaritmando > 0

### Conceitos-Chave para Memorizar

**Propriedades:**
- Produto: log(ab) = log a + log b
- Quociente: log(a/b) = log a - log b
- Potência: log(a^n) = n log a
- Mudança: log_a b = (log b)/(log a)

**Equações:**
- log_a f(x) = k → a^k = f(x)
- log_a f = log_a g → f = g

**Inequações:**
- a > 1: crescente (mantém)
- 0 < a < 1: decrescente (inverte)

**Sempre:** verificar condições (> 0)

### Fórmulas Essenciais

```
Propriedades Operatórias:
log_a (bc) = log_a b + log_a c
log_a (b/c) = log_a b - log_a c
log_a (b^n) = n · log_a b

Mudança de Base:
log_a b = (log_c b) / (log_c a)
log_a b = (log b) / (log a)  [base 10]
log_a b = (ln b) / (ln a)    [base e]
log_a b = 1 / log_b a

Equação:
log_a f(x) = log_a g(x)  ⟹  f(x) = g(x)

Inequação:
a > 1:     log_a f > log_a g  ⟹  f > g
0 < a < 1: log_a f > log_a g  ⟹  f < g

Condições:
Sempre verificar logaritmando > 0
```

### Resumo Visual

```
PROPRIEDADES:

Produto:      Quociente:
log(a×b)      log(a/b)
  =             =
log a + log b log a - log b

Potência:
log(a^n) = n·log a

EQUAÇÃO:
log_a f = log_a g
     ↓
    f = g

INEQUAÇÃO:
a > 1 (cresce):   0 < a < 1 (decresce):
log_a f > log_a g log_a f > log_a g
     ↓                 ↓
    f > g             f < g
  (mantém)          (inverte)
```

---

**Tempo de estudo recomendado:** 90 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - propriedades são muito cobradas!)

## Aula 41 - Química: Propriedades das Substâncias Segundo Ligações - 30min

### Revisão: Ligações Químicas

Já estudamos os três tipos principais:
- **Aula 31:** Ligação Iônica (metal + não-metal, íons)
- **Aula 33:** Ligação Covalente (não-metal + não-metal, moléculas)
- **Aula 35:** Ligação Metálica (metais, mar de elétrons)

**Nesta aula:** Como o tipo de ligação determina as propriedades das substâncias.

### Propriedades dos Compostos Iônicos

**Exemplos:** NaCl, CaO, MgCl₂, K₂SO₄

#### Características Físicas

**1. Estado Físico:**
- **Sólidos** à temperatura ambiente
- Formam cristais (retículo cristalino ordenado)

**2. Pontos de Fusão e Ebulição:**
- **Muito altos**
- Fortes atrações eletrostáticas entre íons

**Exemplos:**
- NaCl: PF = 801°C
- MgO: PF = 2852°C

**3. Dureza:**
- **Duros** (resistem a deformação)
- **Quebradiços** (fraturam ao invés de deformar)

#### Condutividade Elétrica

**Sólidos:** NÃO conduzem
- Íons fixos no retículo, não se movem

**Fundidos (líquidos):** CONDUZEM
- Íons livres para se mover

**Dissolvidos em água:** CONDUZEM
- Íons dispersos na solução, móveis

**Resumo:**
```
Iônico sólido: NÃO conduz
Iônico fundido/dissolvido: CONDUZ
```

#### Solubilidade

**Em água (polar):** Geralmente **solúveis**
- "Semelhante dissolve semelhante"
- Compostos iônicos são polares
- Íons se dispersam na água

**Em solventes apolares:** **Insolúveis**
- Gasolina, benzeno, etc.

**Regras de solubilidade (principais):**
- Sais de Na⁺, K⁺, NH₄⁺: sempre solúveis
- Nitratos (NO₃⁻): sempre solúveis
- Cloretos, brometos, iodetos: geralmente solúveis (exceto Ag⁺, Pb²⁺)
- Sulfatos: geralmente solúveis (exceto Ba²⁺, Pb²⁺)

### Propriedades dos Compostos Covalentes (Moleculares)

**Exemplos:** H₂O, CO₂, CH₄, O₂, N₂

#### Características Físicas

**1. Estado Físico:**
- Maioria: **gases** ou **líquidos** à temp. ambiente
- Alguns sólidos (gelo, açúcar, naftaleno)

**2. Pontos de Fusão e Ebulição:**
- **Baixos** (comparados a iônicos)
- Forças intermoleculares fracas

**Exemplos:**
- H₂O: PE = 100°C
- CO₂: sublima a -78°C

**Exceção:** Substâncias covalentes em rede (SiO₂, diamante)
- PF/PE muito altos
- Ligações covalentes formam rede tridimensional

#### Condutividade Elétrica

**Geralmente:** NÃO conduzem
- Não têm íons ou elétrons livres

**Exceções:**
- **Grafite:** estrutura especial com elétrons livres
- **Ácidos em água:** formam íons (HCl → H⁺ + Cl⁻)

#### Solubilidade

Depende da **polaridade** da molécula:

**Moléculas polares:**
- Solúveis em solventes polares (água)
- Exemplos: H₂O, HCl, NH₃, álcoois

**Moléculas apolares:**
- Solúveis em solventes apolares (gasolina, benzeno)
- Exemplos: O₂, N₂, CH₄, CO₂, gorduras

**Regra de ouro:**
```
"Semelhante dissolve semelhante"
```

### Propriedades das Substâncias Metálicas

**Exemplos:** Fe, Cu, Au, Al, Na

#### Características

**1. Estado Físico:**
- **Sólidos** à temp. ambiente (exceto Hg - mercúrio)

**2. Pontos de Fusão:**
- **Variados** (baixos a muito altos)
- W (tungstênio): 3422°C (alto)
- Hg (mercúrio): -39°C (líquido)
- Ga (gálio): 30°C (derrete na mão)

**3. Condutividade Elétrica e Térmica:**
- **Excelentes condutores** (sempre)
- Elétrons livres transportam carga e calor

**Melhores condutores:**
- Ag (prata) > Cu (cobre) > Au (ouro) > Al (alumínio)

**4. Brilho Metálico:**
- Superfície reflete luz (elétrons livres)

**5. Maleabilidade e Ductilidade:**
- **Maleáveis:** podem ser martelados (lâminas)
- **Dúcteis:** podem ser esticados (fios)

**6. Densidade:**
- Maioria são densos
- Exceções: Li, Na, K (menos densos que água)

### Comparação das Propriedades

```
┌──────────────┬─────────┬──────────┬──────────┐
│  Propriedade │ IÔNICA  │COVALENTE │ METÁLICA │
├──────────────┼─────────┼──────────┼──────────┤
│Estado físico │ Sólidos │Gases/Líq.│ Sólidos  │
├──────────────┼─────────┼──────────┼──────────┤
│   PF / PE    │  Altos  │  Baixos  │ Variados │
├──────────────┼─────────┼──────────┼──────────┤
│Condutividade │Fund/Dis.│   Não    │   Sim    │
│  Elétrica    │         │          │ (sempre) │
├──────────────┼─────────┼──────────┼──────────┤
│ Solubilidade │  H₂O    │  Varia   │  Baixa   │
│              │(polar)  │(polar/ap)│          │
├──────────────┼─────────┼──────────┼──────────┤
│    Dureza    │Duros,   │  Varia   │  Varia   │
│              │quebradiç.│          │(maleáv.) │
├──────────────┼─────────┼──────────┼──────────┤
│   Exemplo    │  NaCl   │   H₂O    │    Fe    │
└──────────────┴─────────┴──────────┴──────────┘
```

### Aplicações Práticas

#### 1. Sal de Cozinha (NaCl) - Iônico
- Sólido cristalino
- Alto PF (801°C)
- Solúvel em água
- Solução conduz eletricidade (íons Na⁺ e Cl⁻)

#### 2. Água (H₂O) - Covalente Polar
- Líquida à temp. ambiente
- PE = 100°C (baixo)
- Polar: dissolve iônicos e polares
- Não conduz pura (mas conduz com íons dissolvidos)

#### 3. Cobre (Cu) - Metálico
- Sólido à temp. ambiente
- Excelente condutor elétrico (fios)
- Maleável e dúctil
- Brilho metálico

### Exercícios Resolvidos

#### Exercício 1
Por que o sal de cozinha (NaCl) não conduz eletricidade quando sólido, mas conduz quando dissolvido em água?

**Resposta:**
**Sólido:** íons Na⁺ e Cl⁻ estão fixos no retículo cristalino, não podem se mover, logo NÃO conduzem.

**Dissolvido:** íons ficam livres na solução aquosa, podem se mover e transportar carga elétrica, logo CONDUZEM.

#### Exercício 2
Explique por que metais são bons condutores de eletricidade.

**Resposta:**
Metais têm **elétrons livres** (mar de elétrons) que se movem facilmente. Ao aplicar diferença de potencial, os elétrons fluem, criando corrente elétrica.

#### Exercício 3
Uma substância é sólida à temperatura ambiente, tem alto ponto de fusão, é solúvel em água e sua solução conduz eletricidade. Que tipo de ligação tem?

**Resposta:**
**Ligação iônica**. As características (sólido, alto PF, solúvel em água, solução condutora) são típicas de compostos iônicos.

#### Exercício 4
(UFMG) Compare NaCl e H₂O quanto à condutividade elétrica.

**Resposta:**
- **NaCl sólido:** não conduz (íons fixos)
- **NaCl fundido/dissolvido:** conduz (íons livres)
- **H₂O pura:** não conduz (covalente, sem íons)
- **H₂O com sais dissolvidos:** conduz (íons do sal)

### Dicas para a Prova

1. **Iônico:** sólidos, altos PF/PE, conduzem fundidos/dissolvidos
2. **Covalente:** gases/líquidos, baixos PF/PE, não conduzem
3. **Metálico:** sólidos, conduzem sempre, maleáveis
4. **Solubilidade:** "semelhante dissolve semelhante"
5. **Condutividade:** precisa de partículas carregadas móveis
6. **Iônicos:** solúveis em água (polar)
7. **Covalentes apolares:** solúveis em apolares
8. **Metais:** sempre conduzem (elétrons livres)

### Conceitos-Chave para Memorizar

**Iônica:**
- Sólidos cristalinos
- Altos PF/PE
- Conduzem fundidos/dissolvidos
- Solúveis em água

**Covalente:**
- Gases/líquidos (maioria)
- Baixos PF/PE
- Não conduzem (geralmente)
- Solubilidade varia

**Metálica:**
- Sólidos (exceto Hg)
- Conduzem sempre
- Maleáveis, dúcteis
- Brilho metálico

### Resumo Visual

```
PROPRIEDADES × LIGAÇÕES:

IÔNICA (NaCl):
├─ Sólido cristalino
├─ Alto PF (801°C)
├─ Conduz fundido/dissolvido
└─ Solúvel H₂O

COVALENTE (H₂O):
├─ Líquido/Gás
├─ Baixo PE (100°C)
├─ Não conduz puro
└─ Polar: dissolve polar

METÁLICA (Cu):
├─ Sólido
├─ Conduz sempre
├─ Maleável, dúctil
└─ Brilho

TABELA:
           Iônico  Cov.  Met.
Estado     Sól.    G/L   Sól.
PF/PE      Alto    Baixo Var.
Conduz     F/D     Não   Sim
```

---

**Tempo de estudo recomendado:** 30 minutos
**Nível de dificuldade:** Médio
**Importância para a prova:** ⭐⭐⭐⭐ (importante - relaciona estrutura e propriedades!)

# 12/02 - Férias Dia 7 (ÚLTIMO DIA DE FÉRIAS!)

## Aula 42 - Matemática: Relação entre Funções Exponencial e Logarítmica - 60min

### Funções Inversas

**Definição:** Duas funções f e g são inversas se:
```
f(g(x)) = x  e  g(f(x)) = x
```

**Notação:** g = f⁻¹ (função inversa de f)

**Graficamente:** Gráficos são simétricos em relação à reta y = x

### Função Exponencial e Logarítmica: Inversas

**Função exponencial:** f(x) = a^x
**Função logarítmica:** g(x) = log_a x

**São funções inversas!**

#### Verificação

**1. f(g(x)) = x:**
```
f(g(x)) = f(log_a x)
        = a^(log_a x)
        = x  ✓
```

**2. g(f(x)) = x:**
```
g(f(x)) = g(a^x)
        = log_a (a^x)
        = x  ✓
```

### Propriedades Fundamentais

**Decorrentes da relação inversa:**

**1. Composição:**
```
a^(log_a x) = x  (x > 0)
log_a (a^x) = x  (x ∈ ℝ)
```

**2. Domínio e Imagem:**

| Função | Domínio | Imagem |
|--------|---------|--------|
| f(x) = a^x | ℝ | ℝ₊* (0, +∞) |
| g(x) = log_a x | ℝ₊* (0, +∞) | ℝ |

**Observe:** Domínio de uma é imagem da outra!

**3. Interceptos:**

**Exponencial:**
- Intercepto y: (0, 1) - sempre!
- Não intercepta eixo x (assíntota)

**Logarítmica:**
- Intercepto x: (1, 0) - sempre!
- Não intercepta eixo y (assíntota)

### Gráficos: Simetria

**Propriedade:** Gráficos de f(x) = a^x e g(x) = log_a x são **simétricos** em relação à **reta y = x**.

#### Exemplo: a = 2

**f(x) = 2^x:**
- Passa por (0, 1), (1, 2), (2, 4)
- Crescente
- Assíntota: y = 0 (eixo x)

**g(x) = log₂ x:**
- Passa por (1, 0), (2, 1), (4, 2)
- Crescente
- Assíntota: x = 0 (eixo y)

**Gráfico:**
```
    |    y=x (diagonal)
  4 |   /    •2^x
  2 | •/   •
  1 |•/──•─────
    |/ •log₂x
    |•____________
      1  2  4
```

**Simetria:** Pontos (a, b) em f correspondem a (b, a) em g.

### Equações Envolvendo Ambas

#### Tipo 1: a^x = k → Usar log

**Exemplo:** 2^x = 5

**Método 1 - Logaritmo decimal:**
```
log(2^x) = log 5
x log 2 = log 5
x = (log 5)/(log 2)
x ≈ 0,699/0,301 ≈ 2,32
```

**Método 2 - Logaritmo na base adequada:**
```
log₂(2^x) = log₂ 5
x = log₂ 5
```

#### Tipo 2: log_a x = k → Usar exponencial

**Exemplo:** log₃ x = 4

```
3⁴ = x
x = 81
```

#### Tipo 3: Mistas

**Exemplo:** 2^x = log₂ 16

**Resolver log₂ 16 primeiro:**
log₂ 16 = log₂ (2⁴) = 4

**Então:**
2^x = 4 = 2²
x = 2

### Mudança de Base: Aplicações

**Fórmula:**
```
log_a b = (log_c b)/(log_c a)
```

**Uso prático:** Calcular logaritmos em bases diferentes de 10 ou e.

**Exemplo:** Calcular log₅ 20

```
log₅ 20 = (log 20)/(log 5)
        ≈ 1,301/0,699
        ≈ 1,86
```

**Ou usando ln:**
```
log₅ 20 = (ln 20)/(ln 5)
        ≈ 2,996/1,609
        ≈ 1,86
```

### Aplicações Práticas

#### Problema 1: Crescimento Exponencial

Uma população de 1000 bactérias dobra a cada hora. Quando atinge 10.000?

**Modelo:** P(t) = 1000 · 2^t

**Resolver:**
1000 · 2^t = 10000
2^t = 10
t = log₂ 10
t = (log 10)/(log 2) = 1/0,301 ≈ 3,32 horas

*[Ver resposta 46 no final do documento]*

#### Problema 2: Decaimento Radioativo

Substância com meia-vida de 5 anos. Tempo para restar 10% da massa inicial?

**Modelo:** M(t) = M₀ · (1/2)^(t/5)

**Resolver:**
(1/2)^(t/5) = 0,1

**Aplicar log:**
log[(1/2)^(t/5)] = log 0,1
(t/5) log(1/2) = log 0,1
(t/5) × (-0,301) = -1
t/5 = 1/0,301 ≈ 3,32
t ≈ 16,6 anos

#### Problema 3: Juros Compostos

Capital de R$ 2000 a 8% ao ano. Quando duplica?

**Modelo:** M = 2000(1,08)^t

**Resolver:**
2000(1,08)^t = 4000
1,08^t = 2
t = log₁.₀₈ 2
t = (log 2)/(log 1,08)
t ≈ 0,301/0,0334 ≈ 9 anos

### Exercícios Resolvidos

#### Exercício 1
Resolva: 3^x = 20

**Solução:**
x = log₃ 20 = (log 20)/(log 3) ≈ 1,301/0,477 ≈ 2,73

*[Ver resposta 47 no final do documento]*

#### Exercício 2
Se log₂ x = 5, qual o valor de x?

**Solução:**
2⁵ = x
x = 32

*[Ver resposta 48 no final do documento]*

#### Exercício 3
Simplifique: 5^(log₅ 7)

**Solução:**
Propriedade: a^(log_a b) = b

5^(log₅ 7) = 7

*[Ver resposta 49 no final do documento]*

#### Exercício 4
Calcule: log₂ (2^(3x)) quando x = 2

**Solução:**
log₂ (2^(3x)) = 3x = 3 × 2 = 6

*[Ver resposta 50 no final do documento]*

### Dicas para a Prova

1. **a^(log_a b) = b** (propriedade inversa)
2. **log_a (a^x) = x** (propriedade inversa)
3. **Simetria:** gráficos refletem em y = x
4. **Equação a^x = k:** aplicar log
5. **Equação log x = k:** passar para exponencial
6. **Mudança de base:** log_a b = (log b)/(log a)
7. **Domínio exp:** ℝ; **Imagem exp:** (0, +∞)
8. **Domínio log:** (0, +∞); **Imagem log:** ℝ

### Conceitos-Chave para Memorizar

**Funções Inversas:**
- f(x) = a^x ⟺ f⁻¹(x) = log_a x
- Composição = identidade
- Gráficos simétricos (y = x)

**Propriedades:**
- a^(log_a x) = x
- log_a (a^x) = x

**Domínio/Imagem:**
- Exp: D = ℝ, Im = (0,+∞)
- Log: D = (0,+∞), Im = ℝ

**Pontos Especiais:**
- Exp: (0, 1)
- Log: (1, 0)

### Fórmulas Essenciais

```
Relação Inversa:
f(x) = a^x  ⟺  f⁻¹(x) = log_a x

Composição:
a^(log_a x) = x  (x > 0)
log_a (a^x) = x  (x ∈ ℝ)

Resolver a^x = k:
x = log_a k = (log k)/(log a)

Resolver log_a x = k:
x = a^k

Mudança de Base:
log_a b = (log b)/(log a)
```

### Resumo Visual

```
SIMETRIA:

    f(x)=a^x    y=x    g(x)=log_a x
         \       /       /
          \     /       /
           \   /       /
         (0,1)/__(1,0)
             /
            /
           /

Pontos correspondentes:
Exp: (0,1), (1,a), (2,a²)
Log: (1,0), (a,1), (a²,2)

RELAÇÃO:
         Exponencial
              ↓
         y = a^x
              ↓
         Aplica log_a
              ↓
         x = log_a y
              ↓
         Logarítmica

PROPRIEDADES INVERSAS:
a^(log_a x) = x
log_a (a^x) = x
```

---

**Tempo de estudo recomendado:** 60 minutos
**Nível de dificuldade:** Médio-Alto
**Importância para a prova:** ⭐⭐⭐⭐⭐ (essencial - relação fundamental!)

---

# 🎉 PERÍODO DE FÉRIAS COMPLETO! 🎉

Você concluiu todas as **14 aulas** do período de férias (26/11 a 02/12)!

**Progresso total:** 43/96 lições concluídas (44,8%)


---

# Respostas dos Exercícios

**1.** S = {x ∈ ℝ | 2 < x < 3} ou (2, 3)

**2.** S = [1, 3]

**3.** Valor máximo = 2 (em x = 2)

**4.** 2 < x < 4 ou x ∈ (2, 4)

**5.** S = ℝ (todos os reais)

**6.** Im(f) = {y ∈ ℝ | y ≥ 1} ou [1, +∞)

**7.** k = 10

**8.** Al₂O₃ (óxido de alumínio)

**9.** S = [-3, -2] ∪ [2, 3]

**10.** S = (-∞, -2) ∪ [-1, 1] ∪ (2, +∞)

**11.** S = [2, 3)

**12.** Dimensões: 4 cm × 6 cm

**13.** Aproximadamente 4,24 s

**14.** 0 ≤ x < 10 ou x > 30 unidades

**15.** S = (-3, 2) ∪ (3, +∞)

**16.** S = [-2, 3)

**17.** Pontos (3, 9) e (-1, 1)

**18.** F─F (ligação simples)

**19.** 2 ligações duplas

**20.** **Polar**. Cl puxa mais os elétrons, formando H^(δ+)─Cl^(δ-).

**21.** a) 32; b) 1/9; c) 4

**22.** 64

**23.** x < 3 ou x ∈ (-∞, 3)

**24.** y²

**25.** x = 1

**26.** x = 0 ou x = 1

**27.** S = [0, 2]

**28.** 13.500 bactérias

**29.** 80 N

**30.** 840 N

**31.** **c) Força de reação da mesa** (perpendicular à superfície)

**32.** 5 m/s² (descendo o plano)

**33.** ≈ 3,3 m/s²

**34.** 25 N

**35.** ≈ 7 m/s²

**36.** ≈ 70 N

**37.** x = 4

**38.** x = 5

**39.** x = 2

**40.** x = 10 ou x = 100

**41.** S = (4, +∞)

**42.** S = (4, +∞)

**43.** x = √17 ou x = -√17

**44.** x = 2

**45.** 1/3

**46.** Aproximadamente 3,3 horas

**47.** x ≈ 2,73

**48.** 32

**49.** 7

**50.** 6

**O que você estudou nas férias:**
- ✅ Matemática: Função Quadrática (aprofundamento), Função Exponencial (completa), Função Logarítmica (completa), Relação Exp-Log
- ✅ Química: Ligações Químicas completas (Iônica, Covalente, Metálica) + Propriedades
- ✅ Física: Forças especiais e Plano Inclinado

**Próximos passos:**
- Semana 2: 03/12 a 07/12 (Geometria, Hidrostática, Estequiometria, Geografia, Humanas, Biologia)
- Semana 3 (final): 09/12 a 13/12 (Revisões intensivas)
- **PROVA: 14/12 - SÁBADO**

**Você está quase na metade! Continue com dedicação! 💪📚**
