<script setup lang="ts">
import { ref, computed, watch, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import studySchedule from "@/data/study-schedule.json";

const route = useRoute();
const router = useRouter();

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

interface CodeData {
  title: string;
  themes: string[];
  subject: string;
  dates: string[];
}

// Subject icons and colors mapping
const subjectConfig: Record<string, { icon: string; name: string; color: string }> = {
  'matematica': { icon: 'fa-calculator', name: 'Matemática', color: '#3b82f6' },
  'fisica': { icon: 'fa-bolt', name: 'Física', color: '#8b5cf6' },
  'quimica': { icon: 'fa-flask', name: 'Química', color: '#10b981' },
  'biologia': { icon: 'fa-dna', name: 'Biologia', color: '#06b6d4' },
  'geografia': { icon: 'fa-earth-americas', name: 'Geografia', color: '#f59e0b' },
  'ciencias-humanas': { icon: 'fa-globe', name: 'Ciências Humanas', color: '#ef4444' },
  'portugues': { icon: 'fa-book', name: 'Português', color: '#ec4899' },
  'filosofia': { icon: 'fa-lightbulb', name: 'Filosofia', color: '#6366f1' },
  'sociologia': { icon: 'fa-users', name: 'Sociologia', color: '#14b8a6' },
  'geral': { icon: 'fa-book-open', name: 'Geral', color: '#64748b' }
};

const getSubjectIcon = (subject: string): string => {
  return subjectConfig[subject]?.icon || 'fa-book-open';
};

const getSubjectName = (subject: string): string => {
  return subjectConfig[subject]?.name || subject.charAt(0).toUpperCase() + subject.slice(1);
};

const getSubjectColor = (subject: string): string => {
  return subjectConfig[subject]?.color || '#64748b';
};

const formatCodeNumber = (code: string): string => {
  // Example: mat-1-1 -> 1-1
  // Example: por-2-2 -> 2-2
  const parts = code.split('-');
  if (parts.length >= 3) {
    const week = parts[1];
    const number = parts[2];
    return `${week}-${number}`;
  }
  return '';
};

// Get all available subjects and themes
const allSubjects = computed(() => {
  const data = studySchedule as any;
  return Object.keys(data.subjects).sort();
});

const allThemes = computed(() => {
  const data = studySchedule as any;
  const themes = data.themes as Record<string, { codes: any[], subjects: string[] }>;

  let themesList = Object.keys(themes);

  // Filter themes by selected subject
  if (selectedSubject.value) {
    themesList = themesList.filter(theme =>
      themes[theme].subjects.includes(selectedSubject.value)
    );
  }

  return themesList.sort();
});

// Get initial date using same logic as calendar
const getInitialDate = (): string => {
  const data = studySchedule as any;
  const allScheduleDates = Object.keys(data.schedule).sort();

  if (allScheduleDates.length === 0) return "";

  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const todayStr = formatDateToISO(today);

  const firstDate = allScheduleDates[0];
  const lastDate = allScheduleDates[allScheduleDates.length - 1];

  // If today is before the first date, return the first date
  if (todayStr < firstDate) {
    return firstDate;
  }
  // If today is after the last date, return the last date
  else if (todayStr > lastDate) {
    return lastDate;
  }
  // Otherwise return today if it exists in schedule, or empty
  return allScheduleDates.includes(todayStr) ? todayStr : "";
};

const formatDateToISO = (date: Date): string => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

// Filter state from query params
const selectedSubject = ref<string>("");
const selectedTheme = ref<string>("");
const selectedDate = ref<string>("");
const searchText = ref<string>("");

// Update URL with current filters
const updateURL = () => {
  isUpdatingFromLocal = true;
  const query: Record<string, string> = {};
  if (selectedSubject.value) query.subject = selectedSubject.value;
  if (selectedTheme.value) query.theme = selectedTheme.value;
  if (selectedDate.value) query.day = selectedDate.value;
  if (searchText.value) query.search = searchText.value;

  // Use replace to avoid infinite loops with watchers
  router.replace({ query });
};

// Track if this is the first load
let isFirstLoad = true;

// Load filters from URL
const loadFromURL = () => {
  selectedSubject.value = (route.query.subject as string) || "";
  selectedTheme.value = (route.query.theme as string) || "";
  // Only set default date on first load and if no query params exist
  if (route.query.day) {
    selectedDate.value = route.query.day as string;
  } else if (isFirstLoad && !route.query.subject && !route.query.theme && !route.query.search) {
    selectedDate.value = getInitialDate();
  } else {
    selectedDate.value = "";
  }
  searchText.value = (route.query.search as string) || "";
  isFirstLoad = false;
};

// Normalize text for better filtering
const normalizeText = (text: string): string => {
  return text
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "") // Remove accents
    .replace(/[^a-z0-9\s]/g, "") // Remove special characters
    .trim();
};

