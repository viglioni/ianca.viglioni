# SERIADO UFMG - Org-mode Build Pipeline

Este diretório contém scripts para converter os materiais de estudo do formato Markdown para Org-mode e exportar para PDF e HTML.

## Visão Geral

O pipeline de conversão segue estes passos:

```
Markdown (.md) → Org-mode (.org) → PDF + HTML
```

### Estrutura de Diretórios

```
ianca.viglioni/
├── docs/
│   ├── material_semana1.md      # Materiais fonte em Markdown
│   ├── material_ferias.md
│   ├── material_semana2.md
│   ├── material_semana3.md
│   ├── org/                      # Arquivos Org-mode gerados
│   │   ├── material_semana1.org
│   │   ├── material_ferias.org
│   │   ├── material_semana2.org
│   │   └── material_semana3.org
│   └── output/
│       ├── html/                 # Arquivos HTML exportados
│       │   ├── material_semana1.html
│       │   └── ...
│       ├── pdf/                  # Arquivos PDF exportados (requer LaTeX)
│       │   ├── material_semana1.pdf
│       │   └── ...
│       └── css/
│           └── org-style.css     # Stylesheet para HTML
└── scripts/
    ├── md2org.sh                 # Converte MD → Org
    ├── build-pdf.sh              # Exporta Org → PDF
    ├── build-html.sh             # Exporta Org → HTML
    ├── build-all.sh              # Executa pipeline completo
    └── README.md                 # Este arquivo
```

## Pré-requisitos

### Obrigatórios

1. **Pandoc** - Para conversão Markdown → Org-mode
   ```bash
   brew install pandoc
   ```

2. **Emacs** - Para exportar Org-mode → HTML (e opcionalmente PDF)
   ```bash
   brew install emacs
   # ou
   brew install emacs-plus
   ```

### Opcional (para PDFs)

3. **LaTeX** - Para gerar PDFs de alta qualidade
   ```bash
   brew install --cask basictex
   # Após instalação, reinicie o terminal ou execute:
   eval "$(/usr/libexec/path_helper)"
   ```

## Como Usar

### Opção 1: Pipeline Completo (Recomendado)

Execute tudo de uma vez:

```bash
cd scripts
./build-all.sh
```

Isso irá:
1. Converter todos os arquivos `.md` para `.org`
2. Exportar todos os arquivos `.org` para PDF (se LaTeX estiver instalado)
3. Exportar todos os arquivos `.org` para HTML

### Opção 2: Passos Individuais

#### 1. Converter Markdown para Org-mode

```bash
cd scripts
./md2org.sh
```

**O que faz:**
- Lê todos os arquivos `docs/material_*.md`
- Converte para Org-mode usando Pandoc
- Adiciona headers com configurações LaTeX e HTML
- Salva em `docs/org/`

**Configurações adicionadas:**
- Metadados (título, autor, data)
- Pacotes LaTeX (amsmath, tikz, babel, geometry)
- Headers HTML (MathJax para fórmulas, viewport responsivo)
- Configurações de exportação (TOC, níveis de título)

#### 2. Gerar PDFs

```bash
./build-pdf.sh
```

**O que faz:**
- Tenta exportar usando Emacs Org-mode (melhor qualidade)
- Se Emacs falhar, usa Pandoc como fallback
- Salva PDFs em `docs/output/pdf/`

**Requer:**
- LaTeX (pdflatex ou xelatex)
- Se não instalado, este passo será pulado

**Características dos PDFs:**
- Formatação profissional com LaTeX
- Fórmulas matemáticas renderizadas com alta qualidade
- Cabeçalhos personalizados (SERIADO UFMG)
- Margens de 2cm
- Suporte a caracteres brasileiros (babel)

#### 3. Gerar HTML

```bash
./build-html.sh
```

**O que faz:**
- Exporta arquivos Org para HTML usando Emacs
- Se Emacs falhar, usa Pandoc como fallback
- Salva HTMLs em `docs/output/html/`

**Características dos HTMLs:**
- MathJax para renderização de fórmulas matemáticas
- CSS customizado (`../css/org-style.css`)
- Responsivo (mobile-friendly)
- Tabela de conteúdos navegável
- Código com syntax highlighting

## Arquivos Gerados

### Arquivos Org-mode

Cada arquivo `.org` gerado contém:

