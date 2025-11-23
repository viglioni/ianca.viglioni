<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  digit: string;
}>();

// 7-segment mapping: [top, top-right, bottom-right, bottom, bottom-left, top-left, middle]
const segmentMap: Record<string, boolean[]> = {
  '0': [true, true, true, true, true, true, false],
  '1': [false, true, true, false, false, false, false],
  '2': [true, true, false, true, true, false, true],
  '3': [true, true, true, true, false, false, true],
  '4': [false, true, true, false, false, true, true],
  '5': [true, false, true, true, false, true, true],
  '6': [true, false, true, true, true, true, true],
  '7': [true, true, true, false, false, false, false],
  '8': [true, true, true, true, true, true, true],
  '9': [true, true, true, true, false, true, true],
  ':': [false, false, false, false, false, false, false], // Special case for colon
};

const segments = computed(() => segmentMap[props.digit] || [false, false, false, false, false, false, false]);
</script>

<template>
  <div v-if="digit === ':'" class="colon">
    <div class="dot"></div>
    <div class="dot"></div>
  </div>
  <div v-else class="digit">
    <div :class="['segment', 'horizontal', 'top', { active: segments[0] }]"></div>
    <div :class="['segment', 'vertical', 'top-right', { active: segments[1] }]"></div>
    <div :class="['segment', 'vertical', 'bottom-right', { active: segments[2] }]"></div>
    <div :class="['segment', 'horizontal', 'bottom', { active: segments[3] }]"></div>
    <div :class="['segment', 'vertical', 'bottom-left', { active: segments[4] }]"></div>
    <div :class="['segment', 'vertical', 'top-left', { active: segments[5] }]"></div>
    <div :class="['segment', 'horizontal', 'middle', { active: segments[6] }]"></div>
  </div>
</template>

<style scoped>
.digit {
  position: relative;
  width: 12px;
  height: 22px;
  display: inline-block;
}

.colon {
  position: relative;
  width: 5px;
  height: 22px;
  display: inline-flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 3px;
}

.dot {
  width: 2px;
  height: 2px;
  background: #ff0000;
  box-shadow: 0 0 2px rgba(255, 0, 0, 0.8);
}

.segment {
  position: absolute;
  background: #2a0000;
  transition: background 0.1s;
}

.segment.active {
  background: #ff0000;
  box-shadow: 0 0 2px rgba(255, 0, 0, 0.8);
}

.segment.horizontal {
  height: 2px;
  width: 9px;
  left: 1.5px;
}

.segment.vertical {
  width: 2px;
  height: 8.5px;
}

.segment.top {
  top: 0;
}

.segment.top-right {
  top: 1px;
  right: 0;
}

.segment.top-left {
  top: 1px;
  left: 0;
}

.segment.middle {
  top: 50%;
  transform: translateY(-50%);
}

.segment.bottom {
  bottom: 0;
}

.segment.bottom-right {
  bottom: 1px;
  right: 0;
}

.segment.bottom-left {
  bottom: 1px;
  left: 0;
}
</style>
