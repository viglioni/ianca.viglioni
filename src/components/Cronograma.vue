<script setup lang="ts">
import { ref, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import studySchedule from "@/data/study-schedule.json";

const route = useRoute();
const router = useRouter();

const currentDate = ref(new Date());

const formatDate = (date: Date): string => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

const formatDisplayDate = (date: Date): string => {
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  return `${day}/${month}`;
};

// Get all dates from the schedule
const allDates = computed(() => {
  const schedule = (studySchedule as any).schedule as Record<string, Task[]>;
  return Object.keys(schedule)
    .map((dateStr) => {
      const date = new Date(dateStr + 'T00:00:00');
      return date;
    })
    .sort((a, b) => a.getTime() - b.getTime());
});

const firstDate = computed(() => allDates.value[0]);
const lastDate = computed(() => allDates.value[allDates.value.length - 1]);

const isFirstDay = computed(() => {
  if (!firstDate.value) return false;
  return formatDate(currentDate.value) === formatDate(firstDate.value);
});

const isLastDay = computed(() => {
  if (!lastDate.value) return false;
  return formatDate(currentDate.value) === formatDate(lastDate.value);
});

const checkpointDates = ['2025-11-22', '2025-12-06'];

const isCheckpoint = (date: Date): boolean => {
  return checkpointDates.includes(formatDate(date));
};

const getDateLabel = (date: Date): string => {
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const compareDate = new Date(date);
  compareDate.setHours(0, 0, 0, 0);

  const diffTime = compareDate.getTime() - today.getTime();
  const diffDays = diffTime / (1000 * 60 * 60 * 24);

  const checkpointLabel = isCheckpoint(date) ? ' 🎯 CHECKPOINT' : '';

  // Check if it's the first or last day of the range
  if (isFirstDay.value) return `Primeiro dia (${formatDisplayDate(date)})${checkpointLabel}`;
  if (isLastDay.value)
    return `Último dia de revisão! (${formatDisplayDate(date)})${checkpointLabel}`;

  if (diffDays === 0) return `Hoje (${formatDisplayDate(date)})${checkpointLabel}`;
  if (diffDays === -1) return `Ontem (${formatDisplayDate(date)})${checkpointLabel}`;
  if (diffDays === 1) return `Amanhã (${formatDisplayDate(date)})${checkpointLabel}`;

  return `${formatDisplayDate(date)}${checkpointLabel}`;
};

interface Task {
  name: string;
  subject: string;
  code: string;
}

interface CodeData {
  title: string;
  themes: string[];
  subject: string;
}

const currentTasks = computed(() => {
  const dateKey = formatDate(currentDate.value);
  const schedule = (studySchedule as any).schedule as Record<string, string[]>;
  const codes = (studySchedule as any).codes as Record<string, CodeData>;
  const codesToday = schedule[dateKey] || [];

  return codesToday.map(code => ({
    name: codes[code]?.title ?? "",
    subject: codes[code]?.subject ?? "",
    code: code
  }));
});

const hasTasks = computed(() => currentTasks.value.length > 0);

const updateURL = (date: Date) => {
  const dateStr = formatDate(date);
  router.push({ query: { ...route.query, day: dateStr } });
};

const previousDay = () => {
  const newDate = new Date(currentDate.value);
  newDate.setDate(newDate.getDate() - 1);
  currentDate.value = newDate;
  updateURL(newDate);
};

const nextDay = () => {
  const newDate = new Date(currentDate.value);
  newDate.setDate(newDate.getDate() + 1);
  currentDate.value = newDate;
  updateURL(newDate);
};

// Check if previous/next buttons should be disabled
const canGoPrevious = computed(() => {
  if (!firstDate.value) return false;
  const currentTime = currentDate.value.getTime();
  const firstTime = firstDate.value.getTime();
  return currentTime > firstTime;
});

const canGoNext = computed(() => {
  if (!lastDate.value) return false;
  const currentTime = currentDate.value.getTime();
  const lastTime = lastDate.value.getTime();
  return currentTime < lastTime;
});

const getInitialDate = (): Date => {
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // If today is before the first date, return the first date
  if (firstDate.value && today < firstDate.value) {
    return new Date(firstDate.value);
  }
  // If today is after the last date, return the last date
  else if (lastDate.value && today > lastDate.value) {
    return new Date(lastDate.value);
  }
  // Otherwise return today
  return today;
};

const updateFromURL = () => {
  const dayParam = route.query.day as string | undefined;

  if (dayParam) {
    // Try to parse the date from URL
    const urlDate = new Date(dayParam + 'T00:00:00');
    if (!isNaN(urlDate.getTime())) {
      urlDate.setHours(0, 0, 0, 0);
      currentDate.value = urlDate;
    } else {
      // Invalid date in URL, use initial date but don't update URL
      const initialDate = getInitialDate();
      currentDate.value = initialDate;
    }
  } else {
    // No day in URL, use initial date but don't auto-add to URL
    const initialDate = getInitialDate();
    currentDate.value = initialDate;
  }
};

// Watch for URL changes
watch(() => route.query.day, (newDay) => {
  if (newDay) {
    const urlDate = new Date(newDay + 'T00:00:00');
    if (!isNaN(urlDate.getTime())) {
      urlDate.setHours(0, 0, 0, 0);
      currentDate.value = urlDate;
    }
  }
});

onMounted(() => {
  updateFromURL();
});
</script>

<template>
  <div class="cronograma-container">
    <div class="cronograma-header">
      <button
        @click="previousDay"
        class="nav-button"
        :disabled="!canGoPrevious"
        aria-label="Dia anterior"
      >
        ◀
      </button>

      <h3 class="date-title">{{ getDateLabel(currentDate) }}</h3>

      <button
        @click="nextDay"
        class="nav-button"
        :disabled="!canGoNext"
        aria-label="Próximo dia"
      >
        ▶
      </button>
    </div>

    <div v-if="hasTasks" class="tasks-list">
      <div v-for="(task, index) in currentTasks" :key="index" class="task-item">
        <span class="task-text">{{ task.name }}</span>
      </div>
    </div>

    <div v-else class="no-tasks rest">
      <p class="rest-emoji">🌴</p>
      <p class="rest-text">Descansar!!</p>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.cronograma-container {
  @apply flex flex-col gap-4;
}

.cronograma-header {
  @apply flex items-center justify-between gap-4;
}

.nav-button {
  @apply px-4 py-2 rounded-lg transition-all duration-300 text-2xl font-bold;
  font-family: "Merriweather", serif;
  background: linear-gradient(135deg, #0d3e47 0%, #1a5560 100%);
  color: #f5f1e8;
  border: 2px solid #1a5560;
  cursor: pointer;
  min-width: 50px;
}

.nav-button:hover:not(:disabled) {
  background: linear-gradient(135deg, #1a5560 0%, #0d3e47 100%);
  border-color: #d4af37;
  color: #d4af37;
  transform: scale(1.05);
}

.nav-button:disabled {
  @apply opacity-40 cursor-not-allowed;
}

.date-title {
  @apply text-2xl md:text-3xl font-bold text-center flex-1;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.tasks-list {
  @apply flex flex-col gap-3;
}

.task-item {
  @apply flex items-start gap-3 p-3 rounded-lg transition-all duration-200;
  font-family: "Merriweather", serif;
  background: linear-gradient(
    90deg,
    rgba(13, 62, 71, 0.05) 0%,
    rgba(26, 85, 96, 0.05) 100%
  );
  border-left: 3px solid #1a5560;
}

.task-item:hover {
  background: linear-gradient(
    90deg,
    rgba(13, 62, 71, 0.1) 0%,
    rgba(26, 85, 96, 0.1) 100%
  );
  border-left-color: #d4af37;
  transform: translateX(4px);
}

.task-bullet {
  @apply text-xl font-bold flex-shrink-0;
  color: #1a5560;
}

.task-text {
  @apply text-base leading-relaxed;
  color: #2d4f56;
}

.no-tasks {
  @apply p-6 text-center rounded-lg;
  background: rgba(212, 175, 55, 0.1);
  border: 2px dashed #d4af37;
}

.no-tasks.rest {
  @apply flex flex-col items-center gap-3;
  background: linear-gradient(
    135deg,
    rgba(76, 175, 80, 0.1) 0%,
    rgba(139, 195, 74, 0.1) 100%
  );
  border: 2px dashed #4caf50;
}

.rest-emoji {
  @apply text-5xl m-0;
}

.rest-text {
  @apply text-2xl font-bold m-0;
  font-family: "Crimson Text", serif;
  color: #2e7d32;
}
</style>
