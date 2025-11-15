<template>
  <nav class="sidebar-nav">
    <h3 class="sidebar-title">Conteúdo</h3>
    <ul class="sidebar-menu">
      <li><a href="#intro" class="sidebar-link">Introdução</a></li>
      <li><a href="#materias" class="sidebar-link">Matérias</a></li>
      <li><a href="#cronograma" class="sidebar-link">Cronograma</a></li>
      <li><a href="#recursos" class="sidebar-link">Recursos</a></li>
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
</style>
