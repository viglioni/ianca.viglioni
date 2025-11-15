<script setup lang="ts">
import { ref, provide, onMounted } from "vue";
import { RouterLink, RouterView } from "vue-router";

// Set default based on screen size
const sidebarOpen = ref(true);

const toggleSidebar = () => {
  sidebarOpen.value = !sidebarOpen.value;
};

// Set initial state based on screen size
onMounted(() => {
  if (window.innerWidth < 768) {
    sidebarOpen.value = false;
  } else {
    sidebarOpen.value = true;
  }
});

// Provide sidebar state
provide("sidebarOpen", sidebarOpen);
provide("toggleSidebar", toggleSidebar);
</script>

<template>
  <div class="ufmg-layout">
    <header class="ufmg-header">
      <div class="header-content">
        <div class="header-left">
          <button
            @click="toggleSidebar"
            class="sidebar-toggle"
            :aria-label="sidebarOpen ? 'Close sidebar' : 'Open sidebar'"
          >
            <span v-if="sidebarOpen">◀</span>
            <span v-else>▶</span>
          </button>
          <RouterLink to="/ufmg" class="home-link">
            <span class="university-icon">🎓</span>
            <span class="home-link-text">UFMG</span>
          </RouterLink>
        </div>

        <nav class="nav-links">
          <RouterLink to="/ufmg/plano" class="nav-link"
            >Plano de Estudos</RouterLink
          >
        </nav>
      </div>
    </header>

    <div class="layout-container">
      <!-- Sidebar (collapsible) -->
      <aside
        :class="[
          'sidebar',
          { 'sidebar-open': sidebarOpen, 'sidebar-closed': !sidebarOpen },
        ]"
      >
        <div class="sidebar-content">
          <RouterView name="sidebar" />
        </div>
      </aside>

      <!-- Main content -->
      <main :class="['main-content', { 'with-sidebar': sidebarOpen }]">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.ufmg-layout {
  @apply min-h-screen flex flex-col;
}

.ufmg-header {
  @apply sticky top-0 z-50;
  background: linear-gradient(90deg, #0d3e47 0%, #1a5560 100%);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.header-content {
  @apply container mx-auto px-6 py-4 flex items-center justify-between;
}

.header-left {
  @apply flex items-center gap-4;
}

.sidebar-toggle {
  @apply p-2 text-xl transition-all duration-300 rounded flex items-center justify-center;
  color: #f5f1e8;
  background: transparent;
  border: none;
  cursor: pointer;
  width: 40px;
  height: 40px;
}

.sidebar-toggle:hover {
  background: rgba(212, 175, 55, 0.2);
  color: #d4af37;
}

.home-link {
  @apply flex items-center gap-2 text-lg font-semibold transition-all duration-300;
  font-family: "Merriweather", serif;
  color: #f5f1e8;
  text-decoration: none;
}

.home-link:hover {
  color: #d4af37;
}

.university-icon {
  @apply text-2xl;
}

.home-link-text {
  @apply hidden md:inline;
}

.nav-links {
  @apply flex items-center gap-6;
}

.nav-link {
  @apply relative px-4 py-2 text-base font-semibold transition-all duration-300;
  font-family: "Merriweather", serif;
  color: #f5f1e8;
  text-decoration: none;
}

.nav-link::after {
  content: "";
  @apply absolute bottom-0 left-0 w-0 h-0.5 transition-all duration-300;
  background: #d4af37;
}

.nav-link:hover {
  color: #d4af37;
}

.nav-link:hover::after {
  @apply w-full;
}

.nav-link.router-link-active {
  color: #d4af37;
}

.nav-link.router-link-active::after {
  @apply w-full;
}

/* Layout container */
.layout-container {
  @apply flex flex-1 relative;
}

/* Sidebar styles */
.sidebar {
  @apply fixed md:sticky top-[73px] left-0 h-[calc(100vh-73px)] z-40 transition-all duration-300;
  background: linear-gradient(180deg, #0d3e47 0%, #1a5560 100%);
  box-shadow: 2px 0 6px rgba(0, 0, 0, 0.2);
}

.sidebar-open {
  width: 300px;
  transform: translateX(0);
}

.sidebar-closed {
  @apply md:w-0 w-0;
  transform: translateX(-100%);
}

@media (min-width: 768px) {
  .sidebar-closed {
    transform: translateX(0);
    overflow: hidden;
  }
}

.sidebar-content {
  @apply p-6 overflow-y-auto h-full;
}

/* Main content */
.main-content {
  @apply flex-1 transition-all duration-300;
}

.main-content.with-sidebar {
  @apply md:ml-0;
}

@media (max-width: 767px) {
  .sidebar-open {
    width: 300px;
  }

  .main-content.with-sidebar {
    @apply ml-0;
  }
}
</style>
