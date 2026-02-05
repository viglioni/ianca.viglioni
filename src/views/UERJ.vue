<script setup lang="ts">
import { ref } from "vue";

const selectedMonth = ref("fevereiro");

const months = [
  { id: "fevereiro", name: "Fevereiro" },
  { id: "marco", name: "Março" },
  { id: "abril", name: "Abril" },
  { id: "maio", name: "Maio" },
  { id: "junho", name: "Junho" },
  { id: "julho", name: "Julho" },
];
</script>

<template>
  <div class="uerj-container">
    <!-- Header com logo -->
    <div class="header-section">
      <img src="/uerj.bg.webp" alt="UERJ Logo" class="logo" />
    </div>

    <!-- Overlay com conteúdo -->
    <div class="uerj-overlay">
      <div class="content-wrapper">
        <!-- Título -->
        <div class="title-section">
          <h1 class="main-title">UERJ 2026</h1>
          <p class="subtitle">Cronograma de Estudos</p>
          <p class="period">10/02/2026 a 01/08/2026</p>
        </div>

        <!-- Estrutura Semanal -->
        <div class="content-section">
          <h2 class="section-heading">📋 Estrutura Semanal Padrão</h2>

          <div class="week-grid">
            <div class="schedule-card">
              <h3 class="schedule-title">Segunda a Sexta (9h/dia)</h3>
              <ul class="schedule-list">
                <li><strong>08:00-12:00</strong> Matemática (4h)</li>
                <li><strong>12:00-13:00</strong> Almoço</li>
                <li><strong>13:00-16:30</strong> Química/Física/Biologia (3,5h)</li>
                <li><strong>16:30-17:00</strong> Intervalo</li>
                <li><strong>17:00-18:00</strong> Humanas (1h)</li>
                <li><strong>18:00-18:30</strong> Flashcards Anki (0,5h)</li>
              </ul>
            </div>

            <div class="schedule-card">
              <h3 class="schedule-title">Sábado (6h)</h3>
              <ul class="schedule-list">
                <li><strong>09:00-15:00</strong> Revisão semanal</li>
                <li>Análise de erros</li>
                <li>Flashcards</li>
              </ul>
            </div>

            <div class="schedule-card highlight">
              <h3 class="schedule-title">Domingo</h3>
              <p class="rest-day">🌟 Descanso total</p>
            </div>
          </div>
        </div>

        <!-- Rotação de Disciplinas -->
        <div class="content-section">
          <h2 class="section-heading">🎯 Rotação de Disciplinas</h2>

          <div class="rotation-grid">
            <div class="rotation-card">
              <h3 class="rotation-title">Alta Complexidade</h3>
              <p class="rotation-subtitle">Matemática é estudada TODOS os dias</p>
              <ul class="rotation-list">
                <li><span class="day">Segunda:</span> Matemática + Química</li>
                <li><span class="day">Terça:</span> Matemática + Física</li>
                <li><span class="day">Quarta:</span> Matemática + Química</li>
                <li><span class="day">Quinta:</span> Matemática + Física</li>
                <li><span class="day">Sexta:</span> Matemática + Biologia</li>
              </ul>
              <div class="warning">
                ⚠️ <strong>Regra:</strong> Física e Química nunca no mesmo dia
              </div>
            </div>

            <div class="rotation-card">
              <h3 class="rotation-title">Humanas (1h diária)</h3>
              <p class="rotation-subtitle">Rotação semanal</p>
              <ul class="rotation-list">
                <li><span class="week-num">Sem 1:</span> Literatura</li>
                <li><span class="week-num">Sem 2:</span> Gramática</li>
                <li><span class="week-num">Sem 3:</span> História</li>
                <li><span class="week-num">Sem 4:</span> Geografia</li>
                <li><span class="week-num">Sem 5:</span> Literatura</li>
                <li><span class="week-num">Sem 6:</span> Filosofia/Sociologia</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Seletor de Mês -->
        <div class="content-section">
          <h2 class="section-heading">📅 Cronograma Mensal Detalhado</h2>

          <div class="month-selector">
            <button
              v-for="month in months"
              :key="month.id"
              @click="selectedMonth = month.id"
              :class="['month-btn', { active: selectedMonth === month.id }]"
            >
              {{ month.name }}
            </button>
          </div>

          <!-- Fevereiro -->
          <div v-if="selectedMonth === 'fevereiro'" class="month-detail">
            <h3 class="month-title">📚 Fevereiro 2026</h3>

            <div class="meta-box">
              <h4 class="meta-title">Meta do Mês</h4>
              <div class="meta-grid">
                <div class="meta-item">Matemática A: Tópicos 1-7</div>
                <div class="meta-item">Química A: Tópicos 1-8</div>
                <div class="meta-item">Física A: Tópicos 1-6</div>
                <div class="meta-item">Biologia A: Tópicos 1-6</div>
                <div class="meta-item">Literatura: Tópicos 1-3</div>
                <div class="meta-item highlight">🎯 1 simulado UERJ (16/02)</div>
              </div>
            </div>

            <!-- Semana 1 -->
            <div class="week-detail">
              <h4 class="week-detail-title">Semana 1: 10-15/02</h4>

              <div class="day-card">
                <div class="day-header">
                  <span class="day-name">Segunda 10/02</span>
                  <span class="day-hours">9h</span>
                </div>
                <ul class="day-tasks">
                  <li>
                    <strong>Matemática (4h):</strong> Tópico 1 - Conjuntos numéricos
                  </li>
                  <li>
                    <strong>Química (3,5h):</strong> Tópico 1 - Leis ponderais e Teoria
                    atômica
                  </li>
                  <li>
                    <strong>Literatura (1h):</strong> Textos Literários e Figuras de
                    Linguagem
                  </li>
                  <li><strong>Anki (0,5h):</strong> Criar cards</li>
                </ul>
              </div>

              <div class="day-card">
                <div class="day-header">
                  <span class="day-name">Terça 11/02</span>
                  <span class="day-hours">9h</span>
                </div>
                <ul class="day-tasks">
                  <li><strong>Matemática (4h):</strong> Tópico 2 - Teoria dos conjuntos</li>
                  <li>
                    <strong>Física (3,5h):</strong> Introdução à Cinemática e Movimento
                    Uniforme
                  </li>
                  <li>
                    <strong>Literatura (1h):</strong> Figuras de linguagem (exercícios)
                  </li>
                  <li><strong>Anki (0,5h):</strong> Revisão</li>
                </ul>
              </div>

              <div class="day-card">
                <div class="day-header">
                  <span class="day-name">Quarta 12/02</span>
                  <span class="day-hours">9h</span>
                </div>
                <ul class="day-tasks">
                  <li>
                    <strong>Matemática (4h):</strong> Tópico 3 - Divisibilidade, MDC e MMC
                  </li>
                  <li>
                    <strong>Química (3,5h):</strong> Tópico 2 - Natureza elétrica da matéria
                  </li>
                  <li>
                    <strong>Literatura (1h):</strong> Exercícios UERJ (figuras de linguagem)
                  </li>
                  <li><strong>Anki (0,5h):</strong> Revisão</li>
                </ul>
              </div>

              <div class="day-card">
                <div class="day-header">
                  <span class="day-name">Quinta 13/02</span>
                  <span class="day-hours">9h</span>
                </div>
                <ul class="day-tasks">
                  <li>
                    <strong>Matemática (4h):</strong> Tópico 4 - Produtos notáveis e
                    fatoração
                  </li>
                  <li>
                    <strong>Física (3,5h):</strong> Tópico 2 - Movimento Uniformemente
                    Variado
                  </li>
                  <li><strong>Literatura (1h):</strong> Gênero épico e dramático</li>
                  <li><strong>Anki (0,5h):</strong> Revisão</li>
                </ul>
              </div>

              <div class="day-card">
                <div class="day-header">
                  <span class="day-name">Sexta 14/02</span>
                  <span class="day-hours">9h</span>
                </div>
                <ul class="day-tasks">
                  <li>
                    <strong>Matemática (4h):</strong> Tópico 5 - Potenciação e radiciação
                  </li>
                  <li>
                    <strong>Biologia (3,5h):</strong> Bioquímica: Água e Sais Minerais
                  </li>
                  <li><strong>Literatura (1h):</strong> Exercícios de gêneros textuais</li>
                  <li><strong>Anki (0,5h):</strong> Revisão</li>
                </ul>
              </div>

              <div class="day-card review">
                <div class="day-header">
                  <span class="day-name">Sábado 15/02</span>
                  <span class="day-hours">6h</span>
                </div>
                <ul class="day-tasks">
                  <li>Revisão geral da semana</li>
                  <li>Revisitar exercícios com erro</li>
                  <li>Flashcards: Revisão espaçada</li>
                </ul>
              </div>

              <div class="week-meta">
                <strong>✅ Meta Semanal:</strong> Mat A 1-5 • Qui A 1-2 • Fís A 1-2 • Bio A 1
                • Lit 1-2
              </div>
            </div>

            <div class="info-note">
              📌 O cronograma completo de todas as semanas (fevereiro a julho) está disponível
              no arquivo <code>cronograma-vestibular-2026.md</code>
            </div>
          </div>

          <!-- Outros meses -->
          <div v-else class="month-detail">
            <h3 class="month-title">
              📚 {{ months.find((m) => m.id === selectedMonth)?.name }} 2026
            </h3>
            <div class="info-note">
              📌 Conteúdo detalhado disponível em
              <code>cronograma-vestibular-2026.md</code>
            </div>
          </div>
        </div>

        <!-- Dicas -->
        <div class="content-section tips">
          <h2 class="section-heading">💡 Lembre-se</h2>
          <div class="tips-grid">
            <div class="tip-card">
              <span class="tip-icon">🎯</span>
              <p>Foco nos tópicos mais recorrentes da UERJ até junho</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">📊</span>
              <p>Total: ~1.450 horas de estudo</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">📝</span>
              <p>16 simulados UERJ + 7 ENEM + 7 redações</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">💪</span>
              <p>Abril: carga reduzida (4 dias, 5h) - sem simulados</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">🔥</span>
              <p>Maio: intensificação (2 UERJ + 1 ENEM por semana)</p>
            </div>
            <div class="tip-card">
              <span class="tip-icon">🌟</span>
              <p>Use Anki diariamente para revisão espaçada</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.uerj-container {
  @apply min-h-screen;
  background: linear-gradient(135deg, #2c3e40 0%, #1e2a2d 100%);
}

.header-section {
  @apply w-full flex items-center justify-center py-8 md:py-12 border-b-2;
  background-color: #32373a;
  border-color: #c9a961;
}

.logo {
  @apply h-32 md:h-40 object-contain;
}

.uerj-overlay {
  @apply min-h-screen flex items-start justify-center p-4 md:p-8;
}

.content-wrapper {
  @apply max-w-6xl w-full pb-12;
}

.title-section {
  @apply text-center mb-8 md:mb-12;
}

.main-title {
  @apply text-4xl md:text-6xl lg:text-7xl font-bold mb-3;
  font-family: "Crimson Text", serif;
  color: #e74c3c;
  text-shadow: 0 2px 8px rgba(231, 76, 60, 0.4);
}

.subtitle {
  @apply text-xl md:text-2xl lg:text-3xl font-semibold mb-2;
  font-family: "Merriweather", serif;
  color: #c9a961;
}

.period {
  @apply text-base md:text-lg;
  font-family: "Merriweather", serif;
  color: #ecf0f1;
  opacity: 0.9;
}

.content-section {
  @apply bg-white/5 backdrop-blur-sm rounded-lg p-4 md:p-8 mb-6 md:mb-8;
  border: 1px solid rgba(201, 169, 97, 0.2);
}

.content-section.tips {
  @apply bg-gradient-to-br from-amber-900/20 to-orange-900/20;
  border-color: rgba(201, 169, 97, 0.3);
}

.section-heading {
  @apply text-2xl md:text-3xl font-bold mb-4 md:mb-6;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

/* Week Grid */
.week-grid {
  @apply grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6;
}

.schedule-card {
  @apply bg-black/30 p-4 md:p-6 rounded-lg;
  border: 1px solid rgba(93, 173, 226, 0.2);
}

.schedule-card.highlight {
  @apply bg-green-900/20 border-green-500/30;
}

.schedule-title {
  @apply text-lg md:text-xl font-bold mb-3 md:mb-4;
  color: #5dade2;
  font-family: "Crimson Text", serif;
}

.schedule-list {
  @apply space-y-2 text-sm md:text-base;
  color: #ecf0f1;
  font-family: "Merriweather", serif;
}

.rest-day {
  @apply text-xl md:text-2xl text-center;
  color: #4ade80;
}

/* Rotation Grid */
.rotation-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6;
}

.rotation-card {
  @apply bg-black/30 p-4 md:p-6 rounded-lg;
  border: 1px solid rgba(201, 169, 97, 0.3);
}

.rotation-title {
  @apply text-lg md:text-xl font-bold mb-2;
  color: #c9a961;
  font-family: "Crimson Text", serif;
}

.rotation-subtitle {
  @apply text-sm md:text-base mb-3 md:mb-4;
  color: #5dade2;
  font-family: "Merriweather", serif;
  font-style: italic;
}

.rotation-list {
  @apply space-y-2 text-sm md:text-base mb-4;
  color: #ecf0f1;
  font-family: "Merriweather", serif;
}

.day,
.week-num {
  @apply font-semibold;
  color: #c9a961;
}

.warning {
  @apply mt-4 p-3 bg-red-900/30 rounded border-l-4 border-red-500 text-sm md:text-base;
  color: #ff6b6b;
}

/* Month Selector */
.month-selector {
  @apply flex flex-wrap gap-2 md:gap-3 mb-6 md:mb-8;
}

.month-btn {
  @apply px-4 md:px-6 py-2 md:py-3 rounded-lg font-semibold transition-all duration-300 text-sm md:text-base;
  background: rgba(201, 169, 97, 0.1);
  border: 2px solid #c9a961;
  color: #ecf0f1;
  font-family: "Merriweather", serif;
}

.month-btn:hover {
  background: rgba(201, 169, 97, 0.2);
  transform: translateY(-2px);
}

.month-btn.active {
  background: #c9a961;
  color: #1e2a2d;
}

/* Month Detail */
.month-detail {
  @apply mt-6;
}

.month-title {
  @apply text-2xl md:text-3xl font-bold mb-4 md:mb-6;
  color: #e74c3c;
  font-family: "Crimson Text", serif;
}

/* Meta Box */
.meta-box {
  @apply mb-6 md:mb-8 p-4 md:p-6 bg-blue-900/20 rounded-lg border-l-4 border-blue-500;
}

.meta-title {
  @apply text-lg md:text-xl font-bold mb-3 md:mb-4;
  color: #5dade2;
  font-family: "Crimson Text", serif;
}

.meta-grid {
  @apply grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 md:gap-3;
}

.meta-item {
  @apply text-sm md:text-base p-2 md:p-3 bg-black/30 rounded;
  color: #ecf0f1;
  font-family: "Merriweather", serif;
}

.meta-item.highlight {
  @apply bg-amber-900/30 border-l-2 border-amber-500;
  color: #fbbf24;
}

/* Week Detail */
.week-detail {
  @apply mb-6 md:mb-8 p-4 md:p-6 bg-black/20 rounded-lg;
  border: 1px solid rgba(201, 169, 97, 0.2);
}

.week-detail-title {
  @apply text-xl md:text-2xl font-bold mb-4 md:mb-6;
  color: #c9a961;
  font-family: "Crimson Text", serif;
}

/* Day Card */
.day-card {
  @apply mb-4 p-3 md:p-4 bg-black/30 rounded-lg;
  border-left: 3px solid #5dade2;
}

.day-card.review {
  border-left-color: #4ade80;
  @apply bg-green-900/10;
}

.day-header {
  @apply flex justify-between items-center mb-3;
}

.day-name {
  @apply text-base md:text-lg font-bold;
  color: #5dade2;
  font-family: "Crimson Text", serif;
}

.day-hours {
  @apply text-sm md:text-base font-semibold px-2 md:px-3 py-1 bg-black/50 rounded;
  color: #c9a961;
}

.day-tasks {
  @apply space-y-2 text-sm md:text-base;
  color: #ecf0f1;
  font-family: "Merriweather", serif;
}

.week-meta {
  @apply mt-4 md:mt-6 p-3 md:p-4 bg-green-900/20 rounded-lg border-l-4 border-green-500 text-sm md:text-base;
  color: #4ade80;
  font-family: "Merriweather", serif;
}

/* Info Note */
.info-note {
  @apply p-4 md:p-6 bg-blue-900/20 rounded-lg border-l-4 border-blue-500 text-sm md:text-base;
  color: #5dade2;
  font-family: "Merriweather", serif;
}

.info-note code {
  @apply px-2 py-1 bg-black/40 rounded text-xs md:text-sm;
  color: #c9a961;
  font-family: monospace;
}

/* Tips Grid */
.tips-grid {
  @apply grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 md:gap-4;
}

.tip-card {
  @apply p-4 md:p-5 bg-black/30 rounded-lg border border-amber-700/30 text-center;
}

.tip-icon {
  @apply text-2xl md:text-3xl mb-2 block;
}

.tip-card p {
  @apply text-sm md:text-base;
  color: #ecf0f1;
  font-family: "Merriweather", serif;
}
</style>
