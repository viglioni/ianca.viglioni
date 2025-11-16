<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="ufmg-container">
    <div class="header-section"></div>
    <div class="ufmg-overlay">
      <div class="content-wrapper">
        <div class="title-section">
          <h1 class="main-title">UFMG Seriado 2025</h1>
          <h2 class="subtitle">Primeiro Ano EM</h2>
        </div>

        <div class="links-section">
          <RouterLink to="/ufmg/plano" class="ufmg-link">
            <span class="link-text">Plano de Estudo</span>
            <svg
              class="link-arrow"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </RouterLink>

          <RouterLink to="/ufmg/material" class="ufmg-link">
            <span class="link-text">Material de Estudo</span>
            <svg
              class="link-arrow"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 5l7 7-7 7"
              />
            </svg>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.ufmg-container {
  @apply flex flex-col;
  @apply min-h-screen flex items-center justify-start w-screen;
  background:
    linear-gradient(135deg, #0d3e47 0%, #1a5560 100%), url("/ufmg.bg");
  background-size: cover, contain;
  background-position: center, center;
  background-repeat: no-repeat;
}

.content-wrapper {
  @apply max-w-4xl w-full flex flex-col gap-20;
}

.title-section {
  @apply text-center;
}

.header-section {
  @apply text-center mb-16 w-screen py-44 border-b-white border-b-2;
  @apply bg-no-repeat bg-center;
  background-color: #0a3d3e;
  background-image: url("/ufmg.bg");
  background-size: cover;
}

.main-title {
  @apply text-6xl md:text-7xl lg:text-8xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #f5f1e8;
  text-shadow:
    0 2px 4px rgba(0, 0, 0, 0.3),
    0 0 20px rgba(212, 175, 55, 0.2);
  letter-spacing: 0.02em;
}

.subtitle {
  @apply text-2xl md:text-3xl lg:text-4xl font-light;
  font-family: "Merriweather", serif;
  color: #d4af37;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
  letter-spacing: 0.05em;
}

.links-section {
  @apply flex flex-col items-center gap-6;
}

.ufmg-link {
  @apply relative flex items-center gap-3 px-8 py-4 rounded-lg transition-all duration-300;
  font-family: "Merriweather", serif;
  background: rgba(212, 175, 55, 0.1);
  border: 2px solid #d4af37;
  text-decoration: none;
  overflow: hidden;
}

.ufmg-link::before {
  content: "";
  @apply absolute inset-0 transition-transform duration-300;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(212, 175, 55, 0.2),
    transparent
  );
  transform: translateX(-100%);
}

.ufmg-link:hover::before {
  transform: translateX(100%);
}

.ufmg-link:hover {
  background: rgba(212, 175, 55, 0.2);
  border-color: #f5f1e8;
  transform: translateY(-2px);
  box-shadow:
    0 4px 12px rgba(0, 0, 0, 0.3),
    0 0 20px rgba(212, 175, 55, 0.3);
}

.link-text {
  @apply text-xl md:text-2xl font-semibold;
  color: #f5f1e8;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.link-arrow {
  @apply w-6 h-6 transition-transform duration-300;
  color: #d4af37;
}

.ufmg-link:hover .link-arrow {
  transform: translateX(4px);
}
</style>
