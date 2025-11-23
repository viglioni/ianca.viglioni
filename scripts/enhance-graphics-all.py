#!/usr/bin/env python3
"""
Script to add enhanced mathematical visualizations to all material files.
"""

import re
from pathlib import Path

# ==================== SEMANA 2 GRAPHICS ====================

def exponential_function_graphs():
    """Gráficos de função exponencial."""
    return """
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
"""

def logarithmic_function_graphs():
    """Gráficos de função logarítmica."""
    return """
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
"""

def quadratic_sign_study():
    """Estudo do sinal da função quadrática."""
    return """
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
"""

# ==================== SEMANA 3 GRAPHICS ====================

def triangle_types_visual():
    """Visualização dos tipos de triângulos."""
    return """
```
    TIPOS DE TRIÂNGULOS

    QUANTO AOS LADOS:
    
    Equilátero              Isósceles              Escaleno
    (3 lados iguais)        (2 lados iguais)       (lados diferentes)
    
         /\\                      /\\                     /\\
        /  \\                    /  \\                   /  \\
       /____\\                  /____\\                 /____\\
      ℓ  ℓ   ℓ                ℓ  b   ℓ              a   b   c
      
    • 3 ângulos 60°         • 2 ângulos iguais     • 3 ângulos diferentes
    
    
    QUANTO AOS ÂNGULOS:
    
    Acutângulo              Retângulo              Obtusângulo
    (3 ângulos agudos)      (1 ângulo reto)        (1 ângulo obtuso)
    
         /\\                      |\\                     /\\
        /  \\                     | \\                   /  \\___
       /____\\                    |__\\                 /      \\
      <90° <90° <90°            90°                   >90°
      
    • Todos < 90°           • Um = 90°             • Um > 90°
```
"""

def circle_elements_visual():
    """Elementos do círculo."""
    return """
```
    CÍRCULO E CIRCUNFERÊNCIA - ELEMENTOS
    
                  Diâmetro (d = 2r)
                 ←─────────→
              ╭─────────────╮
            ╱        │        ╲
          ╱          │          ╲  ← Circunferência
         │           ●───────────│    (linha)
         │         Centro        │
         │     (raio r) →        │
          ╲                     ╱
            ╲                 ╱
              ╰─────────────╯
         └──────────────────────┘
              Círculo (área)
    
    Elementos:
    • Centro: ponto fixo
    • Raio (r): distância do centro até a borda
    • Diâmetro (d): d = 2r
    • Circunferência (C): perímetro = 2πr = πd
    • Área (A): A = πr²
    
    Relações:
    • d = 2r
    • C = 2πr = πd
    • A = πr² = π(d/2)²
```
"""

def pythagorean_theorem_visual():
    """Teorema de Pitágoras visual."""
    return """
```
    TEOREMA DE PITÁGORAS
    
    Triângulo Retângulo:
    
              c (hipotenusa)
            ╱│
          ╱  │
        ╱    │ b (cateto)
      ╱      │
    ╱________│
         a
    (cateto)
    
    FÓRMULA: a² + b² = c²
    
    Onde:
    • c = hipotenusa (lado maior, oposto ao ângulo reto)
    • a, b = catetos (lados menores)
    
    
    TERNAS PITAGÓRICAS CLÁSSICAS:
    
    (3, 4, 5):      3² + 4² = 5²  →  9 + 16 = 25 ✓
    (5, 12, 13):    5² + 12² = 13²  →  25 + 144 = 169 ✓
    (8, 15, 17):    8² + 15² = 17²  →  64 + 225 = 289 ✓
    (7, 24, 25):    7² + 24² = 25²  →  49 + 576 = 625 ✓
    
    Múltiplos também funcionam:
    (6, 8, 10) = 2×(3, 4, 5)
    (9, 12, 15) = 3×(3, 4, 5)
```
"""

def trigonometry_right_triangle():
    """Razões trigonométricas no triângulo retângulo."""
    return """
```
    RAZÕES TRIGONOMÉTRICAS - TRIÂNGULO RETÂNGULO
    
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
```
"""

# ==================== SEMANA 4 GRAPHICS ====================

def formula_summary_visual():
    """Resumo visual de fórmulas essenciais."""
    return """
```
    ╔════════════════════════════════════════════════════════════╗
    ║         FÓRMULAS ESSENCIAIS - GUIA RÁPIDO                  ║
    ╚════════════════════════════════════════════════════════════╝
    
    MATEMÁTICA:
    ┌──────────────────────────────────────────────────────────┐
    │ Função Afim:      f(x) = ax + b                          │
    │ • Raiz: x = -b/a                                         │
    │ • Crescente se a > 0, Decrescente se a < 0              │
    └──────────────────────────────────────────────────────────┘
    
    ┌──────────────────────────────────────────────────────────┐
    │ Função Quadrática: f(x) = ax² + bx + c                   │
    │ • Δ = b² - 4ac                                           │
    │ • x = (-b ± √Δ) / 2a                                     │
    │ • xᵥ = -b/2a    yᵥ = -Δ/4a                              │
    │ • Concavidade ∪ se a > 0, ∩ se a < 0                    │
    └──────────────────────────────────────────────────────────┘
    
    ┌──────────────────────────────────────────────────────────┐
    │ Geometria:                                                │
    │ • Triângulo: A = (b×h)/2                                 │
    │ • Pitágoras: a² + b² = c²                                │
    │ • Círculo: A = πr²,  C = 2πr                            │
    └──────────────────────────────────────────────────────────┘
    
    FÍSICA:
    ┌──────────────────────────────────────────────────────────┐
    │ MRU:              S = S₀ + vt                            │
    │ MRUV:             v = v₀ + at                            │
    │                   S = S₀ + v₀t + at²/2                   │
    │                   v² = v₀² + 2aΔS                        │
    │ Newton:           F = ma                                  │
    │ Hidrostática:     P = ρgh (Stevin)                       │
    │                   F₁/A₁ = F₂/A₂ (Pascal)                 │
    │                   E = ρVg (Arquimedes)                   │
    └──────────────────────────────────────────────────────────┘
    
    QUÍMICA:
    ┌──────────────────────────────────────────────────────────┐
    │ Densidade:        d = m/V                                 │
    │ Mol:              n = m/M                                 │
    │                   N = n × 6,02×10²³                       │
    │ Camadas:          K L M N O P Q                          │
    │ Subcamadas:       s p d f (2 6 10 14 elétrons)          │
    └──────────────────────────────────────────────────────────┘
```
"""

