<template>
    <div v-if="show" class="fixed top-6 right-6 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300">
      You need to login first.
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const show = ref(false);
  
  onMounted(() => {
    window.addEventListener('show-login-popup', () => {
      show.value = true;
      setTimeout(() => show.value = false, 3000);
    });
  });
  </script>
  