```org
#+TITLE: Semana 1 - Fundamentos (18-23 Nov)
#+AUTHOR: Material de Estudo SERIADO UFMG
#+DATE: 2025-11-16
#+OPTIONS: toc:2 num:t H:4 ^:nil
#+LATEX_CLASS: article
#+LATEX_HEADER: \usepackage[brazil]{babel}
#+LATEX_HEADER: \usepackage{amsmath,amssymb}
#+HTML_HEAD: <link rel="stylesheet" href="../css/org-style.css"/>
#+HTML_HEAD: <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

* Conteúdo...
```

### Arquivo CSS

O arquivo `docs/output/css/org-style.css` fornece:

- Tipografia profissional
- Cores e espaçamento otimizados para leitura
- Suporte para tabelas, código, citações
- Design responsivo
- Estilos de impressão
- Destaque para exercícios e exemplos

## Personalização

### Modificar Headers dos Arquivos Org

Edite a função `add_org_headers()` em `md2org.sh`:

```bash
add_org_headers() {
    local org_file=$1
    local title=$2
    
    cat > "${org_file}.tmp" << EOF
#+TITLE: ${title}
# Adicione suas personalizações aqui
EOF
}
```

### Modificar Estilo HTML

Edite `docs/output/css/org-style.css` para customizar:

- Cores (variáveis CSS em `:root`)
- Fontes
- Espaçamentos
- Layout responsivo

### Modificar Configuração PDF

Edite a variável `EMACS_CONFIG` em `build-pdf.sh`:

```bash
EMACS_CONFIG=$(cat << 'EOF'
(require 'ox-latex)
# Adicione suas configurações Emacs Lisp aqui
EOF
)
```

## Solução de Problemas

### "pandoc: command not found"

```bash
brew install pandoc
```

### "emacs: command not found"

```bash
brew install emacs
```

### PDFs não são gerados

Instale LaTeX:
```bash
brew install --cask basictex
eval "$(/usr/libexec/path_helper)"
```

### HTML sem fórmulas matemáticas

Verifique se MathJax está sendo carregado:
- Abra o HTML no navegador
- Abra o console (F12)
- Procure por erros do MathJax
- Verifique conexão com internet (MathJax é CDN)

### CSS não está sendo aplicado

Verifique os caminhos:
- HTML está em: `docs/output/html/`
- CSS está em: `docs/output/css/org-style.css`
- Caminho relativo no HTML: `../css/org-style.css`

## Fluxo de Trabalho Recomendado

1. **Edite os materiais** nos arquivos Markdown (`docs/material_*.md`)

2. **Converta para Org-mode** quando quiser testar a visualização:
   ```bash
   ./md2org.sh
   ```

3. **Gere HTML** para visualização rápida no navegador:
   ```bash
   ./build-html.sh
   ```

4. **Gere PDFs** quando estiver pronto para distribuição final:
   ```bash
   ./build-pdf.sh
   ```

5. **Ou execute tudo de uma vez**:
   ```bash
   ./build-all.sh
   ```

## Integração com Vue

Os arquivos HTML podem ser integrados na aplicação Vue de duas formas:

### Opção 1: Servir HTMLs estáticos

Copie os HTMLs para `public/materials/`:

```bash
cp docs/output/html/*.html public/materials/
```

No Vue Router:
```javascript
{
  path: '/material/:semana',
  name: 'Material',
  component: () => import('@/views/Material.vue')
}
```

### Opção 2: Converter para componentes Vue

Use os HTMLs gerados como base e converta o conteúdo para componentes Vue, mantendo a estrutura e usando o MathJax para fórmulas.

## Recursos

### MathJax

Fórmulas inline: `\( x = \frac{-b \pm \sqrt{b^2-4ac}}{2a} \)`

Fórmulas display: `\[ E = mc^2 \]`

### Org-mode

- [Manual Oficial](https://orgmode.org/manual/)
- [Org Export Reference](https://orgmode.org/manual/Exporting.html)
- [LaTeX Export](https://orgmode.org/manual/LaTeX-Export.html)
- [HTML Export](https://orgmode.org/manual/HTML-Export.html)

### Pandoc

- [Manual](https://pandoc.org/MANUAL.html)
- [Org-mode Output](https://pandoc.org/org.html)

## Licença

Material de estudo para SERIADO UFMG - Uso educacional.

## Suporte

Para questões ou problemas, consulte:
- Logs de erro gerados pelos scripts
- Documentação do Org-mode
- Documentação do Pandoc
