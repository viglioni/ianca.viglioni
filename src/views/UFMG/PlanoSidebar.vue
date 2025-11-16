<script setup lang="ts">
import UFMGSidebar from "./UFMGSidebar.vue";

const sections = [
  { id: "cronograma", label: "Cronograma" },
  { id: "prioridades", label: "Prioridades" },
  { id: "distribuicao", label: "Distribuição de Tempo" },
  { id: "topicos", label: "Tópicos Cobertos" },
  { id: "estrategia", label: "Estratégia de Revisão" },
  { id: "dicas", label: "Dicas para a Prova" },
];
</script>

<template>
  <UFMGSidebar :sections="sections" />
</template>
