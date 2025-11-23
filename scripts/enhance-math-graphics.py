#!/usr/bin/env python3
"""
Script to enhance mathematical visualizations in Markdown files.
Adds improved ASCII diagrams for Venn diagrams, intervals, and graphs.
"""

import re
import sys
from pathlib import Path

def create_venn_diagram_two_sets():
    """Create a visual Venn diagram for two sets."""
    return """
```
        DIAGRAMA DE VENN - DOIS CONJUNTOS
        
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
    • Região A apenas: A - B (A ∩ B̄)
    • Região B apenas: B - A (Ā ∩ B)
    • Interseção X: A ∩ B
    • União: A ∪ B (tudo dentro dos círculos)
    • Complemento: Fora dos círculos
```
"""

def create_interval_line():
    """Create visual interval representations."""
    return """
```
    REPRESENTAÇÃO DE INTERVALOS NA RETA NUMÉRICA

    [a, b] - Intervalo Fechado (inclui ambos extremos)
    ────●═══════════●────────────────────────────
        a           b
    
    (a, b) - Intervalo Aberto (exclui ambos extremos)
    ────○───────────○────────────────────────────
        a           b
    
    [a, b) - Fechado à esquerda, Aberto à direita
    ────●═══════════○────────────────────────────
        a           b
    
    (a, b] - Aberto à esquerda, Fechado à direita
    ────○───────────●────────────────────────────
        a           b
    
    [a, +∞) - Intervalo ilimitado à direita
    ────●═══════════════════════════════════════→
        a
    
    (-∞, b] - Intervalo ilimitado à esquerda
    ←═══════════════●────────────────────────────
                    b
    
    Símbolos: ● = inclui ponto    ○ = exclui ponto
              ═ = pertence        ─ = não pertence
```
"""

def create_function_graph_template():
    """Create a coordinate plane template."""
    return """
```
    PLANO CARTESIANO
    
          y
          │
        4 ├─────────────────
        3 ├─────────────────
        2 ├─────────────────
        1 ├─────────────────
    ──────┼─────────────────── x
       -2-1 0  1  2  3  4
       -1 ├─────────────────
       -2 ├─────────────────
          │
    
    • Quadrante I:   (+, +)
    • Quadrante II:  (-, +)
    • Quadrante III: (-, -)
    • Quadrante IV:  (+, -)
```
"""

def create_linear_function_graph():
    """Create visual representation of linear function."""
    return """
```
    GRÁFICO FUNÇÃO AFIM: f(x) = ax + b
    
    Se a > 0 (crescente):        Se a < 0 (decrescente):
    
         y                            y
         │         ╱                  │╲
         │        ╱                   │ ╲
         │       ╱                    │  ╲
         │      ╱                     │   ╲
    ─────┼─────╱────── x         ─────┼────╲──── x
         │    ╱                        │     ╲
         │   ╱                         │      ╲
         │  ╱                          │       ╲
         
    • Coeficiente angular a: inclinação
    • Coeficiente linear b: interseção com eixo y
    • Raiz (zero): ponto onde f(x) = 0
```
"""

def create_quadratic_function_graph():
    """Create visual representation of quadratic function."""
    return """
```
    GRÁFICO FUNÇÃO QUADRÁTICA: f(x) = ax² + bx + c
    
    Se a > 0 (concavidade para cima):
    
         y
         │
         │      ╱│╲
         │     ╱ │ ╲
         │    ╱  │  ╲
         │   ╱   │   ╲
    ─────┼──────(V)────── x
       x₁│       xᵥ    x₂
         │
    
    Se a < 0 (concavidade para baixo):
    
         y
         │      x₁ xᵥ x₂
    ─────┼──────(Λ)────── x
         │   ╲   │   ╱
         │    ╲  │  ╱
         │     ╲ │ ╱
         │      ╲│╱
    
    Elementos importantes:
    • Vértice V(xᵥ, yᵥ): xᵥ = -b/2a
    • Raízes x₁ e x₂: pontos onde f(x) = 0
    • Eixo de simetria: x = xᵥ
    • Δ = b² - 4ac (discriminante)
      - Δ > 0: duas raízes reais distintas
      - Δ = 0: uma raiz real (dupla)
      - Δ < 0: nenhuma raiz real
```
"""

def create_mru_graphs():
    """Create MRU (uniform motion) graphs."""
    return """
```
    GRÁFICOS DO MOVIMENTO RETILÍNEO UNIFORME (MRU)
    
    1. Posição × Tempo (S × t)     2. Velocidade × Tempo (v × t)
    
       S                               v
       │     ╱                          │  ┌─────────┐
       │    ╱                           │  │         │
       │   ╱  (reta)                    │  │(constante)
       │  ╱                             │  │         │
       │ ╱                              └──┴─────────┴─── t
       └─────────── t                      
       
    Características:
    • S × t: Reta (inclinação = velocidade v)
    • v × t: Horizontal (velocidade constante)
    • S = S₀ + vt
    • Área sob v × t = deslocamento
```
"""