// Get all available dates
const allDates = computed(() => {
  const data = studySchedule as any;
  return Object.keys(data.schedule).sort();
});

// Format date for display
const formatDate = (date: string): string => {
  const [year, month, day] = date.split('-');
  return `${day}/${month}`;
};

// Get filtered codes
const filteredCodes = computed(() => {
  const data = studySchedule as any;
  const codes = data.codes as Record<string, CodeData>;
  const themes = data.themes as Record<string, { codes: { code: string }[], subjects: string[] }>;

  let resultCodes = Object.keys(codes);

  // Filter by subject
  if (selectedSubject.value) {
    resultCodes = resultCodes.filter(
      (code) => codes[code].subject === selectedSubject.value
    );
  }

  // Filter by theme
  if (selectedTheme.value) {
    const themeCodesList = themes[selectedTheme.value]?.codes.map((t) => t.code) || [];
    resultCodes = resultCodes.filter((code) => themeCodesList.includes(code));
  }

  // Filter by date
  if (selectedDate.value) {
    resultCodes = resultCodes.filter((code) =>
      codes[code].dates?.includes(selectedDate.value)
    );
  }

  // Filter by search text
  if (searchText.value) {
    const normalizedSearch = normalizeText(searchText.value);
    resultCodes = resultCodes.filter((code) => {
      const normalizedTitle = normalizeText(codes[code].title);
      const normalizedCode = normalizeText(code);
      return (
        normalizedTitle.includes(normalizedSearch) ||
        normalizedCode.includes(normalizedSearch)
      );
    });
  }

  return resultCodes.sort();
});

const clearFilters = () => {
  selectedSubject.value = "";
  selectedTheme.value = "";
  selectedDate.value = "";
  searchText.value = "";
  updateURL();
};

const setDateFilter = (dateStr: string) => {
  // Parse DD/MM format to YYYY-MM-DD
  const [day, month] = dateStr.split('/');
  const year = '2025'; // Year from the schedule
  const isoDate = `${year}-${month}-${day}`;

  // Clear other filters and set only date
  selectedSubject.value = "";
  selectedTheme.value = "";
  selectedDate.value = isoDate;
  searchText.value = "";
  updateURL();
};

const isDaySelected = (dayStr: string): boolean => {
  if (!selectedDate.value) return false;
  const [day, month] = dayStr.split('/');
  const year = '2025';
  const isoDate = `${year}-${month}-${day}`;
  return selectedDate.value === isoDate;
};

// Watch for subject changes and clear theme if it's not valid
watch(selectedSubject, (newVal, oldVal) => {
  if (newVal !== oldVal) {
    if (selectedTheme.value && !allThemes.value.includes(selectedTheme.value)) {
      selectedTheme.value = "";
    }
    updateURL();
  }
});

// Watch all filters and update URL
watch([selectedTheme, selectedDate, searchText], () => {
  updateURL();
});

// Watch for URL changes (from other components like sidebar calendar)
// Don't update if we're the ones who changed it
let isUpdatingFromLocal = false;
watch(() => route.query, (newQuery, oldQuery) => {
  if (!isUpdatingFromLocal) {
    loadFromURL();
  }
  isUpdatingFromLocal = false;
}, { deep: true });

// Initialize from URL on mount
onMounted(() => {
  loadFromURL();
});
</script>

