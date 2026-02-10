<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import scheduleData from "@/data/uerj-schedule.json";

const selectedMonth = ref("2026-02");
const selectedWeekNum = ref(1);

// Auto-select current week based on today's date
onMounted(() => {
  const today = new Date();
  const startDate = new Date(scheduleData.meta.studyPeriod.start);
  const examDate = new Date(scheduleData.meta.examDate);

  // If today is before start date, show week 1
  if (today < startDate) {
    selectedWeekNum.value = 1;
    return;
  }

  // If today is after exam date, show week 16
  if (today > examDate) {
    selectedWeekNum.value = 16;
    return;
  }

  // Calculate which week we're in (1-16)
  const daysSinceStart = Math.floor((today.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24));
  const currentWeek = Math.min(Math.floor(daysSinceStart / 7) + 1, 16);
  selectedWeekNum.value = currentWeek;
});

// Get all schedule entries (week1-week16 across all months)
const allWeeks = computed(() => {
  const weeks = [];
  for (const [monthKey, monthData] of Object.entries(scheduleData.schedule)) {
    for (const [weekKey, weekData] of Object.entries(monthData)) {
      if (weekKey.startsWith('week')) {
        const weekNum = parseInt(weekKey.replace('week', ''));
        weeks.push({
          monthKey,
          weekNum,
          ...weekData
        });
      }
    }
  }
  return weeks.sort((a, b) => a.weekNum - b.weekNum);
});

const currentWeek = computed(() =>
  allWeeks.value.find(w => w.weekNum === selectedWeekNum.value)
);

const meta = computed(() => scheduleData.meta);
const priorities = computed(() => scheduleData.priorities);
const weeklySchedule = computed(() => scheduleData.weeklySchedule);
const phases = computed(() => scheduleData.phases);
const goals = computed(() => scheduleData.goals);
</script>