def create_mruv_graphs():
    """Create MRUV (uniformly accelerated motion) graphs."""
    return """
```
    GRÁFICOS DO MOVIMENTO RETILÍNEO UNIFORMEMENTE VARIADO (MRUV)
    
    1. Velocidade × Tempo          2. Posição × Tempo
    
       v                              S
       │    ╱                          │      ╱╲
       │   ╱                           │     ╱  ╲
       │  ╱ (reta)                     │    ╱    ╲ (parábola)
       │ ╱                             │   ╱      ╲
       └─────────── t                  └──────────── t
       
    3. Aceleração × Tempo
    
       a
       │  ┌─────────┐
       │  │(constante)
       │  │         │
       └──┴─────────┴─── t
    
    Características:
    • v × t: Reta (inclinação = aceleração a)
    • S × t: Parábola
    • a × t: Horizontal (aceleração constante)
    • Área sob v × t = deslocamento
    • Área sob a × t = variação de velocidade
```
"""

def enhance_venn_section(content):
    """Add enhanced Venn diagram after Venn section."""
    pattern = r'(### Diagrama de Venn\n\n.*?\n\n)'
    venn = create_venn_diagram_two_sets()
    replacement = r'\1' + venn + '\n\n'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def enhance_interval_section(content):
    """Add enhanced interval visualization."""
    pattern = r'(### Intervalos Numéricos\n\n.*?Representação gráfica: ○━━━━━●\n)'
    intervals = create_interval_line()
    replacement = r'\1\n' + intervals + '\n'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def enhance_linear_function_section(content):
    """Add linear function graph visualization."""
    pattern = r'(## Aula \d+ - Matemática: Função Afim.*?### Gráfico da Função Afim\n)'
    if 'GRÁFICO FUNÇÃO AFIM' not in content:
        graph = create_linear_function_graph()
        replacement = r'\1\n' + graph + '\n'
        return re.sub(pattern, replacement, content, flags=re.DOTALL)
    return content

def enhance_quadratic_function_section(content):
    """Add quadratic function graph visualization."""
    pattern = r'(## Aula \d+ - Matemática: Função Quadrática.*?### Gráfico\n)'
    if 'GRÁFICO FUNÇÃO QUADRÁTICA' not in content:
        graph = create_quadratic_function_graph()
        replacement = r'\1\n' + graph + '\n'
        return re.sub(pattern, replacement, content, flags=re.DOTALL)
    return content

def enhance_mru_section(content):
    """Add MRU graphs."""
    if 'GRÁFICOS DO MOVIMENTO RETILÍNEO UNIFORME' not in content:
        pattern = r'(### Gráfico S × t \(Posição × Tempo\)\n)'
        graph = create_mru_graphs()
        replacement = graph + '\n\n' + r'\1'
        return re.sub(pattern, replacement, content)
    return content

def enhance_mruv_section(content):
    """Add MRUV graphs."""
    if 'GRÁFICOS DO MOVIMENTO RETILÍNEO UNIFORMEMENTE VARIADO' not in content:
        pattern = r'(### Gráficos do MRUV\n)'
        graph = create_mruv_graphs()
        replacement = r'\1\n' + graph + '\n'
        return re.sub(pattern, replacement, content)
    return content

def process_file(file_path):
    """Process a single markdown file to add enhanced graphics."""
    print(f"Processing {file_path.name}...")
    
    content = file_path.read_text(encoding='utf-8')
    original_length = len(content)
    
    # Apply enhancements
    content = enhance_venn_section(content)
    content = enhance_interval_section(content)
    content = enhance_linear_function_section(content)
    content = enhance_quadratic_function_section(content)
    content = enhance_mru_section(content)
    content = enhance_mruv_section(content)
    
    # Write back
    file_path.write_text(content, encoding='utf-8')
    
    added = len(content) - original_length
    print(f"✓ {file_path.name} processed - added {added} characters of graphics")

def main():
    docs_dir = Path(__file__).parent.parent / 'docs'
    files = sorted(docs_dir.glob('material_semana*.md'))
    
    if not files:
        print("No material_semana*.md files found")
        return 1
    
    print(f"Found {len(files)} files to process\n")
    
    for file_path in files:
        process_file(file_path)
    
    print(f"\n✅ All files enhanced with improved graphics!")
    return 0

if __name__ == '__main__':
    sys.exit(main())
