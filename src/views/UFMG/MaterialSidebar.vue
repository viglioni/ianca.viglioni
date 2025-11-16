<script setup lang="ts">
import UFMGSidebar from "./UFMGSidebar.vue";

const sections = [
  { id: "dias", label: "Dias de Estudo" },
  { id: "materias", label: "Matérias" },
];
</script>

<template>
  <UFMGSidebar :sections="sections" />
</template>