def periodic_table_visual():
    """Representação simplificada da tabela periódica."""
    return """
```
    TABELA PERIÓDICA - ESTRUTURA SIMPLIFICADA
    
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
```
"""

def add_graphics_semana2(content):
    """Add graphics to semana2."""
    modifications = 0
    
    # Função exponencial
    if 'GRÁFICOS DA FUNÇÃO EXPONENCIAL' not in content:
        pattern = r'(### Gráficos Detalhados\n)'
        replacement = r'\1\n' + exponential_function_graphs() + '\n'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modifications += 1
    
    # Função logarítmica
    if 'GRÁFICOS DA FUNÇÃO LOGARÍTMICA' not in content:
        pattern = r'(### Gráfico da Função Logarítmica\n)'
        replacement = r'\1\n' + logarithmic_function_graphs() + '\n'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modifications += 1
    
    # Estudo do sinal função quadrática
    if 'ESTUDO DO SINAL - FUNÇÃO QUADRÁTICA' not in content:
        pattern = r'(### Estudo do Sinal da Função Quadrática\n)'
        replacement = r'\1\n' + quadratic_sign_study() + '\n'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modifications += 1
    
    return content, modifications

def add_graphics_semana3(content):
    """Add graphics to semana3."""
    modifications = 0
    
    # Tipos de triângulos
    if 'TIPOS DE TRIÂNGULOS' not in content:
        pattern = r'(### Triângulos - Definição e Classificação\n)'
        replacement = r'\1\n' + triangle_types_visual() + '\n'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modifications += 1
    
    # Elementos do círculo
    if 'CÍRCULO E CIRCUNFERÊNCIA - ELEMENTOS' not in content:
        pattern = r'(### Círculo e Circunferência\n)'
        replacement = r'\1\n' + circle_elements_visual() + '\n'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modifications += 1
    
    # Teorema de Pitágoras
    if 'TEOREMA DE PITÁGORAS' not in content and 'Triângulo Retângulo' in content:
        pattern = r'(### Triângulo Retângulo\n)'
        replacement = r'\1\n' + pythagorean_theorem_visual() + '\n'
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            modifications += 1
    
    # Trigonometria
    if 'RAZÕES TRIGONOMÉTRICAS - TRIÂNGULO RETÂNGULO' not in content:
        pattern = r'(## Aula \d+ - Matemática: Trigonometria no Triângulo Retângulo.*?\n### )'
        replacement = r'\1' + '\n' + trigonometry_right_triangle() + '\n\n### '
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            modifications += 1
    
    return content, modifications

def add_graphics_semana4(content):
    """Add graphics to semana4."""
    modifications = 0
    
    # Resumo de fórmulas visual
    if 'FÓRMULAS ESSENCIAIS - GUIA RÁPIDO' not in content:
        pattern = r'(## Aula 85 - Matemática: Fórmulas Essenciais - Folha de Consulta.*?\n### )'
        replacement = r'\1' + '\n' + formula_summary_visual() + '\n\n### '
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            modifications += 1
    
    # Tabela periódica visual
    if 'TABELA PERIÓDICA - ESTRUTURA SIMPLIFICADA' not in content:
        pattern = r'(### BLOCO 2: Tabela Periódica.*?\n)'
        replacement = r'\1\n' + periodic_table_visual() + '\n'
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            modifications += 1
    
    return content, modifications

def main():
    docs_dir = Path(__file__).parent.parent / 'docs'
    
    # Process semana2
    print("Processing material_semana2.md...")
    file2 = docs_dir / 'material_semana2.md'
    content2 = file2.read_text(encoding='utf-8')
    content2, mods2 = add_graphics_semana2(content2)
    file2.write_text(content2, encoding='utf-8')
    print(f"✓ Added {mods2} graphics to semana2")
    
    # Process semana3
    print("Processing material_semana3.md...")
    file3 = docs_dir / 'material_semana3.md'
    content3 = file3.read_text(encoding='utf-8')
    content3, mods3 = add_graphics_semana3(content3)
    file3.write_text(content3, encoding='utf-8')
    print(f"✓ Added {mods3} graphics to semana3")
    
    # Process semana4
    print("Processing material_semana4.md...")
    file4 = docs_dir / 'material_semana4.md'
    content4 = file4.read_text(encoding='utf-8')
    content4, mods4 = add_graphics_semana4(content4)
    file4.write_text(content4, encoding='utf-8')
    print(f"✓ Added {mods4} graphics to semana4")
    
    total = mods2 + mods3 + mods4
    print(f"\n✅ Total graphics added: {total}")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
