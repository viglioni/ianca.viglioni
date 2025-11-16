<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import Cronograma from "@/components/Cronograma.vue";

const router = useRouter();

const checkpoints = [
  {
    date: "2025-11-23",
    display: "23/11 (Sábado)",
    title: "CHECKPOINT SEMANAL 1",
    description: "Revisar pendências da semana 1",
    tasks: [
      "REVISAR PENDÊNCIAS DA SEMANA - verificar itens não concluídos",
      "Matemática - Função quadrática (definição, coeficientes, gráfico, vértice) - 120min",
      "Matemática - Exercícios de conjuntos e função afim - 90min",
      "Biologia - Origem da vida (Terra primitiva, Hipótese de Oparin) + Características dos seres vivos - 60min",
      "Ciências Humanas - Antiguidade Ocidental (Grécia e Roma) + elementos de Arte Clássica - 90min",
      "Tempo livre para recuperar atrasos - 2h",
    ],
  },
  {
    date: "2025-12-07",
    display: "07/12 (Sábado)",
    title: "CHECKPOINT SEMANAL 2",
    description: "Revisar pendências da semana 2",
    tasks: [
      "REVISAR PENDÊNCIAS DA SEMANA",
      "Matemática - REVISÃO INTENSA Todas as funções (afim, quadrática, exp, log) - 150min",
      "Matemática - Questões discursivas e redação matemática - 90min",
      "Física - REVISÃO Dinâmica completa (Leis de Newton, forças, plano inclinado) - 90min",
      "Química - REVISÃO Ligações químicas completo - 60min",
      "Ciências Humanas - Povos originários das Américas + Arte Indígena - 60min",
      "Tempo livre para recuperar atrasos - 1h30min",
    ],
  },
];

const goToCheckpoint = (date: string) => {
  router.push({ query: { day: date } });
  // Scroll to cronograma section
  setTimeout(() => {
    const element = document.getElementById("cronograma");
    if (element) {
      const headerOffset = 100;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.scrollY - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
    }
  }, 100);
};
</script>