<template>
  <div class="uerj-container">
    <div class="uerj-overlay">
      <div class="content-wrapper">
        <!-- Header com logo -->
        <div class="logo-section">
          <img src="/uerj.bg.webp" alt="UERJ Logo" class="logo" />
        </div>

        <!-- Título -->
        <div class="title-section">
          <h1 class="main-title">UERJ 2026</h1>
          <p class="subtitle">{{ meta.title }}</p>
          <div class="info-grid">
            <div class="info-item">
              <strong>Início:</strong> {{ new Date(meta.studyPeriod.start).toLocaleDateString('pt-BR') }}
            </div>
            <div class="info-item">
              <strong>Prova:</strong> {{ new Date(meta.examDate).toLocaleDateString('pt-BR') }}
            </div>
            <div class="info-item">
              <strong>Total:</strong> {{ meta.studyPeriod.totalDays }} dias ({{ meta.studyPeriod.totalWeeks }} semanas)
            </div>
          </div>
        </div>

        <!-- Prioridades -->
        <div class="content-section" id="priorities">
          <h2 class="section-heading">🎯 Prioridades de Estudo</h2>
          <div class="priority-grid">
            <div class="priority-card level1">
              <h3>⭐⭐⭐ Prioridade 1: {{ priorities.level1.name }}</h3>
              <p class="priority-percentage">{{ priorities.level1.percentage }}% ({{ priorities.level1.hoursPerWeek }}h/sem)</p>
              <p class="priority-reason">{{ priorities.level1.reason }}</p>
            </div>
            <div class="priority-card level2">
              <h3>⭐⭐ Prioridade 2: {{ priorities.level2.name }}</h3>
              <p class="priority-percentage">{{ priorities.level2.percentage }}% ({{ priorities.level2.hoursPerWeek }}h/sem)</p>
              <ul class="compact-list">
                <li>Física: {{ priorities.level2.distribution.fisica }}h</li>
                <li>Química: {{ priorities.level2.distribution.quimica }}h</li>
                <li>Biologia: {{ priorities.level2.distribution.biologia }}h</li>
              </ul>
            </div>
            <div class="priority-card level3">
              <h3>⭐ Prioridade 3: {{ priorities.level3.name }}</h3>
              <p class="priority-percentage">{{ priorities.level3.percentage }}% ({{ priorities.level3.hoursPerWeek }}h/sem)</p>
            </div>
            <div class="priority-card level4">
              <h3>Prioridade 4: {{ priorities.level4.name }}</h3>
              <p class="priority-percentage">{{ priorities.level4.percentage }}% ({{ priorities.level4.hoursPerWeek }}h/sem)</p>
            </div>
          </div>
        </div>

        <!-- Lembre-se -->
        <div class="content-section" id="intro">
          <h2 class="section-heading">📖 Lembre-se</h2>
          <ul class="remember-list">
            <li>📅 <strong>Segunda a Sexta:</strong> 9h/dia (quinta 8h - terapia 10-11h)</li>
            <li>📊 <strong>Sábado:</strong> 6h revisão + simulado</li>
            <li>🌴 <strong>Domingo:</strong> descanso total obrigatório</li>
            <li>🎯 <strong>Meta:</strong> {{ goals.overall.target }} para nota {{ goals.overall.gradeNeeded }}</li>
            <li>⚡ <strong>Total:</strong> {{ meta.weeklyHours.total }}h/semana</li>
          </ul>
        </div>

        <!-- Estrutura Semanal -->
        <div class="content-section">
          <h2 class="section-heading">📋 Estrutura Semanal Padrão</h2>

          <div class="week-structure">
            <div class="day-block">
              <h3 class="day-title">Segunda a Sexta (9h/dia)</h3>
              <ul class="compact-list">
                <li><strong>08:00-12:00</strong> (4h) Matemática</li>
                <li><strong>12:00-13:00</strong> Almoço</li>
                <li><strong>13:00-16:30</strong> (3,5h) Química/Física/Biologia</li>
                <li><strong>16:30-17:00</strong> Intervalo</li>
                <li><strong>17:00-18:00</strong> (1h) Humanas</li>
                <li><strong>18:00-18:30</strong> (0,5h) Anki</li>
              </ul>
            </div>

            <div class="day-block">
              <h3 class="day-title">Sábado (6h)</h3>
              <p class="content-text">
                Revisão semanal + Análise de erros + Flashcards
              </p>
            </div>

            <div class="day-block rest">
              <h3 class="day-title">Domingo</h3>
              <p class="rest-day">🌴 Descanso total</p>
            </div>
          </div>
        </div>

        <!-- Rotação -->
        <div class="content-section">
          <h2 class="section-heading">🎯 Rotação de Disciplinas</h2>

          <div class="rotation-blocks">
            <div class="subject-block">
              <h3>Alta Complexidade</h3>
              <p class="note"><em>Matemática é estudada TODOS os dias</em></p>
              <ul class="compact-list">
                <li><strong>Seg:</strong> Matemática + Química</li>
                <li><strong>Ter:</strong> Matemática + Física</li>
                <li><strong>Qua:</strong> Matemática + Química</li>
                <li><strong>Qui:</strong> Matemática + Física</li>
                <li><strong>Sex:</strong> Matemática + Biologia</li>
              </ul>
            </div>

            <div class="subject-block">
              <h3>Humanas (rotação semanal)</h3>
              <ul class="compact-list">
                <li><strong>Sem 1:</strong> Literatura</li>
                <li><strong>Sem 2:</strong> Gramática</li>
                <li><strong>Sem 3:</strong> História</li>
                <li><strong>Sem 4:</strong> Geografia</li>
                <li><strong>Sem 5:</strong> Literatura</li>
                <li><strong>Sem 6:</strong> Filosofia/Sociologia</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Cronograma Detalhado -->
        <div class="content-section" id="cronograma">
          <h2 class="section-heading">📅 Cronograma Semanal (16 semanas)</h2>

          <!-- Seletor de semana -->
          <div class="week-selector">
            <button
              v-for="week in allWeeks"
              :key="week.weekNum"
              @click="selectedWeekNum = week.weekNum"
              :class="['week-btn', { active: selectedWeekNum === week.weekNum }]"
            >
              Semana {{ week.weekNum }}
            </button>
          </div>

          <!-- Semana selecionada -->
          <div v-if="currentWeek" class="week-detail">
            <h3 class="week-title">📍 Semana {{ currentWeek.weekNum }}: {{ currentWeek.dates }}</h3>

            <div v-if="currentWeek.focus" class="focus-box">
              <strong>🎯 Foco da Semana:</strong> {{ currentWeek.focus }}
            </div>

            <div v-if="currentWeek.activity" class="activity-box">
              <strong>📝 Atividade:</strong> {{ currentWeek.activity }}
            </div>

            <div class="subjects-grid">
              <div v-if="currentWeek.matematica" class="subject-card mat">
                <h4>📐 Matemática</h4>
                <p>{{ currentWeek.matematica }}</p>
              </div>
              <div v-if="currentWeek.fisica" class="subject-card fis">
                <h4>⚡ Física</h4>
                <p>{{ currentWeek.fisica }}</p>
              </div>
              <div v-if="currentWeek.quimica" class="subject-card qui">
                <h4>🧪 Química</h4>
                <p>{{ currentWeek.quimica }}</p>
              </div>
              <div v-if="currentWeek.biologia" class="subject-card bio">
                <h4>🧬 Biologia</h4>
                <p>{{ currentWeek.biologia }}</p>
              </div>
              <div v-if="currentWeek.linguagens" class="subject-card ling">
                <h4>📚 Linguagens</h4>
                <p>{{ currentWeek.linguagens }}</p>
              </div>
              <div v-if="currentWeek.humanas" class="subject-card hum">
                <h4>🌍 Humanas</h4>
                <p>{{ currentWeek.humanas }}</p>
              </div>
            </div>

            <div v-if="currentWeek.simulado" class="simulado-box">
              <strong>📝 Simulado:</strong> {{ currentWeek.simulado }}
            </div>

            <div v-if="currentWeek.examDay" class="exam-day-box">
              <strong>🎯 DIA DA PROVA:</strong> {{ currentWeek.examDay }}
            </div>
          </div>
        </div>

        <!-- Simulados -->
        <div class="content-section">
          <h2 class="section-heading">📝 Simulados e Provas</h2>
          <div class="time-grid">
            <div class="time-item">
              <span class="time-label">Simulados UERJ:</span>
              <span class="time-value">16 provas (4h cada)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Simulados ENEM:</span>
              <span class="time-value">7 provas (6,5h cada)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Redações:</span>
              <span class="time-value">7 (com correção)</span>
            </div>
            <div class="time-item">
              <span class="time-label">Análise de erros:</span>
              <span class="time-value">~80h</span>
            </div>
          </div>
        </div>

        <!-- Análise de Provas -->
        <div class="content-section">
          <h2 class="section-heading">📊 Análise de Provas UERJ</h2>
          <p class="content-text mb-4">
            Análise detalhada de <strong>7 provas</strong> do 1º Exame de Qualificação (2015-2018)
          </p>

          <div class="analysis-grid">
            <div class="analysis-card">
              <h3 class="analysis-title">🎯 TOP 3 por Área</h3>
              <div class="subject-analysis">
                <h4>📚 Linguagens</h4>
                <ul class="compact-list">
                  <li>Metáfora (100% das provas)</li>
                  <li>Crônicas contemporâneas</li>
                  <li>Tirinhas/Charges</li>
                </ul>
              </div>
              <div class="subject-analysis">
                <h4>🔢 Matemática</h4>
                <ul class="compact-list">
                  <li>Geometria (100%)</li>
                  <li>PA (86%)</li>
                  <li>Porcentagem (86%)</li>
                </ul>
              </div>
              <div class="subject-analysis">
                <h4>🧪 Ciências da Natureza</h4>
                <ul class="compact-list">
                  <li>Cinemática - Física (100%)</li>
                  <li>Química Orgânica (100%)</li>
                  <li>Ecologia - Biologia (86%)</li>
                </ul>
              </div>
              <div class="subject-analysis">
                <h4>🌍 Ciências Humanas</h4>
                <ul class="compact-list">
                  <li>Cartografia (100%)</li>
                  <li>Brasil República (100%)</li>
                  <li>Urbanização (86%)</li>
                </ul>
              </div>
            </div>

            <div class="analysis-card highlight">
              <h3 class="analysis-title">⚡ Tópicos OBRIGATÓRIOS</h3>
              <ul class="priority-list">
                <li><strong>Linguagens:</strong> Metáfora, Eufemismo, Hipérbole, Crônicas</li>
                <li><strong>Matemática:</strong> Geometria (Pitágoras, áreas), PA, Porcentagem</li>
                <li><strong>Biologia:</strong> Ecologia (sucessão), Fisiologia, Citologia</li>
                <li><strong>Física:</strong> Cinemática (MRU, MRUV, gráficos), Dinâmica</li>
                <li><strong>Química:</strong> Química Orgânica, Estequiometria</li>
                <li><strong>História:</strong> Era Vargas, Ditadura Militar (1964-85)</li>
                <li><strong>Geografia:</strong> Escalas cartográficas, Urbanização</li>
              </ul>
            </div>
          </div>

          <div class="doc-links">
            <a
              href="https://github.com/ianca/ianca.viglioni/tree/main/doc/uerj/qualificacao"
              target="_blank"
              class="doc-link"
            >
              📄 Ver Análises Detalhadas (GitHub)
            </a>
            <a
              href="https://github.com/ianca/ianca.viglioni/blob/main/doc/uerj/qualificacao/COMPILACAO_TOPICOS_RECORRENTES.md"
              target="_blank"
              class="doc-link featured"
            >
              🎯 Compilação Completa de Tópicos Recorrentes
            </a>
          </div>
        </div>

        <!-- Dicas -->
        <div class="content-section motivacao">
          <h2 class="section-heading">🚀 Você Consegue!</h2>
          <p class="motivacao-text">
            Use os sábados para não acumular atrasos, mantenha o Anki em dia para
            revisão espaçada, e lembre-se: <strong>consistência</strong> é mais
            importante que intensidade. Bons estudos!
          </p>
          <p class="motivacao-emoji">📚✨🔥</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.uerj-container {
  @apply min-h-screen bg-repeat;
  background-image: url("/ufmg.plano.bg.jpg");
  background-color: #f5f1e8;
}

