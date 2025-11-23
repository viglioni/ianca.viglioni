<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import CalendarSidebar from "./components/CalendarSidebar.vue";

interface SidebarSection {
  id: string;
  label: string;
}

interface Props {
  sections: SidebarSection[];
  showCalendar?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  showCalendar: true,
});
const activeSection = ref("");

const handleScroll = () => {
  const scrollPosition = window.scrollY + 150; // Offset for header

  // Find which section is currently in view
  for (const section of props.sections) {
    const element = document.getElementById(section.id);
    if (element) {
      const { top, bottom } = element.getBoundingClientRect();
      if (top <= 150 && bottom >= 150) {
        activeSection.value = section.id;
        // Update URL hash without scrolling
        if (window.location.hash !== `#${section.id}`) {
          history.replaceState(null, "", `#${section.id}`);
        }
        break;
      }
    }
  }
};

const scrollToSection = (id: string) => {
  const element = document.getElementById(id);
  if (element) {
    const headerOffset = 100;
    const elementPosition = element.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.scrollY - headerOffset;

    window.scrollTo({
      top: offsetPosition,
      behavior: "smooth",
    });
  }
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
  // Set initial active section
  handleScroll();
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>

<template>
  <nav class="sidebar-nav">
    <h3 class="sidebar-title">Conteúdo</h3>
    <ul class="sidebar-menu">
      <template v-for="section in props.sections" :key="section.id">
        <li>
          <a
            :href="`#${section.id}`"
            :class="['sidebar-link', { active: activeSection === section.id }]"
            @click.prevent="scrollToSection(section.id)"
          >
            {{ section.label }}
          </a>
        </li>

        <!-- Insert calendar after Cronograma -->
        <li v-if="section.id === 'cronograma' && props.showCalendar" class="calendar-item">
          <CalendarSidebar />
        </li>
      </template>
    </ul>
  </nav>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.sidebar-nav {
  @apply flex flex-col gap-6;
}

.sidebar-title {
  @apply text-2xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #f5f1e8;
  border-bottom: 2px solid #d4af37;
  padding-bottom: 0.5rem;
}

.sidebar-menu {
  @apply flex flex-col gap-3 list-none p-0 m-0;
}

.sidebar-link {
  @apply block px-4 py-2 rounded transition-all duration-300;
  font-family: "Merriweather", serif;
  color: #f5f1e8;
  text-decoration: none;
  font-size: 1rem;
}

.sidebar-link:hover {
  background: rgba(212, 175, 55, 0.2);
  color: #d4af37;
  transform: translateX(4px);
}

.sidebar-link.active {
  background: rgba(212, 175, 55, 0.3);
  color: #d4af37;
  border-left: 3px solid #d4af37;
  font-weight: 600;
}

.calendar-item {
  @apply list-none mt-1 mb-4 ml-4;
}
</style>