<template>
  <div class="plano-container">
    <div class="plano-overlay">
      <div class="content-wrapper">
        <div class="title-section">
          <h1 class="main-title">Plano de Estudos</h1>
          <p class="subtitle">SERIADO UFMG ETAPA 1</p>
        </div>

        <div class="content-section" id="intro">
          <h2 class="section-heading">📖 Lembre-se</h2>
          <ul class="remember-list">
            <li>
              🎯 A prova valoriza <strong>pensamento crítico</strong> e
              <strong>contextualização</strong>
            </li>
            <li>
              🧠 Não é decoreba - foco em <strong>compreender</strong> e
              <strong>aplicar</strong>
            </li>
            <li>📊 Use os checkpoints para não acumular atrasos</li>
            <li>💪 Férias = oportunidade de focar em exp/log sem pressão</li>
            <li>
              🌟 Você já domina biologia avançada - revisão básica é suficiente!
            </li>
            <li>📝 Anote dúvidas durante a semana e resolva no sábado</li>
          </ul>
        </div>

        <div class="content-section" id="cronograma">
          <h2 class="section-heading">📅 Cronograma</h2>
          <Cronograma />

          <div class="checkpoints-section">
            <h3 class="checkpoints-heading">🎯 Checkpoints</h3>
            <div class="checkpoint-list">
              <button
                v-for="checkpoint in checkpoints"
                :key="checkpoint.date"
                @click="goToCheckpoint(checkpoint.date)"
                class="checkpoint-item clickable"
              >
                <span class="checkpoint-date">{{ checkpoint.display }}</span>
                <span class="checkpoint-desc">{{ checkpoint.description }}</span>
              </button>
            </div>
          </div>
        </div>

        <div class="content-section" id="prioridades">
          <h2 class="section-heading">🎯 Prioridades</h2>

          <div class="priority-block alta">
            <h3>🔴 ALTA PRIORIDADE (~70% do tempo)</h3>
            <ul>
              <li>
                <strong>Matemática</strong> - foco: funções
                exponencial/logarítmica + tópicos essenciais
              </li>
              <li><strong>Física</strong></li>
              <li><strong>Química</strong> - foco: estequiometria</li>
            </ul>
          </div>

          <div class="priority-block media">
            <h3>🟡 MÉDIA PRIORIDADE (~25% do tempo)</h3>
            <ul>
              <li>
                <strong>Ciências Humanas</strong> (História + Literatura + Artes
                + Filosofia + Sociologia integrados) - MAIOR TEMPO
              </li>
              <li><strong>Geografia</strong> - MENOR TEMPO</li>
              <li>
                <strong>Português</strong> (apenas gramática) - MENOR TEMPO
              </li>
            </ul>
          </div>

          <div class="priority-block baixa">
            <h3>🟢 BAIXA PRIORIDADE (~5% do tempo)</h3>
            <ul>
              <li>
                <strong>Biologia</strong> - revisão rápida focada em conceitos
                básicos do EM
              </li>
            </ul>
          </div>
        </div>

        <div class="content-section" id="distribuicao">
          <h2 class="section-heading">📊 Distribuição de Tempo por Matéria</h2>
          <p class="content-text"><strong>Total: ~165 horas</strong></p>

          <div class="time-grid">
            <div class="time-item">
              <span class="time-label">Matemática:</span>
              <span class="time-value">~66h (40%)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Física:</span>
              <span class="time-value">~33h (20%)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Química:</span>
              <span class="time-value">~25h (15%)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Ciências Humanas:</span>
              <span class="time-value">~25h (15%)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Geografia:</span>
              <span class="time-value">~10h (6%)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Português:</span>
              <span class="time-value">~7h (4%)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Biologia:</span>
              <span class="time-value">~8h (5%)</span>
            </div>
          </div>
        </div>

        <div class="content-section" id="topicos">
          <h2 class="section-heading">📚 Tópicos Cobertos</h2>

          <div class="subject-block">
            <h3>Matemática</h3>
            <ul class="compact-list">
              <li>Conjuntos, MMC e MDC</li>
              <li>Razão, proporção e notação científica</li>
              <li>Produtos notáveis e fatoração</li>
              <li>Função afim e quadrática (completo)</li>
              <li><strong>Função exponencial (FOCO INTENSO)</strong></li>
              <li><strong>Função logarítmica (FOCO INTENSO)</strong></li>
              <li>Geometria plana, Pitágoras e trigonometria básica</li>
            </ul>
          </div>

          <div class="subject-block">
            <h3>Física</h3>
            <ul class="compact-list">
              <li>Grandezas vetoriais e escalares</li>
              <li>Cinemática: MRU, MRUV, queda livre, movimento circular</li>
              <li>Leis de Newton e dinâmica</li>
              <li>Hidrostática completa</li>
            </ul>
          </div>

          <div class="subject-block">
            <h3>Química</h3>
            <ul class="compact-list">
              <li>Propriedades e separação de misturas</li>
              <li>Modelos atômicos e tabela periódica</li>
              <li>Ligações químicas (iônica, covalente, metálica)</li>
              <li><strong>Estequiometria (FOCO INTENSO - 6h30min)</strong></li>
              <li>Reações químicas e leis ponderais</li>
            </ul>
          </div>

          <div class="subject-block">
            <h3>Ciências Humanas Integradas</h3>
            <ul class="compact-list">
              <li>Narrativas de origem + Antiguidade Oriental/Ocidental</li>
              <li>Mundo Medieval + Arte Medieval</li>
              <li>Mundo Moderno + Renascimento</li>
              <li>Povos originários das Américas</li>
              <li>Filosofia: lógica, argumentação, surgimento</li>
              <li>Sociologia: métodos, cultura, desigualdades</li>
            </ul>
          </div>
        </div>

        <div class="content-section" id="estrategia">
          <h2 class="section-heading">💡 Estratégia de Revisão</h2>
          <ul class="strategy-list">
            <li>
              <strong>1ª passada:</strong> Semana 1 (18-23/11) + Férias
              (26/11-02/12)
            </li>
            <li><strong>2ª passada:</strong> Semana 2 (03-07/12)</li>
            <li><strong>Revisão final:</strong> Semana 3 (09-13/12)</li>
            <li><strong>Checkpoints:</strong> Sábados 23/11 e 07/12</li>
          </ul>
        </div>

        <div class="content-section" id="dicas">
          <h2 class="section-heading">✨ Dicas para a Prova</h2>
          <div class="tips-grid">
            <div class="tip-card">
              <span class="tip-icon">📝</span>
              <p>
                <strong>Questões discursivas têm peso 4</strong> - priorize!
              </p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">🧠</span>
              <p>
                A prova valoriza <strong>pensamento crítico</strong> e
                <strong>contextualização</strong>
              </p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">⏰</span>
              <p>Gestão de tempo: 45 objetivas + 1-2 discursivas em 4h</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">📖</span>
              <p>
                Leia todas as questões primeiro - identifique fáceis e difíceis
              </p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">💪</span>
              <p>Sexta 13/12: DIA LEVE - descanso é estratégia!</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">🌟</span>
              <p>
                Você já domina biologia avançada - revisão básica é suficiente!
              </p>
            </div>
          </div>
        </div>

        <div class="content-section motivacao">
          <h2 class="section-heading">🚀 Sucesso nos Estudos!</h2>
          <p class="motivacao-text">
            Você consegue! Use os checkpoints para não acumular atrasos,
            aproveite as férias para dominar exp/log sem pressão, e lembre-se:
            não é decoreba - foco em <strong>compreender</strong> e
            <strong>aplicar</strong>!
          </p>
          <p class="motivacao-emoji">📚✨🍀</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

