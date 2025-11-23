const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Mapping of current keys to better Portuguese names
const themeMapping = {
  // Matemática
  'afim': 'Função Afim',
  'algebra': 'Álgebra',
  'algebricas': 'Expressões Algébricas',
  'algarismos': 'Algarismos Significativos',
  'areas': 'Áreas',
  'conjuntos': 'Conjuntos',
  'estimativa': 'Estimativa',
  'exponencial': 'Função Exponencial',
  'fatoracao': 'Fatoração',
  'funcao': 'Funções',
  'geometria': 'Geometria',
  'inequacoes': 'Inequações',
  'intervalos': 'Intervalos',
  'lineares': 'Sistemas Lineares',
  'logaritmo': 'Logaritmo',
  'mdc': 'MDC',
  'mmc': 'MMC',
  'medida': 'Unidades de Medida',
  'notacao': 'Notação Científica',
  'notaveis': 'Produtos Notáveis',
  'numericos': 'Conjuntos Numéricos',
  'operacoes': 'Operações',
  'proporcao': 'Proporção',
  'proporcionalidade': 'Proporcionalidade',
  'quadratica': 'Função Quadrática',
  'razao': 'Razão',
  'relacao': 'Relações',
  'revisao': 'Revisão',
  'significativos': 'Algarismos Significativos',
  'sistemas': 'Sistemas',
  'subconjuntos': 'Subconjuntos',
  'triangulos': 'Triângulos',
  'trigonometria': 'Trigonometria',
  'unidades': 'Unidades',
  'variacao': 'Taxa de Variação',
  'vertice': 'Vértice',
  'zeros': 'Zeros da Função',

  // Física
  'arquimedes': 'Princípio de Arquimedes',
  'cinematica': 'Cinemática',
  'circular': 'Movimento Circular',
  'escalares': 'Grandezas Escalares',
  'especiais': 'Forças Especiais',
  'estatica': 'Estática',
  'forcas': 'Forças',
  'graficos': 'Gráficos',
  'grandezas': 'Grandezas Físicas',
  'hidrostatica': 'Hidrostática',
  'inclinado': 'Plano Inclinado',
  'livre': 'Queda Livre',
  'movimento': 'Movimento',
  'mru': 'MRU',
  'mruv': 'MRUV',
  'newton': 'Leis de Newton',
  'pascal': 'Princípio de Pascal',
  'plano': 'Plano Inclinado',
  'stevin': 'Teorema de Stevin',
  'vetores': 'Vetores',
  'vetoriais': 'Grandezas Vetoriais',

  // Química
  'atomo': 'Átomo',
  'atomica': 'Estrutura Atômica',
  'atomico': 'Número Atômico',
  'atomicos': 'Modelos Atômicos',
  'bohr': 'Modelo de Bohr',
  'calculos': 'Cálculos',
  'cientifica': 'Notação Científica',
  'covalente': 'Ligação Covalente',
  'dalton': 'Modelo de Dalton',
  'densidade': 'Densidade',
  'ebulicao': 'Temperatura de Ebulição',
  'eletrons': 'Elétrons',
  'estequiometria': 'Estequiometria',
  'estequiometricas': 'Leis Estequiométricas',
  'estrutura': 'Estrutura',
  'fusao': 'Temperatura de Fusão',
  'grupos': 'Grupos da Tabela Periódica',
  'ionica': 'Ligação Iônica',
  'ionizacao': 'Energia de Ionização',
  'leis': 'Leis',
  'ligacoes': 'Ligações Químicas',
  'massa': 'Massa Atômica',
  'metalica': 'Ligação Metálica',
  'misturas': 'Misturas',
  'modelos': 'Modelos Atômicos',
  'mol': 'Mol',
  'neutrons': 'Nêutrons',
  'organizacao': 'Organização',
  'periodica': 'Propriedades Periódicas',
  'periodos': 'Períodos da Tabela',
  'processos': 'Processos',
  'propriedades': 'Propriedades',
  'protons': 'Prótons',
  'quimica': 'Química',
  'quimicas': 'Reações Químicas',
  'radioatividade': 'Radioatividade',
  'raio': 'Raio Atômico',
  'reacoes': 'Reações',
  'rutherford': 'Modelo de Rutherford',
  'separacao': 'Separação de Misturas',
  'simbolo': 'Símbolo Químico',
  'solubilidade': 'Solubilidade',
  'substancias': 'Substâncias',
  'tabela': 'Tabela Periódica',
  'thomson': 'Modelo de Thomson',

  // Biologia
  'bacterias': 'Bactérias',
  'celula': 'Célula',
  'caracteristicas': 'Características dos Seres Vivos',
  'composicao': 'Composição Química',
  'dna': 'DNA',
  'eucariotos': 'Células Eucariotas',
  'funcoes': 'Funções',
  'hipotese': 'Hipótese de Oparin',
  'niveis': 'Níveis de Organização',
  'oparin': 'Hipótese de Oparin',
  'organelas': 'Organelas',
  'origem': 'Origem da Vida',
  'primitiva': 'Terra Primitiva',
  'procariotos': 'Células Procariotas',
  'seres': 'Seres Vivos',
  'terra': 'Terra Primitiva',
  'vida': 'Origem da Vida',
  'virus': 'Vírus',
  'vivos': 'Seres Vivos',

  // Geografia
  'americas': 'Américas',
  'cartografia': 'Cartografia',
  'clima': 'Clima',
  'climatologia': 'Climatologia',
  'coordenadas': 'Coordenadas Geográficas',
  'curvas': 'Curvas de Nível',
  'elementos': 'Elementos do Mapa',
  'escalas': 'Escalas',
  'estrutura': 'Estrutura Geológica',
  'fusos': 'Fusos Horários',
  'geograficas': 'Coordenadas Geográficas',
  'geologica': 'Estrutura Geológica',
  'horarios': 'Fusos Horários',
  'mapas': 'Mapas',
  'nivel': 'Curvas de Nível',
  'projecoes': 'Projeções Cartográficas',

  // Ciências Humanas (História)
  'antiguidade': 'Antiguidade',
  'argumento': 'Argumento',
  'arte': 'Arte',
  'artes': 'Artes',
  'classica': 'Arte Clássica',
  'falacia': 'Falácia',
  'filosofia': 'Filosofia',
  'grecia': 'Grécia Antiga',
  'historia': 'História',
  'logica': 'Lógica',
  'medieval': 'Idade Média',
  'metodos': 'Métodos de Pesquisa',
  'narrativas': 'Narrativas de Origem',
  'ocidental': 'Antiguidade Ocidental',
  'oriental': 'Antiguidade Oriental',
  'pesquisa': 'Métodos de Pesquisa',
  'qualitativo': 'Método Qualitativo',
  'quantitativo': 'Método Quantitativo',
  'renascimento': 'Renascimento',
  'roma': 'Roma Antiga',
  'sociologia': 'Sociologia',
  'tardia': 'Antiguidade Tardia',
  'validade': 'Validade do Argumento',

  // Português
  'concordancia': 'Concordância',
  'modo': 'Modo Verbal',
  'nominal': 'Concordância Nominal',
  'tempo': 'Tempo Verbal',
  'verbal': 'Concordância Verbal',
  'verbais': 'Tempos Verbais',
  'verbos': 'Verbos',

  // Geral
  'exercicios': 'Exercícios',
  'geral': 'Revisão Geral',
};

// Update codes themes
Object.keys(data.codes).forEach(code => {
  const codeData = data.codes[code];
  codeData.themes = codeData.themes.map(theme => themeMapping[theme] || theme);
});

// Rebuild themes index with new names
const newThemes = {};

Object.keys(data.codes).forEach(code => {
  const codeData = data.codes[code];
  codeData.themes.forEach(theme => {
    if (!newThemes[theme]) {
      newThemes[theme] = {
        codes: [],
        subjects: []
      };
    }
    newThemes[theme].codes.push({ code });
    if (!newThemes[theme].subjects.includes(codeData.subject)) {
      newThemes[theme].subjects.push(codeData.subject);
    }
  });
});

// Sort everything
Object.keys(newThemes).forEach(theme => {
  newThemes[theme].codes.sort((a, b) => a.code.localeCompare(b.code));
  newThemes[theme].subjects.sort();
});

const sortedThemes = {};
Object.keys(newThemes).sort().forEach(key => {
  sortedThemes[key] = newThemes[key];
});

data.themes = sortedThemes;

fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2));
console.log('Fixed theme names to proper Portuguese with accents');
console.log('Total themes:', Object.keys(sortedThemes).length);
console.log('Sample themes:', Object.keys(sortedThemes).slice(0, 10));