.uerj-overlay {
  @apply min-h-screen flex items-start justify-center p-4 md:p-8 pt-8 md:pt-12;
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

.logo-section {
  @apply flex justify-center mb-8;
}

.logo {
  @apply h-32 md:h-40 object-contain;
}

.title-section {
  @apply text-center mb-12;
}

.main-title {
  @apply text-4xl md:text-5xl lg:text-6xl font-bold mb-3;
  font-family: "Crimson Text", serif;
  color: #e74c3c;
  text-shadow: 0 2px 4px rgba(231, 76, 60, 0.2);
  letter-spacing: 0.02em;
}

.subtitle {
  @apply text-xl md:text-2xl mb-6;
  font-family: "Merriweather", serif;
  color: #c9a961;
  font-weight: 600;
}

.info-grid {
  @apply grid grid-cols-1 md:grid-cols-3 gap-4 mt-6;
}

.info-item {
  @apply bg-white/70 backdrop-blur-sm rounded-lg p-4 text-center;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  border: 1px solid rgba(201, 169, 97, 0.2);
}

.content-section {
  @apply flex flex-col gap-4 bg-white/70 backdrop-blur-sm rounded-lg p-6 md:p-8 shadow-lg mb-6;
  border: 2px solid rgba(201, 169, 97, 0.2);
  scroll-margin-top: 100px;
}

.section-heading {
  @apply text-2xl md:text-3xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

.content-text {
  @apply text-base md:text-lg leading-relaxed;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

.remember-list {
  @apply list-none space-y-3;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

.remember-list li {
  @apply pl-4 py-2 border-l-4 border-amber-500 bg-amber-50/40 rounded-r;
}

.week-structure {
  @apply grid grid-cols-1 md:grid-cols-3 gap-4;
}

.day-block {
  @apply p-4 bg-white/60 rounded border border-amber-200;
}

.day-block.rest {
  @apply bg-green-50/60 border-green-200;
}

.day-title {
  @apply text-lg font-bold mb-3;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

.rest-day {
  @apply text-xl text-center;
  color: #16a34a;
}

.compact-list {
  @apply list-disc list-inside ml-2 space-y-1;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  font-size: 0.95rem;
}

.rotation-blocks {
  @apply grid grid-cols-1 md:grid-cols-2 gap-6;
}

.subject-block {
  @apply mb-4;
}

.subject-block h3 {
  @apply text-lg font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

.note {
  @apply text-sm mb-2;
  color: #e74c3c;
  font-style: italic;
}

.meta-box {
  @apply mb-6 p-6 bg-gradient-to-r from-blue-50/60 to-cyan-50/60 rounded-lg border-l-4 border-blue-500;
}

.meta-box h4 {
  @apply text-lg font-bold mb-3;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.week-selector {
  @apply flex flex-wrap gap-3 mb-6;
}

.week-btn {
  @apply px-4 py-2 rounded-lg font-semibold transition-all duration-300;
  background: rgba(201, 169, 97, 0.1);
  border: 2px solid #c9a961;
  color: #0d3e47;
  font-family: "Merriweather", serif;
  cursor: pointer;
}

.week-btn:hover {
  background: rgba(201, 169, 97, 0.2);
  transform: translateY(-2px);
}

.week-btn.active {
  background: #c9a961;
  color: #fff;
}

.week-detail {
  @apply space-y-4;
}

.week-title {
  @apply text-xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

.day-detail {
  @apply mb-4 pb-4 border-b border-gray-200 last:border-b-0;
}

.day-detail.review {
  @apply bg-green-50/40 p-4 rounded-lg border-l-4 border-green-500;
}

.day-header {
  @apply flex justify-between items-center mb-3;
}

.day-name {
  @apply text-lg font-bold;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.day-badge {
  @apply text-sm font-semibold px-3 py-1 bg-amber-100 rounded;
  color: #c9a961;
}

.special-badge {
  @apply ml-2 text-xs font-bold px-2 py-1 bg-red-100 text-red-700 rounded;
}

.task-list {
  @apply list-none ml-4 space-y-2;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  font-size: 0.95rem;
}

.task-list li {
  @apply pl-2 border-l-2 border-gray-300;
}

.week-checkpoint {
  @apply mt-6 p-4 bg-green-50/60 rounded-lg border-l-4 border-green-500;
  font-family: "Merriweather", serif;
  color: #16a34a;
}

.info-box {
  @apply p-6 bg-blue-50/60 rounded-lg border-l-4 border-blue-400;
  font-family: "Merriweather", serif;
  color: #2d4f56;
}

.info-box code {
  @apply px-2 py-1 bg-white/60 rounded text-sm;
  color: #c9a961;
  font-family: monospace;
}

.time-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-3 mt-4;
}

.time-item {
  @apply flex justify-between p-3 bg-white/60 rounded border border-amber-200;
  font-family: "Merriweather", serif;
}

.time-label {
  @apply font-semibold;
  color: #0d3e47;
}

.time-value {
  color: #c9a961;
}

.analysis-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-6 mb-6;
}

.analysis-card {
  @apply p-6 bg-white/60 rounded-lg border border-amber-200;
}

.analysis-card.highlight {
  @apply bg-gradient-to-br from-amber-50/80 to-yellow-50/80 border-2 border-amber-400;
}

.analysis-title {
  @apply text-xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

.subject-analysis {
  @apply mb-4 last:mb-0;
}

.subject-analysis h4 {
  @apply text-base font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.compact-list {
  @apply list-none space-y-1;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  font-size: 0.9rem;
}

.compact-list li {
  @apply pl-2 border-l-2 border-gray-300;
}

.priority-list {
  @apply list-none space-y-2;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  font-size: 0.95rem;
}

.priority-list li {
  @apply pl-3 py-2 border-l-4 border-amber-500 bg-white/40 rounded-r;
}

.priority-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-4 mb-6;
}

.priority-card {
  @apply p-5 bg-white/60 rounded-lg border-2;
  font-family: "Merriweather", serif;
}

.priority-card h3 {
  @apply text-lg font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.priority-percentage {
  @apply text-base font-semibold mb-2;
  color: #c9a961;
}

.priority-reason {
  @apply text-sm italic;
  color: #2d4f56;
}

.priority-card.level1 {
  @apply border-red-400 bg-red-50/40;
}

.priority-card.level2 {
  @apply border-orange-400 bg-orange-50/40;
}

.priority-card.level3 {
  @apply border-yellow-400 bg-yellow-50/40;
}

.priority-card.level4 {
  @apply border-blue-400 bg-blue-50/40;
}

.distribution-list {
  @apply list-none space-y-1 mb-2;
  font-size: 0.9rem;
}

.distribution-list li {
  @apply pl-2 border-l-2 border-gray-400;
}

.doc-links {
  @apply flex flex-col md:flex-row gap-3 mt-6;
}

.doc-link {
  @apply flex-1 px-6 py-3 text-center rounded-lg font-semibold transition-all duration-300;
  background: rgba(201, 169, 97, 0.1);
  border: 2px solid #c9a961;
  color: #0d3e47;
  font-family: "Merriweather", serif;
  text-decoration: none;
}

.doc-link:hover {
  background: rgba(201, 169, 97, 0.2);
  transform: translateY(-2px);
}

.doc-link.featured {
  background: #c9a961;
  color: #fff;
  border-color: #b8935a;
}

.doc-link.featured:hover {
  background: #b8935a;
}

.motivacao {
  @apply bg-gradient-to-r from-amber-100/80 to-yellow-100/80 border-2 border-amber-400;
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

.week-selector {
  @apply flex flex-wrap gap-2 mb-6;
}

.week-btn {
  @apply flex-1 px-4 py-2 rounded-lg font-semibold transition-all duration-200;
  background: rgba(201, 169, 97, 0.1);
  border: 2px solid #c9a961;
  color: #0d3e47;
  font-family: "Merriweather", serif;
  font-size: 0.9rem;
  min-width: 120px;
}

.week-btn:hover {
  background: rgba(201, 169, 97, 0.2);
  transform: translateY(-2px);
}

.week-btn.active {
  background: #c9a961;
  color: #fff;
  border-color: #b8935a;
}

.week-title {
  @apply text-2xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #c9a961;
}

.focus-box {
  @apply p-4 mb-4 bg-amber-50/60 rounded-lg border-l-4 border-amber-500;
  font-family: "Merriweather", serif;
  color: #0d3e47;
}

.activity-box {
  @apply p-4 mb-4 bg-blue-50/60 rounded-lg border-l-4 border-blue-500;
  font-family: "Merriweather", serif;
  color: #0d3e47;
}

.subjects-grid {
  @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4;
}

.subject-card {
  @apply p-4 rounded-lg border-2;
  font-family: "Merriweather", serif;
}

.subject-card h4 {
  @apply text-base font-bold mb-2;
  font-family: "Crimson Text", serif;
}

.subject-card p {
  @apply text-sm;
  color: #2d4f56;
}

.subject-card.mat {
  @apply bg-blue-50/40 border-blue-400;
}

.subject-card.fis {
  @apply bg-purple-50/40 border-purple-400;
}

.subject-card.qui {
  @apply bg-green-50/40 border-green-400;
}

.subject-card.bio {
  @apply bg-cyan-50/40 border-cyan-400;
}

.subject-card.ling {
  @apply bg-pink-50/40 border-pink-400;
}

.subject-card.hum {
  @apply bg-orange-50/40 border-orange-400;
}

.simulado-box {
  @apply p-4 mb-4 bg-green-50/60 rounded-lg border-l-4 border-green-500;
  font-family: "Merriweather", serif;
  color: #16a34a;
  font-weight: 600;
}

.exam-day-box {
  @apply p-6 bg-gradient-to-r from-red-50/80 to-orange-50/80 rounded-lg border-2 border-red-500;
  font-family: "Crimson Text", serif;
  color: #dc2626;
  font-size: 1.2rem;
  font-weight: bold;
  text-align: center;
}
</style>
