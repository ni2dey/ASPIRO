<template>
  <div class="relative bg-darkblue text-white text-center py-20 px-6 overflow-hidden font-sans">
    <!-- Top Wavy Curve -->
    <div class="absolute top-0 left-0 w-full">
      <svg viewBox="0 0 1440 120" class="w-full h-16" preserveAspectRatio="none">
        <path
          fill="none"
          stroke="#005a9c"
          stroke-width="3"
          d="M0,60 C360,120 1080,0 1440,60 L1440,0 L0,0 Z"
        />
      </svg>
    </div>

    <!-- Text Content -->
    <div class="relative z-10">
      <h2 class="text-4xl md:text-5xl font-bold mb-4">"Take Charge Of Your Career"</h2>
      <p class="text-lg md:text-xl italic mb-4">Land The Perfect Job.</p>
      <p class="text-xl md:text-2xl italic font-bold">Define Your Own Success!</p>
    </div>

    <!-- Bottom Wavy Curve -->
    <div class="absolute bottom-0 left-0 w-full">
      <svg viewBox="0 0 1440 120" class="w-full h-16" preserveAspectRatio="none">
        <path
          fill="none"
          stroke="#005a9c"
          stroke-width="3"
          d="M0,60 C360,0 1080,120 1440,60 L1440,120 L0,120 Z"
        />
      </svg>
    </div>
  </div>
</template>

<script setup>
// No additional setup required
</script>

<style scoped>

</style>
