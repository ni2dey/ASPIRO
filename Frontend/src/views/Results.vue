<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Background -->
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-white bg-opacity-90"></div>
    </div>

    <!-- Main Content -->
    <div class="relative z-10 flex flex-col min-h-screen">
      <NavBar class="z-20" />

      <!-- Content Area -->
      <div class="flex-grow flex items-center justify-center px-4 py-12">
        <div class="w-full max-w-3xl min-h-[400px] flex items-center justify-center">
          <!-- Loading Screen -->
          <div v-if="loading" class="flex flex-col items-center justify-center min-h-[400px] space-y-6 text-center">
            <div class="loader"></div>
              <p class="text-xl font-semibold text-gray-800">
                Please wait a moment, analyzing your answers...
              </p>
          </div>

          <!-- Results Section -->
          <div
            v-else
            class="bg-white rounded-xl shadow-2xl w-full p-10 text-center space-y-6 animate-fadeUp"
          >
            <h2 class="text-3xl font-bold text-word">🧭 Your career compass points here!</h2>

            <p class="text-lg text-gray-700">
              <span v-if="maxType === 'A'">
                You're all set to jump into the working world! Time to put your
                skills into action and gain some real-world experience.
              </span>
              <span v-else-if="maxType === 'B'">
                You've got a strong academic streak! Consider diving deeper
                with an M.Tech or exploring the business side with an MBA.
              </span>
              <span v-else>
                Looks like you're still exploring — and that's totally okay!
                Take your time to learn, try different things, and discover what
                clicks for you.
              </span>
            </p>

            <!-- Buttons -->
            <div class="flex flex-col sm:flex-row justify-center gap-4 pt-4">
              <router-link to="/addskill">
                <button
                  v-if="maxType === 'A'"
                  class="px-6 py-3 bg-green hover:bg-darkgreen text-white font-bold rounded-lg transition"
                >
                  Add Skills
                </button>
              </router-link>
              <router-link to="/next">
                <button
                  class="px-6 py-3 bg-blue hover:bg-darkblue text-white font-bold rounded-lg transition"
                >
                  Retake Quiz
                </button>
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <Footer class="z-20 mt-auto" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import NavBar from '../components/Core/NavBar.vue';
import Footer from '../components/Core/Footer.vue';

const router = useRouter();
const route = useRoute();

const loading = ref(true);
const resultText = ref('');
const maxType = ref('');

const calculateResult = () => {
  const responses = JSON.parse(route.query.responses || '[]');
  const counts = { A: 0, B: 0, C: 0 };
  responses.forEach((type) => {
    if (['A', 'B', 'C'].includes(type)) {
      counts[type]++;
    }
  });

  maxType.value = Object.entries(counts).sort((a, b) => b[1] - a[1])[0][0];
};

onMounted(() => {
  setTimeout(() => {
    loading.value = false;
    calculateResult();
  }, 5000); // 5 seconds loader
});
</script>

<style scoped>
.loader {
  width: 40px;
  aspect-ratio: 1.154;
  --_g: no-repeat radial-gradient(farthest-side,#1e3a8a 90%,#0000);
  background: 
    var(--_g) 50% 0,
    var(--_g) 0 100%,
    var(--_g) 100% 100%;
  background-size: 35% calc(35% * 1.154);
  animation: l16 1s infinite;
}

@keyframes l16 {
  50%, 100% {
    background-position: 100% 100%, 50% 0, 0 100%;
  }
}
@keyframes fadeUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeUp {
  animation: fadeUp 0.8s ease-out;
}
</style>