/* Main content styles */
.plano-container {
  @apply min-h-screen bg-repeat;
  background-image: url("/ufmg.plano.bg.jpg");
  background-color: #f5f1e8;
}

.plano-overlay {
  @apply min-h-screen flex items-start justify-center p-4 md:p-8 pt-24;
  background: linear-gradient(
    135deg,
    rgba(245, 241, 232, 0.88) 0%,
    rgba(255, 255, 255, 0.82) 50%,
    rgba(245, 241, 232, 0.88) 100%
  );
}

.content-wrapper {
  @apply max-w-5xl w-full pb-12;
}

.title-section {
  @apply text-center mb-12;
}

.main-title {
  @apply text-4xl md:text-5xl lg:text-6xl font-bold mb-3;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  letter-spacing: 0.02em;
}

.subtitle {
  @apply text-xl md:text-2xl mb-6;
  font-family: "Merriweather", serif;
  color: #1a5560;
  font-weight: 600;
}

.info-grid {
  @apply grid grid-cols-1 md:grid-cols-3 gap-4 mt-6;
}

.info-item {
  @apply bg-white/70 backdrop-blur-sm rounded-lg p-4 text-center;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  border: 1px solid rgba(13, 62, 71, 0.15);
}

.content-section {
  @apply flex flex-col gap-4 bg-white/70 backdrop-blur-sm rounded-lg p-6 md:p-8 shadow-lg mb-6;
  border: 2px solid rgba(13, 62, 71, 0.2);
  scroll-margin-top: 100px;
}