<template>
  <div class="material-container">
    <div class="material-overlay">
      <div class="content-wrapper">
        <div class="title-section">
          <h1 class="main-title">Material de Estudo</h1>
          <p class="subtitle">SERIADO UFMG ETAPA 1</p>
        </div>

        <div class="content-section" id="filtros">
          <h2 class="section-heading">🔍 Filtros</h2>

          <div class="filters-container">
            <div class="filter-group">
              <label class="filter-label">Disciplina</label>
              <select v-model="selectedSubject" class="filter-select">
                <option value="">Todas</option>
                <option v-for="subject in allSubjects" :key="subject" :value="subject">
                  {{ subject.charAt(0).toUpperCase() + subject.slice(1) }}
                </option>
              </select>
            </div>

            <div class="filter-group">
              <label class="filter-label">Tema</label>
              <select v-model="selectedTheme" class="filter-select">
                <option value="">Todos</option>
                <option v-for="theme in allThemes" :key="theme" :value="theme">
                  {{ theme }}
                </option>
              </select>
            </div>

            <div class="filter-group">
              <label class="filter-label">Data</label>
              <select v-model="selectedDate" class="filter-select">
                <option value="">Todas</option>
                <option v-for="date in allDates" :key="date" :value="date">
                  {{ formatDate(date) }}
                </option>
              </select>
            </div>

            <div class="filter-group">
              <label class="filter-label">Buscar</label>
              <input
                v-model="searchText"
                type="text"
                placeholder="Digite para buscar..."
                class="filter-input"
              />
            </div>

            <div class="filter-group">
              <button @click="clearFilters" class="clear-button">
                Limpar Filtros
              </button>
            </div>
          </div>

          <div class="results-section">
            <h3 class="results-heading">
              {{ filteredCodes.length }} resultado(s) encontrado(s)
            </h3>
            <div class="codes-list">
              <div v-for="code in filteredCodes" :key="code" class="code-item">
                <span
                  class="subject-badge"
                  :style="{ backgroundColor: getSubjectColor((studySchedule as any).codes[code].subject) }"
                >
                  <i :class="['fas', getSubjectIcon((studySchedule as any).codes[code].subject)]"></i>
                  <span>{{ getSubjectName((studySchedule as any).codes[code].subject) }} {{ formatCodeNumber(code) }}</span>
                </span>
                <span class="code-title">{{ (studySchedule as any).codes[code].title }}</span>
              </div>
            </div>
          </div>
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
                <button
                  v-for="day in week.days"
                  :key="day"
                  @click="setDateFilter(day)"
                  :class="['day-card', { selected: isDaySelected(day) }]"
                >
                  {{ day }}
                </button>
              </div>
            </div>
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

.day-card.selected {
  background: linear-gradient(135deg, #d4af37 0%, #b8941f 100%);
  color: #0d3e47;
  border-color: #0d3e47;
  font-weight: bold;
}

.filters-container {
  @apply grid grid-cols-1 md:grid-cols-5 gap-4 mb-6;
}

.filter-group {
  @apply flex flex-col gap-2;
}

.filter-label {
  @apply text-sm font-bold;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.filter-select,
.filter-input {
  @apply px-3 py-2 rounded-lg border-2 transition-all duration-200;
  font-family: "Merriweather", serif;
  background: white;
  border-color: rgba(26, 85, 96, 0.3);
  color: #0d3e47;
}

.filter-select:focus,
.filter-input:focus {
  outline: none;
  border-color: #d4af37;
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
}

.clear-button {
  @apply px-4 py-2 rounded-lg font-bold transition-all duration-200 mt-auto;
  font-family: "Merriweather", serif;
  background: linear-gradient(135deg, rgba(13, 62, 71, 0.1) 0%, rgba(26, 85, 96, 0.1) 100%);
  border: 2px solid rgba(26, 85, 96, 0.3);
  color: #0d3e47;
  cursor: pointer;
}

.clear-button:hover {
  background: linear-gradient(135deg, #0d3e47 0%, #1a5560 100%);
  border-color: #d4af37;
  color: #f5f1e8;
}

.results-section {
  @apply flex flex-col gap-3;
}

.results-heading {
  @apply text-xl font-bold;
  font-family: "Crimson Text", serif;
  color: #1a5560;
}

.codes-list {
  @apply flex flex-col gap-3 max-h-[500px] overflow-y-auto;
}

.code-item {
  @apply flex items-center gap-4 p-4 rounded-lg transition-all duration-200;
  background: linear-gradient(90deg, rgba(13, 62, 71, 0.05) 0%, rgba(26, 85, 96, 0.05) 100%);
  border-left: 3px solid #1a5560;
  min-height: 50px;
}

.code-item:hover {
  background: linear-gradient(90deg, rgba(13, 62, 71, 0.1) 0%, rgba(26, 85, 96, 0.1) 100%);
  border-left-color: #d4af37;
  transform: translateX(4px);
}

.subject-badge {
  @apply px-3 py-2 rounded font-bold flex-shrink-0;
  font-family: "Merriweather", serif;
  color: white;
  height: 40px;
  min-width: 220px;
  display: flex;
  align-items: center;
  white-space: nowrap;
  font-size: 14px;
}

.subject-badge i {
  font-size: 18px;
  width: 22px;
  margin-right: 10px;
  text-align: center;
  flex-shrink: 0;
}

.subject-badge span {
  text-align: left;
  flex: 1;
}

.code-title {
  @apply text-base;
  font-family: "Merriweather", serif;
  color: #2d4f56;
  line-height: 1.5;
}

</style>
