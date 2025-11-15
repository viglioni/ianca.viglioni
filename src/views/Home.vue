<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="home-container">
    <div class="home-overlay">
      <h1 class="home-title">Mundinho Ianca Viglioni</h1>
      <div class="links-container">
        <div class="links-wrapper">
          <RouterLink to="/ufmg" class="nav-link group">
            <span class="nav-link-text"> UFMG Seriado </span>
            <div class="nav-link-hover"></div>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-container {
  @apply min-h-screen bg-repeat;
  background-image: url("/home.bg.png");
}

.home-overlay {
  @apply min-h-screen bg-black/40 flex flex-col p-8;
}

.home-title {
  @apply text-6xl md:text-7xl lg:text-8xl font-black text-white pt-12 pb-8 text-center drop-shadow-2xl tracking-tight;
  font-family: "Honk", cursive;
}

.links-container {
  @apply flex-1 flex items-center justify-center;
}

.links-wrapper {
  @apply flex flex-col gap-6;
}

.nav-link {
  @apply relative px-12 py-6 bg-cyan-400 text-black border-4 border-black overflow-hidden;
  box-shadow:
    8px 8px 0 0 #000,
    8px 8px 0 4px #ff00ff,
    -4px -4px 0 0 #ffff00 inset,
    4px 4px 0 0 #00ffff inset;
  transition:
    transform 0.1s,
    box-shadow 0.1s;
  image-rendering: pixelated;
  text-decoration: none;
  display: block;
}

.nav-link:hover {
  transform: translate(4px, 4px);
  box-shadow:
    4px 4px 0 0 #000,
    4px 4px 0 4px #00ff00,
    -4px -4px 0 0 #ffff00 inset,
    4px 4px 0 0 #ff00ff inset;
}

.nav-link:active {
  transform: translate(8px, 8px);
  box-shadow:
    0px 0px 0 0 #000,
    0px 0px 0 4px #ff0000,
    -2px -2px 0 0 #ffff00 inset,
    2px 2px 0 0 #00ffff inset;
}

.nav-link-text {
  @apply relative z-10 text-4xl font-bold uppercase tracking-wider;
  font-family: "Alumni Sans Pinstripe", sans-serif;
  text-shadow: 2px 2px 0 #000;
}

.nav-link-hover {
  display: none;
}
</style>
