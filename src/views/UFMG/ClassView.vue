<script setup lang="ts">
import { defineAsyncComponent, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import studySchedule from "@/data/study-schedule.json";

const route = useRoute();
const router = useRouter();
const code = route.params.code as string;
const data = studySchedule as any;

// Check if code exists
if (!data.codes || !data.codes[code]) {
  router.push("/ufmg/material");
}

// Load the class component dynamically
const ClassComponent = defineAsyncComponent({
  loader: () => import(`./classes/${code}.vue`),
  onError() {
    router.push("/ufmg/material");
  },
});
</script>

<template>
  <ClassComponent v-if="data.codes && data.codes[code]" />
</template>
