<script setup lang="ts">
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import studySchedule from "@/data/study-schedule.json";

const route = useRoute();
const router = useRouter();

const formatDate = (date: Date): string => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};

interface Task {
  name: string;
  subject: string;
  code: string;
}

// Get all dates from the schedule
const allDates = computed(() => {
  const schedule = (studySchedule as any).schedule as Record<string, string[]>;
  return Object.keys(schedule)
    .map((dateStr) => {
      const date = new Date(dateStr + "T00:00:00");
      return date;
    })
    .sort((a, b) => a.getTime() - b.getTime());
});

const selectedDay = computed(() => {
  const dayParam = route.query.day as string | undefined;
  return dayParam || "";
});

const selectDay = (date: Date) => {
  const dateStr = formatDate(date);
  router.push({ query: { ...route.query, day: dateStr } });
};

const isSelected = (date: Date): boolean => {
  return formatDate(date) === selectedDay.value;
};

const getDayNumber = (date: Date): number => {
  return date.getDate();
};

const getMonthName = (date: Date): string => {
  const months = [
    "Jan",
    "Fev",
    "Mar",
    "Abr",
    "Mai",
    "Jun",
    "Jul",
    "Ago",
    "Set",
    "Out",
    "Nov",
    "Dez",
  ];
  return months[date.getMonth()];
};

// Group dates by month
const datesByMonth = computed(() => {
  const grouped = new Map<string, Date[]>();

  allDates.value.forEach((date) => {
    const monthKey = `${date.getFullYear()}-${date.getMonth()}`;
    if (!grouped.has(monthKey)) {
      grouped.set(monthKey, []);
    }
    grouped.get(monthKey)!.push(date);
  });

  return Array.from(grouped.entries()).map(([key, dates]) => ({
    monthKey: key,
    monthName: getMonthName(dates[0]),
    year: dates[0].getFullYear(),
    dates: dates,
  }));
});
</script>

<template>
  <div class="calendario-container">
    <div
      v-for="month in datesByMonth"
      :key="month.monthKey"
      class="month-group"
    >
      <h4 class="month-header">{{ month.monthName }} {{ month.year }}</h4>
      <div class="days-grid">
        <button
          v-for="date in month.dates"
          :key="formatDate(date)"
          @click="selectDay(date)"
          :class="['day-button', { selected: isSelected(date) }]"
          :aria-label="`Dia ${getDayNumber(date)} de ${month.monthName}`"
        >
          {{ getDayNumber(date) }}
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.calendario-container {
  @apply flex flex-col gap-4;
}

.month-group {
  @apply flex flex-col gap-2;
}

.month-header {
  @apply text-sm font-bold text-center;
  font-family: "Crimson Text", serif;
  color: #d4af37;
}

.days-grid {
  @apply grid grid-cols-7 gap-1;
}

.day-button {
  @apply aspect-square flex items-center justify-center rounded text-sm transition-all duration-200;
  font-family: "Merriweather", serif;
  background: rgba(245, 241, 232, 0.15);
  color: #f5f1e8;
  border: 1px solid rgba(245, 241, 232, 0.3);
  cursor: pointer;
  min-width: 32px;
  font-weight: 500;
}

.day-button:hover {
  background: rgba(212, 175, 55, 0.3);
  border-color: #d4af37;
  color: #d4af37;
  transform: scale(1.05);
}

.day-button.selected {
  background: #d4af37;
  color: #0d3e47;
  border-color: #f5f1e8;
  font-weight: bold;
}
</style>
