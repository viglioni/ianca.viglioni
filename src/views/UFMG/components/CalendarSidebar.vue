<script setup lang="ts">
import { useRouter } from "vue-router";
import Cronograma from "@/components/Cronograma.vue";
import CalendarioEstudos from "@/components/CalendarioEstudos.vue";

const router = useRouter();

const goToCheckpoint = (date: string) => {
  router.push({ query: { day: date } });
};
</script>

<template>
  <div class="calendar-sidebar-container">
    <div class="cronograma-section">
      <Cronograma />
    </div>
    <div class="calendario-section">
      <CalendarioEstudos />
    </div>
    <div class="checkpoints-sidebar">
      <h4 class="checkpoints-title">🎯 Checkpoints</h4>
      <div class="checkpoint-sidebar-list">
        <button
          @click="goToCheckpoint('2025-11-23')"
          class="checkpoint-sidebar-item"
        >
          <span class="checkpoint-sidebar-date">23/11</span>
        </button>
        <button
          @click="goToCheckpoint('2025-12-07')"
          class="checkpoint-sidebar-item"
        >
          <span class="checkpoint-sidebar-date">07/12</span>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.calendar-sidebar-container {
  @apply flex flex-col gap-4;
}

.cronograma-section {
  @apply px-2 py-1;
}

.calendario-section {
  @apply px-2 py-1;
}

.checkpoints-sidebar {
  @apply mt-2 px-2;
}

.checkpoints-title {
  @apply text-sm font-bold mb-2;
  font-family: "Crimson Text", serif;
  color: #d4af37;
}

.checkpoint-sidebar-list {
  @apply flex gap-2;
}

.checkpoint-sidebar-item {
  @apply px-2 py-1 rounded text-xs cursor-pointer transition-all duration-200;
  background: rgba(212, 175, 55, 0.2);
  border: 1px solid #d4af37;
  font-family: "Merriweather", serif;
}

.checkpoint-sidebar-item:hover {
  background: rgba(212, 175, 55, 0.4);
  border-color: #f5f1e8;
  transform: scale(1.05);
}

.checkpoint-sidebar-date {
  color: #f5f1e8;
  font-weight: 500;
}
</style>
