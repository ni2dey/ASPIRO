<template>
  <div class="relative min-h-screen flex flex-col">
    <!-- Background Overlay -->
    <div class="fixed inset-0 bg-background bg-cover bg-center bg-fixed z-0">
      <div class="absolute inset-0 bg-white bg-opacity-90"></div>
    </div>

    <div class="relative z-10 flex flex-col flex-grow">
      <NavBar />

      <!-- Loader -->
      <div v-if="loading" class="flex flex-col items-center justify-center min-h-[400px] space-y-6 text-center">
        <div class="loader"></div>
          <p class="text-xl font-semibold text-gray-800">
            Please wait a moment, analyzing your skills...
          </p>
      </div>

      <!-- Results -->
      <div v-else class="flex-grow flex flex-col items-center justify-center px-4 py-20 pb-50">
        <!-- Show recommendations if available -->
        <template v-if="recommendations.length">
          <h2 class="text-4xl font-extrabold mb-10 text-word">Here's What Suits You Best 👇</h2>
          <transition-group
            name="fade-slide"
            tag="ul"
            class="space-y-6 w-full max-w-3xl"
          >
            <li
              v-for="(item, index) in recommendations"
              :key="item + index"
              class="recommendation-card"
            >
              <span class="text-2xl font-semibold text-darkblue">✅ {{ item }}</span>
              <a
                :href="getCourseUrl(item)"
                target="_blank"
                class="explore-link text-blue hover:text-darkblue hover:underline"
              >
                Explore Courses →
              </a>
            </li>
          </transition-group>

          <!-- Try Again Button -->
          <div class="mt-12">
            <button
              @click="tryAgain"
              class="px-8 py-3 bg-darkblue text-white text-lg rounded-full hover:bg-blue transition duration-200"
            >
              Try Again
            </button>
          </div>
        </template>

        <!-- Show fallback if no recommendations -->
        <template v-else>
          <div class="text-center bg-white bg-opacity-90 p-10 rounded-2xl shadow-md max-w-xl">
            <h2 class="text-3xl font-bold text-gray-800 mb-4">No Courses Found 😕</h2>
            <p class="text-lg font-semibold text-gray-600 mb-8">
              We couldn't find any course recommendations based on your skills.
              You can try again with different skills.
            </p>
            <button
              @click="tryAgain"
              class="px-8 py-3 bg-darkblue text-white text-lg rounded-lg hover:bg-blue transition duration-200"
            >
              Try Again
            </button>
          </div>
        </template>
      </div>

      <Footer class="mt-16 w-full relative z-18" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import NavBar from '../components/Core/NavBar.vue';
import Footer from '../components/Core/Footer.vue';

const loading = ref(true);
const recommendations = ref([]);
const route = useRoute();
const router = useRouter();

const tryAgain = () => {
  router.push('/addskill');
};

onMounted(async () => {
  const skillsQuery = route.query.skills || '';
  const skillsArray = skillsQuery.split(',').map(s => s.trim());

  try {
    const response = await fetch('http://127.0.0.1:5000/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ skills: skillsArray }),
    });

    const result = await response.json();
    recommendations.value = Array.isArray(result) ? result : [];
  } catch (err) {
    recommendations.value = [];
    console.error('Error fetching recommendations:', err);
  }

  // Force 5-second loader
  setTimeout(() => {
    loading.value = false;
  }, 5000);
});

function formatDomain(name) {
  return name.toLowerCase().replace(/\s+/g, '-');
}

function getCourseUrl(domain) {
  return `http://127.0.0.1:5000/api/course/${formatDomain(domain)}`;
}
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
.recommendation-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: white;
  background-opacity: 90%;
  padding: 1.5rem;
  border-radius: 1.5rem;
  border: 1px solid #e5e7eb;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.recommendation-card:hover {
  transform: translateY(-4px) scale(1.02);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

/* Transition Group Animations */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.6s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(30px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Add fade-slide-in animation for heading */
@keyframes fade-slide-in {
  0% {
    opacity: 0;
    transform: translateY(-20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-slide-in {
  animation: fade-slide-in 0.8s ease-out;
}
</style>