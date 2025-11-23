const fs = require('fs');
const path = require('path');

const jsonPath = path.join(__dirname, '../src/data/study-schedule.json');
const classesDir = path.join(__dirname, '../src/views/UFMG/classes');
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));

// Ensure classes directory exists
if (!fs.existsSync(classesDir)) {
  fs.mkdirSync(classesDir, { recursive: true });
}

// Template for class component
const createTemplate = (code, codeData) => {
  return `<script setup lang="ts">
import { ref } from "vue";

const code = "${code}";
const title = "${codeData.title}";
const subject = "${codeData.subject}";
const themes = ${JSON.stringify(codeData.themes)};
const dates = ${JSON.stringify(codeData.dates)};
</script>

<template>
  <div class="class-container">
    <div class="class-header">
      <h1 class="class-title">{{ title }}</h1>
      <div class="class-meta">
        <span class="class-code">{{ code }}</span>
        <span class="class-subject">{{ subject }}</span>
      </div>
    </div>

    <div class="class-content">
      <section class="class-section">
        <h2>Temas</h2>
        <ul>
          <li v-for="theme in themes" :key="theme">{{ theme }}</li>
        </ul>
      </section>

      <section class="class-section">
        <h2>Conteúdo</h2>
        <p>Conteúdo da aula será adicionado aqui...</p>
      </section>
    </div>
  </div>
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Text:wght@400;600;700&family=Merriweather:wght@300;400;700&display=swap");

.class-container {
  @apply min-h-screen bg-repeat p-8;
  background-image: url("/ufmg.plano.bg.jpg");
  background-color: #f5f1e8;
}

.class-header {
  @apply mb-8 text-center;
}

.class-title {
  @apply text-4xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.class-meta {
  @apply flex gap-4 justify-center;
}

.class-code,
.class-subject {
  @apply px-4 py-2 rounded font-bold;
  font-family: "Merriweather", serif;
  background: #1a5560;
  color: #f5f1e8;
}

.class-content {
  @apply max-w-4xl mx-auto bg-white/80 backdrop-blur-sm rounded-lg p-8 shadow-lg;
}

.class-section {
  @apply mb-8;
}

.class-section h2 {
  @apply text-2xl font-bold mb-4;
  font-family: "Crimson Text", serif;
  color: #0d3e47;
}

.class-section ul {
  @apply list-disc list-inside;
  font-family: "Merriweather", serif;
}

.class-section li {
  @apply mb-2;
  color: #2d4f56;
}

.class-section p {
  font-family: "Merriweather", serif;
  color: #2d4f56;
  line-height: 1.8;
}
</style>
`;
};

// Create a component for each code
let count = 0;
Object.keys(data.codes).forEach(code => {
  const codeData = data.codes[code];
  const filename = `${code}.vue`;
  const filepath = path.join(classesDir, filename);

  const content = createTemplate(code, codeData);
  fs.writeFileSync(filepath, content);
  count++;
});

console.log(`Created ${count} class components in src/views/UFMG/classes/`);