.section-heading {
  @apply text-2xl md:text-3xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.content-text {
  @apply text-base md:text-lg leading-relaxed;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

/* Priority blocks */
.priority-block {
  @apply p-4 rounded-lg mb-3;
  border-left: 4px solid;
}

.priority-block.alta {
  @apply bg-red-50/80;
  border-color: #dc2626;
}

.priority-block.media {
  @apply bg-yellow-50/80;
  border-color: #ca8a04;
}

.priority-block.baixa {
  @apply bg-green-50/80;
  border-color: #16a34a;
}

.priority-block h3 {
  @apply text-lg font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.priority-block ul {
  @apply list-disc list-inside ml-2 space-y-1;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

/* Time grid */
.time-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-3 mt-4;
}

.time-item {
  @apply flex justify-between p-3 bg-white/60 rounded border border-teal-200;
  font-family: "Merriweather", serif;
}

.time-label {
  @apply font-semibold;
  color: #0d3e47;
}

.time-value {
  @apply text-teal-700;
}

/* Week blocks */
.week-block {
  @apply mb-6 p-4 bg-gradient-to-r from-teal-50/60 to-cyan-50/60 rounded-lg border-l-4 border-teal-600;
}

.week-block.final {
  @apply border-amber-600 from-amber-50/60 to-yellow-50/60;
}

.week-title {
  @apply text-xl font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.week-desc {
  @apply text-base mb-2;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

.checkpoint {
  @apply text-base font-semibold mt-2;
  font-family: "Merriweather", serif;
  color: #1a5560;
}

.topic-list {
  @apply list-disc list-inside ml-4 mt-2 space-y-1;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  font-size: 0.95rem;
}

/* Subject blocks */
.subject-block {
  @apply mb-4;
}

.subject-block h3 {
  @apply text-lg font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.compact-list {
  @apply list-disc list-inside ml-2 space-y-1;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  font-size: 0.95rem;
}

/* Remember list */
.remember-list {
  @apply list-none space-y-3;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

.remember-list li {
  @apply pl-4 py-2 border-l-4 border-teal-500 bg-teal-50/40 rounded-r;
}

/* Strategy list */
.strategy-list {
  @apply list-none space-y-2;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

.strategy-list li {
  @apply pl-4 border-l-2 border-teal-400;
}

/* Tips grid */
.tips-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-4;
}

.tip-card {
  @apply p-4 bg-gradient-to-br from-teal-50/70 to-cyan-50/70 rounded-lg border border-teal-200 flex flex-col items-center text-center;
}

.tip-icon {
  @apply text-3xl mb-2;
}

.tip-card p {
  @apply text-sm;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

/* Motivation section */
.motivacao {
  @apply bg-gradient-to-r from-teal-100/80 to-cyan-100/80 border-2 border-teal-400;
}

.motivacao-text {
  @apply text-lg text-center;
  font-family: "Merriweather", serif;
  color: #0d3e47;
  line-height: 1.8;
}

.motivacao-emoji {
  @apply text-4xl text-center mt-4;
}

/* Checkpoints section */
.checkpoints-section {
  @apply mt-6 pt-6 border-t-2 border-teal-200;
}

.checkpoints-heading {
  @apply text-xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.checkpoint-list {
  @apply flex flex-col gap-3;
}

.checkpoint-item {
  @apply flex flex-col md:flex-row md:items-center gap-2 p-3 rounded-lg w-full text-left;
  background: linear-gradient(90deg, rgba(212, 175, 55, 0.1) 0%, rgba(212, 175, 55, 0.05) 100%);
  border-left: 3px solid #d4af37;
  border-top: none;
  border-right: none;
  border-bottom: none;
  font-family: "Merriweather", serif;
  cursor: default;
}

.checkpoint-item.clickable {
  @apply cursor-pointer transition-all duration-200;
}

.checkpoint-item.clickable:hover {
  background: linear-gradient(90deg, rgba(212, 175, 55, 0.2) 0%, rgba(212, 175, 55, 0.1) 100%);
  border-left-color: #b8941f;
  transform: translateX(4px);
}

.checkpoint-date {
  @apply font-bold text-base;
  color: #0d3e47;
  min-width: 140px;
}

.checkpoint-desc {
  @apply text-sm;
  color: #2d4f56;
}
</style>
