<script setup lang="ts">
const weeks = [
  {
    id: "semana1",
    name: "Semana 1",
    period: "18/11 - 23/11",
    days: ["18/11", "19/11", "20/11", "21/11", "22/11", "23/11"],
  },
  {
    id: "ferias",
    name: "Férias",
    period: "26/11 - 02/12",
    days: ["26/11", "27/11", "28/11", "29/11", "30/11", "01/12", "02/12"],
  },
  {
    id: "semana2",
    name: "Semana 2",
    period: "03/12 - 07/12",
    days: ["03/12", "04/12", "05/12", "06/12", "07/12"],
  },
  {
    id: "semana3",
    name: "Semana 3",
    period: "09/12 - 14/12",
    days: ["09/12", "10/12", "11/12", "12/12", "13/12", "14/12"],
  },
];

const subjects = [
  { id: "matematica", name: "Matemática", icon: "📐" },
  { id: "fisica", name: "Física", icon: "⚡" },
  { id: "quimica", name: "Química", icon: "🧪" },
  { id: "ciencias-humanas", name: "Ciências Humanas", icon: "🌍" },
  { id: "geografia", name: "Geografia", icon: "🗺️" },
  { id: "portugues", name: "Português", icon: "📖" },
  { id: "biologia", name: "Biologia", icon: "🧬" },
];
</script>

<template>
  <div class="material-container">
    <div class="material-overlay">
      <div class="content-wrapper">
        <div class="title-section">
          <h1 class="main-title">Material de Estudo</h1>
          <p class="subtitle">SERIADO UFMG ETAPA 1</p>
        </div>

        <div class="content-section" id="dias">
          <h2 class="section-heading">📅 Dias de Estudo</h2>
          <div class="weeks-container">
            <div v-for="week in weeks" :key="week.id" class="week-group">
              <div class="week-header">
                <h3 class="week-title">{{ week.name }}</h3>
                <span class="week-period">{{ week.period }}</span>
              </div>
              <div class="days-grid">
                <div v-for="day in week.days" :key="day" class="day-card">
                  {{ day }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="content-section" id="materias">
          <h2 class="section-heading">📚 Matérias</h2>
          <div class="subjects-grid">
            <button
              v-for="subject in subjects"
              :key="subject.id"
              class="subject-card"
            >
              <span class="subject-icon">{{ subject.icon }}</span>
              <span class="subject-name">{{ subject.name }}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.material-container {
  @apply min-h-screen bg-repeat;
  background-image: url("/ufmg.plano.bg.jpg");
  background-color: #f5f1e8;
}

.material-overlay {
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

.weeks-container {
  @apply flex flex-col gap-6;
}

.week-group {
  @apply flex flex-col gap-3;
}

.week-header {
  @apply flex flex-col md:flex-row md:items-center md:justify-between gap-1 pb-2 border-b-2 border-teal-200;
}

.week-title {
  @apply text-xl font-bold;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.week-period {
  @apply text-sm;
  font-family: "Merriweather", serif;
  color: #1a5560;
  font-weight: 500;
}

.days-grid {
  @apply grid grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-3;
}

.day-card {
  @apply aspect-square flex items-center justify-center rounded-lg text-base font-semibold transition-all duration-200 cursor-pointer;
  font-family: "Merriweather", serif;
  background: linear-gradient(135deg, rgba(13, 62, 71, 0.1) 0%, rgba(26, 85, 96, 0.1) 100%);
  border: 2px solid rgba(26, 85, 96, 0.3);
  color: #0d3e47;
}

.day-card:hover {
  background: linear-gradient(135deg, #0d3e47 0%, #1a5560 100%);
  border-color: #d4af37;
  color: #f5f1e8;
  transform: scale(1.05);
}

.subjects-grid {
  @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4;
}

.subject-card {
  @apply flex flex-col items-center gap-3 p-6 rounded-lg transition-all duration-200 cursor-pointer;
  background: linear-gradient(135deg, rgba(13, 62, 71, 0.05) 0%, rgba(26, 85, 96, 0.05) 100%);
  border: 2px solid rgba(26, 85, 96, 0.2);
  border-left-width: 4px;
  border-left-color: #1a5560;
}

.subject-card:hover {
  background: linear-gradient(135deg, rgba(13, 62, 71, 0.1) 0%, rgba(26, 85, 96, 0.1) 100%);
  border-left-color: #d4af37;
  transform: translateX(4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.subject-icon {
  @apply text-4xl;
}

.subject-name {
  @apply text-lg font-bold;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}
</style>
